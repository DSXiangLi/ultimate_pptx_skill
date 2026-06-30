# Ultimate PPTX Builder Implementation Plan

> **Goal:** Build a validated, IR-first editable PPTX skill that can evolve from documentation to runnable conversion tooling.

## Phase 0 — Skill Skeleton

**Deliverables**

- `SKILL.md`
- `references/*.md`
- `schemas/*.json`
- `examples/minimal-deck.ir.json`
- `scripts/validate_skill.py`

**Acceptance**

- `python3 scripts/validate_skill.py` passes.
- Skill frontmatter is valid.
- Required references exist.
- Schemas/examples parse as JSON.
- Example IR passes core policy checks.

## Phase 1 — IR Compiler MVP

**Deliverables**

- `scripts/compile_spec_to_ir.py`
- `examples/content-contract.sample.json`
- tests for content → IR

**Acceptance**

- Given sample content, compiler emits valid IR.
- Critical content gets priority ≥4.
- No generated critical text is rasterized.

## Phase 2 — HTML Preview Renderer

**Deliverables**

- `scripts/render_ir_html.py`
- template CSS
- traceability report

**Acceptance**

- Every exportable IR object appears as a DOM node with `data-ir-id`.
- Preview renders at 1280×720.
- Traceability report has zero missing IDs.

## Phase 3 — PPTX Export Renderer

**Deliverables**

- `scripts/export_ir_pptx.py`
- native text/shape/image/rasterIsland support
- export report

**Acceptance**

- Example IR exports to `.pptx`.
- Native text objects remain editable.
- Raster island is inserted as image with metadata sidecar.

## Phase 4 — QA Automation

**Deliverables**

- `scripts/render_pptx_png.py`
- `scripts/audit_pptx_editability.py`
- `scripts/compare_preview_pptx.py`
- `qa-report.json`

**Acceptance**

- HTML and PPTX screenshots are produced.
- Editability audit lists every priority ≥4 object.
- QA report validates against schema.

## Phase 5 — Style Program Library

**Deliverables**

- 3 initial PPTX styles: `swiss-grid-pptx`, `glass-fintech-pptx`, `data-news-pptx`
- style compatibility table

**Acceptance**

- Each style has Base DNA and ≥2 SOTA DNA.
- Each style declares PPTX material strategy.
- Each style can generate at least 3 different layout/topology combinations without visual sameness.
