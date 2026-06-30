#!/usr/bin/env python3
"""Validate controlled glass-fintech visual-anchor variants.

This proves that `glass-fintech-pptx` is a visual anchor family rather than a
single one-off template. Each variant is a 5-slide mini benchmark with different
visual coordinates, while keeping the same anchor DNA, narrative safety,
layout/text safety, editability, and visual fidelity gates.
"""
from __future__ import annotations
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ANCHOR = ROOT / "examples" / "visual-anchors" / "glass-fintech-pptx.anchor.json"
VARIANTS = [
    "sober-committee",
    "luminous-strategy",
    "dense-risk-review",
]
THRESHOLD = 88.0


EXPECTED_VISUAL_GRAMMAR = {
    "sober-committee": {
        "motif": "strict-grid",
        "panel_material": "matte-glass",
        "metric_style": "formal-compact",
        "risk_rail_treatment": "committee-footer",
        "required_roles": {"committee-gridline", "committee-ruler"},
    },
    "luminous-strategy": {
        "motif": "spotlight-orb",
        "panel_material": "luminous-glass",
        "metric_style": "hero-kpi",
        "risk_rail_treatment": "presentation-footer",
        "required_roles": {"luminous-ribbon", "spotlight-orb"},
    },
    "dense-risk-review": {
        "motif": "terminal-grid",
        "panel_material": "dense-cockpit",
        "metric_style": "status-chip",
        "risk_rail_treatment": "monitoring-status-bar",
        "required_roles": {"terminal-gridline", "status-chip"},
    },
}


def check_visual_grammar_realization(ir, variant):
    """Block variants that only declare coordinates but do not alter visual grammar.

    This is intentionally stricter than role-signature checks. It requires the
    compiler to materialize variant-specific grammar in IR fields and object
    roles that will survive PPTX export/rendering.
    """
    deck = ir.get("deck") or {}
    grammar = deck.get("visual_grammar") or {}
    expected = EXPECTED_VISUAL_GRAMMAR[variant]
    for key in ["motif", "panel_material", "metric_style", "risk_rail_treatment"]:
        if grammar.get(key) != expected[key]:
            fail("variant %s has weak coordinate realization: visual_grammar.%s=%r expected %r" % (variant, key, grammar.get(key), expected[key]))
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    missing = sorted(expected["required_roles"] - roles)
    if missing:
        fail("variant %s missing variant-specific visual roles: %s" % (variant, ", ".join(missing)))


def check_cross_variant_distance(results):
    signatures = {}
    for result in results:
        variant = result["variant"]
        ir = load_json(ROOT / "build" / ("glass-fintech-%s" % variant) / ("glass-fintech-%s.ir.json" % variant))
        grammar = ir.get("deck", {}).get("visual_grammar") or {}
        signatures[variant] = (
            grammar.get("motif"),
            grammar.get("panel_material"),
            grammar.get("metric_style"),
            grammar.get("risk_rail_treatment"),
            grammar.get("layout_rhythm"),
        )
    values = list(signatures.values())
    if len(set(values)) != len(values):
        fail("visual variants have duplicate visual grammar signatures: %s" % signatures)
    variants = list(signatures)
    for i, a in enumerate(variants):
        for b in variants[i+1:]:
            distance = sum(1 for x, y in zip(signatures[a], signatures[b]) if x != y)
            if distance < 4:
                fail("VISUAL_VARIANT_DISTANCE_TOO_LOW between %s and %s: distance=%d signatures=%s" % (a, b, distance, signatures))


def fail(msg: str) -> None:
    print("FAIL glass variants: " + msg)
    sys.exit(1)


def run(cmd):
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("command failed: %s\nSTDOUT:\n%s\nSTDERR:\n%s" % (" ".join(map(str, cmd)), proc.stdout, proc.stderr))
    return proc.stdout


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail("invalid JSON %s: %s" % (path, exc))


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def check_contract(contract, variant):
    if contract.get("style_program") != "glass-fintech-pptx":
        fail("variant %s must use glass-fintech-pptx" % variant)
    if contract.get("visual_anchor") != "glass-fintech-pptx":
        fail("variant %s must declare visual_anchor" % variant)
    if contract.get("visual_variant") != variant:
        fail("variant contract visual_variant mismatch: %s" % variant)
    coords = contract.get("visual_coordinates") or {}
    for key in ["luminosity", "panel_density", "accent_energy", "data_prominence", "motif_variation", "compliance_tone"]:
        if not coords.get(key):
            fail("variant %s missing coordinate %s" % (variant, key))
    slides = contract.get("slides", [])
    if len(slides) != 5:
        fail("variant %s must contain exactly 5 slides" % variant)
    if not any(s.get("topology") in {"glass-dashboard", "glass-chart-focus", "glass-table", "glass-matrix", "glass-scenario"} for s in slides):
        fail("variant %s needs at least one evidence/data slide" % variant)
    if not any(s.get("topology") in {"glass-action-rail", "glass-process", "glass-timeline"} or "下一步" in s.get("title", "") for s in slides):
        fail("variant %s needs action/closure slide" % variant)


