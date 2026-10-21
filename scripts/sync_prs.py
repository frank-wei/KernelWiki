#!/usr/bin/env python3
"""Search a merge-date window for new upstream PRs and add them to the wiki.

One command runs the whole intake path that otherwise spans several scripts:

  1. Search each tracked repo for PRs merged inside ``--since..--until``
     (per ledger keyword, or every merged PR with ``--no-keywords``). Windows
     that hit GitHub's 1000-result search cap are bisected by date.
  2. For every PR not already in ``candidates/<repo>.yaml``, fetch the
     authoritative PR object and changed files, apply the shared
     ``pr_policy.classify_scope`` rule, and append an include/exclude/defer row.
  3. Generate ``sources/prs/<repo>/PR-<N>.md`` for each new include with the
     same renderer as ``scripts/generate-pr-pages.py``.
  4. Keep the derived records in sync: architecture receipt rows,
     ``data/refresh-search-results.yaml``, ledger ``searched_at`` plus
     ``data/refresh-cutoff.yaml`` (full-repo syncs only), PR-page counts in
     ``references/primer.md``, ``SKILL.md`` and ``references/schema.md``,
     and the generated ``queries/*.md`` indices.

Existing ledger rows and pages are never rewritten. The script needs an
authenticated ``gh`` CLI with GitHub API access.

With ``--from-prefilter`` the search step is replaced by the candidate list
from scripts/local_prefilter.py (full-recall offline scan of a local clone), so
GitHub is only queried for PRs that already passed the scope policy locally.

Usage:
  python3 scripts/sync_prs.py --from-prefilter .worklog/prefilter/vllm_2026-05-21_2026-10-20.json --max-new 20 --validate
  python3 scripts/sync_prs.py --since 2026-05-21 --until 2026-10-20 --dry-run
  python3 scripts/sync_prs.py --since 2026-05-21 --until 2026-10-20 --repos vllm,sglang
  python3 scripts/sync_prs.py --since 2026-05-21 --no-keywords --repos deepgemm --validate
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import time
import urllib.parse
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _yaml_compat import yaml  # noqa: E402
from pr_policy import classify_scope  # noqa: E402
import refresh_candidate_ledger as refresh  # noqa: E402
from local_prefilter import add_complete_file_receipts  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
CANDIDATES_DIR = REPO_ROOT / "candidates"
PRS_DIR = REPO_ROOT / "sources" / "prs"
RECEIPT_PATH = REPO_ROOT / "data" / "pr-architecture-evidence.json"
PRIMER_PATH = REPO_ROOT / "references" / "primer.md"
SKILL_PATH = REPO_ROOT / "SKILL.md"
SCHEMA_DOC_PATH = REPO_ROOT / "references" / "schema.md"

SEARCH_RESULT_CAP = 1000
SEARCH_SLEEP_SECONDS = 2.5  # GitHub search API allows 30 requests/minute.
EXCLUDE_ROW_PATH_LIMIT = 50


def _load_script(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GEN = _load_script("generate_pr_pages", "generate-pr-pages.py")
VALIDATE = _load_script("kernelwiki_validate", "validate.py")


def dump_yaml(data):
    """Serialize ledgers exactly like refresh_candidate_ledger.py does."""
    return yaml.safe_dump(data, sort_keys=False, default_flow_style=False, width=200, allow_unicode=True)


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

def gh_search_window(repo_full, query, start, end, retries=3):
    """Return up to SEARCH_RESULT_CAP merged PRs in [start, end] matching query."""
    cmd = [
        "gh", "search", "prs",
        "--repo", repo_full,
        "--merged",
        "--merged-at", f"{start.isoformat()}..{end.isoformat()}",
        "--limit", str(SEARCH_RESULT_CAP),
        "--json", "number,title,closedAt",
    ]
    if query:
        cmd.append(query)
    for attempt in range(retries):
        try:
            out = subprocess.check_output(cmd, text=True, timeout=120)
            time.sleep(SEARCH_SLEEP_SECONDS)
            return json.loads(out)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError) as e:
            wait = SEARCH_SLEEP_SECONDS * (4 ** (attempt + 1))
            print(f"    WARN: search failed ({e}); retrying in {wait:.0f}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"gh search failed for {repo_full} query={query!r} window={start}..{end}")


def search_range(repo_full, query, start, end, search_fn=gh_search_window):
    """Search [start, end], bisecting by date whenever the result cap is hit."""
    rows = search_fn(repo_full, query, start, end)
    if len(rows) < SEARCH_RESULT_CAP:
        return rows
    if start >= end:
        print(f"    WARN: {repo_full} {query!r} has >= {SEARCH_RESULT_CAP} merges on {start}; "
              "results for that day are truncated", file=sys.stderr)
        return rows
    mid = start + (end - start) // 2
    return (search_range(repo_full, query, start, mid, search_fn)
            + search_range(repo_full, query, mid + timedelta(days=1), end, search_fn))


def search_repo(repo_full, keywords, since, until, search_fn=gh_search_window):
    """Union per-keyword results (or all merged PRs when keywords is empty)."""
    seen = {}
    for query in keywords or [None]:
        for row in search_range(repo_full, query, since, until, search_fn):
            seen.setdefault(row["number"], {
                "number": row["number"],
                "title": row.get("title", ""),
                "closedAt": (row.get("closedAt") or "")[:10],
            })
    return [seen[n] for n in sorted(seen)]


# ---------------------------------------------------------------------------
# Classification and page generation
# ---------------------------------------------------------------------------

class PRHeadFileReader:
    """Read complete PR-head files through the GitHub contents API.

    Supplies the immutable complete-file receipts that pr_policy requires for
    ``.cu`` and weak-tuning ``.py`` hunks that are inconclusive on their own.
    """

    def __init__(self, repo_full):
        self.repo_full = repo_full

    def read(self, sha, path):
        try:
            return subprocess.check_output(
                ["gh", "api", "-H", "Accept: application/vnd.github.raw",
                 f"repos/{self.repo_full}/contents/{urllib.parse.quote(path)}?ref={sha}"],
                timeout=60,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return None


RATE_LIMIT_FLOOR = 100  # core requests kept in reserve before pausing


def wait_for_core_rate_limit():
    """Sleep until the GitHub core quota resets when it is nearly exhausted.

    ``rate_limit`` itself does not count against the quota. Without this, a
    long run would turn every request after exhaustion into a ``defer`` row.
    """
    try:
        core = json.loads(subprocess.check_output(["gh", "api", "rate_limit"], text=True, timeout=60))
        core = core["resources"]["core"]
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError, KeyError):
        return
    if core["remaining"] >= RATE_LIMIT_FLOOR:
        return
    wait = max(0, core["reset"] - int(time.time())) + 5
    print(f"    rate limit: {core['remaining']} core requests left; sleeping {wait}s until reset")
    time.sleep(wait)


def fetch_evidence_with_receipts(repo_full, number):
    """Fetch PR evidence, then resolve inconclusive hunks from PR-head files."""
    wait_for_core_rate_limit()
    evidence = refresh.fetch_pr_evidence(repo_full, number)
    if evidence is None:
        return None
    pr, files = evidence
    head_sha = (pr.get("head") or {}).get("sha")
    if head_sha:
        add_complete_file_receipts(files, head_sha, PRHeadFileReader(repo_full))
    return pr, files


def build_ledger_row(hit, evidence):
    """Apply the shared scope policy to one search hit.

    Returns (ledger_row, scope_or_None). ``evidence`` is ``(pr, files)`` or
    None when GitHub could not supply complete evidence.
    """
    row = {
        "number": hit["number"],
        "title": hit.get("title", ""),
        "date": hit.get("closedAt", ""),
    }
    if evidence is None:
        row.update({
            "decision": "defer",
            "reason": "authoritative PR evidence unavailable; needs-triage",
            "files_changed": [],
        })
        return row, None
    pr, files = evidence
    if pr.get("title"):
        row["title"] = pr["title"]
    if not pr.get("merged_at"):
        row.update({
            "decision": "exclude",
            "reason": "remove: PR is not merged",
            "files_changed": [],
        })
        return row, None
    scope = classify_scope(pr.get("title") or "", pr.get("body") or "", files)
    filenames = [item.get("filename") for item in files if item.get("filename")]
    row.update({
        "decision": "include" if scope.retain else "exclude",
        "reason": scope.reason,
        "files_changed": list(scope.evidence_paths) if scope.retain else filenames[:EXCLUDE_ROW_PATH_LIMIT],
        "files_reviewed_count": len(filenames),
        "scope_disposition": scope.disposition,
    })
    return row, scope


def page_path_for(repo_full, number):
    return PRS_DIR / repo_full.split("/")[1] / f"PR-{number}.md"


def write_page(repo_full, evidence, scope, captured_at):
    """Render and write one PR page; returns its path."""
    pr, files = evidence
    path = page_path_for(repo_full, pr["number"])
    if path.exists():
        raise FileExistsError(f"{path.relative_to(REPO_ROOT)} already exists")
    content = GEN.generate_page(repo_full, pr, files, scope.reason, captured_at)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def recount_ledger(data):
    decisions = [str(r.get("decision", "")).lower() for r in data["prs"]]
    data["included"] = decisions.count("include")
    data["excluded"] = decisions.count("exclude")
    data["deferred"] = decisions.count("defer")
    data["total_candidates"] = data["included"] + data["excluded"] + data["deferred"]


def sync_repo(slug, args, captured_at, evidence_fn=fetch_evidence_with_receipts,
              search_fn=gh_search_window):
    """Search, classify, and generate pages for one repo. Returns a summary dict."""
    ledger_path = CANDIDATES_DIR / f"{slug}.yaml"
    data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    repo_full = data.get("repo") or refresh.REPO_SLUG_TO_FULL[slug]
    report = args.prefilter.get(slug)
    if report is not None:
        print(f"\n{repo_full}: {len(report['candidates'])} local-prefilter candidate(s) "
              f"for {report['since']}..{report['until']} (clone HEAD {report['clone_head'][:12]})")
        hits = [
            {"number": c["number"], "title": c["title"], "closedAt": c["date"]}
            for c in sorted(report["candidates"], key=lambda c: c["number"])
        ]
    else:
        keywords = [] if args.no_keywords else (args.keywords or data.get("keywords_used") or [])
        label = "all merged PRs" if not keywords else f"{len(keywords)} keyword(s)"
        print(f"\n{repo_full}: searching {args.since}..{args.until} with {label}")
        hits = search_repo(repo_full, keywords, args.since, args.until, search_fn)
    if args.retry_deferred:
        rows = data.get("prs") or []
        hit_numbers = {hit["number"] for hit in hits}
        retry = [r for r in rows if isinstance(r, dict) and str(r.get("decision")) == "defer"
                 and "needs-triage" in str(r.get("reason", "")) and r.get("number") in hit_numbers]
        if retry:
            data["prs"] = [r for r in rows if r not in retry]
            print(f"  retrying {len(retry)} deferred needs-triage row(s)")
    known = {row.get("number") for row in data.get("prs") or [] if isinstance(row, dict)}
    new_hits = [hit for hit in hits if hit["number"] not in known]
    if args.max_new is not None:
        new_hits = new_hits[:args.max_new]
    print(f"  {len(hits)} hit(s), {len(new_hits)} not yet in {ledger_path.relative_to(REPO_ROOT)}")

    summary = {"slug": slug, "repo": repo_full, "hits": len(hits), "new": len(new_hits),
               "include": 0, "exclude": 0, "defer": 0, "pages": [], "seen": []}
    if args.dry_run:
        for hit in new_hits[:20]:
            print(f"    #{hit['number']} {hit['closedAt']} {hit['title']}")
        if len(new_hits) > 20:
            print(f"    ... {len(new_hits) - 20} more")
        return summary

    new_rows = []
    for hit in new_hits:
        evidence = evidence_fn(repo_full, hit["number"])
        row, scope = build_ledger_row(hit, evidence)
        if row["decision"] == "include":
            try:
                path = write_page(repo_full, evidence, scope, captured_at)
                summary["pages"].append(path)
            except Exception as e:  # keep the ledger honest instead of aborting the run
                row["decision"] = "defer"
                row["reason"] = f"page generation failed: {e}; needs-triage"
        summary[row["decision"]] += 1
        new_rows.append(row)
        print(f"    #{row['number']}: {row['decision']} - {row['reason'][:100]}")

    if new_rows:
        data["prs"] = (data.get("prs") or []) + new_rows
        recount_ledger(data)
        ledger_path.write_text(dump_yaml(data), encoding="utf-8")
    summary["seen"] = [hit for hit in hits if hit["number"] in known or
                       hit["number"] in {r["number"] for r in new_rows}]
    return summary


# ---------------------------------------------------------------------------
# Derived records
# ---------------------------------------------------------------------------

def update_architecture_receipt(page_paths):
    """Add frozen-evidence receipt rows for newly generated pages."""
    if not page_paths:
        return
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    for path in page_paths:
        rel = path.relative_to(PRS_DIR).as_posix()
        receipt["rows"][rel] = VALIDATE.architecture_receipt_record(VALIDATE.extract_frontmatter(path))
    RECEIPT_PATH.write_text(
        json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8"
    )


def update_search_results(summaries, until, today):
    """Record searched PR numbers so the AC-5 subset check covers this sync.

    Blocks for repos that were not searched in this run are left untouched.
    """
    path = refresh.REFRESH_RESULTS_PATH
    existing = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.is_file() else {}
    blocks = {row["repo_slug"]: row for row in existing.get("repos", []) or []}
    for summary in summaries:
        old = blocks.get(summary["slug"], {})
        numbers = set(old.get("pr_numbers_seen", []) or []) | {h["number"] for h in summary["seen"]}
        last_dates = [str(old.get("last_pr_date_seen") or "")] + [h["closedAt"] for h in summary["seen"]]
        blocks[summary["slug"]] = {
            "repo_slug": summary["slug"],
            "searched_at": today,
            "cutoff_date_used": until.isoformat(),
            "pr_numbers_seen": sorted(numbers),
            "last_pr_date_seen": max(last_dates),
        }
    # The top-level date mirrors data/refresh-cutoff.yaml, which only advances
    # on a full-repo sync (see update_refresh_cutoff).
    cutoff = yaml.safe_load(refresh.REFRESH_CUTOFF_PATH.read_text(encoding="utf-8"))["cutoff_date"]
    payload = {
        "cutoff_date": str(cutoff),
        "repos": [blocks[slug] for slug in sorted(blocks)],
    }
    header = (
        "## AC-5 refresh search-results record. Schema: data/schemas.yaml ::\n"
        "## refresh-search-results. Generated by\n"
        "## scripts/refresh_candidate_ledger.py. Byte-stable for identical\n"
        "## query inputs (pr_numbers_seen sorted ascending; repos keyed by\n"
        "## repo_slug ascending).\n"
    )
    path.write_text(header + dump_yaml(payload), encoding="utf-8")


def update_refresh_cutoff(synced_slugs, until):
    """Advance searched_at/cutoff only when every ledger was searched."""
    all_slugs = {p.stem for p in CANDIDATES_DIR.glob("*.yaml")}
    current = yaml.safe_load(refresh.REFRESH_CUTOFF_PATH.read_text(encoding="utf-8")) or {}
    current_cutoff = date.fromisoformat(str(current.get("cutoff_date")))
    if set(synced_slugs) != all_slugs:
        print(f"\nNote: not every ledger was synced; ledger searched_at and data/refresh-cutoff.yaml "
              f"stay at {current_cutoff} (they advance only when all {len(all_slugs)} repos are synced).")
        return
    if until <= current_cutoff:
        return
    for slug in sorted(all_slugs):
        ledger_path = CANDIDATES_DIR / f"{slug}.yaml"
        data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
        data["searched_at"] = until.isoformat()
        ledger_path.write_text(dump_yaml(data), encoding="utf-8")
    refresh.write_cutoff(until)
    print(f"\nAdvanced all ledger searched_at and data/refresh-cutoff.yaml to {until}")


def page_counts():
    """Return {repo_dir_name: page_count} and the overall status distribution."""
    counts = {}
    statuses = []
    for repo_dir in sorted(p for p in PRS_DIR.iterdir() if p.is_dir()):
        pages = sorted(repo_dir.glob("PR-*.md"))
        counts[repo_dir.name] = len(pages)
        statuses.extend(VALIDATE.extract_frontmatter(p).get("status") for p in pages)
    return counts, statuses.count("merged"), statuses.count("closed"), len(statuses)


def sync_count_text(primer, skill, schema_doc, counts, merged, closed, total, ledgers):
    """Rewrite the hard-coded PR-page counts in the shipped docs."""
    def primer_row(match):
        name = match.group(1).split("/")[1]
        return f"| {match.group(1)} | {counts.get(name, 0)} |"

    primer = re.sub(r"^\| ([\w.-]+/[\w.-]+) \| \d+ \|", primer_row, primer, flags=re.MULTILINE)
    listed = set(re.findall(r"^\| [\w.-]+/([\w.-]+) \| \d+ \|", primer, flags=re.MULTILINE))
    missing = [(repo, slug) for slug, repo in sorted(ledgers.items())
               if counts.get(repo.split("/")[1]) and repo.split("/")[1] not in listed]
    if missing:
        rows = re.findall(r"^\| [\w.-]+/[\w.-]+ \| \d+ \|.*$", primer, flags=re.MULTILINE)
        anchor = rows[-1]
        extra = "".join(
            f"\n| {repo} | {counts[repo.split('/')[1]]} | `candidates/{slug}.yaml` |" for repo, slug in missing
        )
        primer = primer.replace(anchor, anchor + extra, 1)

    skill = re.sub(
        r"current distribution: \d+ merged, \d+ closed without merge",
        f"current distribution: {merged} merged, {closed} closed without merge",
        skill,
    )
    closed_words = {0: "none", 1: "one", 2: "two", 3: "three"}
    closed_text = closed_words.get(closed, str(closed))
    schema_doc = re.sub(
        r"\(\d+ of \d+ are `merged`; \w+ (?:is|are) `closed` without merge\)",
        f"({merged} of {total} are `merged`; {closed_text} {'is' if closed == 1 else 'are'} `closed` without merge)",
        schema_doc,
    )
    return primer, skill, schema_doc


def update_count_docs():
    counts, merged, closed, total = page_counts()
    ledgers = {}
    for p in CANDIDATES_DIR.glob("*.yaml"):
        repo = (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("repo")
        if repo:
            ledgers[p.stem] = repo
    texts = [path.read_text(encoding="utf-8") for path in (PRIMER_PATH, SKILL_PATH, SCHEMA_DOC_PATH)]
    updated = sync_count_text(*texts, counts, merged, closed, total, ledgers)
    for path, before, after in zip((PRIMER_PATH, SKILL_PATH, SCHEMA_DOC_PATH), texts, updated):
        if before != after:
            path.write_text(after, encoding="utf-8")
            print(f"Updated counts in {path.relative_to(REPO_ROOT)}")
    print(f"PR pages: {total} ({merged} merged, {closed} closed)")


def run_script(*argv):
    print(f"\n$ python3 {' '.join(argv)}")
    return subprocess.run([sys.executable, *argv], cwd=REPO_ROOT).returncode


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--since", default=None, type=date.fromisoformat,
                        help="First merge date to search (YYYY-MM-DD, inclusive; required without --from-prefilter).")
    parser.add_argument("--until", default=date.today(), type=date.fromisoformat,
                        help="Last merge date to search (YYYY-MM-DD, inclusive; default: today).")
    parser.add_argument("--repos", default=None,
                        help="Comma-separated ledger slugs, e.g. vllm,sglang (default: every candidates/*.yaml).")
    parser.add_argument("--keywords", default=None, type=lambda s: [k.strip() for k in s.split(",") if k.strip()],
                        help="Comma-separated search terms overriding each ledger's keywords_used.")
    parser.add_argument("--no-keywords", action="store_true",
                        help="Classify every merged PR in the window (full recall, many more API calls).")
    parser.add_argument("--max-new", type=int, default=None,
                        help="Classify at most N new PRs per repo (lowest numbers first).")
    parser.add_argument("--captured-at", default=date.today().isoformat(),
                        help="captured_at for new pages (default: today).")
    parser.add_argument("--from-prefilter", action="append", default=[], metavar="REPORT",
                        help="Use a scripts/local_prefilter.py report instead of searching (repeatable, one per repo).")
    parser.add_argument("--retry-deferred", action="store_true",
                        help="Re-fetch ledger rows previously deferred as needs-triage (e.g. after a network failure).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Search only; list new PRs without fetching evidence or writing files.")
    parser.add_argument("--validate", action="store_true",
                        help="Run scripts/validate.py after syncing.")
    args = parser.parse_args(argv)
    if args.since is None and not args.from_prefilter:
        parser.error("--since is required unless --from-prefilter is given")
    if args.since and args.since > args.until:
        parser.error("--since must not be after --until")
    date.fromisoformat(args.captured_at)
    return args


def load_prefilter_reports(paths):
    """Map ledger slug -> local_prefilter report, refusing stale policy digests."""
    repo_to_slug = {
        (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("repo"): p.stem
        for p in CANDIDATES_DIR.glob("*.yaml")
    }
    policy_sha = hashlib.sha256((SCRIPTS_DIR / "pr_policy.py").read_bytes()).hexdigest()
    reports = {}
    for path in paths:
        report = json.loads(Path(path).read_text(encoding="utf-8"))
        slug = repo_to_slug.get(report.get("repo"))
        if slug is None:
            sys.exit(f"{path}: repo {report.get('repo')!r} has no candidates/*.yaml ledger")
        if report.get("policy_sha256") != policy_sha:
            sys.exit(f"{path}: produced with a different scripts/pr_policy.py; rerun local_prefilter.py")
        if slug in reports:
            sys.exit(f"{path}: duplicate report for {slug}")
        reports[slug] = report
    return reports


def main(argv=None):
    args = parse_args(argv)
    available = sorted(p.stem for p in CANDIDATES_DIR.glob("*.yaml"))
    args.prefilter = load_prefilter_reports(args.from_prefilter)
    if args.prefilter:
        if args.repos:
            sys.exit("--repos cannot be combined with --from-prefilter (each report names its repo)")
        args.repos = ",".join(sorted(args.prefilter))
        args.since = min(date.fromisoformat(r["since"]) for r in args.prefilter.values())
        args.until = min(date.fromisoformat(r["until"]) for r in args.prefilter.values())
    slugs = args.repos.split(",") if args.repos else available
    unknown = [s for s in slugs if s not in available]
    if unknown:
        sys.exit(f"Unknown ledger slug(s): {', '.join(unknown)}. Available: {', '.join(available)}")

    summaries = [sync_repo(slug, args, args.captured_at) for slug in slugs]

    print("\nSummary")
    for s in summaries:
        print(f"  {s['slug']:16} hits={s['hits']:5} new={s['new']:5} include={s['include']:4} "
              f"exclude={s['exclude']:4} defer={s['defer']:4} pages={len(s['pages'])}")
    if args.dry_run:
        print("\nDry run: no files written.")
        return 0

    new_pages = [p for s in summaries for p in s["pages"]]
    update_architecture_receipt(new_pages)
    update_refresh_cutoff(slugs, args.until)
    update_search_results(summaries, args.until, args.captured_at)
    update_count_docs()
    status = run_script("scripts/generate-indices.py")
    if args.validate and status == 0:
        status = run_script("scripts/validate.py")
    if new_pages:
        print("\nNew pages:")
        for p in new_pages:
            print(f"  {p.relative_to(REPO_ROOT)}")
    return status


if __name__ == "__main__":
    sys.exit(main())
