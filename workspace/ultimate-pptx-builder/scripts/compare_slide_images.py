#!/usr/bin/env python3
"""Compare reference and actual slide PNG images.

The metric is intentionally simple and dependency-light: mean absolute RGB error
normalized to 0..1, converted into a 0..100 fidelity score.
"""
from pathlib import Path
import argparse
import json
from PIL import Image, ImageChops, ImageStat


def compare_pair(expected, actual, diff_path=None):
    exp = Image.open(expected).convert("RGB")
    act = Image.open(actual).convert("RGB")
    if exp.size != act.size:
        act = act.resize(exp.size)
    diff = ImageChops.difference(exp, act)
    stat = ImageStat.Stat(diff)
    mae = sum(stat.mean) / (3 * 255)
    score = round(max(0, 100 * (1 - mae)), 2)
    if diff_path:
        # Amplify subtle differences for human inspection.
        amplified = diff.point(lambda p: min(255, p * 4))
        Path(diff_path).parent.mkdir(parents=True, exist_ok=True)
        amplified.save(diff_path)
    return {"mae": round(mae, 6), "score": score, "size": list(exp.size)}


def compare_dirs(expected_dir, actual_dir, diff_dir):
    expected = sorted(Path(expected_dir).glob("slide-*.png"))
    actual = sorted(Path(actual_dir).glob("slide-*.png"))
    if not expected:
        raise RuntimeError("no expected slide images found")
    if len(expected) != len(actual):
        raise RuntimeError(f"slide count mismatch: expected {len(expected)} actual {len(actual)}")
    slides = []
    for idx, (e, a) in enumerate(zip(expected, actual), start=1):
        diff_path = Path(diff_dir) / f"slide-{idx:02d}-diff.png"
        metric = compare_pair(e, a, diff_path)
        metric.update({
            "slide": idx,
            "expected": str(e),
            "actual": str(a),
            "diff": str(diff_path),
        })
        slides.append(metric)
    overall = round(sum(s["score"] for s in slides) / len(slides), 2)
    return {"overall_score": overall, "slides": slides}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("expected_dir")
    ap.add_argument("actual_dir")
    ap.add_argument("diff_dir")
    ap.add_argument("output")
    args = ap.parse_args()
    report = compare_dirs(args.expected_dir, args.actual_dir, args.diff_dir)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.output}")

if __name__ == "__main__":
    main()
