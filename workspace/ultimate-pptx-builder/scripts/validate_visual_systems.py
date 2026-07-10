#!/usr/bin/env python3
"""Validate multi-visual-system generalization.

This gate is stricter than glass-fintech visual-language validation. It proves
that the PPTX builder is not trapped in one dark-glass local optimum by compiling
the same content and same narrative intent through multiple full style anchors.
"""
from __future__ import annotations
from pathlib import Path
import copy
import json
import subprocess
import sys
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
BASE_CONTRACT = ROOT / "examples" / "variants" / "glass-fintech-visual-language-base.contract.json"
NARRATIVE_INTENT = "strategy_update"
THRESHOLD = 86.0
STYLE_SYSTEMS = {
    "glass-fintech-pptx": {
        "visual_language": "luminous-glass",
        "anchor_path": ROOT / "examples" / "visual-anchors" / "glass-fintech-pptx.anchor.json",
        "style_path": ROOT / "examples" / "glass-fintech-pptx.style.json",
        "expected_grammar": {
            "surface": "dark-glass-finance",
            "composition": "dashboard-cards",
            "material": "translucent-glass",
        },
        "required_roles": {"glass-panel", "risk-rail", "spotlight-orb", "luminous-ribbon"},
    },
    "paper-analyst-report": {
        "visual_language": "editorial-ledger",
        "anchor_path": ROOT / "examples" / "visual-anchors" / "paper-analyst-report.anchor.json",
        "style_path": ROOT / "examples" / "paper-analyst-report.style.json",
        "expected_grammar": {
            "surface": "warm-paper-research",
            "composition": "editorial-report-grid",
            "material": "paper-ink",
        },
        "required_roles": {"paper-sheet", "editorial-rule", "research-folio"},
    },
    "market-atlas-infographic": {
        "visual_language": "modular-market-map",
        "anchor_path": ROOT / "examples" / "visual-anchors" / "market-atlas-infographic.anchor.json",
        "style_path": ROOT / "examples" / "market-atlas-infographic.style.json",
        "expected_grammar": {
            "surface": "atlas-map-canvas",
            "composition": "modular-infographic-map",
            "material": "flat-map-tiles",
        },
        "required_roles": {"atlas-canvas", "route-map", "scenario-map", "process-state-map", "route-line", "map-node", "signal-node"},
    },
}


def fail(msg: str) -> NoReturn:
    print("FAIL visual systems: " + msg)
    sys.exit(1)


def run(cmd):
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        fail("command failed: %s\nSTDOUT:\n%s\nSTDERR:\n%s" % (" ".join(map(str, cmd)), proc.stdout, proc.stderr))
    return proc.stdout


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("missing required file: %s" % path.relative_to(ROOT))
    except Exception as exc:
        fail("invalid JSON %s: %s" % (path.relative_to(ROOT), exc))


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def build_contract(style_program: str, config: dict) -> dict:
    base = load_json(BASE_CONTRACT)
    contract = copy.deepcopy(base)
    contract["deck_id"] = "multi-system-%s" % style_program
    contract["style_program"] = style_program
    contract["visual_anchor"] = style_program
    contract["visual_language"] = config["visual_language"]
    contract["narrative_intent"] = NARRATIVE_INTENT
    contract.pop("visual_variant", None)
    return contract


def slide_fingerprint(contract: dict) -> str:
    return json.dumps(contract.get("slides", []), ensure_ascii=False, sort_keys=True)


def required_native_texts(contract: dict) -> dict[str, set[str]]:
    """Critical source texts that every visual system must preserve natively."""
    out: dict[str, set[str]] = {}
    for slide in contract.get("slides", []):
        texts = {slide.get("kicker", ""), slide.get("title", ""), slide.get("risk_note", "")}
        texts.update(slide.get("body", []))
        for metric in slide.get("metrics", []):
            texts.update([metric.get("label", ""), metric.get("value", ""), metric.get("delta", "")])
        for scenario in slide.get("scenarios", []):
            texts.update([scenario.get("name", ""), scenario.get("impact", ""), scenario.get("action", "")])
        for step in slide.get("process", []):
            texts.update([step.get("step", ""), step.get("title", ""), step.get("text", "")])
        out[slide["id"]] = {t for t in texts if t}
    return out


