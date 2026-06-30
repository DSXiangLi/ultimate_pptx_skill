#!/usr/bin/env python3
"""Render Slide IR to a traceable HTML preview.

Every exportable IR object becomes a DOM node with `data-ir-id`. HTML is a
preview renderer, not the source of truth.
"""
from pathlib import Path
import argparse
import html
import json


def hex_to_rgb(value, default="FFFFFF"):
    v = str(value or default).strip().lstrip("#")
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6:
        v = default
    return tuple(int(v[i:i+2], 16) for i in (0, 2, 4))


def css_color(value, opacity=1.0, default="FFFFFF"):
    r, g, b = hex_to_rgb(value, default)
    op = max(0.0, min(1.0, float(opacity if opacity is not None else 1.0)))
    if op >= 0.999:
        return "#%02X%02X%02X" % (r, g, b)
    return "rgba(%d,%d,%d,%.3f)" % (r, g, b, op)


def style_box(box, z):
    return (
        "position:absolute;left:%spx;top:%spx;"
        "width:%spx;height:%spx;z-index:%s;box-sizing:border-box;"
    ) % (box["x"], box["y"], box["w"], box["h"], z)


def render_chart_svg(obj):
    box = obj["box"]
    w, h = int(box["w"]), int(box["h"])
    categories = obj.get("categories", [])
    series = obj.get("series", [])
    tone = {"positive": "#31D0AA", "warning": "#FBBF24", "accent": "#8B5CF6"}
    title = html.escape(obj.get("title", ""))
    label_color = "#B6C7D8"
    plot_x, plot_y, plot_w, plot_h = 44, 66, max(1, w - 70), max(1, h - 116)
    max_total = 100
    if categories:
        max_total = max(max_total, max(sum(float(s.get("values", [0] * len(categories))[i]) for s in series if i < len(s.get("values", []))) for i in range(len(categories))))
    parts = [
        '<svg width="100%%" height="100%%" viewBox="0 0 %d %d" preserveAspectRatio="none">' % (w, h),
        '<rect x="0" y="0" width="%d" height="%d" rx="18" fill="rgba(19,36,58,.48)" stroke="rgba(42,111,145,.75)"/>' % (w, h),
        '<text x="18" y="22" fill="#EAF7FF" font-size="12" font-weight="700">%s</text>' % title,
    ]
    lx = 18
    for idx, s in enumerate(series[:3]):
        gx = lx + idx * 72
        parts.append('<rect x="%d" y="32" width="10" height="10" rx="2" fill="%s" opacity=".90"/>' % (gx, tone.get(s.get("tone"), "#5ED7FF")))
        parts.append('<text x="%d" y="41" fill="%s" font-size="10">%s</text>' % (gx + 15, label_color, html.escape(s.get("name", ""))))
    for val in [0, 50, 100]:
        yy = plot_y + plot_h - plot_h * val / max_total
        parts.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="rgba(94,215,255,.18)" stroke-width="1"/>' % (plot_x, yy, plot_x + plot_w, yy))
        parts.append('<text x="10" y="%.1f" fill="%s" font-size="9">%d%%</text>' % (yy + 3, label_color, val))
    if categories:
        gap = 10
        bw = max(10, (plot_w - gap * (len(categories) + 1)) / len(categories))
        for i, cat in enumerate(categories):
            x = plot_x + gap + i * (bw + gap)
            y_cursor = plot_y + plot_h
            for s in series:
                vals = s.get("values", [])
                val = float(vals[i]) if i < len(vals) else 0
                bh = plot_h * val / max_total
                y_cursor -= bh
                parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s" opacity=".86"/>' % (x, y_cursor, bw, bh, tone.get(s.get("tone"), "#5ED7FF")))
                if i == len(categories) - 1 and bh >= 13:
                    parts.append('<text x="%.1f" y="%.1f" fill="#EAF7FF" font-size="8" text-anchor="middle">%d</text>' % (x + bw / 2, y_cursor + bh / 2 + 3, int(round(val))))
            parts.append('<text x="%.1f" y="%d" fill="%s" font-size="10" text-anchor="middle">%s</text>' % (x + bw / 2, h - 30, label_color, html.escape(str(cat))))
    source = html.escape(obj.get("source", ""))
    if source:
        parts.append('<text x="18" y="%d" fill="%s" font-size="8">%s</text>' % (h - 10, label_color, source[:52]))
    parts.append('</svg>')
    return "".join(parts)


