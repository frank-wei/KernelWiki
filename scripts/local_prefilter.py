#!/usr/bin/env python3
"""Offline PR prefilter over a local upstream clone.

Walks the first-parent history of a local clone for a merge-date window, maps
each squash/merge commit to its PR number, and applies the shared
``pr_policy.classify_scope`` rule to the commit's complete diff. ``.cu`` and
weak-tuning ``.py`` hunks that are inconclusive on their own are resolved with
complete-file receipts read from the clone, mirroring the evolve audit's
PR-head raw-file evidence.

No network access is used and no tracked file is modified: the report goes to
``.worklog/prefilter/`` (gitignored). Retained PRs are *candidates* only;
publishing a page still requires the authoritative GitHub PR object (title,
description, author, changed-file totals) via scripts/sync_prs.py.

Usage:
  python3 scripts/local_prefilter.py --repo vllm --since 2026-05-21
  python3 scripts/local_prefilter.py --repo sglang --since 2026-05-21 --until 2026-10-20 --clones ~/upstream
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _yaml_compat import yaml  # noqa: E402
import pr_policy  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
CANDIDATES_DIR = REPO_ROOT / "candidates"
DEFAULT_OUT_DIR = REPO_ROOT / ".worklog" / "prefilter"

COMMIT_MARKER = "\x00KWCOMMIT\x00"
PREVIEW_PATCH_LIMIT = 200_000  # bytes of each evidence hunk scanned for the architecture preview
PR_SUBJECT_RES = (
    re.compile(r"\(#(\d+)\)\s*$"),
    re.compile(r"^Merge pull request #(\d+)\b"),
)


SRC_PREFIX, DST_PREFIX = "KWSRC/", "KWDST/"
_DIFF_HEADER_RE = re.compile(rf"(?m)^diff --git {SRC_PREFIX}(.+) {DST_PREFIX}(.+)$")


def _c_quote(path):
    return '"' + path.replace("\\", "\\\\").replace('"', '\\"') + '"'


def quote_diff_headers(diff_text):
    """Rewrite headers to quoted a/ b/ paths for pr_policy's shlex-based parser.

    Git leaves paths with spaces unquoted, so iter_commits emits distinctive
    prefixes that make the old/new split unambiguous even for renames.
    """
    def repl(match):
        old, new = match.group(1), match.group(2)
        if old.startswith('"') or new.startswith('"'):
            return match.group(0)  # git already C-quoted this path
        return f"diff --git {_c_quote('a/' + old)} {_c_quote('b/' + new)}"

    return _DIFF_HEADER_RE.sub(repl, diff_text)


def pr_number_from_subject(subject):
    for pattern in PR_SUBJECT_RES:
        match = pattern.search(subject)
        if match:
            return int(match.group(1))
    return None


class BlobReader:
    """Read file contents at a commit through one ``git cat-file --batch`` process."""

    def __init__(self, clone):
        self.proc = subprocess.Popen(
            ["git", "-C", str(clone), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            env={**os.environ, "GIT_NO_LAZY_FETCH": "1"},
        )

    def read(self, sha, path):
        self.proc.stdin.write(f"{sha}:{path}\n".encode("utf-8"))
        self.proc.stdin.flush()
        header = self.proc.stdout.readline().decode("utf-8", "replace").split()
        if len(header) != 3:  # "<spec> missing"
            return None
        size = int(header[2])
        data = self.proc.stdout.read(size)
        self.proc.stdout.read(1)  # trailing newline
        return data

    def close(self):
        self.proc.stdin.close()
        self.proc.wait()


def add_complete_file_receipts(files, sha, blobs):
    """Attach complete-file evidence where a hunk alone is inconclusive."""
    for item in files:
        needs_cuda = pr_policy.cuda_requires_complete_evidence(item)
        needs_python = pr_policy.python_requires_complete_evidence(item)
        if not (needs_cuda or needs_python):
            continue
        data = blobs.read(sha, item["filename"])
        if data is None:
            continue
        text = data.decode("utf-8", "replace")
        digest = hashlib.sha256(data).hexdigest()
        if needs_cuda:
            item.update({
                "complete_file_evidence_complete": True,
                "complete_file_sha256": digest,
                "complete_file_device_pattern_sha256": pr_policy.device_code_pattern_sha256(),
                "complete_file_device_signal": pr_policy.cuda_translation_unit_device_signal(text),
            })
        if needs_python:
            languages = sorted(set(pr_policy.python_dsl_languages(text)))
            item.update({
                "complete_file_python_dsl_evidence_complete": True,
                "complete_file_python_dsl_sha256": digest,
                "complete_file_python_dsl_pattern_sha256": pr_policy.python_dsl_pattern_sha256(),
                "complete_file_python_dsl_signal": bool(languages),
                "complete_file_python_dsl_languages": languages,
            })


def iter_commits(clone, since, until):
    """Yield (sha, commit_date, subject, diff_text) along first-parent history."""
    cmd = [
        "git", "-C", str(clone), "log", "--first-parent", "--diff-merges=first-parent",
        "-p", "--no-color", "--no-ext-diff", "-M",
        f"--src-prefix={SRC_PREFIX}", f"--dst-prefix={DST_PREFIX}",
        f"--since={since.isoformat()} 00:00:00", f"--until={until.isoformat()} 23:59:59",
        "--format=%x00KWCOMMIT%x00%H%x00%cs%x00%s", "HEAD",
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, env={**os.environ, "GIT_NO_LAZY_FETCH": "1"})
    header, lines = None, []

    def flush():
        sha, commit_date, subject = header.split("\x00", 2)
        return sha, commit_date, subject, "".join(lines)

    for raw in proc.stdout:
        line = raw.decode("utf-8", "replace")
        if line.startswith(COMMIT_MARKER):
            if header is not None:
                yield flush()
            header, lines = line[len(COMMIT_MARKER):].rstrip("\n"), []
        else:
            lines.append(line)
    if header is not None:
        yield flush()
    if proc.wait() != 0:
        raise RuntimeError(f"git log failed in {clone}")


def prefilter(clone, since, until, known_numbers):
    blobs = BlobReader(clone)
    candidates, removed, already, no_pr = [], {}, [], 0
    rule_counts = Counter()
    try:
        for index, (sha, commit_date, subject, diff_text) in enumerate(iter_commits(clone, since, until), 1):
            if index % 500 == 0:
                print(f"  ... {index} commits scanned", file=sys.stderr)
            number = pr_number_from_subject(subject)
            if number is None:
                no_pr += 1
                continue
            if number in known_numbers:
                already.append(number)
                continue
            files = pr_policy.parse_git_diff_files(quote_diff_headers(diff_text))
            add_complete_file_receipts(files, sha, blobs)
            decision = pr_policy.classify_scope(subject, "", files)
            rule_counts[decision.rule] += 1
            if not decision.retain:
                removed[number] = decision.rule
                continue
            # Informational preview only: limit to qualifying paths and cap each
            # hunk so a giant generated file cannot stall the scan.
            evidence = set(decision.evidence_paths)
            preview_files = [
                {**f, "patch": f["patch"][:PREVIEW_PATCH_LIMIT]}
                for f in files if f["filename"] in evidence
            ]
            archs, disposition, _ = pr_policy.derive_architectures(subject, "", preview_files)
            candidates.append({
                "number": number,
                "merge_sha": sha,
                "date": commit_date,
                "title": subject,
                "rule": decision.rule,
                "evidence_paths": list(decision.evidence_paths),
                "files_count": len(files),
                "architectures_preview": archs,
                "architecture_disposition_preview": disposition,
            })
    finally:
        blobs.close()
    return candidates, removed, sorted(already), no_pr, rule_counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", required=True, help="Ledger slug, e.g. vllm (candidates/<slug>.yaml).")
    parser.add_argument("--since", required=True, type=date.fromisoformat)
    parser.add_argument("--until", default=date.today(), type=date.fromisoformat)
    parser.add_argument("--clones", default=str(Path.home() / "upstream"),
                        help="Directory holding the clones (default: ~/upstream).")
    parser.add_argument("--out", default=None, help="Report path (default: .worklog/prefilter/<slug>_<since>_<until>.json).")
    args = parser.parse_args(argv)

    ledger_path = CANDIDATES_DIR / f"{args.repo}.yaml"
    if not ledger_path.is_file():
        sys.exit(f"No ledger {ledger_path.relative_to(REPO_ROOT)}")
    ledger = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    repo_full = ledger["repo"]
    clone = Path(args.clones).expanduser() / repo_full.split("/")[1]
    if not (clone / ".git").exists():
        sys.exit(f"No clone at {clone}")
    known = {row.get("number") for row in ledger.get("prs") or [] if isinstance(row, dict)}
    head = subprocess.check_output(
        ["git", "-C", str(clone), "log", "-1", "--format=%H %cs"], text=True
    ).split()

    print(f"{repo_full}: scanning {clone} first-parent history {args.since}..{args.until} (HEAD {head[0][:12]} {head[1]})")
    candidates, removed, already, no_pr, rule_counts = prefilter(clone, args.since, args.until, known)

    report = {
        "repo": repo_full,
        "clone": str(clone),
        "clone_head": head[0],
        "clone_head_date": head[1],
        "since": args.since.isoformat(),
        "until": args.until.isoformat(),
        "policy_sha256": hashlib.sha256((REPO_ROOT / "scripts" / "pr_policy.py").read_bytes()).hexdigest(),
        "generated_at": date.today().isoformat(),
        "evidence_note": "commit subject + complete local diff; PR description not consulted; architectures_preview uses evidence-path hunks capped at 200 KB",
        "counts": {
            "pr_commits_classified": len(candidates) + len(removed),
            "candidates": len(candidates),
            "removed": len(removed),
            "already_in_ledger": len(already),
            "commits_without_pr_number": no_pr,
            "by_rule": dict(sorted(rule_counts.items())),
        },
        "candidates": candidates,
        "removed": {str(k): v for k, v in sorted(removed.items())},
        "already_in_ledger": already,
    }
    out = Path(args.out) if args.out else DEFAULT_OUT_DIR / f"{args.repo}_{args.since}_{args.until}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")

    c = report["counts"]
    print(f"\nPR commits classified: {c['pr_commits_classified']}  candidates: {c['candidates']}  "
          f"removed: {c['removed']}  already in ledger: {c['already_in_ledger']}  "
          f"commits without PR number: {c['commits_without_pr_number']}")
    for rule, n in c["by_rule"].items():
        print(f"  {rule:40} {n}")
    blackwell = sum(
        any(a.startswith(pr_policy.BLACKWELL_EXACT_PREFIXES) or a == "blackwell"
            for a in cand["architectures_preview"])
        for cand in candidates
    )
    print(f"  candidates with Blackwell evidence in title/diff: {blackwell}")
    print(f"\nReport: {out.relative_to(REPO_ROOT) if out.is_relative_to(REPO_ROOT) else out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
