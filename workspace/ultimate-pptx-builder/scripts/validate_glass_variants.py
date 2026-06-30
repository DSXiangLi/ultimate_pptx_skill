#!/usr/bin/env python3
"""Validate controlled glass-fintech visual-language variants.

This proves that `glass-fintech-pptx` is a visual anchor family rather than a
single one-off template or a set of business-scenario presets.

The important rule: controlled visual-language validation uses the *same*
content contract and the *same* narrative_intent for every run. Only
`visual_language` and visual coordinates change. This prevents narrative
structure from doing the work that visual language should do.
"""
from __future__ import annotations
from pathlib import Path
import copy
import json
import subprocess
import sys
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
ANCHOR = ROOT / "examples" / "visual-anchors" / "glass-fintech-pptx.anchor.json"
BASE_CONTRACT = ROOT / "examples" / "variants" / "glass-fintech-visual-language-base.contract.json"
VISUAL_LANGUAGES = [
    "matte-institutional",
    "luminous-glass",
    "terminal-cockpit",
]
PURE_NARRATIVE_INTENT = "strategy_update"
THRESHOLD = 88.0

CONTROLLED_COORDINATES = {
    "matte-institutional": {
        "luminosity": "sober",
        "panel_density": "medium",
        "accent_energy": "quiet",
        "data_prominence": "table-led",
        "motif_variation": "precision-rules",
        "formality": "formal",
    },
    "luminous-glass": {
        "luminosity": "luminous",
        "panel_density": "medium",
        "accent_energy": "high",
        "data_prominence": "chart-led",
        "motif_variation": "spotlight-orb",
        "formality": "presentation",
    },
    "terminal-cockpit": {
        "luminosity": "dim",
        "panel_density": "dense",
        "accent_energy": "signal-coded",
        "data_prominence": "matrix-led",
        "motif_variation": "terminal-grid",
        "formality": "operational",
    },
}

EXPECTED_VISUAL_GRAMMAR = {
    "matte-institutional": {
        "motif": "strict-grid",
        "panel_material": "matte-glass",
        "metric_style": "formal-compact",
        "footer_treatment": "formal-source-band",
        "required_roles": {"institutional-gridline", "institutional-ruler"},
    },
    "luminous-glass": {
        "motif": "spotlight-orb",
        "panel_material": "luminous-glass",
        "metric_style": "hero-kpi",
        "footer_treatment": "presentation-source-band",
        "required_roles": {"luminous-ribbon", "spotlight-orb"},
    },
    "terminal-cockpit": {
        "motif": "terminal-grid",
        "panel_material": "dense-cockpit",
        "metric_style": "status-chip",
        "footer_treatment": "monitoring-status-bar",
        "required_roles": {"terminal-gridline", "status-chip"},
    },
}


def fail(msg: str) -> NoReturn:
    print("FAIL glass visual languages: " + msg)
    sys.exit(1)


def run(cmd):
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("command failed: %s\nSTDOUT:\n%s\nSTDERR:\n%s" % (" ".join(map(str, cmd)), proc.stdout, proc.stderr))
    return proc.stdout


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail("invalid JSON %s: %s" % (path, exc))


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def build_controlled_contract(visual_language: str) -> dict:
    base = load_json(BASE_CONTRACT)
    contract = copy.deepcopy(base)
    contract["deck_id"] = "glass-fintech-%s-same-content" % visual_language
    contract["style_program"] = "glass-fintech-pptx"
    contract["visual_anchor"] = "glass-fintech-pptx"
    contract["visual_language"] = visual_language
    contract["narrative_intent"] = PURE_NARRATIVE_INTENT
    contract["visual_coordinates"] = CONTROLLED_COORDINATES[visual_language]
    contract.pop("visual_variant", None)
    return contract


def check_base_contract():
    base = load_json(BASE_CONTRACT)
    if base.get("visual_variant"):
        fail("base contract must not use legacy visual_variant")
    if len(base.get("slides", [])) != 5:
        fail("base contract must contain exactly 5 slides")
    if base.get("narrative_intent") != PURE_NARRATIVE_INTENT:
        fail("base contract narrative_intent must be %s" % PURE_NARRATIVE_INTENT)
    slide_fingerprint = json.dumps(base.get("slides", []), ensure_ascii=False, sort_keys=True)
    if not slide_fingerprint:
        fail("base contract has empty slide fingerprint")
    return slide_fingerprint


