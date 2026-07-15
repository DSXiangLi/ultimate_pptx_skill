#!/usr/bin/env python3
"""Rebuild a PPTX from decompiled raw Slide IR for C3 fidelity diagnostics.

This is not the user-facing cloner product.  It is an internal diagnostic
artifact that proves whether the reverse compiler understands enough of the
source PPTX to materialize a strict, editable PPTX package.

First C3 slice:
- preserve slide count and slide size;
- rebuild text-bearing objects as native editable text boxes;
- rebuild simple non-text shapes as native rectangles/rounded rectangles when possible;
- materialize unsupported/images/groups/charts/tables as classified placeholders;
- write a report so later gates can distinguish unsupported effects from silent loss.
"""
from __future__ import annotations

import argparse
import io
import json
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE  # type: ignore
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN  # type: ignore
from pptx.util import Emu, Pt


SLIDE_W_EMU = 12192000
SLIDE_H_EMU = 6858000


def rgb(value: Any, default: str = "E5E7EB") -> RGBColor:
    v = str(value or default).strip().lstrip("#").upper()
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6 or any(ch not in "0123456789ABCDEF" for ch in v):
        v = default
    return RGBColor(int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))


def blank_layout(prs):
    for layout in prs.slide_layouts:
        if layout.name.lower() == "blank":
            return layout
    return prs.slide_layouts[6]


def apply_slide_background(slide, background: Dict[str, Any]) -> Dict[str, Any]:
    """Apply reconstructable slide-level background material."""
    kind = (background or {}).get("kind")
    if kind == "solid" and (background or {}).get("rgb"):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = rgb(background.get("rgb"), "FFFFFF")
        return {"kind": "solid", "rgb": str(background.get("rgb")).upper(), "produced": "native-slide-background"}
    if kind and kind not in {"default", "unknown"}:
        return {"kind": kind, "produced": "classified-background-degradation", "reason": background.get("degradation", "background kind not reconstructed yet")}
    return {"kind": kind or "default", "produced": "default"}


def box_emu(obj: Dict[str, Any]) -> Tuple[Emu, Emu, Emu, Emu]:
    box = obj.get("box") or {}
    return (
        Emu(int(round(float(box.get("x_emu", 0))))),
        Emu(int(round(float(box.get("y_emu", 0))))),
        Emu(max(1, int(round(float(box.get("w_emu", 0)))))),
        Emu(max(1, int(round(float(box.get("h_emu", 0)))))),
    )


def text_style(obj: Dict[str, Any]) -> Dict[str, Any]:
    font = obj.get("font") or {}
    style = obj.get("style") or {}
    return {
        "font": font.get("name") or style.get("font") or "Aptos",
        "size_pt": font.get("size_pt") or style.get("size") or 14,
        "bold": bool(font.get("bold", style.get("bold", False))),
        "color": font.get("color_rgb") or style.get("color") or "111827",
    }


def fill_color(obj: Dict[str, Any], default: str = "E5E7EB") -> str:
    style = obj.get("style") or {}
    return style.get("fill_rgb") or obj.get("fill") or default


def line_color(obj: Dict[str, Any], default: str = "CBD5E1") -> str:
    style = obj.get("style") or {}
    return style.get("line_rgb") or obj.get("stroke") or default


def placeholder_fill_for(typ: str) -> str:
    return {
        "image": "EEF2FF",
        "group": "F5F3FF",
        "chart": "ECFEFF",
        "table": "F0FDF4",
    }.get(typ, "F3F4F6")


def add_native_text(slide, obj: Dict[str, Any]) -> str:
    shp = slide.shapes.add_textbox(*box_emu(obj))
    shp.name = str(obj.get("id") or "rebuilt_text")[:250]
    tf = shp.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = str(obj.get("text") or "")
    st = text_style(obj)
    run.font.name = st["font"]
    try:
        run.font.size = Pt(float(st["size_pt"]))
    except Exception:
        run.font.size = Pt(14)
    run.font.bold = bool(st["bold"])
    run.font.color.rgb = rgb(st["color"], "111827")
    return "native-text"


