#!/usr/bin/env python3
# Export Slide IR to a minimal editable PPTX package with no external deps.
#
# Supports native editable text boxes and simple shapes, including the native
# translucency/shadow strategy used by glass-fintech-pptx.
from pathlib import Path
import argparse
import html
import json
import zipfile

SLIDE_W_EMU = 12192000
SLIDE_H_EMU = 6858000
BASE_W_PX = 1280
BASE_H_PX = 720
EMU_PER_PX_X = SLIDE_W_EMU / BASE_W_PX
EMU_PER_PX_Y = SLIDE_H_EMU / BASE_H_PX
CRITICAL_ROLES = {"title", "body", "risk", "source", "footnote", "metric", "metric-label", "metric-note"}


def esc(s):
    return html.escape(str(s), quote=True)


def emu(v, axis="x"):
    return int(round(float(v) * (EMU_PER_PX_X if axis == "x" else EMU_PER_PX_Y)))


def re_hex(v):
    return len(v) == 6 and all(ch in "0123456789ABCDEF" for ch in v)


def color(value, default="111827"):
    v = str(value or default).strip().lstrip("#").upper()
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if not re_hex(v):
        return default
    return v


def alpha_xml(opacity):
    op = max(0.0, min(1.0, float(opacity if opacity is not None else 1.0)))
    if op >= 0.999:
        return ""
    return '<a:alpha val="%d"/>' % int(round(op * 100000))


def solid_fill(value, default="111827", opacity=1.0):
    return '<a:solidFill><a:srgbClr val="%s">%s</a:srgbClr></a:solidFill>' % (color(value, default), alpha_xml(opacity))


def line_xml(value, default="D1D5DB", opacity=1.0):
    if float(opacity if opacity is not None else 1.0) <= 0:
        return '<a:ln><a:noFill/></a:ln>'
    return '<a:ln w="9525">%s</a:ln>' % solid_fill(value, default, opacity)


def xfrm(box):
    return (
        '<a:xfrm><a:off x="%s" y="%s"/><a:ext cx="%s" cy="%s"/></a:xfrm>'
        % (emu(box["x"], "x"), emu(box["y"], "y"), emu(box["w"], "x"), emu(box["h"], "y"))
    )


def shadow_xml(enabled):
    if not enabled:
        return ""
    return '<a:effectLst><a:outerShdw blurRad="63500" dist="25400" dir="5400000" algn="tl" rotWithShape="0"><a:srgbClr val="000000"><a:alpha val="25000"/></a:srgbClr></a:outerShdw></a:effectLst>'


def text_shape(obj, shape_id):
    box = obj["box"]
    st = obj.get("style", {})
    font = esc(st.get("font", "Microsoft YaHei"))
    size_pt = float(st.get("size", 16))
    size = int(size_pt * 100)
    b = ' b="1"' if st.get("bold") else ""
    fill = solid_fill(st.get("color", "111827"), "111827", st.get("opacity", 1.0))
    text = esc(obj.get("text", ""))
    role = obj.get("role", "")
    # PowerPoint/LibreOffice default Chinese line spacing is renderer-dependent.
    # Write explicit paragraph leading so wrapped native text does not collapse
    # into near-overlap in finance tables, matrix cells, and process cards.
    if role in {"risk", "source", "footnote"}:
        leading = 118000
    elif role in {"metric", "metric-label", "metric-note"}:
        leading = 112000
    elif size_pt <= 9:
        leading = 126000
    else:
        leading = 130000
    return '''<p:sp>
  <p:nvSpPr><p:cNvPr id="%s" name="%s"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
  <p:spPr>%s<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>
  <p:txBody><a:bodyPr wrap="square" anchor="t" lIns="0" tIns="0" rIns="0" bIns="0"/><a:lstStyle/><a:p><a:pPr><a:lnSpc><a:spcPct val="%s"/></a:lnSpc></a:pPr>
    <a:r><a:rPr lang="zh-CN" sz="%s"%s>%s<a:latin typeface="%s"/><a:ea typeface="%s"/></a:rPr><a:t>%s</a:t></a:r>
  </a:p></p:txBody>
</p:sp>''' % (shape_id, esc(obj['id']), xfrm(box), leading, size, b, fill, font, font, text)


