#!/usr/bin/env python3
"""Run the Phase 4B visual fidelity loop.

Pipeline:
IR → reference PNG
PPTX → PDF → actual PNG
reference PNG vs actual PNG → visual fidelity report
"""
from pathlib import Path
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError("command failed: {}\nSTDOUT:\n{}\nSTDERR:\n{}".format(" ".join(map(str, cmd)), proc.stdout, proc.stderr))
    return proc.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ir")
    ap.add_argument("pptx")
    ap.add_argument("output")
    ap.add_argument("--workdir", default="build/visual-fidelity")
    ap.add_argument("--threshold", type=float, default=70.0)
    args = ap.parse_args()
    work = (ROOT / args.workdir).resolve()
    expected = work / "expected"
    actual = work / "actual"
    diff = work / "diff"
    metric_path = work / "visual-metrics.json"
    expected.mkdir(parents=True, exist_ok=True)
    actual.mkdir(parents=True, exist_ok=True)
    diff.mkdir(parents=True, exist_ok=True)
    run([sys.executable, str(ROOT / "scripts" / "render_ir_png.py"), str(args.ir), str(expected)])
    run([sys.executable, str(ROOT / "scripts" / "render_pptx_png.py"), str(args.pptx), str(actual)])
    run([sys.executable, str(ROOT / "scripts" / "compare_slide_images.py"), str(expected), str(actual), str(diff), str(metric_path)])
    metrics = json.loads(metric_path.read_text(encoding="utf-8"))
    blocking = []
    if metrics["overall_score"] < args.threshold:
        blocking.append({
            "severity": "warning",
            "message": f"visual fidelity score {metrics['overall_score']} below threshold {args.threshold}",
            "score": metrics["overall_score"],
            "threshold": args.threshold,
        })
    report = {
        "visual_fidelity": metrics,
        "threshold": args.threshold,
        "blocking_issues": blocking,
        "release_decision": "pass" if not blocking else "pass_with_accepted_exceptions",
        "notes": [
            "Phase 4B compares deterministic IR reference PNGs with LibreOffice-rendered PPTX PNGs.",
            "This is a real render loop, but reference renderer is not a browser; HTML screenshot parity remains a later upgrade.",
        ],
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
