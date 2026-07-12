import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


VALID_CORPUS = {
    "version": 1,
    "required_style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"],
    "required_scenarios": ["macro-review", "fund-comparison", "allocation-decision"],
    "required_density_modes": ["executive", "analyst", "dense"],
    "required_gate_reports": [
        "layout-safety",
        "text-spacing",
        "alignment-graph",
        "component-layout-contract",
        "visual-layout-architecture",
        "visual-aesthetic-contract",
        "visual-dna-realization",
        "ooxml-visual-properties",
        "rendered-perceptual-layout",
        "visual-fidelity",
        "qa-report"
    ],
    "cases": [
        {"id": "macro-exec", "scenario": "macro-review", "density_mode": "executive", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "low", "must_preserve": ["conclusion", "source", "risk"]},
        {"id": "macro-analyst", "scenario": "macro-review", "density_mode": "analyst", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "medium", "must_preserve": ["evidence", "logic", "source", "risk"]},
        {"id": "macro-dense", "scenario": "macro-review", "density_mode": "dense", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "high", "must_preserve": ["conclusion", "evidence", "logic", "source", "risk"]},
        {"id": "fund-exec", "scenario": "fund-comparison", "density_mode": "executive", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "low", "must_preserve": ["recommendation", "source", "risk"]},
        {"id": "fund-analyst", "scenario": "fund-comparison", "density_mode": "analyst", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "medium", "must_preserve": ["recommendation", "evidence", "logic", "source", "risk"]},
        {"id": "fund-dense", "scenario": "fund-comparison", "density_mode": "dense", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "high", "must_preserve": ["recommendation", "evidence", "logic", "source", "risk"]},
        {"id": "alloc-exec", "scenario": "allocation-decision", "density_mode": "executive", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "low", "must_preserve": ["decision", "source", "risk"]},
        {"id": "alloc-analyst", "scenario": "allocation-decision", "density_mode": "analyst", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "medium", "must_preserve": ["decision", "evidence", "logic", "source", "risk"]},
        {"id": "alloc-dense", "scenario": "allocation-decision", "density_mode": "dense", "style_programs": ["glass-fintech-pptx", "paper-analyst-report", "market-atlas-infographic"], "content_pressure": "high", "must_preserve": ["decision", "evidence", "logic", "source", "risk"]}
    ]
}


class FinanceBenchmarkCorpusTests(unittest.TestCase):
    def run_gate(self, corpus):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            corpus_path = tmp / "corpus.json"
            report = tmp / "report.json"
            corpus_path.write_text(json.dumps(corpus, ensure_ascii=False), encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_finance_benchmark_corpus.py"), str(corpus_path), "--report", str(report)],
                cwd=str(ROOT), text=True, capture_output=True,
            )
            data = json.loads(report.read_text(encoding="utf-8")) if report.exists() else None
            return proc, data

    def test_missing_density_and_style_coverage_fails(self):
        bad = dict(VALID_CORPUS)
        bad["cases"] = [dict(VALID_CORPUS["cases"][0], style_programs=["glass-fintech-pptx"])]
        proc, report = self.run_gate(bad)
        self.assertIsNotNone(report)
        assert report is not None
        self.assertNotEqual(proc.returncode, 0)
        codes = {i["code"] for i in report["issues"]}
        self.assertIn("BENCHMARK_SCENARIO_DENSITY_COVERAGE_MISSING", codes)
        self.assertIn("BENCHMARK_STYLE_COVERAGE_MISSING", codes)

    def test_valid_corpus_passes_static_coverage(self):
        proc, report = self.run_gate(VALID_CORPUS)
        self.assertIsNotNone(report)
        assert report is not None
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertEqual(report["release_decision"], "pass")
        self.assertEqual(report["coverage"]["scenario_density_pairs"], 9)
        self.assertEqual(report["coverage"]["style_programs"], 3)


if __name__ == "__main__":
    unittest.main()
