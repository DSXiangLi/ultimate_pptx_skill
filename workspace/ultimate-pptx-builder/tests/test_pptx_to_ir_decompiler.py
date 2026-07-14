#!/usr/bin/env python3
"""Tests for PPTX OOXML/object inventory to raw Slide IR decompiler."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_pptx_specimen_analyzer import make_sample_pptx

ROOT = Path(__file__).resolve().parents[1]
DECOMPILER = ROOT / "scripts" / "decompile_pptx_to_ir.py"


class PptxToIrDecompilerTests(unittest.TestCase):
    def test_decompiler_preserves_slide_count_text_and_source_references(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            pptx = tmp / "sample.pptx"
            out = tmp / "decompiled.raw.ir.json"
            make_sample_pptx(pptx)

            proc = subprocess.run(
                [sys.executable, str(DECOMPILER), str(pptx), "--out", str(out), "--deck-id", "sample-deck"],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertTrue(out.exists())
            data = json.loads(out.read_text(encoding="utf-8"))

            self.assertEqual(data["deck"]["id"], "sample-deck")
            self.assertEqual(len(data["deck"]["slides"]), 1)
            slide = data["deck"]["slides"][0]
            self.assertEqual(slide["source_xml_path"], "ppt/slides/slide1.xml")
            self.assertEqual(slide["background"]["kind"], "solid")
            self.assertEqual(slide["background"]["rgb"], "123456")
            self.assertGreaterEqual(len(slide["objects"]), 3)

            texts = "\n".join(obj.get("text", "") for obj in slide["objects"])
            self.assertIn("Clone Analyzer Title", texts)
            self.assertIn("Metric 42%", texts)
            self.assertIn("Grouped Insight", texts)

            object_types = {obj["type"] for obj in slide["objects"]}
            self.assertIn("text", object_types)
            self.assertIn("shape", object_types)
            self.assertIn("image", object_types)
            self.assertIn("group", object_types)

            grouped = [obj for obj in slide["objects"] if obj.get("text") == "Grouped Insight"]
            self.assertTrue(grouped)
            self.assertRegex(grouped[0].get("group_id", ""), r"^slide01_shape\d+$")
            self.assertEqual(grouped[0].get("parent_group_name"), "sample_group")

            image_objs = [obj for obj in slide["objects"] if obj["type"] == "image"]
            self.assertTrue(image_objs)
            image_ref = image_objs[0].get("image_ref") or {}
            self.assertRegex(image_ref.get("relationship_id", ""), r"^rId\d+$")
            self.assertRegex(image_ref.get("package_path", ""), r"^ppt/media/.+\.png$")
            self.assertEqual(image_ref.get("ext"), "png")

            for obj in slide["objects"]:
                self.assertIn("id", obj)
                self.assertIn("box", obj)
                self.assertIn("z", obj)
                self.assertIn("source_xml_path", obj)
                self.assertIn("source_shape_id", obj)
                self.assertIn("editability", obj)
                self.assertIn("render_policy", obj)

            critical_text = [obj for obj in slide["objects"] if obj.get("text")]
            self.assertTrue(all(obj["editability"]["priority"] >= 4 for obj in critical_text))
            self.assertTrue(all(obj["render_policy"] == "native" for obj in critical_text))

    def test_decompiler_preserves_picture_fill_shape_media_reference(self):
        pptx = ROOT / "research" / "pptx-template-library" / "files" / "it-software-sales-proposal-slides.pptx"
        if not pptx.exists():
            self.skipTest("template library fixture is unavailable")
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "decompiled.raw.ir.json"
            proc = subprocess.run(
                [sys.executable, str(DECOMPILER), str(pptx), "--out", str(out), "--deck-id", "it-software-sales-proposal-slides"],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(out.read_text(encoding="utf-8"))
            slide10 = data["deck"]["slides"][9]
            shape315 = next(obj for obj in slide10["objects"] if obj.get("source_shape_id") == "315")
            fill_ref = shape315.get("fill_image_ref") or {}
            self.assertEqual(shape315["type"], "shape")
            self.assertRegex(fill_ref.get("relationship_id", ""), r"^rId\d+$")
            self.assertEqual(fill_ref.get("package_path"), "ppt/media/image12.png")


if __name__ == "__main__":
    unittest.main()
