#!/usr/bin/env python3
"""Regression tests for visual aesthetic contract checks."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_visual_aesthetic_contract.py"


class VisualAestheticContractTest(unittest.TestCase):
    def run_checker(self, ir: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as td:
            ir_path = Path(td) / "deck.ir.json"
            ir_path.write_text(json.dumps(ir, ensure_ascii=False), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER), str(ir_path)],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )

    def test_bottom_edge_large_glow_is_blocked_as_visual_noise(self):
        """Bottom decorative orbs should stay atmospheric, not become visual subjects."""
        ir = {
            "deck": {
                "style_program": "glass-fintech-pptx",
                "size": {"w": 1280, "h": 720},
                "slides": [
                    {
                        "id": "s01",
                        "objects": [
                            {
                                "id": "s01_bg",
                                "type": "shape",
                                "role": "background",
                                "box": {"x": 0, "y": 0, "w": 1280, "h": 720},
                                "opacity": 1.0,
                            },
                            {
                                "id": "s01_orb_cyan",
                                "type": "shape",
                                "role": "decorative-glow",
                                "box": {"x": 870, "y": -70, "w": 360, "h": 360},
                                "opacity": 0.16,
                            },
                            {
                                "id": "s01_orb_violet",
                                "type": "shape",
                                "role": "decorative-glow",
                                "box": {"x": -120, "y": 410, "w": 330, "h": 330},
                                "opacity": 0.13,
                            },
                            {
                                "id": "s01_panel",
                                "type": "shape",
                                "role": "glass-panel",
                                "box": {"x": 80, "y": 180, "w": 640, "h": 300},
                                "opacity": 0.58,
                            },
                        ],
                    }
                ],
            }
        }

        proc = self.run_checker(ir)

        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("GLASS_DECORATIVE_NOISE_TOO_STRONG", proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
