#!/usr/bin/env python3
"""Visual DNA realization gate.

This gate blocks shallow visual systems that declare a style grammar but only
realize it through decoration. It requires each style to materialize information-
bearing components such as metric cards, charts/tables, route maps, guardrails,
and source/risk rails.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STYLE_RULES = {
    "glass-fintech-pptx": {
        "information_roles": {"glass-panel", "metric-card", "metric", "chart", "risk-rail"},
        "must_have_any": [
            {"glass-panel", "metric-card"},
            {"chart", "metric"},
            {"risk-rail", "risk"},
        ],
        "decorative_roles": {"spotlight-orb", "luminous-ribbon", "decorative-ghost-number", "divider", "background"},
    },
    "paper-analyst-report": {
        "information_roles": {"paper-sheet", "ledger-metric", "chart", "table", "research-folio", "analyst-note"},
        "must_have_any": [
            {"paper-sheet", "research-folio"},
            {"ledger-metric", "chart", "table"},
            {"editorial-rule", "analyst-note", "research-folio"},
        ],
        "decorative_roles": {"editorial-rule", "background"},
    },
    "market-atlas-infographic": {
        "information_roles": {"route-map", "signal-field", "scenario-map", "process-state-map", "map-node", "signal-node", "guardrail", "trigger-row"},
        "must_have_any": [
            {"route-map", "signal-field", "scenario-map", "process-state-map"},
            {"map-node", "signal-node", "process-node", "scenario-zone"},
            {"guardrail", "risk", "research-folio"},
        ],
        "decorative_roles": {"atlas-canvas", "atlas-gridline", "route-line", "legend-marker", "background"},
    },
}

CRITICAL_NARRATIVE_ROLES = {"title", "body", "risk"}


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def iter_objects(ir: dict):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def issue(code: str, severity: str, message: str, evidence=None) -> dict:
    return {"code": code, "severity": severity, "message": message, "evidence": evidence or {}}


def check_ir(ir: dict) -> dict:
    deck = ir.get("deck") or {}
    style = deck.get("style_program") or deck.get("visual_anchor") or "unknown"
    rules = STYLE_RULES.get(style)
    issues = []
    objects = [obj for _, obj in iter_objects(ir)]
    roles = {obj.get("role") for obj in objects}
    role_counts = {}
    for obj in objects:
        role_counts[obj.get("role", "")] = role_counts.get(obj.get("role", ""), 0) + 1

    if not rules:
        issues.append(issue("VISUAL_DNA_UNKNOWN_STYLE", "warning", f"No visual DNA rule registered for style {style}", {"style": style}))
        rules = {"information_roles": set(), "must_have_any": [], "decorative_roles": set()}

    grammar = deck.get("visual_system_grammar") or {}
    if not grammar:
        issues.append(issue("VISUAL_DNA_GRAMMAR_MISSING", "blocking", "Deck has no visual_system_grammar declaration"))

    missing_groups = []
    for group in rules["must_have_any"]:
        if not (roles & group):
            missing_groups.append(sorted(group))
    if missing_groups:
        issues.append(issue(
            "VISUAL_DNA_INFORMATION_COMPONENT_MISSING",
            "blocking",
            "Visual DNA lacks required information-bearing component groups",
            {"missing_role_groups": missing_groups, "present_roles": sorted(r for r in roles if r)},
        ))

    information_objects = [obj for obj in objects if obj.get("role") in rules["information_roles"]]
    decorative_objects = [obj for obj in objects if obj.get("role") in rules["decorative_roles"]]
    critical_texts = [obj for obj in objects if obj.get("role") in CRITICAL_NARRATIVE_ROLES]
    priority_info = [obj for obj in information_objects if obj.get("editability", {}).get("priority", 0) >= 3]

    if decorative_objects and len(information_objects) < max(2, len(decorative_objects) // 3):
        issues.append(issue(
            "DECORATION_ONLY_VISUAL_DNA",
            "blocking",
            "Style is realized mainly through decorative objects rather than information-bearing components",
            {"information_count": len(information_objects), "decorative_count": len(decorative_objects)},
        ))

    if not critical_texts:
        issues.append(issue("VISUAL_DNA_NARRATIVE_ROLES_MISSING", "blocking", "Deck lacks critical narrative title/body/risk roles"))

    if len(priority_info) < 2:
        issues.append(issue(
            "VISUAL_DNA_PRIORITY_COMPONENT_TOO_WEAK",
            "blocking",
            "Information-bearing visual DNA must include at least two editable semantic components; critical text remains checked separately as native priority>=4 by export/editability gates",
            {"priority_information_count": len(priority_info)},
        ))

    # Component contract/layout graph evidence is required for Atlas route-map style.
    if style == "market-atlas-infographic":
        refs = set(deck.get("component_contract_refs") or [])
        has_layout_graph = any((slide.get("layout_graph") or {}).get("components") for slide in deck.get("slides", []))
        if "atlas-route-map" not in refs or not has_layout_graph:
            issues.append(issue(
                "VISUAL_DNA_COMPONENT_CONTRACT_EVIDENCE_MISSING",
                "blocking",
                "Atlas DNA must carry component_contract_refs and authored layout_graph evidence",
                {"component_contract_refs": sorted(refs), "has_layout_graph": has_layout_graph},
            ))

    blocking = [i for i in issues if i["severity"] == "blocking"]
    warning = [i for i in issues if i["severity"] == "warning"]
    total_required_groups = max(1, len(rules["must_have_any"]))
    score = max(0.0, 100.0 - 18.0 * len(missing_groups) - 15.0 * len(blocking) - 4.0 * len(warning))
    return {
        "gate": "visual_dna_realization",
        "style_program": style,
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len(warning),
        "realization_score": round(score, 2),
        "evidence": {
            "role_counts": role_counts,
            "information_roles_present": sorted({obj.get("role") for obj in information_objects}),
            "decorative_roles_present": sorted({obj.get("role") for obj in decorative_objects}),
            "required_groups_total": total_required_groups,
            "missing_groups_count": len(missing_groups),
        },
        "issues": issues,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("--report", required=True)
    args = ap.parse_args(argv)
    ir = load_json(args.ir)
    report = check_ir(ir)
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if report["release_decision"] != "pass":
        print("FAIL visual DNA realization", report["blocking_count"])
        return 1
    print("PASS visual DNA realization score=%.2f" % report["realization_score"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
