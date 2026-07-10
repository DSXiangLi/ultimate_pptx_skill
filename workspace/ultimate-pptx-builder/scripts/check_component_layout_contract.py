#!/usr/bin/env python3
"""Component-level layout contract gate for Slide IR.

This gate catches component grammar failures that plain bbox overlap checks miss:
children can be inside a legal parent container while still violating the
component's semantic slots (e.g. bottom bands covering route cards, floating
badges covering card bodies, guardrail notes orphaned between a map and footer).
"""
import argparse
import json
import sys
from pathlib import Path


PANEL_MIN_AREA = 50000


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def box(obj):
    b = obj.get("box") or {}
    return {
        "x": float(b.get("x", 0) or 0),
        "y": float(b.get("y", 0) or 0),
        "w": float(b.get("w", 0) or 0),
        "h": float(b.get("h", 0) or 0),
    }


def right(b):
    return b["x"] + b["w"]


def bottom(b):
    return b["y"] + b["h"]


def area(b):
    return max(0.0, b["w"]) * max(0.0, b["h"])


def intersection(a, b):
    x1 = max(a["x"], b["x"])
    y1 = max(a["y"], b["y"])
    x2 = min(right(a), right(b))
    y2 = min(bottom(a), bottom(b))
    if x2 <= x1 or y2 <= y1:
        return None
    return {"x": x1, "y": y1, "w": x2 - x1, "h": y2 - y1}


def contains(parent, child, pad=0.0):
    pb, cb = box(parent), box(child)
    return cb["x"] >= pb["x"] + pad and cb["y"] >= pb["y"] + pad and right(cb) <= right(pb) - pad and bottom(cb) <= bottom(pb) - pad


def issue(code, slide, object_ids, message, severity="blocking", evidence=None):
    return {
        "code": code,
        "severity": severity,
        "slide_id": slide.get("id"),
        "object_ids": object_ids,
        "message": message,
        "evidence": evidence or {},
    }


def is_route_map_panel(obj):
    oid = obj.get("id", "")
    return obj.get("type") == "shape" and obj.get("role") == "route-map" and ("panel" in oid or area(box(obj)) >= PANEL_MIN_AREA)


def route_map_cards(panel, objects):
    pb = box(panel)
    out = []
    for obj in objects:
        if obj is panel or obj.get("type") != "shape":
            continue
        oid = obj.get("id", "")
        role = obj.get("role")
        if role not in {"route-map", "map-node"}:
            continue
        b = box(obj)
        if area(b) < 900:
            continue
        if contains(panel, obj) and b["w"] < pb["w"] * 0.55 and b["h"] < pb["h"] * 0.75:
            out.append(obj)
    return out


def bottom_bands(panel, objects):
    pb = box(panel)
    out = []
    for obj in objects:
        if obj is panel or obj.get("type") != "shape":
            continue
        oid = obj.get("id", "")
        role = obj.get("role")
        b = box(obj)
        if not contains(panel, obj):
            continue
        is_rule = "rule_matrix" in oid or "bottom" in oid or "guardrail" in oid
        is_wide_trigger = role == "trigger-row" and b["w"] >= pb["w"] * 0.55
        is_low = b["y"] >= pb["y"] + pb["h"] * 0.52
        if (is_rule or is_wide_trigger) and is_low:
            out.append(obj)
    return out


def floating_badges(panel, objects):
    pb = box(panel)
    out = []
    for obj in objects:
        if obj is panel or obj.get("type") != "shape":
            continue
        oid = obj.get("id", "")
        b = box(obj)
        if not contains(panel, obj):
            continue
        if obj.get("role") == "trigger-row" and "rule_matrix" not in oid and b["w"] < pb["w"] * 0.35 and b["h"] < pb["h"] * 0.35:
            out.append(obj)
    return out


