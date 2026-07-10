import json
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_png(path, width, height, bg=(250, 250, 250), rect=None):
    rows = []
    for y in range(height):
        raw = bytearray([0])
        for x in range(width):
            c = bg
            if rect:
                rx, ry, rw, rh, rc = rect
                if rx <= x < rx + rw and ry <= y < ry + rh:
                    c = rc
            raw.extend(bytes(c))
        rows.append(bytes(raw))
    data = zlib.compress(b"".join(rows))

    def chunk(kind, payload):
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", data)
    png += chunk(b"IEND", b"")
    Path(path).write_bytes(png)


def make_pptx(path, slide_xml):
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", "<Types xmlns='http://schemas.openxmlformats.org/package/2006/content-types'/>")
        zf.writestr("ppt/slides/slide1.xml", slide_xml)


class OoxmlAndRenderedQaTests(unittest.TestCase):
    def test_ooxml_audit_blocks_missing_alpha_for_translucent_ir_object(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir = {
                "deck": {
                    "slides": [{"id": "s1", "objects": [{
                        "id": "translucent_panel",
                        "type": "shape",
                        "role": "glass-panel",
                        "box": {"x": 0, "y": 0, "w": 100, "h": 100},
                        "z": 1,
                        "style": {"opacity": 0.4},
                        "editability": {"priority": 3},
                        "render_policy": "native",
                    }]}]
                }
            }
            ir_path = tmp / "deck.ir.json"
            pptx = tmp / "deck.pptx"
            report = tmp / "report.json"
            ir_path.write_text(json.dumps(ir), encoding="utf-8")
            make_pptx(pptx, "<p:sld xmlns:p='http://schemas.openxmlformats.org/presentationml/2006/main'><p:cSld/></p:sld>")
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_ooxml_visual_properties.py"), str(ir_path), str(pptx), "--report", str(report)],
                cwd=str(ROOT), text=True, capture_output=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertIn("PPTX_ALPHA_MISSING", {i["code"] for i in data["issues"]})

    def test_rendered_perceptual_blocks_bottom_edge_pressure(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            bad_dir = tmp / "actual"
            bad_dir.mkdir()
            write_png(bad_dir / "slide-01.png", 200, 120, rect=(20, 108, 160, 10, (20, 20, 20)))
            report = tmp / "report.json"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_rendered_perceptual_layout.py"), str(bad_dir), "--report", str(report), "--bottom-safe-ratio", "0.08"],
                cwd=str(ROOT), text=True, capture_output=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertIn("RENDERED_BOTTOM_EDGE_PRESSURE", {i["code"] for i in data["issues"]})

    def test_rendered_perceptual_passes_safe_image(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            good_dir = tmp / "actual"
            good_dir.mkdir()
            write_png(good_dir / "slide-01.png", 200, 120, rect=(20, 30, 160, 40, (20, 20, 20)))
            report = tmp / "report.json"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_rendered_perceptual_layout.py"), str(good_dir), "--report", str(report), "--bottom-safe-ratio", "0.08"],
                cwd=str(ROOT), text=True, capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["release_decision"], "pass")


if __name__ == "__main__":
    unittest.main()
