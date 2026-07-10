#!/usr/bin/env python3
"""Role-aware text spacing gate for Slide IR.

This gate is stricter than collision detection: it traverses priority text blocks
and checks whether non-overlapping text is still too close for its semantic
relationship. It is intentionally deterministic and dependency-free so it can run
inside every PPTX validation loop.
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

DECORATIVE_ROLES = {"page-number", "folio", "research-folio", "kicker", "section-label"}
FOOTER_ROLES = {"risk", "source", "footnote"}
METRIC_ROLES = {"metric", "metric-label", "metric-note", "metric-delta"}
TEXT_TYPES = {"text"}


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


def ink_box(obj):
    """Conservative rendered-text extent estimate inside a native text box.

    Full text boxes often include spare vertical capacity. Spacing should be
    measured between likely ink extents, not entire authoring containers.
    """
    b = box(obj)
    fs = size(obj) or 10.0
    text = obj.get("text", "")
    # Width estimate is deliberately capped by the authoring box.
    chars_per_line = max(1, int(b["w"] / max(fs * 0.58, 4.0)))
    lines = max(1, int(math.ceil(len(text) / float(chars_per_line))))
    ink_h = min(b["h"], max(fs * 1.15 * lines, min(b["h"], fs * 1.1)))
    return {"x": b["x"], "y": b["y"], "w": b["w"], "h": ink_h}


def right(b):
    return b["x"] + b["w"]


def bottom(b):
    return b["y"] + b["h"]


def center_y(b):
    return b["y"] + b["h"] / 2.0


def center_x(b):
    return b["x"] + b["w"] / 2.0


def overlap_1d(a1, a2, b1, b2):
    return max(0.0, min(a2, b2) - max(a1, b1))


def horizontal_gap(a, b):
    if right(a) <= b["x"]:
        return b["x"] - right(a)
    if right(b) <= a["x"]:
        return a["x"] - right(b)
    return 0.0


def vertical_gap(a, b):
    if bottom(a) <= b["y"]:
        return b["y"] - bottom(a)
    if bottom(b) <= a["y"]:
        return a["y"] - bottom(b)
    return 0.0


def euclidean_gap(a, b):
    hg = horizontal_gap(a, b)
    vg = vertical_gap(a, b)
    return math.sqrt(hg * hg + vg * vg)


def priority(obj):
    return int((obj.get("editability") or {}).get("priority", 0) or 0)


def size(obj):
    return float((obj.get("style") or {}).get("size", 0) or 0)


def metric_group_id(obj):
    oid = obj.get("id", "")
    patterns = [
        r"(.+?_metric_\d+)_",
        r"(.+?_signal_point_\d+)_",
        r"(.+?_macro_zone_\d+)_",
        r"(.+?_macro_matrix_\d+)_",
        r"(.+?_scenario_zone_\d+)_",
        r"(.+?_bridge_asset_\d+)_",
        r"(.+?_process_signal_\d+)_",
        r"(.+?_process_\d+)_",
    ]
    for pat in patterns:
        m = re.match(pat, oid)
        if m:
            return m.group(1)
    return None


def is_decorative(obj):
    return obj.get("role") in DECORATIVE_ROLES or priority(obj) <= 2


def text_objects(slide):
    out = []
    for obj in slide.get("objects", []):
        if obj.get("type") in TEXT_TYPES and obj.get("text") and priority(obj) >= 3 and not is_decorative(obj):
            obj = dict(obj)
            obj["_box"] = ink_box(obj)
            out.append(obj)
    return out


def classify(a, b):
    ar, br = a.get("role"), b.get("role")
    if ar in FOOTER_ROLES or br in FOOTER_ROLES:
        return "footer"
    ag, bg = metric_group_id(a), metric_group_id(b)
    ax, bx = a["_box"], b["_box"]
    x_overlap = overlap_1d(ax["x"], right(ax), bx["x"], right(bx))
    y_overlap = overlap_1d(ax["y"], bottom(ax), bx["y"], bottom(bx))
    y_gap = vertical_gap(ax, bx)
    if ag and ag == bg:
        if ar in METRIC_ROLES and br in METRIC_ROLES:
            return "metric-stack"
        if ar == "process-step" and br == "process-step" and y_overlap > 0:
            return "component-row"
        if y_overlap > 0:
            return "component-row"
        return "component-stack"
    if x_overlap >= min(ax["w"], bx["w"]) * 0.45 and y_gap > 0:
        if ar == "body" and br == "body":
            return "paragraph-stack"
        return "vertical-stack"
    return "unrelated"


def min_gap_for(relation, a, b):
    if relation == "metric-stack":
        return 2.0
    if relation == "component-row":
        return 6.0
    if relation == "component-stack":
        return 4.0
    if relation == "paragraph-stack":
        return 6.0
    if relation == "vertical-stack":
        return 6.0
    if relation == "footer":
        return 10.0
    return 8.0


def issue(code, slide, a, b, gap, required, relation, severity="blocking"):
    return {
        "code": code,
        "severity": severity,
        "slide_id": slide.get("id"),
        "object_ids": [a.get("id"), b.get("id")],
        "roles": [a.get("role"), b.get("role")],
        "relation": relation,
        "gap": round(float(gap), 2),
        "required_gap": round(float(required), 2),
    }


def check_slide(slide):
    issues = []
    texts = text_objects(slide)
    for i, a in enumerate(texts):
        for b in texts[i + 1:]:
            ab, bb = a["_box"], b["_box"]
            x_ov = overlap_1d(ab["x"], right(ab), bb["x"], right(bb))
            y_ov = overlap_1d(ab["y"], bottom(ab), bb["y"], bottom(bb))
            relation = classify(a, b)
            required = min_gap_for(relation, a, b)
            if x_ov > 0 and y_ov > 0:
                # Collision remains the layout-safety gate's job; duplicate only if priority is high.
                if priority(a) >= 4 and priority(b) >= 4 and relation != "metric-stack":
                    issues.append(issue("TEXT_COLLISION", slide, a, b, 0, required, relation))
                continue
            if relation in {"paragraph-stack", "vertical-stack", "metric-stack", "footer", "component-stack", "component-row"}:
                gap = vertical_gap(ab, bb) if horizontal_gap(ab, bb) == 0 or x_ov > 0 else horizontal_gap(ab, bb)
            else:
                # For side-by-side text, only consider pairs that project onto each other vertically.
                if y_ov < min(ab["h"], bb["h"]) * 0.2:
                    continue
                gap = horizontal_gap(ab, bb)
            if gap + 0.5 < required:
                if relation == "metric-stack":
                    code = "METRIC_STACK_GAP_TOO_SMALL"
                elif relation == "paragraph-stack":
                    code = "PARAGRAPH_RHYTHM_TOO_TIGHT"
                elif relation == "footer":
                    code = "FOOTER_TEXT_SEPARATION_TOO_SMALL"
                elif relation == "vertical-stack":
                    code = "TEXT_STACK_GAP_TOO_SMALL"
                elif relation == "component-row":
                    code = "COMPONENT_ROW_GAP_TOO_SMALL"
                elif relation == "component-stack":
                    code = "COMPONENT_STACK_GAP_TOO_SMALL"
                else:
                    code = "UNRELATED_TEXT_GAP_TOO_SMALL"
                issues.append(issue(code, slide, a, b, gap, required, relation))
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("--report", required=True)
    args = ap.parse_args(argv)
    ir = load_json(args.ir)
    issues = []
    for slide in (ir.get("deck") or {}).get("slides", []):
        issues.extend(check_slide(slide))
    blocking = [i for i in issues if i.get("severity") == "blocking"]
    report = {
        "gate": "text_spacing",
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i.get("severity") == "warning"]),
        "issues": issues,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if blocking:
        print("FAIL text spacing: %d blocking issues" % len(blocking))
        return 1
    print("PASS text spacing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
