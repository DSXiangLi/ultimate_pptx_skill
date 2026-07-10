#!/usr/bin/env python3
"""Validate the ultimate-pptx-builder skill skeleton and executable phases.

Dependency-free checks:
- skill authoring contract
- JSON parseability
- IR editability policy
- style program policy
- Phase 1 content-contract → Slide IR compiler
- Phase 2 IR → HTML preview traceability
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "references/architecture.md",
    "references/acceptance-matrix.md",
    "references/authoring-contract.md",
    "references/slide-ir-schema.md",
    "references/editability-policy.md",
    "references/style-program.md",
    "references/pptx-capability-matrix.md",
    "references/qa-loop.md",
    "references/layout-text-safety.md",
    "references/text-spacing-and-alignment-qa.md",
    "references/component-contract-dsl.md",
    "references/authored-layout-graph.md",
    "references/layout-defect-taxonomy.md",
    "references/finance-benchmark-decks.md",
    "references/visual-quality-rubric.md",
    "references/conversion-rules.md",
    "references/implementation-plan.md",
    "references/phase1-ir-compiler.md",
    "references/phase2-html-preview.md",
    "references/phase3-pptx-export.md",
    "references/phase4-qa-report.md",
    "references/phase4b-visual-fidelity.md",
    "references/style-glass-fintech-pptx.md",
    "references/narrative-visual-expansion-roadmap.md",
    "references/narrative-kernel.md",
    "references/visual-anchor-system.md",
    "references/visual-variant-distinctiveness.md",
    "references/visual-system-generalization.md",
    "references/visual-dna-model.md",
    "references/visual-dna-realization-gate.md",
    "docs/learning/README.md",
    "docs/learning/phase4b-visual-rendering.md",
    "docs/learning/glass-fintech-showcase.md",
    "schemas/deck.schema.json",
    "schemas/slide-ir.schema.json",
    "schemas/style-program.schema.json",
    "schemas/qa-report.schema.json",
    "schemas/narrative-kernel.schema.json",
    "schemas/visual-anchor.schema.json",
    "schemas/component-contract.schema.json",
    "examples/minimal-deck.ir.json",
    "examples/swiss-grid-pptx.style.json",
    "examples/glass-fintech-pptx.style.json",
    "examples/paper-analyst-report.style.json",
    "examples/market-atlas-infographic.style.json",
    "examples/content-contract.sample.json",
    "examples/glass-fintech-showcase.contract.json",
    "examples/glass-fintech-benchmark.contract.json",
    "examples/narrative-kernel.finance.json",
    "examples/visual-anchors/glass-fintech-pptx.anchor.json",
    "examples/visual-anchors/paper-analyst-report.anchor.json",
    "examples/visual-anchors/market-atlas-infographic.anchor.json",
    "examples/component-contracts/atlas-route-map.contract.json",
    "examples/variants/glass-fintech-matte-institutional.contract.json",
    "examples/variants/glass-fintech-luminous-glass.contract.json",
    "examples/variants/glass-fintech-terminal-cockpit.contract.json",
    "examples/variants/glass-fintech-visual-language-base.contract.json",
    "scripts/compile_spec_to_ir.py",
    "scripts/render_ir_html.py",
    "scripts/export_ir_pptx.py",
    "scripts/check_pptx_package.py",
    "scripts/run_qa.py",
    "scripts/render_ir_png.py",
    "scripts/render_pptx_png.py",
    "scripts/compare_slide_images.py",
    "scripts/run_visual_fidelity.py",
    "scripts/check_layout_safety.py",
    "scripts/check_text_spacing.py",
    "scripts/check_alignment_graph.py",
    "scripts/check_component_layout_contract.py",
    "scripts/check_component_contracts.py",
    "scripts/check_visual_layout_architecture.py",
    "scripts/check_visual_aesthetic_contract.py",
    "scripts/check_visual_dna_realization.py",
    "scripts/check_narrative_safety.py",
    "scripts/check_visual_anchor.py",
    "scripts/check_narrative_visual_orthogonality.py",
    "scripts/validate_glass_variants.py",
    "scripts/validate_visual_systems.py",
    "scripts/validate_glass_showcase.py",
    "scripts/validate_glass_benchmark.py",
    "tests/test_visual_aesthetic_contract.py",
    "tests/test_pptx_alpha_export.py",
    "tests/test_text_spacing_and_alignment_gates.py",
    "tests/test_component_layout_contract.py",
    "tests/test_component_contract_dsl.py",
    "tests/test_authored_layout_graph.py",
    "tests/test_visual_dna_realization.py",
]
CRITICAL_ROLES = {"title", "body", "risk", "source", "footnote"}


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def check_required_files():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    print(f"PASS required files: {len(REQUIRED)} present")


def check_skill_frontmatter():
    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    m = re.search(r"\n---\n", content[4:])
    if not m:
        fail("SKILL.md frontmatter closing delimiter not found")
    fm_text = content[4:m.start()+4]
    if "name: ultimate-pptx-builder" not in fm_text:
        fail("frontmatter name missing")
    desc = re.search(r"description:\s*(.+)", fm_text)
    if not desc:
        fail("frontmatter description missing")
    if len(desc.group(1)) > 1024:
        fail("description too long")
    if len(content[m.end()+4:].strip()) == 0:
        fail("SKILL.md body empty")
    print("PASS skill frontmatter")


def check_acceptance_language():
    targets = [
        "SKILL.md",
        "references/implementation-plan.md",
        "references/acceptance-matrix.md",
        "references/phase1-ir-compiler.md",
        "references/phase2-html-preview.md",
        "references/phase3-pptx-export.md",
        "references/phase4-qa-report.md",
        "references/layout-text-safety.md",
        "references/text-spacing-and-alignment-qa.md",
        "references/layout-defect-taxonomy.md",
        "references/phase4b-visual-fidelity.md",
        "references/style-glass-fintech-pptx.md",
        "references/narrative-visual-expansion-roadmap.md",
        "references/narrative-kernel.md",
        "references/visual-anchor-system.md",
        "references/visual-variant-distinctiveness.md",
        "references/visual-system-generalization.md",
        "references/visual-dna-model.md",
        "references/qa-loop.md",
        "references/editability-policy.md",
    ]
    for t in targets:
        txt = (ROOT / t).read_text(encoding="utf-8")
        if "Acceptance" not in txt and "验收" not in txt and "Release" not in txt:
            fail(f"{t} lacks acceptance/release criteria")
    print("PASS acceptance criteria present")


def load_json(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid JSON {path}: {e}")


def check_json_files():
    for p in REQUIRED:
        if p.endswith(".json"):
            load_json(p)
    print("PASS JSON parseability")


def iter_objects(ir):
    deck = ir.get("deck") or fail("IR missing deck")
    for slide in deck.get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def validate_ir_policy(ir, label):
    deck = ir.get("deck") or fail(f"{label}: IR missing deck")
    seen_slides = set()
    for slide in deck.get("slides", []):
        sid = slide.get("id")
        if sid in seen_slides:
            fail(f"{label}: duplicate slide id {sid}")
        seen_slides.add(sid)
        seen = set()
        z_values = []
        for obj in slide.get("objects", []):
            oid = obj.get("id")
            if not oid:
                fail(f"{label}: object missing id")
            if oid in seen:
                fail(f"{label}: duplicate object id in {sid}: {oid}")
            seen.add(oid)
            for key in ["type", "role", "box", "z", "editability", "render_policy"]:
                if key not in obj:
                    fail(f"{label}: {oid} missing {key}")
            box = obj["box"]
            if box.get("w", 0) <= 0 or box.get("h", 0) <= 0:
                fail(f"{label}: {oid} has non-positive box")
            z_values.append(obj["z"])
            priority = obj["editability"].get("priority")
            role = obj.get("role")
            if priority >= 4 and obj.get("render_policy") == "raster":
                fail(f"{label}: priority >=4 object cannot be raster: {oid}")
            if role in CRITICAL_ROLES and obj.get("render_policy") == "raster":
                fail(f"{label}: critical role rasterized: {oid}")
            if role in CRITICAL_ROLES and priority < 4:
                fail(f"{label}: critical role priority too low: {oid}")
            if obj.get("type") == "rasterIsland":
                if "source" not in obj:
                    fail(f"{label}: rasterIsland missing source metadata: {oid}")
                forbidden = set(obj.get("must_not_contain", []))
                if not {"title", "body", "risk", "source"}.issubset(forbidden):
                    fail(f"{label}: rasterIsland must exclude critical roles: {oid}")
        if len(z_values) != len(set(z_values)):
            fail(f"{label}: z-order values must be deterministic and unique in slide {sid}")


def check_ir_policy():
    validate_ir_policy(load_json("examples/minimal-deck.ir.json"), "minimal example")
    print("PASS minimal IR policy")


def check_style_policy():
    for style_file in ["examples/swiss-grid-pptx.style.json", "examples/glass-fintech-pptx.style.json"]:
        st = load_json(style_file)["style_program"]
        if len(st.get("base_dna", [])) < 1:
            fail(style_file + " needs at least one base DNA")
        if len(st.get("sota_dna", [])) < 2:
            fail(style_file + " needs at least two SOTA DNA moves")
        if "pptx_material_strategy" not in st:
            fail(style_file + " missing PPTX material strategy")
        if "degradation_rules" not in st:
            fail(style_file + " missing degradation rules")
    print("PASS style policy")


def run_phase1_compiler():
    out = ROOT / "build" / "validation-phase1.ir.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "compile_spec_to_ir.py"),
        str(ROOT / "examples" / "content-contract.sample.json"),
        str(out),
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 1 compiler failed: " + (proc.stderr or proc.stdout))
    try:
        ir = json.loads(out.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"Phase 1 compiler produced invalid JSON: {e}")
    validate_ir_policy(ir, "phase1 compiler output")
    return out, ir


def check_phase1_compiler():
    run_phase1_compiler()
    print("PASS Phase 1 compiler output")


class TraceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ir_ids = []
        self.slide_styles = []
        self.style_text = []
        self._in_style = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "data-ir-id" in attr:
            self.ir_ids.append(attr["data-ir-id"])
        if tag == "section" and attr.get("class") == "slide":
            self.slide_styles.append(attr.get("style", ""))
        if tag == "style":
            self._in_style = True

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False

    def handle_data(self, data):
        if self._in_style:
            self.style_text.append(data)


def check_phase2_html_traceability():
    ir_path, ir = run_phase1_compiler()
    html_path = ROOT / "build" / "validation-preview.html"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "render_ir_html.py"),
        str(ir_path),
        str(html_path),
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 2 HTML renderer failed: " + (proc.stderr or proc.stdout))
    if not html_path.exists():
        fail("Phase 2 HTML renderer did not create output")
    html_text = html_path.read_text(encoding="utf-8")
    parser = TraceParser()
    parser.feed(html_text)
    ir_ids = [obj["id"] for _, obj in iter_objects(ir)]
    html_ids = parser.ir_ids
    missing = sorted(set(ir_ids) - set(html_ids))
    extra = sorted(set(html_ids) - set(ir_ids))
    duplicates = sorted({x for x in html_ids if html_ids.count(x) > 1})
    if missing:
        fail("Phase 2 traceability missing IR IDs in HTML: " + ", ".join(missing))
    if extra:
        fail("Phase 2 traceability has unknown HTML data-ir-id: " + ", ".join(extra))
    if duplicates:
        fail("Phase 2 traceability has duplicate HTML data-ir-id: " + ", ".join(duplicates))
    if len(html_ids) != len(ir_ids):
        fail(f"Phase 2 traceability count mismatch: HTML {len(html_ids)} vs IR {len(ir_ids)}")
    size = ir["deck"].get("size", {"w": 1280, "h": 720})
    expected_w = f"width:{size['w']}px"
    expected_h = f"height:{size['h']}px"
    if not parser.slide_styles:
        fail("Phase 2 preview has no .slide section")
    for style in parser.slide_styles:
        compact = style.replace(" ", "")
        if expected_w not in compact or expected_h not in compact:
            fail("Phase 2 slide size does not match IR size")
    css_text = "\n".join(parser.style_text)
    if re.search(r"(^|[;{\s])content\s*:", css_text):
        fail("Phase 2 preview CSS must not use generated content for meaningful text")
    print("PASS Phase 2 HTML traceability")


def check_phase3_pptx_export():
    ir_path, ir = run_phase1_compiler()
    pptx_path = ROOT / "build" / "validation-deck.pptx"
    report_path = ROOT / "build" / "validation-export-report.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "export_ir_pptx.py"),
        str(ir_path),
        str(pptx_path),
        "--report",
        str(report_path),
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 3 PPTX exporter failed: " + (proc.stderr or proc.stdout))
    if not pptx_path.exists():
        fail("Phase 3 exporter did not create PPTX")
    if not zipfile.is_zipfile(pptx_path):
        fail("Phase 3 PPTX output is not a zip/OPC package")
    pkg_proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_pptx_package.py"), str(pptx_path)], cwd=str(ROOT), text=True, capture_output=True)
    if pkg_proc.returncode != 0:
        fail("Phase 3 PPTX Office package validation failed: " + (pkg_proc.stderr or pkg_proc.stdout))
    with zipfile.ZipFile(pptx_path) as zf:
        names = set(zf.namelist())
        required_parts = {"[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml", "ppt/slides/slide1.xml"}
        missing = sorted(required_parts - names)
        if missing:
            fail("Phase 3 PPTX missing required package parts: " + ", ".join(missing))
        slide_xml = zf.read("ppt/slides/slide1.xml").decode("utf-8")
        for part in ["[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml", "ppt/slides/slide1.xml"]:
            try:
                ET.fromstring(zf.read(part))
            except Exception as e:
                fail(f"Phase 3 PPTX XML part is not parseable ({part}): {e}")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("release_decision") != "pass":
        fail("Phase 3 export report release decision is not pass")
    if report.get("blocking_issues"):
        fail("Phase 3 export report contains blocking issues")
    audit_count = len(report.get("objects_audited", []))
    ir_count = sum(1 for _ in iter_objects(ir))
    if audit_count != ir_count:
        fail(f"Phase 3 audit count mismatch: report {audit_count} vs IR {ir_count}")
    critical_texts = [
        obj.get("text", "")
        for _, obj in iter_objects(ir)
        if obj.get("type") == "text" and (obj.get("role") in CRITICAL_ROLES or obj.get("editability", {}).get("priority", 1) >= 4)
    ]
    for text in critical_texts:
        if text and text not in slide_xml:
            fail("Phase 3 critical text missing from native slide XML: " + text[:40])
    for obj in report.get("objects_audited", []):
        if obj.get("role") in CRITICAL_ROLES or obj.get("priority", 1) >= 4:
            if obj.get("actual") != "native-text" and obj.get("type") == "text":
                fail("Phase 3 critical text is not native-text: " + str(obj.get("id")))
    print("PASS Phase 3 PPTX export audit")


def check_phase4b_visual_fidelity():
    ir_path, _ir = run_phase1_compiler()
    pptx_path = ROOT / "build" / "validation-deck.pptx"
    export_report_path = ROOT / "build" / "validation-export-report.json"
    visual_report_path = ROOT / "build" / "validation-visual-fidelity-report.json"
    export_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "export_ir_pptx.py"),
        str(ir_path),
        str(pptx_path),
        "--report",
        str(export_report_path),
    ]
    proc = subprocess.run(export_cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 4B setup export failed: " + (proc.stderr or proc.stdout))
    visual_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_visual_fidelity.py"),
        str(ir_path),
        str(pptx_path),
        str(visual_report_path),
        "--workdir",
        "build/validation-visual-fidelity",
        "--threshold",
        "70",
    ]
    proc = subprocess.run(visual_cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 4B visual fidelity failed: " + (proc.stderr or proc.stdout))
    report = json.loads(visual_report_path.read_text(encoding="utf-8"))
    vf = report.get("visual_fidelity", {})
    if "overall_score" not in vf or not isinstance(vf["overall_score"], (int, float)):
        fail("Phase 4B report missing numeric overall_score")
    if vf["overall_score"] < 70:
        fail(f"Phase 4B visual score below MVP threshold: {vf['overall_score']}")
    slides = vf.get("slides", [])
    if not slides:
        fail("Phase 4B report has no per-slide metrics")
    for slide in slides:
        for key in ["expected", "actual", "diff"]:
            if not Path(slide[key]).exists():
                fail(f"Phase 4B {key} image missing: {slide[key]}")
    if report.get("release_decision") not in {"pass", "pass_with_accepted_exceptions"}:
        fail("Phase 4B release decision invalid")
    print("PASS Phase 4B visual fidelity")


def check_phase4_qa_report():
    ir_path, _ir = run_phase1_compiler()
    pptx_path = ROOT / "build" / "validation-deck.pptx"
    export_report_path = ROOT / "build" / "validation-export-report.json"
    qa_report_path = ROOT / "build" / "validation-qa-report.json"
    visual_report_path = ROOT / "build" / "validation-visual-fidelity-report.json"
    export_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "export_ir_pptx.py"),
        str(ir_path),
        str(pptx_path),
        "--report",
        str(export_report_path),
    ]
    proc = subprocess.run(export_cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 4 setup export failed: " + (proc.stderr or proc.stdout))
    qa_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "run_qa.py"),
        str(ir_path),
        str(export_report_path),
        str(qa_report_path),
        "--pptx",
        str(pptx_path),
    ]
    if visual_report_path.exists():
        qa_cmd.extend(["--visual-report", str(visual_report_path)])
    proc = subprocess.run(qa_cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("Phase 4 QA script failed: " + (proc.stderr or proc.stdout))
    qa = json.loads(qa_report_path.read_text(encoding="utf-8"))
    for key in ["deck_id", "scores", "blocking_issues", "objects_audited", "release_decision"]:
        if key not in qa:
            fail(f"Phase 4 QA report missing required field: {key}")
    for score_name in ["fidelity", "editability", "design", "practicality"]:
        value = qa["scores"].get(score_name)
        if not isinstance(value, (int, float)) or value < 0 or value > 100:
            fail(f"Phase 4 QA score invalid: {score_name}={value}")
    if qa["blocking_issues"] and qa["release_decision"] == "pass":
        fail("Phase 4 QA report cannot pass with blocking issues")
    if not qa.get("objects_audited"):
        fail("Phase 4 QA report has no audited objects")
    if qa["scores"].get("editability", 0) < 90:
        fail("Phase 4 QA editability score below release threshold")
    if visual_report_path.exists():
        if "visual_fidelity" not in qa:
            fail("Phase 4 QA report missing visual_fidelity section when visual report exists")
        if qa["scores"].get("fidelity") != qa["visual_fidelity"].get("overall_score"):
            fail("Phase 4 QA fidelity score must come from Phase 4B visual report")
    print("PASS Phase 4 QA report")


def check_glass_showcase():
    cmd = [sys.executable, str(ROOT / "scripts" / "validate_glass_showcase.py")]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("glass-fintech showcase failed: " + (proc.stderr or proc.stdout))
    if "PASS glass-fintech showcase" not in proc.stdout:
        fail("glass-fintech showcase validator did not report PASS")
    print("PASS glass-fintech showcase")


def check_glass_benchmark():
    cmd = [sys.executable, str(ROOT / "scripts" / "validate_glass_benchmark.py")]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("glass-fintech benchmark failed: " + (proc.stderr or proc.stdout))
    if "PASS glass benchmark" not in proc.stdout:
        fail("glass-fintech benchmark validator did not report PASS")
    print("PASS glass-fintech benchmark")




def check_narrative_visual_orthogonality():
    cmd = [sys.executable, str(ROOT / "scripts" / "check_narrative_visual_orthogonality.py")]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("narrative/visual orthogonality failed: " + (proc.stderr or proc.stdout))
    if "PASS narrative/visual orthogonality" not in proc.stdout:
        fail("narrative/visual orthogonality checker did not report PASS")
    print("PASS narrative/visual orthogonality")

def check_glass_variants():
    cmd = [sys.executable, str(ROOT / "scripts" / "validate_glass_variants.py")]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("glass-fintech controlled variants failed: " + (proc.stderr or proc.stdout))
    if "PASS glass visual languages" not in proc.stdout:
        fail("glass-fintech visual-language validator did not report PASS")
    print("PASS glass-fintech controlled visual languages")


def check_visual_systems():
    cmd = [sys.executable, str(ROOT / "scripts" / "validate_visual_systems.py")]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("multi-visual-system validation failed: " + (proc.stderr or proc.stdout))
    if "PASS visual systems" not in proc.stdout:
        fail("multi-visual-system validator did not report PASS")
    print("PASS multi-visual-system generalization")


def check_visual_aesthetic_contract_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_visual_aesthetic_contract.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("visual aesthetic contract regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS visual aesthetic contract regression tests")


def check_pptx_alpha_export_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_pptx_alpha_export.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("pptx alpha export regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS pptx alpha export regression tests")

def check_text_spacing_alignment_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_text_spacing_and_alignment_gates.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("text spacing/alignment graph regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS text spacing/alignment graph regression tests")


def check_component_layout_contract_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_component_layout_contract.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("component layout contract regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS component layout contract regression tests")




def check_component_contract_dsl_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_component_contract_dsl.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("component contract DSL regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS component contract DSL regression tests")


def check_authored_layout_graph_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_authored_layout_graph.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("authored layout graph regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS authored layout graph regression tests")


def check_visual_dna_realization_tests():
    cmd = [sys.executable, "-m", "unittest", "tests/test_visual_dna_realization.py", "-v"]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("visual DNA realization regression tests failed: " + (proc.stderr or proc.stdout))
    print("PASS visual DNA realization regression tests")

def main():
    check_required_files()
    check_skill_frontmatter()
    check_acceptance_language()
    check_json_files()
    check_ir_policy()
    check_style_policy()
    check_phase1_compiler()
    check_phase2_html_traceability()
    check_phase3_pptx_export()
    check_phase4b_visual_fidelity()
    check_phase4_qa_report()
    check_glass_showcase()
    check_glass_benchmark()
    check_narrative_visual_orthogonality()
    check_glass_variants()
    check_visual_systems()
    check_visual_aesthetic_contract_tests()
    check_pptx_alpha_export_tests()
    check_text_spacing_alignment_tests()
    check_component_layout_contract_tests()
    check_component_contract_dsl_tests()
    check_authored_layout_graph_tests()
    check_visual_dna_realization_tests()
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
