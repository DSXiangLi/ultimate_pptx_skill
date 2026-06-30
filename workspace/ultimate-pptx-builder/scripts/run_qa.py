#!/usr/bin/env python3
"""Generate a Phase 4 QA report from IR + export report.

This MVP is not a visual-diff engine yet. It formalizes the QA surface so later
visual renderers can plug into the same `qa-report.json` contract.
"""
from pathlib import Path
import argparse
import json
import os

CRITICAL_ROLES = {"title", "body", "risk", "source", "footnote"}


def iter_objects(ir):
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            yield slide, obj


def score_editability(report):
    audited = report.get("objects_audited", [])
    critical = [o for o in audited if o.get("priority", 1) >= 4 or o.get("role") in CRITICAL_ROLES]
    if not critical:
        return 100
    passed = [o for o in critical if o.get("pass")]
    return round(100 * len(passed) / len(critical), 2)


def score_design(ir):
    roles = {obj.get("role") for _, obj in iter_objects(ir)}
    score = 70
    if "title" in roles:
        score += 10
    if "body" in roles:
        score += 10
    if any(r in roles for r in ["supporting-card", "chart", "table"]):
        score += 5
    if "risk" in roles or "source" in roles:
        score += 5
    return min(score, 100)


def score_practicality(ir, pptx_path):
    score = 100
    issues = []
    risk_present = any(obj.get("role") in {"risk", "source"} for _, obj in iter_objects(ir))
    if not risk_present:
        score -= 25
        issues.append({"severity": "blocker", "message": "finance deck lacks risk/source text"})
    for _, obj in iter_objects(ir):
        if obj.get("type") == "text":
            size = float(obj.get("style", {}).get("size", 16))
            role = obj.get("role")
            if role in {"risk", "source"}:
                if size < 9:
                    score -= 10
                    issues.append({"severity": "warning", "object_id": obj.get("id"), "message": "risk/source font below 9px"})
            elif size < 10:
                score -= 10
                issues.append({"severity": "warning", "object_id": obj.get("id"), "message": "text font below 10px"})
    if pptx_path and Path(pptx_path).exists():
        size_mb = Path(pptx_path).stat().st_size / (1024 * 1024)
        if size_mb > 20:
            score -= 20
            issues.append({"severity": "warning", "message": f"PPTX file is large: {size_mb:.1f} MB"})
    return max(score, 0), issues


def generate(ir, export_report, pptx_path=None, visual_report=None):
    blocking = list(export_report.get("blocking_issues", []))
    practicality_score, practicality_issues = score_practicality(ir, pptx_path)
    blocking.extend([i for i in practicality_issues if i.get("severity") == "blocker"])
    fidelity_score = 90
    notes = []
    if visual_report:
        fidelity_score = visual_report.get("visual_fidelity", {}).get("overall_score", fidelity_score)
        notes.append("Fidelity score comes from Phase 4B visual render comparison.")
        for issue in visual_report.get("blocking_issues", []):
            if issue.get("severity") == "blocker":
                blocking.append(issue)
            else:
                notes.append(issue)
    else:
        notes.append("Phase 4 MVP uses structural/heuristic fidelity because no visual report was supplied.")
    scores = {
        "fidelity": fidelity_score,
        "editability": score_editability(export_report),
        "design": score_design(ir),
        "practicality": practicality_score,
    }
    release = "pass" if not blocking and min(scores.values()) >= 90 else "fail"
    result = {
        "deck_id": ir.get("deck", {}).get("id", "unknown"),
        "scores": scores,
        "blocking_issues": blocking,
        "objects_audited": export_report.get("objects_audited", []),
        "release_decision": release,
        "notes": notes + [
            "Raster islands are currently placeholders in Phase 3 MVP and must be revisited for final visual fidelity.",
        ] + practicality_issues,
    }
    if visual_report:
        result["visual_fidelity"] = visual_report.get("visual_fidelity", visual_report)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("export_report")
    ap.add_argument("output")
    ap.add_argument("--pptx", default=None)
    ap.add_argument("--visual-report", default=None)
    args = ap.parse_args()
    ir = json.loads(Path(args.ir).read_text(encoding="utf-8"))
    report = json.loads(Path(args.export_report).read_text(encoding="utf-8"))
    visual_report = json.loads(Path(args.visual_report).read_text(encoding="utf-8")) if args.visual_report else None
    qa = generate(ir, report, args.pptx, visual_report=visual_report)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.output}")

if __name__ == "__main__":
    main()
