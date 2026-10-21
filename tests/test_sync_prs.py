import importlib.util
import unittest
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sync_prs", ROOT / "scripts/sync_prs.py")
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


def merged_pr(number, title="[Kernel] SM100 kernel"):
    return {
        "number": number,
        "title": title,
        "body": "Tuned on B200.",
        "merged_at": "2026-07-01T00:00:00Z",
    }


DEVICE_FILE = {
    "filename": "csrc/sm100/kernel.cu",
    "status": "added",
    "patch": "@@ -0,0 +1,2 @@\n+__global__ void k(float* x) {\n+}",
}
DOC_FILE = {"filename": "docs/index.md", "status": "modified", "patch": "@@ -1 +1,2 @@\n+doc"}


class SearchRangeTests(unittest.TestCase):
    def test_capped_window_is_bisected_until_complete(self):
        calls = []

        def fake_search(repo, query, start, end):
            calls.append((start, end))
            days = (end - start).days + 1
            if days > 2:
                return [{"number": i} for i in range(SYNC.SEARCH_RESULT_CAP)]
            return [{"number": start.toordinal() * 10 + i} for i in range(days)]

        rows = SYNC.search_range("o/r", "kw", date(2026, 1, 1), date(2026, 1, 8), fake_search)

        self.assertEqual(8, len(rows))
        self.assertEqual(8, len({r["number"] for r in rows}))
        d = lambda day: date(2026, 1, day)  # noqa: E731
        self.assertEqual(
            [(d(1), d(8)), (d(1), d(4)), (d(1), d(2)), (d(3), d(4)),
             (d(5), d(8)), (d(5), d(6)), (d(7), d(8))],
            calls,
        )

    def test_keyword_results_are_unioned_and_sorted(self):
        def fake_search(repo, query, start, end):
            return {
                "a": [{"number": 3, "title": "x", "closedAt": "2026-02-01T00:00:00Z"}],
                "b": [{"number": 1, "title": "y", "closedAt": "2026-01-01T00:00:00Z"},
                      {"number": 3, "title": "x", "closedAt": "2026-02-01T00:00:00Z"}],
            }[query]

        rows = SYNC.search_repo("o/r", ["a", "b"], date(2026, 1, 1), date(2026, 3, 1), fake_search)

        self.assertEqual([1, 3], [r["number"] for r in rows])
        self.assertEqual("2026-01-01", rows[0]["closedAt"])


class LedgerRowTests(unittest.TestCase):
    hit = {"number": 7, "title": "search title", "closedAt": "2026-07-01"}

    def test_device_kernel_pr_is_included_with_evidence_paths(self):
        row, scope = SYNC.build_ledger_row(self.hit, (merged_pr(7), [DEVICE_FILE, DOC_FILE]))

        self.assertEqual("include", row["decision"])
        self.assertEqual(["csrc/sm100/kernel.cu"], row["files_changed"])
        self.assertEqual(2, row["files_reviewed_count"])
        self.assertTrue(scope.retain)

    def test_docs_only_pr_is_excluded(self):
        row, scope = SYNC.build_ledger_row(self.hit, (merged_pr(7, "[Doc] docs"), [DOC_FILE]))

        self.assertEqual("exclude", row["decision"])
        self.assertEqual("removed", row["scope_disposition"])

    def test_missing_evidence_is_deferred_and_unmerged_is_excluded(self):
        deferred, _ = SYNC.build_ledger_row(self.hit, None)
        unmerged, _ = SYNC.build_ledger_row(self.hit, ({**merged_pr(7), "merged_at": None}, [DEVICE_FILE]))

        self.assertEqual("defer", deferred["decision"])
        self.assertEqual("exclude", unmerged["decision"])