def native_texts_by_slide(ir: dict) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for slide in ir.get("deck", {}).get("slides", []):
        out[slide["id"]] = {
            obj.get("text", "")
            for obj in slide.get("objects", [])
            if obj.get("type") == "text" and obj.get("render_policy") == "native" and obj.get("text")
        }
    return out

def check_contract(contract: dict, style_program: str, base_fingerprint: str):
    if contract.get("style_program") != style_program:
        fail("%s contract style_program mismatch" % style_program)
    if contract.get("visual_anchor") != style_program:
        fail("%s contract visual_anchor mismatch" % style_program)
    if "visual_variant" in contract:
        fail("%s must not use legacy visual_variant" % style_program)
    if contract.get("narrative_intent") != NARRATIVE_INTENT:
        fail("%s changed narrative_intent" % style_program)
    if slide_fingerprint(contract) != base_fingerprint:
        fail("%s changed slide content; multi-system validation must use same content" % style_program)


def check_ir(ir: dict, style_program: str, config: dict):
    deck = ir.get("deck") or fail("%s missing IR deck" % style_program)
    if deck.get("style_program") != style_program:
        fail("%s IR style_program mismatch" % style_program)
    if deck.get("visual_anchor") != style_program:
        fail("%s IR visual_anchor mismatch" % style_program)
    if deck.get("visual_language") != config["visual_language"]:
        fail("%s IR visual_language mismatch" % style_program)
    if deck.get("narrative_intent") != NARRATIVE_INTENT:
        fail("%s IR narrative_intent mismatch" % style_program)
    slides = deck.get("slides", [])
    if len(slides) != 5:
        fail("%s must compile the same 5-slide validation deck" % style_program)
    grammar = deck.get("visual_system_grammar") or {}
    for key, expected in config["expected_grammar"].items():
        if grammar.get(key) != expected:
            fail("%s grammar.%s=%r expected %r" % (style_program, key, grammar.get(key), expected))
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    missing = sorted(config["required_roles"] - roles)
    if missing:
        fail("%s missing style-system roles: %s" % (style_program, ", ".join(missing)))
    if "title" not in roles or "body" not in roles or "risk" not in roles:
        fail("%s missing critical native narrative roles" % style_program)
    for _, obj in iter_objects(ir):
        if obj.get("type") == "text" and obj.get("editability", {}).get("priority", 0) >= 4:
            if obj.get("render_policy") != "native":
                fail("%s priority text not native: %s" % (style_program, obj.get("id")))


