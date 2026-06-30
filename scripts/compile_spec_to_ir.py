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


VARIANT_PROFILES = {
    "default": {
        "name": "default",
        "visual_grammar": {
            "motif": "orb",
            "panel_material": "balanced-glass",
            "metric_style": "standard-kpi",
            "footer_treatment": "standard-footer",
            "layout_rhythm": "balanced-dashboard",
            "chart_treatment": "balanced-vector",
        },
        "palette": {},
        "orb_cyan": {"x": 870, "y": -70, "w": 360, "h": 360, "opacity": 0.16, "role": "decorative-glow"},
        "orb_violet": {"x": -120, "y": 410, "w": 330, "h": 330, "opacity": 0.13, "role": "decorative-glow"},
        "ghost_opacity": 0.026,
        "ghost_size": 38,
        "hairline_opacity": 0.85,
        "panel_opacity": 0.52,
        "metric_card_opacity": 0.58,
        "metric_value_size": 27,
        "risk_fill": "0B1828",
        "risk_opacity": 0.58,
        "risk_stroke_opacity": 0.62,
        "risk_height": 30,
        "extra_grid": False,
        "gold_orb": False,
    },
    "matte-institutional": {
        "name": "matte-institutional",
        "visual_grammar": {
            "motif": "strict-grid",
            "panel_material": "matte-glass",
            "metric_style": "formal-compact",
            "footer_treatment": "formal-source-band",
            "layout_rhythm": "strict-institutional-grid",
            "chart_treatment": "subdued-grid-vector",
        },
        "palette": {"background": "08111A", "panel": "111B25", "panel_alt": "151F2B", "stroke": "83B7CC", "stroke_soft": "2E4758", "accent": "5F6F80", "warning": "B9964B", "muted": "D1D9E2", "text": "F4FAFF"},
        "orb_cyan": {"x": 928, "y": -42, "w": 260, "h": 260, "opacity": 0.055, "role": "decorative-glow"},
        "orb_violet": {"x": -72, "y": 482, "w": 220, "h": 220, "opacity": 0.035, "role": "decorative-glow"},
        "ghost_opacity": 0.010,
        "ghost_size": 28,
        "hairline_opacity": 0.52,
        "panel_opacity": 0.46,
        "metric_card_opacity": 0.48,
        "metric_value_size": 23,
        "risk_fill": "08121D",
        "risk_opacity": 0.76,
        "risk_stroke_opacity": 0.78,
        "risk_height": 34,
        "extra_grid": True,
        "gold_orb": False,
        "chart": {"series_palette": ["67E8F9", "8B5CF6", "FBBF24"], "axis_style": "hud-grid-axis", "legend_style": "terminal-legend", "marker_style": "glow-square", "bar_shape": "roundRect", "panel_opacity": 0.46, "grid_opacity": 0.34, "label_color": "B8C2CC", "value_label_color": "E6EEF5"},
        "fonts": {"title": "Bahnschrift SemiBold", "body": "Microsoft YaHei", "metric": "Consolas", "caption": "Microsoft YaHei"},
    },
    "luminous-glass": {
        "name": "luminous-glass",
        "visual_grammar": {
            "motif": "spotlight-orb",
            "panel_material": "luminous-glass",
            "metric_style": "hero-kpi",
            "footer_treatment": "presentation-source-band",
            "layout_rhythm": "asymmetric-presentation-flow",
            "chart_treatment": "spotlight-chart-vector",
        },
        "palette": {"background": "071326", "panel": "142A46", "panel_alt": "1C3D60", "stroke": "67E8F9", "stroke_soft": "328BB5", "accent": "A78BFA", "warning": "FACC15", "positive": "34D399"},
        "orb_cyan": {"x": 760, "y": -132, "w": 520, "h": 520, "opacity": 0.28, "role": "spotlight-orb"},
        "orb_violet": {"x": -190, "y": 318, "w": 470, "h": 470, "opacity": 0.22, "role": "spotlight-orb"},
        "ghost_opacity": 0.060,
        "ghost_size": 48,
        "hairline_opacity": 0.98,
        "panel_opacity": 0.56,
        "metric_card_opacity": 0.66,
        "metric_value_size": 31,
        "risk_fill": "0B1B31",
        "risk_opacity": 0.54,
        "risk_stroke_opacity": 0.70,
        "risk_height": 30,
        "extra_grid": False,
        "gold_orb": True,
    },
    "terminal-cockpit": {
        "name": "terminal-cockpit",
        "visual_grammar": {
            "motif": "terminal-grid",
            "panel_material": "dense-cockpit",
            "metric_style": "status-chip",
            "footer_treatment": "monitoring-status-bar",
            "layout_rhythm": "dense-operational-cockpit",
            "chart_treatment": "monitoring-grid-vector",
        },
        "palette": {"background": "020806", "panel": "07130F", "panel_alt": "0A1C16", "stroke": "22D3A6", "stroke_soft": "13543F", "accent": "7DD3FC", "warning": "F59E0B", "positive": "22C55E", "muted": "9DB9AE", "text": "D8FFF2"},
        "orb_cyan": {"x": 1030, "y": -18, "w": 170, "h": 170, "opacity": 0.035, "role": "decorative-glow"},
        "orb_violet": {"x": -42, "y": 520, "w": 160, "h": 160, "opacity": 0.018, "role": "decorative-glow"},
        "ghost_opacity": 0.018,
        "ghost_size": 30,
        "hairline_opacity": 0.68,
        "panel_opacity": 0.60,
        "metric_card_opacity": 0.62,
        "metric_value_size": 22,
        "risk_fill": "07111A",
        "risk_opacity": 0.84,
        "risk_stroke_opacity": 0.85,
        "risk_height": 38,
        "extra_grid": True,
        "gold_orb": False,
    },
}


def variant_profile(contract):
    language = contract.get("visual_language") or contract.get("visual_variant") or contract.get("variant") or "default"
    return VARIANT_PROFILES.get(language, VARIANT_PROFILES["default"])



def vp(profile, key):
    return (profile or {}).get(key, VARIANT_PROFILES["default"].get(key))


def pal(profile, key):
    overrides = (profile or {}).get("palette", {})
    if key in overrides:
        return overrides[key]
    return PALETTE.get(key, PALETTE.get("text", "111827"))

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


def text_obj(oid, role, text, x, y, w, h, z, size, color="111827", bold=False, priority=5, opacity=1.0, font=None):
    return {
        "id": oid,
        "type": "text",
        "role": role,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "z": z,
        "text": text,
        "style": {"font": font or FONT, "size": size, "color": color, "bold": bold, "opacity": opacity},
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


def chart_obj(oid, chart, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
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
            "font": profile.get("fonts", {}).get("body") or profile.get("fonts", {}).get("chart") or FONT,
            "title_font": profile.get("fonts", {}).get("title") or profile.get("fonts", {}).get("body") or FONT,
            "title_color": pal(profile, "text"),
            "label_color": profile.get("chart", {}).get("label_color", pal(profile, "muted")),
            "grid_color": pal(profile, "stroke_soft"),
            "panel_fill": pal(profile, "panel"),
            "panel_stroke": pal(profile, "stroke_soft"),
            "opacity": profile.get("chart", {}).get("panel_opacity", 0.42 if profile.get("name") == "matte-institutional" else (0.58 if profile.get("name") == "luminous-glass" else 0.54)),
            "stroke_opacity": 0.62 if profile.get("name") == "matte-institutional" else (0.90 if profile.get("name") == "luminous-glass" else 0.82),
            "chart_treatment": profile.get("visual_grammar", {}).get("chart_treatment"),
            "series_palette": profile.get("chart", {}).get("series_palette", []),
            "axis_style": profile.get("chart", {}).get("axis_style"),
            "legend_style": profile.get("chart", {}).get("legend_style"),
            "marker_style": profile.get("chart", {}).get("marker_style"),
            "bar_shape": profile.get("chart", {}).get("bar_shape", "rect"),
            "grid_opacity": profile.get("chart", {}).get("grid_opacity", 0.22),
            "value_label_color": profile.get("chart", {}).get("value_label_color", "EAF7FF"),
        },
        "editability": edit("vector-chart", 5, ["data", "text", "position", "style"]),
        "render_policy": "native-vector-group",
    }



