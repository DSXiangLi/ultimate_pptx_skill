#!/usr/bin/env python3
"""Render Slide IR directly to reference PNG images with Pillow.

This deterministic renderer supports the native-shape glass simulation used by
the glass-fintech showcase. It remains deliberately browser-free because the
local environment lacks Chromium/Playwright.
"""
from pathlib import Path
import argparse
import json
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720


def color(value, default="#FFFFFF", opacity=1.0):
    v = str(value or default).strip()
    if not v.startswith("#"):
        v = "#" + v
    if len(v) == 4:
        v = "#" + "".join(ch * 2 for ch in v[1:])
    if len(v) != 7:
        v = default
    r, g, b = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
    a = int(round(max(0.0, min(1.0, float(opacity if opacity is not None else 1.0))) * 255))
    return (r, g, b, a)


def font(size=16, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, int(size))
    return ImageFont.load_default()


def text_width(draw, text, fnt):
    if hasattr(draw, "textbbox"):
        return draw.textbbox((0, 0), text, font=fnt)[2]
    if hasattr(draw, "textsize"):
        return draw.textsize(text, font=fnt)[0]
    try:
        return fnt.getsize(text)[0]
    except Exception:
        return len(str(text)) * 8


def wrap_text(draw, text, fnt, max_width):
    words = str(text).split()
    if not words:
        return [""]
    lines = []
    line = words[0]
    for word in words[1:]:
        candidate = line + " " + word
        if text_width(draw, candidate, fnt) <= max_width:
            line = candidate
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def draw_text(base, obj):
    box = obj["box"]
    style = obj.get("style", {})
    fnt = font(style.get("size", 16), style.get("bold", False))
    fill = color(style.get("color"), "#111827", style.get("opacity", 1.0))
    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    lines = wrap_text(draw, obj.get("text", ""), fnt, max(1, w - 4))
    line_h = max(12, int(float(style.get("size", 16)) * 1.25))
    yy = y
    for line in lines:
        if yy + line_h > y + h:
            break
        draw.text((x, yy), line, font=fnt, fill=fill)
        yy += line_h
    base.alpha_composite(overlay)


def draw_shape(base, obj):
    box = obj["box"]
    xy = [box["x"], box["y"], box["x"] + box["w"], box["y"] + box["h"]]
    fill = color(obj.get("fill"), "#E5E7EB", obj.get("opacity", 1.0))
    stroke = color(obj.get("stroke"), "#D1D5DB", obj.get("stroke_opacity", 1.0))
    if obj.get("shadow"):
        shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        sxy = [xy[0] + 10, xy[1] + 16, xy[2] + 10, xy[3] + 16]
        if obj.get("shape") == "ellipse":
            sd.ellipse(sxy, fill=(0, 0, 0, 55))
        elif obj.get("shape") == "roundRect" and hasattr(sd, "rounded_rectangle"):
            sd.rounded_rectangle(sxy, radius=18, fill=(0, 0, 0, 55))
        else:
            sd.rectangle(sxy, fill=(0, 0, 0, 55))
        base.alpha_composite(shadow)
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    if obj.get("shape") == "ellipse":
        draw.ellipse(xy, fill=fill, outline=stroke, width=2)
    elif obj.get("shape") == "roundRect" and hasattr(draw, "rounded_rectangle"):
        draw.rounded_rectangle(xy, radius=18, fill=fill, outline=stroke, width=2)
    else:
        draw.rectangle(xy, fill=fill, outline=stroke, width=2)
    base.alpha_composite(overlay)


def draw_raster_placeholder(base, obj):
    box = obj["box"]
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    xy = [box["x"], box["y"], box["x"] + box["w"], box["y"] + box["h"]]
    draw.rectangle(xy, fill=(243, 244, 246, 255), outline=(229, 231, 235, 255), width=2)
    draw.text((box["x"] + 12, box["y"] + 12), "rasterIsland placeholder", font=font(14, False), fill=(107, 114, 128, 255))
    base.alpha_composite(overlay)


