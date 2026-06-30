#!/usr/bin/env python3
"""Render PPTX to slide PNG images via LibreOffice + pdftoppm.

Requires system commands: libreoffice/soffice and pdftoppm.
"""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import sys
import tempfile


def cmd_path(*names):
    for n in names:
        p = shutil.which(n)
        if p:
            return p
    return None


def render(pptx, outdir, dpi=96, timeout=90):
    pptx = Path(pptx).resolve()
    outdir = Path(outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    soffice = cmd_path("libreoffice", "soffice")
    pdftoppm = cmd_path("pdftoppm")
    if not soffice:
        raise RuntimeError("LibreOffice/soffice not found")
    if not pdftoppm:
        raise RuntimeError("pdftoppm not found")
    with tempfile.TemporaryDirectory(prefix="ultimate-pptx-lo-") as td:
        tdir = Path(td)
        profile = tdir / "lo-profile"
        pdf_dir = tdir / "pdf"
        png_prefix = tdir / "slide"
        pdf_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            soffice,
            "--headless",
            f"-env:UserInstallation=file://{profile}",
            "--convert-to",
            "pdf",
            "--outdir",
            str(pdf_dir),
            str(pptx),
        ]
        proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError("LibreOffice conversion failed:\nSTDOUT:\n{}\nSTDERR:\n{}".format(proc.stdout, proc.stderr))
        pdfs = sorted(pdf_dir.glob("*.pdf"))
        if not pdfs:
            raise RuntimeError("LibreOffice did not produce a PDF. stdout={} stderr={}".format(proc.stdout, proc.stderr))
        pdf = pdfs[0]
        proc = subprocess.run([pdftoppm, "-png", "-r", str(dpi), str(pdf), str(png_prefix)], text=True, capture_output=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError("pdftoppm conversion failed:\nSTDOUT:\n{}\nSTDERR:\n{}".format(proc.stdout, proc.stderr))
        generated = sorted(tdir.glob("slide-*.png"))
        if not generated:
            raise RuntimeError("pdftoppm did not produce PNG slides")
        written = []
        for idx, src in enumerate(generated, start=1):
            dst = outdir / f"slide-{idx:02d}.png"
            shutil.copyfile(src, dst)
            written.append(str(dst))
        return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("outdir")
    ap.add_argument("--dpi", type=int, default=96)
    args = ap.parse_args()
    for p in render(args.pptx, args.outdir, dpi=args.dpi):
        print(p)

if __name__ == "__main__":
    main()