def table_obj(oid, table, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
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
            "title_color": pal(profile, "text"),
            "label_color": pal(profile, "muted"),
            "header_fill": pal(profile, "panel_alt"),
            "row_fill": pal(profile, "panel"),
            "row_alt_fill": "0B1A28" if profile.get("name") == "terminal-cockpit" else "102135",
            "stroke": pal(profile, "stroke_soft"),
            "opacity": 0.48 if profile.get("name") == "matte-institutional" else (0.58 if profile.get("name") == "terminal-cockpit" else 0.54),
            "stroke_opacity": 0.82 if profile.get("name") in {"matte-institutional", "terminal-cockpit"} else 0.75,
            "panel_material": profile.get("visual_grammar", {}).get("panel_material"),
        },
        "editability": edit("vector-table", 5, ["data", "text", "position", "style"]),
        "render_policy": "native-vector-group",
    }


def normalize_z(objects):
    for idx, obj in enumerate(sorted(objects, key=lambda o: (o.get("z", 0), o.get("id", "")))):
        obj["z"] = idx
    return objects


def add_body_paragraphs(objects, sid, body, x, y, w, line_h, z, size=16, max_items=3, gap=10, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    yy = y
    for i, paragraph in enumerate(body[:max_items], start=1):
        h = max(float(line_h), estimate_text_height(paragraph, w, size) + 2)
        objects.append(text_obj("%s_body_%d" % (sid, i), "body", paragraph, x, yy, w, h, z + i, size, color=pal(profile, "text"), priority=5))
        yy += h + gap


def add_process(objects, sid, steps, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    if not steps:
        return
    gap = 18
    step_w = (w - gap * (len(steps) - 1)) / len(steps)
    for i, step in enumerate(steps, start=1):
        sx = x + (i - 1) * (step_w + gap)
        tone = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"], PALETTE["stroke"]][(i - 1) % 4]
        objects.append(shape_obj("%s_process_%d_card" % (sid, i), "process-step", sx, y, step_w, h, z + i * 10, fill=pal(profile, "panel_alt"), stroke=tone, opacity=0.56, stroke_opacity=0.9, shadow=True))
        objects.append(text_obj("%s_process_%d_num" % (sid, i), "process-step", step.get("step", "%02d" % i), sx + 18, y + 16, 54, 30, z + i * 10 + 1, 18, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_process_%d_title" % (sid, i), "process-step", step.get("title", ""), sx + 18, y + 54, step_w - 36, 30, z + i * 10 + 2, 18, color=pal(profile, "text"), bold=True, priority=5))
        objects.append(text_obj("%s_process_%d_text" % (sid, i), "process-step", step.get("text", ""), sx + 18, y + 94, step_w - 36, h - 108, z + i * 10 + 3, 13, color=pal(profile, "muted"), priority=5))


def add_matrix(objects, sid, matrix, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    cells = matrix.get("cells", [])
    x_labels = matrix.get("x_labels", [])
    y_labels = matrix.get("y_labels", [])
    objects.append(text_obj(sid + "_matrix_title", "body", matrix.get("title", ""), x, y - 36, w, 30, z, 18, color=pal(profile, "text"), bold=True, priority=5))
    rows = len(cells) or 1
    cols = max((len(r) for r in cells), default=1)
    label_w = 92
    label_h = 30
    cell_w = (w - label_w) / cols
    cell_h = (h - label_h) / rows
    for c, lab in enumerate(x_labels[:cols]):
        objects.append(text_obj("%s_matrix_x_%d" % (sid, c), "matrix-cell", lab, x + label_w + c * cell_w, y, cell_w, 24, z + 1 + c, 12, color=pal(profile, "muted"), bold=True, priority=5))
    for r, row in enumerate(cells):
        objects.append(text_obj("%s_matrix_y_%d" % (sid, r), "matrix-cell", y_labels[r] if r < len(y_labels) else "", x, y + label_h + r * cell_h + 16, label_w - 8, 28, z + 20 + r, 12, color=pal(profile, "muted"), bold=True, priority=5))
        for c, txt in enumerate(row):
            intensity = [0.64, 0.48, 0.36][min(r, 2)]
            stroke = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"]][min(c, 2)]
            cx = x + label_w + c * cell_w
            cy = y + label_h + r * cell_h
            objects.append(shape_obj("%s_matrix_%d_%d_cell" % (sid, r, c), "matrix-cell", cx + 4, cy + 4, cell_w - 8, cell_h - 8, z + 40 + r * cols + c, fill=pal(profile, "panel_alt"), stroke=stroke, opacity=intensity, stroke_opacity=0.75, shadow=False))
            objects.append(text_obj("%s_matrix_%d_%d_text" % (sid, r, c), "matrix-cell", txt, cx + 18, cy + 18, cell_w - 36, cell_h - 24, z + 80 + r * cols + c, 14, color=pal(profile, "text"), priority=5))


def add_timeline(objects, sid, timeline, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    if not timeline:
        return
    objects.append(shape_obj(sid + "_timeline_line", "timeline-step", x + 28, y + h / 2, w - 56, 2, z, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="rect", priority=2, opacity=0.65, stroke_opacity=0))
    gap = w / len(timeline)
    for i, item in enumerate(timeline, start=1):
        cx = x + (i - 0.5) * gap
        tone = [PALETTE["positive"], PALETTE["accent"], PALETTE["warning"], PALETTE["stroke"], PALETTE["positive"]][(i - 1) % 5]
        objects.append(shape_obj("%s_timeline_%d_dot" % (sid, i), "timeline-step", cx - 16, y + h / 2 - 16, 32, 32, z + i * 10, fill=tone, stroke=tone, shape="ellipse", priority=3, opacity=0.9, stroke_opacity=0))
        objects.append(text_obj("%s_timeline_%d_date" % (sid, i), "timeline-step", item.get("date", ""), cx - gap/2 + 8, y + 18, gap - 16, 24, z + i * 10 + 1, 12, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_timeline_%d_title" % (sid, i), "timeline-step", item.get("title", ""), cx - gap/2 + 8, y + h/2 + 28, gap - 16, 28, z + i * 10 + 2, 14, color=pal(profile, "text"), bold=True, priority=5))
        objects.append(text_obj("%s_timeline_%d_text" % (sid, i), "timeline-step", item.get("text", ""), cx - gap/2 + 8, y + h/2 + 62, gap - 16, 48, z + i * 10 + 3, 11, color=pal(profile, "muted"), priority=5))


def add_scenarios(objects, sid, scenarios, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    if not scenarios:
        return
    gap = 24
    card_w = (w - gap * (len(scenarios)-1)) / len(scenarios)
    for i, sc in enumerate(scenarios, start=1):
        sx = x + (i-1)*(card_w+gap)
        tone = [PALETTE["positive"], PALETTE["warning"], PALETTE["accent"]][(i-1)%3]
        objects.append(shape_obj("%s_scenario_%d_card" % (sid, i), "scenario-card", sx, y, card_w, h, z+i*10, fill=pal(profile, "panel_alt"), stroke=tone, opacity=0.56, stroke_opacity=0.86, shadow=True))
        objects.append(text_obj("%s_scenario_%d_name" % (sid, i), "body", sc.get("name", ""), sx+24, y+24, card_w-48, 32, z+i*10+1, 20, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_scenario_%d_impact" % (sid, i), "metric", sc.get("impact", ""), sx+24, y+76, card_w-48, 42, z+i*10+2, 26, color=pal(profile, "text"), bold=True, priority=5))
        objects.append(text_obj("%s_scenario_%d_action" % (sid, i), "body", sc.get("action", ""), sx+24, y+138, card_w-48, 60, z+i*10+3, 15, color=pal(profile, "muted"), priority=5))

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



def fit_title_size_no_orphan(text, width, preferred_size, min_size=20):
    size = fit_title_size(text, width, preferred_size, min_size=min_size)
    while size > min_size:
        lines = estimate_lines(text, width, size)
        if lines <= 1:
            return size
        capacity_units = max(1.0, float(width) * 0.88 / max(float(size), 1.0))
        total = text_units(text)
        last_units = total - capacity_units * int((total - 0.001) // capacity_units)
        if last_units >= 4.0:
            return size
        size -= 1
    return size

def add_metric(objects, prefix, metric, x, y, w, h, z, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    c = tone_color(metric.get("tone"))
    name = profile.get("name", "default")
    metric_style = profile.get("visual_grammar", {}).get("metric_style", "standard-kpi")
    card_role = "metric-card"
    if metric_style == "status-chip":
        card_role = "status-chip"
    card_fill = pal(profile, "panel_alt")
    card_stroke = c if name != "matte-institutional" else pal(profile, "stroke_soft")
    card_opacity = profile.get("metric_card_opacity", 0.58)
    stroke_opacity = 0.74 if name == "matte-institutional" else (0.96 if name == "luminous-glass" else 0.88)
    card_shape = "rect" if metric_style == "status-chip" else "roundRect"
    card_shadow = True if name == "luminous-glass" else False
    objects.append(shape_obj(prefix + "_card", card_role, x, y, w, h, z, fill=card_fill, stroke=card_stroke, shape=card_shape, opacity=card_opacity, stroke_opacity=stroke_opacity, shadow=card_shadow))
    if metric_style == "hero-kpi":
        objects.append(shape_obj(prefix + "_hero_bar", "luminous-ribbon", x, y, max(5, w), 5, z + 1, fill=c, stroke=c, shape="rect", priority=1, opacity=0.88, stroke_opacity=0.0))
    elif metric_style == "status-chip":
        objects.append(shape_obj(prefix + "_status_dot", "status-chip", x + 14, y + 14, 12, 12, z + 1, fill=c, stroke=c, shape="ellipse", priority=2, opacity=0.96, stroke_opacity=0.0))
    elif metric_style == "formal-compact":
        objects.append(shape_obj(prefix + "_ruler", "institutional-ruler", x + 16, y + h - 14, max(20, w - 32), 1, z + 1, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.55, stroke_opacity=0.0))
    # Intrinsic metric-card layout. Never position value and delta by fixed
    # absolute offsets; allocate a vertical text stack that fits the card.
    compact = h < 100 or metric_style in {"formal-compact", "status-chip"}
    pad_x = 30 if metric_style == "status-chip" else 24
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
        label_size, value_size, delta_size = 12, int(profile.get("metric_value_size", 27)), 11
    if metric_style == "hero-kpi" and h >= 100:
        value_size = max(value_size, int(profile.get("metric_value_size", 31)))
        value_h = max(value_h, 42)
    needed = pad_top + label_h + gap + value_h + gap + delta_h + pad_bottom
    if needed > h:
        overflow = needed - h
        value_h = max(22, value_h - overflow)
        value_size = max(17, value_size - int(round(overflow / 3.0)))
    label_y = y + pad_top
    value_y = label_y + label_h + gap
    delta_y = value_y + value_h + gap
    objects.append(text_obj(prefix + "_label", "metric-label", metric.get("label", ""), x + pad_x, label_y, w - 2 * pad_x, label_h, z + 2, label_size, color=pal(profile, "muted"), priority=4))
    objects.append(text_obj(prefix + "_value", "metric", metric.get("value", ""), x + pad_x, value_y, w - 2 * pad_x, value_h, z + 3, value_size, color=pal(profile, "text"), bold=True, priority=5))
    objects.append(text_obj(prefix + "_delta", "metric-note", metric.get("delta", ""), x + pad_x, delta_y, w - 2 * pad_x, delta_h, z + 4, delta_size, color=c, priority=4))
    glow_role = "spotlight-orb" if metric_style == "hero-kpi" else "decorative-glow"
    glow_opacity = 0.58 if metric_style == "hero-kpi" else (0.28 if metric_style == "formal-compact" else 0.42)
    objects.append(shape_obj(prefix + "_glow", glow_role, x + w - 48, y + 18, 24, 24, z + 5, fill=c, stroke=c, shape="ellipse", priority=1, opacity=glow_opacity, stroke_opacity=0.0))


def glass_frame(objects, slide_id, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    name = profile.get("name", "default")
    cyan = profile["orb_cyan"]
    violet = profile["orb_violet"]
    objects.append(shape_obj(slide_id + "_bg", "background", 0, 0, 1280, 720, 0, fill=pal(profile, "background"), stroke=pal(profile, "background"), shape="rect", priority=2))
    objects.append(shape_obj(slide_id + "_orb_cyan", cyan.get("role", "decorative-glow"), cyan["x"], cyan["y"], cyan["w"], cyan["h"], 1, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="ellipse", priority=1, opacity=cyan["opacity"], stroke_opacity=0.0))
    objects.append(shape_obj(slide_id + "_orb_violet", violet.get("role", "decorative-glow"), violet["x"], violet["y"], violet["w"], violet["h"], 2, fill=pal(profile, "accent"), stroke=pal(profile, "accent"), shape="ellipse", priority=1, opacity=violet["opacity"], stroke_opacity=0.0))
    if profile.get("gold_orb"):
        objects.append(shape_obj(slide_id + "_orb_gold", "spotlight-orb", 1000, 392, 260, 260, 3, fill=pal(profile, "warning"), stroke=pal(profile, "warning"), shape="ellipse", priority=1, opacity=0.16, stroke_opacity=0.0))
    if name == "luminous-glass":
        objects.append(shape_obj(slide_id + "_luminous_ribbon", "luminous-ribbon", 64, 50, 520, 8, 5, fill=pal(profile, "warning"), stroke=pal(profile, "warning"), shape="rect", priority=1, opacity=0.72, stroke_opacity=0.0))
        objects.append(shape_obj(slide_id + "_luminous_sweep", "luminous-ribbon", 820, 104, 310, 14, 6, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="roundRect", priority=1, opacity=0.34, stroke_opacity=0.0))
    if name == "matte-institutional":
        for gi, gx in enumerate([224, 384, 544, 704, 864, 1024], start=1):
            objects.append(shape_obj("%s_grid_v_%d" % (slide_id, gi), "institutional-gridline", gx, 64, 1, 520, 4 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.12, stroke_opacity=0.0))
        for gi, gy in enumerate([188, 332, 476], start=1):
            objects.append(shape_obj("%s_grid_h_%d" % (slide_id, gi), "institutional-ruler", 64, gy, 1152, 1, 12 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.14, stroke_opacity=0.0))
    elif name == "terminal-cockpit":
        objects.append(shape_obj(slide_id + "_terminal_top_status", "terminal-status-bar", 64, 48, 1152, 26, 72, fill="04100C", stroke=pal(profile, "stroke_soft"), shape="rect", priority=2, opacity=0.92, stroke_opacity=0.75))
        objects.append(text_obj(slide_id + "_terminal_path", "terminal-status-bar", "SYS / ALLOCATION / LIVE SIGNAL", 82, 53, 420, 18, 73, 10, color=pal(profile, "stroke"), bold=True, priority=2, opacity=0.9))
        objects.append(shape_obj(slide_id + "_terminal_left_rail", "terminal-status-bar", 48, 88, 6, 500, 74, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="rect", priority=1, opacity=0.42, stroke_opacity=0.0))
        for gi, gx in enumerate(range(88, 1216, 64), start=1):
            objects.append(shape_obj("%s_terminal_v_%d" % (slide_id, gi), "terminal-gridline", gx, 80, 1, 506, 4 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.26, stroke_opacity=0.0))
        for gi, gy in enumerate(range(104, 600, 48), start=1):
            objects.append(shape_obj("%s_terminal_h_%d" % (slide_id, gi), "terminal-gridline", 64, gy, 1152, 1, 30 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.22, stroke_opacity=0.0))
        for ci, (cx, tone) in enumerate([(82, "positive"), (112, "warning"), (142, "accent")], start=1):
            objects.append(shape_obj("%s_status_chip_%d" % (slide_id, ci), "status-chip", cx, 626, 18, 10, 82 + ci, fill=pal(profile, tone), stroke=pal(profile, tone), shape="rect", priority=2, opacity=0.96, stroke_opacity=0.0))
    elif profile.get("extra_grid"):
        for gi, gx in enumerate([320, 640, 960], start=1):
            objects.append(shape_obj("%s_grid_v_%d" % (slide_id, gi), "divider", gx, 48, 1, 548, 4 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.10, stroke_opacity=0.0))
    objects.append(shape_obj(slide_id + "_top_hairline", "divider", 64, 42, 1152, 2, 70, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="rect", priority=2, opacity=profile.get("hairline_opacity", 0.85), stroke_opacity=0.0))
    risk_h = profile.get("risk_height", 30)
    risk_y = 648 - risk_h
    risk_shape = "rect" if name == "terminal-cockpit" else "roundRect"
    objects.append(shape_obj(slide_id + "_risk_rail", "risk-rail", 64, risk_y, 1152, risk_h, 80, fill=profile.get("risk_fill", "0B1828"), stroke=pal(profile, "stroke_soft"), shape=risk_shape, priority=3, opacity=profile.get("risk_opacity", 0.58), stroke_opacity=profile.get("risk_stroke_opacity", 0.62), shadow=False))


def compile_glass_slide(slide, index, profile=None):
    profile = profile or VARIANT_PROFILES["default"]
    sid = slide["id"]
    objects = []
    topology = slide.get("topology", "glass-dashboard")
    metrics = slide.get("metrics", [])
    body = slide.get("body", [])
    glass_frame(objects, sid, profile)
    objects.append(text_obj(sid + "_kicker", "kicker", slide.get("kicker", ""), 80, 58, 560, 30, 10, 13, color=pal(profile, "stroke"), bold=True, priority=4))
    name = profile.get("name", "default")
    if name == "terminal-cockpit":
        objects.append(text_obj(sid + "_terminal_page", "terminal-page-node", "NODE-%02d" % index, 1030, 53, 150, 22, 11, 14, color=pal(profile, "stroke"), bold=True, priority=2, opacity=0.96))
    elif name == "matte-institutional":
        objects.append(text_obj(sid + "_folio", "institutional-folio", "%02d" % index, 1130, 62, 58, 30, 11, 22, color=pal(profile, "muted"), bold=True, priority=1, opacity=0.55))
    else:
        objects.append(text_obj(sid + "_ghost_num", "decorative-ghost-number", "%02d" % index, 1110, 54, 96, 52, 11, 38, color=pal(profile, "white"), bold=True, priority=1, opacity=profile.get("ghost_opacity", 0.026)))
    title_w = 720 if topology in {"glass-cover", "glass-hero"} else 960
    content_heavy = {"glass-dashboard", "glass-table", "glass-chart-focus", "glass-matrix", "glass-scenario", "glass-process", "glass-timeline", "glass-compliance", "glass-quote", "glass-action-rail"}
    preferred_title_size = 30 if topology in {"glass-cover", "glass-hero"} else (28 if topology in content_heavy or len(slide.get("title", "")) > 30 else 32)
    title_size = fit_title_size(slide["title"], title_w, preferred_title_size)
    title_h = max(88, estimate_text_height(slide["title"], title_w, title_size) + 8)
    objects.append(text_obj(sid + "_title", "title", slide["title"], 80, 96, title_w, title_h, 20, title_size, color=pal(profile, "text"), bold=True, priority=5))
    show_subtitle = topology in {"glass-cover", "glass-hero", "glass-dashboard"}
    if slide.get("subtitle") and show_subtitle:
        subtitle_y = 96 + title_h + 12
        subtitle_h = max(28, estimate_text_height(slide["subtitle"], 760, 15) + 4)
        objects.append(text_obj(sid + "_subtitle", "body", slide["subtitle"], 84, subtitle_y, 760, subtitle_h, 21, 15, color=pal(profile, "muted"), priority=5))

    if topology in {"glass-cover", "glass-hero"}:
        objects.append(shape_obj(sid + "_hero_panel", "glass-panel", 64, 78, 744, 262, 15, fill=pal(profile, "panel"), stroke=pal(profile, "stroke"), opacity=0.52, stroke_opacity=0.7, shadow=True))
        objects.append(shape_obj(sid + "_body_panel", "glass-panel", 64, 386, 744, 204, 30, fill=pal(profile, "panel"), stroke=pal(profile, "stroke_soft"), opacity=0.52, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 420, 674, 50, 35, 17, 2, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 850, 118 + (i - 1) * 152, 330, 126, 40 + (i - 1) * 10, profile)
    elif topology == "glass-dashboard":
        objects.append(shape_obj(sid + "_left_panel", "glass-panel", 64, 236, 520, 140, 30, fill=pal(profile, "panel"), stroke=pal(profile, "stroke_soft"), opacity=0.52, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 266, 448, 38, 35, 15, 2, profile=profile)
        if slide.get("chart"):
            objects.append(chart_obj(sid + "_chart", slide["chart"], 96, 396, 448, 180, 39, profile))
        positions = [(640, 230), (930, 230), (640, 390), (930, 390)]
        for i, metric in enumerate(metrics[:4], start=1):
            x, y0 = positions[i - 1]
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, x, y0, 246, 126, 45 + (i - 1) * 10, profile)
    elif topology == "glass-chart-focus":
        objects.append(shape_obj(sid + "_note_panel", "glass-panel", 64, 232, 360, 240, 30, fill=pal(profile, "panel"), stroke=pal(profile, "stroke_soft"), opacity=0.52, stroke_opacity=0.75, shadow=True))
        add_body_paragraphs(objects, sid, body, 92, 264, 306, 48, 35, 14, 3, profile=profile)
        if slide.get("chart"):
            objects.append(chart_obj(sid + "_chart", slide["chart"], 462, 232, 716, 240, 44, profile))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 500, 320, 92, 70 + i * 10, profile)
    elif topology == "glass-table":
        # The table object already exports its own editable vector panel; avoid
        # an additional outer glass panel that creates a double-container frame.
        if slide.get("table"):
            objects.append(table_obj(sid + "_table", slide["table"], 86, 272, 1108, 316, 40, profile))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 166, 320, 86, 55 + i * 10, profile)
    elif topology == "glass-matrix":
        objects.append(shape_obj(sid + "_matrix_panel", "glass-panel", 64, 250, 760, 342, 30, fill=pal(profile, "panel"), stroke=pal(profile, "stroke_soft"), opacity=0.48, stroke_opacity=0.75, shadow=True))
        add_matrix(objects, sid, slide.get("matrix", {}), 92, 302, 704, 258, 40, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 870, 176 + (i-1)*140, 306, 124, 80+i*10, profile)
    elif topology == "glass-scenario":
        add_body_paragraphs(objects, sid, body, 88, 246, 1040, 36, 30, 15, 1, profile=profile)
        add_scenarios(objects, sid, slide.get("scenarios", []), 84, 318, 1112, 166, 44, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 80 + i * 10, profile)
    elif topology == "glass-process":
        add_body_paragraphs(objects, sid, body, 88, 238, 1040, 36, 30, 15, 1, profile=profile)
        add_process(objects, sid, slide.get("process", []), 84, 306, 1112, 174, 44, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 502, 320, 92, 90 + i * 10, profile)
    elif topology == "glass-timeline":
        add_body_paragraphs(objects, sid, body, 88, 238, 1040, 36, 30, 15, 1, profile=profile)
        add_timeline(objects, sid, slide.get("timeline", []), 84, 298, 1112, 196, 44, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 110 + i * 10, profile)
    elif topology == "glass-quote":
        q = slide.get("quote", {})
        objects.append(shape_obj(sid + "_quote_panel", "glass-panel", 122, 256, 1036, 228, 30, fill=pal(profile, "panel"), stroke=pal(profile, "stroke"), opacity=0.52, stroke_opacity=0.8, shadow=True))
        objects.append(text_obj(sid + "_quote_mark", "quote-mark", "“", 150, 256, 90, 80, 40, 72, color=pal(profile, "stroke"), bold=True, priority=2, opacity=0.8))
        objects.append(text_obj(sid + "_quote_text", "quote", q.get("text", body[0] if body else ""), 230, 304, 850, 78, 42, 32, color=pal(profile, "text"), bold=True, priority=5))
        objects.append(text_obj(sid + "_quote_author", "quote", q.get("author", ""), 234, 410, 620, 30, 43, 15, color=pal(profile, "muted"), priority=5))
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 504, 320, 90, 80 + i * 10, profile)
    elif topology == "glass-compliance":
        objects.append(shape_obj(sid + "_compliance_panel", "glass-panel", 64, 252, 1152, 328, 30, fill=PALETTE["panel"], stroke=PALETTE["warning"], opacity=0.48, stroke_opacity=0.8, shadow=True))
        add_body_paragraphs(objects, sid, body, 96, 286, 1050, 58, 40, 16, 5, profile=profile)
        # Compliance pages should be calmer than dashboard pages; avoid bottom KPI noise.
        for i, metric in enumerate(metrics[:0], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 506, 320, 70, 90 + i * 10, profile)
    else:
        # Keep KPI cards and explanatory text as separate zones; one big panel
        # behind both reads as cards pressing into another container.
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 64 + (i - 1) * 392, 278, 368, 132, 42 + (i - 1) * 10, profile)
        objects.append(shape_obj(sid + "_body_panel", "glass-panel", 64, 428, 1152, 96, 70, fill=pal(profile, "panel"), stroke=pal(profile, "stroke_soft"), opacity=0.44, stroke_opacity=0.65, shadow=True))
        add_body_paragraphs(objects, sid, body, 112, 450, 1040, 34, 75, 16, 2, profile=profile)
    if slide.get("risk_note"):
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 88, 623, 1090, 22, 900, 10, color=pal(profile, "muted"), priority=5))
    apply_text_dna(objects, profile)
    return {"id": sid, "objects": normalize_z(objects)}



VISUAL_SYSTEM_PROFILES = {
    "paper-analyst-report": {
        "visual_language": "editorial-ledger",
        "visual_system_grammar": {
            "surface": "warm-paper-research",
            "composition": "editorial-report-grid",
            "material": "paper-ink",
            "chromatic_mode": "warm-light-low-saturation",
            "container_grammar": "thin-rules-ledger-cards",
        },
        "palette": {"background": "F7F2E8", "paper": "FFFDF7", "ink": "17202A", "muted": "5B6570", "rule": "B9A77F", "accent": "315C72", "positive": "3E7C59", "warning": "A36B2D", "panel": "F2EBDC", "panel_alt": "EBE2D0", "stroke_soft": "D4C3A0", "text": "17202A", "white": "FFFFFF"},
        "fonts": {"title": "Georgia", "body": "Aptos", "metric": "Georgia", "caption": "Aptos"},
        "chart": {"series_palette": ["315C72", "7D8F69", "C08B3E"], "axis_style": "print-thin-axis", "legend_style": "caption-ledger", "marker_style": "small-square", "bar_shape": "rect", "panel_opacity": 1.0, "grid_opacity": 0.28, "label_color": "5B6570", "value_label_color": "17202A"},
        "container": {"metric_shape": "rect", "scenario_shape": "rect", "process_shape": "rect", "metric_shadow": False, "metric_opacity": 1.0, "metric_stroke_opacity": 0.95},
    },
    "market-atlas-infographic": {
        "visual_language": "modular-market-map",
        "visual_system_grammar": {
            "surface": "atlas-map-canvas",
            "composition": "modular-infographic-map",
            "material": "flat-map-tiles",
            "chromatic_mode": "sand-mint-cartographic",
            "container_grammar": "map-tiles-route-lines",
        },
        "palette": {"background": "DCEBE1", "paper": "FBFFF8", "ink": "0B2B24", "muted": "2C5148", "rule": "579A86", "accent": "1457A8", "positive": "187956", "warning": "B86414", "panel": "D2E8DA", "panel_alt": "BFDCCB", "stroke_soft": "4E927E", "text": "0B2B24", "white": "FFFFFF"},
        "fonts": {"title": "Aptos Display", "body": "Aptos", "metric": "Arial Narrow", "caption": "Aptos"},
        "chart": {"series_palette": ["1457A8", "187956", "B86414"], "axis_style": "coordinate-grid-axis", "legend_style": "map-legend", "marker_style": "route-node", "bar_shape": "roundRect", "panel_opacity": 0.72, "grid_opacity": 0.46, "label_color": "2C5148", "value_label_color": "0B2B24"},
        "container": {"metric_shape": "roundRect", "scenario_shape": "roundRect", "process_shape": "roundRect", "metric_shadow": False, "metric_opacity": 0.94, "metric_stroke_opacity": 0.88},
    },
}


def system_pal(profile, key):
    return profile["palette"].get(key, PALETTE.get(key, "111827"))


def system_tone_color(profile, tone):
    return {
        "positive": system_pal(profile, "positive"),
        "warning": system_pal(profile, "warning"),
        "accent": system_pal(profile, "accent"),
    }.get(tone, system_pal(profile, "accent"))


def system_font(profile, role):
    fonts = profile.get("fonts", {})
    if role in {"title", "kicker"}:
        return fonts.get("title") or FONT
    if role in {"metric", "metric-label", "metric-note"}:
        return fonts.get("metric") or fonts.get("body") or FONT
    if role in {"risk", "research-folio"}:
        return fonts.get("caption") or fonts.get("body") or FONT
    return fonts.get("body") or FONT


def system_text_obj(profile, oid, role, text, x, y, w, h, z, size, color="111827", bold=False, priority=5, opacity=1.0):
    return text_obj(oid, role, text, x, y, w, h, z, size, color=color, bold=bold, priority=priority, opacity=opacity, font=system_font(profile, role))


def container_value(profile, key, default=None):
    return profile.get("container", {}).get(key, default)


def apply_text_dna(objects, profile):
    for obj in objects:
        if obj.get("type") == "text":
            role = obj.get("role", "")
            obj.setdefault("style", {})["font"] = system_font(profile, role)
    return objects


def chart_profile_for_system(profile):
    chart = profile.get("chart", {})
    fonts = profile.get("fonts", {})
    return {
        "name": profile["visual_language"],
        "palette": {
            "text": system_pal(profile, "ink"),
            "muted": system_pal(profile, "muted"),
            "stroke_soft": system_pal(profile, "stroke_soft"),
            "panel": system_pal(profile, "paper"),
        },
        "fonts": fonts,
        "chart": chart,
        "visual_grammar": {"chart_treatment": profile["visual_system_grammar"]["composition"]},
    }


def add_system_metric(objects, prefix, metric, x, y, w, h, z, profile, role="ledger-metric"):
    tone = system_tone_color(profile, metric.get("tone"))
    shape = container_value(profile, "metric_shape", "rect")
    opacity = container_value(profile, "metric_opacity", 0.96)
    stroke_opacity = container_value(profile, "metric_stroke_opacity", 0.90)
    shadow = container_value(profile, "metric_shadow", False)
    is_atlas = role == "map-tile"
    objects.append(shape_obj(prefix + "_card", role, x, y, w, h, z, fill=system_pal(profile, "paper"), stroke=tone if is_atlas else system_pal(profile, "stroke_soft"), shape=shape, opacity=opacity, stroke_opacity=stroke_opacity, shadow=shadow))
    if is_atlas:
        objects.append(shape_obj(prefix + "_node", "route-line", x + 10, y + 12, 14, 14, z + 1, fill=tone, stroke=tone, shape="ellipse", priority=2, opacity=0.95, stroke_opacity=0.0))
        objects.append(system_text_obj(profile, prefix + "_label", "metric-label", metric.get("label", ""), x + 32, y + 10, w - 44, 18, z + 2, 9, color=system_pal(profile, "muted"), bold=True, priority=4))
        objects.append(system_text_obj(profile, prefix + "_value", "metric", metric.get("value", ""), x + 16, y + 34, w - 28, 32, z + 3, 21, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(system_text_obj(profile, prefix + "_delta", "metric-note", metric.get("delta", ""), x + 16, y + 70, w - 28, 18, z + 4, 9, color=tone, priority=4))
    else:
        objects.append(shape_obj(prefix + "_rule", "editorial-rule", x, y, 4, h, z + 1, fill=tone, stroke=tone, shape="rect", priority=2, opacity=0.92, stroke_opacity=0.0))
        objects.append(system_text_obj(profile, prefix + "_label", "metric-label", metric.get("label", ""), x + 18, y + 10, w - 36, 18, z + 2, 9, color=system_pal(profile, "muted"), bold=True, priority=4))
        objects.append(system_text_obj(profile, prefix + "_value", "metric", metric.get("value", ""), x + 18, y + 31, w - 36, 34, z + 3, 24, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(system_text_obj(profile, prefix + "_delta", "metric-note", metric.get("delta", ""), x + 18, y + 66, w - 36, 18, z + 4, 9, color=tone, priority=4))


def paper_frame(objects, sid, index, slide):
    profile = VISUAL_SYSTEM_PROFILES["paper-analyst-report"]
    objects.append(shape_obj(sid + "_bg", "background", 0, 0, 1280, 720, 0, fill=system_pal(profile, "background"), stroke=system_pal(profile, "background"), shape="rect", priority=1))
    objects.append(shape_obj(sid + "_sheet", "paper-sheet", 54, 38, 1172, 632, 1, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=2, opacity=1.0, stroke_opacity=0.9, shadow=False))
    objects.append(shape_obj(sid + "_top_rule", "editorial-rule", 82, 82, 1116, 2, 5, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.9, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_folio", "research-folio", "INSTITUTIONAL RESEARCH / %02d" % index, 84, 56, 300, 20, 6, 9, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(text_obj(sid + "_report_code", "research-folio", "EXHIBIT %02d · STRATEGY MEMO · AS-OF 2026Q3" % index, 842, 56, 350, 20, 6, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(shape_obj(sid + "_left_margin_rule", "editorial-rule", 82, 118, 3, 470, 6, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.52, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_kicker", "kicker", slide.get("kicker", ""), 96, 94, 480, 24, 10, 11, color=system_pal(profile, "accent"), bold=True, priority=4))


def atlas_frame(objects, sid, index, slide):
    profile = VISUAL_SYSTEM_PROFILES["market-atlas-infographic"]
    objects.append(shape_obj(sid + "_bg", "atlas-canvas", 0, 0, 1280, 720, 0, fill=system_pal(profile, "background"), stroke=system_pal(profile, "background"), shape="rect", priority=1))
    objects.append(shape_obj(sid + "_zone_left", "background", 64, 104, 630, 500, 1, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "panel"), shape="rect", priority=1, opacity=0.36, stroke_opacity=0.0))
    objects.append(shape_obj(sid + "_zone_right", "background", 730, 202, 470, 330, 1, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.72, stroke_opacity=0.35))
    objects.append(shape_obj(sid + "_zone_bottom", "background", 72, 412, 1138, 158, 1, fill=system_pal(profile, "panel_alt"), stroke=system_pal(profile, "panel_alt"), shape="rect", priority=1, opacity=0.30, stroke_opacity=0.0))
    for gx in [96, 256, 416, 576, 736, 896, 1056, 1216]:
        objects.append(shape_obj("%s_grid_v_%d" % (sid, gx), "atlas-gridline", gx, 52, 1, 590, 2, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=1, opacity=0.22, stroke_opacity=0.0))
    for gy in [118, 238, 358, 478, 598]:
        objects.append(shape_obj("%s_grid_h_%d" % (sid, gy), "atlas-gridline", 64, gy, 1152, 1, 2, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=1, opacity=0.20, stroke_opacity=0.0))
    objects.append(shape_obj(sid + "_route_primary", "route-line", 88, 160, 1060, 8, 4, fill=system_pal(profile, "accent"), stroke=system_pal(profile, "accent"), shape="rect", priority=2, opacity=0.38, stroke_opacity=0.0))
    objects.append(shape_obj(sid + "_route_secondary", "route-line", 190, 540, 880, 6, 4, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.30, stroke_opacity=0.0))
    for n, (nx, ny, tone) in enumerate([(716, 156, "accent"), (748, 536, "positive"), (1160, 156, "warning")], start=1):
        objects.append(shape_obj("%s_node_%d" % (sid, n), "route-line", nx, ny, 18, 18, 5, fill=system_tone_color(profile, tone), stroke=system_tone_color(profile, tone), shape="rect", priority=2, opacity=0.88, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_folio", "research-folio", "MARKET ATLAS / ZONE-%02d" % index, 80, 54, 300, 22, 8, 10, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(text_obj(sid + "_legend_1", "research-folio", "SIGNAL FIELD", 760, 206, 160, 18, 8, 9, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(text_obj(sid + "_legend_2", "research-folio", "ALLOCATION ROUTE", 92, 402, 220, 18, 8, 9, color=system_pal(profile, "positive"), bold=True, priority=2))
    objects.append(text_obj(sid + "_kicker", "kicker", slide.get("kicker", ""), 82, 84, 520, 24, 10, 11, color=system_pal(profile, "accent"), bold=True, priority=4))


def compile_paper_slide(slide, index):
    profile = VISUAL_SYSTEM_PROFILES["paper-analyst-report"]
    sid = slide["id"]
    objects = []
    body = slide.get("body", [])
    metrics = slide.get("metrics", [])
    paper_frame(objects, sid, index, slide)
    paper_title_w = 600 if index == 1 else 820
    paper_title_size = 23 if index == 1 else 30
    title_size = fit_title_size_no_orphan(slide["title"], paper_title_w, paper_title_size, min_size=20)
    title_h = max(76, estimate_text_height(slide["title"], paper_title_w, title_size) + 8)
    objects.append(text_obj(sid + "_title", "title", slide["title"], 96, 126, paper_title_w, title_h, 20, title_size, color=system_pal(profile, "ink"), bold=True, priority=5))
    if slide.get("subtitle"):
        objects.append(text_obj(sid + "_subtitle", "body", slide.get("subtitle", ""), 98, 126 + title_h + 8, 780, 32, 21, 13, color=system_pal(profile, "muted"), priority=5))
    objects.append(shape_obj(sid + "_body_rule", "editorial-rule", 96, 244, 812, 1, 24, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.75, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_exhibit_label", "research-folio", "EXHIBIT %02d / EVIDENCE CHAIN" % index, 96, 224, 280, 18, 25, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
    add_body_paragraphs(objects, sid, body, 104, 268, 710, 42, 30, size=15, max_items=3, gap=10, profile={"palette": {"text": system_pal(profile, "ink"), "muted": system_pal(profile, "muted")}, "fonts": profile.get("fonts", {})})
    objects.append(shape_obj(sid + "_analyst_note_box", "analyst-note", 690, 268, 176, 96, 38, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "rule"), shape="rect", priority=3, opacity=1.0, stroke_opacity=0.55))
    objects.append(text_obj(sid + "_analyst_note_k", "research-folio", "ANALYST NOTE", 704, 280, 140, 16, 39, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
    objects.append(text_obj(sid + "_analyst_note_t", "body", "结论优先，证据随后；所有数值保留为可编辑对象。", 704, 304, 140, 42, 40, 9, color=system_pal(profile, "muted"), priority=2))
    for i, metric in enumerate(metrics[:4], start=1):
        add_system_metric(objects, "%s_metric_%d" % (sid, i), metric, 918, 108 + (i - 1) * 94, 244, 88, 42 + i * 10, profile, role="ledger-metric")
    if slide.get("chart"):
        objects.append(chart_obj(sid + "_chart", slide["chart"], 96, 402, 770, 184, 70, chart_profile_for_system(profile)))
    elif slide.get("scenarios"):
        objects.append(shape_obj(sid + "_scenario_table", "analyst-note", 96, 396, 770, 176, 70, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "rule"), shape="rect", priority=3, opacity=1.0, stroke_opacity=0.62))
        objects.append(text_obj(sid + "_scenario_head", "research-folio", "SCENARIO ASSUMPTIONS / TRIGGER RESPONSE", 112, 410, 430, 16, 72, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
        for i, sc in enumerate(slide.get("scenarios", [])[:3], start=1):
            y0 = 434 + (i - 1) * 42
            objects.append(shape_obj("%s_scenario_%d_rule" % (sid, i), "editorial-rule", 112, y0 - 8, 722, 1, 73 + i, fill=system_pal(profile, "stroke_soft"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=2, opacity=0.72, stroke_opacity=0.0))
            objects.append(text_obj("%s_scenario_%d_name" % (sid, i), "body", sc.get("name", ""), 112, y0, 86, 22, 80 + i, 12, color=system_pal(profile, "accent"), bold=True, priority=5))
            objects.append(text_obj("%s_scenario_%d_impact" % (sid, i), "metric", sc.get("impact", ""), 218, y0, 230, 28, 90 + i, 15, color=system_pal(profile, "ink"), bold=True, priority=5))
            objects.append(text_obj("%s_scenario_%d_action" % (sid, i), "body", sc.get("action", ""), 486, y0, 320, 26, 100 + i, 10, color=system_pal(profile, "muted"), priority=5))
    elif slide.get("process"):
        objects.append(shape_obj(sid + "_process_checklist", "analyst-note", 96, 394, 770, 182, 70, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "rule"), shape="rect", priority=3, opacity=1.0, stroke_opacity=0.62))
        objects.append(text_obj(sid + "_process_head", "research-folio", "EXECUTION CHECKLIST / COMMITTEE TRACKING", 112, 408, 430, 16, 72, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
        for i, step in enumerate(slide.get("process", [])[:4], start=1):
            y0 = 432 + (i - 1) * 34
            objects.append(shape_obj("%s_process_%d_box" % (sid, i), "editorial-rule", 112, y0 + 2, 16, 16, 80 + i, fill="FFFDF7", stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=1.0, stroke_opacity=0.9))
            objects.append(text_obj("%s_process_%d_num" % (sid, i), "process-step", step.get("step", ""), 136, y0, 42, 20, 82 + i, 10, color=system_pal(profile, "accent"), bold=True, priority=5))
            objects.append(text_obj("%s_process_%d_title" % (sid, i), "process-step", step.get("title", ""), 184, y0, 110, 20, 84 + i, 11, color=system_pal(profile, "ink"), bold=True, priority=5))
            objects.append(text_obj("%s_process_%d_text" % (sid, i), "process-step", step.get("text", ""), 318, y0, 470, 22, 88 + i, 9, color=system_pal(profile, "muted"), priority=5))
    if slide.get("risk_note"):
        objects.append(shape_obj(sid + "_source_band", "research-folio", 82, 606, 1116, 1, 890, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.72, stroke_opacity=0.0))
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 86, 618, 1092, 28, 900, 9, color=system_pal(profile, "muted"), priority=5))
    apply_text_dna(objects, profile)
    return {"id": sid, "objects": normalize_z(objects)}


def compile_atlas_slide(slide, index):
    profile = VISUAL_SYSTEM_PROFILES["market-atlas-infographic"]
    sid = slide["id"]
    objects = []
    body = slide.get("body", [])
    metrics = slide.get("metrics", [])
    atlas_frame(objects, sid, index, slide)
    atlas_title_w = 600
    title_size = fit_title_size_no_orphan(slide["title"], atlas_title_w, 23, min_size=20)
    title_h = max(70, estimate_text_height(slide["title"], atlas_title_w, title_size) + 8)
    objects.append(text_obj(sid + "_title", "title", slide["title"], 82, 112, atlas_title_w, title_h, 20, title_size, color=system_pal(profile, "ink"), bold=True, priority=5))
    if slide.get("subtitle"):
        objects.append(text_obj(sid + "_subtitle", "body", slide.get("subtitle", ""), 84, 112 + title_h + 8, 560, 46, 21, 12, color=system_pal(profile, "muted"), priority=5))
    add_body_paragraphs(objects, sid, body, 88, 238, 470, 38, 30, size=14, max_items=3, gap=10, profile={"palette": {"text": system_pal(profile, "ink"), "muted": system_pal(profile, "muted")}})
    tile_positions = [(760, 214), (1000, 214), (1000, 354), (760, 354)] if slide.get("process") else [(760, 230), (1000, 230), (760, 362), (1000, 362)]
    for i, metric in enumerate(metrics[:4], start=1):
        x, y = tile_positions[i - 1]
        add_system_metric(objects, "%s_metric_%d" % (sid, i), metric, x, y, 190, 100, 42 + i * 10, profile, role="map-tile")
    if slide.get("chart"):
        objects.append(chart_obj(sid + "_chart", slide["chart"], 88, 430, 640, 154, 78, chart_profile_for_system(profile)))
    elif slide.get("scenarios"):
        for i, sc in enumerate(slide.get("scenarios", [])[:3], start=1):
            x = 610 + (i - 1) * 190
            objects.append(shape_obj("%s_scenario_%d" % (sid, i), "map-tile", x, 430, 170, 120, 78 + i, fill=system_pal(profile, "paper"), stroke=system_tone_color(profile, ["positive", "warning", "accent"][(i - 1) % 3]), shape="rect", priority=3, opacity=0.96, stroke_opacity=0.88))
            objects.append(text_obj("%s_scenario_%d_name" % (sid, i), "body", sc.get("name", ""), x + 12, 444, 146, 20, 84 + i, 12, color=system_pal(profile, "accent"), bold=True, priority=5))
            objects.append(text_obj("%s_scenario_%d_impact" % (sid, i), "metric", sc.get("impact", ""), x + 12, 462, 146, 56, 90 + i, 15, color=system_pal(profile, "ink"), bold=True, priority=5))
            objects.append(text_obj("%s_scenario_%d_action" % (sid, i), "body", sc.get("action", ""), x + 12, 526, 146, 20, 96 + i, 9, color=system_pal(profile, "muted"), priority=5))
    elif slide.get("process"):
        route = [(92, 414), (294, 488), (496, 414), (698, 488)]
        for i in range(len(route) - 1):
            x1, y1 = route[i]
            x2, y2 = route[i + 1]
            objects.append(shape_obj("%s_process_route_%d" % (sid, i + 1), "route-line", min(x1, x2) + 74, min(y1, y2) + 36, abs(x2 - x1) + 54, 5, 76 + i, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.34, stroke_opacity=0.0))
        for i, step in enumerate(slide.get("process", [])[:4], start=1):
            x, y = route[i - 1]
            objects.append(shape_obj("%s_process_%d_tile" % (sid, i), "map-tile", x, y, 166, 116, 82 + i, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "rule"), shape="roundRect", priority=3, opacity=0.96, stroke_opacity=0.78))
            objects.append(shape_obj("%s_process_%d_node" % (sid, i), "route-line", x + 12, y + 12, 16, 16, 84 + i, fill=system_pal(profile, "accent"), stroke=system_pal(profile, "accent"), shape="ellipse", priority=2, opacity=0.95, stroke_opacity=0.0))
            objects.append(text_obj("%s_process_%d_num" % (sid, i), "process-step", step.get("step", ""), x + 36, y + 10, 34, 18, 86 + i, 10, color=system_pal(profile, "accent"), bold=True, priority=5))
            objects.append(text_obj("%s_process_%d_title" % (sid, i), "process-step", step.get("title", ""), x + 74, y + 10, 78, 18, 88 + i, 10, color=system_pal(profile, "ink"), bold=True, priority=5))
            objects.append(text_obj("%s_process_%d_text" % (sid, i), "process-step", step.get("text", ""), x + 12, y + 40, 140, 52, 92 + i, 8, color=system_pal(profile, "muted"), priority=5))
    if slide.get("risk_note"):
        objects.append(shape_obj(sid + "_source_band", "route-line", 76, 612, 1128, 6, 890, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.34, stroke_opacity=0.0))
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 84, 628, 1090, 26, 900, 9, color=system_pal(profile, "muted"), priority=5))
    apply_text_dna(objects, profile)
    return {"id": sid, "objects": normalize_z(objects)}


def compile_visual_system_contract(contract):
    style = contract.get("style_program")
    profile = VISUAL_SYSTEM_PROFILES[style]
    compiler = compile_paper_slide if style == "paper-analyst-report" else compile_atlas_slide
    return {
        "deck": {
            "id": contract.get("deck_id", style),
            "size": contract.get("size", DEFAULT_SIZE),
            "style_program": style,
            "visual_anchor": contract.get("visual_anchor", style),
            "visual_language": contract.get("visual_language", profile["visual_language"]),
            "narrative_intent": contract.get("narrative_intent"),
            "visual_coordinates": contract.get("visual_coordinates", {}),
            "visual_system_grammar": profile["visual_system_grammar"],
            "slides": [compiler(s, i) for i, s in enumerate(contract["slides"], start=1)],
        }
    }

def compile_glass_contract(contract):
    profile = variant_profile(contract)
    return {
        "deck": {
            "id": contract.get("deck_id", "glass-fintech-showcase"),
            "size": contract.get("size", DEFAULT_SIZE),
            "style_program": contract.get("style_program"),
            "visual_anchor": contract.get("visual_anchor", contract.get("style_program")),
            "visual_language": contract.get("visual_language", profile.get("name", "default")),
            "narrative_intent": contract.get("narrative_intent"),
            "visual_coordinates": contract.get("visual_coordinates", {}),
            "visual_grammar": profile.get("visual_grammar", {}),
            "visual_system_grammar": {
                "surface": "dark-glass-finance",
                "composition": "dashboard-cards",
                "material": "translucent-glass",
                "chromatic_mode": "dark-cyan-violet-gold",
                "container_grammar": "glass-panels-kpi-cards",
            },
            "slides": [compile_glass_slide(s, i, profile) for i, s in enumerate(contract["slides"], start=1)],
        }
    }


def compile_contract(contract):
    if "slides" not in contract or not contract["slides"]:
        raise ValueError("content contract requires at least one slide")
    if contract.get("style_program") == "glass-fintech-pptx":
        return compile_glass_contract(contract)
    if contract.get("style_program") in VISUAL_SYSTEM_PROFILES:
        return compile_visual_system_contract(contract)
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