def check_contract(contract, visual_language, base_fingerprint):
    if contract.get("style_program") != "glass-fintech-pptx":
        fail("%s must use glass-fintech-pptx" % visual_language)
    if contract.get("visual_anchor") != "glass-fintech-pptx":
        fail("%s must declare visual_anchor" % visual_language)
    if contract.get("visual_language") != visual_language:
        fail("contract visual_language mismatch: %s" % visual_language)
    if "visual_variant" in contract:
        fail("%s must not use legacy visual_variant; use visual_language + narrative_intent" % visual_language)
    if contract.get("narrative_intent") != PURE_NARRATIVE_INTENT:
        fail("%s changed narrative_intent during visual-language validation" % visual_language)
    if json.dumps(contract.get("slides", []), ensure_ascii=False, sort_keys=True) != base_fingerprint:
        fail("%s changed slide content/structure; visual-language validation must use identical slides" % visual_language)
    coords = contract.get("visual_coordinates") or {}
    for key in ["luminosity", "panel_density", "accent_energy", "data_prominence", "motif_variation", "formality"]:
        if not coords.get(key):
            fail("%s missing coordinate %s" % (visual_language, key))
    slides = contract.get("slides", [])
    if not any(s.get("topology") in {"glass-dashboard", "glass-chart-focus", "glass-table", "glass-matrix", "glass-scenario"} for s in slides):
        fail("%s needs at least one evidence/data slide" % visual_language)
    if not any(s.get("topology") in {"glass-action-rail", "glass-process", "glass-timeline"} or "下一步" in s.get("title", "") for s in slides):
        fail("%s needs action/closure slide" % visual_language)


def check_ir(ir, visual_language):
    deck = ir.get("deck") or fail("%s missing IR deck" % visual_language)
    if deck.get("visual_language") != visual_language:
        fail("IR visual_language mismatch for %s" % visual_language)
    if deck.get("narrative_intent") != PURE_NARRATIVE_INTENT:
        fail("IR narrative_intent changed for %s" % visual_language)
    slides = deck.get("slides", [])
    if len(slides) != 5:
        fail("IR %s must have 5 slides" % visual_language)
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    if "risk" not in roles or "risk-rail" not in roles:
        fail("%s missing risk rail DNA" % visual_language)
    if "title" not in roles or "body" not in roles:
        fail("%s missing native narrative text roles" % visual_language)
    if not ({"chart", "table", "metric", "matrix-cell", "scenario-card"} & roles):
        fail("%s missing data/finance evidence roles" % visual_language)
    for _, obj in iter_objects(ir):
        if obj.get("type") == "text" and obj.get("editability", {}).get("priority", 0) >= 4:
            if obj.get("render_policy") != "native":
                fail("%s priority text not native: %s" % (visual_language, obj.get("id")))


def check_visual_grammar_realization(ir, visual_language):
    deck = ir.get("deck") or {}
    grammar = deck.get("visual_grammar") or {}
    expected = EXPECTED_VISUAL_GRAMMAR[visual_language]
    for key in ["motif", "panel_material", "metric_style", "footer_treatment"]:
        if grammar.get(key) != expected[key]:
            fail("%s has weak coordinate realization: visual_grammar.%s=%r expected %r" % (visual_language, key, grammar.get(key), expected[key]))
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    missing = sorted(expected["required_roles"] - roles)
    if missing:
        fail("%s missing visual-language-specific roles: %s" % (visual_language, ", ".join(missing)))


def check_same_content_ir(results):
    fingerprints = {}
    for result in results:
        visual_language = result["visual_language"]
        ir = load_json(ROOT / "build" / ("glass-fintech-%s" % visual_language) / ("glass-fintech-%s.ir.json" % visual_language))
        slide_text = []
        for slide in ir.get("deck", {}).get("slides", []):
            texts = []
            for obj in slide.get("objects", []):
                if obj.get("type") == "text" and obj.get("role") in {"kicker", "title", "body", "metric-label", "metric", "metric-note", "risk"}:
                    texts.append((obj.get("role"), obj.get("text")))
            slide_text.append(tuple(texts))
        fingerprints[visual_language] = tuple(slide_text)
    values = list(fingerprints.values())
    if len(set(values)) != 1:
        fail("same-content validation failed: compiled native text fingerprints differ across visual languages")


def check_cross_visual_language_distance(results):
    signatures = {}
    for result in results:
        visual_language = result["visual_language"]
        ir = load_json(ROOT / "build" / ("glass-fintech-%s" % visual_language) / ("glass-fintech-%s.ir.json" % visual_language))
        grammar = ir.get("deck", {}).get("visual_grammar") or {}
        signatures[visual_language] = (
            grammar.get("motif"),
            grammar.get("panel_material"),
            grammar.get("metric_style"),
            grammar.get("footer_treatment"),
            grammar.get("layout_rhythm"),
        )
    values = list(signatures.values())
    if len(set(values)) != len(values):
        fail("visual languages have duplicate visual grammar signatures: %s" % signatures)
    visual_languages = list(signatures)
    for i, a in enumerate(visual_languages):
        for b in visual_languages[i+1:]:
            distance = sum(1 for x, y in zip(signatures[a], signatures[b]) if x != y)
            if distance < 4:
                fail("VISUAL_VARIANT_DISTANCE_TOO_LOW between %s and %s: distance=%d signatures=%s" % (a, b, distance, signatures))


