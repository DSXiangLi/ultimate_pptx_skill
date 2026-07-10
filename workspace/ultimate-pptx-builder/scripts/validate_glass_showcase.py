#!/usr/bin/env python3
"""Validate the glass-fintech-pptx end-to-end showcase.

This script is intentionally stricter than the generic validator: it proves one
style line can go from style program + content contract to IR, HTML, PPTX,
visual fidelity artifacts, and QA report.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "glass-fintech-showcase"
THRESHOLD = 88.0


class TraceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "data-ir-id" in attr:
            self.ids.append(attr["data-ir-id"])


def fail(msg):
    print("FAIL glass showcase: " + msg)
    sys.exit(1)


def run(cmd):
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("command failed: %s\nSTDOUT:\n%s\nSTDERR:\n%s" % (" ".join(map(str, cmd)), proc.stdout, proc.stderr))
    return proc.stdout


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        fail("invalid JSON %s: %s" % (path, e))


def iter_objects(ir):
    for slide in ir["deck"].get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def check_inputs():
    style = load_json(ROOT / "examples" / "glass-fintech-pptx.style.json")["style_program"]
    if style.get("id") != "glass-fintech-pptx":
        fail("style id must be glass-fintech-pptx")
    if len(style.get("base_dna", [])) < 3:
        fail("glass style needs at least three Base DNA constraints")
    if len(style.get("sota_dna", [])) < 3:
        fail("glass style needs at least three SOTA DNA moves")
    contract = load_json(ROOT / "examples" / "glass-fintech-showcase.contract.json")
    if contract.get("style_program") != "glass-fintech-pptx":
        fail("showcase contract must use glass-fintech-pptx")
    if len(contract.get("slides", [])) < 3:
        fail("glass showcase must have at least three slides")
    chart_count = 0
    for slide in contract["slides"]:
        if not slide.get("metrics"):
            fail("each glass slide needs metric cards: %s" % slide.get("id"))
        if slide.get("chart"):
            chart_count += 1
        if not slide.get("risk_note"):
            fail("each glass slide needs native risk/source rail: %s" % slide.get("id"))
    if chart_count < 1:
        fail("glass showcase must include at least one financial chart contract")


def check_ir(ir):
    deck = ir.get("deck") or fail("compiled IR missing deck")
    if deck.get("style_program") != "glass-fintech-pptx":
        fail("compiled IR style_program mismatch")
    slides = deck.get("slides", [])
    if len(slides) < 3:
        fail("compiled glass IR must have at least three slides")
    total_objects = 0
    glass_panels = 0
    metric_values = 0
    chart_objects = 0
    for slide in slides:
        ids = set()
        z_values = []
        for obj in slide.get("objects", []):
            total_objects += 1
            oid = obj.get("id")
            if oid in ids:
                fail("duplicate object id %s in %s" % (oid, slide.get("id")))
            ids.add(oid)
            z_values.append(obj.get("z"))
            if obj.get("type") == "rasterIsland":
                fail("glass showcase must avoid rasterIsland in MVP: %s" % oid)
            if obj.get("role") == "glass-panel":
                glass_panels += 1
            if obj.get("role") == "metric":
                metric_values += 1
            if obj.get("type") == "chart":
                chart_objects += 1
                if obj.get("render_policy") != "native-vector-group":
                    fail("glass chart must use native-vector-group render policy: %s" % oid)
                if obj.get("editability", {}).get("priority", 0) < 5:
                    fail("glass chart priority must be 5: %s" % oid)
                if not obj.get("series"):
                    fail("glass chart missing series data: %s" % oid)
            if obj.get("type") == "text" and obj.get("role") in {"title", "body", "risk", "metric", "metric-label", "metric-note"}:
                if obj.get("render_policy") != "native":
                    fail("critical glass text is not native: %s" % oid)
                if obj.get("editability", {}).get("priority", 0) < 4:
                    fail("critical glass text priority too low: %s" % oid)
            if obj.get("type") == "shape" and obj.get("role") in {"glass-panel", "decorative-glow"}:
                if "opacity" not in obj:
                    fail("glass material shape missing opacity: %s" % oid)
        if len(z_values) != len(set(z_values)):
            fail("z-order values must be unique in slide %s" % slide.get("id"))
    if total_objects < 45:
        fail("glass showcase IR too shallow; expected rich object graph")
    if glass_panels < 3:
        fail("glass showcase needs multiple glass panels")
    if metric_values < 9:
        fail("glass showcase needs at least nine metric values")
    if chart_objects < 1:
        fail("glass showcase needs at least one editable chart object")


def check_html_trace(ir, html_path):
    parser = TraceParser()
    parser.feed(Path(html_path).read_text(encoding="utf-8"))
    ir_ids = [obj["id"] for _, obj in iter_objects(ir)]
    if set(ir_ids) != set(parser.ids):
        missing = sorted(set(ir_ids) - set(parser.ids))
        extra = sorted(set(parser.ids) - set(ir_ids))
        fail("HTML trace mismatch missing=%s extra=%s" % (missing, extra))
    if len(ir_ids) != len(parser.ids):
        fail("HTML trace count mismatch")


def main():
    check_inputs()
    BUILD.mkdir(parents=True, exist_ok=True)
    ir_path = BUILD / "glass-fintech-showcase.ir.json"
    html_path = BUILD / "glass-fintech-showcase.html"
    pptx_path = BUILD / "glass-fintech-showcase.pptx"
    export_report_path = BUILD / "glass-fintech-export-report.json"
    aesthetic_report_path = BUILD / "glass-fintech-visual-aesthetic-contract-report.json"
    visual_report_path = BUILD / "glass-fintech-visual-fidelity-report.json"
    qa_report_path = BUILD / "glass-fintech-qa-report.json"
    run([sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(ROOT / "examples" / "glass-fintech-showcase.contract.json"), str(ir_path)])
    ir = load_json(ir_path)
    check_ir(ir)
    run([sys.executable, str(ROOT / "scripts" / "render_ir_html.py"), str(ir_path), str(html_path)])
    check_html_trace(ir, html_path)
    run([sys.executable, str(ROOT / "scripts" / "check_visual_aesthetic_contract.py"), str(ir_path), "--report", str(aesthetic_report_path)])
    aesthetic = load_json(aesthetic_report_path) or {}
    if aesthetic.get("release_decision") != "pass" or aesthetic.get("blocking_count", 0):
        fail("HTML-stage visual aesthetic contract failed")
    run([sys.executable, str(ROOT / "scripts" / "export_ir_pptx.py"), str(ir_path), str(pptx_path), "--report", str(export_report_path)])
    export_report = load_json(export_report_path)
    if export_report.get("release_decision") != "pass" or export_report.get("blocking_issues"):
        fail("PPTX export audit failed")
    chart_audits = [o for o in export_report.get("objects_audited", []) if o.get("type") == "chart"]
    if not chart_audits:
        fail("PPTX export report missing chart audit")
    if any(o.get("actual") != "editable-vector-chart" or not o.get("pass") for o in chart_audits):
        fail("glass chart must export as editable-vector-chart")
    run([
        sys.executable,
        str(ROOT / "scripts" / "run_visual_fidelity.py"),
        str(ir_path),
        str(pptx_path),
        str(visual_report_path),
        "--workdir",
        "build/glass-fintech-showcase/visual-fidelity",
        "--threshold",
        str(THRESHOLD),
    ])
    visual = load_json(visual_report_path)
    score = visual.get("visual_fidelity", {}).get("overall_score")
    if not isinstance(score, (int, float)) or score < THRESHOLD:
        fail("visual fidelity %.2f below threshold %.2f" % (score or -1, THRESHOLD))
    run([
        sys.executable,
        str(ROOT / "scripts" / "run_qa.py"),
        str(ir_path),
        str(export_report_path),
        str(qa_report_path),
        "--pptx",
        str(pptx_path),
        "--visual-report",
        str(visual_report_path),
    ])
    qa = load_json(qa_report_path)
    if qa.get("scores", {}).get("fidelity") != score:
        fail("QA fidelity must equal visual fidelity score")
    if qa.get("scores", {}).get("editability", 0) < 95:
        fail("QA editability below 95")
    if qa.get("release_decision") not in {"pass", "pass_with_accepted_exceptions"}:
        fail("QA release decision invalid")
    print("PASS glass-fintech showcase score=%.2f editability=%.2f" % (score, qa["scores"]["editability"]))


if __name__ == "__main__":
    main()
