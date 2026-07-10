import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_gate(ir_path, report_path):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_component_layout_contract.py"), str(ir_path), "--report", str(report_path)],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
    )


def write_ir(path, slides):
    path.write_text(
        json.dumps({"deck": {"id": "component-test", "size": {"w": 1280, "h": 720}, "slides": slides}}, ensure_ascii=False),
        encoding="utf-8",
    )


def shape_obj(oid, role, x, y, w, h, z=1, priority=3):
    return {
        "id": oid,
        "type": "shape",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "editability": {"priority": priority},
        "render_policy": "native",
    }


def text_obj(oid, role, text, x, y, w, h, z=10, size=9, priority=4):
    return {
        "id": oid,
        "type": "text",
        "role": role,
        "text": text,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "style": {"size": size},
        "editability": {"priority": priority},
        "render_policy": "native",
    }


class ComponentLayoutContractTests(unittest.TestCase):
    def test_atlas_route_map_blocks_bottom_band_intruding_node_cards_and_floating_badge(self):
        """Page2 failure class: bottom rule band and NOW badge visually cover route cards."""
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "bad-route-map.ir.json"
            report = tmp / "bad-route-map.report.json"
            slide = {
                "id": "ls02",
                "objects": [
                    shape_obj("ls02_budget_map_panel", "route-map", 88, 398, 610, 186, z=20),
                    shape_obj("ls02_macro_zone_1", "route-map", 126, 456, 170, 72, z=30),
                    shape_obj("ls02_macro_zone_2", "route-map", 308, 456, 170, 72, z=30),
                    shape_obj("ls02_macro_zone_3", "route-map", 490, 456, 170, 72, z=30),
                    shape_obj("ls02_macro_now_card", "trigger-row", 341, 440, 132, 44, z=60),
                    shape_obj("ls02_macro_rule_matrix", "trigger-row", 106, 518, 574, 64, z=70),
                    text_obj("ls02_macro_zone_1_body", "body", "观察窗口", 136, 486, 150, 24, z=80),
                    text_obj("ls02_macro_zone_2_body", "body", "确认窗口", 318, 486, 150, 24, z=80),
                    text_obj("ls02_macro_zone_3_body", "body", "部署窗口", 500, 486, 150, 24, z=80),
                ],
            }
            write_ir(ir_path, [slide])

            proc = run_gate(ir_path, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            codes = {i["code"] for i in data["issues"]}
            self.assertIn("ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION", codes)
            self.assertIn("ATLAS_FLOATING_BADGE_COVERS_CARD", codes)

    def test_atlas_route_map_allows_separated_cards_badge_and_bottom_band(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "good-route-map.ir.json"
            report = tmp / "good-route-map.report.json"
            slide = {
                "id": "ls02",
                "objects": [
                    shape_obj("ls02_budget_map_panel", "route-map", 88, 398, 610, 220, z=20),
                    shape_obj("ls02_macro_zone_1", "route-map", 126, 442, 170, 64, z=30),
                    shape_obj("ls02_macro_zone_2", "route-map", 308, 442, 170, 64, z=30),
                    shape_obj("ls02_macro_zone_3", "route-map", 490, 442, 170, 64, z=30),
                    # Small top-right badge overlaps only the card chrome, not the card body.
                    shape_obj("ls02_macro_now_card", "trigger-row", 398, 430, 72, 22, z=60),
                    shape_obj("ls02_macro_rule_matrix", "trigger-row", 106, 528, 574, 44, z=70),
                ],
            }
            write_ir(ir_path, [slide])

            proc = run_gate(ir_path, report)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["release_decision"], "pass")
            self.assertEqual(data.get("engine"), "component_contract_dsl")
            self.assertIn("atlas-route-map", data.get("contracts", []))

    def test_atlas_allocation_map_blocks_orphaned_guardrail_near_footer(self):
        """Page3 failure class: guardrail note sits outside map panel and too close to footer."""
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "bad-guardrail.ir.json"
            report = tmp / "bad-guardrail.report.json"
            slide = {
                "id": "ls03",
                "objects": [
                    shape_obj("ls03_budget_map_panel", "route-map", 88, 398, 610, 186, z=20),
                    shape_obj("ls03_bridge_node_1", "map-node", 196, 462, 36, 36, z=40),
                    shape_obj("ls03_bridge_node_2", "map-node", 386, 462, 36, 36, z=40),
                    shape_obj("ls03_bridge_node_3", "map-node", 576, 462, 36, 36, z=40),
                    text_obj("ls03_bridge_asset_3_limit", "metric-note", "8%", 580, 564, 42, 16, z=80, size=8),
                    text_obj("ls03_guardrail_note", "metric-note", "回撤>5%或周撤>3%：暂停加仓", 120, 596, 420, 16, z=80, size=8),
                    shape_obj("ls03_footer_mask", "footer-mask", 80, 620, 1120, 34, z=888, priority=1),
                    text_obj("ls03_risk", "risk", "风险提示：市场波动可能导致配置建议调整。", 96, 630, 1060, 16, z=900, size=7, priority=4),
                ],
            }
            write_ir(ir_path, [slide])

            proc = run_gate(ir_path, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            codes = {i["code"] for i in data["issues"]}
            self.assertIn("ATLAS_GUARDRAIL_TEXT_ORPHANED", codes)
            self.assertIn("ATLAS_FOOTER_GUARDRAIL_COLLISION", codes)


if __name__ == "__main__":
    unittest.main()