def draw_chart(base, obj):
    box = obj["box"]
    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    xy = [x, y, x + w, y + h]
    st = obj.get("style", {})
    panel_fill = color(st.get("panel_fill", "13243A"), "#13243A", 0.48)
    panel_stroke = color(st.get("panel_stroke", "2A6F91"), "#2A6F91", 0.75)
    if hasattr(draw, "rounded_rectangle"):
        draw.rounded_rectangle(xy, radius=18, fill=panel_fill, outline=panel_stroke, width=2)
    else:
        draw.rectangle(xy, fill=panel_fill, outline=panel_stroke, width=2)
    title_f = font(12, True)
    label_f = font(10, False)
    tiny_f = font(8, False)
    draw.text((x + 18, y + 8), obj.get("title", ""), font=title_f, fill=color(st.get("title_color"), "#EAF7FF"))
    categories = obj.get("categories", [])
    series = obj.get("series", [])
    tone = {"positive": "31D0AA", "warning": "FBBF24", "accent": "8B5CF6"}
    lx = x + 18
    for idx, s in enumerate(series[:3]):
        gx = lx + idx * 72
        draw.rectangle([gx, y + 32, gx + 10, y + 42], fill=color(tone.get(s.get("tone"), "5ED7FF"), "#5ED7FF", 0.9))
        draw.text((gx + 15, y + 29), s.get("name", ""), font=label_f, fill=color("B6C7D8", "#B6C7D8"))
    plot_x, plot_y, plot_w, plot_h = x + 44, y + 66, max(1, w - 70), max(1, h - 116)
    max_total = 100
    if categories:
        for i in range(len(categories)):
            total = sum(float(s.get("values", [0] * len(categories))[i]) for s in series if i < len(s.get("values", [])))
            max_total = max(max_total, total)
    grid = color(st.get("grid_color"), "#2A6F91", 0.22)
    for val in [0, 50, 100]:
        yy = plot_y + plot_h - plot_h * val / max_total
        draw.line((plot_x, yy, plot_x + plot_w, yy), fill=grid, width=1)
        txt = "%d%%" % val
        draw.text((x + 10, yy - 6), txt, font=tiny_f, fill=color("B6C7D8", "#B6C7D8"))
    if categories:
        gap = 10
        bw = max(10, (plot_w - gap * (len(categories) + 1)) / len(categories))
        for i, cat in enumerate(categories):
            bx = plot_x + gap + i * (bw + gap)
            cursor = plot_y + plot_h
            for s in series:
                vals = s.get("values", [])
                val = float(vals[i]) if i < len(vals) else 0
                bh = plot_h * val / max_total
                cursor -= bh
                draw.rectangle([bx, cursor, bx + bw, cursor + bh], fill=color(tone.get(s.get("tone"), "5ED7FF"), "#5ED7FF", 0.86))
                if i == len(categories) - 1 and bh >= 13:
                    label = str(int(round(val)))
                    draw.text((bx + bw / 2 - text_width(draw, label, tiny_f) / 2, cursor + bh / 2 - 5), label, font=tiny_f, fill=color("EAF7FF", "#EAF7FF"))
            cat_txt = str(cat)
            draw.text((bx + bw / 2 - text_width(draw, cat_txt, label_f) / 2, y + h - 36), cat_txt, font=label_f, fill=color("B6C7D8", "#B6C7D8"))
    source = str(obj.get("source", ""))[:42]
    if source:
        draw.text((x + 18, y + h - 16), source, font=tiny_f, fill=color("B6C7D8", "#B6C7D8", 0.88))
    base.alpha_composite(overlay)


def draw_table(base, obj):
    box = obj["box"]
    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    st = obj.get("style", {})
    xy = [x, y, x+w, y+h]
    if hasattr(draw, "rounded_rectangle"):
        draw.rounded_rectangle(xy, radius=18, fill=color(st.get("row_fill", "13243A"), "#13243A", 0.52), outline=color(st.get("stroke", "2A6F91"), "#2A6F91", 0.75), width=2)
    else:
        draw.rectangle(xy, fill=color(st.get("row_fill", "13243A"), "#13243A", 0.52), outline=color(st.get("stroke", "2A6F91"), "#2A6F91", 0.75), width=2)
    title_f = font(13, True)
    header_f = font(10, True)
    cell_f = font(9, False)
    tiny_f = font(8, False)
    draw.text((x+14, y+10), obj.get("title", ""), font=title_f, fill=color(st.get("title_color"), "#EAF7FF"))
    cols = obj.get("columns", [])
    rows = obj.get("rows", [])
    if cols:
        tx, ty = x+14, y+38
        tw, th = w-28, h-64
        col_w = tw / len(cols)
        row_h = th / max(1, len(rows)+1)
        for c, col in enumerate(cols):
            cx = tx + c*col_w
            draw.rectangle([cx, ty, cx+col_w, ty+row_h], fill=color(st.get("header_fill", "19324D"), "#19324D", 0.82), outline=color(st.get("stroke", "2A6F91"), "#2A6F91", 0.5))
            draw.text((cx+5, ty+5), str(col)[:14], font=header_f, fill=color("B6C7D8", "#B6C7D8"))
        for r, row in enumerate(rows):
            ry = ty + (r+1)*row_h
            fill = st.get("row_fill", "13243A") if r % 2 == 0 else st.get("row_alt_fill", "102135")
            for c, cell in enumerate(row[:len(cols)]):
                cx = tx + c*col_w
                draw.rectangle([cx, ry, cx+col_w, ry+row_h], fill=color(fill, "#13243A", 0.58), outline=color(st.get("stroke", "2A6F91"), "#2A6F91", 0.35))
                lines = wrap_text(draw, str(cell), cell_f, col_w-10)
                yy = ry + 4
                for line in lines[:2]:
                    draw.text((cx+5, yy), line, font=cell_f, fill=color("EAF7FF", "#EAF7FF"))
                    yy += 12
    if obj.get("source"):
        draw.text((x+14, y+h-15), str(obj.get("source"))[:72], font=tiny_f, fill=color("B6C7D8", "#B6C7D8", 0.88))
    base.alpha_composite(overlay)


def render(ir, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    size = ir.get("deck", {}).get("size", {"w": W, "h": H})
    slides = ir.get("deck", {}).get("slides", [])
    written = []
    for idx, slide in enumerate(slides, start=1):
        img = Image.new("RGBA", (int(size.get("w", W)), int(size.get("h", H))), (255, 255, 255, 255))
        for obj in sorted(slide.get("objects", []), key=lambda o: o.get("z", 0)):
            if obj.get("type") == "shape":
                draw_shape(img, obj)
            elif obj.get("type") == "text":
                draw_text(img, obj)
            elif obj.get("type") == "chart":
                draw_chart(img, obj)
            elif obj.get("type") == "table":
                draw_table(img, obj)
            elif obj.get("type") == "rasterIsland":
                draw_raster_placeholder(img, obj)
        path = outdir / ("slide-%02d.png" % idx)
        img.convert("RGB").save(path)
        written.append(str(path))
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("outdir")
    args = ap.parse_args()
    ir = json.loads(Path(args.ir).read_text(encoding="utf-8"))
    written = render(ir, Path(args.outdir))
    for p in written:
        print(p)


if __name__ == "__main__":
    main()
