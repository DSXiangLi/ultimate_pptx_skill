#!/usr/bin/env python3
"""Rendered perceptual layout QA using dependency-free PNG analysis.

This gate complements IR geometry by inspecting rendered slide PNGs. It estimates
foreground pixels relative to corner background color and blocks bottom/edge
pressure that can remain invisible to object-only checks.
"""
from __future__ import annotations

import argparse
import json
import struct
import sys
import zlib
from pathlib import Path


def issue(code, severity, message, evidence=None):
    return {"code": code, "severity": severity, "message": message, "evidence": evidence or {}}


def paeth(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def read_png_rgb(path: Path):
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError(f"not a PNG: {path}")
    pos = 8
    width = height = color_type = bit_depth = None
    idat = []
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos+4])[0]
        kind = data[pos+4:pos+8]
        payload = data[pos+8:pos+8+length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, bit_depth, color_type, _comp, _filter, _interlace = struct.unpack(">IIBBBBB", payload)
        elif kind == b"IDAT":
            idat.append(payload)
        elif kind == b"IEND":
            break
    if width is None or height is None or bit_depth is None or color_type is None:
        raise ValueError(f"missing PNG IHDR: {path}")
    if bit_depth != 8 or color_type not in {2, 6, 0}:
        raise ValueError(f"unsupported PNG format bit_depth={bit_depth} color_type={color_type}: {path}")
    channels = {0: 1, 2: 3, 6: 4}[color_type]
    raw = zlib.decompress(b"".join(idat))
    stride = width * channels
    rows = []
    i = 0
    prev = [0] * stride
    bpp = channels
    for _y in range(height):
        f = raw[i]
        i += 1
        scan = list(raw[i:i+stride])
        i += stride
        recon = [0] * stride
        for x in range(stride):
            left = recon[x-bpp] if x >= bpp else 0
            up = prev[x]
            up_left = prev[x-bpp] if x >= bpp else 0
            val = scan[x]
            if f == 0:
                r = val
            elif f == 1:
                r = (val + left) & 255
            elif f == 2:
                r = (val + up) & 255
            elif f == 3:
                r = (val + ((left + up) // 2)) & 255
            elif f == 4:
                r = (val + paeth(left, up, up_left)) & 255
            else:
                raise ValueError(f"unsupported PNG filter {f}: {path}")
            recon[x] = r
        prev = recon
        if color_type == 0:
            rows.append([(v, v, v) for v in recon])
        else:
            row = []
            for x in range(0, stride, channels):
                row.append((recon[x], recon[x+1], recon[x+2]))
            rows.append(row)
    return width, height, rows


def color_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])


def median_color(samples):
    return tuple(sorted(c[i] for c in samples)[len(samples)//2] for i in range(3))


def analyze_png(path: Path, bottom_safe_ratio: float, edge_safe_ratio: float, threshold: int):
    w, h, rows = read_png_rgb(path)
    corner_samples = []
    n = max(2, min(w, h) // 20)
    for y in list(range(n)) + list(range(h-n, h)):
        for x in list(range(n)) + list(range(w-n, w)):
            corner_samples.append(rows[y][x])
    bg = median_color(corner_samples)
    xs, ys = [], []
    bottom_band_pixels = 0
    bottom_start = int(h * (1 - bottom_safe_ratio))
    for y, row in enumerate(rows):
        for x, pix in enumerate(row):
            if color_dist(pix, bg) >= threshold:
                xs.append(x)
                ys.append(y)
                if y >= bottom_start:
                    bottom_band_pixels += 1
    if not xs:
        return {"path": str(path), "w": w, "h": h, "foreground_count": 0, "issues": []}
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    bottom_gap = h - 1 - max_y
    left_gap = min_x
    right_gap = w - 1 - max_x
    issues = []
    required_bottom = max(2, int(h * bottom_safe_ratio))
    required_edge = max(2, int(w * edge_safe_ratio))
    bottom_density = bottom_band_pixels / max(1, w * max(1, h - bottom_start))
    if bottom_gap < required_bottom and bottom_density > 0.03:
        issues.append(issue("RENDERED_BOTTOM_EDGE_PRESSURE", "blocking", "Rendered foreground is too close to the bottom edge with meaningful bottom-band density", {"slide": path.name, "bottom_gap_px": bottom_gap, "required_px": required_bottom, "bottom_density": round(bottom_density, 4)}))
    if left_gap < required_edge or right_gap < required_edge:
        issues.append(issue("RENDERED_SIDE_EDGE_PRESSURE", "warning", "Rendered foreground is close to horizontal edge", {"slide": path.name, "left_gap_px": left_gap, "right_gap_px": right_gap, "required_px": required_edge}))
    if bottom_density > 0.16:
        issues.append(issue("RENDERED_BOTTOM_DENSITY_HEAVY", "warning", "Bottom safe band has high foreground density", {"slide": path.name, "bottom_density": round(bottom_density, 4)}))
    return {"path": str(path), "w": w, "h": h, "foreground_count": len(xs), "foreground_bbox": {"x": min_x, "y": min_y, "w": max_x-min_x+1, "h": max_y-min_y+1}, "bottom_gap_px": bottom_gap, "issues": issues}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("actual_dir")
    ap.add_argument("--report", required=True)
    ap.add_argument("--bottom-safe-ratio", type=float, default=0.018)
    ap.add_argument("--edge-safe-ratio", type=float, default=0.006)
    ap.add_argument("--threshold", type=int, default=45)
    args = ap.parse_args(argv)
    actual = Path(args.actual_dir)
    paths = sorted(actual.glob("slide-*.png"))
    issues = []
    slides = []
    if not paths:
        issues.append(issue("RENDERED_ACTUAL_IMAGES_MISSING", "blocking", "No slide-*.png files found", {"actual_dir": str(actual)}))
    for path in paths:
        try:
            result = analyze_png(path, args.bottom_safe_ratio, args.edge_safe_ratio, args.threshold)
            slides.append(result)
            issues.extend(result.get("issues", []))
        except Exception as exc:
            issues.append(issue("RENDERED_PNG_ANALYSIS_ERROR", "blocking", str(exc), {"slide": path.name}))
    blocking = [i for i in issues if i["severity"] == "blocking"]
    report = {
        "gate": "rendered_perceptual_layout",
        "release_decision": "fail" if blocking else "pass",
        "blocking_count": len(blocking),
        "warning_count": len([i for i in issues if i["severity"] == "warning"]),
        "slides": slides,
        "issues": issues,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if report["release_decision"] != "pass":
        print("FAIL rendered perceptual layout", report["blocking_count"])
        return 1
    print("PASS rendered perceptual layout slides=%d warnings=%d" % (len(slides), report["warning_count"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
