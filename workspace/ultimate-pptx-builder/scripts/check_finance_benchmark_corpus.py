#!/usr/bin/env python3
"""Finance PPTX benchmark corpus validator.

The corpus is a regression contract for multi-scenario, multi-density, multi-style
finance deck generation. It does not replace full rendering gates; it ensures the
benchmark surface itself is broad enough and, when a build root is provided,
verifies that required gate reports exist and pass for real visual-system builds.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def issue(code, severity, message, evidence=None):
    return {"code": code, "severity": severity, "message": message, "evidence": evidence or {}}


def check_static(corpus):
    issues = []
    required_styles = set(corpus.get("required_style_programs") or [])
    required_scenarios = set(corpus.get("required_scenarios") or [])
    required_densities = set(corpus.get("required_density_modes") or [])
    required_reports = set(corpus.get("required_gate_reports") or [])
    cases = corpus.get("cases") or []

    if not required_styles or not required_scenarios or not required_densities:
        issues.append(issue("BENCHMARK_REQUIRED_AXES_MISSING", "blocking", "Corpus must declare required styles, scenarios, and density modes"))

    case_ids = [c.get("id") for c in cases]
    if len(case_ids) != len(set(case_ids)):
        issues.append(issue("BENCHMARK_DUPLICATE_CASE_ID", "blocking", "Benchmark case IDs must be unique"))

    pairs = {(c.get("scenario"), c.get("density_mode")) for c in cases}
    required_pairs = {(s, d) for s in required_scenarios for d in required_densities}
    missing_pairs = sorted(required_pairs - pairs)
    if missing_pairs:
        issues.append(issue(
            "BENCHMARK_SCENARIO_DENSITY_COVERAGE_MISSING",
            "blocking",
            "Corpus does not cover every required scenario × density pair",
            {"missing_pairs": missing_pairs},
        ))

    styles_seen = set()
    pressure_seen = set()
    preserve_failures = []
    for c in cases:
        styles = set(c.get("style_programs") or [])
        styles_seen |= styles
        pressure_seen.add(c.get("content_pressure"))
        if not required_styles.issubset(styles):
            preserve_failures.append({"case": c.get("id"), "missing_styles": sorted(required_styles - styles)})
        must = set(c.get("must_preserve") or [])
        if not {"source", "risk"}.issubset(must):
            preserve_failures.append({"case": c.get("id"), "missing_must_preserve": sorted({"source", "risk"} - must)})
        if c.get("content_pressure") == "high" and not {"evidence", "logic"}.issubset(must):
            preserve_failures.append({"case": c.get("id"), "high_pressure_missing": sorted({"evidence", "logic"} - must)})
    missing_styles_global = sorted(required_styles - styles_seen)
    if missing_styles_global or preserve_failures:
        issues.append(issue(
            "BENCHMARK_STYLE_COVERAGE_MISSING",
            "blocking",
            "Each benchmark case must run across all required style programs and preserve finance-critical fields",
            {"missing_styles_global": missing_styles_global, "case_failures": preserve_failures[:12]},
        ))

    if not {"low", "medium", "high"}.issubset(pressure_seen):
        issues.append(issue(
            "BENCHMARK_CONTENT_PRESSURE_COVERAGE_MISSING",
            "blocking",
            "Corpus must include low/medium/high content pressure",
            {"present": sorted(x for x in pressure_seen if x)},
        ))

    minimum_reports = {
        "layout-safety", "text-spacing", "alignment-graph", "component-layout-contract",
        "visual-layout-architecture", "visual-aesthetic-contract", "visual-dna-realization",
        "ooxml-visual-properties", "rendered-perceptual-layout", "visual-fidelity", "qa-report",
    }
    missing_reports = sorted(minimum_reports - required_reports)
    if missing_reports:
        issues.append(issue("BENCHMARK_REQUIRED_GATE_REPORTS_MISSING", "blocking", "Corpus must require every formal release gate report", {"missing_reports": missing_reports}))

    return issues, {
        "cases": len(cases),
        "scenario_density_pairs": len(pairs),
        "style_programs": len(styles_seen),
        "content_pressures": sorted(x for x in pressure_seen if x),
        "required_gate_reports": len(required_reports),
    }


def report_file_for(build, style, report_key):
    mapping = {
        "layout-safety": f"{style}-layout-safety-report.json",
        "text-spacing": f"{style}-text-spacing-report.json",
        "alignment-graph": f"{style}-alignment-graph-report.json",
        "component-layout-contract": f"{style}-component-layout-contract-report.json",
        "visual-layout-architecture": f"{style}-visual-layout-architecture-report.json",
        "visual-aesthetic-contract": f"{style}-visual-aesthetic-contract-report.json",
        "visual-dna-realization": f"{style}-visual-dna-realization-report.json",
        "ooxml-visual-properties": f"{style}-ooxml-visual-properties-report.json",
        "rendered-perceptual-layout": f"{style}-rendered-perceptual-layout-report.json",
        "visual-fidelity": f"{style}-visual-fidelity-report.json",
        "qa-report": f"{style}-qa-report.json",
    }
    return build / mapping[report_key]


def report_failure_evidence(report_key, data):
    """Return failure evidence for heterogeneous gate report shapes."""
    if report_key == "qa-report":
        blocking = data.get("blocking_issues") or []
        editability = float((data.get("scores") or {}).get("editability", 0))
        if blocking or editability < 95:
            return {"blocking_issues": len(blocking), "editability": editability}
        return None
    if report_key == "visual-fidelity":
        decision = data.get("release_decision")
        blocking = data.get("blocking_issues") or []
        score = float((data.get("visual_fidelity") or {}).get("overall_score", 0))
        threshold = float(data.get("threshold", 90))
        if decision == "fail" or blocking or score < threshold:
            return {"release_decision": decision, "blocking_issues": len(blocking), "score": score, "threshold": threshold}
        return None
    if data.get("release_decision") == "fail" or data.get("blocking_count", 0):
        return {"release_decision": data.get("release_decision"), "blocking_count": data.get("blocking_count")}
    return None


def check_build_reports(corpus, build_root: Path):
    issues = []
    required_styles = corpus.get("required_style_programs") or []
    required_reports = corpus.get("required_gate_reports") or []
    for style in required_styles:
        build = build_root / f"visual-system-{style}"
        if not build.exists():
            issues.append(issue("BENCHMARK_BUILD_MISSING", "blocking", "Expected visual-system build directory missing", {"style": style, "path": str(build)}))
            continue
        for key in required_reports:
            path = report_file_for(build, style, key)
            if not path.exists():
                issues.append(issue("BENCHMARK_GATE_REPORT_MISSING", "blocking", "Required gate report missing", {"style": style, "gate": key, "path": str(path)}))
                continue
            data = load_json(path)
            failure = report_failure_evidence(key, data)
            if failure:
                evidence = {"style": style, "gate": key, "path": str(path)}
                evidence.update(failure)
                issues.append(issue("BENCHMARK_GATE_REPORT_FAILED", "blocking", "Required gate report failed", evidence))
    return issues


def check(corpus, build_root=None):
    issues, coverage = check_static(corpus)
    if build_root:
        issues.extend(check_build_reports(corpus, Path(build_root)))
    blocking = [i for i in issues if i["severity"] == "blocking"]
    return {
        "gate": "finance_benchmark_corpus",
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i["severity"] == "warning"]),
        "coverage": coverage,
        "issues": issues,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus")
    ap.add_argument("--report", required=True)
    ap.add_argument("--build-root")
    args = ap.parse_args(argv)
    try:
        report = check(load_json(args.corpus), args.build_root)
    except Exception as exc:
        report = {"gate": "finance_benchmark_corpus", "release_decision": "fail", "blocking_count": 1, "warning_count": 0, "coverage": {}, "issues": [issue("BENCHMARK_CORPUS_CHECK_ERROR", "blocking", str(exc))]}
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if report["release_decision"] != "pass":
        print("FAIL finance benchmark corpus", report["blocking_count"])
        return 1
    print("PASS finance benchmark corpus cases=%d styles=%d pairs=%d" % (report["coverage"].get("cases", 0), report["coverage"].get("style_programs", 0), report["coverage"].get("scenario_density_pairs", 0)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
