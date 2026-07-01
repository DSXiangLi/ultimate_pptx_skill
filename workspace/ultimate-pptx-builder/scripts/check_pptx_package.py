#!/usr/bin/env python3
"""Validate Office-compatible PPTX package structure.

This gate is intentionally stricter than ZIP/XML well-formedness and less
brittle than checking one hand-written package layout. It validates relationship
resolution, slide shape ids/names, and optional python-pptx roundtrip reading so
minimal OOXML packages that PowerPoint/WPS may repair are not accepted blindly.
"""
from __future__ import annotations

from pathlib import Path, PurePosixPath
import argparse
import collections
import shutil
import sys
import tempfile
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
    "ppt/theme/theme1.xml",
    "ppt/presProps.xml",
    "ppt/viewProps.xml",
    "ppt/tableStyles.xml",
}


def rels(zipf: zipfile.ZipFile, name: str) -> list[dict[str, str]]:
    root = ET.fromstring(zipf.read(name))
    return [rel.attrib for rel in root.findall(f"{REL_NS}Relationship")]


def part_base(rels_name: str) -> PurePosixPath:
    # ppt/slides/_rels/slide1.xml.rels -> ppt/slides
    p = PurePosixPath(rels_name)
    if p.parent.name == "_rels":
        return p.parent.parent
    return p.parent


def resolve_target(rels_name: str, target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return str(part_base(rels_name).joinpath(target))


def normalized_target(rels_name: str, target: str) -> str:
    raw = resolve_target(rels_name, target)
    parts: list[str] = []
    for part in PurePosixPath(raw).parts:
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def find_rels(zipf: zipfile.ZipFile, rels_name: str, rel_type_suffix: str) -> list[tuple[dict[str, str], str]]:
    out = []
    for rel in rels(zipf, rels_name):
        if rel.get("Type", "").endswith(rel_type_suffix):
            out.append((rel, normalized_target(rels_name, rel.get("Target", ""))))
    return out


def require_rel(zipf: zipfile.ZipFile, names: set[str], rels_name: str, rel_type_suffix: str, label: str, target_must_exist=True) -> list[str]:
    found = find_rels(zipf, rels_name, rel_type_suffix)
    if not found:
        return [f"{rels_name} lacks {label} relationship"]
    issues = []
    if target_must_exist:
        for _rel, target in found:
            if target not in names:
                issues.append(f"{rels_name} {label} target missing: {target}")
    return issues


def strict_slide_shape_checks(zipf: zipfile.ZipFile, names: set[str]) -> list[str]:
    issues: list[str] = []
    for slide in sorted(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml")):
        root = ET.fromstring(zipf.read(slide))
        ids: list[str] = []
        blank_non_group: list[str] = []
        for parent in root.iter():
            for child in list(parent):
                if child.tag == f"{P_NS}cNvPr":
                    cid = child.attrib.get("id", "")
                    ids.append(cid)
                    # group shape id=1 may be blank in some producers; regular shapes should be named.
                    if cid != "1" and not child.attrib.get("name"):
                        blank_non_group.append(cid)
        for cid, count in collections.Counter(ids).items():
            if count > 1:
                issues.append(f"{slide} duplicate cNvPr id: {cid}")
        if blank_non_group:
            issues.append(f"{slide} has blank regular shape names: {blank_non_group[:8]}")
    return issues


def python_pptx_roundtrip(path: Path) -> list[str]:
    try:
        from pptx import Presentation
    except Exception as exc:
        return [f"python-pptx unavailable for roundtrip check: {exc}"]
    try:
        prs = Presentation(str(path))
        if len(prs.slides) <= 0:
            return ["python-pptx opened package but found zero slides"]
        tmpdir = Path(tempfile.mkdtemp(prefix="pptx-roundtrip-"))
        try:
            prs.save(str(tmpdir / "roundtrip.pptx"))
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)
    except Exception as exc:
        return [f"python-pptx roundtrip failed: {exc}"]
    return []


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
                    except Exception as exc:
                        issues.append(f"XML parse failure {name}: {exc}")
            if issues:
                return issues

            pres = ET.fromstring(z.read("ppt/presentation.xml"))
            if pres.find(f"{P_NS}sldMasterIdLst") is None:
                issues.append("presentation.xml lacks p:sldMasterIdLst")
            if pres.find(f"{P_NS}sldIdLst") is None:
                issues.append("presentation.xml lacks p:sldIdLst")
            issues += require_rel(z, names, "ppt/_rels/presentation.xml.rels", "/slideMaster", "slideMaster")
            issues += require_rel(z, names, "ppt/_rels/presentation.xml.rels", "/theme", "theme")

            slide_parts = sorted(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
            if not slide_parts:
                issues.append("no slide parts")
            for slide in slide_parts:
                rel_name = slide.replace("ppt/slides/", "ppt/slides/_rels/") + ".rels"
                if rel_name not in names:
                    issues.append(f"missing slide rels: {rel_name}")
                    continue
                issues += require_rel(z, names, rel_name, "/slideLayout", "slideLayout")

            layout_rels = sorted(n for n in names if n.startswith("ppt/slideLayouts/_rels/") and n.endswith(".rels"))
            if not layout_rels:
                issues.append("no slide layout rels")
            for rel_name in layout_rels:
                issues += require_rel(z, names, rel_name, "/slideMaster", "slideMaster")

            master_rels = sorted(n for n in names if n.startswith("ppt/slideMasters/_rels/") and n.endswith(".rels"))
            if not master_rels:
                issues.append("no slide master rels")
            for rel_name in master_rels:
                issues += require_rel(z, names, rel_name, "/theme", "theme")
                issues += require_rel(z, names, rel_name, "/slideLayout", "slideLayout")

            issues += strict_slide_shape_checks(z, names)
    except zipfile.BadZipFile as exc:
        issues.append(f"bad zip file: {exc}")
    if not issues:
        issues += python_pptx_roundtrip(path)
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
