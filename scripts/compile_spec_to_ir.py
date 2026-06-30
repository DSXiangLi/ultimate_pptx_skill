#!/usr/bin/env python3
"""Compile content contracts into Ultimate PPTX Slide IR.

Phase 1 keeps a simple default compiler. The glass-fintech showcase adds a
style-specific compiler branch so one visual style can run end-to-end at high
quality before adding more styles.
"""
from pathlib import Path
import argparse
import json
TEXT_RENDER_SCALE = 1.30

DEFAULT_SIZE = {"w": 1280, "h": 720}
FONT = "Microsoft YaHei"

PALETTE = {
    "background": "07111F",
    "panel": "13243A",
    "panel_alt": "19324D",
    "stroke": "5ED7FF",
    "stroke_soft": "2A6F91",
    "accent": "7C3AED",
    "positive": "31D0AA",
    "warning": "FBBF24",
    "text": "EAF7FF",
    "muted": "B6C7D8",
    "white": "FFFFFF",
}


def edit(level="text", priority=5, can=None):
    return {"level": level, "priority": priority, "user_can_edit": can or ["text", "position", "style"]}


def text_obj(oid, role, text, x, y, w, h, z, size, color="111827", bold=False, priority=5, opacity=1.0):
    return {
        "id": oid,
        "type": "text",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "text": text,
        "style": {"font": FONT, "size": size, "color": color, "bold": bold, "opacity": opacity},
        "editability": edit("text", priority),
        "render_policy": "native",
    }


def shape_obj(oid, role, x, y, w, h, z, fill="FFFFFF", stroke="D1D5DB", shape="roundRect", priority=3, opacity=1.0, stroke_opacity=1.0, shadow=False):
    return {
        "id": oid,
        "type": "shape",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "shape": shape,
        "fill": fill,
        "stroke": stroke,
        "opacity": opacity,
        "stroke_opacity": stroke_opacity,
        "shadow": shadow,
        "editability": edit("style", priority, ["fill", "stroke", "position"]),
        "render_policy": "native",
    }


def chart_obj(oid, chart, x, y, w, h, z):
    return {
        "id": oid,
        "type": "chart",
        "role": "chart",
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "kind": chart.get("kind", "stacked-bar"),
        "title": chart.get("title", ""),
        "unit": chart.get("unit", ""),
        "categories": chart.get("categories", []),
        "series": chart.get("series", []),
        "source": chart.get("source", ""),
        "style": {
            "font": FONT,
            "title_color": PALETTE["text"],
            "label_color": PALETTE["muted"],
            "grid_color": PALETTE["stroke_soft"],
            "panel_fill": PALETTE["panel"],
            "panel_stroke": PALETTE["stroke_soft"],
            "opacity": 0.50,
            "stroke_opacity": 0.75,
        },
        "editability": edit("vector-chart", 5, ["data", "text", "position", "style"]),
        "render_policy": "native-vector-group",
    }



def table_obj(oid, table, x, y, w, h, z):
    return {
        "id": oid,
        "type": "table",
        "role": "table",
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "title": table.get("title", ""),
        "columns": table.get("columns", []),
        "rows": table.get("rows", []),
        "source": table.get("source", ""),
        "style": {
            "font": FONT,
            "title_color": PALETTE["text"],
            "label_color": PALETTE["muted"],
            "header_fill": "19324D",
            "row_fill": PALETTE["panel"],
            "row_alt_fill": "102135",
            "stroke": PALETTE["stroke_soft"],
            "opacity": 0.54,
            "stroke_opacity": 0.75,
        },
        "editability": edit("vector-table", 5, ["data", "text", "position", "style"]),
        "render_policy": "native-vector-group",
    }


def normalize_z(objects):
    for idx, obj in enumerate(sorted(objects, key=lambda o: (o.get("z", 0), o.get("id", "")))):
        obj["z"] = idx
    return objects


def add_body_paragraphs(objects, sid, body, x, y, w, line_h, z, size=16, max_items=3, gap=10):
    yy = y
    for i, paragraph in enumerate(body[:max_items], start=1):
        h = max(float(line_h), estimate_text_height(paragraph, w, size) + 2)
        objects.append(text_obj("%s_body_%d" % (sid, i), "body", paragraph, x, yy, w, h, z + i, size, color=PALETTE["text"], priority=5))
        yy += h + gap


