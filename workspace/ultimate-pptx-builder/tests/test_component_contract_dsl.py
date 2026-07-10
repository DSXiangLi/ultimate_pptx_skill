import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def shape_obj(oid, role, x, y, w, h, z=1, component=None, priority=3):
    obj = {
        "id": oid,
        "type": "shape",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "editability": {"priority": priority},
        "render_policy": "native",
    }
    if component:
        obj["component"] = component
    return obj


def text_obj(oid, role, text, x, y, w, h, z=10, size=8, component=None, priority=4):
    obj = {
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
    if component:
        obj["component"] = component
    return obj


def write_ir(path, slides):
    path.write_text(
        json.dumps({"deck": {"id": "component-dsl-test", "size": {"w": 1280, "h": 720}, "slides": slides}}, ensure_ascii=False),
        encoding="utf-8",
    )


def write_contract(contract_dir):
    contract_dir.mkdir(parents=True, exist_ok=True)
    contract = {
        "id": "atlas-route-map",
        "version": 1,
        "component_selector": {"role": "route-map", "id_contains": "panel"},
        "slots": [
            {"id": "card_lane", "members": {"id_contains_any": ["_zone_"], "role_any": ["route-map", "map-node"]}},
            {"id": "bottom_band", "members": {"id_contains_any": ["rule_matrix"]}},
            {"id": "status_badge", "members": {"id_contains_any": ["now_card"]}},
            {"id": "guardrail_note", "members": {"id_contains_any": ["guardrail_note"], "type_any": ["text"]}},
            {"id": "footer", "members": {"role_any": ["footer-mask", "risk", "source", "footnote"]}},
        ],
        "rules": [
            {
                "type": "forbid_slot_overlap",
                "code": "ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION",
                "slot_a": "bottom_band",
                "slot_b": "card_lane",
                "min_overlap_h": 6,
                "min_overlap_w_ratio": 0.25,
            },
            {
                "type": "conditional_badge_overlap",
                "code": "ATLAS_FLOATING_BADGE_COVERS_CARD",
                "badge_slot": "status_badge",
                "target_slot": "card_lane",
                "max_body_intrusion": 16,
            },
            {
                "type": "must_be_inside_component",
                "code": "ATLAS_GUARDRAIL_TEXT_ORPHANED",
                "slot": "guardrail_note",
                "pad": 4,
                "only_if_near_component_bottom": {"before": 8, "after": 42},
            },
            {
                "type": "min_gap_between_slots",
                "code": "ATLAS_FOOTER_GUARDRAIL_COLLISION",
                "slot_a": "guardrail_note",
                "slot_b": "footer",
                "axis": "vertical",
                "min_gap": 16,
                "allow_overlap_projection": True,
            },
        ],
    }
    (contract_dir / "atlas-route-map.contract.json").write_text(json.dumps(contract, ensure_ascii=False, indent=2), encoding="utf-8")


def run_dsl_gate(ir_path, contract_dir, report_path):
    return subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_component_contracts.py"),
            str(ir_path),
            "--contracts",
            str(contract_dir),
            "--report",
            str(report_path),
        ],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
    )


class ComponentContractDslTests(unittest.TestCase):
    def test_dsl_contract_blocks_bad_route_map_slots_badge_and_footer_gap(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            contracts = tmp / "contracts"
            write_contract(contracts)
            ir_path = tmp / "bad.ir.json"
            report = tmp / "bad.report.json"
            write_ir(ir_path, [{
                "id": "ls02",
                "objects": [
                    shape_obj("ls02_budget_map_panel", "route-map", 88, 398, 610, 186),
                    shape_obj("ls02_macro_zone_1", "route-map", 126, 456, 170, 72),
                    shape_obj("ls02_macro_zone_2", "route-map", 308, 456, 170, 72),
                    shape_obj("ls02_macro_now_card", "trigger-row", 341, 440, 132, 44),
                    shape_obj("ls02_macro_rule_matrix", "trigger-row", 106, 518, 574, 64),
                    text_obj("ls02_guardrail_note", "metric-note", "回撤>5%或周撤>3%：暂停加仓", 120, 596, 420, 16),
                    shape_obj("ls02_footer_mask", "footer-mask", 80, 620, 1120, 34),
                ],
            }])

            proc = run_dsl_gate(ir_path, contracts, report)
            self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            codes = {i["code"] for i in data["issues"]}
            self.assertIn("ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION", codes)
            self.assertIn("ATLAS_FLOATING_BADGE_COVERS_CARD", codes)
            self.assertIn("ATLAS_GUARDRAIL_TEXT_ORPHANED", codes)
            self.assertIn("ATLAS_FOOTER_GUARDRAIL_COLLISION", codes)

    def test_dsl_contract_accepts_separated_route_map_slots_and_corner_badge(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            contracts = tmp / "contracts"
            write_contract(contracts)
            ir_path = tmp / "good.ir.json"
            report = tmp / "good.report.json"
            write_ir(ir_path, [{
                "id": "ls02",
                "objects": [
                    shape_obj("ls02_budget_map_panel", "route-map", 88, 398, 610, 220),
                    shape_obj("ls02_macro_zone_1", "route-map", 126, 442, 170, 64),
                    shape_obj("ls02_macro_zone_2", "route-map", 308, 442, 170, 64),
                    shape_obj("ls02_macro_now_card", "trigger-row", 398, 430, 72, 22),
                    shape_obj("ls02_macro_rule_matrix", "trigger-row", 106, 548, 574, 52),
                    text_obj("ls02_guardrail_note", "metric-note", "回撤>5%或周撤>3%：暂停加仓", 120, 582, 420, 16),
                    shape_obj("ls02_footer_mask", "footer-mask", 80, 642, 1120, 34),
                ],
            }])

            proc = run_dsl_gate(ir_path, contracts, report)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            data = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(data["release_decision"], "pass")
            self.assertEqual(data["blocking_count"], 0)


if __name__ == "__main__":
    unittest.main()
