#!/usr/bin/env python3
"""Generic component contract DSL gate for Slide IR.

This gate validates declarative component contracts: component selection, slot
membership, forbidden slot overlap, bounded badge overlap, inside-component
requirements, and slot-to-slot gaps. It is intentionally small and JSON-only for
now so the contract format stays auditable inside the skill.
"""
import argparse
import json
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def obj_id(obj):
    return obj.get("id", "")


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


def contains_box(parent, child, pad=0.0):
    pb = box(parent)
    cb = box(child)
    return cb["x"] >= pb["x"] + pad and cb["y"] >= pb["y"] + pad and right(cb) <= right(pb) - pad and bottom(cb) <= bottom(pb) - pad


def matches_selector(obj, selector):
    if not selector:
        return True
    if "id" in selector and obj_id(obj) != selector["id"]:
        return False
    if "id_contains" in selector and selector["id_contains"] not in obj_id(obj):
        return False
    if "id_contains_any" in selector and not any(s in obj_id(obj) for s in selector.get("id_contains_any") or []):
        return False
    if "role" in selector and obj.get("role") != selector["role"]:
        return False
    if "role_any" in selector and obj.get("role") not in set(selector.get("role_any") or []):
        return False
    if "type" in selector and obj.get("type") != selector["type"]:
        return False
    if "type_any" in selector and obj.get("type") not in set(selector.get("type_any") or []):
        return False
    if "component" in selector and obj.get("component") != selector["component"]:
        return False
    return True


def issue(code, contract, slide, object_ids, message, severity="blocking", evidence=None):
    return {
        "code": code,
        "severity": severity,
        "contract_id": contract.get("id"),
        "slide_id": slide.get("id"),
        "object_ids": object_ids,
        "message": message,
        "evidence": evidence or {},
    }


def load_contracts(path):
    root = Path(path)
    files = []
    if root.is_file():
        files = [root]
    else:
        files = sorted(root.glob("*.contract.json")) + sorted(root.glob("*.json"))
    contracts = []
    seen = set()
    for f in files:
        if f in seen:
            continue
        seen.add(f)
        data = load_json(f)
        data["_path"] = str(f)
        contracts.append(data)
    return contracts


def component_instances(slide, contract):
    objects = slide.get("objects", [])
    selector = contract.get("component_selector") or {}
    roots = [o for o in objects if matches_selector(o, selector)]
    return roots


def objects_for_slot(slide, root, slot):
    members = slot.get("members") or {}
    out = []
    for obj in slide.get("objects", []):
        if obj is root:
            continue
        if not matches_selector(obj, members):
            continue
        # Component contracts are scoped to the component root. Footer/source slots
        # are allowed to live outside the component; all other slots default to
        # children contained by the component panel unless explicitly external.
        slot_id = slot.get("id", "")
        is_external_slot = slot.get("external") or "guardrail" in slot_id or slot_id in {"footer", "source", "risk", "footnote"}
        if is_external_slot or obj.get("role") in {"footer-mask", "risk", "source", "footnote"}:
            out.append(obj)
        elif contains_box(root, obj) or obj.get("component") == root.get("id"):
            out.append(obj)
    return out


def build_slots(slide, root, contract):
    slots = {}
    for slot in contract.get("slots") or []:
        slots[slot.get("id")] = objects_for_slot(slide, root, slot)
    return slots


def check_forbid_slot_overlap(rule, contract, slide, slots):
    issues = []
    a_objs = slots.get(rule.get("slot_a"), [])
    b_objs = slots.get(rule.get("slot_b"), [])
    min_h = float(rule.get("min_overlap_h", 1) or 1)
    min_w_ratio = float(rule.get("min_overlap_w_ratio", 0) or 0)
    for a in a_objs:
        ab = box(a)
        offenders = []
        evidence = []
        for b in b_objs:
            bb = box(b)
            inter = intersection(ab, bb)
            if not inter:
                continue
            ratio_base = max(1.0, min(ab["w"], bb["w"]))
            if inter["h"] >= min_h and inter["w"] >= ratio_base * min_w_ratio:
                offenders.append(obj_id(b))
                evidence.append({"a": obj_id(a), "b": obj_id(b), "overlap_w": round(inter["w"], 2), "overlap_h": round(inter["h"], 2)})
        if offenders:
            issues.append(issue(rule.get("code", "SLOT_OVERLAP_FORBIDDEN"), contract, slide, [obj_id(a)] + offenders, "slot overlap violates component contract", evidence={"pairs": evidence}))
    return issues


