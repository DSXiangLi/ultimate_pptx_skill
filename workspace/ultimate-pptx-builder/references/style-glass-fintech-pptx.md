# Glass Fintech PPTX Style Program

## Purpose

`glass-fintech-pptx` is the first end-to-end style anchor for `ultimate-pptx-builder`. It focuses on one style done deeply rather than many shallow presets.

## Visual Thesis

A finance-grade cockpit: dark institutional canvas, translucent native glass panels, cyan/violet light accents, metric cards, and a persistent native risk rail.

## Programmable Grammar

- Canvas: dark navy full-slide native shape.
- Depth: low-opacity accent orbs behind content, exported as native shapes.
- Glass: translucent rounded rectangles with highlight stroke and subtle shadow.
- Information: metric cards, action rails, source/risk text, and body narrative blocks.
- Constraint: no business-critical content may enter raster.

## PPTX Material Strategy

| Material | PPTX representation | Notes |
|---|---|---|
| Background | native rectangle | not raster in MVP |
| Glow orb | native oval/rect surrogate with opacity | blur simulated, not promised |
| Glass card | native roundRect with opacity + stroke + shadow | editable fill/stroke/position |
| Metric value | native text | priority 5 |
| Risk rail | native shape + native text | priority 5 text |
| Financial chart | editable vector group of native shapes/text | MVP path; not Office chart XML yet, but not raster |

## Acceptance Criteria

- `examples/glass-fintech-pptx.style.json` has Base DNA and at least two SOTA DNA moves.
- `examples/glass-fintech-showcase.contract.json` compiles to at least three slides.
- The compiled IR contains no `rasterIsland` objects for this showcase.
- All title/body/metric/risk text remains native with priority >= 4.
- At least one financial chart remains priority 5 and exports as `editable-vector-chart`.
- HTML preview, PPTX export, visual fidelity report, and QA report are generated.
- Visual fidelity score must be >= 88 for the showcase.
- QA editability score must be >= 95.

## Why One Style First

The goal is to prove a complete generative style line: style program → content contract → IR → HTML → PPTX → visual diff → QA. Only after one style is strong should more styles be added.
