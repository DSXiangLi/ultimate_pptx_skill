#!/usr/bin/env python3
"""Tests for the PPTX cloner acceptance loop."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_pptx_specimen_analyzer import make_sample_pptx

ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "scripts" / "run_pptx_cloner_loop.py"
sys.path.insert(0, str(ROOT / "scripts"))


class PptxClonerLoopTests(unittest.TestCase):
    def test_loop_passes_c1_c2_for_simple_deck_and_writes_report(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            pptx = tmp / "sample.pptx"
            out = tmp / "specimen"
            report = out / "cloner-loop-report.json"
            make_sample_pptx(pptx)

            proc = subprocess.run(
                [
                    sys.executable,
                    str(LOOP),
                    str(pptx),
                    "--deck-id",
                    "sample-deck",
                    "--out",
                    str(out),
                    "--skip-render",
                    "--max-iterations",
                    "2",
                ],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertTrue(report.exists())
            data = json.loads(report.read_text(encoding="utf-8"))

            self.assertEqual(data["release_decision"], "pass")
            self.assertEqual(data["blocking_count"], 0)
            self.assertTrue(data["next_phase_allowed"])
            self.assertEqual(data["next_phase"], "C3 diagnostic rebuild fidelity")
            self.assertTrue((out / "original.pptx").exists())
            self.assertTrue((out / "decompiled.raw.ir.json").exists())
            gate_ids = {gate["id"] for gate in data["gates"]}
            self.assertIn("C1-EVIDENCE-PACK", gate_ids)
            self.assertIn("C2-TEXT-RECALL", gate_ids)
            self.assertIn("C2-CRITICAL-TEXT-EDITABILITY", gate_ids)

    def test_evaluator_fails_with_actionable_queue_for_missing_ir(self):
        from run_pptx_cloner_loop import evaluate_c1_c2  # type: ignore
        from analyze_pptx_specimen import analyze  # type: ignore

        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            pptx = tmp / "sample.pptx"
            out = tmp / "specimen"
            make_sample_pptx(pptx)
            analyze(pptx, out, deck_id="sample-deck", skip_render=True)

            report = evaluate_c1_c2(out, require_render=False)

            self.assertEqual(report["release_decision"], "fail")
            self.assertGreater(report["blocking_count"], 0)
            codes = {item["code"] for item in report["optimization_queue"]}
            self.assertIn("decompiled_ir_missing", codes)
            owners = {item["owner"] for item in report["optimization_queue"]}
            self.assertIn("C2 decompiler", owners)


if __name__ == "__main__":
    unittest.main()
