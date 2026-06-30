#!/usr/bin/env python3
"""Visual anchor checker for Ultimate PPTX Builder.

The checker verifies that a generated IR expresses a bounded visual anchor rather
than a one-off template: immutable DNA evidence, editability/material policy,
page-role coverage, variant metadata, and anti-template-smell basics.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import sys



EXPECTED_VARIANT_GRAMMAR = {
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

DNA_ROLE_EVIDENCE = {
    "dark institutional finance surface": {"background"},
    "translucent glass panels": {"glass-panel", "metric-card", "risk-rail"},
    "native editable title/body/risk text": {"title", "body", "risk"},
    "editable vector chart/table where data matters": {"chart", "table"},
    "persistent source/risk rail": {"risk-rail", "risk"},
    "data-first financial credibility": {"metric", "chart", "table", "matrix-cell"},
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"FAIL visual anchor: invalid JSON {path}: {exc}")


def issue(code, message, level="blocking"):
    return {"code": code, "level": level, "message": message}


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def check_anchor_schema(anchor_doc):
    issues=[]
    anchor=anchor_doc.get("visual_anchor") or {}
    required=["id","immutable_dna","mutable_coordinates","controlled_visual_languages","mutation_operators","page_role_variants","density_modes","pptx_material_policy","anti_drift","qa_rubric"]
    for k in required:
        if not anchor.get(k):
            issues.append(issue("ANCHOR_FIELD_MISSING", f"visual_anchor missing {k}"))
    if len(anchor.get("immutable_dna", [])) < 4:
        issues.append(issue("WEAK_IMMUTABLE_DNA", "Anchor needs at least four immutable DNA statements."))
    if len(anchor.get("mutable_coordinates", {})) < 3:
        issues.append(issue("WEAK_MUTABLE_COORDINATES", "Anchor needs at least three mutable coordinates."))
    if len(anchor.get("mutation_operators", [])) < 3:
        issues.append(issue("WEAK_MUTATION_OPERATORS", "Anchor needs at least three mutation operators."))
    return issues



def check_variant_grammar(deck, roles):
    issues = []
    variant = deck.get("visual_language") or deck.get("visual_variant")
    if not variant or variant == "default":
        return issues
    expected = EXPECTED_VARIANT_GRAMMAR.get(variant)
    grammar = deck.get("visual_grammar") or {}
    if not expected:
        if not grammar:
            issues.append(issue("WEAK_COORDINATE_REALIZATION", f"Variant {variant!r} declares a visual variant but no visual_grammar."))
        return issues
    for key in ["motif", "panel_material", "metric_style", "footer_treatment"]:
        if grammar.get(key) != expected[key]:
            issues.append(issue("WEAK_COORDINATE_REALIZATION", f"Variant {variant} visual_grammar.{key}={grammar.get(key)!r}; expected {expected[key]!r}."))
    missing = sorted(expected["required_roles"] - roles)
    if missing:
        issues.append(issue("COMPONENT_GRAMMAR_UNCHANGED", f"Variant {variant} missing variant-specific visible roles: {', '.join(missing)}."))
    # Decorative-only changes are not enough: each controlled variant must alter
    # at least one content-bearing component role, not just background glow.
    content_variant_roles = roles & {"status-chip", "luminous-ribbon", "institutional-ruler"}
    if not content_variant_roles:
        issues.append(issue("VISUAL_VARIANT_DISTANCE_TOO_LOW", f"Variant {variant} lacks visible grammar roles beyond generic glass objects."))
    return issues


def check_ir(anchor, ir):
    issues=[]
    deck=ir.get("deck") or {}
    if deck.get("style_program") != anchor.get("id"):
        issues.append(issue("ANCHOR_STYLE_MISMATCH", f"IR style_program {deck.get('style_program')!r} != anchor {anchor.get('id')!r}"))
    roles=set()
    types=set()
    render_policies=set()
    slide_role_signatures=[]
    for slide, obj in iter_objects(ir):
        roles.add(obj.get("role"))
        types.add(obj.get("type"))
        render_policies.add(obj.get("render_policy"))
        if obj.get("editability", {}).get("priority", 0) >= 4 and obj.get("render_policy") == "raster":
            issues.append(issue("CRITICAL_RASTER", f"Critical object rasterized: {obj.get('id')}"))
        if obj.get("type") == "rasterIsland" and obj.get("role") not in {"background", "decorative"}:
            issues.append(issue("NON_DECORATIVE_RASTER", f"Raster island is not decorative: {obj.get('id')}"))
    slides=deck.get("slides", [])
    if not slides:
        issues.append(issue("NO_SLIDES", "IR has no slides."))
    for slide in slides:
        sig=tuple(sorted({obj.get("role") for obj in slide.get("objects", []) if obj.get("role") not in {"background", "decorative-glow", "divider"}}))
        slide_role_signatures.append(sig)
    dna_hits=0
    for dna in anchor.get("immutable_dna", []):
        expected=DNA_ROLE_EVIDENCE.get(dna)
        if expected and expected.intersection(roles):
            dna_hits += 1
        elif not expected:
            # Textual DNA without direct role mapping is considered declared but not machine-evidenced.
            pass
    if dna_hits < 4:
        issues.append(issue("DNA_EVIDENCE_TOO_WEAK", f"Only {dna_hits} machine-evidenced DNA signals found; need >=4."))
    if "risk" not in roles or "risk-rail" not in roles:
        issues.append(issue("MISSING_RISK_RAIL_DNA", "Glass finance anchor requires persistent risk/source rail."))
    if not ({"chart", "table", "metric", "matrix-cell"} & roles):
        issues.append(issue("MISSING_DATA_DNA", "Anchor deck needs finance data objects."))
    if len(slides) >= 5 and len(set(slide_role_signatures)) < 3:
        issues.append(issue("TEMPLATE_SMELL", "Slide role signatures are too repetitive for an anchor family."))
    if not ({"native", "native-vector-group"} <= render_policies or "native-vector-group" in render_policies):
        issues.append(issue("WEAK_MATERIAL_POLICY", "IR should include native and/or editable vector-group material evidence."))
    issues.extend(check_variant_grammar(deck, roles))
    return issues


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("anchor")
    ap.add_argument("ir")
    ap.add_argument("--report")
    args=ap.parse_args()
    anchor_doc=load_json(Path(args.anchor))
    ir=load_json(Path(args.ir))
    anchor=anchor_doc.get("visual_anchor") or {}
    issues=check_anchor_schema(anchor_doc)+check_ir(anchor, ir)
    blocking=[x for x in issues if x.get("level") == "blocking"]
    report={
        "checker":"check_visual_anchor",
        "anchor": str(args.anchor),
        "ir": str(args.ir),
        "issue_count": len(issues),
        "blocking_count": len(blocking),
        "release_decision": "fail" if blocking else "pass",
        "issues": issues,
    }
    if args.report:
        Path(args.report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if blocking:
        print("FAIL visual anchor blocking=%d issues=%d" % (len(blocking), len(issues)))
        for item in blocking[:12]:
            print("- %s: %s" % (item["code"], item["message"]))
        return 1
    print("PASS visual anchor issues=%d" % len(issues))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