def add_native_shape(slide, obj: Dict[str, Any], placeholder: bool = False) -> str:
    typ = obj.get("type") or "shape"
    shape_kind = MSO_SHAPE.ROUNDED_RECTANGLE if placeholder else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_kind, *box_emu(obj))
    suffix = "__placeholder" if placeholder else ""
    shp.name = (str(obj.get("id") or "rebuilt_shape") + suffix)[:250]
    shp.fill.solid()
    shp.fill.fore_color.rgb = rgb(placeholder_fill_for(typ) if placeholder else fill_color(obj), "E5E7EB")
    try:
        shp.line.color.rgb = rgb(line_color(obj), "CBD5E1")
        width_emu = (obj.get("style") or {}).get("line_width_emu")
        if width_emu:
            shp.line.width = Emu(int(width_emu))
        else:
            shp.line.width = Pt(0.75)
    except Exception:
        pass
    return "native-placeholder" if placeholder else "native-shape"


def add_native_image(slide, obj: Dict[str, Any], source_pptx: Path) -> str:
    image_ref = obj.get("image_ref") or {}
    package_path = str(image_ref.get("package_path") or "").lstrip("/")
    if not package_path:
        raise ValueError("image_ref.package_path is missing")
    if not source_pptx.exists():
        raise FileNotFoundError(str(source_pptx))
    with zipfile.ZipFile(str(source_pptx)) as zf:
        blob = zf.read(package_path)
    stream = io.BytesIO(blob)
    shp = slide.shapes.add_picture(stream, *box_emu(obj))
    shp.name = str(obj.get("id") or "rebuilt_image")[:250]
    return "native-image"


def add_picture_fill_shape_as_image(slide, obj: Dict[str, Any], source_pptx: Path) -> str:
    fill_ref = obj.get("fill_image_ref") or {}
    package_path = str(fill_ref.get("package_path") or "").lstrip("/")
    if not package_path:
        raise ValueError("fill_image_ref.package_path is missing")
    if not source_pptx.exists():
        raise FileNotFoundError(str(source_pptx))
    with zipfile.ZipFile(str(source_pptx)) as zf:
        blob = zf.read(package_path)
    stream = io.BytesIO(blob)
    shp = slide.shapes.add_picture(stream, *box_emu(obj))
    shp.name = (str(obj.get("id") or "rebuilt_picture_fill_shape") + "__picture_fill")[:250]
    return "native-picture-fill-shape-image"


def apply_table_cell_style(cell, style: Dict[str, Any]) -> bool:
    if not style:
        return False
    applied = False
    fill_rgb = style.get("fill_rgb")
    if fill_rgb:
        try:
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(fill_rgb)
            applied = True
        except Exception:
            pass
    try:
        tf = cell.text_frame
        for key in ["margin_left", "margin_right", "margin_top", "margin_bottom"]:
            value = style.get(key + "_emu")
            if value is not None:
                setattr(tf, key, Emu(int(value)))
                applied = True
        alignment = str(style.get("alignment") or "").upper()
        if alignment and tf.paragraphs:
            align_map = {
                "LEFT": PP_ALIGN.LEFT,
                "CENTER": PP_ALIGN.CENTER,
                "RIGHT": PP_ALIGN.RIGHT,
                "JUSTIFY": PP_ALIGN.JUSTIFY,
            }
            if alignment in align_map:
                tf.paragraphs[0].alignment = align_map[alignment]
                applied = True
        font_style = style.get("font") or {}
        if font_style and tf.paragraphs:
            runs = tf.paragraphs[0].runs
            if runs:
                font = runs[0].font
                if font_style.get("name"):
                    font.name = str(font_style.get("name"))
                    applied = True
                if font_style.get("size_pt"):
                    font.size = Pt(float(font_style.get("size_pt")))
                    applied = True
                if font_style.get("bold") is not None:
                    font.bold = bool(font_style.get("bold"))
                    applied = True
                if font_style.get("italic") is not None:
                    font.italic = bool(font_style.get("italic"))
                    applied = True
                if font_style.get("color_rgb"):
                    font.color.rgb = rgb(font_style.get("color_rgb"))
                    applied = True
    except Exception:
        pass
    return applied