def add_process(objects, sid, steps, x, y, w, h, z):
    if not steps:
        return
    gap = 18
    step_w = (w - gap * (len(steps) - 1)) / len(steps)
    for i, step in enumerate(steps, start=1):
        sx = x + (i - 1) * (step_w + gap)
        tone = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"], PALETTE["stroke"]][(i - 1) % 4]
        objects.append(shape_obj("%s_process_%d_card" % (sid, i), "process-step", sx, y, step_w, h, z + i * 10, fill=PALETTE["panel_alt"], stroke=tone, opacity=0.56, stroke_opacity=0.9, shadow=True))
        objects.append(text_obj("%s_process_%d_num" % (sid, i), "process-step", step.get("step", "%02d" % i), sx + 18, y + 16, 54, 30, z + i * 10 + 1, 18, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_process_%d_title" % (sid, i), "process-step", step.get("title", ""), sx + 18, y + 54, step_w - 36, 30, z + i * 10 + 2, 18, color=PALETTE["text"], bold=True, priority=5))
        objects.append(text_obj("%s_process_%d_text" % (sid, i), "process-step", step.get("text", ""), sx + 18, y + 94, step_w - 36, h - 108, z + i * 10 + 3, 13, color=PALETTE["muted"], priority=5))


def add_matrix(objects, sid, matrix, x, y, w, h, z):
    cells = matrix.get("cells", [])
    x_labels = matrix.get("x_labels", [])
    y_labels = matrix.get("y_labels", [])
    objects.append(text_obj(sid + "_matrix_title", "body", matrix.get("title", ""), x, y - 36, w, 30, z, 18, color=PALETTE["text"], bold=True, priority=5))
    rows = len(cells) or 1
    cols = max((len(r) for r in cells), default=1)
    label_w = 92
    label_h = 30
    cell_w = (w - label_w) / cols
    cell_h = (h - label_h) / rows
    for c, lab in enumerate(x_labels[:cols]):
        objects.append(text_obj("%s_matrix_x_%d" % (sid, c), "matrix-cell", lab, x + label_w + c * cell_w, y, cell_w, 24, z + 1 + c, 12, color=PALETTE["muted"], bold=True, priority=5))
    for r, row in enumerate(cells):
        objects.append(text_obj("%s_matrix_y_%d" % (sid, r), "matrix-cell", y_labels[r] if r < len(y_labels) else "", x, y + label_h + r * cell_h + 16, label_w - 8, 28, z + 20 + r, 12, color=PALETTE["muted"], bold=True, priority=5))
        for c, txt in enumerate(row):
            intensity = [0.64, 0.48, 0.36][min(r, 2)]
            stroke = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"]][min(c, 2)]
            cx = x + label_w + c * cell_w
            cy = y + label_h + r * cell_h
            objects.append(shape_obj("%s_matrix_%d_%d_cell" % (sid, r, c), "matrix-cell", cx + 4, cy + 4, cell_w - 8, cell_h - 8, z + 40 + r * cols + c, fill=PALETTE["panel_alt"], stroke=stroke, opacity=intensity, stroke_opacity=0.75, shadow=False))
            objects.append(text_obj("%s_matrix_%d_%d_text" % (sid, r, c), "matrix-cell", txt, cx + 18, cy + 18, cell_w - 36, cell_h - 24, z + 80 + r * cols + c, 14, color=PALETTE["text"], priority=5))


def add_timeline(objects, sid, timeline, x, y, w, h, z):
    if not timeline:
        return
    objects.append(shape_obj(sid + "_timeline_line", "timeline-step", x + 28, y + h / 2, w - 56, 2, z, fill=PALETTE["stroke"], stroke=PALETTE["stroke"], shape="rect", priority=2, opacity=0.65, stroke_opacity=0))
    gap = w / len(timeline)
    for i, item in enumerate(timeline, start=1):
        cx = x + (i - 0.5) * gap
        tone = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"], PALETTE["stroke"], PALETTE["positive"]][(i - 1) % 5]
        objects.append(shape_obj("%s_timeline_%d_dot" % (sid, i), "timeline-step", cx - 16, y + h / 2 - 16, 32, 32, z + i * 10, fill=tone, stroke=tone, shape="ellipse", priority=3, opacity=0.9, stroke_opacity=0))
        objects.append(text_obj("%s_timeline_%d_date" % (sid, i), "timeline-step", item.get("date", ""), cx - gap/2 + 8, y + 18, gap - 16, 24, z + i * 10 + 1, 12, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_timeline_%d_title" % (sid, i), "timeline-step", item.get("title", ""), cx - gap/2 + 8, y + h/2 + 28, gap - 16, 28, z + i * 10 + 2, 14, color=PALETTE["text"], bold=True, priority=5))
        objects.append(text_obj("%s_timeline_%d_text" % (sid, i), "timeline-step", item.get("text", ""), cx - gap/2 + 8, y + h/2 + 62, gap - 16, 48, z + i * 10 + 3, 11, color=PALETTE["muted"], priority=5))


def add_scenarios(objects, sid, scenarios, x, y, w, h, z):
    if not scenarios:
        return
    gap = 24
    card_w = (w - gap * (len(scenarios)-1)) / len(scenarios)
    for i, sc in enumerate(scenarios, start=1):
        sx = x + (i-1)*(card_w+gap)
        tone = [PALETTE["positive"], PALETTE["warning"], PALETTE["accent"]][(i-1)%3]
        objects.append(shape_obj("%s_scenario_%d_card" % (sid, i), "scenario-card", sx, y, card_w, h, z+i*10, fill=PALETTE["panel_alt"], stroke=tone, opacity=0.56, stroke_opacity=0.86, shadow=True))
        objects.append(text_obj("%s_scenario_%d_name" % (sid, i), "body", sc.get("name", ""), sx+24, y+24, card_w-48, 32, z+i*10+1, 20, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_scenario_%d_impact" % (sid, i), "metric", sc.get("impact", ""), sx+24, y+76, card_w-48, 42, z+i*10+2, 26, color=PALETTE["text"], bold=True, priority=5))
        objects.append(text_obj("%s_scenario_%d_action" % (sid, i), "body", sc.get("action", ""), sx+24, y+138, card_w-48, 60, z+i*10+3, 15, color=PALETTE["muted"], priority=5))

def raster_bg():
    return {
        "id": "bg_texture",
        "type": "rasterIsland",
        "role": "background",
        "box": {"x": 0, "y": 0, "w": 1280, "h": 720},
        "z": 0,
        "editability": {"level": "replaceable", "priority": 1, "user_can_edit": ["replace", "regenerate"]},
        "render_policy": "raster",
        "source": {"kind": "texture", "regenerable": True, "description": "style-program generated background texture"},
        "must_not_contain": ["title", "body", "risk", "source", "chart-data"],
    }


def compile_slide(slide):
    objects = [raster_bg()]
    objects.append(text_obj("title", "title", slide["title"], 80, 64, 860, 92, 10, 34, bold=True))
    body = slide.get("body", [])
    card_h = 240 if len(body) <= 2 else 300
    objects.append(shape_obj("body_card", "supporting-card", 80, 190, 720, card_h, 5))
    y = 230
    for idx, paragraph in enumerate(body, start=1):
        objects.append(text_obj("body_%d" % idx, "body", paragraph, 118, y, 650, 74, 11 + idx, 20, color="1F2937"))
        y += 86
    risk = slide.get("risk_note") or slide.get("source") or ""
    if risk:
        objects.append(text_obj("risk_note", "risk", risk, 80, 650, 1120, 32, 30, 10, color="6B7280"))
    return {"id": slide["id"], "objects": objects}


def tone_color(tone):
    return {
        "positive": PALETTE["positive"],
        "warning": PALETTE["warning"],
        "accent": PALETTE["accent"],
    }.get(tone, PALETTE["stroke"])


def text_units(text):
    text = str(text or "")
    cjk = sum(1 for c in text if ord(c) > 127)
    ascii_chars = max(0, len(text) - cjk)
    return cjk * 1.0 + ascii_chars * 0.55


def estimate_lines(text, width, size):
    usable_w = max(1.0, float(width) * 0.88)
    return max(1, int(__import__("math").ceil((text_units(text) * float(size) * TEXT_RENDER_SCALE) / usable_w)))


def estimate_text_height(text, width, size):
    lines = estimate_lines(text, width, size)
    if lines > 1:
        return lines * size * 1.38 + max(8, size * 0.55)
    return lines * size * 1.05


def last_line_units(text, width, size):
    capacity = max(1.0, float(width) * 0.88 / max(size * TEXT_RENDER_SCALE, 1))
    total = text_units(text)
    if total <= capacity:
        return total
    return total - capacity * int((total - 0.001) // capacity)


def fit_title_size(text, width, preferred_size, min_size=26):
    size = preferred_size
    while size > min_size and estimate_lines(text, width, size) > 1 and last_line_units(text, width, size) < 4.0:
        size -= 1
    return size


def add_metric(objects, prefix, metric, x, y, w, h, z):
    c = tone_color(metric.get("tone"))
    objects.append(shape_obj(prefix + "_card", "metric-card", x, y, w, h, z, fill=PALETTE["panel_alt"], stroke=c, opacity=0.58, stroke_opacity=0.88, shadow=True))
    # Intrinsic metric-card layout. Never position value and delta by fixed
    # absolute offsets; allocate a vertical text stack that fits the card.
    compact = h < 100
    pad_x = 24
    if h < 90:
        pad_top, pad_bottom, gap = 8, 6, 4
        label_h, value_h, delta_h = 16, 27, 16
        label_size, value_size, delta_size = 10, 19, 10
    elif compact:
        pad_top, pad_bottom, gap = 10, 8, 4
        label_h, value_h, delta_h = 16, 27, 16
        label_size, value_size, delta_size = 10, 19, 10
    else:
        pad_top, pad_bottom, gap = 16, 10, 5
        label_h, value_h, delta_h = 22, 38, 18
        label_size, value_size, delta_size = 12, 27, 11
    needed = pad_top + label_h + gap + value_h + gap + delta_h + pad_bottom
    if needed > h:
        # Last-resort shrink for unusual cards. Validation will still catch
        # impossible cards, but the compiler should degrade gracefully.
        overflow = needed - h
        value_h = max(22, value_h - overflow)
        value_size = max(17, value_size - int(round(overflow / 3.0)))
    label_y = y + pad_top
    value_y = label_y + label_h + gap
    delta_y = value_y + value_h + gap
    objects.append(text_obj(prefix + "_label", "metric-label", metric.get("label", ""), x + pad_x, label_y, w - 2 * pad_x, label_h, z + 1, label_size, color=PALETTE["muted"], priority=4))
    objects.append(text_obj(prefix + "_value", "metric", metric.get("value", ""), x + pad_x, value_y, w - 2 * pad_x, value_h, z + 2, value_size, color=PALETTE["text"], bold=True, priority=5))
    objects.append(text_obj(prefix + "_delta", "metric-note", metric.get("delta", ""), x + pad_x, delta_y, w - 2 * pad_x, delta_h, z + 3, delta_size, color=c, priority=4))
    objects.append(shape_obj(prefix + "_glow", "decorative-glow", x + w - 48, y + 18, 24, 24, z + 4, fill=c, stroke=c, shape="ellipse", priority=1, opacity=0.42, stroke_opacity=0.0))


def glass_frame(objects, slide_id):
    objects.append(shape_obj(slide_id + "_bg", "background", 0, 0, 1280, 720, 0, fill=PALETTE["background"], stroke=PALETTE["background"], shape="rect", priority=2))
    objects.append(shape_obj(slide_id + "_orb_cyan", "decorative-glow", 870, -70, 360, 360, 1, fill=PALETTE["stroke"], stroke=PALETTE["stroke"], shape="ellipse", priority=1, opacity=0.16, stroke_opacity=0.0))
    objects.append(shape_obj(slide_id + "_orb_violet", "decorative-glow", -120, 410, 330, 330, 2, fill=PALETTE["accent"], stroke=PALETTE["accent"], shape="ellipse", priority=1, opacity=0.13, stroke_opacity=0.0))
    objects.append(shape_obj(slide_id + "_top_hairline", "divider", 64, 42, 1152, 2, 3, fill=PALETTE["stroke"], stroke=PALETTE["stroke"], shape="rect", priority=2, opacity=0.85, stroke_opacity=0.0))
    objects.append(shape_obj(slide_id + "_risk_rail", "risk-rail", 64, 618, 1152, 30, 80, fill="0B1828", stroke=PALETTE["stroke_soft"], shape="roundRect", priority=3, opacity=0.58, stroke_opacity=0.62, shadow=False))


def compile_glass_slide(slide, index):
    sid = slide["id"]
    objects = []
    topology = slide.get("topology", "glass-dashboard")
    metrics = slide.get("metrics", [])
    body = slide.get("body", [])
    glass_frame(objects, sid)
    objects.append(text_obj(sid + "_kicker", "kicker", slide.get("kicker", ""), 80, 58, 560, 30, 10, 13, color=PALETTE["stroke"], bold=True, priority=4))
    objects.append(text_obj(sid + "_ghost_num", "decorative-ghost-number", "%02d" % index, 1110, 54, 96, 52, 11, 38, color=PALETTE["white"], bold=True, priority=1, opacity=0.026))
    title_w = 720 if topology in {"glass-cover", "glass-hero"} else 960
    content_heavy = {"glass-dashboard", "glass-table", "glass-chart-focus", "glass-matrix", "glass-scenario", "glass-process", "glass-timeline", "glass-compliance", "glass-quote", "glass-action-rail"}
    preferred_title_size = 30 if topology in {"glass-cover", "glass-hero"} else (28 if topology in content_heavy or len(slide.get("title", "")) > 30 else 32)
    title_size = fit_title_size(slide["title"], title_w, preferred_title_size)
    title_h = max(88, estimate_text_height(slide["title"], title_w, title_size) + 8)
    objects.append(text_obj(sid + "_title", "title", slide["title"], 80, 96, title_w, title_h, 20, title_size, color=PALETTE["text"], bold=True, priority=5))
    show_subtitle = topology in {"glass-cover", "glass-hero", "glass-dashboard"}
    if slide.get("subtitle") and show_subtitle:
        subtitle_y = 96 + title_h + 12
        subtitle_h = max(28, estimate_text_height(slide["subtitle"], 760, 15) + 4)
        objects.append(text_obj(sid + "_subtitle", "body", slide["subtitle"], 84, subtitle_y, 760, subtitle_h, 21, 15, color=PALETTE["muted"], priority=5))

    if topology in {"glass-cover", "glass-hero"}:
        objects.append(shape_obj(sid + "_hero_panel", "glass-panel", 64, 78, 744, 262, 15, fill=PALETTE["panel"], stroke=PALETTE["stroke"], opacity=0.52, stroke_opacity=0.7, shadow=True))
        objects.append(shape_obj(sid + "_body_panel", "glass-panel", 64, 386, 744, 210, 30, fill=PALETTE["panel"], stroke=PALETTE["stroke_soft"], opacity=0.52, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 420, 674, 50, 35, 17, 2)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 850, 118 + (i - 1) * 152, 330, 126, 40 + (i - 1) * 10)
    elif topology == "glass-dashboard":
        objects.append(shape_obj(sid + "_left_panel", "glass-panel", 64, 236, 520, 140, 30, fill=PALETTE["panel"], stroke=PALETTE["stroke_soft"], opacity=0.52, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 266, 448, 38, 35, 15, 2)
        if slide.get("chart"):
            objects.append(chart_obj(sid + "_chart", slide["chart"], 96, 396, 448, 180, 39))
        positions = [(640, 230), (930, 230), (640, 390), (930, 390)]
        for i, metric in enumerate(metrics[:4], start=1):
            x, y0 = positions[i - 1]
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, x, y0, 246, 126, 45 + (i - 1) * 10)
    elif topology == "glass-chart-focus":
        objects.append(shape_obj(sid + "_note_panel", "glass-panel", 64, 232, 360, 240, 30, fill=PALETTE["panel"], stroke=PALETTE["stroke_soft"], opacity=0.52, stroke_opacity=0.75, shadow=True))
        add_body_paragraphs(objects, sid, body, 92, 264, 306, 48, 35, 14, 3)
        if slide.get("chart"):
            objects.append(chart_obj(sid + "_chart", slide["chart"], 462, 232, 716, 240, 44))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 500, 320, 92, 70 + i * 10)
    elif topology == "glass-table":
        # The table object already exports its own editable vector panel; avoid
        # an additional outer glass panel that creates a double-container frame.
        if slide.get("table"):
            objects.append(table_obj(sid + "_table", slide["table"], 86, 272, 1108, 316, 40))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 166, 320, 86, 55 + i * 10)
    elif topology == "glass-matrix":
        objects.append(shape_obj(sid + "_matrix_panel", "glass-panel", 64, 250, 760, 342, 30, fill=PALETTE["panel"], stroke=PALETTE["stroke_soft"], opacity=0.48, stroke_opacity=0.75, shadow=True))
        add_matrix(objects, sid, slide.get("matrix", {}), 92, 302, 704, 258, 40)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 870, 176 + (i-1)*140, 306, 124, 80+i*10)
    elif topology == "glass-scenario":
        add_body_paragraphs(objects, sid, body, 88, 246, 1040, 36, 30, 15, 1)
        add_scenarios(objects, sid, slide.get("scenarios", []), 84, 318, 1112, 166, 44)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 80 + i * 10)
    elif topology == "glass-process":
        add_body_paragraphs(objects, sid, body, 88, 238, 1040, 36, 30, 15, 1)
        add_process(objects, sid, slide.get("process", []), 84, 306, 1112, 174, 44)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 502, 320, 92, 90 + i * 10)
    elif topology == "glass-timeline":
        add_body_paragraphs(objects, sid, body, 88, 238, 1040, 36, 30, 15, 1)
        add_timeline(objects, sid, slide.get("timeline", []), 84, 298, 1112, 196, 44)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 110 + i * 10)
    elif topology == "glass-quote":
        q = slide.get("quote", {})
        objects.append(shape_obj(sid + "_quote_panel", "glass-panel", 122, 256, 1036, 228, 30, fill=PALETTE["panel"], stroke=PALETTE["stroke"], opacity=0.52, stroke_opacity=0.8, shadow=True))
        objects.append(text_obj(sid + "_quote_mark", "quote-mark", "“", 150, 256, 90, 80, 40, 72, color=PALETTE["stroke"], bold=True, priority=2, opacity=0.8))
        objects.append(text_obj(sid + "_quote_text", "quote", q.get("text", body[0] if body else ""), 230, 304, 850, 78, 42, 32, color=PALETTE["text"], bold=True, priority=5))
        objects.append(text_obj(sid + "_quote_author", "quote", q.get("author", ""), 234, 410, 620, 30, 43, 15, color=PALETTE["muted"], priority=5))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 80 + i * 10)
    elif topology == "glass-compliance":
        objects.append(shape_obj(sid + "_compliance_panel", "glass-panel", 64, 252, 1152, 328, 30, fill=PALETTE["panel"], stroke=PALETTE["warning"], opacity=0.48, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 286, 1050, 58, 40, 16, 5)
        # Compliance pages should be calmer than dashboard pages; avoid bottom KPI noise.
        for i, metric in enumerate(metrics[:0], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 506, 320, 70, 90 + i * 10)
    else:
        # Keep KPI cards and explanatory text as separate zones; one big panel
        # behind both reads as cards pressing into another container.
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 64 + (i - 1) * 392, 278, 368, 132, 42 + (i - 1) * 10)
        objects.append(shape_obj(sid + "_body_panel", "glass-panel", 64, 428, 1152, 96, 70, fill=PALETTE["panel"], stroke=PALETTE["stroke_soft"], opacity=0.44, stroke_opacity=0.65, shadow=True))
        add_body_paragraphs(objects, sid, body, 112, 450, 1040, 34, 75, 16, 2)
    if slide.get("risk_note"):
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 88, 623, 1090, 22, 900, 10, color=PALETTE["muted"], priority=5))
    return {"id": sid, "objects": normalize_z(objects)}


def compile_glass_contract(contract):
    return {
        "deck": {
            "id": contract.get("deck_id", "glass-fintech-showcase"),
            "size": contract.get("size", DEFAULT_SIZE),
            "style_program": contract.get("style_program"),
            "slides": [compile_glass_slide(s, i) for i, s in enumerate(contract["slides"], start=1)],
        }
    }


def compile_contract(contract):
    if "slides" not in contract or not contract["slides"]:
        raise ValueError("content contract requires at least one slide")
    if contract.get("style_program") == "glass-fintech-pptx":
        return compile_glass_contract(contract)
    return {
        "deck": {
            "id": contract.get("deck_id", "untitled-deck"),
            "size": contract.get("size", DEFAULT_SIZE),
            "style_program": contract.get("style_program"),
            "slides": [compile_slide(s) for s in contract["slides"]],
        }
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="content contract JSON")
    ap.add_argument("output", help="output Slide IR JSON")
    args = ap.parse_args(argv)
    contract = json.loads(Path(args.input).read_text(encoding="utf-8"))
    ir = compile_contract(contract)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(ir, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote %s" % args.output)


if __name__ == "__main__":
    main()