def shape(obj, shape_id, placeholder=False):
    box = obj["box"]
    fill = obj.get("fill", "E5E7EB")
    stroke = obj.get("stroke", "D1D5DB")
    prst = obj.get("shape") or "rect"
    if prst not in {"roundRect", "rect", "ellipse"}:
        prst = "rect"
    name = esc(obj["id"] + ("__raster_placeholder" if placeholder else ""))
    return '''<p:sp>
  <p:nvSpPr><p:cNvPr id="%s" name="%s"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
  <p:spPr>%s<a:prstGeom prst="%s"><a:avLst/></a:prstGeom>%s%s%s</p:spPr>
</p:sp>''' % (
        shape_id,
        name,
        xfrm(box),
        prst,
        solid_fill(fill, "E5E7EB", obj.get("opacity", 1.0)),
        line_xml(stroke, "D1D5DB", obj.get("stroke_opacity", 1.0)),
        shadow_xml(obj.get("shadow", False)),
    )


def make_text_obj(oid, text, x, y, w, h, size=10, color_value="B6C7D8", bold=False, font="Microsoft YaHei"):
    return {
        "id": oid,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "text": text,
        "style": {"font": font, "size": size, "color": color_value, "bold": bold},
    }


def make_shape_obj(oid, x, y, w, h, fill, stroke=None, opacity=1.0, stroke_opacity=0.0, prst="rect"):
    return {
        "id": oid,
        "box": {"x": x, "y": y, "w": w, "h": h},
        "fill": fill,
        "stroke": stroke or fill,
        "opacity": opacity,
        "stroke_opacity": stroke_opacity,
        "shape": prst,
        "shadow": False,
    }


def chart_tone_color(tone, style=None, index=0):
    style = style or {}
    palette = style.get("series_palette") or []
    if palette:
        return color(palette[index % len(palette)], "5ED7FF")
    return {"positive": "31D0AA", "warning": "FBBF24", "accent": "7C3AED"}.get(tone, "5ED7FF")


