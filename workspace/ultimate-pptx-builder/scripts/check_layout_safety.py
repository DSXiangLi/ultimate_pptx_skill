#!/usr/bin/env python3
"""Layout and text safety checker for generated Slide IR.

This gate is stricter than visual fidelity. Fidelity can pass when a flawed IR is
faithfully rendered. This checker validates whether the IR itself is safe for
finance PPT use: safe zones, estimated text capacity, pairwise text collision,
metric-card internal layout, multi-line text leading, container collisions,
footer separation, table density, title/decor collisions, and long-deck template smell.
"""
from pathlib import Path
import argparse
import json
import math
import re
import sys
TEXT_RENDER_SCALE = 1.30

CRITICAL_ROLES = {"title", "body", "risk", "source", "footnote", "metric", "metric-note", "metric-label", "metric-card", "risk-rail", "table", "chart"}
DECORATIVE_ROLES = {"background", "decorative-glow", "decorative-ghost-number", "quote-mark", "divider"}
FOOTER_ROLES = {"risk", "risk-rail"}
TEXT_COLLISION_ROLES = {"title", "body", "risk", "source", "footnote", "metric", "metric-note", "metric-label", "process-step", "matrix-cell", "timeline-step", "quote"}
CONTAINER_ROLES = {"glass-panel", "metric-card", "scenario-card", "process-step", "matrix-cell", "supporting-card"}
CONTAINER_TYPES = {"chart", "table"}
PROTECTED_WRAP_TERMS = ["风险预算", "评审版本", "投委会", "形成", "现金流", "稳定器", "触发器", "出海链条", "承担", "红利拥挤", "先进制造", "AI算力"]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def issue(slide, obj_id, code, msg, severity="blocking", other=None):
    item = {"slide": slide, "object": obj_id, "code": code, "severity": severity, "message": msg}
    if other:
        item["other"] = other
    return item


def intersects(a, b):
    return not (a["x"] + a["w"] <= b["x"] or b["x"] + b["w"] <= a["x"] or a["y"] + a["h"] <= b["y"] or b["y"] + b["h"] <= a["y"])


