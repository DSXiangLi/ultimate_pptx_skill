import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def obj(oid, role, typ="shape", x=0, y=0, w=100, h=40, priority=3):
    return {
        "id": oid,
        "type": typ,
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": priority,
        "editability": {"priority": priority},
        "render_policy": "native",
    }


def deck(style, roles):
    objects = [obj("title", "title", "text", priority=5), obj("risk", "risk", "text", y=620, priority=5)]
    for i, role in enumerate(roles, start=1):
        objects.append(obj(f"{style}_{role}_{i}", role, x=60 + i * 12, y=120 + i * 8, priority=4 if role in {"metric-card", "chart", "table", "route-map", "signal-field", "paper-sheet"} else 3))
    slide = {"id": "s1", "objects": objects}
    deck_obj = {
        "id": style,
        "style_program": style,
        "visual_system_grammar": {"surface": "declared", "composition": "declared", "material": "declared"},
        "slides": [slide],
    }
    if style == "market-atlas-infographic":
        deck_obj["component_contract_refs"] = ["atlas-route-map"]
        slide["layout_graph"] = {
            "source": "authored",
            "components": [
                {"id": "s1_route", "contract_ref": "atlas-route-map", "slots": {"map": [objects[-1]["id"]]}}
            ],
        }
    return {"deck": deck_obj}


class VisualDnaRealizationTests(unittest.TestCase):
    def run_gate(self, ir):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ir_path = tmp / "deck.ir.json"
            report = tmp / "report.json"
            ir_path.write_text(json.dumps(ir, ensure_ascii=False), encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check_visual_dna_realization.py"), str(ir_path), "--report", str(report)],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            return proc, json.loads(report.read_text(encoding="utf-8")) if report.exists() else None

    def test_declared_dna_without_information_bearing_components_fails(self):
        proc, report = self.run_gate(deck("glass-fintech-pptx", ["spotlight-orb", "luminous-ribbon"]))
        self.assertNotEqual(proc.returncode, 0)
        self.assertIsNotNone(report)
        codes = {i["code"] for i in report["issues"]}
        self.assertIn("VISUAL_DNA_INFORMATION_COMPONENT_MISSING", codes)
        self.assertIn("DECORATION_ONLY_VISUAL_DNA", codes)

    def test_each_visual_system_requires_distinct_information_bearing_grammar(self):
        cases = {
            "glass-fintech-pptx": ["glass-panel", "metric-card", "chart", "risk-rail", "spotlight-orb", "luminous-ribbon"],
            "paper-analyst-report": ["paper-sheet", "editorial-rule", "ledger-metric", "chart", "table", "research-folio"],
            "market-atlas-infographic": ["atlas-canvas", "route-map", "signal-field", "map-node", "route-line", "guardrail"],
        }
        for style, roles in cases.items():
            with self.subTest(style=style):
                proc, report = self.run_gate(deck(style, roles))
                self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIsNotNone(report)
                self.assertEqual(report["release_decision"], "pass")
                self.assertGreaterEqual(report["realization_score"], 90)


if __name__ == "__main__":
    unittest.main()
