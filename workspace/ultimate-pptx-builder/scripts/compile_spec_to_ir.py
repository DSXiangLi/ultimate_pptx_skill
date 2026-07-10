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
        "orb_violet": {"x": -120, "y": 410, "w": 330, "h": 330, "opacity": 0.045, "role": "decorative-glow"},
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
        "orb_cyan": {"x": 1060, "y": 12, "w": 96, "h": 96, "opacity": 0.014, "role": "decorative-glow"},
        "orb_violet": {"x": -36, "y": 536, "w": 96, "h": 96, "opacity": 0.012, "role": "decorative-glow"},
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
        "orb_cyan": {"x": 1020, "y": -82, "w": 256, "h": 256, "opacity": 0.15, "role": "spotlight-orb"},
        "orb_violet": {"x": -138, "y": 350, "w": 360, "h": 360, "opacity": 0.070, "role": "spotlight-orb"},
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
        "chart": {"series_palette": ["67E8F9", "A78BFA", "FACC15"], "axis_style": "luminous-glass-axis", "legend_style": "spotlight-legend", "marker_style": "glow-node", "bar_shape": "roundRect", "panel_opacity": 0.50, "grid_opacity": 0.24, "label_color": "C9D6E2", "value_label_color": "F4FAFF"},
        "fonts": {"title": "Bahnschrift SemiBold", "body": "Microsoft YaHei", "metric": "Aptos Display", "caption": "Microsoft YaHei"},
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
    "muted": "C9D6E2",
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


def obj_box(obj):
    return obj.get("box", {}) or {}


def same_row(objs, tol=4):
    if len(objs) < 2:
        return False
    ys = [float(obj_box(o).get("y", 0) or 0) for o in objs]
    return max(ys) - min(ys) <= tol


def same_size(objs, dim, tol=4):
    if len(objs) < 2:
        return False
    key = "w" if dim == "width" else "h"
    vals = [float(obj_box(o).get(key, 0) or 0) for o in objs]
    return max(vals) - min(vals) <= tol


def infer_layout_relations(sid, objects):
    """Declare concrete alignment intent for downstream QA.

    These relations are intentionally conservative: they describe component rows,
    repeated body columns, and parent padding only when object IDs/roles make the
    intended relationship explicit. The alignment graph gate then validates these
    declarations instead of relying on vague visual inspection.
    """
    relations = []
    by_id = {o.get("id"): o for o in objects if o.get("id")}

    body_ids = [o.get("id") for o in objects if o.get("type") == "text" and o.get("role") == "body" and ("_body_" in o.get("id", "") or o.get("id", "").startswith("body_"))]
    body_objs = [by_id[i] for i in body_ids if i in by_id]
    if len(body_objs) >= 2:
        left = min(float(obj_box(o).get("x", 0) or 0) for o in body_objs)
        col = [o for o in body_objs if abs(float(obj_box(o).get("x", 0) or 0) - left) <= 8]
        if len(col) >= 2:
            relations.append({"id": sid + "_body_column_left", "type": "align-left", "objects": [o["id"] for o in col], "tolerance": 4})

    row_patterns = [
        ("metric-chip-row", "_metric_", ("_chip", "_card")),
        ("process-signal-row", "_process_signal_", ("",)),
        ("scenario-zone-row", "_scenario_zone_", ("",)),
        ("scenario-card-row", "_scenario_", ("_card",)),
        ("process-card-row", "_process_", ("_card",)),
    ]
    for rel_name, marker, suffixes in row_patterns:
        candidates = []
        for o in objects:
            oid = o.get("id", "")
            if o.get("type") == "shape" and marker in oid and any(oid.endswith(suf) for suf in suffixes):
                candidates.append(o)
        if len(candidates) >= 2:
            candidates = sorted(candidates, key=lambda o: (float(obj_box(o).get("y", 0) or 0), float(obj_box(o).get("x", 0) or 0)))
            rows = []
            for obj in candidates:
                y = float(obj_box(obj).get("y", 0) or 0)
                for row in rows:
                    if abs(float(obj_box(row[0]).get("y", 0) or 0) - y) <= 6:
                        row.append(obj)
                        break
                else:
                    rows.append([obj])
            for ri, row in enumerate(rows, start=1):
                if len(row) >= 2 and same_row(row, 6):
                    rel = {"id": "%s_%s_%d" % (sid, rel_name, ri), "type": "row", "objects": [o["id"] for o in row], "align": ["top"], "tolerance": 6}
                    equal = []
                    if same_size(row, "width", 6):
                        equal.append("width")
                    if same_size(row, "height", 6):
                        equal.append("height")
                    if equal:
                        rel["equal"] = equal
                    if len(row) >= 3:
                        rel["gutter"] = {"mode": "equal", "tolerance": 8}
                    relations.append(rel)

    container_roles = {"signal-chip", "scenario-zone", "process-node", "supporting-card", "glass-panel", "metric-card", "ledger-metric"}
    for prefix, cols in [
        ("scenario", ["name", "impact", "action"]),
        ("process", ["num", "title", "text"]),
    ]:
        for col in cols:
            ids = []
            for o in objects:
                oid = o.get("id", "")
                if o.get("type") == "text" and ("_%s_" % prefix) in oid and oid.endswith("_" + col):
                    ids.append(oid)
            if len(ids) >= 2:
                xs = [float(obj_box(by_id[i]).get("x", 0) or 0) for i in ids if i in by_id]
                if xs and max(xs) - min(xs) <= 3:
                    relations.append({"id": "%s_%s_%s_column" % (sid, prefix, col), "type": "align-left", "objects": ids, "tolerance": 3})
        # Row top alignment for each numbered table row; only declare it when
        # the row actually uses a tabular horizontal grammar.
        for n in range(1, 8):
            row_ids = []
            for o in objects:
                oid = o.get("id", "")
                if o.get("type") == "text" and ("_%s_%d_" % (prefix, n)) in oid:
                    row_ids.append(oid)
            row_objs = [by_id[i] for i in row_ids if i in by_id]
            if len(row_objs) >= 2 and same_row(row_objs, 4):
                relations.append({"id": "%s_%s_%d_row" % (sid, prefix, n), "type": "row", "objects": row_ids, "align": ["top"], "tolerance": 4})

    container_roles = {"signal-chip", "scenario-zone", "process-node", "supporting-card", "glass-panel", "metric-card", "ledger-metric"}
    for parent in objects:
        if parent.get("type") != "shape" or parent.get("role") not in container_roles:
            continue
        pid = parent.get("id", "")
        children = [o.get("id") for o in objects if o.get("type") == "text" and o.get("id", "").startswith(pid + "_") and (o.get("editability") or {}).get("priority", 0) >= 4]
        if children:
            relations.append({"id": pid + "_padding", "type": "parent-padding", "parent": pid, "children": children, "padding": {"x": 2, "y": 2}, "tolerance": 8})

    return relations


def slide_ir(sid, objects, layout_graph=None):
    normalized = normalize_z(objects)
    out = {"id": sid, "objects": normalized, "layout_relations": infer_layout_relations(sid, normalized)}
    if layout_graph:
        out["layout_graph"] = layout_graph
    return out


