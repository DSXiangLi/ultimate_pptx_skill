# Phase 2: IR to HTML Preview Renderer

## Purpose

Prove that HTML is a traceable preview generated from IR, not the source of truth.

## Deliverables

- `scripts/render_ir_html.py`
- generated output: `build/validation-preview.html`

## Acceptance Criteria

- Renderer runs with `python3`.
- Every IR object in the generated validation deck appears in HTML with `data-ir-id`.
- Every `data-ir-id` in HTML maps back to exactly one IR object.
- HTML preview is fixed at the IR deck size, default 1280×720.
- Critical content does not exist only as CSS pseudo content or decoration.

## Command

```bash
python3 scripts/validate_skill.py
```

The validator compiles the sample contract, renders HTML, and checks traceability.

## Blocking Failures

- Missing `data-ir-id` for any exportable object.
- Extra `data-ir-id` not present in IR.
- Duplicate IDs.
- Renderer treating arbitrary DOM as source.