def validate_system(style_program: str, config: dict, base_fingerprint: str, expected_texts: dict[str, set[str]]) -> dict:
    for p in [config["anchor_path"], config["style_path"]]:
        load_json(p)
    build = ROOT / "build" / ("visual-system-%s" % style_program)
    build.mkdir(parents=True, exist_ok=True)
    contract_path = build / ("%s.contract.json" % style_program)
    ir_path = build / ("%s.ir.json" % style_program)
    pptx_path = build / ("%s.pptx" % style_program)
    narrative_path = build / ("%s-narrative-safety-report.json" % style_program)
    layout_path = build / ("%s-layout-safety-report.json" % style_program)
    text_spacing_path = build / ("%s-text-spacing-report.json" % style_program)
    alignment_graph_path = build / ("%s-alignment-graph-report.json" % style_program)
    component_layout_path = build / ("%s-component-layout-contract-report.json" % style_program)
    visual_layout_path = build / ("%s-visual-layout-architecture-report.json" % style_program)
    aesthetic_path = build / ("%s-visual-aesthetic-contract-report.json" % style_program)
    export_path = build / ("%s-export-report.json" % style_program)
    visual_path = build / ("%s-visual-fidelity-report.json" % style_program)
    qa_path = build / ("%s-qa-report.json" % style_program)

    contract = build_contract(style_program, config)
    check_contract(contract, style_program, base_fingerprint)
    contract_path.write_text(json.dumps(contract, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    run([sys.executable, str(ROOT / "scripts" / "check_narrative_safety.py"), str(contract_path), "--report", str(narrative_path)])
    run([sys.executable, str(ROOT / "scripts" / "compile_spec_to_ir.py"), str(contract_path), str(ir_path)])
    ir = load_json(ir_path)
    check_ir(ir, style_program, config)
    run([sys.executable, str(ROOT / "scripts" / "check_layout_safety.py"), str(ir_path), "--report", str(layout_path)])
    layout = load_json(layout_path)
    if layout.get("release_decision") != "pass" or layout.get("blocking_count", 0):
        fail("%s layout safety failed: %s" % (style_program, layout_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "check_text_spacing.py"), str(ir_path), "--report", str(text_spacing_path)])
    text_spacing = load_json(text_spacing_path)
    if text_spacing.get("release_decision") != "pass" or text_spacing.get("blocking_count", 0):
        fail("%s text spacing failed: %s" % (style_program, text_spacing_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "check_alignment_graph.py"), str(ir_path), "--report", str(alignment_graph_path)])
    alignment_graph = load_json(alignment_graph_path)
    if alignment_graph.get("release_decision") != "pass" or alignment_graph.get("blocking_count", 0):
        fail("%s alignment graph failed: %s" % (style_program, alignment_graph_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "check_component_layout_contract.py"), str(ir_path), "--report", str(component_layout_path)])
    component_layout = load_json(component_layout_path)
    if component_layout.get("release_decision") != "pass" or component_layout.get("blocking_count", 0):
        fail("%s component layout contract failed: %s" % (style_program, component_layout_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "check_visual_layout_architecture.py"), str(ir_path), "--report", str(visual_layout_path)])
    visual_layout = load_json(visual_layout_path)
    if visual_layout.get("release_decision") != "pass" or visual_layout.get("blocking_count", 0):
        fail("%s visual layout architecture failed: %s" % (style_program, visual_layout_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "check_visual_aesthetic_contract.py"), str(ir_path), "--report", str(aesthetic_path)])
    aesthetic = load_json(aesthetic_path)
    if aesthetic.get("release_decision") != "pass" or aesthetic.get("blocking_count", 0):
        fail("%s visual aesthetic contract failed: %s" % (style_program, aesthetic_path.relative_to(ROOT)))
    run([sys.executable, str(ROOT / "scripts" / "export_ir_pptx.py"), str(ir_path), str(pptx_path), "--report", str(export_path)])
    run([sys.executable, str(ROOT / "scripts" / "check_pptx_package.py"), str(pptx_path)])
    export = load_json(export_path)
    if export.get("critical_raster_count"):
        fail("%s has critical rasterized objects" % style_program)
    run([sys.executable, str(ROOT / "scripts" / "run_visual_fidelity.py"), str(ir_path), str(pptx_path), str(visual_path), "--workdir", str(build / "visual-fidelity"), "--threshold", str(THRESHOLD)])
    visual = load_json(visual_path)
    score = visual.get("visual_fidelity", {}).get("overall_score", 0)
    if score < THRESHOLD:
        fail("%s visual fidelity below threshold: %.2f" % (style_program, score))
    run([sys.executable, str(ROOT / "scripts" / "run_qa.py"), str(ir_path), str(export_path), str(qa_path), "--pptx", str(pptx_path), "--visual-report", str(visual_path)])
    qa = load_json(qa_path)
    edit_score = qa.get("scores", {}).get("editability", 0)
    if edit_score < 95:
        fail("%s editability below 95: %.2f" % (style_program, edit_score))
    native_texts = native_texts_by_slide(ir)
    for slide_id, required in expected_texts.items():
        missing = sorted(required - native_texts.get(slide_id, set()))
        if missing:
            fail("%s missing required native same-content text on %s: %s" % (style_program, slide_id, missing[:5]))
    return {"style_program": style_program, "score": float(score), "editability": float(edit_score)}



def obj_box(obj: dict) -> dict:
    return obj.get("box", {}) or {}


def rounded_ratio(value: float) -> float:
    return round(float(value), 2)


