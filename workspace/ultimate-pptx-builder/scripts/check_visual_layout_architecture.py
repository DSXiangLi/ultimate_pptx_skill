#!/usr/bin/env python3
"""Visual layout architecture gate.

This gate complements geometric layout safety. It catches systemic visual-layout
failures that can pass overlap/text-capacity checks but still produce weak PPTX:
route/title intrusion, process-page density overload, chart undersizing, and
style-DNA/page-intent hierarchy mismatch.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CRITICAL_ROLES = {"title", "body", "metric", "metric-label", "metric-note", "process-step", "chart", "table", "risk"}
DECORATIVE_ROUTE_IDS = {"source_band"}
SEMANTIC_ATLAS_ROUTE_TOKENS = (
    "_budget_route_",
    "_macro_route_",
    "_bridge_route_",
    "_state_route_",
    "_scenario_branch_",
    "_allocation_route_spine",
    "_decision_route_",
)


def is_semantic_atlas_route(obj):
    oid = obj.get("id", "")
    return any(tok in oid for tok in SEMANTIC_ATLAS_ROUTE_TOKENS) or obj.get("role") in {
        "semantic-route",
        "scenario-branch",
    }


def is_decorative_atlas_motif(obj):
    """Background motif only; excludes business routes/state nodes.

    Earlier gates treated any id containing `_node_1` as decorative. That became
    wrong once Atlas grew semantic state-machine nodes such as `state_node_1`.
    """
    oid = obj.get("id", "")
    if obj.get("role") == "atlas-gridline":
        return True
    if any(tok in oid for tok in ["_route_primary", "_route_secondary"]):
        return True
    if any(oid.endswith(tok) for tok in ["_node_1", "_node_2", "_node_3"]):
        return not any(
            semantic in oid
            for semantic in [
                "_state_node_",
                "_bridge_node_",
                "_budget_station_",
                "_macro_station_",
                "_scenario_zone_",
                "_decision_node_",
            ]
        )
    return False


def box(o):
    return o.get("box", {}) or {}


def right(b):
    return float(b.get("x", 0)) + float(b.get("w", 0))


def bottom(b):
    return float(b.get("y", 0)) + float(b.get("h", 0))


def area(b):
    return max(0.0, float(b.get("w", 0))) * max(0.0, float(b.get("h", 0)))


def intersects(a, b, pad=0.0):
    return not (
        right(a) <= float(b.get("x", 0)) - pad
        or right(b) <= float(a.get("x", 0)) - pad
        or bottom(a) <= float(b.get("y", 0)) - pad
        or bottom(b) <= float(a.get("y", 0)) - pad
    )


def style_size(o):
    return float((o.get("style") or {}).get("size", 0) or 0)


def load_deck(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("deck", data)


def slide_roles(slide):
    out = {}
    for o in slide.get("objects", []):
        out[o.get("role")] = out.get(o.get("role"), 0) + 1
    return out


def issue(issues, deck, slide, code, severity, message, obj_id=None, classification="C", prevention=None):
    issues.append({
        "deck": deck.get("id"),
        "visual_anchor": deck.get("visual_anchor") or deck.get("style_program"),
        "slide": slide.get("id"),
        "code": code,
        "severity": severity,
        "class": classification,
        "object_id": obj_id,
        "message": message,
        "prevention": prevention or "Add layout-architecture gate or style-DNA grammar variant.",
    })


def check_deck(deck):
    issues = []
    style = deck.get("visual_anchor") or deck.get("style_program") or ""
    for slide in deck.get("slides", []):
        objects = slide.get("objects", [])
        roles = slide_roles(slide)
        titles = [o for o in objects if o.get("role") == "title"]
        title = titles[0] if titles else None
        title_safe = None
        if title:
            tb = box(title)
            title_safe = {
                "x": float(tb.get("x", 0)) - 8,
                "y": float(tb.get("y", 0)) - 8,
                "w": float(tb.get("w", 0)) + 16,
                "h": float(tb.get("h", 0)) + 24,
            }

        # Atlas routes are information-bearing motifs, but decorative routes must not enter title safe zones.
        if "market-atlas" in style and title_safe:
            for o in objects:
                if o.get("role") == "route-line" and not any(tok in o.get("id", "") for tok in DECORATIVE_ROUTE_IDS):
                    b = box(o)
                    if intersects(b, title_safe, pad=0):
                        issue(
                            issues, deck, slide,
                            "ROUTE_TITLE_SAFE_AREA_INTRUSION", "blocking",
                            "Route/node motif enters the title safe area; this is a style-DNA adaptation bug, not a local polish issue.",
                            o.get("id"), "B",
                            "Routes must be clipped, shifted, faded, or masked around title/subtitle zones.",
                        )


        # Atlas content-zone masks must sit above decorative background motifs.
        # If they are below grids/routes, opacity changes only tint the page and
        # cannot actually prevent route/grid bleed-through inside content regions.
        if "market-atlas" in style:
            motif_z = [float(o.get("z", 0)) for o in objects if is_decorative_atlas_motif(o)]
            max_motif_z = max(motif_z) if motif_z else 0.0
            for zone in [o for o in objects if o.get("role") == "background" and any(o.get("id", "").endswith(suffix) for suffix in ["_zone_left", "_zone_right", "_zone_bottom"] )]:
                if float(zone.get("z", 0)) <= max_motif_z:
                    issue(
                        issues, deck, slide,
                        "ATLAS_CONTENT_MASK_BELOW_MOTIF", "blocking",
                        f"Atlas content mask z={zone.get('z')} is below/inside decorative motif z={max_motif_z:.0f}; it cannot block grid/route bleed-through.",
                        zone.get("id"), "S",
                        "Place content masks above decorative grids/routes and below business text/cards, or clip motifs away from content zones.",
                    )
            risks = [o for o in objects if o.get("role") == "risk"]
            footer_masks = [o for o in objects if o.get("role") == "footer-mask"]
            for risk in risks:
                rb = box(risk)
                protected = any(intersects(box(m), rb, pad=-4) and float(m.get("z", 0)) < float(risk.get("z", 0)) and float(m.get("opacity", 0) or 0) >= 0.75 for m in footer_masks)
                if not protected:
                    issue(
                        issues, deck, slide,
                        "ATLAS_FOOTER_UNMASKED", "blocking",
                        "Atlas risk/footer text lacks a strong footer-mask, so bottom grid/routes can bleed through compliance text.",
                        risk.get("id"), "S",
                        "Add a dedicated footer-mask above decorative motifs and below risk/source text.",
                    )

        # Decorative layer must stay subordinate to content. Strong map grids/routes
        # and large glows can pass geometry checks while still making the slide feel
        # chaotic or non-design intentional.
        for o in objects:
            role = o.get("role")
            oid = o.get("id", "")
            op = float(o.get("opacity", 1.0) if o.get("opacity", 1.0) is not None else 1.0)
            b = box(o)
            if "market-atlas" in style and role == "background" and (oid.endswith("_zone_left") or oid.endswith("_zone_bottom")) and op < 0.28:
                issue(
                    issues, deck, slide,
                    "ATLAS_CONTENT_ZONE_UNDERMASKED", "blocking",
                    f"Atlas content isolation zone opacity {op:.2f} is too low; grid/routes will bleed through content regions.",
                    oid, "S",
                    "Do not solve atlas visual noise by fading the content mask. Keep content zones >=0.28 opacity and fade/clamp decorative routes instead.",
                )
            if "market-atlas" in style and role == "atlas-gridline" and op > 0.085:
                issue(
                    issues, deck, slide,
                    "ATLAS_GRID_TOO_PROMINENT", "blocking",
                    f"Atlas gridline opacity {op:.2f} exceeds strict readability threshold; background grid is competing with content.",
                    oid, "S",
                    "Map grids must be atmospheric (<0.085 opacity) unless clipped away from content zones.",
                )
            if "market-atlas" in style and role == "route-line" and "source_band" not in oid and not is_semantic_atlas_route(o) and op > 0.26:
                issue(
                    issues, deck, slide,
                    "ATLAS_ROUTE_TOO_PROMINENT", "blocking",
                    f"Atlas route opacity {op:.2f} is too prominent for a decorative/infrastructure line.",
                    oid, "S",
                    "Decorative routes must stay below content hierarchy or become semantic connectors only.",
                )
            if "glass-fintech" in style and role in {"decorative-glow", "spotlight-orb"}:
                if area(b) > 36000 and op > 0.035 and title_safe and intersects(b, title_safe, pad=-20):
                    issue(
                        issues, deck, slide,
                        "GLASS_GLOW_COMPETES_WITH_TITLE", "blocking",
                        f"Large glow area={area(b):.0f} opacity={op:.2f} competes with the title safe area.",
                        oid, "S",
                        "Reduce glow size/opacity or move it outside title safe zones.",
                    )
            if role == "risk":
                if style_size(o) and style_size(o) < 9:
                    issue(issues, deck, slide, "FOOTER_TEXT_TOO_SMALL", "blocking", "Risk/source footer text below 9px is not acceptable for finance PPT review.", oid, "S", "Use >=9px footer text or shorten the note.")
                if bottom(b) > 662:
                    issue(issues, deck, slide, "FOOTER_SAFE_ZONE_TOO_LOW", "blocking", "Risk/source footer exceeds strict bottom safe zone.", oid, "S", "Keep risk/source text above y=662 in 16:9 canvas.")

        # Chart pages must allocate enough physical area for axis/legend labels.
        for o in objects:
            if o.get("type") == "chart" or o.get("role") == "chart":
                a = area(box(o))
                if a < 95_000:
                    issue(
                        issues, deck, slide,
                        "CHART_AREA_TOO_SMALL_FOR_EDITABLE_LABELS", "blocking",
                        f"Chart area {a:.0f}px is below the minimum for readable editable axis/legend labels.",
                        o.get("id"), "C",
                        "Use a chart-led page variant, enlarge the chart, or reduce competing KPI/card modules.",
                    )

        # Process pages with process text plus many metric/map cards are density failures.
        process_text = roles.get("process-step", 0)
        card_count = sum(roles.get(r, 0) for r in ["metric-card", "map-tile", "ledger-metric", "scenario-card", "analyst-note"])
        route_count = roles.get("route-line", 0)
        if process_text >= 12 and card_count >= 6:
            issue(
                issues, deck, slide,
                "PROCESS_PAGE_CONTENT_BUDGET_EXCEEDED", "blocking",
                f"Process page has {process_text} process text objects and {card_count} content cards; this exceeds one-slide density budget.",
                None, "C",
                "Use a dedicated process/checklist/route layout variant, reduce secondary KPI cards, or split the page.",
            )
        if "market-atlas" in style and process_text >= 12 and route_count >= 12:
            issue(
                issues, deck, slide,
                "ATLAS_PROCESS_ROUTE_COMPLEXITY_TOO_HIGH", "blocking",
                f"Atlas process page has {route_count} route-line objects; routes are competing with process content.",
                None, "B",
                "Process routes should be semantic and sparse; hide decorative routes and keep only essential connectors.",
            )

        # Microtext: non-folio business objects below 9px are not acceptable as readable content.
        for o in objects:
            role = o.get("role")
            if role in {"metric-note", "process-step", "body"} and style_size(o) and style_size(o) < 9:
                issue(
                    issues, deck, slide,
                    "MICROTEXT_BELOW_ROLE_THRESHOLD", "warning",
                    f"{role} text uses {style_size(o):.1f}px; likely unreadable after PPTX rendering/export.",
                    o.get("id"), "C",
                    "Increase component size, reduce copy, or move detail to speaker notes/appendix.",
                )
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", help="IR JSON deck paths")
    ap.add_argument("--report", help="Write JSON report")
    args = ap.parse_args()
    all_issues = []
    for p in args.paths:
        deck = load_deck(Path(p))
        all_issues.extend(check_deck(deck))
    blocking = [i for i in all_issues if i["severity"] == "blocking"]
    report = {
        "issue_count": len(all_issues),
        "blocking_count": len(blocking),
        "release_decision": "fail" if blocking else "pass",
        "issues": all_issues,
    }
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if blocking:
        print(f"FAIL visual layout architecture: {len(blocking)} blocking issues")
        for i in blocking[:12]:
            print(f"{i['visual_anchor']} {i['slide']} {i['code']}: {i['message']}")
        return 1
    print(f"PASS visual layout architecture: {len(all_issues)} non-blocking issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
