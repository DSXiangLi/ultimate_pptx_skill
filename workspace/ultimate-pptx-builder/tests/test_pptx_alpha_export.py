#!/usr/bin/env python3
"""Regression tests for PPTX alpha/opacity export."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts" / "export_ir_pptx.py"
A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


class PptxAlphaExportTest(unittest.TestCase):
    def test_shape_opacity_is_written_as_drawingml_alpha(self):
        ir = {
            "deck": {
                "id": "alpha-regression",
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
                                "fill": "07111F",
                                "stroke": "07111F",
                                "shape": "rect",
                                "opacity": 1.0,
                                "stroke_opacity": 0.0,
                                "editability": {"priority": 2},
                            },
                            {
                                "id": "s01_orb_violet",
                                "type": "shape",
                                "role": "decorative-glow",
                                "box": {"x": -120, "y": 410, "w": 330, "h": 330},
                                "fill": "7C3AED",
                                "stroke": "7C3AED",
                                "shape": "ellipse",
                                "opacity": 0.045,
                                "stroke_opacity": 0.0,
                                "editability": {"priority": 1},
                            },
                        ],
                    }
                ],
            }
        }
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            ir_path = td_path / "deck.ir.json"
            pptx_path = td_path / "deck.pptx"
            report_path = td_path / "export.json"
            ir_path.write_text(json.dumps(ir, ensure_ascii=False), encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(EXPORTER), str(ir_path), str(pptx_path), "--report", str(report_path)],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            with zipfile.ZipFile(pptx_path) as z:
                root = ET.fromstring(z.read("ppt/slides/slide1.xml"))
            alpha_vals = []
            for sp in root.iter(f"{P_NS}sp"):
                c_nv_pr = sp.find(f"{P_NS}nvSpPr/{P_NS}cNvPr")
                if c_nv_pr is None or c_nv_pr.attrib.get("name") != "s01_orb_violet":
                    continue
                alpha_vals = [node.attrib.get("val") for node in sp.iter(f"{A_NS}alpha")]
            self.assertIn("4500", alpha_vals)


if __name__ == "__main__":
    unittest.main()
