#!/usr/bin/env python3
"""Executable aesthetic-contract checks for rendered/compiled visual systems.

This is not a substitute for human visual review. It blocks known structural
anti-aesthetic regressions that previously slipped through package/fidelity gates:
- Glass losing its luminous orb DNA and becoming a dark table/grid.
- Atlas using map words and decorative lines without actual route/legend/content semantics.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    print("FAIL visual aesthetic contract: " + msg)
    sys.exit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read {path}: {exc}")
        raise


def iter_objects(ir: dict):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def box_area(obj: dict) -> float:
    b = obj.get("box", {}) or {}
    return float(b.get("w", 0)) * float(b.get("h", 0))


def check_glass(ir: dict) -> list[str]:
    issues: list[str] = []
    deck = ir.get("deck", {})
    if deck.get("style_program") != "glass-fintech-pptx":
        return issues
    visual_language = deck.get("visual_language")
    if visual_language == "matte-institutional":
        issues.append("GLASS_BASELINE_USES_MATTE_VARIANT: cross-system representative must not use the intentionally sober matte variant as the flagship Glass aesthetic")

    orb_objs = []
    grid_objs = []
    panel_objs = []
    for _, obj in iter_objects(ir):
        role = obj.get("role", "")
        if "orb" in role or "glow" in role:
            orb_objs.append(obj)
        if "gridline" in role or "ruler" in role:
            grid_objs.append(obj)
        if role == "glass-panel":
            panel_objs.append(obj)

    large_luminous_orbs = [
        obj for obj in orb_objs
        if box_area(obj) >= 220 * 220 and float(obj.get("opacity", 0)) >= 0.05
    ]
    if len(large_luminous_orbs) < 2:
        issues.append("GLASS_ORB_DNA_COLLAPSED: need at least two large luminous orb/glow objects with area>=220^2 and opacity>=0.05")

    if grid_objs and len(grid_objs) > len(orb_objs) * 2 + 6:
        issues.append("GLASS_GRID_DOMINATES_ORBS: grid/ruler motifs outnumber luminous motifs enough to create dark-table aesthetics")

    if panel_objs:
        avg_panel_opacity = sum(float(o.get("opacity", 1)) for o in panel_objs) / len(panel_objs)
        if avg_panel_opacity < 0.50:
            issues.append("GLASS_PANEL_TOO_FLAT_DIM: average glass panel opacity below 0.50 weakens material presence")
    return issues


def check_atlas(ir: dict) -> list[str]:
    issues: list[str] = []
    deck = ir.get("deck", {})
    if deck.get("style_program") != "market-atlas-infographic":
        return issues

    for slide, obj in iter_objects(ir):
        pass

    for slide in deck.get("slides", []):
        sid = slide.get("id", "")
        objs = slide.get("objects", [])
        roles = [o.get("role", "") for o in objs]
        texts = [o.get("text", "") for o in objs if o.get("type") == "text"]
        map_tiles = [o for o in objs if o.get("role") == "map-tile"]
        route_lines = [o for o in objs if o.get("role") == "route-line" and "source_band" not in o.get("id", "")]
        map_nodes = [o for o in objs if o.get("role") in {"map-node", "process-node"}]
        legends = [t for t in texts if t in {"SIGNAL FIELD", "ALLOCATION ROUTE"}]

        if "ALLOCATION ROUTE" in legends and not route_lines:
            issues.append(f"{sid}: ATLAS_EMPTY_ALLOCATION_ROUTE_LABEL")
        if len(map_tiles) == 3:
            xs = {round((o.get("box", {}) or {}).get("x", 0)) for o in map_tiles}
            ys = {round((o.get("box", {}) or {}).get("y", 0)) for o in map_tiles}
            if len(xs) == 2 and len(ys) == 2:
                issues.append(f"{sid}: ATLAS_INCOMPLETE_TILE_GRID: three map tiles creates an obvious missing fourth tile / unfinished dashboard")
        if len(route_lines) < 2 and not any(r == "chart" for r in roles):
            issues.append(f"{sid}: ATLAS_ROUTE_SEMANTICS_TOO_WEAK: atlas page lacks enough route/path objects to justify map language")
        if len(map_nodes) < max(2, len(route_lines)):
            issues.append(f"{sid}: ATLAS_ROUTE_NODES_TOO_WEAK: route lines are not anchored by enough map/process nodes")

        if sid == "ls02":
            joined_text = "\n".join(texts)
            has_rule_matrix = any(o.get("id", "").endswith("_macro_rule_matrix") for o in objs)
            required_rule_terms = ["SCORE", "STAGE", "ACTION", "ROLLBACK", "政策VETO", "CONFIRM EARLY"]
            missing_terms = [term for term in required_rule_terms if term not in joined_text]
            if not has_rule_matrix:
                issues.append(f"{sid}: ATLAS_MACRO_ROUTE_MISSING_DECISION_RULE_MATRIX: macro route must expose Score/Stage/Action/Rollback, not just staged color bands")
            if missing_terms:
                issues.append(f"{sid}: ATLAS_MACRO_ROUTE_RULE_NOT_AUDITABLE: missing decision-rule terms {missing_terms}")

        if sid == "ls03":
            joined_text = "\n".join(texts)
            has_decision_chain = any("_decision_chain_" in o.get("id", "") for o in objs)
            required_chain_terms = ["Trigger", "Action", "Funding", "Limit", "Guardrail", "DD>5%", "另类现金≥8"]
            missing_terms = [term for term in required_chain_terms if term not in joined_text]
            if not has_decision_chain:
                issues.append(f"{sid}: ATLAS_ALLOCATION_BRIDGE_MISSING_DECISION_CHAIN: allocation page must show Trigger/Action/Funding/Limit/Guardrail, not repeated KPI cards")
            if missing_terms:
                issues.append(f"{sid}: ATLAS_ALLOCATION_GUARDRAIL_NOT_AUDITABLE: missing decision-chain terms {missing_terms}")

    # Palette authority: current mint-only palette is too soft for institutional finance.
    grammar = deck.get("visual_system_grammar", {})
    if grammar.get("chromatic_mode") == "sand-mint-cartographic":
        issues.append("ATLAS_CHROMATIC_MODE_TOO_SOFT: sand/mint dominant palette lacks institutional finance authority")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ir", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    ir = load_json(args.ir)
    issues = check_glass(ir) + check_atlas(ir)
    report = {"release_decision": "fail" if issues else "pass", "blocking_count": len(issues), "blocking_issues": issues}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if issues:
        fail("; ".join(issues[:8]))
    print("PASS visual aesthetic contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
