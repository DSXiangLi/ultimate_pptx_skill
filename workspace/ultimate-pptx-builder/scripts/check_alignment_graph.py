#!/usr/bin/env python3
"""Alignment graph gate for Slide IR.

Validates declared layout relations so PPTX QA can check alignment intent rather
than relying only on overlap or a few hard-coded component names.
"""
import argparse
import json
import sys
from pathlib import Path


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


def edge(b, kind):
    if kind == "left":
        return b["x"]
    if kind == "right":
        return b["x"] + b["w"]
    if kind == "top":
        return b["y"]
    if kind == "bottom":
        return b["y"] + b["h"]
    if kind == "center-x":
        return b["x"] + b["w"] / 2.0
    if kind == "center-y":
        return b["y"] + b["h"] / 2.0
    raise ValueError("unknown edge %s" % kind)


def object_map(slide):
    return {o.get("id"): o for o in slide.get("objects", []) if o.get("id")}


def issue(code, slide, relation, message, severity="blocking", evidence=None):
    return {
        "code": code,
        "severity": severity,
        "slide_id": slide.get("id"),
        "relation_id": relation.get("id"),
        "relation_type": relation.get("type"),
        "message": message,
        "evidence": evidence or {},
    }


def check_align(slide, rel, objs, kind):
    tol = float(rel.get("tolerance", 3) or 3)
    vals = [(o.get("id"), edge(box(o), kind)) for o in objs]
    if not vals:
        return []
    anchor = vals[0][1]
    diffs = [(oid, round(v - anchor, 2)) for oid, v in vals if abs(v - anchor) > tol]
    if diffs:
        code = "DECLARED_ALIGN_%s_BROKEN" % kind.upper().replace("-", "_")
        return [issue(code, slide, rel, "%s alignment exceeds tolerance" % kind, evidence={"anchor": round(anchor, 2), "tolerance": tol, "diffs": diffs})]
    return []


def check_equal(slide, rel, objs, dim):
    tol = float(rel.get("tolerance", 3) or 3)
    vals = [(o.get("id"), box(o)["w" if dim == "width" else "h"]) for o in objs]
    if not vals:
        return []
    anchor = vals[0][1]
    diffs = [(oid, round(v - anchor, 2)) for oid, v in vals if abs(v - anchor) > tol]
    if diffs:
        return [issue("EQUAL_%s_BROKEN" % dim.upper(), slide, rel, "%s equality exceeds tolerance" % dim, evidence={"anchor": round(anchor, 2), "tolerance": tol, "diffs": diffs})]
    return []


def check_gutter(slide, rel, objs):
    gutter = rel.get("gutter") or {}
    if gutter.get("mode") != "equal" or len(objs) < 3:
        return []
    tol = float(gutter.get("tolerance", rel.get("tolerance", 3)) or 3)
    ordered = sorted(objs, key=lambda o: box(o)["x"])
    gaps = []
    for a, b in zip(ordered, ordered[1:]):
        ab, bb = box(a), box(b)
        gaps.append((a.get("id") + "→" + b.get("id"), bb["x"] - (ab["x"] + ab["w"])))
    anchor = gaps[0][1]
    diffs = [(pair, round(g - anchor, 2)) for pair, g in gaps if abs(g - anchor) > tol]
    if diffs:
        return [issue("EQUAL_GUTTER_BROKEN", slide, rel, "equal gutter exceeds tolerance", evidence={"anchor_gap": round(anchor, 2), "tolerance": tol, "diffs": diffs})]
    return []