def add_native_table(slide, obj: Dict[str, Any]) -> str:
    table_ref = obj.get("table_ref") or {}
    cells = table_ref.get("cells") or []
    cell_styles = table_ref.get("cell_styles") or []
    rows = int(table_ref.get("row_count") or len(cells) or 0)
    cols = int(table_ref.get("column_count") or (len(cells[0]) if cells else 0) or 0)
    if rows <= 0 or cols <= 0:
        raise ValueError("table_ref has no rows/columns")
    shape = slide.shapes.add_table(rows, cols, *box_emu(obj))
    shape.name = (str(obj.get("id") or "rebuilt_table") + "__table")[:250]
    table = shape.table
    styled_count = 0
    for r, row in enumerate(cells[:rows]):
        for c, value in enumerate(row[:cols]):
            cell = table.cell(r, c)
            cell.text = str(value or "")
            style = cell_styles[r][c] if r < len(cell_styles) and c < len(cell_styles[r]) else {}
            if apply_table_cell_style(cell, style):
                styled_count += 1
    obj["_styled_table_cells"] = styled_count
    return "native-table"


def add_placeholder_label(slide, obj: Dict[str, Any], label: str) -> None:
    # Keep label tiny and non-critical. It is diagnostic metadata, not source content.
    x, y, w, h = box_emu(obj)
    label_h = Emu(min(int(h), 240000))
    synthetic = {
        "id": str(obj.get("id") or "placeholder") + "__unsupported_label",
        "text": label,
        "box": {"x_emu": int(x) + 60000, "y_emu": int(y) + 40000, "w_emu": max(1, int(w) - 120000), "h_emu": max(1, int(label_h))},
        "font": {"name": "Aptos", "size_pt": 6, "color_rgb": "64748B", "bold": False},
    }
    add_native_text(slide, synthetic)


def is_critical_text(obj: Dict[str, Any]) -> bool:
    return bool((obj.get("text") or "").strip()) and int((obj.get("editability") or {}).get("priority") or 0) >= 4


def is_empty_text_container(obj: Dict[str, Any]) -> bool:
    return obj.get("type") == "text" and not (obj.get("text") or "").strip() and (obj.get("classification") or {}).get("kind") == "empty-text-container"