class ResolveLandedTests(unittest.TestCase):
    sha = "165fff5c58e0639dd5b5a78d421dc6a8eaa7f3fc"
    hit = {"number": 7, "title": "t", "closedAt": "2026-10-19", "landedSha": sha}
    closed = {**merged_pr(7), "merged_at": None, "state": "closed",
              "closed_at": "2026-10-19T19:00:26Z", "merge_commit_sha": "5b08" * 10}

    def commit(self, subject, sha=None):
        return lambda repo, s: {
            "sha": sha or s,
            "commit": {"message": f"{subject}\n\nbody", "committer": {"date": "2026-10-19T18:59:00Z"}},
        }

    def test_bot_landed_pr_is_merged_at_landed_commit(self):
        evidence = SYNC.resolve_landed((self.closed, [DEVICE_FILE]), self.hit, "o/r",
                                       self.commit("Fix sort (#7)"))
        row, _ = SYNC.build_ledger_row(self.hit, evidence)

        self.assertEqual(self.sha, evidence[0]["merge_commit_sha"])
        self.assertEqual("2026-10-19T18:59:00Z", evidence[0]["merged_at"])
        self.assertEqual("include", row["decision"])

    def test_unconfirmed_landing_stays_unmerged(self):
        cases = [
            (self.hit, self.commit("Fix sort (#70)")),
            (self.hit, self.commit("Fix sort (#7)", sha="0" * 40)),
            (self.hit, lambda repo, s: None),
            ({**self.hit, "landedSha": None}, self.commit("Fix sort (#7)")),
        ]
        for hit, commit_fn in cases:
            evidence = SYNC.resolve_landed((self.closed, [DEVICE_FILE]), hit, "o/r", commit_fn)
            self.assertIsNone(evidence[0]["merged_at"])

    def test_github_merged_and_open_prs_are_untouched(self):
        def fail(repo, sha):
            raise AssertionError("commit lookup not expected")

        merged = (merged_pr(7), [DEVICE_FILE])
        opened = ({**self.closed, "state": "open"}, [DEVICE_FILE])
        self.assertIs(merged, SYNC.resolve_landed(merged, self.hit, "o/r", fail))
        self.assertIs(opened, SYNC.resolve_landed(opened, self.hit, "o/r", fail))
        self.assertIsNone(SYNC.resolve_landed(None, self.hit, "o/r", fail))

    def test_relanded_prefilter_pr_is_processed_once_at_latest_landing(self):
        def candidate(number, sha, day):
            return {"number": number, "merge_sha": sha * 40, "date": day, "title": f"t (#{number})"}

        report = {"since": "2026-05-21", "until": "2026-10-20", "clone_head": "f" * 40, "candidates": [
            candidate(900001, "a", "2026-06-01"),
            candidate(900001, "b", "2026-06-09"),
            candidate(900002, "c", "2026-06-03"),
        ]}
        args = SimpleNamespace(prefilter={"tilekernels": report}, retry_deferred=False,
                               max_new=None, dry_run=False)
        seen = []

        def evidence(repo, number):
            seen.append(number)
            return None

        with mock.patch.object(Path, "write_text", lambda *a, **k: None):  # keep the real ledger untouched
            summary = SYNC.sync_repo("tilekernels", args, "2026-10-20", evidence_fn=evidence)

        self.assertEqual([900001, 900002], seen)
        self.assertEqual("b" * 40, [h for h in summary["seen"] if h["number"] == 900001][0]["landedSha"])


class CountTextTests(unittest.TestCase):
    def test_counts_are_rewritten_and_missing_repo_rows_appended(self):
        primer = (
            "| Repo | PR pages | Ledger |\n|---|---:|---|\n"
            "| vllm-project/vllm | 205 | `candidates/vllm.yaml` |\n\nQuery by repo"
        )
        skill = "current distribution: 942 merged, 2 closed without merge"
        schema = "(942 of 944 are `merged`; two are `closed` without merge)"
        counts = {"vllm": 210, "quack": 3}
        ledgers = {"vllm": "vllm-project/vllm", "quack": "Dao-AILab/quack"}

        primer, skill, schema = SYNC.sync_count_text(primer, skill, schema, counts, 950, 2, 952, ledgers)

        self.assertIn("| vllm-project/vllm | 210 | `candidates/vllm.yaml` |", primer)
        self.assertIn("| Dao-AILab/quack | 3 | `candidates/quack.yaml` |\n\nQuery by repo", primer)
        self.assertEqual("current distribution: 950 merged, 2 closed without merge", skill)
        self.assertEqual("(950 of 952 are `merged`; two are `closed` without merge)", schema)


if __name__ == "__main__":
    unittest.main()
