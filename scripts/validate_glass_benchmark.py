#!/usr/bin/env python3
"""Validate a 15-slide glass-fintech benchmark deck.

This benchmark simulates a realistic finance user input contract, then proves
that the skill can handle narrative structure and multiple content presentation
modes beyond the 3-slide showcase.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "glass-fintech-benchmark"
CONTRACT = ROOT / "examples" / "glass-fintech-benchmark.contract.json"
THRESHOLD = 88.0
REQUIRED_TOPOLOGIES = {
    "glass-cover",
    "glass-hero",
    "glass-dashboard",
    "glass-chart-focus",
    "glass-table",
    "glass-process",
    "glass-matrix",
    "glass-scenario",
    "glass-timeline",
    "glass-quote",
    "glass-compliance",
}

class TraceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "data-ir-id" in attr:
            self.ids.append(attr["data-ir-id"])

def fail(msg):
    print("FAIL glass benchmark: " + msg)
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
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj

def check_contract(contract):
    if contract.get("style_program") != "glass-fintech-pptx":
        fail("benchmark must use glass-fintech-pptx")
    slides = contract.get("slides", [])
    if len(slides) != 15:
        fail("benchmark contract must contain exactly 15 slides")
    tops = {s.get("topology") for s in slides}
    missing = sorted(REQUIRED_TOPOLOGIES - tops)
    if missing:
        fail("benchmark missing topology coverage: " + ", ".join(missing))
    if not contract.get("simulated_user_input"):
        fail("benchmark must include simulated_user_input section")
    if len(contract["simulated_user_input"].get("raw_user_request", "")) < 80:
        fail("simulated raw user request is too shallow")
    if len(contract["simulated_user_input"].get("data_assumptions", [])) < 8:
        fail("simulated input needs realistic data assumptions")
    chart_slides = sum(1 for s in slides if s.get("chart"))
    table_slides = sum(1 for s in slides if s.get("table"))
    if chart_slides < 4:
        fail("benchmark needs at least four chart slides")
    if table_slides < 2:
        fail("benchmark needs at least two table slides")
    for slide in slides:
        if not slide.get("risk_note"):
            fail("each benchmark slide needs risk/source rail: %s" % slide.get("id"))
        if not slide.get("narrative_job"):
            fail("each benchmark slide needs narrative_job: %s" % slide.get("id"))

def check_ir(ir):
    deck = ir.get("deck") or fail("compiled IR missing deck")
    slides = deck.get("slides", [])
    if len(slides) != 15:
        fail("compiled benchmark IR must contain exactly 15 slides")
    roles = set()
    chart_count = table_count = process_count = matrix_count = timeline_count = 0
    for slide in slides:
        ids = set()
        z_values = []
        for obj in slide.get("objects", []):
            oid = obj.get("id")
            if oid in ids:
                fail("duplicate object id %s in %s" % (oid, slide.get("id")))
            ids.add(oid)
            z_values.append(obj.get("z"))
            roles.add(obj.get("role"))
            if obj.get("type") == "rasterIsland":
                fail("benchmark MVP must avoid rasterIsland: %s" % oid)
            if obj.get("editability", {}).get("priority", 0) >= 4 and obj.get("render_policy") == "raster":
                fail("priority >=4 object cannot be raster: %s" % oid)
            if obj.get("type") == "chart":
                chart_count += 1
                if obj.get("render_policy") != "native-vector-group":
                    fail("chart must use native-vector-group: %s" % oid)
            if obj.get("type") == "table":
                table_count += 1
                if obj.get("render_policy") != "native-vector-group":
                    fail("table must use native-vector-group: %s" % oid)
            if obj.get("role") == "process-step":
                process_count += 1
            if obj.get("role") == "matrix-cell":
                matrix_count += 1
            if obj.get("role") == "timeline-step":
                timeline_count += 1
        if len(z_values) != len(set(z_values)):
            fail("z-order values must be unique in slide %s" % slide.get("id"))
    if chart_count < 4:
        fail("compiled benchmark needs at least four chart objects")
    if table_count < 2:
        fail("compiled benchmark needs at least two table objects")
    if process_count < 4:
        fail("compiled benchmark needs process steps")
    if matrix_count < 6:
        fail("compiled benchmark needs matrix cells")
    if timeline_count < 4:
        fail("compiled benchmark needs timeline steps")
    for role in ["title", "body", "risk", "metric", "chart", "table", "process-step", "matrix-cell", "timeline-step", "quote"]:
        if role not in roles:
            fail("missing role coverage in IR: %s" % role)

def check_html_trace(ir, html_path):
    parser = TraceParser()
    parser.feed(Path(html_path).read_text(encoding="utf-8"))
    ir_ids = [obj["id"] for _, obj in iter_objects(ir)]
    if set(ir_ids) != set(parser.ids):
        missing = sorted(set(ir_ids) - set(parser.ids))
        extra = sorted(set(parser.ids) - set(ir_ids))
        fail("HTML trace mismatch missing=%s extra=%s" % (missing[:10], extra[:10]))
    if len(ir_ids) != len(parser.ids):
        fail("HTML trace count mismatch")

def main():
    contract = load_json(CONTRACT)
    check_contract(contract)
    BUILD.mkdir(parents=True, exist_ok=True)
    ir_path = BUILD / "glass-fintech-benchmark.ir.json"
    html_path = BUILD / "glass-fintech-benchmark.html"
    pptx_path = BUILD / "glass-fintech-benchmark.pptx"
    export_report_path = BUILD / "glass-fintech-benchmark-export-report.json"
    visual_report_path = BUILD / "glass-fintech-benchmark-visual-fidelity-report.json"
    layout_report_path = BUILD / "glass-fintech-benchmark-layout-safety-report.json"
    narrative_report_path = BUILD / "glass-fintech-benchmark-narrative-safety-report.json"
    qa_report_path = BUILD / "glass-fintech-benchmark-qa-report.json"
    anchor_report_path = BUILD / "glass-fintech-benchmark-visual-anchor-report.json"
    run([sys.executable, str(ROOT / "scripts" / "check_narrative_safety.py"), str(CONTRACT), "--report", str(narrative_report_path)])
    narrative = load_json(narrative_report_path)
    if narrative.get("release_decision") != "pass" or narrative.get("blocking_count", 0):
        fail("narrative safety gate failed")
    run([sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(CONTRACT), str(ir_path)])
    ir = load_json(ir_path)
    check_ir(ir)
    run([sys.executable, str(ROOT / "scripts" / "check_layout_safety.py"), str(ir_path), "--report", str(layout_report_path)])
    layout = load_json(layout_report_path)
    if layout.get("release_decision") != "pass" or layout.get("blocking_count", 0):
        fail("layout/text safety gate failed")
    run([sys.executable, str(ROOT / "scripts" / "check_visual_anchor.py"), str(ROOT / "examples" / "visual-anchors" / "glass-fintech-pptx.anchor.json"), str(ir_path), "--report", str(anchor_report_path)])
    anchor = load_json(anchor_report_path)
    if anchor.get("release_decision") != "pass" or anchor.get("blocking_count", 0):
        fail("visual anchor gate failed")
    run([sys.executable, str(ROOT / "scripts" / "render_ir_html.py"), str(ir_path), str(html_path)])
    check_html_trace(ir, html_path)
    run([sys.executable, str(ROOT / "scripts" / "export_ir_pptx.py"), str(ir_path), str(pptx_path), "--report", str(export_report_path)])
    export_report = load_json(export_report_path)
    if export_report.get("release_decision") != "pass" or export_report.get("blocking_issues"):
        fail("PPTX export audit failed")
    audits = export_report.get("objects_audited", [])
    if sum(1 for o in audits if o.get("type") == "chart" and o.get("actual") == "editable-vector-chart") < 4:
        fail("export audit needs four editable-vector-chart objects")
    if sum(1 for o in audits if o.get("type") == "table" and o.get("actual") == "editable-vector-table") < 2:
        fail("export audit needs two editable-vector-table objects")
    run([sys.executable, str(ROOT / "scripts" / "run_visual_fidelity.py"), str(ir_path), str(pptx_path), str(visual_report_path), "--workdir", "build/glass-fintech-benchmark/visual-fidelity", "--threshold", str(THRESHOLD)])
    visual = load_json(visual_report_path)
    score = visual.get("visual_fidelity", {}).get("overall_score")
    if not isinstance(score, (int, float)) or score < THRESHOLD:
        fail("visual fidelity %.2f below threshold %.2f" % (score or -1, THRESHOLD))
    run([sys.executable, str(ROOT / "scripts" / "run_qa.py"), str(ir_path), str(export_report_path), str(qa_report_path), "--pptx", str(pptx_path), "--visual-report", str(visual_report_path)])
    qa = load_json(qa_report_path)
    if qa.get("scores", {}).get("editability", 0) < 95:
        fail("QA editability below 95")
    if qa.get("release_decision") not in {"pass", "pass_with_accepted_exceptions"}:
        fail("QA release decision invalid")
    slide_count = len(ir["deck"]["slides"])
    print("PASS glass benchmark slides=%d score=%.2f editability=%.2f layout=%s" % (slide_count, score, qa["scores"]["editability"], layout["release_decision"]))

if __name__ == "__main__":
    main()