def chart_vector_parts(obj, shape_id):
    box = obj["box"]
    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
    st = obj.get("style", {})
    categories = obj.get("categories", [])
    series = obj.get("series", [])
    parts = []

    def add_shape(oid, sx, sy, sw, sh, fill, stroke=None, opacity=1.0, stroke_opacity=0.0, prst="rect"):
        nonlocal shape_id
        parts.append(shape(make_shape_obj(oid, sx, sy, sw, sh, fill, stroke, opacity, stroke_opacity, prst), shape_id))
        shape_id += 1

    def add_text(oid, text, tx, ty, tw, th, size=10, color_value="B6C7D8", bold=False, font=None):
        nonlocal shape_id
        parts.append(text_shape(make_text_obj(oid, text, tx, ty, tw, th, size, color_value, bold, font or st.get("font", "Microsoft YaHei")), shape_id))
        shape_id += 1

    add_shape(obj["id"] + "_panel", x, y, w, h, st.get("panel_fill", "13243A"), st.get("panel_stroke", "2A6F91"), st.get("opacity", 0.48), st.get("stroke_opacity", 0.75), "roundRect")
    add_text(obj["id"] + "_title", obj.get("title", ""), x + 18, y + 8, max(1, w - 36), 20, 12, st.get("title_color", "EAF7FF"), True, st.get("title_font"))
    lx = x + 18
    for idx, ser in enumerate(series[:3]):
        gx = lx + idx * 72
        c = chart_tone_color(ser.get("tone"), st, idx)
        add_shape(obj["id"] + "_legend_swatch_%d" % (idx + 1), gx, y + 32, 10, 10, c, c, 0.92, 0.0)
        add_text(obj["id"] + "_legend_label_%d" % (idx + 1), ser.get("name", ""), gx + 15, y + 29, 54, 14, 9, st.get("label_color", "B6C7D8"), False)
    plot_x, plot_y, plot_w, plot_h = x + 44, y + 66, max(1, w - 70), max(1, h - 116)
    max_total = 100
    if categories:
        for i in range(len(categories)):
            total = sum(float(s.get("values", [0] * len(categories))[i]) for s in series if i < len(s.get("values", [])))
            max_total = max(max_total, total)
    for val in [0, 50, 100]:
        yy = plot_y + plot_h - plot_h * val / max_total
        add_shape(obj["id"] + "_grid_%d" % val, plot_x, yy, plot_w, 1, st.get("grid_color", "2A6F91"), st.get("grid_color", "2A6F91"), st.get("grid_opacity", 0.22), 0.0)
        add_text(obj["id"] + "_axis_%d" % val, "%d%%" % val, x + 8, yy - 7, 32, 12, 8, st.get("label_color", "B6C7D8"), False)
    if categories:
        gap = 10
        bw = max(10, (plot_w - gap * (len(categories) + 1)) / len(categories))
        bar_prst = st.get("bar_shape", "rect") if st.get("bar_shape") in {"rect", "roundRect"} else "rect"
        for i, cat in enumerate(categories):
            bx = plot_x + gap + i * (bw + gap)
            cursor = plot_y + plot_h
            for sidx, ser in enumerate(series):
                vals = ser.get("values", [])
                val = float(vals[i]) if i < len(vals) else 0
                bh = plot_h * val / max_total
                cursor -= bh
                c = chart_tone_color(ser.get("tone"), st, sidx)
                add_shape(obj["id"] + "_bar_%d_%d" % (i + 1, sidx + 1), bx, cursor, bw, max(1, bh), c, c, 0.88, 0.0, bar_prst)
                if i == len(categories) - 1 and bh >= 13:
                    add_text(obj["id"] + "_label_%d_%d" % (i + 1, sidx + 1), str(int(round(val))), bx, cursor + bh / 2 - 6, bw, 12, 8, st.get("value_label_color", "EAF7FF"), False)
            add_text(obj["id"] + "_cat_%d" % (i + 1), str(cat), bx - 4, y + h - 38, bw + 8, 14, 9, st.get("label_color", "B6C7D8"), False)
    source = str(obj.get("source", ""))[:42]
    if source:
        add_text(obj["id"] + "_source", source, x + 18, y + h - 18, w - 36, 12, 7, st.get("label_color", "B6C7D8"), False)
    return parts, shape_id


def table_vector_parts(obj, shape_id):
    box = obj["box"]
    x, y, w, h = box["x"], box["y"], box["w"], box["h"]
    st = obj.get("style", {})
    cols = obj.get("columns", [])
    rows = obj.get("rows", [])
    parts = []

    def add_shape(oid, sx, sy, sw, sh, fill, stroke=None, opacity=1.0, stroke_opacity=0.0, prst="rect"):
        nonlocal shape_id
        parts.append(shape(make_shape_obj(oid, sx, sy, sw, sh, fill, stroke, opacity, stroke_opacity, prst), shape_id))
        shape_id += 1

    def add_text(oid, text, tx, ty, tw, th, size=9, color_value="EAF7FF", bold=False):
        nonlocal shape_id
        parts.append(text_shape(make_text_obj(oid, text, tx, ty, tw, th, size, color_value, bold), shape_id))
        shape_id += 1

    add_shape(obj["id"] + "_panel", x, y, w, h, st.get("row_fill", "13243A"), st.get("stroke", "2A6F91"), 0.52, st.get("stroke_opacity", 0.75), "roundRect")
    add_text(obj["id"] + "_title", obj.get("title", ""), x+14, y+10, w-28, 20, 13, st.get("title_color", "EAF7FF"), True)
    if cols:
        tx, ty = x+14, y+38
        tw, th = w-28, h-64
        col_w = tw / len(cols)
        row_h = th / max(1, len(rows)+1)
        for c, col in enumerate(cols):
            cx = tx + c*col_w
            add_shape(obj["id"] + "_head_%d" % c, cx, ty, col_w, row_h, st.get("header_fill", "19324D"), st.get("stroke", "2A6F91"), 0.82, 0.5)
            add_text(obj["id"] + "_head_text_%d" % c, str(col)[:18], cx+6, ty+6, col_w-12, row_h-10, 10, st.get("label_color", "B6C7D8"), True)
        for r, row in enumerate(rows):
            ry = ty + (r+1)*row_h
            fill = st.get("row_fill", "13243A") if r % 2 == 0 else st.get("row_alt_fill", "102135")
            for c, cell in enumerate(row[:len(cols)]):
                cx = tx + c*col_w
                add_shape(obj["id"] + "_cell_%d_%d" % (r, c), cx, ry, col_w, row_h, fill, st.get("stroke", "2A6F91"), 0.58, 0.35)
                add_text(obj["id"] + "_cell_text_%d_%d" % (r, c), str(cell), cx+6, ry+5, col_w-12, row_h-10, 9, "EAF7FF", False)
    source = str(obj.get("source", ""))[:72]
    if source:
        add_text(obj["id"] + "_source", source, x+14, y+h-16, w-28, 12, 7, st.get("label_color", "B6C7D8"), False)
    return parts, shape_id


