#!/usr/bin/env python3
"""OOXML visual property audit.

Checks that IR visual effects that matter for PPTX materialization are present in
actual PPTX XML, rather than only in Python objects or HTML preview.
"""
from __future__ import annotations

import argparse
import html
import json
import sys
import zipfile
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def style_opacity(obj):
    st = obj.get("style") or {}
    vals = []
    for key in ["opacity", "fill_opacity", "stroke_opacity"]:
        if key in st:
            try:
                vals.append(float(st[key]))
            except Exception:
                pass
    return vals


def issue(code, severity, message, evidence=None):
    return {"code": code, "severity": severity, "message": message, "evidence": evidence or {}}


def read_pptx_xml(pptx):
    if not zipfile.is_zipfile(pptx):
        raise ValueError("not a PPTX/ZIP package")
    texts = []
    with zipfile.ZipFile(pptx) as zf:
        for name in zf.namelist():
            if name.startswith("ppt/slides/slide") and name.endswith(".xml"):
                texts.append(zf.read(name).decode("utf-8", errors="ignore"))
    return "\n".join(texts)


def check(ir, pptx):
    issues = []
    xml = read_pptx_xml(pptx)
    alpha_count = xml.count("<a:alpha") + xml.count(":alpha")
    translucent = []
    for slide, obj in iter_objects(ir):
        vals = style_opacity(obj)
        if vals and min(vals) < 0.999 and obj.get("render_policy") != "raster":
            translucent.append({"slide": slide.get("id"), "id": obj.get("id"), "opacity_values": vals})
    if translucent and alpha_count < len(translucent):
        issues.append(issue(
            "PPTX_ALPHA_MISSING",
            "blocking",
            "IR contains translucent native/vector objects but PPTX slide XML does not contain enough a:alpha entries",
            {"translucent_object_count": len(translucent), "alpha_xml_count": alpha_count, "examples": translucent[:8]},
        ))

    # Critical native text should have XML presence. This complements export report
    # and catches broken XML materialization when audit is run independently.
    xml_text_compact = "".join(html.unescape(xml).split())
    missing_text = []
    for _slide, obj in iter_objects(ir):
        text = obj.get("text")
        if not text:
            continue
        if obj.get("type") == "text" and obj.get("editability", {}).get("priority", 0) >= 4 and obj.get("render_policy") == "native":
            if "".join(text.split()) not in xml_text_compact:
                missing_text.append(obj.get("id"))
    if missing_text:
        issues.append(issue(
            "PPTX_CRITICAL_TEXT_XML_MISSING",
            "blocking",
            "Priority native text is missing from PPTX slide XML",
            {"missing_object_ids": missing_text[:12], "missing_count": len(missing_text)},
        ))

    blocking = [i for i in issues if i["severity"] == "blocking"]
    return {
        "gate": "ooxml_visual_properties",
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i["severity"] == "warning"]),
        "evidence": {"alpha_xml_count": alpha_count, "translucent_native_object_count": len(translucent)},
        "issues": issues,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("pptx")
    ap.add_argument("--report", required=True)
    args = ap.parse_args(argv)
    try:
        report = check(load_json(args.ir), args.pptx)
    except Exception as exc:
        report = {"gate": "ooxml_visual_properties", "release_decision": "fail", "blocking_count": 1, "warning_count": 0, "issues": [issue("PPTX_OOXML_AUDIT_ERROR", "blocking", str(exc))]}
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if report["release_decision"] != "pass":
        print("FAIL OOXML visual properties", report["blocking_count"])
        return 1
    print("PASS OOXML visual properties")
    return 0


if __name__ == "__main__":
    sys.exit(main())