def validate_visual_language(visual_language: str, base_fingerprint: str) -> dict:
    build = ROOT / "build" / ("glass-fintech-%s" % visual_language)
    build.mkdir(parents=True, exist_ok=True)
    contract_path = build / ("glass-fintech-%s.contract.json" % visual_language)
    ir_path = build / ("glass-fintech-%s.ir.json" % visual_language)
    pptx_path = build / ("glass-fintech-%s.pptx" % visual_language)
    narrative_path = build / ("glass-fintech-%s-narrative-safety-report.json" % visual_language)
    layout_path = build / ("glass-fintech-%s-layout-safety-report.json" % visual_language)
    anchor_path = build / ("glass-fintech-%s-visual-anchor-report.json" % visual_language)
    export_path = build / ("glass-fintech-%s-export-report.json" % visual_language)
    visual_path = build / ("glass-fintech-%s-visual-fidelity-report.json" % visual_language)
    qa_path = build / ("glass-fintech-%s-qa-report.json" % visual_language)

    contract = build_controlled_contract(visual_language)
    check_contract(contract, visual_language, base_fingerprint)
    contract_path.write_text(json.dumps(contract, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    run([sys.executable, str(ROOT / "scripts" / "check_narrative_safety.py"), str(contract_path), "--report", str(narrative_path)])
    run([sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(contract_path), str(ir_path)])
    ir = load_json(ir_path)
    check_ir(ir, visual_language)
    check_visual_grammar_realization(ir, visual_language)
    run([sys.executable, str(ROOT / "scripts" / "check_layout_safety.py"), str(ir_path), "--report", str(layout_path)])
    layout = load_json(layout_path)
    if layout.get("release_decision") != "pass" or layout.get("blocking_count", 0):
        fail("layout safety failed for %s" % visual_language)
    run([sys.executable, str(ROOT / "scripts" / "check_visual_anchor.py"), str(ANCHOR), str(ir_path), "--report", str(anchor_path)])
    anchor = load_json(anchor_path)
    if anchor.get("release_decision") != "pass":
        fail("visual anchor failed for %s" % visual_language)
    run([sys.executable, str(ROOT / "scripts" / "export_ir_pptx.py"), str(ir_path), str(pptx_path), "--report", str(export_path)])
    export = load_json(export_path)
    if export.get("release_decision") != "pass" or export.get("blocking_issues"):
        fail("PPTX export audit failed for %s" % visual_language)
    run([sys.executable, str(ROOT / "scripts" / "run_visual_fidelity.py"), str(ir_path), str(pptx_path), str(visual_path), "--workdir", str(build / "visual-fidelity"), "--threshold", str(THRESHOLD)])
    visual = load_json(visual_path)
    score = visual.get("visual_fidelity", {}).get("overall_score")
    if not isinstance(score, (int, float)) or score < THRESHOLD:
        fail("visual fidelity %.2f below %.2f for %s" % (score or -1, THRESHOLD, visual_language))
    run([sys.executable, str(ROOT / "scripts" / "run_qa.py"), str(ir_path), str(export_path), str(qa_path), "--pptx", str(pptx_path), "--visual-report", str(visual_path)])
    qa = load_json(qa_path)
    if qa.get("scores", {}).get("editability", 0) < 95:
        fail("QA editability below 95 for %s" % visual_language)
    return {
        "visual_language": visual_language,
        "narrative_intent": PURE_NARRATIVE_INTENT,
        "same_content_base": str(BASE_CONTRACT.relative_to(ROOT)),
        "slides": len(ir["deck"]["slides"]),
        "score": score,
        "editability": qa["scores"]["editability"],
        "layout": layout["release_decision"],
    }


def main():
    base_fingerprint = check_base_contract()
    results = [validate_visual_language(v, base_fingerprint) for v in VISUAL_LANGUAGES]
    check_same_content_ir(results)
    check_cross_visual_language_distance(results)
    out = ROOT / "build" / "glass-fintech-visual-languages-summary.json"
    out.write_text(json.dumps({"release_decision": "pass", "same_content_base": str(BASE_CONTRACT.relative_to(ROOT)), "variants": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = "; ".join("%s score=%.2f edit=%.2f" % (r["visual_language"], r["score"], r["editability"]) for r in results)
    print("PASS glass visual languages same_content=1 count=%d %s" % (len(results), summary))


if __name__ == "__main__":
    main()