def check_parent_padding(slide, rel, by_id):
    parent = by_id.get(rel.get("parent"))
    children = [by_id.get(cid) for cid in rel.get("children", []) if by_id.get(cid)]
    if not parent or not children:
        return [issue("RELATION_OBJECT_MISSING", slide, rel, "parent-padding relation references missing objects")]
    pb = box(parent)
    pad = rel.get("padding") or {}
    px = float(pad.get("x", 0) or 0)
    py = float(pad.get("y", 0) or 0)
    tol = float(rel.get("tolerance", 3) or 3)
    failures = []
    for child in children:
        cb = box(child)
        if cb["x"] < pb["x"] + px - tol or cb["y"] < pb["y"] + py - tol:
            failures.append(child.get("id"))
        if cb["x"] + cb["w"] > pb["x"] + pb["w"] - px + tol or cb["y"] + cb["h"] > pb["y"] + pb["h"] - py + tol:
            failures.append(child.get("id"))
    if failures:
        return [issue("PARENT_PADDING_BROKEN", slide, rel, "child object violates parent padding", evidence={"objects": sorted(set(failures)), "padding": pad, "tolerance": tol})]
    return []


def check_relation(slide, rel, by_id):
    rtype = rel.get("type")
    ids = rel.get("objects", [])
    objs = [by_id.get(oid) for oid in ids if by_id.get(oid)]
    if rtype != "parent-padding" and len(objs) != len(ids):
        return [issue("RELATION_OBJECT_MISSING", slide, rel, "relation references missing objects")]
    issues = []
    if rtype in {"align-left", "align-right", "align-top", "align-bottom", "align-center-x", "align-center-y"}:
        kind = rtype.replace("align-", "")
        issues.extend(check_align(slide, rel, objs, kind))
    elif rtype == "row":
        for kind in rel.get("align", []):
            issues.extend(check_align(slide, rel, objs, kind))
        for dim in rel.get("equal", []):
            issues.extend(check_equal(slide, rel, objs, dim))
        issues.extend(check_gutter(slide, rel, objs))
    elif rtype == "parent-padding":
        issues.extend(check_parent_padding(slide, rel, by_id))
    elif rtype == "vertical-stack":
        # Text rhythm is checked by check_text_spacing.py. This relation type is accepted here.
        pass
    else:
        issues.append(issue("UNKNOWN_LAYOUT_RELATION", slide, rel, "unknown layout relation type"))
    return issues


def inferred_alignment_warnings(slide):
    # Lightweight non-blocking hint: strong near-miss left anchors among priority objects.
    objs = [o for o in slide.get("objects", []) if (o.get("editability") or {}).get("priority", 0) >= 4]
    xs = []
    for o in objs:
        xs.append((o.get("id"), box(o)["x"]))
    warnings = []
    for i, (oid, x) in enumerate(xs):
        for oid2, x2 in xs[i + 1:]:
            d = abs(x - x2)
            if 8 <= d <= 16:
                warnings.append(issue("INFERRED_ALIGNMENT_NEAR_MISS", slide, {"id": "inferred-left-edge", "type": "inferred"}, "priority objects have near-miss left edges", severity="warning", evidence={"objects": [oid, oid2], "delta": round(d, 2)}))
                if len(warnings) >= 6:
                    return warnings
    return warnings


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("--report", required=True)
    args = ap.parse_args(argv)
    ir = load_json(args.ir)
    issues = []
    for slide in (ir.get("deck") or {}).get("slides", []):
        by_id = object_map(slide)
        relations = slide.get("layout_relations", [])
        if not relations:
            issues.append(issue("LAYOUT_RELATIONS_MISSING", slide, {"id": "slide-layout-contract", "type": "missing"}, "slide has no declared layout relations"))
        for rel in relations:
            issues.extend(check_relation(slide, rel, by_id))
        issues.extend(inferred_alignment_warnings(slide))
    blocking = [i for i in issues if i.get("severity") == "blocking"]
    report = {
        "gate": "alignment_graph",
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i.get("severity") == "warning"]),
        "issues": issues,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if blocking:
        print("FAIL alignment graph: %d blocking issues" % len(blocking))
        return 1
    print("PASS alignment graph")
    return 0


if __name__ == "__main__":
    sys.exit(main())
