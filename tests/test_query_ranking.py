import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import query  # noqa: E402


def page(path, title, fm_type=None, body=""):
    fm = {"id": path, "title": title}
    if fm_type:
        fm["type"] = fm_type
    return {"path": path, "fm": fm, "body": body}


def score(p, text):
    return query.score_keyword_match(p, query.query_terms(text.split()))


class KeywordMatchTests(unittest.TestCase):
    def test_terms_match_on_token_boundaries_only(self):
        p = page("wiki/kernels/fused-moe.md", "Fused MoE and Adjacent Operations", "kernel")

        self.assertEqual(0, score(p, "era"))
        self.assertEqual(10, score(p, "operation"))

    def test_stopwords_are_dropped_unless_the_query_is_only_stopwords(self):
        self.assertEqual([["fuse"], ["gate up"]], query.query_terms("how to fuse gate-up on".split()))
        self.assertEqual([["on"]], query.query_terms(["on"]))

    def test_hyphenated_terms_and_aliases_match(self):
        p = page("wiki/kernels/gated-dual-gemm.md", "Gated Dual GEMM (Gate-Up + Activation)", "kernel",
                 body="tcgen05 tcgen05")

        self.assertEqual(10, score(p, "gate-up"))
        self.assertEqual(2, score(p, "UMMA"))


class SectionTests(unittest.TestCase):
    def test_half_the_slots_go_to_wiki_and_unused_slots_flow_over(self):
        wiki = [page(f"wiki/kernels/k{i}.md", "w", "kernel") for i in range(8)]
        sources = [page(f"sources/prs/r/PR-{i}.md", "s") for i in range(8)]

        self.assertEqual((5, 5), tuple(map(len, query.split_sections(wiki + sources, 10))))
        self.assertEqual((2, 1), tuple(map(len, query.split_sections(wiki + sources, 3))))
        self.assertEqual((2, 8), tuple(map(len, query.split_sections(wiki[:2] + sources, 10))))
        self.assertEqual((8, 2), tuple(map(len, query.split_sections(wiki + sources[:2], 10))))


class CorpusRankingRegressionTests(unittest.TestCase):
    """The 2026-10-20 intake (944 -> 4,559 PR pages) pushed wiki pages out of
    mixed top-k results; these queries guard both layers on the real corpus."""

    @classmethod
    def setUpClass(cls):
        cls.pages = query.load_all_pages()

    def sections(self, text):
        wiki, sources = query.split_sections(query.rank_pages(self.pages, text.split()), 10)
        return [p["path"] for p in wiki], [p["path"] for p in sources]

    def test_topic_queries_list_their_wiki_pages_first(self):
        cases = {
            "tcgen05 tmem epilogue": ["hardware/tmem", "hardware/tcgen05-mma", "migration/register-to-tmem",
                                      "techniques/epilogue-fusion"],
            "nvfp4 grouped gemm moe on blackwell": ["kernels/grouped-gemm", "kernels/fused-moe", "kernels/nvfp4-gemm"],
            "how to fuse gate-up dual GEMM on Blackwell": ["kernels/gated-dual-gemm"],
            "cluster launch control persistent scheduler": ["hardware/clc"],
        }
        for text, expected in cases.items():
            with self.subTest(query=text):
                wiki, _ = self.sections(text)
                self.assertLessEqual({f"wiki/{e}.md" for e in expected}, set(wiki), wiki)

    def test_queries_naming_a_specific_pr_rank_it_top_three_in_sources(self):
        cases = {
            "Frost Moe Grouped Gemm SM120 Swap-AB": "sources/prs/flashinfer/PR-6504.md",
            "InjectTcgen05Fence pass": "sources/prs/tilelang/PR-2003.md",
            "half-subpartition TMEM tiles tcgen05.ld": "sources/prs/tilelang/PR-2880.md",
            "Blockscaled Ragged Contiguous Grouped Gemm": "sources/prs/cutlass/PR-2790.md",
            "densegemm backend for MoE": "sources/prs/TensorRT-LLM/PR-10479.md",
        }
        for text, expected in cases.items():
            with self.subTest(query=text):
                _, sources = self.sections(text)
                self.assertIn(expected, sources[:3], sources)


if __name__ == "__main__":
    unittest.main()
