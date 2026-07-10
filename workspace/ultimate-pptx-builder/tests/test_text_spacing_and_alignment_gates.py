import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(script, ir_path, report_path):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), str(ir_path), "--report", str(report_path)],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
    )


def write_ir(path, slides):
    path.write_text(
        json.dumps({"deck": {"id": "test", "size": {"w": 1280, "h": 720}, "slides": slides}}, ensure_ascii=False),
        encoding="utf-8",
    )


def text_obj(oid, role, text, x, y, w, h, size=12, priority=4):
    return {
        "id": oid,
        "type": "text",
        "role": role,
        "text": text,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": 10,
        "style": {"size": size},
        "editability": {"priority": priority},
        "render_policy": "native",
    }


def shape_obj(oid, role, x, y, w, h):
    return {
        "id": oid,
        "type": "shape",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": 1,
        "editability": {"priority": 3},
        "render_policy": "native",
    }


class TextSpacingAndAlignmentGateTests(unittest.TestCase):
    def test_text_spacing_blocks_unrelated_priority_text_with_tiny_gap(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "spacing.ir.json"
            report = tmp / "spacing.report.json"
            write_ir(
                ir_path,
                [
                    {
                        "id": "s01",
                        "objects": [
                            text_obj("left_body", "body", "左侧正文", 100, 100, 120, 30),
                            text_obj("right_body", "body", "右侧正文", 224, 102, 120, 30),
                        ],
                    }
                ],
            )
            proc = run_script("check_text_spacing.py", ir_path, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertTrue(any(i["code"] == "UNRELATED_TEXT_GAP_TOO_SMALL" for i in data["issues"]))

    def test_text_spacing_allows_declared_compact_metric_stack(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "metric.ir.json"
            report = tmp / "metric.report.json"
            write_ir(
                ir_path,
                [
                    {
                        "id": "s01",
                        "objects": [
                            text_obj("s01_metric_1_label", "metric-label", "收益", 100, 100, 120, 12, size=8),
                            text_obj("s01_metric_1_value", "metric", "+3.2%", 100, 116, 120, 20, size=13),
                            text_obj("s01_metric_1_delta", "metric-note", "较基准+80bp", 100, 140, 120, 16, size=8),
                        ],
                    }
                ],
            )
            proc = run_script("check_text_spacing.py", ir_path, report)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_alignment_graph_blocks_declared_left_alignment_break(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "alignment.ir.json"
            report = tmp / "alignment.report.json"
            slide = {
                "id": "s01",
                "layout_relations": [
                    {"id": "title-column", "type": "align-left", "objects": ["title", "subtitle", "body"], "tolerance": 4}
                ],
                "objects": [
                    text_obj("title", "title", "标题", 80, 80, 400, 40),
                    text_obj("subtitle", "body", "副标题", 82, 130, 400, 24),
                    text_obj("body", "body", "正文", 104, 180, 400, 40),
                ],
            }
            write_ir(ir_path, [slide])
            proc = run_script("check_alignment_graph.py", ir_path, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertTrue(any(i["code"] == "DECLARED_ALIGN_LEFT_BROKEN" for i in data["issues"]))

    def test_alignment_graph_blocks_equal_gutter_break(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "gutter.ir.json"
            report = tmp / "gutter.report.json"
            slide = {
                "id": "s01",
                "layout_relations": [
                    {
                        "id": "metric-row",
                        "type": "row",
                        "objects": ["card1", "card2", "card3"],
                        "align": ["top", "bottom"],
                        "equal": ["width", "height"],
                        "gutter": {"mode": "equal", "tolerance": 3},
                    }
                ],
                "objects": [
                    shape_obj("card1", "metric-card", 80, 180, 120, 60),
                    shape_obj("card2", "metric-card", 220, 180, 120, 60),
                    shape_obj("card3", "metric-card", 390, 180, 120, 60),
                ],
            }
            write_ir(ir_path, [slide])
            proc = run_script("check_alignment_graph.py", ir_path, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertTrue(any(i["code"] == "EQUAL_GUTTER_BROKEN" for i in data["issues"]))


if __name__ == "__main__":
    unittest.main()
