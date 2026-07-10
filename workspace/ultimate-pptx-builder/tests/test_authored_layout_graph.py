import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AuthoredLayoutGraphTests(unittest.TestCase):
    def test_market_atlas_ir_declares_component_contract_refs_and_authored_layout_graph(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            out = tmp / "atlas.ir.json"
            contract = ROOT / "build" / "visual-system-market-atlas-infographic" / "market-atlas-infographic.contract.json"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(contract), str(out)],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            ir = json.loads(out.read_text(encoding="utf-8"))
            deck = ir["deck"]
            self.assertIn("atlas-route-map", deck.get("component_contract_refs", []))
            by_id = {s["id"]: s for s in deck["slides"]}
            for slide_id in ["ls02", "ls03"]:
                graph = by_id[slide_id].get("layout_graph") or {}
                components = graph.get("components") or []
                self.assertTrue(components, "%s should carry authored layout_graph components" % slide_id)
                self.assertTrue(
                    any(c.get("contract_ref") == "atlas-route-map" for c in components),
                    "%s should reference atlas-route-map contract" % slide_id,
                )
                self.assertTrue(
                    any("slots" in c and c["slots"] for c in components),
                    "%s component graph should declare semantic slots" % slide_id,
                )


if __name__ == "__main__":
    unittest.main()
