# OOXML Property Audit + Rendered Perceptual QA

## Purpose

Phase C adds two QA gates for defects that pure IR checks cannot reliably catch:

1. **OOXML visual property audit** — verifies that PPTX materialization actually preserved important native visual properties and critical native text in slide XML.
2. **Rendered perceptual layout QA** — inspects rendered slide PNGs to catch real bottom/edge pressure after Office/LibreOffice rendering.

These gates sit after the compiler/export pipeline:

```text
IR → PPTX export → OOXML property audit → PPTX render → visual fidelity → rendered perceptual QA
```

## Gate 1: OOXML visual properties

Script:

```bash
python3 scripts/check_ooxml_visual_properties.py <deck.ir.json> <deck.pptx> --report <ooxml-report.json>
```

Blocking examples:

- `PPTX_ALPHA_MISSING` — IR contains translucent native/vector objects but slide XML lacks matching `<a:alpha>` evidence.
- `PPTX_CRITICAL_TEXT_XML_MISSING` — priority native text is absent from slide XML.
- `PPTX_OOXML_AUDIT_ERROR` — PPTX package cannot be inspected.

The text check unescapes XML entities and normalizes whitespace, because finance text such as `PMI>50` appears as `PMI&gt;50` in OOXML.

## Gate 2: Rendered perceptual layout

Script:

```bash
python3 scripts/check_rendered_perceptual_layout.py <visual-fidelity/actual> --report <rendered-perceptual-report.json>
```

It uses dependency-free PNG parsing and foreground estimation against corner background color.

Blocking examples:

- `RENDERED_ACTUAL_IMAGES_MISSING` — no rendered slide PNGs exist.
- `RENDERED_PNG_ANALYSIS_ERROR` — PNG cannot be parsed.
- `RENDERED_BOTTOM_EDGE_PRESSURE` — meaningful foreground density reaches the bottom safe band.

Warnings:

- `RENDERED_SIDE_EDGE_PRESSURE` — foreground is close to horizontal edges.
- `RENDERED_BOTTOM_DENSITY_HEAVY` — bottom band is visually dense, but not enough to block alone.

The bottom-edge blocker requires both:

```text
bottom gap below required safe pixels
AND bottom safe band density > 0.03
```

This avoids false positives from full-canvas antialiasing, subtle background gradients, or one-pixel decorative edges.

## Pipeline integration

`validate_visual_systems.py` now runs both gates for every visual system:

```text
export_ir_pptx.py
check_ooxml_visual_properties.py
check_pptx_package.py
run_visual_fidelity.py
check_rendered_perceptual_layout.py
run_qa.py
```

## Acceptance

```bash
python3 -m unittest tests/test_ooxml_and_rendered_qa.py -v
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Expected:

- synthetic missing-alpha PPTX fails with `PPTX_ALPHA_MISSING`;
- synthetic bottom-pressure PNG fails with `RENDERED_BOTTOM_EDGE_PRESSURE`;
- synthetic safe PNG passes;
- real Glass/Paper/Atlas builds pass with zero blockers.

## Boundary

This gate is not a substitute for full visual review. It is a deterministic watchdog for common conversion/rendering failures. Human/vision review remains necessary for taste, hierarchy, semantic clarity, and subtle density issues.
