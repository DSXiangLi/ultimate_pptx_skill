#!/usr/bin/env python3
"""Narrative safety checker for finance-grade PPTX content contracts.

This gate checks whether a deck follows the narrative kernel: audience job,
one-slide-one-job, claim/evidence/takeaway, deck arc, risk/source credibility,
and closure. It is deliberately lightweight and dependency-free so it can run
inside validate_skill.py.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import re
import sys

GENERIC_TITLES = {
    "市场分析", "核心观点", "总结展望", "数据分析", "趋势分析", "风险提示", "行动计划",
    "目录", "背景介绍", "主要内容", "策略建议", "关键洞察", "核心分析"
}
CLAIM_MARKERS = [
    "：", ":", "提升", "下降", "转向", "决定", "建议", "不", "只", "需", "需要", "进入", "控制",
    "优先", "从", "到", "共同", "路径", "下一步", "结论", "风险", "预算", "配置", "验证", "复核"
]
EVIDENCE_KEYS = ("metrics", "chart", "table", "matrix", "timeline", "process", "quote", "body")
OPENING_TOPS = {"cover", "hero", "summary", "glass-cover", "glass-hero"}
EVIDENCE_TOPS = {"dashboard", "chart", "chart-focus", "table", "matrix", "glass-dashboard", "glass-chart-focus", "glass-table", "glass-matrix"}
RISK_TOPS = {"scenario", "risk", "compliance", "quote", "glass-scenario", "glass-compliance", "glass-quote"}
ACTION_TOPS = {"action", "process", "timeline", "roadmap", "glass-action-rail", "glass-process", "glass-timeline"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"FAIL narrative safety: invalid JSON {path}: {exc}")


def issue(code: str, message: str, slide_id: str | None = None, level: str = "blocking") -> dict:
    out = {"code": code, "level": level, "message": message}
    if slide_id:
        out["slide_id"] = slide_id
    return out


def text_len(items) -> int:
    if not items:
        return 0
    if isinstance(items, str):
        return len(items.strip())
    if isinstance(items, list):
        return sum(len(str(x).strip()) for x in items)
    return len(str(items).strip())


def topology_family(topology: str) -> str:
    t = topology or ""
    for prefix in ("glass-",):
        if t.startswith(prefix):
            return t[len(prefix):]
    return t


def title_has_claim(title: str, topology: str) -> bool:
    t = (title or "").strip()
    if len(t) < 8 or t in GENERIC_TITLES:
        return False
    if re.fullmatch(r"[\u4e00-\u9fffA-Za-z\s]{2,10}", t) and not any(m in t for m in CLAIM_MARKERS):
        return False
    family = topology_family(topology)
    if family in {"compliance"} and any(k in t for k in ["合规", "适当性", "风险", "边界"]):
        return True
    return any(m in t for m in CLAIM_MARKERS) or len(t) >= 18


def has_evidence(slide: dict) -> bool:
    for key in EVIDENCE_KEYS:
        val = slide.get(key)
        if key == "body":
            if text_len(val) >= 18:
                return True
        elif val:
            return True
    return False


def has_takeaway(slide: dict) -> bool:
    if text_len(slide.get("body")) >= 18:
        return True
    subtitle = slide.get("subtitle", "")
    return len(subtitle.strip()) >= 12


def classify_arc(slide: dict) -> set[str]:
    top = slide.get("topology", "")
    family = topology_family(top)
    title = slide.get("title", "")
    job = slide.get("narrative_job", "")
    joined = " ".join([top, family, title, job])
    out = set()
    if top in OPENING_TOPS or family in OPENING_TOPS or any(k in joined for k in ["主论点", "摘要", "结论", "Executive"]):
        out.add("opening")
    if top in EVIDENCE_TOPS or family in EVIDENCE_TOPS or any(slide.get(k) for k in ["chart", "table", "metrics", "matrix"]):
        out.add("evidence")
    if top in RISK_TOPS or family in RISK_TOPS or any(k in joined for k in ["风险", "合规", "情景", "压力", "原则", "权衡"]):
        out.add("risk_or_turn")
    if top in ACTION_TOPS or family in ACTION_TOPS or any(k in joined for k in ["下一步", "行动", "执行", "路径", "复核", "监控", "日历"]):
        out.add("action")
    return out


def check_contract(contract: dict) -> list[dict]:
    issues = []
    user = contract.get("simulated_user_input", {})
    if not user.get("audience") or not user.get("scenario"):
        issues.append(issue("MISSING_AUDIENCE_JOB", "Deck must declare audience and scenario."))
    if not (user.get("desired_after_state") or user.get("desired_outcome") or user.get("raw_user_request")):
        issues.append(issue("MISSING_AUDIENCE_JOB", "Deck must declare desired after-state or raw user request."))

    slides = contract.get("slides", [])
    if not slides:
        issues.append(issue("ARC_GAP", "Deck has no slides."))
        return issues

    arc = set()
    prev_job = None
    duplicate_run = 0
    for idx, slide in enumerate(slides):
        sid = slide.get("id", f"slide-{idx+1}")
        top = slide.get("topology", "")
        title = slide.get("title", "")
        job = (slide.get("narrative_job") or "").strip()
        if not job:
            issues.append(issue("MISSING_NARRATIVE_JOB", "Slide must declare one primary narrative job.", sid))
        if title.strip() in GENERIC_TITLES or len(title.strip()) < 6:
            issues.append(issue("GENERIC_AI_TITLE", f"Title is generic or too weak: {title!r}", sid))
        if not title_has_claim(title, top):
            issues.append(issue("TITLE_NOT_CLAIM", f"Title should state a claim/action, not only a topic: {title!r}", sid))
        if not slide.get("risk_note"):
            issues.append(issue("MISSING_RISK_OR_SOURCE", "Finance slide must include risk/source rail.", sid))
        evidence = has_evidence(slide)
        if not evidence:
            issues.append(issue("CLAIM_WITHOUT_EVIDENCE", "Slide claim has no evidence/takeaway/source payload.", sid))
        if any(slide.get(k) for k in ["chart", "table", "metrics"]) and not has_takeaway(slide):
            issues.append(issue("EVIDENCE_WITHOUT_TAKEAWAY", "Data-heavy slide needs body/subtitle takeaway.", sid))
        if prev_job and job and job == prev_job:
            duplicate_run += 1
            if duplicate_run >= 1:
                issues.append(issue("DUPLICATE_NARRATIVE_JOB", "Consecutive slides repeat the same narrative job.", sid, level="warning"))
        else:
            duplicate_run = 0
        prev_job = job
        arc |= classify_arc(slide)

    required_arc = {"opening", "evidence", "risk_or_turn", "action"}
    missing_arc = sorted(required_arc - arc)
    if missing_arc:
        issues.append(issue("ARC_GAP", "Deck arc missing: " + ", ".join(missing_arc)))

    final = slides[-1]
    final_text = " ".join([final.get("topology", ""), final.get("title", ""), final.get("narrative_job", ""), " ".join(final.get("body", []))])
    if not any(k in final_text for k in ["下一步", "行动", "执行", "复核", "评审", "监控", "版本", "决策"]):
        issues.append(issue("WEAK_CLOSURE", "Final slide should leave action, decision, monitoring, or review path.", final.get("id")))
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("contract")
    ap.add_argument("--report")
    args = ap.parse_args()
    contract_path = Path(args.contract)
    contract = load_json(contract_path)
    issues = check_contract(contract)
    blocking = [x for x in issues if x.get("level") == "blocking"]
    report = {
        "checker": "check_narrative_safety",
        "contract": str(contract_path),
        "issue_count": len(issues),
        "blocking_count": len(blocking),
        "release_decision": "fail" if blocking else "pass",
        "issues": issues,
    }
    if args.report:
        Path(args.report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if blocking:
        print("FAIL narrative safety blocking=%d issues=%d" % (len(blocking), len(issues)))
        for item in blocking[:12]:
            loc = (item.get("slide_id") + " ") if item.get("slide_id") else ""
            print("- %s%s: %s" % (loc, item["code"], item["message"]))
        return 1
    print("PASS narrative safety slides=%d warnings=%d" % (len(contract.get("slides", [])), len(issues)))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
