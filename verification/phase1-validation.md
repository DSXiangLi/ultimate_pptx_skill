# Phase 1 Validation Record

## Scope

Validate the minimal content contract → Slide IR compiler.

## Deliverables

- `examples/content-contract.sample.json`
- `scripts/compile_spec_to_ir.py`
- `references/phase1-ir-compiler.md`
- validator-generated output: `build/validation-phase1.ir.json`

## Command

```bash
cd /home/lixiang/workspace/ultimate-pptx-builder
python3 scripts/validate_skill.py
```

## Result

```text
PASS required files: 21 present
PASS skill frontmatter
PASS acceptance criteria present
PASS JSON parseability
PASS minimal IR policy
PASS style policy
PASS Phase 1 compiler output
ALL CHECKS PASSED
```

## Acceptance Evidence

- The validator automatically runs `scripts/compile_spec_to_ir.py`.
- The compiler output is parsed as JSON.
- The generated IR is checked with the same editability policy as the static minimal example.
- Critical roles (`title`, `body`, `risk`, `source`, `footnote`) must have priority ≥4 and cannot be rasterized.
- `rasterIsland` must contain source metadata and declare `must_not_contain` critical roles.

## Phase 1 Decision

Status: **PASS**

Phase 2 may begin only while `python3 scripts/validate_skill.py` remains green.