def check_route_map(panel, slide, objects):
    issues = []
    cards = route_map_cards(panel, objects)
    bands = bottom_bands(panel, objects)
    badges = floating_badges(panel, objects)

    for band in bands:
        bb = box(band)
        offenders = []
        for card in cards:
            inter = intersection(bb, box(card))
            if not inter:
                continue
            # A bottom band may share a parent, but it must not intrude into the
            # card body. Any substantial vertical overlap is a grammar failure.
            if inter["h"] >= 6 and inter["w"] >= min(box(card)["w"], bb["w"]) * 0.25:
                offenders.append(card.get("id"))
        if offenders:
            issues.append(issue(
                "ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION",
                slide,
                [band.get("id")] + offenders,
                "route-map bottom band intrudes into node/card body slot",
                evidence={"band": band.get("id"), "cards": offenders},
            ))

    for badge in badges:
        bdb = box(badge)
        for card in cards:
            cb = box(card)
            inter = intersection(bdb, cb)
            if not inter:
                continue
            # Corner badges are allowed only if they stay near the card chrome.
            # Covering more than ~16px into the card means it reads as a floating
            # panel covering the semantic card, not a status marker.
            if bottom(bdb) > cb["y"] + 16:
                issues.append(issue(
                    "ATLAS_FLOATING_BADGE_COVERS_CARD",
                    slide,
                    [badge.get("id"), card.get("id")],
                    "floating status badge covers route-map card body instead of staying in a badge slot",
                    evidence={"overlap_h": round(inter["h"], 2), "badge_bottom": round(bottom(bdb), 2), "card_body_start": round(cb["y"] + 16, 2)},
                ))
                break

    return issues


def is_guardrail_text(obj):
    oid = obj.get("id", "")
    text = obj.get("text", "")
    role = obj.get("role")
    return obj.get("type") == "text" and ("guardrail" in oid.lower() or "回撤" in text or "偏离" in text) and role not in {"risk", "source", "footnote"}


def footer_objects(objects):
    return [o for o in objects if o.get("role") in {"footer-mask", "risk", "source", "footnote"}]


def check_guardrails(slide, objects):
    issues = []
    panels = [o for o in objects if is_route_map_panel(o)]
    # Guardrail/footer checks are Atlas route-map component checks. Without a
    # route-map panel, words like “偏离” in ordinary metric deltas are not evidence
    # of an orphaned guardrail note.
    if not panels:
        return issues
    footers = footer_objects(objects)
    for note in [o for o in objects if is_guardrail_text(o)]:
        nb = box(note)
        containing = [p for p in panels if contains(p, note, pad=4)]
        nearest_panel = min(panels, key=lambda p: abs(nb["y"] - bottom(box(p))))
        pb = box(nearest_panel)
        near_route_map_bottom = nb["y"] >= bottom(pb) - 8 and nb["y"] <= bottom(pb) + 42
        if not near_route_map_bottom:
            continue
        if not containing:
            # Between map and footer / just below the map: visually orphaned.
            issues.append(issue(
                "ATLAS_GUARDRAIL_TEXT_ORPHANED",
                slide,
                [note.get("id"), nearest_panel.get("id")],
                "guardrail note sits outside its route-map panel instead of occupying a declared slot",
                evidence={"note_y": round(nb["y"], 2), "panel_bottom": round(bottom(pb), 2)},
            ))
        for footer in footers:
            fb = box(footer)
            gap = fb["y"] - bottom(nb)
            if -1 <= gap < 16 and nb["x"] < right(fb) and right(nb) > fb["x"]:
                issues.append(issue(
                    "ATLAS_FOOTER_GUARDRAIL_COLLISION",
                    slide,
                    [note.get("id"), footer.get("id")],
                    "guardrail note is too close to footer/risk rail and reads as an orphaned footer collision",
                    evidence={"gap": round(gap, 2), "required_gap": 16},
                ))
                break
    return issues


def check_slide(slide):
    objects = slide.get("objects", [])
    issues = []
    for panel in [o for o in objects if is_route_map_panel(o)]:
        issues.extend(check_route_map(panel, slide, objects))
    issues.extend(check_guardrails(slide, objects))
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("--report", required=True)
    ap.add_argument("--contracts", default=str(Path(__file__).resolve().parents[1] / "examples" / "component-contracts"), help="Component contract file or directory; defaults to examples/component-contracts")
    args = ap.parse_args(argv)

    # The public gate name remains component_layout_contract for release-report
    # stability, but the implementation now runs the generic declarative DSL.
    from check_component_contracts import check_ir as check_dsl_ir
    from check_component_contracts import load_contracts as load_dsl_contracts

    ir = load_json(args.ir)
    contracts = load_dsl_contracts(args.contracts)
    issues = check_dsl_ir(ir, contracts)
    blocking = [i for i in issues if i.get("severity") == "blocking"]
    report = {
        "gate": "component_layout_contract",
        "engine": "component_contract_dsl",
        "contracts": [c.get("id") for c in contracts],
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i.get("severity") == "warning"]),
        "issues": issues,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if blocking:
        print("FAIL component layout contract: %d blocking issues" % len(blocking))
        return 1
    print("PASS component layout contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