def slide_xml(slide):
    objects = sorted(slide.get("objects", []), key=lambda o: o.get("z", 0))
    parts = []
    report_objects = []
    shape_id = 2
    for obj in objects:
        priority = obj.get("editability", {}).get("priority", 1)
        role = obj.get("role", "")
        expected = "native" if priority >= 4 or role in CRITICAL_ROLES else obj.get("render_policy")
        actual = "unsupported"
        passed = False
        note = ""
        if obj.get("type") == "text":
            parts.append(text_shape(obj, shape_id))
            actual = "native-text"
            passed = True
        elif obj.get("type") == "shape":
            parts.append(shape(obj, shape_id))
            actual = "native-shape"
            passed = True
        elif obj.get("type") == "chart":
            chart_parts, shape_id = chart_vector_parts(obj, shape_id)
            parts.extend(chart_parts)
            actual = "editable-vector-chart"
            passed = True
            note = "MVP: chart exported as editable vector group of native shapes/text, not as raster."
            shape_id -= 1
        elif obj.get("type") == "table":
            table_parts, shape_id = table_vector_parts(obj, shape_id)
            parts.extend(table_parts)
            actual = "editable-vector-table"
            passed = True
            note = "MVP: table exported as editable vector group of native shapes/text, not raster."
            shape_id -= 1
        elif obj.get("type") == "rasterIsland":
            placeholder_obj = dict(obj)
            placeholder_obj["fill"] = "F3F4F6"
            placeholder_obj["stroke"] = "E5E7EB"
            placeholder_obj["shape"] = "rect"
            parts.append(shape(placeholder_obj, shape_id, placeholder=True))
            actual = "native-placeholder-for-rasterIsland"
            passed = priority <= 2 and role not in CRITICAL_ROLES and "source" in obj
            note = "MVP: rasterIsland exported as replaceable placeholder."
        else:
            note = "unsupported object type %s in MVP" % obj.get("type")
        report_objects.append({
            "id": obj.get("id"),
            "role": role,
            "type": obj.get("type"),
            "priority": priority,
            "expected": expected,
            "actual": actual,
            "pass": passed,
            "note": note,
        })
        shape_id += 1
    body = "\n".join(parts)
    xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree>
    <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
    <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    %s
  </p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>''' % body
    return xml, report_objects



def theme_xml():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Ultimate PPTX Theme">
  <a:themeElements>
    <a:clrScheme name="Office">
      <a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>
      <a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1F2937"/></a:dk2><a:lt2><a:srgbClr val="F8FAFC"/></a:lt2>
      <a:accent1><a:srgbClr val="2563EB"/></a:accent1><a:accent2><a:srgbClr val="059669"/></a:accent2><a:accent3><a:srgbClr val="D97706"/></a:accent3>
      <a:accent4><a:srgbClr val="7C3AED"/></a:accent4><a:accent5><a:srgbClr val="0891B2"/></a:accent5><a:accent6><a:srgbClr val="DC2626"/></a:accent6>
      <a:hlink><a:srgbClr val="2563EB"/></a:hlink><a:folHlink><a:srgbClr val="7C3AED"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Ultimate PPTX Fonts">
      <a:majorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:majorFont>
      <a:minorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Ultimate PPTX Format">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln><a:ln w="25400" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln><a:ln w="38100" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>'''


def blank_sp_tree():
    return '''<p:cSld name="Blank"><p:spTree>
  <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
  <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
</p:spTree></p:cSld>'''