def check_ir(ir, variant):
    deck = ir.get("deck") or fail("variant %s missing IR deck" % variant)
    if deck.get("visual_variant") != variant:
        fail("IR visual_variant mismatch for %s" % variant)
    slides = deck.get("slides", [])
    if len(slides) != 5:
        fail("IR variant %s must have 5 slides" % variant)
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    if "risk" not in roles or "risk-rail" not in roles:
        fail("variant %s missing risk rail DNA" % variant)
    if "title" not in roles or "body" not in roles:
        fail("variant %s missing native narrative text roles" % variant)
    if not ({"chart", "table", "metric", "matrix-cell", "scenario-card"} & roles):
        fail("variant %s missing data/finance evidence roles" % variant)
    for _, obj in iter_objects(ir):
        if obj.get("type") == "text" and obj.get("editability", {}).get("priority", 0) >= 4:
            if obj.get("render_policy") != "native":
                fail("variant %s priority text not native: %s" % (variant, obj.get("id")))


def validate_variant(variant: str) -> dict:
    contract_path = ROOT / "examples" / "variants" / ("glass-fintech-%s.contract.json" % variant)
    build = ROOT / "build" / ("glass-fintech-%s" % variant)
    build.mkdir(parents=True, exist_ok=True)
    ir_path = build / ("glass-fintech-%s.ir.json" % variant)
    pptx_path = build / ("glass-fintech-%s.pptx" % variant)
    narrative_path = build / ("glass-fintech-%s-narrative-safety-report.json" % variant)
    layout_path = build / ("glass-fintech-%s-layout-safety-report.json" % variant)
    anchor_path = build / ("glass-fintech-%s-visual-anchor-report.json" % variant)
    export_path = build / ("glass-fintech-%s-export-report.json" % variant)
    visual_path = build / ("glass-fintech-%s-visual-fidelity-report.json" % variant)
    qa_path = build / ("glass-fintech-%s-qa-report.json" % variant)

    contract = load_json(contract_path)
    check_contract(contract, variant)
    run([sys.executable, str(ROOT / "scripts" / "check_narrative_safety.py"), str(contract_path), "--report", str(narrative_path)])
    run([sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(contract_path), str(ir_path)])
    ir = load_json(ir_path)
    check_ir(ir, variant)
    check_visual_grammar_realization(ir, variant)
    run([sys.executable, str(ROOT / "scripts" / "check_layout_safety.py"), str(ir_path), "--report", str(layout_path)])
    layout = load_json(layout_path)
    if layout.get("release_decision") != "pass" or layout.get("blocking_count", 0):
        fail("layout safety failed for %s" % variant)
    run([sys.executable, str(ROOT / "scripts" / "check_visual_anchor.py"), str(ANCHOR), str(ir_path), "--report", str(anchor_path)])
    anchor = load_json(anchor_path)
    if anchor.get("release_decision") != "pass":
        fail("visual anchor failed for %s" % variant)
    run([sys.executable, str(ROOT / "scripts" / "export_ir_pptx.py"), str(ir_path), str(pptx_path), "--report", str(export_path)])
    export = load_json(export_path)
    if export.get("release_decision") != "pass" or export.get("blocking_issues"):
        fail("PPTX export audit failed for %s" % variant)
    run([sys.executable, str(ROOT / "scripts" / "run_visual_fidelity.py"), str(ir_path), str(pptx_path), str(visual_path), "--workdir", str(build / "visual-fidelity"), "--threshold", str(THRESHOLD)])
    visual = load_json(visual_path)
    score = visual.get("visual_fidelity", {}).get("overall_score")
    if not isinstance(score, (int, float)) or score < THRESHOLD:
        fail("visual fidelity %.2f below %.2f for %s" % (score or -1, THRESHOLD, variant))
    run([sys.executable, str(ROOT / "scripts" / "run_qa.py"), str(ir_path), str(export_path), str(qa_path), "--pptx", str(pptx_path), "--visual-report", str(visual_path)])
    qa = load_json(qa_path)
    if qa.get("scores", {}).get("editability", 0) < 95:
        fail("QA editability below 95 for %s" % variant)
    return {
        "variant": variant,
        "slides": len(ir["deck"]["slides"]),
        "score": score,
        "editability": qa["scores"]["editability"],
        "layout": layout["release_decision"],
    }


def main():
    results = [validate_variant(v) for v in VARIANTS]
    check_cross_variant_distance(results)
    out = ROOT / "build" / "glass-fintech-variants-summary.json"
    out.write_text(json.dumps({"release_decision": "pass", "variants": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = "; ".join("%s score=%.2f edit=%.2f" % (r["variant"], r["score"], r["editability"]) for r in results)
    print("PASS glass variants count=%d %s" % (len(results), summary))


if __name__ == "__main__":
    main()