def check_conditional_badge_overlap(rule, contract, slide, slots):
    issues = []
    badges = slots.get(rule.get("badge_slot"), [])
    targets = slots.get(rule.get("target_slot"), [])
    max_intrusion = float(rule.get("max_body_intrusion", 16) or 16)
    for badge in badges:
        bdb = box(badge)
        for target in targets:
            tb = box(target)
            inter = intersection(bdb, tb)
            if not inter:
                continue
            body_start = tb["y"] + max_intrusion
            if bottom(bdb) > body_start:
                issues.append(issue(
                    rule.get("code", "BADGE_OVERLAP_TOO_DEEP"),
                    contract,
                    slide,
                    [obj_id(badge), obj_id(target)],
                    "badge intrudes beyond allowed chrome/body boundary",
                    evidence={"overlap_h": round(inter["h"], 2), "badge_bottom": round(bottom(bdb), 2), "allowed_body_start": round(body_start, 2)},
                ))
                break
    return issues


def near_component_bottom(root, obj, spec):
    if not spec:
        return True
    rb = box(root)
    ob = box(obj)
    before = float(spec.get("before", 0) or 0)
    after = float(spec.get("after", 0) or 0)
    return ob["y"] >= bottom(rb) - before and ob["y"] <= bottom(rb) + after


def check_must_be_inside_component(rule, contract, slide, root, slots):
    issues = []
    pad = float(rule.get("pad", 0) or 0)
    for obj in slots.get(rule.get("slot"), []):
        if not near_component_bottom(root, obj, rule.get("only_if_near_component_bottom")):
            continue
        if not contains_box(root, obj, pad=pad):
            issues.append(issue(
                rule.get("code", "COMPONENT_CHILD_OUTSIDE"),
                contract,
                slide,
                [obj_id(obj), obj_id(root)],
                "slot member must stay inside its component root",
                evidence={"pad": pad, "object_y": round(box(obj)["y"], 2), "component_bottom": round(bottom(box(root)), 2)},
            ))
    return issues


def check_min_gap_between_slots(rule, contract, slide, slots):
    issues = []
    min_gap = float(rule.get("min_gap", 0) or 0)
    axis = rule.get("axis", "vertical")
    for a in slots.get(rule.get("slot_a"), []):
        ab = box(a)
        for b in slots.get(rule.get("slot_b"), []):
            bb = box(b)
            if axis == "vertical":
                if rule.get("allow_overlap_projection") and not (ab["x"] < right(bb) and right(ab) > bb["x"]):
                    continue
                gap = bb["y"] - bottom(ab)
                if -1 <= gap < min_gap:
                    issues.append(issue(
                        rule.get("code", "SLOT_GAP_TOO_SMALL"),
                        contract,
                        slide,
                        [obj_id(a), obj_id(b)],
                        "slot-to-slot vertical gap is below component contract",
                        evidence={"gap": round(gap, 2), "required_gap": min_gap},
                    ))
            else:
                gap = bb["x"] - right(ab)
                if -1 <= gap < min_gap:
                    issues.append(issue(rule.get("code", "SLOT_GAP_TOO_SMALL"), contract, slide, [obj_id(a), obj_id(b)], "slot-to-slot horizontal gap is below component contract", evidence={"gap": round(gap, 2), "required_gap": min_gap}))
    return issues


def check_rule(rule, contract, slide, root, slots):
    rtype = rule.get("type")
    if rtype == "forbid_slot_overlap":
        return check_forbid_slot_overlap(rule, contract, slide, slots)
    if rtype == "conditional_badge_overlap":
        return check_conditional_badge_overlap(rule, contract, slide, slots)
    if rtype == "must_be_inside_component":
        return check_must_be_inside_component(rule, contract, slide, root, slots)
    if rtype == "min_gap_between_slots":
        return check_min_gap_between_slots(rule, contract, slide, slots)
    return [issue("UNKNOWN_COMPONENT_CONTRACT_RULE", contract, slide, [obj_id(root)], "unknown component contract rule type", evidence={"rule_type": rtype})]


def check_ir(ir, contracts):
    issues = []
    for slide in (ir.get("deck") or {}).get("slides", []):
        for contract in contracts:
            for root in component_instances(slide, contract):
                slots = build_slots(slide, root, contract)
                for rule in contract.get("rules") or []:
                    issues.extend(check_rule(rule, contract, slide, root, slots))
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("--contracts", required=True, help="Contract JSON file or directory containing *.contract.json")
    ap.add_argument("--report", required=True)
    args = ap.parse_args(argv)
    ir = load_json(args.ir)
    contracts = load_contracts(args.contracts)
    issues = check_ir(ir, contracts)
    blocking = [i for i in issues if i.get("severity") == "blocking"]
    report = {
        "gate": "component_contract_dsl",
        "contracts": [c.get("id") for c in contracts],
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i.get("severity") == "warning"]),
        "issues": issues,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if blocking:
        print("FAIL component contract DSL: %d blocking issues" % len(blocking))
        return 1
    print("PASS component contract DSL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
