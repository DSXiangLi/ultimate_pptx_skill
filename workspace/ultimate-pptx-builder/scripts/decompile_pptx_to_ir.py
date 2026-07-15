#!/usr/bin/env python3
"""Decompile PPTX specimen into raw Slide IR for clone fidelity work.

This is Phase C2's first slice. It intentionally preserves conservative source
references and avoids semantic overclaiming; later phases can mine role semantics
and component contracts from this raw IR.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from analyze_pptx_specimen import inventory_objects, sha256_file  # noqa: E402


def editability_for(obj: Dict[str, Any]) -> Dict[str, Any]:
    text = (obj.get("text") or "").strip()
    typ = obj.get("type")
    if typ == "text" and not text:
        return {"priority": 1, "reason": "empty/decorative text container; preserve as metadata only"}
    if text:
        return {"priority": 5, "reason": "source object contains text; preserve native editability"}
    if typ in {"shape", "table", "chart"}:
        return {"priority": 3, "reason": "native PowerPoint object candidate"}
    if typ == "image":
        return {"priority": 2, "reason": "image asset; preserve source reference and raster fallback"}
    return {"priority": 2, "reason": "non-critical raw object"}


def render_policy_for(obj: Dict[str, Any]) -> str:
    text = (obj.get("text") or "").strip()
    typ = obj.get("type")
    if typ == "text" and not text:
        return "skip"
    if text:
        return "native"
    if typ in {"text", "shape", "table", "chart"}:
        return "native"
    if typ == "image":
        return "raster"
    if typ == "group":
        return "hybrid"
    return "native"


def classification_for(obj: Dict[str, Any]) -> Dict[str, Any]:
    text = (obj.get("text") or "").strip()
    typ = obj.get("type")
    if typ == "text" and not text:
        return {
            "kind": "empty-text-container",
            "reason": "text-frame object has no source text; treat as structural/decorative metadata rather than a visual placeholder",
        }
    return {"kind": "source-object"}


def box_for(obj: Dict[str, Any]) -> Dict[str, Any]:
    box = obj.get("box", {})
    return {
        "x": box.get("x_px", 0),
        "y": box.get("y_px", 0),
        "w": box.get("w_px", 0),
        "h": box.get("h_px", 0),
        "x_emu": box.get("x_emu", 0),
        "y_emu": box.get("y_emu", 0),
        "w_emu": box.get("w_emu", 0),
        "h_emu": box.get("h_emu", 0),
    }


def raw_ir_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    out = {
        "id": obj.get("id"),
        "type": obj.get("type"),
        "role_guess": "unknown",
        "box": box_for(obj),
        "z": obj.get("z", 0),
        "text": obj.get("text", ""),
        "style": obj.get("style", {}),
        "font": obj.get("font", {}),
        "source_xml_path": obj.get("source_xml_path"),
        "source_shape_id": obj.get("source_shape_id"),
        "source_shape_name": obj.get("source_shape_name") or obj.get("name", ""),
        "editability": editability_for(obj),
        "render_policy": render_policy_for(obj),
        "classification": classification_for(obj),
    }
    if obj.get("type") == "image":
        out["image_ref"] = {
            "content_type": obj.get("image_content_type"),
            "ext": obj.get("image_ext"),
            "sha1": obj.get("image_sha1"),
            "relationship_id": obj.get("image_relationship_id", ""),
            "relationship_type": obj.get("image_relationship_type", ""),
            "target": obj.get("image_target", ""),
            "package_path": obj.get("image_package_path", ""),
        }
    if obj.get("group_id"):
        out["group_id"] = obj.get("group_id")
        out["parent_group_name"] = obj.get("parent_group_name", "")
        out["group_depth"] = obj.get("group_depth", 0)
    if obj.get("child_count") is not None:
        out["child_count"] = obj.get("child_count")
    if obj.get("fill_image_package_path"):
        out["fill_image_ref"] = {
            "relationship_id": obj.get("fill_image_relationship_id", ""),
            "relationship_type": obj.get("fill_image_relationship_type", ""),
            "target": obj.get("fill_image_target", ""),
            "package_path": obj.get("fill_image_package_path", ""),
        }
    return out


def decompile(pptx: Path, deck_id: Optional[str] = None) -> Dict[str, Any]:
    pptx = pptx.resolve()
    inv = inventory_objects(pptx)
    slides: List[Dict[str, Any]] = []
    for slide in inv["slides"]:
        slides.append({
            "id": "slide-{:02d}".format(slide["index"]),
            "index": slide["index"],
            "source_xml_path": slide["source_xml_path"],
            "background": slide.get("background", {"kind": "default"}),
            "objects": [raw_ir_object(obj) for obj in slide["objects"]],
        })
    return {
        "deck": {
            "id": deck_id or pptx.stem,
            "source_pptx": str(pptx),
            "source_sha256": sha256_file(pptx),
            "size": inv.get("slide_size", {}),
            "slides": slides,
        },
        "decompiler": {
            "phase": "C2-raw-ir-v1",
            "semantic_confidence": "raw-object-inventory-only",
            "notes": [
                "role_guess is conservative; template archetype mining happens after rebuild fidelity evidence",
                "text-bearing objects are marked native and priority 5 to protect editability",
            ],
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Decompile PPTX into raw Slide IR")
    ap.add_argument("pptx")
    ap.add_argument("--out", required=True)
    ap.add_argument("--deck-id", default="")
    args = ap.parse_args()
    try:
        data = decompile(Path(args.pptx), deck_id=args.deck_id or None)
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as exc:
        print("FAIL decompile pptx to raw IR: {}".format(exc), file=sys.stderr)
        return 1
    print(str(args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
