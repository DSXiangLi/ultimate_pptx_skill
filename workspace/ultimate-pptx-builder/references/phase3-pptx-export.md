# Phase 3: IR to PPTX Export MVP

## Purpose

Prove that the IR can produce an actual `.pptx` file with native editable PowerPoint text and shapes without relying on HTML as the source of truth.

## MVP Scope

Supported now:

- native editable text boxes
- native editable simple shapes
- deterministic z-order
- export report for editability audit
- dependency-free OOXML package generation

Explicitly not solved yet:

- high-fidelity raster image embedding
- native editable charts/tables
- full theme/master/layout support
- visual screenshot comparison

`rasterIsland` objects are exported as replaceable placeholder shapes in this MVP, with source metadata retained in the export report. This is intentionally honest degradation, not a claim of full fidelity.

## Deliverables

- `scripts/export_ir_pptx.py`
- generated output: `build/validation-deck.pptx`
- generated report: `build/validation-export-report.json`

## Acceptance Criteria

- Exporter runs with `python3` and no third-party dependencies.
- Output is a valid zip/OPC-style `.pptx` package with presentation and slide parts.
- Priority ≥4 text appears as native PowerPoint text (`<a:t>...</a:t>`), not as a picture.
- Export report audits every IR object.
- No critical role (`title`, `body`, `risk`, `source`, `footnote`) fails editability audit.
- Raster islands are non-critical and documented as placeholders until image embedding is implemented.

## Command

```bash
python3 scripts/validate_skill.py
```

The validator compiles IR, renders HTML preview, exports PPTX, inspects the OOXML package, and checks the export report.

## Blocking Failures

- PPTX file not created or not a zip package.
- Missing `ppt/presentation.xml` or slide XML.
- Critical text missing from slide XML text runs.
- Export report has blocking critical editability failures.
- A critical object is rasterized or unsupported.