def rebuild(ir: Dict[str, Any], pptx_path: Path, report_path: Path) -> Dict[str, Any]:
    deck = ir.get("deck") or {}
    slides_ir = deck.get("slides") or []
    if not slides_ir:
        raise ValueError("raw IR has no slides")

    prs = Presentation()
    source_pptx = Path(str(deck.get("source_pptx") or ""))
    size = deck.get("size") or {}
    prs.slide_width = Emu(int(size.get("w_emu") or SLIDE_W_EMU))
    prs.slide_height = Emu(int(size.get("h_emu") or SLIDE_H_EMU))
    layout = blank_layout(prs)

    materialization: List[Dict[str, Any]] = []
    unsupported: List[Dict[str, Any]] = []
    critical_failures: List[Dict[str, Any]] = []
    backgrounds: List[Dict[str, Any]] = []

    for slide_ir in slides_ir:
        slide = prs.slides.add_slide(layout)
        background_result = apply_slide_background(slide, slide_ir.get("background") or {})
        background_result["slide_id"] = slide_ir.get("id")
        background_result["source_xml_path"] = slide_ir.get("source_xml_path")
        backgrounds.append(background_result)
        objects = sorted(slide_ir.get("objects") or [], key=lambda o: o.get("z", 0))
        for obj in objects:
            typ = obj.get("type") or "unknown"
            source_id = obj.get("source_shape_id")
            produced = "unsupported"
            note = ""
            try:
                if is_empty_text_container(obj):
                    produced = "skipped-empty-text-container"
                    note = "empty/decorative text container classified in C2; no visual placeholder emitted"
                elif (obj.get("text") or "").strip():
                    produced = add_native_text(slide, obj)
                elif typ == "group" and int(obj.get("child_count") or 0) > 0:
                    produced = "expanded-group-container"
                    note = "group children were emitted as separate IR objects; container is structural only"
                elif typ == "image":
                    produced = add_native_image(slide, obj, source_pptx)
                elif obj.get("fill_image_ref"):
                    produced = add_picture_fill_shape_as_image(slide, obj, source_pptx)
                elif typ == "table" and obj.get("table_ref"):
                    produced = add_native_table(slide, obj)
                elif typ == "shape":
                    produced = add_native_shape(slide, obj)
                else:
                    produced = add_native_shape(slide, obj, placeholder=True)
                    note = "classified placeholder for unsupported/non-critical raw object type"
                    add_placeholder_label(slide, obj, "{} placeholder".format(typ))
                    unsupported.append({
                        "id": obj.get("id"),
                        "type": typ,
                        "source_shape_id": source_id,
                        "reason": "first C3 baseline does not reconstruct this object class natively yet",
                    })
            except Exception as exc:
                note = "materialization error: {}".format(exc)
                if is_critical_text(obj):
                    critical_failures.append({"id": obj.get("id"), "type": typ, "error": str(exc)})
            if is_critical_text(obj) and produced != "native-text":
                critical_failures.append({
                    "id": obj.get("id"),
                    "type": typ,
                    "produced": produced,
                    "reason": "critical text was not rebuilt as native text",
                })
            materialization.append({
                "slide_id": slide_ir.get("id"),
                "id": obj.get("id"),
                "type": typ,
                "source_shape_id": source_id,
                "source_shape_name": obj.get("source_shape_name", ""),
                "group_id": obj.get("group_id", ""),
                "parent_group_name": obj.get("parent_group_name", ""),
                "child_count": obj.get("child_count"),
                "classification": (obj.get("classification") or {}).get("kind", ""),
                "table_rows": (obj.get("table_ref") or {}).get("row_count"),
                "table_columns": (obj.get("table_ref") or {}).get("column_count"),
                "styled_table_cells": obj.get("_styled_table_cells", 0),
                "has_text": bool((obj.get("text") or "").strip()),
                "editability_priority": (obj.get("editability") or {}).get("priority"),
                "produced": produced,
                "note": note,
            })

    pptx_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(pptx_path))
    report = {
        "deck_id": deck.get("id"),
        "pptx_path": str(pptx_path),
        "rebuilder": "C3-raw-ir-baseline-python-pptx",
        "slide_count": len(slides_ir),
        "object_count": sum(len(s.get("objects") or []) for s in slides_ir),
        "materialized_count": len(materialization),
        "unsupported_count": len(unsupported),
        "unsupported_objects": unsupported[:200],
        "backgrounds": backgrounds,
        "critical_failures": critical_failures,
        "objects": materialization,
        "release_decision": "pass" if not critical_failures else "fail",
        "notes": [
            "This rebuilt PPTX is an internal diagnostic artifact, not the reusable template product.",
            "Images/groups/charts/tables are classified placeholders in the first C3 baseline unless they contain critical text.",
        ],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description="Rebuild decompiled raw Slide IR into a diagnostic PPTX")
    ap.add_argument("ir", help="decompiled.raw.ir.json")
    ap.add_argument("output", help="rebuilt PPTX path")
    ap.add_argument("--report", default="", help="rebuild report path")
    args = ap.parse_args()
    try:
        ir = json.loads(Path(args.ir).read_text(encoding="utf-8"))
        pptx_path = Path(args.output)
        report_path = Path(args.report) if args.report else pptx_path.with_name("rebuild-report.json")
        report = rebuild(ir, pptx_path, report_path)
    except Exception as exc:
        print("FAIL rebuild decompiled IR PPTX: {}".format(exc), file=sys.stderr)
        return 1
    print(json.dumps({
        "release_decision": report["release_decision"],
        "pptx": str(args.output),
        "report": str(report_path),
        "unsupported_count": report["unsupported_count"],
        "critical_failures": len(report["critical_failures"]),
    }, ensure_ascii=False, indent=2))
    return 0 if report["release_decision"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
