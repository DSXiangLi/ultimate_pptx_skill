#!/usr/bin/env python3
"""Validate Office-compatible PPTX package structure.

This is intentionally stricter than ZIP/XML well-formedness. LibreOffice can open
minimal packages that Windows PowerPoint repairs because they lack slide
master/layout/theme relationships. This gate catches that class of failure.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import sys
import zipfile
import xml.etree.ElementTree as ET

REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"
P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

REQ_PARTS = {
    "[Content_Types].xml",
    "_rels/.rels",
    "docProps/core.xml",
    "docProps/app.xml",
    "ppt/presentation.xml",
    "ppt/_rels/presentation.xml.rels",
    "ppt/slideMasters/slideMaster1.xml",
    "ppt/slideMasters/_rels/slideMaster1.xml.rels",
    "ppt/slideLayouts/slideLayout1.xml",
    "ppt/slideLayouts/_rels/slideLayout1.xml.rels",
    "ppt/theme/theme1.xml",
    "ppt/presProps.xml",
    "ppt/viewProps.xml",
    "ppt/tableStyles.xml",
}


def rels(zipf: zipfile.ZipFile, name: str) -> list[dict[str, str]]:
    root = ET.fromstring(zipf.read(name))
    out = []
    for rel in root.findall(f"{REL_NS}Relationship"):
        out.append(rel.attrib)
    return out


def has_rel(zipf: zipfile.ZipFile, name: str, rel_type_suffix: str, target_suffix: str | None = None) -> bool:
    for rel in rels(zipf, name):
        if not rel.get("Type", "").endswith(rel_type_suffix):
            continue
        if target_suffix is not None and not rel.get("Target", "").endswith(target_suffix):
            continue
        return True
    return False


def check(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return [f"missing file: {path}"]
    try:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad:
                issues.append(f"bad zip member: {bad}")
            names = set(z.namelist())
            for part in sorted(REQ_PARTS):
                if part not in names:
                    issues.append(f"missing required Office part: {part}")
            for name in z.namelist():
                if name.endswith(".xml") or name.endswith(".rels"):
                    try:
                        ET.fromstring(z.read(name))
                    except Exception as exc:  # pragma: no cover - diagnostic path
                        issues.append(f"XML parse failure {name}: {exc}")
            if issues:
                return issues
            pres = ET.fromstring(z.read("ppt/presentation.xml"))
            if pres.find(f"{P_NS}sldMasterIdLst") is None:
                issues.append("presentation.xml lacks p:sldMasterIdLst")
            if not has_rel(z, "ppt/_rels/presentation.xml.rels", "/slideMaster", "slideMasters/slideMaster1.xml"):
                issues.append("presentation rels lacks slideMaster relationship")
            if not has_rel(z, "ppt/_rels/presentation.xml.rels", "/theme", "theme/theme1.xml"):
                issues.append("presentation rels lacks theme relationship")
            slide_parts = sorted(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
            if not slide_parts:
                issues.append("no slide parts")
            for slide in slide_parts:
                rel_name = slide.replace("ppt/slides/", "ppt/slides/_rels/") + ".rels"
                if rel_name not in names:
                    issues.append(f"missing slide rels: {rel_name}")
                    continue
                if not has_rel(z, rel_name, "/slideLayout", "../slideLayouts/slideLayout1.xml"):
                    issues.append(f"{rel_name} lacks slideLayout relationship")
            if not has_rel(z, "ppt/slideLayouts/_rels/slideLayout1.xml.rels", "/slideMaster", "../slideMasters/slideMaster1.xml"):
                issues.append("slideLayout1 rels lacks slideMaster relationship")
            if not has_rel(z, "ppt/slideMasters/_rels/slideMaster1.xml.rels", "/theme", "../theme/theme1.xml"):
                issues.append("slideMaster1 rels lacks theme relationship")
            if not has_rel(z, "ppt/slideMasters/_rels/slideMaster1.xml.rels", "/slideLayout", "../slideLayouts/slideLayout1.xml"):
                issues.append("slideMaster1 rels lacks slideLayout relationship")
    except zipfile.BadZipFile as exc:
        issues.append(f"bad zip file: {exc}")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx", nargs="+")
    args = ap.parse_args()
    all_issues: list[str] = []
    for item in args.pptx:
        issues = check(Path(item))
        if issues:
            all_issues.extend(f"{item}: {issue}" for issue in issues)
        else:
            print(f"PASS pptx package: {item}")
    if all_issues:
        print("FAIL pptx package")
        for issue in all_issues:
            print("-", issue)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