def visual_dna_signature(ir: dict) -> dict:
    """Extract visual DNA from actual IR objects, not declarations.

    This intentionally inspects charts, typography, cards/components, and layout
    skeletons so style systems cannot pass by changing only background/surface.
    """
    title_sizes = []
    title_widths = []
    body_sizes = []
    metric_sizes = []
    fonts = set()
    chart_styles = []
    chart_boxes = []
    atlas_viz_shapes = []
    atlas_viz_palette = []
    card_shapes = []
    card_boxes = []
    role_counts = {}
    title_xs = []
    metric_xs = []
    process_xs = []
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            role = obj.get("role", "")
            role_counts[role] = role_counts.get(role, 0) + 1
            box = obj_box(obj)
            if obj.get("type") == "text":
                style = obj.get("style", {})
                if style.get("font"):
                    fonts.add(style.get("font"))
                if role == "title":
                    title_sizes.append(style.get("size"))
                    title_widths.append(box.get("w"))
                    title_xs.append(box.get("x"))
                elif role in {"body", "risk", "kicker"}:
                    body_sizes.append(style.get("size"))
                elif role in {"metric", "metric-label", "metric-note"}:
                    metric_sizes.append(style.get("size"))
            elif obj.get("type") == "chart":
                st = obj.get("style", {})
                chart_styles.append((
                    st.get("font"),
                    st.get("title_color"),
                    st.get("label_color"),
                    st.get("grid_color"),
                    st.get("panel_fill"),
                    st.get("panel_stroke"),
                    st.get("chart_treatment"),
                    tuple(st.get("series_palette", [])),
                    st.get("axis_style"),
                    st.get("legend_style"),
                    st.get("marker_style"),
                ))
                chart_boxes.append((box.get("x"), box.get("y"), box.get("w"), box.get("h")))
            elif obj.get("type") == "shape" and role in {"route-map", "scenario-map", "process-state-map", "asset-allocation-band", "scenario-zone", "trigger-row", "route-line", "map-node", "signal-chip", "process-node", "guardrail"}:
                if role in {"asset-allocation-band", "scenario-zone", "trigger-row", "route-line", "map-node", "signal-chip", "process-node", "guardrail"} and obj.get("fill"):
                    atlas_viz_palette.append(obj.get("fill"))
                if role in {"route-map", "scenario-map", "process-state-map"}:
                    atlas_viz_shapes.append((role, obj.get("shape"), obj.get("fill"), obj.get("stroke"), obj.get("opacity"), obj.get("stroke_opacity")))
                    chart_boxes.append((box.get("x"), box.get("y"), box.get("w"), box.get("h")))
            elif obj.get("type") == "shape" and role in {"glass-panel", "ledger-metric", "map-tile", "signal-chip", "supporting-card", "process-step"}:
                card_shapes.append((role, obj.get("shape"), obj.get("fill"), obj.get("stroke"), obj.get("opacity"), obj.get("stroke_opacity"), bool(obj.get("shadow"))))
                card_boxes.append((role, box.get("w"), box.get("h")))
                if role in {"ledger-metric", "map-tile"}:
                    metric_xs.append(box.get("x"))
                if role == "process-step":
                    process_xs.append(box.get("x"))
    def avg(vals):
        vals = [v for v in vals if isinstance(v, (int, float))]
        return rounded_ratio(sum(vals) / len(vals)) if vals else None
    if atlas_viz_shapes:
        # Treat semantic native Atlas maps as data-viz DNA. This prevents the gate
        # from forcing Atlas back into ordinary chart objects when route maps,
        # scenario zones, and state machines are the stronger visual language.
        chart_styles.extend(
            ("native-atlas-map", role, shape, fill, stroke, opacity, stroke_opacity, tuple(sorted(set(atlas_viz_palette))), "coordinate-route", "atlas-legend", "semantic-node")
            for role, shape, fill, stroke, opacity, stroke_opacity in atlas_viz_shapes
        )
    return {
        "font_set": tuple(sorted(fonts)),
        "title_size_avg": avg(title_sizes),
        "title_width_avg": avg(title_widths),
        "body_size_avg": avg(body_sizes),
        "metric_size_avg": avg(metric_sizes),
        "chart_styles": tuple(sorted(set(chart_styles))),
        "chart_boxes": tuple(sorted(set(chart_boxes))),
        "card_shapes": tuple(sorted(set(card_shapes))),
        "card_boxes": tuple(sorted(set(card_boxes))),
        "role_counts": tuple(sorted(role_counts.items())),
        "layout_signature": (
            avg(title_xs),
            avg(metric_xs),
            avg(process_xs),
            len(set(chart_boxes)),
            len(set(card_boxes)),
        ),
    }


