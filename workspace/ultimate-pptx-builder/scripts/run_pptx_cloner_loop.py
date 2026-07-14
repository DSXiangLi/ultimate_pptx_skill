#!/usr/bin/env python3
"""Run the PPTX cloner acceptance loop for a source deck.

This is the orchestration layer for the reverse-compiler workflow.  The current
executable slice validates C1/C2 end-to-end:

    source PPTX -> specimen evidence pack -> raw Slide IR -> acceptance report

Later C3-C7 builders can plug into the same loop by adding stages and gates, but
this file deliberately avoids pretending that a reusable template generator exists
before the rebuild/template-abstraction phases are implemented.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from analyze_pptx_specimen import analyze, create_contact_sheet, inventory_objects  # noqa: E402
from check_pptx_package import check as check_pptx_package  # noqa: E402
from compare_slide_images import compare_dirs  # noqa: E402
from decompile_pptx_to_ir import decompile  # noqa: E402
from rebuild_decompiled_ir_pptx import rebuild as rebuild_decompiled_ir  # noqa: E402
from render_pptx_png import render as render_pptx  # noqa: E402


REQUIRED_EVIDENCE_FILES = [
    "original.pptx",
    "provenance.json",
    "extracted-text.md",
    "object-inventory.json",
    "theme-inventory.json",
    "master-layout-inventory.json",
    "asset-inventory.json",
]

REQUIRED_IR_OBJECT_FIELDS = [
    "id",
    "type",
    "box",
    "z",
    "source_xml_path",
    "source_shape_id",
    "editability",
    "render_policy",
]


FAILURE_ACTIONS = {
    "missing_evidence_file": {
        "owner": "C1 analyzer",
        "action": "Extend analyze_pptx_specimen.py so the evidence pack always writes the missing file before later phases run.",
    },
    "missing_unpacked_slide_xml": {
        "owner": "C1 analyzer",
        "action": "Fix package unzip/input validation; do not continue if slide XML is absent from the preserved source package.",
    },
    "render_missing": {
        "owner": "C1 renderer",
        "action": "Repair render_pptx_png/LibreOffice/pdftoppm path or classify the render blocker; visual abstraction cannot start without full-size renders.",
    },
    "contact_sheet_missing": {
        "owner": "C1 renderer",
        "action": "Regenerate rendered/contact-sheet.png from slide PNGs so reviewers can inspect the specimen family quickly.",
    },
    "decompiled_ir_missing": {
        "owner": "C2 decompiler",
        "action": "Run or fix decompile_pptx_to_ir.py; raw IR is required before rebuild or template abstraction.",
    },
    "slide_count_mismatch": {
        "owner": "C2 decompiler",
        "action": "Fix slide enumeration so decompiled IR recalls every source slide exactly once.",
    },
    "object_count_mismatch": {
        "owner": "C2 decompiler",
        "action": "Fix object conversion/classification until raw IR object recall matches the C1 inventory or every unsupported object is explicitly classified.",
    },
    "text_recall_mismatch": {
        "owner": "C2 decompiler",
        "action": "Fix text extraction/decompilation; critical text recall must be 100% before C3 rebuild or template abstraction.",
    },
    "missing_ir_object_field": {
        "owner": "C2 decompiler",
        "action": "Add the missing source/reference/editability fields to raw IR objects so later gates can trace every decision to source evidence.",
    },
    "critical_text_not_native": {
        "owner": "C2 decompiler/export policy",
        "action": "Protect text-bearing objects as native/editable priority >=4; never let critical text silently become raster.",
    },
    "rebuilt_pptx_missing": {
        "owner": "C3 rebuilder",
        "action": "Fix rebuild_decompiled_ir_pptx.py so raw IR always materializes a rebuilt.pptx diagnostic package.",
    },
    "rebuilt_critical_failure": {
        "owner": "C3 rebuilder",
        "action": "Fix C3 materialization so critical/text-bearing source objects are rebuilt as native editable text.",
    },
    "rebuilt_package_invalid": {
        "owner": "C3 package/export",
        "action": "Fix rebuilt PPTX package relationships/parts until scripts/check_pptx_package.py passes.",
    },
    "rebuilt_slide_count_mismatch": {
        "owner": "C3 rebuilder",
        "action": "Fix rebuild slide creation so rebuilt PPTX slide count matches the source exactly.",
    },
    "rebuilt_text_recall_mismatch": {
        "owner": "C3 rebuilder",
        "action": "Fix rebuilt PPTX native text materialization until source text recall is 100%.",
    },
    "rebuilt_render_missing": {
        "owner": "C3 render/fidelity",
        "action": "Fix rebuilt PPTX rendering or package compatibility so LibreOffice can render every rebuilt slide.",
    },
    "rebuilt_visual_diff_missing": {
        "owner": "C3 render/fidelity",
        "action": "Fix visual diff generation; C3 must record baseline visual fidelity even when score is not yet blocking.",
    },
}


def utc_now() -> str:
    return _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def gate(gate_id: str, name: str, passed: bool, details: Dict[str, Any], failures: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    return {
        "id": gate_id,
        "name": name,
        "passed": bool(passed),
        "details": details,
        "failures": failures or [],
    }


def text_items_from_inventory(inventory: Dict[str, Any]) -> List[Tuple[int, str]]:
    items: List[Tuple[int, str]] = []
    for slide in inventory.get("slides", []):
        idx = int(slide.get("index", 0))
        for obj in slide.get("objects", []):
            text = (obj.get("text") or "").strip()
            if text:
                items.append((idx, text))
    return items


def text_items_from_ir(ir: Dict[str, Any]) -> List[Tuple[int, str]]:
    items: List[Tuple[int, str]] = []
    for slide in ir.get("deck", {}).get("slides", []):
        idx = int(slide.get("index", 0))
        for obj in slide.get("objects", []):
            text = (obj.get("text") or "").strip()
            if text:
                items.append((idx, text))
    return items


def flatten_ir_objects(ir: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [obj for slide in ir.get("deck", {}).get("slides", []) for obj in slide.get("objects", [])]


def evaluate_c1_c2(specimen_dir: Path, require_render: bool = False) -> Dict[str, Any]:
    gates: List[Dict[str, Any]] = []

    missing_files = [name for name in REQUIRED_EVIDENCE_FILES if not (specimen_dir / name).exists()]
    evidence_failures = [
        {"code": "missing_evidence_file", "file": name, **FAILURE_ACTIONS["missing_evidence_file"]}
        for name in missing_files
    ]
    gates.append(gate(
        "C1-EVIDENCE-PACK",
        "Specimen evidence pack files exist",
        not missing_files,
        {"required_files": REQUIRED_EVIDENCE_FILES, "missing_files": missing_files},
        evidence_failures,
    ))

    provenance = read_json(specimen_dir / "provenance.json") if (specimen_dir / "provenance.json").exists() else {}
    inventory = read_json(specimen_dir / "object-inventory.json") if (specimen_dir / "object-inventory.json").exists() else {}
    slide_count = int(provenance.get("slide_count") or inventory.get("slide_count") or 0)
    missing_slide_xml = []
    for idx in range(1, slide_count + 1):
        rel = specimen_dir / "unpacked" / "ppt" / "slides" / "slide{}.xml".format(idx)
        if not rel.exists():
            missing_slide_xml.append("ppt/slides/slide{}.xml".format(idx))
    gates.append(gate(
        "C1-UNPACKED-SLIDES",
        "Source package unpacks with slide XML evidence",
        slide_count > 0 and not missing_slide_xml,
        {"slide_count": slide_count, "missing_slide_xml": missing_slide_xml},
        [{"code": "missing_unpacked_slide_xml", "path": p, **FAILURE_ACTIONS["missing_unpacked_slide_xml"]} for p in missing_slide_xml],
    ))

    rendered_dir = specimen_dir / "rendered"
    rendered_slides = sorted(rendered_dir.glob("slide-*.png")) if rendered_dir.exists() else []
    render_pass = (not require_render) or (slide_count > 0 and len(rendered_slides) == slide_count)
    render_failures = []
    if require_render and len(rendered_slides) != slide_count:
        render_failures.append({"code": "render_missing", "expected": slide_count, "actual": len(rendered_slides), **FAILURE_ACTIONS["render_missing"]})
    if require_render and rendered_slides and not (rendered_dir / "contact-sheet.png").exists():
        render_failures.append({"code": "contact_sheet_missing", **FAILURE_ACTIONS["contact_sheet_missing"]})
    gates.append(gate(
        "C1-RENDER-EVIDENCE",
        "Full-size render/contact-sheet evidence exists when required",
        render_pass and not any(f["code"] == "contact_sheet_missing" for f in render_failures),
        {"require_render": require_render, "expected_slides": slide_count, "rendered_slides": len(rendered_slides), "contact_sheet_exists": (rendered_dir / "contact-sheet.png").exists()},
        render_failures,
    ))

    ir_path = specimen_dir / "decompiled.raw.ir.json"
    ir = read_json(ir_path) if ir_path.exists() else {}
    gates.append(gate(
        "C2-IR-EXISTS",
        "Decompiled raw Slide IR exists",
        bool(ir),
        {"path": str(ir_path), "exists": ir_path.exists()},
        [] if ir else [{"code": "decompiled_ir_missing", **FAILURE_ACTIONS["decompiled_ir_missing"]}],
    ))

    ir_slide_count = len(ir.get("deck", {}).get("slides", [])) if ir else 0
    gates.append(gate(
        "C2-SLIDE-RECALL",
        "IR slide count matches source inventory",
        bool(ir) and ir_slide_count == slide_count and slide_count > 0,
        {"source_slide_count": slide_count, "ir_slide_count": ir_slide_count},
        [] if (bool(ir) and ir_slide_count == slide_count and slide_count > 0) else [{"code": "slide_count_mismatch", "source_slide_count": slide_count, "ir_slide_count": ir_slide_count, **FAILURE_ACTIONS["slide_count_mismatch"]}],
    ))

    source_object_count = int(inventory.get("object_count") or 0)
    ir_objects = flatten_ir_objects(ir) if ir else []
    gates.append(gate(
        "C2-OBJECT-RECALL",
        "IR object count matches source inventory",
        bool(ir) and len(ir_objects) == source_object_count and source_object_count > 0,
        {"source_object_count": source_object_count, "ir_object_count": len(ir_objects)},
        [] if (bool(ir) and len(ir_objects) == source_object_count and source_object_count > 0) else [{"code": "object_count_mismatch", "source_object_count": source_object_count, "ir_object_count": len(ir_objects), **FAILURE_ACTIONS["object_count_mismatch"]}],
    ))

    source_text = text_items_from_inventory(inventory)
    ir_text = text_items_from_ir(ir) if ir else []
    missing_text = sorted(set(source_text) - set(ir_text))
    gates.append(gate(
        "C2-TEXT-RECALL",
        "Critical/source text recall is 100% in raw IR",
        bool(ir) and not missing_text,
        {"source_text_items": len(source_text), "ir_text_items": len(ir_text), "missing_text_items": [{"slide": s, "text": t} for s, t in missing_text[:20]]},
        [] if (bool(ir) and not missing_text) else [{"code": "text_recall_mismatch", "missing_count": len(missing_text), **FAILURE_ACTIONS["text_recall_mismatch"]}],
    ))

    missing_field_failures: List[Dict[str, Any]] = []
    critical_text_failures: List[Dict[str, Any]] = []
    for obj in ir_objects:
        missing = [field for field in REQUIRED_IR_OBJECT_FIELDS if field not in obj]
        if missing:
            missing_field_failures.append({"code": "missing_ir_object_field", "object_id": obj.get("id"), "missing_fields": missing, **FAILURE_ACTIONS["missing_ir_object_field"]})
        if (obj.get("text") or "").strip():
            priority = int((obj.get("editability") or {}).get("priority") or 0)
            if priority < 4 or obj.get("render_policy") != "native":
                critical_text_failures.append({"code": "critical_text_not_native", "object_id": obj.get("id"), "priority": priority, "render_policy": obj.get("render_policy"), **FAILURE_ACTIONS["critical_text_not_native"]})
    gates.append(gate(
        "C2-IR-OBJECT-CONTRACT",
        "Every IR object has source/editability/render-policy fields",
        bool(ir) and not missing_field_failures,
        {"object_count": len(ir_objects), "required_fields": REQUIRED_IR_OBJECT_FIELDS, "missing_field_failure_count": len(missing_field_failures)},
        missing_field_failures[:50],
    ))
    gates.append(gate(
        "C2-CRITICAL-TEXT-EDITABILITY",
        "Text-bearing objects remain native/editable priority >=4",
        bool(ir) and not critical_text_failures,
        {"text_object_count": len(ir_text), "failure_count": len(critical_text_failures)},
        critical_text_failures[:50],
    ))

    all_failures = [failure for g in gates for failure in g["failures"]]
    release_decision = "pass" if all(g["passed"] for g in gates) else "fail"
    return {
        "generated_at_utc": utc_now(),
        "phase": "C1-C2 executable baseline",
        "release_decision": release_decision,
        "blocking_count": len(all_failures),
        "gates": gates,
        "optimization_queue": all_failures,
        "next_phase_allowed": release_decision == "pass",
        "next_phase": "C3 diagnostic rebuild fidelity" if release_decision == "pass" else "fix blocking C1/C2 failures before C3",
    }


def render_rebuilt_and_compare(specimen_dir: Path, rebuilt_pptx: Path, slide_count: int, dpi: int) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    details: Dict[str, Any] = {
        "rendered_slides": 0,
        "expected_slides": slide_count,
        "contact_sheet_exists": False,
        "visual_fidelity_report": "",
        "overall_score": None,
    }
    failures: List[Dict[str, Any]] = []
    rendered_dir = specimen_dir / "rebuilt-rendered"
    diff_dir = specimen_dir / "rebuilt-diff"
    visual_report = specimen_dir / "rebuild-visual-fidelity-report.json"
    for path in [rendered_dir, diff_dir]:
        if path.exists():
            shutil.rmtree(str(path))
        path.mkdir(parents=True, exist_ok=True)
    try:
        rendered = render_pptx(rebuilt_pptx, rendered_dir, dpi=dpi)
        details["rendered_slides"] = len(rendered)
        if rendered:
            create_contact_sheet(rendered_dir)
            details["contact_sheet_exists"] = (rendered_dir / "contact-sheet.png").exists()
    except Exception as exc:
        failures.append({"code": "rebuilt_render_missing", "error": str(exc), **FAILURE_ACTIONS["rebuilt_render_missing"]})
        return details, failures
    if details["rendered_slides"] != slide_count:
        failures.append({"code": "rebuilt_render_missing", "expected": slide_count, "actual": details["rendered_slides"], **FAILURE_ACTIONS["rebuilt_render_missing"]})
        return details, failures
    try:
        metrics = compare_dirs(specimen_dir / "rendered", rendered_dir, diff_dir)
        write_json(visual_report, {
            "visual_fidelity": metrics,
            "threshold": "non-blocking-first-C3-baseline",
            "release_decision": "pass",
            "notes": [
                "First C3 baseline records source-vs-rebuilt visual score but does not block on low score yet.",
                "Images/groups/charts/tables may still be placeholders; use unsupported_objects in rebuild-report.json as the optimization queue for fidelity upgrades.",
            ],
        })
        details["visual_fidelity_report"] = str(visual_report)
        details["overall_score"] = metrics.get("overall_score")
    except Exception as exc:
        failures.append({"code": "rebuilt_visual_diff_missing", "error": str(exc), **FAILURE_ACTIONS["rebuilt_visual_diff_missing"]})
    return details, failures


def evaluate_c3(specimen_dir: Path, require_render: bool = False, dpi: int = 96) -> Dict[str, Any]:
    gates: List[Dict[str, Any]] = []
    ir_path = specimen_dir / "decompiled.raw.ir.json"
    rebuilt_pptx = specimen_dir / "rebuilt.pptx"
    rebuild_report_path = specimen_dir / "rebuild-report.json"
    ir = read_json(ir_path) if ir_path.exists() else {}
    source_inventory = read_json(specimen_dir / "object-inventory.json") if (specimen_dir / "object-inventory.json").exists() else {}
    source_slide_count = int(source_inventory.get("slide_count") or 0)

    rebuild_report: Dict[str, Any] = {}
    rebuild_failures: List[Dict[str, Any]] = []
    try:
        rebuild_report = rebuild_decompiled_ir(ir, rebuilt_pptx, rebuild_report_path)
    except Exception as exc:
        rebuild_failures.append({"code": "rebuilt_pptx_missing", "error": str(exc), **FAILURE_ACTIONS["rebuilt_pptx_missing"]})
    if rebuild_report.get("critical_failures"):
        for item in rebuild_report.get("critical_failures", [])[:50]:
            rebuild_failures.append({"code": "rebuilt_critical_failure", "failure": item, **FAILURE_ACTIONS["rebuilt_critical_failure"]})
    gates.append(gate(
        "C3-REBUILD-PPTX",
        "Raw IR materializes a diagnostic rebuilt.pptx with critical text preserved",
        rebuilt_pptx.exists() and not rebuild_failures,
        {
            "rebuilt_pptx": str(rebuilt_pptx),
            "rebuild_report": str(rebuild_report_path),
            "unsupported_count": rebuild_report.get("unsupported_count"),
            "critical_failure_count": len(rebuild_report.get("critical_failures") or []),
        },
        rebuild_failures,
    ))

    package_issues: List[str] = []
    if rebuilt_pptx.exists():
        package_issues = check_pptx_package(rebuilt_pptx)
    else:
        package_issues = ["rebuilt.pptx does not exist"]
    gates.append(gate(
        "C3-STRICT-PACKAGE",
        "Rebuilt PPTX passes strict Office package gate",
        not package_issues,
        {"package_issues": package_issues[:50]},
        [] if not package_issues else [{"code": "rebuilt_package_invalid", "issues": package_issues[:50], **FAILURE_ACTIONS["rebuilt_package_invalid"]}],
    ))

    rebuilt_inventory: Dict[str, Any] = {}
    rebuilt_inv_error = ""
    if rebuilt_pptx.exists():
        try:
            rebuilt_inventory = inventory_objects(rebuilt_pptx)
        except Exception as exc:
            rebuilt_inv_error = str(exc)
    rebuilt_slide_count = int(rebuilt_inventory.get("slide_count") or 0)
    slide_pass = source_slide_count > 0 and rebuilt_slide_count == source_slide_count
    gates.append(gate(
        "C3-REBUILT-SLIDE-RECALL",
        "Rebuilt PPTX slide count matches source",
        slide_pass,
        {"source_slide_count": source_slide_count, "rebuilt_slide_count": rebuilt_slide_count, "inventory_error": rebuilt_inv_error},
        [] if slide_pass else [{"code": "rebuilt_slide_count_mismatch", "source_slide_count": source_slide_count, "rebuilt_slide_count": rebuilt_slide_count, "error": rebuilt_inv_error, **FAILURE_ACTIONS["rebuilt_slide_count_mismatch"]}],
    ))

    source_text = text_items_from_inventory(source_inventory)
    rebuilt_text = text_items_from_inventory(rebuilt_inventory) if rebuilt_inventory else []
    missing_text = sorted(set(source_text) - set(rebuilt_text))
    text_pass = not missing_text
    gates.append(gate(
        "C3-REBUILT-TEXT-RECALL",
        "Rebuilt PPTX native text recall is 100%",
        text_pass,
        {"source_text_items": len(source_text), "rebuilt_text_items": len(rebuilt_text), "missing_text_items": [{"slide": s, "text": t} for s, t in missing_text[:30]]},
        [] if text_pass else [{"code": "rebuilt_text_recall_mismatch", "missing_count": len(missing_text), **FAILURE_ACTIONS["rebuilt_text_recall_mismatch"]}],
    ))

    render_details: Dict[str, Any] = {"require_render": require_render}
    render_failures: List[Dict[str, Any]] = []
    if require_render:
        render_details, render_failures = render_rebuilt_and_compare(specimen_dir, rebuilt_pptx, source_slide_count, dpi)
        render_details["require_render"] = True
    gates.append(gate(
        "C3-REBUILT-RENDER-BASELINE",
        "Rebuilt PPTX renders and records visual fidelity baseline when required",
        (not require_render) or not render_failures,
        render_details,
        render_failures,
    ))

    all_failures = [failure for g in gates for failure in g["failures"]]
    release_decision = "pass" if all(g["passed"] for g in gates) else "fail"
    return {
        "phase": "C3 diagnostic rebuild baseline",
        "release_decision": release_decision,
        "blocking_count": len(all_failures),
        "gates": gates,
        "optimization_queue": all_failures,
        "artifacts": {
            "rebuilt_pptx": str(rebuilt_pptx),
            "rebuild_report": str(rebuild_report_path),
            "rebuilt_rendered": str(specimen_dir / "rebuilt-rendered"),
            "visual_fidelity_report": str(specimen_dir / "rebuild-visual-fidelity-report.json"),
        },
    }


def merge_phase_reports(c12: Dict[str, Any], c3: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not c3:
        return c12
    gates = list(c12.get("gates") or []) + list(c3.get("gates") or [])
    failures = [failure for g in gates for failure in g.get("failures", [])]
    merged = dict(c12)
    merged["phase"] = "C1-C3 diagnostic rebuild baseline"
    merged["gates"] = gates
    merged["blocking_count"] = len(failures)
    merged["optimization_queue"] = failures
    merged["release_decision"] = "pass" if all(g.get("passed") for g in gates) else "fail"
    merged["next_phase_allowed"] = merged["release_decision"] == "pass"
    merged["next_phase"] = "C4 template archetype mining" if merged["next_phase_allowed"] else "fix blocking C1/C2/C3 failures before C4"
    merged["c3_artifacts"] = c3.get("artifacts", {})
    return merged

def run_iteration(pptx: Path, specimen_dir: Path, deck_id: str, source_url: str, license_note: str, skip_render: bool, require_render: bool, dpi: int) -> Dict[str, Any]:
    provenance = analyze(
        pptx,
        specimen_dir,
        deck_id=deck_id,
        source_url=source_url,
        license_note=license_note,
        skip_render=skip_render,
        dpi=dpi,
    )
    ir = decompile(specimen_dir / "original.pptx", deck_id=deck_id)
    write_json(specimen_dir / "decompiled.raw.ir.json", ir)
    report = evaluate_c1_c2(specimen_dir, require_render=require_render and not skip_render)
    if report.get("release_decision") == "pass":
        c3_report = evaluate_c3(specimen_dir, require_render=require_render and not skip_render, dpi=dpi)
        report = merge_phase_reports(report, c3_report)
    report["source"] = {
        "pptx": str(pptx.resolve()),
        "deck_id": deck_id,
        "specimen_dir": str(specimen_dir.resolve()),
        "provenance": provenance,
    }
    return report


def failure_signature(report: Dict[str, Any]) -> Tuple[str, ...]:
    return tuple(sorted("{}:{}".format(f.get("code"), f.get("object_id") or f.get("file") or f.get("path") or "") for f in report.get("optimization_queue", [])))


def main() -> int:
    ap = argparse.ArgumentParser(description="Run PPTX cloner C1/C2 acceptance loop")
    ap.add_argument("pptx", help="Source PPTX specimen")
    ap.add_argument("--deck-id", default="", help="Stable deck/template id; defaults to PPTX stem")
    ap.add_argument("--out", default="", help="Specimen output directory; defaults to specimens/<deck-id>")
    ap.add_argument("--source-url", default="", help="Original source URL if known")
    ap.add_argument("--license-note", default="", help="License/attribution note")
    ap.add_argument("--skip-render", action="store_true", help="Skip rendering; render gate becomes non-blocking")
    ap.add_argument("--require-render", action="store_true", help="Require slide PNGs/contact sheet for acceptance")
    ap.add_argument("--dpi", type=int, default=96, help="Render DPI when rendering is enabled")
    ap.add_argument("--max-iterations", type=int, default=3, help="Maximum loop attempts before declaring stalled")
    ap.add_argument("--report", default="", help="Report path; defaults to <out>/cloner-loop-report.json")
    args = ap.parse_args()

    pptx = Path(args.pptx)
    deck_id = args.deck_id or pptx.stem
    specimen_dir = Path(args.out) if args.out else ROOT / "specimens" / deck_id
    report_path = Path(args.report) if args.report else specimen_dir / "cloner-loop-report.json"

    if not pptx.exists():
        print("FAIL cloner loop: missing PPTX {}".format(pptx), file=sys.stderr)
        return 2

    history: List[Dict[str, Any]] = []
    previous_signature: Optional[Tuple[str, ...]] = None
    stalled = False
    final_report: Optional[Dict[str, Any]] = None

    for iteration in range(1, max(1, args.max_iterations) + 1):
        report = run_iteration(
            pptx=pptx,
            specimen_dir=specimen_dir,
            deck_id=deck_id,
            source_url=args.source_url,
            license_note=args.license_note,
            skip_render=args.skip_render,
            require_render=args.require_render,
            dpi=args.dpi,
        )
        sig = failure_signature(report)
        history.append({
            "iteration": iteration,
            "release_decision": report["release_decision"],
            "blocking_count": report["blocking_count"],
            "failure_signature": list(sig),
        })
        report["loop"] = {
            "iteration": iteration,
            "max_iterations": max(1, args.max_iterations),
            "history": history,
            "stalled": False,
            "stalled_reason": "",
        }
        final_report = report
        if report["release_decision"] == "pass":
            break
        if previous_signature is not None and sig == previous_signature:
            stalled = True
            report["loop"]["stalled"] = True
            report["loop"]["stalled_reason"] = "same blocking failures repeated; engineering change required before another useful iteration"
            final_report = report
            break
        previous_signature = sig

    if final_report is None:
        print("FAIL cloner loop: no report generated", file=sys.stderr)
        return 1
    if stalled:
        final_report["release_decision"] = "fail"
    write_json(report_path, final_report)
    print(json.dumps({
        "release_decision": final_report["release_decision"],
        "blocking_count": final_report["blocking_count"],
        "report": str(report_path),
        "next_phase_allowed": final_report.get("next_phase_allowed", False),
        "next_phase": final_report.get("next_phase"),
    }, ensure_ascii=False, indent=2))
    return 0 if final_report["release_decision"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