def intersection(a, b):
    x = max(0, min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"]))
    y = max(0, min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"]))
    return x * y, x, y


def weighted_text_units(text):
    text = str(text or "")
    cjk = sum(1 for c in text if ord(c) > 127)
    ascii_chars = max(0, len(text) - cjk)
    return cjk * 1.0 + ascii_chars * 0.55


def text_capacity(text, box, font_size, role="body"):
    # Conservative CJK-aware estimate. PPT text metrics vary by Office version;
    # measure capacity in weighted pixels, not pseudo character counts. The old
    # checker accidentally let CJK use ~0.58em width, which missed title/body wraps.
    if not text:
        return 0, 0, 0
    weighted_units = weighted_text_units(text)
    usable_w = max(1.0, box["w"] * 0.88)
    needed_lines = max(1, int(math.ceil((weighted_units * font_size * TEXT_RENDER_SCALE) / usable_w)))
    chars_per_line = max(1, int(usable_w / max(font_size * TEXT_RENDER_SCALE, 1)))
    if needed_lines > 1:
        line_height = font_size * 1.38
        required_h = needed_lines * line_height + max(8, font_size * 0.55)
    else:
        line_height = font_size * 1.05
        required_h = needed_lines * line_height
    return needed_lines, required_h, chars_per_line


def term_wrap_issues(text, box, font_size):
    out = []
    text = str(text or "")
    if not text:
        return out
    capacity_units = max(1.0, box["w"] * 0.88 / max(font_size * TEXT_RENDER_SCALE, 1))
    total_units = weighted_text_units(text)
    lines = max(1, int(math.ceil(total_units / capacity_units)))
    if lines <= 1:
        return out
    for term in PROTECTED_WRAP_TERMS:
        start = 0
        while True:
            idx = text.find(term, start)
            if idx < 0:
                break
            before = weighted_text_units(text[:idx])
            after = before + weighted_text_units(term)
            for line_no in range(1, lines):
                br = line_no * capacity_units
                if before < br < after:
                    out.append((term, br, before, after))
            start = idx + 1
    return out


def estimated_text_hitbox(obj):
    box = dict(obj["box"])
    text = obj.get("text", "")
    role = obj.get("role", "body")
    font_size = obj.get("font_size") or obj.get("style", {}).get("size", 14)
    _lines, required_h, _cpl = text_capacity(text, box, font_size, role)
    # If text is likely to overflow, use required_h; otherwise use actual rendered
    # text height instead of the oversized text-box height. This catches overlap
    # while avoiding false positives from deliberately tall title boxes.
    box["h"] = min(max(required_h, font_size * 1.05), max(required_h, obj["box"]["h"]))
    return box


def check_text_object(slide_id, obj, settings):
    out = []
    box = obj["box"]
    text = obj.get("text", "")
    role = obj.get("role", "body")
    priority = obj.get("editability", {}).get("priority", 1)
    font_size = obj.get("font_size") or obj.get("style", {}).get("size", 14)
    if not text:
        return out
    lines, required_h, cpl = text_capacity(text, box, font_size, role)
    tolerance = 1.12 if role in {"risk", "source", "footnote"} else 1.0
    if priority >= 4 and required_h > box["h"] * tolerance:
        out.append(issue(slide_id, obj["id"], "TEXT_OVERFLOW_RISK", "priority-%s text likely exceeds box: required_h=%.1f box_h=%.1f lines=%d cpl=%d text=%r" % (priority, required_h, box["h"], lines, cpl, text[:60])))
    if role == "title" and len(text) > settings["max_title_chars"]:
        out.append(issue(slide_id, obj["id"], "TITLE_TOO_LONG", "title exceeds %d chars; use shorter judgment title or split subtitle: %r" % (settings["max_title_chars"], text[:80]), severity="warning"))
    if role in {"title", "body", "quote", "process-step", "matrix-cell", "timeline-step"} and priority >= 4:
        for term, br, before, after in term_wrap_issues(text, box, font_size):
            out.append(issue(slide_id, obj["id"], "PROTECTED_TERM_WRAP_RISK", "estimated line break %.1f falls inside protected term %r span %.1f-%.1f; rewrite, widen, or shrink text" % (br, term, before, after)))
    return out


def check_pairwise_text_collisions(slide_id, objects, settings):
    out = []
    texts = [o for o in objects if o.get("type") == "text" and o.get("role") in TEXT_COLLISION_ROLES and o.get("editability", {}).get("priority", 1) >= 4]
    for i, a in enumerate(texts):
        a_box = estimated_text_hitbox(a)
        for b in texts[i + 1:]:
            # same paragraph sequence can be adjacent; overlap is never acceptable
            b_box = estimated_text_hitbox(b)
            area, iw, ih = intersection(a_box, b_box)
            if area > settings["text_collision_min_area"] and ih >= settings["text_collision_min_height"]:
                out.append(issue(slide_id, a.get("id"), "TEXT_BOX_COLLISION", "estimated rendered text collides with %s: overlap=%.1f (%sx%s), texts=%r / %r" % (b.get("id"), area, round(iw, 1), round(ih, 1), a.get("text", "")[:40], b.get("text", "")[:40]), other=b.get("id")))
    return out


def metric_group_issues(slide_id, objects, settings):
    out = []
    groups = {}
    for o in objects:
        m = re.match(r"(.+_metric_\d+)_(card|label|value|delta)$", o.get("id", ""))
        if m:
            groups.setdefault(m.group(1), {})[m.group(2)] = o
    for gid, group in groups.items():
        card = group.get("card")
        if card:
            cb = card["box"]
            for key in ["label", "value", "delta"]:
                obj = group.get(key)
                if not obj:
                    continue
                hb = estimated_text_hitbox(obj)
                if hb["x"] < cb["x"] + settings["metric_inner_pad_x"] or hb["x"] + hb["w"] > cb["x"] + cb["w"] - settings["metric_inner_pad_x"]:
                    out.append(issue(slide_id, card["id"], "METRIC_CHILD_X_PADDING", "metric child %s violates horizontal padding" % obj["id"], other=obj["id"]))
                if hb["y"] < cb["y"] + settings["metric_inner_pad_y"] or hb["y"] + hb["h"] > cb["y"] + cb["h"] - settings["metric_inner_pad_y"]:
                    out.append(issue(slide_id, card["id"], "METRIC_CHILD_Y_PADDING", "metric child %s violates vertical padding: child=%s card=%s" % (obj["id"], hb, cb), other=obj["id"]))
        ordered = [group.get("label"), group.get("value"), group.get("delta")]
        ordered = [x for x in ordered if x]
        for a, b in zip(ordered, ordered[1:]):
            ab, bb = estimated_text_hitbox(a), estimated_text_hitbox(b)
            gap = bb["y"] - (ab["y"] + ab["h"])
            if gap < settings["metric_min_vertical_gap"]:
                out.append(issue(slide_id, a["id"], "METRIC_TEXT_COLLISION", "metric text stack has gap %.1f before %s; min_gap=%s" % (gap, b["id"], settings["metric_min_vertical_gap"]), other=b["id"]))
    return out



def is_visual_container(obj):
    if obj.get("type") in CONTAINER_TYPES:
        return True
    return obj.get("type") == "shape" and obj.get("role") in CONTAINER_ROLES


def expanded_box(box, pad):
    return {"x": box["x"] - pad, "y": box["y"] - pad, "w": box["w"] + 2 * pad, "h": box["h"] + 2 * pad}


def contains_box(parent, child, pad=0):
    p, c = parent["box"], child["box"]
    return c["x"] >= p["x"] + pad and c["y"] >= p["y"] + pad and c["x"] + c["w"] <= p["x"] + p["w"] - pad and c["y"] + c["h"] <= p["y"] + p["h"] - pad


def allowed_nested_container(parent, child):
    pid, cid = parent.get("id", ""), child.get("id", "")
    prole, crole = parent.get("role"), child.get("role")
    # Matrix cells are intentionally grouped inside a matrix panel.
    if pid.endswith("_matrix_panel") and crole == "matrix-cell":
        return True
    # Scenario/process primitives are their own cards, not nested glass panels.
    return False


def allowed_container_gap_pair(a, b):
    # Regular matrix grids intentionally use tighter internal gutters than
    # cross-zone containers. Their overlap is still blocked above; only the
    # generic 14px warning is suppressed for same-matrix cells.
    if a.get("role") == "matrix-cell" and b.get("role") == "matrix-cell":
        a_prefix = a.get("id", "").split("_matrix_")[0]
        b_prefix = b.get("id", "").split("_matrix_")[0]
        return a_prefix and a_prefix == b_prefix
    return False


def check_container_collisions(slide_id, objects, settings):
    out = []
    containers = [o for o in objects if is_visual_container(o) and o.get("role") not in DECORATIVE_ROLES]
    for i, a in enumerate(containers):
        for b in containers[i + 1:]:
            # risk rail is allowed to live at the bottom; other checks handle footer spacing.
            if a.get("role") == "risk-rail" or b.get("role") == "risk-rail":
                continue
            area, iw, ih = intersection(a["box"], b["box"])
            a_contains_b = contains_box(a, b, pad=0)
            b_contains_a = contains_box(b, a, pad=0)
            if area > 0:
                if a_contains_b and not allowed_nested_container(a, b):
                    out.append(issue(slide_id, a["id"], "NESTED_CONTAINER_DOUBLE_PANEL", "container %s contains %s; avoid double glass/panel boxes unless explicitly allowed" % (a["id"], b["id"]), other=b["id"]))
                elif b_contains_a and not allowed_nested_container(b, a):
                    out.append(issue(slide_id, b["id"], "NESTED_CONTAINER_DOUBLE_PANEL", "container %s contains %s; avoid double glass/panel boxes unless explicitly allowed" % (b["id"], a["id"]), other=a["id"]))
                elif not a_contains_b and not b_contains_a:
                    overlap_ratio = area / max(1.0, min(a["box"]["w"] * a["box"]["h"], b["box"]["w"] * b["box"]["h"]))
                    if overlap_ratio >= settings["container_overlap_ratio"] or ih >= settings["container_overlap_min_height"]:
                        out.append(issue(slide_id, a["id"], "CONTAINER_OVERLAP", "container overlaps %s: ratio=%.3f overlap=%sx%s" % (b["id"], overlap_ratio, round(iw, 1), round(ih, 1)), other=b["id"]))
            else:
                if allowed_container_gap_pair(a, b):
                    continue
                ea = expanded_box(a["box"], settings["container_min_gap"])
                if intersects(ea, b["box"]):
                    out.append(issue(slide_id, a["id"], "CONTAINER_GAP_TOO_SMALL", "container is closer than %spx to %s" % (settings["container_min_gap"], b["id"]), other=b["id"], severity="warning"))
    return out


def table_cell_issues(slide_id, obj, settings):
    out = []
    box = obj["box"]
    columns = obj.get("columns", [])
    rows = obj.get("rows", [])
    if not columns:
        return out
    cell_count = len(columns) * len(rows)
    if len(columns) > settings["max_table_columns"]:
        out.append(issue(slide_id, obj["id"], "TABLE_TOO_MANY_COLUMNS", "finance PPT table has %d columns; max %d before splitting or moving detail to appendix" % (len(columns), settings["max_table_columns"])))
    if cell_count > settings["max_table_cells"]:
        out.append(issue(slide_id, obj["id"], "TABLE_TOO_DENSE", "finance PPT table has %d visible cells; max %d for projector-safe benchmark pages" % (cell_count, settings["max_table_cells"])))
    if len(rows) > settings["max_table_rows"]:
        out.append(issue(slide_id, obj["id"], "TABLE_TOO_MANY_ROWS", "finance PPT table has %d rows; max %d before split/appendix" % (len(rows), settings["max_table_rows"]), severity="warning"))
    col_w = (box["w"] - 48) / max(1, len(columns))
    row_h = (box["h"] - 58) / max(1, len(rows) + 1)
    if row_h < settings["min_table_row_height"]:
        out.append(issue(slide_id, obj["id"], "TABLE_ROW_TOO_SHORT", "table row height %.1f is too small for finance deck readability; min %.1f" % (row_h, settings["min_table_row_height"])))
    for r_i, row in enumerate(rows):
        for c_i, cell in enumerate(row):
            text = str(cell)
            if not text:
                continue
            b = {"x": 0, "y": 0, "w": col_w, "h": row_h}
            lines, req_h, cpl = text_capacity(text, b, settings["table_font_size"], "table")
            if req_h > row_h * 1.05:
                out.append(issue(slide_id, obj["id"], "TABLE_CELL_OVERFLOW_RISK", "table cell r%d c%d likely overflows: required_h=%.1f row_h=%.1f cpl=%d text=%r" % (r_i + 1, c_i + 1, req_h, row_h, cpl, text[:50])))
    return out



def check_title_container_gap(slide_id, objects, settings):
    out = []
    titles = [o for o in objects if o.get("type") == "text" and o.get("role") == "title"]
    containers = [o for o in objects if is_visual_container(o) and o.get("role") not in DECORATIVE_ROLES and o.get("role") != "risk-rail"]
    for title in titles:
        tb = estimated_text_hitbox(title)
        for c in containers:
            cb = c.get("box", {})
            horizontal_overlap = min(tb["x"] + tb["w"], cb["x"] + cb["w"]) - max(tb["x"], cb["x"])
            if horizontal_overlap <= 0:
                continue
            if cb["y"] >= tb["y"]:
                gap = cb["y"] - (tb["y"] + tb["h"])
                if gap < settings["title_content_gap"]:
                    out.append(issue(slide_id, title["id"], "TITLE_CONTENT_GAP_TOO_SMALL", "title is only %.1fpx above container %s; min_gap=%s" % (gap, c["id"], settings["title_content_gap"]), other=c["id"]))
    return out


def check_title_text_gap_and_wrap(slide_id, objects, settings):
    out = []
    titles = [o for o in objects if o.get("type") == "text" and o.get("role") == "title"]
    texts = [o for o in objects if o.get("type") == "text" and o.get("role") in {"body", "quote"} and o.get("editability", {}).get("priority", 1) >= 4]
    for title in titles:
        tb = estimated_text_hitbox(title)
        font_size = title.get("style", {}).get("size", 14)
        lines, _required_h, _cpl = text_capacity(title.get("text", ""), title["box"], font_size, "title")
        if lines > 1:
            capacity_units = max(1.0, title["box"]["w"] * 0.88 / max(font_size, 1))
            total_units = weighted_text_units(title.get("text", ""))
            last_units = total_units - capacity_units * math.floor((total_units - 0.001) / capacity_units)
            if last_units < settings["title_orphan_min_units"]:
                out.append(issue(slide_id, title["id"], "TITLE_ORPHAN_WRAP", "title last line is only %.1f weighted chars; min %.1f. Widen title, reduce font, or split wording." % (last_units, settings["title_orphan_min_units"])))
        for txt in texts:
            if txt["id"] == title["id"] or txt.get("role") == "risk":
                continue
            xb = estimated_text_hitbox(txt)
            # Only protect the title band; deep body text is handled by container gaps.
            if xb["y"] > 280:
                continue
            horizontal_overlap = min(tb["x"] + tb["w"], xb["x"] + xb["w"]) - max(tb["x"], xb["x"])
            if horizontal_overlap <= 0:
                continue
            if xb["y"] >= tb["y"]:
                gap = xb["y"] - (tb["y"] + tb["h"])
                if gap < settings["title_text_gap"]:
                    out.append(issue(slide_id, title["id"], "TITLE_TEXT_GAP_TOO_SMALL", "title is only %.1fpx above text %s; min_gap=%s" % (gap, txt["id"], settings["title_text_gap"]), other=txt["id"]))
    return out


def check_alignment_grid(slide_id, objects, settings):
    out = []
    by_id = {o.get("id"): o for o in objects}
    tol = settings["alignment_tolerance"]
    # Chart-focus layouts should put the explanatory panel and chart on the same row.
    note_panels = [o for o in objects if o.get("id", "").endswith("_note_panel")]
    charts = [o for o in objects if o.get("type") == "chart"]
    for panel in note_panels:
        for chart in charts:
            dy = abs(panel["box"]["y"] - chart["box"]["y"])
            if dy > tol:
                out.append(issue(slide_id, panel["id"], "CONTENT_ROW_TOP_MISALIGNMENT", "note panel top differs from chart top by %.1fpx; max %.1f" % (dy, tol), other=chart["id"]))
    # Action pages: the KPI card row should share the same left/right grid as the body panel.
    body_panels = [o for o in objects if o.get("id", "").endswith("_body_panel") and o.get("role") == "glass-panel"]
    metric_cards = [o for o in objects if re.search(r"_metric_\d+_card$", o.get("id", ""))]
    for panel in body_panels:
        above = [c for c in metric_cards if c["box"]["y"] + c["box"]["h"] <= panel["box"]["y"] + 4]
        if len(above) >= 3:
            left = min(c["box"]["x"] for c in above)
            right = max(c["box"]["x"] + c["box"]["w"] for c in above)
            pleft = panel["box"]["x"]
            pright = panel["box"]["x"] + panel["box"]["w"]
            if abs(left - pleft) > settings["edge_alignment_tolerance"] or abs(right - pright) > settings["edge_alignment_tolerance"]:
                out.append(issue(slide_id, panel["id"], "CARD_ROW_EDGE_MISALIGNMENT", "metric card row span %.1f-%.1f does not align with panel span %.1f-%.1f" % (left, right, pleft, pright)))
    # Same-row metric cards should have matching tops and bottoms.
    rows = []
    for card in sorted(metric_cards, key=lambda o: (o["box"]["y"], o["box"]["x"])):
        placed = False
        for row in rows:
            if abs(row[0]["box"]["y"] - card["box"]["y"]) <= 12:
                row.append(card)
                placed = True
                break
        if not placed:
            rows.append([card])
    for row in rows:
        if len(row) < 3:
            continue
        tops = [c["box"]["y"] for c in row]
        bottoms = [c["box"]["y"] + c["box"]["h"] for c in row]
        if max(tops) - min(tops) > tol or max(bottoms) - min(bottoms) > tol:
            out.append(issue(slide_id, row[0]["id"], "CARD_ROW_BASELINE_MISALIGNMENT", "metric card row tops/bottoms differ by %.1f/%.1fpx" % (max(tops)-min(tops), max(bottoms)-min(bottoms))))
    return out


def check_slide(slide, deck_size, settings):
    out = []
    sid = slide.get("id", "unknown")
    w, h = deck_size["w"], deck_size["h"]
    safe = settings["safe_margin"]
    bottom_safe = settings["bottom_safe_margin"]
    title_objs = [o for o in slide.get("objects", []) if o.get("role") == "title"]
    decor_page_nums = [o for o in slide.get("objects", []) if re.search(r"ghost|page", o.get("id", ""), re.I)]
    footer_rails = [o for o in slide.get("objects", []) if o.get("role") == "risk-rail"]
    footer_y = min((o.get("box", {}).get("y", h) for o in footer_rails), default=None)
    title_text = " ".join(o.get("text", "") for o in title_objs)
    compliance_body_count = 0

    for obj in slide.get("objects", []):
        box = obj.get("box", {})
        role = obj.get("role")
        typ = obj.get("type")
        priority = obj.get("editability", {}).get("priority", 1)
        if typ == "shape" and role in DECORATIVE_ROLES:
            continue
        if priority >= 4 or role in CRITICAL_ROLES or typ in {"chart", "table"}:
            if box["x"] < safe or box["y"] < safe or box["x"] + box["w"] > w - safe:
                out.append(issue(sid, obj["id"], "SAFE_ZONE_XY", "critical object violates side/top safe zone: box=%s safe=%d" % (box, safe)))
            if box["y"] + box["h"] > h - bottom_safe:
                out.append(issue(sid, obj["id"], "BOTTOM_SAFE_ZONE", "critical object too close to bottom edge: y+h=%.1f limit=%.1f box=%s" % (box["y"] + box["h"], h - bottom_safe, box)))
        if footer_y is not None and role not in FOOTER_ROLES and role not in DECORATIVE_ROLES and (priority >= 3 or role == "glass-panel" or typ in {"chart", "table"}):
            limit = footer_y - settings["footer_gap"]
            if box["y"] + box["h"] > limit:
                out.append(issue(sid, obj["id"], "FOOTER_SEPARATION", "content enters footer separation band: y+h=%.1f limit=%.1f" % (box["y"] + box["h"], limit)))
        if typ == "text":
            if role == "body" and priority >= 4:
                compliance_body_count += 1
            out.extend(check_text_object(sid, obj, settings))
        elif typ == "table":
            out.extend(table_cell_issues(sid, obj, settings))

    out.extend(check_pairwise_text_collisions(sid, slide.get("objects", []), settings))
    out.extend(metric_group_issues(sid, slide.get("objects", []), settings))
    out.extend(check_container_collisions(sid, slide.get("objects", []), settings))
    out.extend(check_title_container_gap(sid, slide.get("objects", []), settings))
    out.extend(check_title_text_gap_and_wrap(sid, slide.get("objects", []), settings))
    out.extend(check_alignment_grid(sid, slide.get("objects", []), settings))

    if ("合规" in title_text or "适用" in title_text or "Compliance" in title_text) and compliance_body_count > settings["max_compliance_body_paragraphs"]:
        out.append(issue(sid, "compliance_body", "COMPLIANCE_TEXT_DENSITY", "compliance/suitability page has %d body paragraphs; max %d for PPT readability" % (compliance_body_count, settings["max_compliance_body_paragraphs"])))

    for decor in decor_page_nums:
        dbox = decor.get("box", {})
        area_ratio = (dbox.get("w", 0) * dbox.get("h", 0)) / float(w * h)
        if area_ratio > settings["max_page_number_area_ratio"]:
            out.append(issue(sid, decor["id"], "OVERSIZED_PAGE_NUMBER", "decorative page number too large for long-form deck: area_ratio=%.4f limit=%.4f" % (area_ratio, settings["max_page_number_area_ratio"])))
        for title in title_objs:
            tb = estimated_text_hitbox(title)
            tb["w"] += settings["title_decor_gap"]
            if intersects(tb, dbox):
                out.append(issue(sid, decor["id"], "TITLE_DECOR_COLLISION", "title/page-number decorative zone collides or is too close"))
    return out


def check_deck(ir, settings):
    deck = ir.get("deck", {})
    size = deck.get("size", {"w": 1280, "h": 720})
    slides = deck.get("slides", [])
    issues = []
    for slide in slides:
        issues.extend(check_slide(slide, size, settings))

    if len(slides) >= settings["long_deck_min_slides"]:
        large_ghost_count = 0
        w, h = size["w"], size["h"]
        for slide in slides:
            for o in slide.get("objects", []):
                if re.search(r"ghost|page", o.get("id", ""), re.I):
                    b = o.get("box", {})
                    area_ratio = (b.get("w", 0) * b.get("h", 0)) / float(w * h)
                    if area_ratio > settings["max_page_number_area_ratio"]:
                        large_ghost_count += 1
                        break
        ratio = large_ghost_count / float(len(slides) or 1)
        if ratio > settings["max_deck_page_number_ratio"]:
            issues.append(issue("deck", "page-number-system", "REPETITIVE_PAGE_NUMBER_SYSTEM", "large page-number motif appears on %.0f%% of slides; reduce it on content-heavy pages" % (ratio * 100)))
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir_json")
    ap.add_argument("--report", default="")
    ap.add_argument("--safe-margin", type=int, default=48)
    ap.add_argument("--bottom-safe-margin", type=int, default=64)
    ap.add_argument("--max-title-chars", type=int, default=34)
    ap.add_argument("--max-page-number-area-ratio", type=float, default=0.012)
    ap.add_argument("--max-deck-page-number-ratio", type=float, default=0.35)
    ap.add_argument("--long-deck-min-slides", type=int, default=8)
    ap.add_argument("--title-decor-gap", type=int, default=56)
    ap.add_argument("--footer-gap", type=int, default=16)
    ap.add_argument("--text-collision-min-area", type=float, default=40.0)
    ap.add_argument("--text-collision-min-height", type=float, default=3.0)
    ap.add_argument("--metric-inner-pad-x", type=float, default=12.0)
    ap.add_argument("--metric-inner-pad-y", type=float, default=8.0)
    ap.add_argument("--metric-min-vertical-gap", type=float, default=3.0)
    ap.add_argument("--max-table-columns", type=int, default=5)
    ap.add_argument("--max-table-rows", type=int, default=6)
    ap.add_argument("--max-table-cells", type=int, default=28)
    ap.add_argument("--min-table-row-height", type=float, default=38.0)
    ap.add_argument("--table-font-size", type=float, default=10.0)
    ap.add_argument("--max-compliance-body-paragraphs", type=int, default=4)
    ap.add_argument("--container-min-gap", type=float, default=14.0)
    ap.add_argument("--container-overlap-ratio", type=float, default=0.02)
    ap.add_argument("--container-overlap-min-height", type=float, default=4.0)
    ap.add_argument("--title-content-gap", type=float, default=34.0)
    ap.add_argument("--title-text-gap", type=float, default=12.0)
    ap.add_argument("--title-orphan-min-units", type=float, default=4.0)
    ap.add_argument("--alignment-tolerance", type=float, default=8.0)
    ap.add_argument("--edge-alignment-tolerance", type=float, default=8.0)
    args = ap.parse_args(argv)
    settings = vars(args).copy()
    ir = load_json(args.ir_json)
    issues = check_deck(ir, settings)
    blocking = [x for x in issues if x.get("severity") == "blocking"]
    report = {
        "ir": str(args.ir_json),
        "settings": settings,
        "issue_count": len(issues),
        "blocking_count": len(blocking),
        "issues": issues,
        "release_decision": "pass" if not blocking else "fail",
    }
    if args.report:
        Path(args.report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if blocking:
        print("FAIL layout safety: %d blocking issues" % len(blocking))
        for x in blocking[:30]:
            print("- {slide} {object} {code}: {message}".format(**x))
        if len(blocking) > 30:
            print("... %d more" % (len(blocking) - 30))
        return 1
    print("PASS layout safety: 0 blocking issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
