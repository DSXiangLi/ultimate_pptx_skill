# Phase 4B: Visual Fidelity Loop MVP

## Purpose

Add a real visual loop to the builder rather than relying only on structural checks.

The current MVP compares:

```text
Slide IR → deterministic reference PNG
PPTX → LibreOffice PDF → pdftoppm PNG
reference PNG vs actual PNG → visual fidelity report
```

## Why Not Browser Screenshot First?

The local environment has LibreOffice, `pdftoppm`, and Pillow, but no Chromium/Node/Playwright. Therefore Phase 4B starts with an IR reference renderer. This is less expressive than HTML screenshots but immediately gives us a reproducible visual regression gate.

See `docs/learning/phase4b-visual-rendering.md` before changing this pipeline.

## Deliverables

- `scripts/render_ir_png.py`
- `scripts/render_pptx_png.py`
- `scripts/compare_slide_images.py`
- `scripts/run_visual_fidelity.py`
- generated expected PNGs under `build/visual-fidelity/expected/`
- generated actual PNGs under `build/visual-fidelity/actual/`
- generated diff PNGs under `build/visual-fidelity/diff/`
- generated report: `build/visual-fidelity-report.json`

## Acceptance Criteria

- IR reference PNGs are generated for every slide.
- PPTX actual PNGs are generated through LibreOffice + pdftoppm.
- Expected/actual slide counts match.
- Diff PNGs are produced for human inspection.
- Report includes `overall_score`, per-slide scores, threshold, blocking issues, and release decision.
- Validator runs the visual loop as part of `python3 scripts/validate_skill.py`.

## Current Threshold

Phase 4B uses a deliberately permissive threshold of `70`. This is not the final quality bar; it prevents the MVP from failing on font/rendering differences while still catching catastrophic blank/missing render failures.

## Known Limitations

- Reference image is IR/Pillow-rendered, not browser-rendered HTML.
- Text font metrics differ between Pillow and LibreOffice.
- Raster islands remain placeholders until Phase 3 exporter embeds real images.
- The visual score is mean absolute RGB error, not perceptual SSIM.

## Next Upgrade

When Chromium or Playwright is available, add:

```text
HTML preview → browser screenshot → compare with PPTX render
```

Then replace the placeholder `fidelity` score in QA with the measured visual score.