def dna_distance(a: dict, b: dict) -> int:
    keys = [
        "font_set",
        "title_size_avg",
        "title_width_avg",
        "body_size_avg",
        "metric_size_avg",
        "chart_styles",
        "chart_boxes",
        "card_shapes",
        "card_boxes",
        "layout_signature",
    ]
    return sum(1 for key in keys if a.get(key) != b.get(key))


def check_visual_dna_depth(results: list[dict]):
    signatures = {}
    for result in results:
        style_program = result["style_program"]
        ir = load_json(ROOT / "build" / ("visual-system-%s" % style_program) / ("%s.ir.json" % style_program))
        sig = visual_dna_signature(ir)
        signatures[style_program] = sig
        chart_styles = sig.get("chart_styles", ())
        if not chart_styles:
            fail("%s missing chart DNA evidence" % style_program)
        if all(len(style) >= 8 and not style[7] for style in chart_styles):
            fail("%s chart DNA missing series_palette evidence" % style_program)
    systems = list(signatures)
    for i, a in enumerate(systems):
        for b in systems[i + 1:]:
            dist = dna_distance(signatures[a], signatures[b])
            if dist < 8:
                fail("VISUAL_DNA_DISTANCE_TOO_LOW between %s and %s: distance=%d signatures=%s" % (a, b, dist, signatures))
            if signatures[a].get("chart_styles") == signatures[b].get("chart_styles"):
                fail("CHART_DNA_UNCHANGED between %s and %s" % (a, b))
            if signatures[a].get("font_set") == signatures[b].get("font_set") and signatures[a].get("title_size_avg") == signatures[b].get("title_size_avg"):
                fail("TYPOGRAPHY_DNA_UNCHANGED between %s and %s" % (a, b))
            if signatures[a].get("card_shapes") == signatures[b].get("card_shapes"):
                fail("CONTAINER_DNA_UNCHANGED between %s and %s" % (a, b))

def check_cross_system_distance(results: list[dict]):
    grammars = {}
    for result in results:
        style_program = result["style_program"]
        ir = load_json(ROOT / "build" / ("visual-system-%s" % style_program) / ("%s.ir.json" % style_program))
        grammar = ir.get("deck", {}).get("visual_system_grammar") or {}
        grammars[style_program] = (grammar.get("surface"), grammar.get("composition"), grammar.get("material"), grammar.get("chromatic_mode"), grammar.get("container_grammar"))
    values = list(grammars.values())
    if len(set(values)) != len(values):
        fail("style systems have duplicate visual-system grammar signatures: %s" % grammars)
    systems = list(grammars)
    for i, a in enumerate(systems):
        for b in systems[i + 1:]:
            distance = sum(1 for x, y in zip(grammars[a], grammars[b]) if x != y)
            if distance < 4:
                fail("VISUAL_SYSTEM_DISTANCE_TOO_LOW between %s and %s: %s" % (a, b, grammars))


def main():
    base = load_json(BASE_CONTRACT)
    if base.get("narrative_intent") != NARRATIVE_INTENT:
        fail("base narrative_intent must remain %s" % NARRATIVE_INTENT)
    base_fingerprint = slide_fingerprint(base)
    expected_texts = required_native_texts(base)
    results = []
    for style_program, config in STYLE_SYSTEMS.items():
        results.append(validate_system(style_program, config, base_fingerprint, expected_texts))
    check_cross_system_distance(results)
    check_visual_dna_depth(results)
    print("PASS visual systems same_content=1 count=%d %s" % (len(results), "; ".join("%s score=%.2f edit=%.2f" % (r["style_program"], r["score"], r["editability"]) for r in results)))


if __name__ == "__main__":
    main()