def atlas_authored_layout_graph(sid, objects):
    """Declare authored component-layout evidence for Atlas components.

    This is not a solver yet. It records the component contract and semantic slots
    that the compiler intentionally authored so downstream gates can distinguish
    authored layout intent from geometry inferred after the fact.
    """
    ids = {o.get("id") for o in objects if o.get("id")}
    panel_id = sid + "_budget_map_panel"
    if panel_id not in ids:
        return None

    def keep(pattern):
        return sorted([oid for oid in ids if pattern in oid])

    is_allocation_bridge = any((sid + "_bridge_node_") in oid for oid in ids)
    if is_allocation_bridge:
        slots = {
            "header": [sid + "_budget_map_title", sid + "_budget_source"],
            "bridge_nodes": keep("_bridge_node_"),
            "bridge_routes": keep("_bridge_route_"),
            "asset_lanes": keep("_bridge_asset_"),
            "limit_rule": [sid + "_bridge_limit_rule"],
            "guardrail": [sid + "_bridge_guardrail", sid + "_bridge_guardrail_label", sid + "_bridge_dd_rule"],
            "footer": [sid + "_footer_mask", sid + "_risk_note", sid + "_source_band"],
        }
        component_type = "allocation-bridge-route-map"
        authored_relations = [
            {"id": sid + "_bridge_nodes_row", "type": "row", "objects": keep("_bridge_node_"), "source": "authored"},
            {"id": sid + "_bridge_asset_lanes", "type": "slot-stack", "objects": keep("_bridge_asset_"), "source": "authored"},
            {"id": sid + "_guardrail_footer_gap", "type": "separate-band", "from_slot": "guardrail", "to_slot": "footer", "min_gap": 16, "source": "authored"},
        ]
    else:
        slots = {
            "header": [sid + "_budget_map_title", sid + "_budget_source"],
            "card_lane": keep("_macro_zone_"),
            "station_lane": keep("_macro_station_"),
            "route_lines": keep("_macro_route_") + [sid + "_macro_rollback_route"],
            "status_badge": [sid + "_macro_now_card", sid + "_macro_now_text"],
            "bottom_matrix": keep("_macro_matrix_") + [sid + "_macro_rule_matrix"],
            "footer": [sid + "_footer_mask", sid + "_risk_note", sid + "_source_band"],
        }
        component_type = "macro-budget-route-map"
        authored_relations = [
            {"id": sid + "_macro_cards_row", "type": "row", "objects": [sid + "_macro_zone_1", sid + "_macro_zone_2", sid + "_macro_zone_3"], "source": "authored"},
            {"id": sid + "_status_badge_to_confirm_card", "type": "semantic-child", "parent": sid + "_macro_zone_2", "child": sid + "_macro_now_card", "allowed_overlap": "corner-badge", "source": "authored"},
            {"id": sid + "_bottom_matrix_separate_band", "type": "separate-band", "from_slot": "card_lane", "to_slot": "bottom_matrix", "min_gap": 8, "source": "authored"},
        ]

    # Drop absent IDs so the graph is evidence, not wishful declaration.
    clean_slots = {k: [oid for oid in v if oid in ids] for k, v in slots.items()}
    clean_relations = []
    for rel in authored_relations:
        rel = dict(rel)
        if "objects" in rel:
            rel["objects"] = [oid for oid in rel.get("objects", []) if oid in ids]
            if not rel["objects"]:
                continue
        if "parent" in rel and rel["parent"] not in ids:
            continue
        if "child" in rel and rel["child"] not in ids:
            continue
        clean_relations.append(rel)

    return {
        "source": "authored",
        "components": [
            {
                "id": panel_id,
                "type": component_type,
                "contract_ref": "atlas-route-map",
                "root": panel_id,
                "slots": clean_slots,
                "relations": clean_relations,
            }
        ],
    }


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
    return slide_ir(slide["id"], objects)


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
        objects.append(shape_obj(slide_id + "_orb_gold", "spotlight-orb", 1000, 392, 260, 260, 3, fill=pal(profile, "warning"), stroke=pal(profile, "warning"), shape="ellipse", priority=1, opacity=0.055, stroke_opacity=0.0))
    if name == "luminous-glass":
        objects.append(shape_obj(slide_id + "_luminous_ribbon", "luminous-ribbon", 64, 50, 520, 8, 5, fill=pal(profile, "warning"), stroke=pal(profile, "warning"), shape="rect", priority=1, opacity=0.72, stroke_opacity=0.0))
        objects.append(shape_obj(slide_id + "_luminous_sweep", "luminous-ribbon", 820, 104, 310, 14, 6, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="roundRect", priority=1, opacity=0.34, stroke_opacity=0.0))
    if name == "matte-institutional":
        for gi, gx in enumerate([224, 384, 544, 704, 864, 1024], start=1):
            objects.append(shape_obj("%s_grid_v_%d" % (slide_id, gi), "institutional-gridline", gx, 64, 1, 520, 4 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.055, stroke_opacity=0.0))
        for gi, gy in enumerate([188, 332, 476], start=1):
            objects.append(shape_obj("%s_grid_h_%d" % (slide_id, gi), "institutional-ruler", 64, gy, 1152, 1, 12 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.060, stroke_opacity=0.0))
    elif name == "terminal-cockpit":
        objects.append(shape_obj(slide_id + "_terminal_top_status", "terminal-status-bar", 64, 48, 1152, 26, 72, fill="04100C", stroke=pal(profile, "stroke_soft"), shape="rect", priority=2, opacity=0.92, stroke_opacity=0.75))
        objects.append(text_obj(slide_id + "_terminal_path", "terminal-status-bar", "SYS / ALLOCATION / LIVE SIGNAL", 82, 53, 420, 18, 73, 10, color=pal(profile, "stroke"), bold=True, priority=2, opacity=0.9))
        objects.append(shape_obj(slide_id + "_terminal_left_rail", "terminal-status-bar", 48, 88, 6, 500, 74, fill=pal(profile, "stroke"), stroke=pal(profile, "stroke"), shape="rect", priority=1, opacity=0.42, stroke_opacity=0.0))
        for gi, gx in enumerate(range(88, 1216, 64), start=1):
            objects.append(shape_obj("%s_terminal_v_%d" % (slide_id, gi), "terminal-gridline", gx, 80, 1, 506, 4 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.26, stroke_opacity=0.0))
        for gi, gy in enumerate(range(104, 600, 48), start=1):
            objects.append(shape_obj("%s_terminal_h_%d" % (slide_id, gi), "terminal-gridline", 64, gy, 1152, 1, 30 + gi, fill=pal(profile, "stroke_soft"), stroke=pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.10, stroke_opacity=0.0))
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
    title_w = 720 if topology in {"glass-cover", "glass-hero"} else (900 if name == "luminous-glass" else 960)
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
            objects.append(chart_obj(sid + "_chart", slide["chart"], 88, 390, 520, 188, 39, profile))
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
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 520, 320, 74, 80 + i * 10, profile)
    elif topology == "glass-process":
        add_body_paragraphs(objects, sid, body, 88, 238, 1040, 36, 30, 15, 1, profile=profile)
        add_process(objects, sid, slide.get("process", []), 84, 306, 1112, 174, 44, profile=profile)
        for i, metric in enumerate(metrics[:3], start=1):
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 520, 320, 74, 90 + i * 10, profile)
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
            add_metric(objects, "%s_metric_%d" % (sid, i), metric, 88 + (i - 1) * 370, 520, 320, 74, 80 + i * 10, profile)
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
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 88, 600, 1090, 24, 900, 10, color=pal(profile, "muted"), priority=5))
    apply_text_dna(objects, profile)
    return slide_ir(sid, objects)



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
            "chromatic_mode": "institutional-cartographic-navy-sage",
            "container_grammar": "map-tiles-route-lines",
        },
        "palette": {"background": "EEF2EA", "paper": "FBFCF7", "ink": "0E2723", "muted": "334E48", "rule": "6F8278", "accent": "173B67", "positive": "23624D", "warning": "8C5A2B", "panel": "E1E8DC", "panel_alt": "D3DED4", "stroke_soft": "72857B", "text": "0E2723", "white": "FFFFFF"},
        "fonts": {"title": "Aptos Display", "body": "Aptos", "metric": "Arial Narrow", "caption": "Aptos"},
        "chart": {"series_palette": ["1457A8", "187956", "B86414"], "axis_style": "coordinate-grid-axis", "legend_style": "map-legend", "marker_style": "route-node", "bar_shape": "roundRect", "panel_opacity": 0.72, "grid_opacity": 0.10, "label_color": "2C5148", "value_label_color": "0B2B24"},
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
        objects.append(shape_obj(prefix + "_node", "map-node", x + 12, y + 14, 9, 9, z + 1, fill=tone, stroke=tone, shape="ellipse", priority=2, opacity=0.62, stroke_opacity=0.0))
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
    # Atlas grammar constants. The style must read as a controlled investment map:
    # light header, left analysis field, right decision rail, weak compliance footer.
    left_x, left_w = 80, 624
    right_x, right_w = 724, 480
    main_y = 222
    footer_y = 616
    has_chart = bool(slide.get("chart"))
    has_scenarios = bool(slide.get("scenarios"))
    has_process = bool(slide.get("process"))
    if not has_process:
        objects.append(shape_obj(sid + "_zone_left", "background", left_x, main_y, left_w, 150, 6, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "panel"), shape="rect", priority=1, opacity=0.76, stroke_opacity=0.0))
    if has_chart:
        objects.append(shape_obj(sid + "_zone_bottom", "background", 88, 394, 610, 194, 6, fill=system_pal(profile, "panel_alt"), stroke=system_pal(profile, "panel_alt"), shape="rect", priority=1, opacity=0.86, stroke_opacity=0.0))
        objects.append(shape_obj(sid + "_zone_right", "background", right_x, 222, right_w, 336, 7, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.96, stroke_opacity=0.28))
    elif has_scenarios:
        objects.append(shape_obj(sid + "_zone_right", "background", right_x, 222, right_w, 364, 7, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.96, stroke_opacity=0.28))
    elif has_process:
        pass
    else:
        objects.append(shape_obj(sid + "_zone_bottom", "background", 88, 410, 610, 154, 6, fill=system_pal(profile, "panel_alt"), stroke=system_pal(profile, "panel_alt"), shape="rect", priority=1, opacity=0.84, stroke_opacity=0.0))
        objects.append(shape_obj(sid + "_zone_right", "background", right_x, 222, right_w, 336, 7, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=1, opacity=0.96, stroke_opacity=0.28))
    for gx in [80, 240, 400, 560, 720, 880, 1040, 1200]:
        objects.append(shape_obj("%s_grid_v_%d" % (sid, gx), "atlas-gridline", gx, 62, 1, 552, 2, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=1, opacity=(0.016 if has_process else 0.020), stroke_opacity=0.0))
    for gy in [118, 222, 326, 430, 534, 638]:
        objects.append(shape_obj("%s_grid_h_%d" % (sid, gy), "atlas-gridline", 80, gy, 1120, 1, 2, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=1, opacity=(0.014 if has_process else 0.018), stroke_opacity=0.0))
    if not (has_chart or has_process):
        objects.append(shape_obj(sid + "_route_primary", "route-line", 96, 250, 584, 6, 4, fill=system_pal(profile, "accent"), stroke=system_pal(profile, "accent"), shape="rect", priority=2, opacity=0.052, stroke_opacity=0.0))
        objects.append(shape_obj(sid + "_route_secondary", "route-line", 178, 532, 470, 5, 4, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.040, stroke_opacity=0.0))
        for n, (nx, ny, tone) in enumerate([(708, 250, "accent"), (704, 532, "positive"), (1160, 250, "warning")], start=1):
            objects.append(shape_obj("%s_node_%d" % (sid, n), "map-node", nx, ny, 10, 10, 5, fill=system_tone_color(profile, tone), stroke=system_tone_color(profile, tone), shape="rect", priority=2, opacity=0.20, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_folio", "research-folio", "MARKET ATLAS / ZONE-%02d" % index, 80, 54, 300, 22, 10, 10, color=system_pal(profile, "muted"), bold=True, priority=2))
    if not has_process:
        objects.append(text_obj(sid + "_legend_1", "research-folio", "SIGNAL FIELD", right_x + 18, 206, 160, 18, 11, 9, color=system_pal(profile, "muted"), bold=True, priority=2))
    if not (has_chart or has_scenarios or has_process):
        objects.append(text_obj(sid + "_legend_2", "research-folio", "ALLOCATION ROUTE", 96, 402, 220, 18, 11, 9, color=system_pal(profile, "positive"), bold=True, priority=2))
    if not has_process and not has_chart:
        route_y = 454
        route_nodes = [(142, "DEF"), (332, "RISK"), (522, "HEDGE")]
        objects.append(shape_obj(sid + "_allocation_route_spine", "route-line", 148, route_y + 8, 392, 3, 74, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.22, stroke_opacity=0.0))
        for ni, (nx, label) in enumerate(route_nodes, start=1):
            objects.append(shape_obj("%s_allocation_stop_%d" % (sid, ni), "map-node", nx, route_y, 18, 18, 76 + ni, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "positive" if ni != 2 else "accent"), shape="ellipse", priority=2, opacity=0.94, stroke_opacity=0.80))
            objects.append(text_obj("%s_allocation_stop_%d_label" % (sid, ni), "research-folio", label, nx - 22, route_y + 26, 70, 16, 80 + ni, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(text_obj(sid + "_kicker", "kicker", slide.get("kicker", ""), 82, 78, 520, 18, 12, 10, color=system_pal(profile, "accent"), bold=True, priority=4))


def add_atlas_legend(objects, sid, x, y, z, profile, items):
    objects.append(text_obj(sid + "_atlas_legend_label", "research-folio", "LEGEND", x, y, 82, 14, z, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    cx = x + 62
    for i, (label, tone) in enumerate(items, start=1):
        px = cx + (i - 1) * 120
        color = system_tone_color(profile, tone)
        objects.append(shape_obj("%s_atlas_legend_%d_dot" % (sid, i), "legend-marker", px, y + 3, 8, 8, z + i, fill=color, stroke=color, shape="ellipse", priority=2, opacity=0.86, stroke_opacity=0.0))
        objects.append(text_obj("%s_atlas_legend_%d_text" % (sid, i), "research-folio", label, px + 12, y - 1, 100, 16, z + i, 8, color=system_pal(profile, "muted"), bold=True, priority=2))


def add_atlas_signal_field_map(objects, sid, metrics, x, y, w, h, z, profile):
    """Render metrics as a field/compass, not independent dashboard cards."""
    cx = x + w / 2
    cy = y + h / 2 + 6
    objects.append(shape_obj(sid + "_signal_field_axis_h", "atlas-axis", x + 44, cy, w - 88, 2, z, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.20, stroke_opacity=0.0))
    objects.append(shape_obj(sid + "_signal_field_axis_v", "atlas-axis", cx, y + 44, 2, h - 88, z, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.20, stroke_opacity=0.0))
    objects.append(shape_obj(sid + "_signal_field_core", "map-node", cx - 54, cy - 32, 108, 64, z + 5, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "accent"), shape="roundRect", priority=3, opacity=0.92, stroke_opacity=0.72))
    objects.append(text_obj(sid + "_signal_field_core_k", "research-folio", "REGIME", cx - 42, cy - 24, 84, 14, z + 6, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    objects.append(text_obj(sid + "_signal_field_core_v", "metric", "中性偏积极", cx - 44, cy - 8, 88, 40, z + 7, 11, color=system_pal(profile, "ink"), bold=True, priority=5))
    positions = [(x + 22, y + 20), (x + w - 152, y + 20), (x + 22, y + h - 76), (x + w - 152, y + h - 76)]
    for i, metric in enumerate(metrics[:4], start=1):
        px, py = positions[i - 1]
        tone = system_tone_color(profile, metric.get("tone"))
        objects.append(shape_obj("%s_signal_point_%d" % (sid, i), "signal-node", px, py, 130, 58, z + 10 + i, fill=system_pal(profile, "paper"), stroke=tone, shape="roundRect", priority=3, opacity=0.90, stroke_opacity=0.62))
        objects.append(text_obj("%s_signal_point_%d_label" % (sid, i), "metric-label", metric.get("label", ""), px + 12, py + 7, 102, 14, z + 20 + i, 8, color=system_pal(profile, "muted"), bold=True, priority=4))
        objects.append(text_obj("%s_signal_point_%d_value" % (sid, i), "metric", metric.get("value", ""), px + 12, py + 23, 102, 20, z + 30 + i, 13, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(text_obj("%s_signal_point_%d_delta" % (sid, i), "metric-note", metric.get("delta", ""), px + 12, py + 42, 110, 12, z + 40 + i, 8, color=tone, priority=4))
        # Connector from field point to regime core. Thin rectangles keep PPTX editable.
        mx = px + 65
        my = py + 29
        objects.append(shape_obj("%s_signal_vector_%d" % (sid, i), "signal-vector", min(mx, cx), min(my, cy), max(abs(cx - mx), 2), 2, z + 2 + i, fill=tone, stroke=tone, shape="rect", priority=2, opacity=0.16, stroke_opacity=0.0))


def add_atlas_budget_route_map(objects, sid, chart, x, y, w, h, z, profile):
    """Atlas-native budget route.

    Two grammars are used:
    - Macro route pages (months): signal score -> staged risk-budget checkpoints.
    - Allocation pages (current/proposed/limit): current -> action -> target bridge.

    Both avoid chart axes and generic stacked bars; values stay native/editable.
    """
    cats = chart.get("categories", [])
    series = chart.get("series", [])
    objects.append(shape_obj(sid + "_budget_map_panel", "route-map", x, y, w, h, z, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=3, opacity=0.98, stroke_opacity=0.48))
    objects.append(text_obj(sid + "_budget_map_title", "research-folio", "ALLOCATION ROUTE MAP / " + chart.get("title", "配置路径"), x + 18, y + 12, w - 36, 16, z + 2, 8, color=system_pal(profile, "muted"), bold=True, priority=4))
    if not cats or not series:
        return

    is_allocation_bridge = set(cats[:3]) == {"当前", "建议", "上限"} or cats[:3] == ["当前", "建议", "上限"]

    if is_allocation_bridge:
        # Slide03: make the core read as a decision bridge, not a chart.
        col_x = [x + 126, x + 316, x + 506]
        heads = [("CURRENT", "当前配置"), ("PROPOSED", "建议动作"), ("LIMIT", "风险上限")]
        for i, (eng, zh) in enumerate(heads):
            objects.append(text_obj("%s_bridge_head_%d" % (sid, i + 1), "research-folio", eng, col_x[i] - 46, y + 48, 96, 12, z + 5 + i, 8, color=system_pal(profile, "muted"), bold=True, priority=3))
            objects.append(shape_obj("%s_bridge_node_%d" % (sid, i + 1), "map-node", col_x[i] - 18, y + 70, 36, 36, z + 10 + i, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "positive" if i < 2 else "warning"), shape="ellipse", priority=3, opacity=0.96, stroke_opacity=0.76))
            objects.append(text_obj("%s_bridge_node_label_%d" % (sid, i + 1), "research-folio", zh, col_x[i] - 44, y + 110, 90, 12, z + 12 + i, 8, color=system_pal(profile, "ink"), bold=True, priority=3))
        for i in [0, 1]:
            objects.append(shape_obj("%s_bridge_route_%d" % (sid, i + 1), "route-line", col_x[i] + 24, y + 86, col_x[i + 1] - col_x[i] - 48, 4, z + 14 + i, fill=system_pal(profile, "positive" if i == 0 else "warning"), stroke=system_pal(profile, "positive" if i == 0 else "warning"), shape="rect", priority=2, opacity=0.34, stroke_opacity=0.0))
            objects.append(text_obj("%s_bridge_route_label_%d" % (sid, i + 1), "metric-note", "加权益 / 控久期" if i == 0 else "护栏 / 不突破", col_x[i] + 54, y + 64, 118, 14, z + 18 + i, 8, color=system_pal(profile, "muted"), bold=True, priority=3))

        lane_y = [y + 120, y + 142, y + 164]
        for j, ser in enumerate(series[:3]):
            tone = system_tone_color(profile, ser.get("tone"))
            vals = [float(v) for v in ser.get("values", [0, 0, 0])[:3]]
            yy = lane_y[j]
            objects.append(text_obj("%s_bridge_asset_%d" % (sid, j + 1), "metric-label", ser.get("name", ""), x + 20, yy - 5, 72, 14, z + 34 + j, 8, color=tone, bold=True, priority=4))
            for i, v in enumerate(vals):
                objects.append(shape_obj("%s_bridge_asset_%d_stop_%d" % (sid, j + 1, i + 1), "signal-chip", col_x[i] - 34, yy - 8, 68, 18, z + 38 + j * 3 + i, fill=system_pal(profile, "panel"), stroke=tone, shape="roundRect", priority=3, opacity=0.82, stroke_opacity=0.46))
                objects.append(text_obj("%s_bridge_asset_%d_val_%d" % (sid, j + 1, i + 1), "metric-note", "%d%%" % int(v), col_x[i] - 18, yy - 5, 38, 12, z + 42 + j * 3 + i, 8, color=system_pal(profile, "ink"), bold=True, priority=4))
            delta = int(vals[1] - vals[0])
            objects.append(text_obj("%s_bridge_asset_%d_delta" % (sid, j + 1), "metric-note", "%+dpct" % delta, col_x[0] + 86, yy - 5, 58, 12, z + 52 + j, 8, color=tone, bold=True, priority=4))

        objects.append(shape_obj(sid + "_bridge_guardrail", "guardrail", x + w - 102, y + 52, 2, h - 86, z + 64, fill=system_pal(profile, "warning"), stroke=system_pal(profile, "warning"), shape="rect", priority=3, opacity=0.46, stroke_opacity=0.0))
        objects.append(text_obj(sid + "_bridge_guardrail_label", "research-folio", "DD GUARDRAIL", x + w - 140, y + 42, 108, 12, z + 65, 8, color=system_pal(profile, "warning"), bold=True, priority=3))
        objects.append(text_obj(sid + "_bridge_limit_rule", "metric-note", "上限：权益≤62；固收≥30；另类现金≥8（尾部对冲底仓）", x + 20, y + 28, w - 60, 16, z + 70, 8, color=system_pal(profile, "ink"), bold=True, priority=4))
        objects.append(text_obj(sid + "_bridge_dd_rule", "metric-note", "回撤>5%或周撤>3%：停加权益，回建议仓位", x + 20, y + h - 24, w - 60, 16, z + 71, 8, color=system_pal(profile, "warning"), bold=True, priority=4))
        if chart.get("source"):
            objects.append(text_obj(sid + "_budget_source", "research-folio", "Source: 投研/Wind/Bloomberg", x + w - 244, y + 14, 218, 12, z + 72, 8, color=system_pal(profile, "muted"), priority=2))
        return

    # Slide02: macro decision route. The route is signal-gated, not month-driven.
    route_x = x + 38
    route_y = y + 34
    route_w = w - 76
    route_h = h - 96
    n = max(1, len(cats))
    first_vals = [float(ser.get("values", [0] * n)[0]) for ser in series[:3]]
    last_vals = [float(ser.get("values", [0] * n)[n - 1]) for ser in series[:3]]
    asset_names = [ser.get("name", "") for ser in series[:3]]

    zone_defs = [
        {
            "eng": "WATCH", "zh": "观察", "tone": "warning",
            "if": "IF 增长弱修复 / 估值拥挤",
            "then": "THEN 维持中性预算",
            "window": "6-7月观察窗口",
        },
        {
            "eng": "CONFIRM", "zh": "确认", "tone": "positive",
            "if": "IF 流动性宽松延续",
            "then": "THEN 小幅加风险",
            "window": "8-9月确认窗口",
        },
        {
            "eng": "DEPLOY", "zh": "部署", "tone": "accent",
            "if": "IF 增长/盈利确认",
            "then": "THEN 执行目标预算",
            "window": "10月后分段执行",
        },
    ]
    zone_w = (route_w - 24) / 3
    node_centers = []
    for i, zd in enumerate(zone_defs, start=1):
        zx = route_x + (i - 1) * (zone_w + 12)
        zy = route_y + 10
        tone = system_tone_color(profile, zd["tone"])
        objects.append(shape_obj("%s_macro_zone_%d" % (sid, i), "route-map", zx, zy, zone_w, 64, z + 3 + i, fill=tone, stroke=tone, shape="roundRect", priority=3, opacity=0.13 + i * 0.018, stroke_opacity=0.0))
        objects.append(text_obj("%s_macro_zone_%d_label" % (sid, i), "research-folio", "%s / %s" % (zd["eng"], zd["zh"]), zx + 12, zy + 7, zone_w - 24, 14, z + 8 + i, 8, color=system_pal(profile, "ink"), bold=True, priority=4))
        objects.append(text_obj("%s_macro_zone_%d_if" % (sid, i), "metric-note", zd["if"], zx + 12, zy + 27, zone_w - 24, 14, z + 12 + i, 8, color=system_pal(profile, "ink"), bold=True, priority=4))
        objects.append(text_obj("%s_macro_zone_%d_then" % (sid, i), "metric-note", zd["then"], zx + 12, zy + 45, zone_w - 24, 14, z + 16 + i, 8, color=tone, bold=True, priority=4))
        cx = zx + zone_w / 2
        cy = zy + 68
        node_centers.append((cx, cy, tone))
        objects.append(shape_obj("%s_macro_station_%d" % (sid, i), "map-node", cx - 12, cy - 12, 24, 24, z + 30 + i, fill=system_pal(profile, "paper"), stroke=tone, shape="ellipse", priority=3, opacity=0.98, stroke_opacity=0.92))
        objects.append(text_obj("%s_macro_station_%d_name" % (sid, i), "research-folio", zd["eng"], cx - 30, cy + 13, 64, 9, z + 34 + i, 7, color=system_pal(profile, "muted"), bold=True, priority=2))

    # Forward business route: signal-confirmed stages.
    for i in range(2):
        x1, y1, tone1 = node_centers[i]
        x2, y2, tone2 = node_centers[i + 1]
        objects.append(shape_obj("%s_macro_route_%d" % (sid, i + 1), "route-line", x1 + 16, y1 - 2, x2 - x1 - 32, 4, z + 44 + i, fill=tone2, stroke=tone2, shape="rect", priority=3, opacity=0.36, stroke_opacity=0.0))
        objects.append(text_obj("%s_macro_route_%d_rule" % (sid, i + 1), "research-folio", "触发确认" if i == 0 else "条件满足", x1 + 56, y1 - 20, 74, 12, z + 46 + i, 8, color=tone2, bold=True, priority=2))

    # Rollback / fail path makes this a risk route, not a one-way timeline.
    rb_y = y + h - 82
    objects.append(shape_obj(sid + "_macro_rollback_route", "route-line", node_centers[2][0] - 18, rb_y, node_centers[0][0] - node_centers[2][0] + 36, 3, z + 46, fill=system_pal(profile, "warning"), stroke=system_pal(profile, "warning"), shape="rect", priority=3, opacity=0.24, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_macro_rollback_label", "research-folio", "ROLLBACK PATH", route_x + route_w - 112, rb_y + 4, 106, 12, z + 48, 8, color=system_pal(profile, "warning"), bold=True, priority=2))

    # Current state marker stays in the chrome above the active card; it must not cover card body.
    now_x = node_centers[1][0] - 46
    now_y = route_y - 6
    objects.append(shape_obj(sid + "_macro_now_card", "trigger-row", now_x, now_y, 124, 22, z + 56, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "positive"), shape="roundRect", priority=3, opacity=0.84, stroke_opacity=0.54))
    objects.append(text_obj(sid + "_macro_now_text", "metric-note", "NOW CONFIRM", now_x + 8, now_y + 5, 108, 12, z + 58, 8, color=system_pal(profile, "ink"), bold=True, priority=4))

    target = "/".join(str(int(v)) for v in last_vals)
    target_label = "%s 权/固/另类" % target if len(asset_names) >= 3 else "Target " + target
    matrix_y = y + h - 62
    objects.append(shape_obj(sid + "_macro_rule_matrix", "trigger-row", x + 18, matrix_y, w - 36, 62, z + 60, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "positive"), shape="roundRect", priority=3, opacity=0.78, stroke_opacity=0.30))
    cols = [x + 30, x + 170, x + 306, x + 462]
    matrix = [
        ("SCORE", "增长+1 流动性+2\n估值-1\n政策VETO=0"),
        ("STAGE", "+2 CONFIRM EARLY\n≥3 DEPLOY"),
        ("ACTION", target_label + "\n分段执行"),
        ("ROLLBACK", "政策收紧→WATCH\n盈利失败→CONFIRM"),
    ]
    for mi, (head, body) in enumerate(matrix):
        mw = [126, 126, 146, 154][mi]
        tone = ["muted", "positive", "accent", "warning"][mi]
        objects.append(text_obj("%s_macro_matrix_%d_head" % (sid, mi + 1), "research-folio", head, cols[mi], matrix_y + 5, mw, 10, z + 62 + mi, 8, color=system_tone_color(profile, tone) if tone != "muted" else system_pal(profile, "muted"), bold=True, priority=3))
        objects.append(text_obj("%s_macro_matrix_%d_body" % (sid, mi + 1), "metric-note", body, cols[mi], matrix_y + 17, mw, 42, z + 66 + mi, 8, color=system_pal(profile, "ink"), bold=True, priority=4))
    if chart.get("source"):
        objects.append(text_obj(sid + "_budget_source", "research-folio", "Source: 投研/Wind/Bloomberg", x + w - 244, y + 14, 218, 12, z + 66, 8, color=system_pal(profile, "muted"), priority=2))


def add_atlas_scenario_map(objects, sid, metrics, scenarios, x, y, w, h, z, profile):
    objects.append(shape_obj(sid + "_scenario_map_panel", "scenario-map", x, y, w, h, z, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=3, opacity=0.98, stroke_opacity=0.54))
    objects.append(text_obj(sid + "_scenario_map_title", "research-folio", "SCENARIO PRESSURE MAP", x + 18, y + 14, 220, 16, z + 1, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    start_x = x + 52
    start_y = y + h / 2
    objects.append(shape_obj(sid + "_scenario_origin", "map-node", start_x - 16, start_y - 16, 32, 32, z + 8, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "positive"), shape="ellipse", priority=3, opacity=0.96, stroke_opacity=0.78))
    objects.append(text_obj(sid + "_scenario_origin_label", "research-folio", "CURRENT\nBOOK", start_x - 28, start_y + 22, 70, 28, z + 9, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    row_y = [y + 52, y + 138, y + 224]
    tones = ["positive", "warning", "accent"]
    for i, sc in enumerate(scenarios[:3], start=1):
        metric = metrics[i - 1] if i - 1 < len(metrics) else {}
        ry = row_y[i - 1]
        tone_name = tones[i - 1]
        tone = system_tone_color(profile, tone_name)
        # Branch connector from origin to scenario zone.
        objects.append(shape_obj("%s_scenario_branch_%d" % (sid, i), "scenario-branch", start_x + 14, start_y - 1 if ry >= start_y else ry + 44, 116, 3, z + 4 + i, fill=tone, stroke=tone, shape="rect", priority=2, opacity=0.28, stroke_opacity=0.0))
        objects.append(shape_obj("%s_scenario_zone_%d" % (sid, i), "scenario-zone", x + 184, ry, w - 178, 78, z + 20 + i, fill=system_pal(profile, "panel"), stroke=tone, shape="roundRect", priority=3, opacity=0.96, stroke_opacity=0.76))
        objects.append(shape_obj("%s_scenario_zone_%d_pin" % (sid, i), "map-node", x + 198, ry + 14, 12, 12, z + 30 + i, fill=tone, stroke=tone, shape="ellipse", priority=2, opacity=0.88, stroke_opacity=0.0))
        objects.append(text_obj("%s_scenario_zone_%d_name" % (sid, i), "body", sc.get("name", ""), x + 218, ry + 8, 54, 18, z + 31 + i, 11, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(text_obj("%s_scenario_zone_%d_prob_label" % (sid, i), "metric-label", metric.get("label", ""), x + 286, ry + 6, 68, 14, z + 32 + i, 8, color=system_pal(profile, "muted"), bold=True, priority=4))
        objects.append(text_obj("%s_scenario_zone_%d_prob" % (sid, i), "metric", metric.get("value", ""), x + 286, ry + 24, 58, 22, z + 33 + i, 13, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_scenario_zone_%d_impact" % (sid, i), "metric", sc.get("impact", ""), x + 356, ry + 8, 112, 30, z + 34 + i, 10, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(text_obj("%s_scenario_zone_%d_trigger" % (sid, i), "metric-note", metric.get("delta", ""), x + 218, ry + 52, 138, 18, z + 35 + i, 8, color=system_pal(profile, "muted"), priority=4))
        objects.append(text_obj("%s_scenario_zone_%d_action" % (sid, i), "body", sc.get("action", ""), x + 366, ry + 52, 96, 18, z + 36 + i, 9, color=tone, bold=True, priority=5))
    add_atlas_legend(objects, sid + "_scenario", x + 18, y + h - 24, z + 80, profile, [("基准", "positive"), ("紧缩", "warning"), ("衰退", "accent")])


def add_atlas_process_state_machine(objects, sid, process, metrics, x, y, w, h, z, profile):
    """Execution page: state machine with step-mapped signal windows.

    The signal field is intentionally embedded into the process panel and mapped
    1:1 to the four state-machine nodes. This prevents a floating right-rail
    reading and makes the visual grammar auditable: signal window -> step node.
    """
    objects.append(shape_obj(sid + "_process_map_panel", "process-state-map", x, y, w, h, z + 30, fill=system_pal(profile, "paper"), stroke=system_pal(profile, "stroke_soft"), shape="rect", priority=3, opacity=0.98, stroke_opacity=0.54))
    objects.append(text_obj(sid + "_process_map_title", "research-folio", "EXECUTION STATE MACHINE / TRIGGER-GATED LOOP", x + 18, y + 14, 330, 16, z + 31, 8, color=system_pal(profile, "muted"), bold=True, priority=2))

    signal_x = x + 18
    signal_y = y + 42
    signal_w = 758
    signal_h = 82
    objects.append(shape_obj(sid + "_process_signal_field_panel", "signal-field", signal_x, signal_y, signal_w, signal_h, z + 32, fill=system_pal(profile, "background"), stroke=system_pal(profile, "rule"), shape="roundRect", priority=3, opacity=0.62, stroke_opacity=0.24))
    objects.append(text_obj(sid + "_process_signal_field_title", "research-folio", "STEP SIGNAL WINDOWS / 与四步执行节点一一对应", signal_x + 12, signal_y + 8, 330, 14, z + 34, 8, color=system_pal(profile, "muted"), bold=True, priority=2))

    nodes = [(x + 92, y + 158), (x + 286, y + 158), (x + 480, y + 158), (x + 674, y + 158)]
    window_specs = []
    tones = ["positive", "accent", "warning", "positive"]
    for i in range(4):
        metric = metrics[i] if i < len(metrics) else {}
        step = process[i] if i < len(process) else {}
        if i < len(metrics):
            label = metric.get("label", step.get("title", ""))
            value = metric.get("value", step.get("title", ""))
            delta = metric.get("delta", step.get("text", ""))
        else:
            label = step.get("title", "")
            value = "月度"
            delta = "偏离阈值即复盘"
        window_specs.append(("%02d" % (i + 1), label, value, delta, tones[i]))

    chip_w = 170
    chip_gap = 14
    chip_y = signal_y + 28
    for i, (step_no, label, value, delta, tone_name) in enumerate(window_specs, start=1):
        chip_x = signal_x + 12 + (i - 1) * (chip_w + chip_gap)
        tone = system_tone_color(profile, tone_name)
        objects.append(shape_obj("%s_process_signal_%d" % (sid, i), "signal-chip", chip_x, chip_y, chip_w, 42, z + 38 + i, fill=system_pal(profile, "panel"), stroke=tone, shape="roundRect", priority=3, opacity=0.84, stroke_opacity=0.50))
        objects.append(text_obj("%s_process_signal_%d_step" % (sid, i), "process-step", step_no, chip_x + 8, chip_y + 5, 18, 14, z + 40 + i, 8, color=tone, bold=True, priority=4))
        objects.append(text_obj("%s_process_signal_%d_label" % (sid, i), "metric-label", label, chip_x + 34, chip_y + 5, 80, 14, z + 42 + i, 8, color=system_pal(profile, "muted"), bold=True, priority=4))
        objects.append(text_obj("%s_process_signal_%d_value" % (sid, i), "metric", value, chip_x + 118, chip_y + 4, 42, 16, z + 46 + i, 9, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_process_signal_%d_delta" % (sid, i), "metric-note", delta, chip_x + 8, chip_y + 23, chip_w - 16, 14, z + 50 + i, 8, color=system_pal(profile, "ink"), priority=4))
        nx, ny = nodes[i - 1]
        cx = chip_x + chip_w / 2
        objects.append(shape_obj("%s_process_signal_to_node_%d" % (sid, i), "signal-vector", cx - 1, chip_y + 36, 2, max(18, ny - chip_y - 62), z + 36 + i, fill=tone, stroke=tone, shape="rect", priority=2, opacity=0.18, stroke_opacity=0.0))

    for i in range(len(nodes) - 1):
        x1, y1 = nodes[i]
        x2, y2 = nodes[i + 1]
        objects.append(shape_obj("%s_state_route_%d" % (sid, i + 1), "route-line", x1 + 44, y1 - 2, x2 - x1 - 88, 4, z + 58 + i, fill=system_pal(profile, "positive" if i < 1 else "accent"), stroke=system_pal(profile, "positive" if i < 1 else "accent"), shape="rect", priority=2, opacity=0.30, stroke_opacity=0.0))
    # Feedback loop makes it a state machine, not a one-way checklist.
    objects.append(shape_obj(sid + "_state_feedback_route", "route-line", x + 160, y + 126, 570, 3, z + 58, fill=system_pal(profile, "warning"), stroke=system_pal(profile, "warning"), shape="rect", priority=2, opacity=0.16, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_state_feedback_label", "research-folio", "月度复盘 / 授权覆核 / 再平衡", x + 420, y + 132, 250, 14, z + 60, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    for i, step in enumerate(process[:4], start=1):
        nx, ny = nodes[i - 1]
        tone_name = tones[i - 1]
        tone = system_tone_color(profile, tone_name)
        objects.append(shape_obj("%s_state_node_%d" % (sid, i), "process-node", nx - 24, ny - 24, 48, 48, z + 64 + i, fill=system_pal(profile, "panel"), stroke=tone, shape="ellipse", priority=3, opacity=0.96, stroke_opacity=0.82))
        objects.append(text_obj("%s_state_num_%d" % (sid, i), "process-step", step.get("step", ""), nx - 13, ny - 11, 30, 20, z + 68 + i, 10, color=tone, bold=True, priority=5))
        objects.append(text_obj("%s_state_title_%d" % (sid, i), "process-step", step.get("title", ""), nx - 58, ny + 34, 116, 18, z + 72 + i, 10, color=system_pal(profile, "ink"), bold=True, priority=5))
        objects.append(text_obj("%s_state_text_%d" % (sid, i), "process-step", step.get("text", ""), nx - 74, ny + 58, 148, 44, z + 76 + i, 8, color=system_pal(profile, "muted"), priority=5))

    # Compact governance strip remains inside the process panel as the right-side control rail.
    gx = x + 820
    gy = y + 66
    objects.append(shape_obj(sid + "_governance_strip", "trigger-row", gx - 16, gy - 14, 238, 154, z + 62, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "rule"), shape="roundRect", priority=3, opacity=0.70, stroke_opacity=0.28))
    objects.append(text_obj(sid + "_governance_head", "research-folio", "GOVERNANCE", gx, gy - 2, 120, 14, z + 70, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
    rows = [
        ("Trigger", "PMI>50 / 盈利确认"),
        ("Budget", "单周新增≤8%"),
        ("Hedge", "利率/政策扰动"),
        ("Review", "月度 / 偏离5ppt"),
    ]
    for i, (k, v) in enumerate(rows, start=1):
        ry = gy + 18 + (i - 1) * 28
        objects.append(text_obj("%s_governance_%d_k" % (sid, i), "research-folio", k, gx, ry, 68, 15, z + 72 + i, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
        objects.append(text_obj("%s_governance_%d_v" % (sid, i), "body", v, gx + 72, ry, 138, 18, z + 76 + i, 8, color=system_pal(profile, "ink"), priority=5))
    add_atlas_legend(objects, sid + "_process", x + 804, y + 224, z + 100, profile, [("当前节点", "positive"), ("风险部署", "accent"), ("风控闸门", "warning")])


def compile_paper_slide(slide, index):
    profile = VISUAL_SYSTEM_PROFILES["paper-analyst-report"]
    sid = slide["id"]
    objects = []
    body = slide.get("body", [])
    metrics = slide.get("metrics", [])
    paper_frame(objects, sid, index, slide)
    # Keep the research title inside the editorial text column. The right KPI
    # rail starts around x=920; title boxes must not silently extend beneath it.
    paper_title_w = 600 if index == 1 else 760
    paper_title_size = 23 if index == 1 else 28
    title_size = fit_title_size_no_orphan(slide["title"], paper_title_w, paper_title_size, min_size=20)
    title_h = max(76, estimate_text_height(slide["title"], paper_title_w, title_size) + 8)
    title_y = 126
    objects.append(text_obj(sid + "_title", "title", slide["title"], 96, title_y, paper_title_w, title_h, 20, title_size, color=system_pal(profile, "ink"), bold=True, priority=5))
    subtitle_y = title_y + title_h + 12
    if slide.get("subtitle"):
        objects.append(text_obj(sid + "_subtitle", "body", slide.get("subtitle", ""), 98, subtitle_y, 760, 34, 21, 13, color=system_pal(profile, "muted"), priority=5))
    body_rule_y = max(252, subtitle_y + (48 if slide.get("subtitle") else 28))
    body_y = body_rule_y + 24
    objects.append(shape_obj(sid + "_body_rule", "editorial-rule", 96, body_rule_y, 812, 1, 24, fill=system_pal(profile, "rule"), stroke=system_pal(profile, "rule"), shape="rect", priority=2, opacity=0.75, stroke_opacity=0.0))
    objects.append(text_obj(sid + "_exhibit_label", "research-folio", "EXHIBIT %02d / EVIDENCE CHAIN" % index, 96, body_rule_y - 22, 280, 18, 25, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
    # The analyst note is a right-column sidebar. Body text must never flow under it.
    # Chart pages reserve the lower half for editable axes/labels, so keep all
    # source paragraphs native but use a tighter research-brief rhythm.
    body_line_h = 34 if slide.get("chart") else 42
    body_size = 13 if slide.get("chart") else 15
    body_gap = 6 if slide.get("chart") else 10
    add_body_paragraphs(objects, sid, body, 104, body_y, 548, body_line_h, 30, size=body_size, max_items=3, gap=body_gap, profile={"palette": {"text": system_pal(profile, "ink"), "muted": system_pal(profile, "muted")}, "fonts": profile.get("fonts", {})})
    objects.append(shape_obj(sid + "_analyst_note_box", "analyst-note", 676, body_y, 190, 106, 38, fill=system_pal(profile, "panel"), stroke=system_pal(profile, "rule"), shape="rect", priority=3, opacity=1.0, stroke_opacity=0.55))
    objects.append(text_obj(sid + "_analyst_note_k", "research-folio", "ANALYST NOTE", 692, body_y + 12, 150, 16, 39, 8, color=system_pal(profile, "accent"), bold=True, priority=2))
    objects.append(text_obj(sid + "_analyst_note_t", "body", "结论优先，证据随后；所有数值保留为可编辑对象。", 692, body_y + 36, 150, 48, 40, 9, color=system_pal(profile, "muted"), priority=2))
    for i, metric in enumerate(metrics[:4], start=1):
        add_system_metric(objects, "%s_metric_%d" % (sid, i), metric, 906, 112 + (i - 1) * 104, 272, 92, 42 + i * 10, profile, role="ledger-metric")
    if slide.get("chart"):
        objects.append(chart_obj(sid + "_chart", slide["chart"], 96, 394, 770, 196, 70, chart_profile_for_system(profile)))
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
    return slide_ir(sid, objects)


def compile_atlas_slide(slide, index):
    profile = VISUAL_SYSTEM_PROFILES["market-atlas-infographic"]
    sid = slide["id"]
    objects = []
    body = slide.get("body", [])
    metrics = slide.get("metrics", [])
    atlas_frame(objects, sid, index, slide)
    atlas_title_w = 640
    title_size = fit_title_size_no_orphan(slide["title"], atlas_title_w, 21, min_size=17)
    title_h = min(72, max(54, estimate_text_height(slide["title"], atlas_title_w, title_size) + 10))
    title_y = 98
    objects.append(text_obj(sid + "_title", "title", slide["title"], 82, title_y, atlas_title_w, title_h, 20, title_size, color=system_pal(profile, "ink"), bold=True, priority=5))
    subtitle_y = title_y + title_h + 8
    if slide.get("subtitle"):
        objects.append(text_obj(sid + "_subtitle", "body", slide.get("subtitle", ""), 84, subtitle_y, 600, 34, 21, 11, color=system_pal(profile, "muted"), priority=5))
    body_y = 222
    if slide.get("process"):
        # Process slides already carry the main warning in the subtitle. Preserve
        # same-content body text natively, but move it into the Signal Field note
        # zone so the left narrative column does not create orphan punctuation.
        if body:
            objects.append(text_obj(sid + "_signal_note", "body", body[0], 84, body_y + 22, 560, 34, 42, 9, color=system_pal(profile, "muted"), priority=5))
    else:
        add_body_paragraphs(objects, sid, body, 88, body_y, 500, 34, 30, size=12, max_items=3, gap=8, profile={"palette": {"text": system_pal(profile, "ink"), "muted": system_pal(profile, "muted")}})
    if slide.get("chart") and len(metrics) >= 4:
        add_atlas_signal_field_map(objects, sid, metrics, 748, 236, 418, 268, 42, profile)
    elif not slide.get("scenarios") and not slide.get("process"):
        # Cover / thesis pages keep compact signal chips, but they no longer masquerade as a full Atlas map.
        tile_positions = [(748, 236), (904, 236), (1060, 236)]
        for i, metric in enumerate(metrics[:3], start=1):
            x, y = tile_positions[i - 1]
            tone = system_tone_color(profile, metric.get("tone"))
            objects.append(shape_obj("%s_metric_%d_chip" % (sid, i), "signal-chip", x, y, 138, 82, 42 + i * 10, fill=system_pal(profile, "paper"), stroke=tone, shape="roundRect", priority=3, opacity=0.84, stroke_opacity=0.68))
            objects.append(text_obj("%s_metric_%d_label" % (sid, i), "metric-label", metric.get("label", ""), x + 12, y + 8, 114, 16, 44 + i * 10, 8, color=system_pal(profile, "muted"), bold=True, priority=4))
            objects.append(text_obj("%s_metric_%d_value" % (sid, i), "metric", metric.get("value", ""), x + 12, y + 28, 114, 24, 45 + i * 10, 17, color=system_pal(profile, "ink"), bold=True, priority=5))
            objects.append(text_obj("%s_metric_%d_delta" % (sid, i), "metric-note", metric.get("delta", ""), x + 12, y + 54, 114, 22, 46 + i * 10, 8, color=tone, priority=4))
        # Fill the lower half of the right panel with a real decision map.
        # Allocation pages need an auditable if/then chain instead of repeated KPI cards.
        map_x, map_y = 748, 342
        is_allocation_chart = bool(slide.get("chart")) and (slide.get("chart", {}).get("categories", [])[:3] == ["当前", "建议", "上限"])
        objects.append(text_obj(sid + "_right_field_head", "research-folio", "DECISION CHAIN / LIMIT GUARDRAIL" if is_allocation_chart else "BUDGET CORRIDOR / DECISION MAP", map_x, map_y, 330, 16, 74, 8, color=system_pal(profile, "muted"), bold=True, priority=2))
        if is_allocation_chart:
            decision_rows = [
                ("Trigger", "权益风险预算释放 +5pct"),
                ("Action", "权益50→55；提高弹性但不追满"),
                ("Funding", "固收-4pct；另类现金-1pct"),
                ("Limit", "权益≤62；固收≥30；另类现金≥8"),
                ("Guardrail", "DD>5%或周撤>3%：停加风险/回建议仓位"),
            ]
            for j, (key, val) in enumerate(decision_rows, start=1):
                yy = map_y + 28 + (j - 1) * 30
                tone = "warning" if key == "Guardrail" else ("accent" if key in {"Trigger", "Action"} else "positive")
                objects.append(shape_obj("%s_decision_chain_%d" % (sid, j), "trigger-row", map_x, yy, 388, 24, 76 + j, fill=system_pal(profile, "panel"), stroke=system_tone_color(profile, tone), shape="roundRect", priority=3, opacity=0.76, stroke_opacity=0.34))
                objects.append(text_obj("%s_decision_chain_%d_key" % (sid, j), "research-folio", key, map_x + 10, yy + 5, 74, 13, 84 + j, 8, color=system_tone_color(profile, tone), bold=True, priority=3))
                objects.append(text_obj("%s_decision_chain_%d_val" % (sid, j), "body", val, map_x + 90, yy + 4, 286, 17, 90 + j, 8, color=system_pal(profile, "ink"), priority=5))
        else:
            band_labels = [("DEFENSIVE", "warning"), ("NEUTRAL+", "positive"), ("RISK ADD", "accent")]
            for j, (label, tone_name) in enumerate(band_labels, start=1):
                yy = map_y + 30 + (j - 1) * 34
                tone = system_tone_color(profile, tone_name)
                objects.append(shape_obj("%s_corridor_band_%d" % (sid, j), "route-map", map_x, yy, 388, 18, 74 + j, fill=tone, stroke=tone, shape="roundRect", priority=2, opacity=0.13 + j * 0.035, stroke_opacity=0.0))
                objects.append(text_obj("%s_corridor_band_%d_label" % (sid, j), "research-folio", label, map_x + 10, yy + 3, 110, 12, 78 + j, 7, color=system_pal(profile, "ink"), bold=True, priority=3))
            path_nodes = [(map_x + 136, map_y + 78), (map_x + 232, map_y + 63), (map_x + 328, map_y + 48)]
            for j, (nx, ny) in enumerate(path_nodes, start=1):
                if j > 1:
                    px, py = path_nodes[j - 2]
                    objects.append(shape_obj("%s_decision_route_%d" % (sid, j - 1), "route-line", px + 8, py + 5, nx - px - 10, 3, 90 + j, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.30, stroke_opacity=0.0))
                objects.append(shape_obj("%s_decision_node_%d" % (sid, j), "map-node", nx, ny, 14, 14, 96 + j, fill=system_pal(profile, "positive" if j < 3 else "accent"), stroke=system_pal(profile, "background"), shape="ellipse", priority=3, opacity=0.94, stroke_opacity=0.5))
            rule_rows = [
                ("Trigger", metrics[0].get("delta", "") if len(metrics) > 0 else "signal pass"),
                ("Budget", metrics[2].get("value", "") if len(metrics) > 2 else "neutral+"),
                ("Action", "纪律性加风险 / 保留回撤保护"),
            ]
            for j, (key, val) in enumerate(rule_rows, start=1):
                yy = map_y + 146 + (j - 1) * 22
                objects.append(text_obj("%s_decision_rule_%d_key" % (sid, j), "research-folio", key, map_x, yy, 76, 14, 104 + j, 8, color=system_pal(profile, "accent"), bold=True, priority=3))
                objects.append(text_obj("%s_decision_rule_%d_val" % (sid, j), "body", val, map_x + 82, yy, 300, 16, 108 + j, 8, color=system_pal(profile, "ink"), priority=5))
    if slide.get("chart"):
        add_atlas_budget_route_map(objects, sid, slide["chart"], 88, 398, 610, 204, 78, profile)
    elif slide.get("scenarios"):
        add_atlas_scenario_map(objects, sid, metrics, slide.get("scenarios", []), 724, 232, 468, 344, 78, profile)
    elif slide.get("process"):
        add_atlas_process_state_machine(objects, sid, slide.get("process", []), metrics, 88, 306, 1088, 278, 78, profile)
    if slide.get("risk_note"):
        objects.append(shape_obj(sid + "_footer_mask", "footer-mask", 80, 620, 1120, 34, 888, fill=system_pal(profile, "background"), stroke=system_pal(profile, "background"), shape="rect", priority=1, opacity=0.78, stroke_opacity=0.0))
        objects.append(shape_obj(sid + "_source_band", "route-line", 80, 622, 1120, 1, 890, fill=system_pal(profile, "positive"), stroke=system_pal(profile, "positive"), shape="rect", priority=2, opacity=0.04, stroke_opacity=0.0))
        objects.append(text_obj(sid + "_risk_note", "risk", slide["risk_note"], 88, 630, 1080, 20, 900, 9, color=system_pal(profile, "muted"), priority=5))
    apply_text_dna(objects, profile)
    return slide_ir(sid, objects, layout_graph=atlas_authored_layout_graph(sid, objects))


def compile_visual_system_contract(contract):
    style = contract.get("style_program")
    profile = VISUAL_SYSTEM_PROFILES[style]
    compiler = compile_paper_slide if style == "paper-analyst-report" else compile_atlas_slide
    deck = {
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
    if style == "market-atlas-infographic":
        deck["component_contract_refs"] = ["atlas-route-map"]
    return {"deck": deck}

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