def slide_layout_xml():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  %s
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>''' % blank_sp_tree()


def slide_master_xml():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  %s
  <p:clrMap accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" bg1="lt1" bg2="lt2" folHlink="folHlink" hlink="hlink" tx1="dk1" tx2="dk2"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId2"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>''' % blank_sp_tree()

def build_pptx(ir, pptx_path, report_path):
    deck = ir["deck"]
    slides = deck.get("slides", [])
    if not slides:
        raise ValueError("deck has no slides")
    slide_xmls = []
    audit = []
    for slide in slides:
        sx, objs = slide_xml(slide)
        slide_xmls.append(sx)
        audit.extend({"slide_id": slide.get("id"), **obj} for obj in objs)
    content_overrides = "\n".join(
        '<Override PartName="/ppt/slides/slide%s.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' % i
        for i in range(1, len(slide_xmls) + 1)
    )
    slide_ids = "\n".join('<p:sldId id="%s" r:id="rId%s"/>' % (255+i, i + 2) for i in range(1, len(slide_xmls) + 1))
    slide_rels = "\n".join('<Relationship Id="rId%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide%s.xml"/>' % (i + 2, i) for i in range(1, len(slide_xmls) + 1))
    files = {
        "[Content_Types].xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
  <Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
  <Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  %s
</Types>''' % content_overrides,
        "_rels/.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''',
        "docProps/core.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>%s</dc:title><dc:creator>ultimate-pptx-builder</dc:creator></cp:coreProperties>''' % esc(deck.get('id', 'Ultimate PPTX')),
        "docProps/app.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>ultimate-pptx-builder</Application><PresentationFormat>On-screen Show (16:9)</PresentationFormat><Slides>%s</Slides></Properties>''' % len(slide_xmls),
        "ppt/presentation.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId2"/></p:sldMasterIdLst>
  <p:sldIdLst>%s</p:sldIdLst>
  <p:sldSz cx="%s" cy="%s" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle><a:defPPr><a:defRPr lang="zh-CN"/></a:defPPr></p:defaultTextStyle>
</p:presentation>''' % (slide_ids, SLIDE_W_EMU, SLIDE_H_EMU),
        "ppt/_rels/presentation.xml.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  %s
  <Relationship Id="rId9991" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>
  <Relationship Id="rId9992" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>
  <Relationship Id="rId9993" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>
</Relationships>''' % slide_rels,
        "ppt/slideMasters/slideMaster1.xml": slide_master_xml(),
        "ppt/slideMasters/_rels/slideMaster1.xml.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>''',
        "ppt/slideLayouts/slideLayout1.xml": slide_layout_xml(),
        "ppt/slideLayouts/_rels/slideLayout1.xml.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>''',
        "ppt/theme/theme1.xml": theme_xml(),
        "ppt/presProps.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentationPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>''',
        "ppt/viewProps.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:viewPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:normalViewPr><p:restoredLeft sz="15620"/><p:restoredTop sz="94660"/></p:normalViewPr></p:viewPr>''',
        "ppt/tableStyles.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>''',
    }
    for i, sx in enumerate(slide_xmls, start=1):
        files["ppt/slides/slide%s.xml" % i] = sx
        files["ppt/slides/_rels/slide%s.xml.rels" % i] = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>'''
    pptx_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(pptx_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, text in files.items():
            zf.writestr(name, text)
    blocking = [o for o in audit if (o["priority"] >= 4 or o["role"] in CRITICAL_ROLES) and not o["pass"]]
    report = {
        "deck_id": deck.get("id"),
        "pptx_path": str(pptx_path),
        "objects_audited": audit,
        "blocking_issues": blocking,
        "release_decision": "pass" if not blocking else "fail",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Slide IR JSON")
    ap.add_argument("output", help="PPTX output path")
    ap.add_argument("--report", default=None, help="export report JSON path")
    args = ap.parse_args()
    ir = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = Path(args.report) if args.report else Path(args.output).with_suffix(".export-report.json")
    build_pptx(ir, Path(args.output), report)
    print("wrote %s" % args.output)
    print("wrote %s" % report)


if __name__ == "__main__":
    main()
