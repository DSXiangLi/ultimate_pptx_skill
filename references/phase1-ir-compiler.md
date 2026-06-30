# Phase 1: Content Contract to Slide IR Compiler

## Purpose

Prove the first executable step in the IR-first pipeline: a structured content contract can compile into Slide IR with editability policy applied before any HTML or PPTX rendering exists.

## Deliverables

- `examples/content-contract.sample.json`
- `scripts/compile_spec_to_ir.py`
- generated output: `build/phase1-sample.ir.json`

## Acceptance Criteria

- The compiler runs with `python3`.
- The output is valid JSON.
- The output passes `scripts/validate_skill.py` IR policy checks when copied or supplied as validation input in later phases.
- All `title`, `body`, and `risk` objects are `render_policy: native` with `editability.priority: 5`.
- The only raster object is a background `rasterIsland` with source metadata and explicit `must_not_contain` critical roles.

## Command

```bash
python3 scripts/compile_spec_to_ir.py examples/content-contract.sample.json build/phase1-sample.ir.json
python3 scripts/validate_skill.py
```

## Blocking Failures

- Missing slide title.
- Duplicate object IDs.
- Critical text emitted as raster.
- Raster island without source metadata.
- Risk/source note missing when finance scenario requires it.