def render_table_html(obj):
    box = obj["box"]
    cols = obj.get("columns", [])
    rows = obj.get("rows", [])
    title = html.escape(obj.get("title", ""))
    cell_w = 100 / max(1, len(cols))
    parts = [
        '<div style="position:absolute;inset:0;border-radius:18px;background:rgba(19,36,58,.52);border:1px solid rgba(42,111,145,.75);overflow:hidden;padding:14px;box-sizing:border-box;color:#EAF7FF;font-family:Microsoft YaHei,Arial;">',
        '<div style="font-weight:700;font-size:13px;margin-bottom:8px;">%s</div>' % title,
        '<table style="width:100%;height:calc(100%% - 34px);border-collapse:collapse;table-layout:fixed;font-size:10px;">',
        '<tr>' + ''.join('<th style="width:%.2f%%;padding:5px;border:1px solid rgba(94,215,255,.22);background:rgba(25,50,77,.72);color:#B6C7D8;text-align:left;">%s</th>' % (cell_w, html.escape(str(c))) for c in cols) + '</tr>'
    ]
    for r, row in enumerate(rows):
        bg = 'rgba(19,36,58,.52)' if r % 2 == 0 else 'rgba(16,33,53,.58)'
        parts.append('<tr>' + ''.join('<td style="padding:5px;border:1px solid rgba(94,215,255,.16);background:%s;color:#EAF7FF;vertical-align:top;">%s</td>' % (bg, html.escape(str(cell))) for cell in row[:len(cols)]) + '</tr>')
    parts.append('</table>')
    if obj.get("source"):
        parts.append('<div style="position:absolute;left:14px;right:14px;bottom:5px;font-size:8px;color:#B6C7D8;white-space:nowrap;overflow:hidden;">%s</div>' % html.escape(str(obj.get("source"))[:80]))
    parts.append('</div>')
    return ''.join(parts)


def render_obj(obj):
    oid = html.escape(obj["id"])
    typ = obj["type"]
    role = html.escape(obj.get("role", ""))
    style = style_box(obj["box"], obj.get("z", 0))
    attrs = 'data-ir-id="%s" data-ir-type="%s" data-ir-role="%s"' % (oid, typ, role)
    if typ == "text":
        st = obj.get("style", {})
        css = style + (
            "font-family:%s;font-size:%spx;color:%s;font-weight:%s;"
            "line-height:1.25;white-space:normal;overflow:hidden;"
        ) % (
            st.get("font", "Arial"),
            st.get("size", 16),
            css_color(st.get("color", "111827"), st.get("opacity", 1.0), "111827"),
            "700" if st.get("bold") else "400",
        )
        return '<div class="ir-text" %s style="%s">%s</div>' % (attrs, css, html.escape(obj.get("text", "")))
    if typ == "shape":
        radius = "50%" if obj.get("shape") == "ellipse" else ("18px" if obj.get("shape") == "roundRect" else "0")
        shadow = "box-shadow:0 20px 48px rgba(0,0,0,.30);" if obj.get("shadow") else ""
        css = style + "background:%s;border:1px solid %s;border-radius:%s;%s" % (
            css_color(obj.get("fill", "FFFFFF"), obj.get("opacity", 1.0), "FFFFFF"),
            css_color(obj.get("stroke", "D1D5DB"), obj.get("stroke_opacity", 1.0), "D1D5DB"),
            radius,
            shadow,
        )
        return '<div class="ir-shape" %s style="%s"></div>' % (attrs, css)
    if typ == "chart":
        css = style + "border-radius:18px;overflow:hidden;filter:drop-shadow(0 18px 36px rgba(0,0,0,.28));"
        return '<div class="ir-chart" %s style="%s">%s</div>' % (attrs, css, render_chart_svg(obj))
    if typ == "table":
        css = style + "border-radius:18px;overflow:hidden;filter:drop-shadow(0 18px 36px rgba(0,0,0,.24));"
        return '<div class="ir-table" %s style="%s">%s</div>' % (attrs, css, render_table_html(obj))
    if typ == "rasterIsland":
        css = style + "background:linear-gradient(135deg,#F8FAFC,#E5E7EB);"
        note = html.escape(obj.get("source", {}).get("description", "raster island"))
        return '<div class="ir-raster" %s title="%s" style="%s"></div>' % (attrs, note, css)
    css = style + "outline:1px dashed #9CA3AF;"
    return '<div class="ir-unsupported" %s style="%s">%s</div>' % (attrs, css, typ)


def render(ir):
    deck = ir["deck"]
    size = deck.get("size", {"w": 1280, "h": 720})
    slides = []
    for slide in deck.get("slides", []):
        objects = sorted(slide.get("objects", []), key=lambda o: o.get("z", 0))
        body = "\n".join(render_obj(o) for o in objects)
        slides.append(
            '<section class="slide" data-slide-id="%s" style="position:relative;width:%spx;height:%spx;overflow:hidden;background:white;">\n%s\n</section>'
            % (html.escape(slide["id"]), size["w"], size["h"], body)
        )
    return """<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>Ultimate PPTX Preview</title>
<style>
body { margin: 0; background: #111827; display: grid; gap: 24px; padding: 24px; }
.slide { box-shadow: 0 16px 48px rgba(0,0,0,.35); }
</style>
</head>
<body>
%s
</body>
</html>
""" % "\n".join(slides)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Slide IR JSON")
    ap.add_argument("output", help="HTML preview output")
    args = ap.parse_args()
    ir = json.loads(Path(args.input).read_text(encoding="utf-8"))
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(render(ir), encoding="utf-8")
    print("wrote %s" % args.output)


if __name__ == "__main__":
    main()
