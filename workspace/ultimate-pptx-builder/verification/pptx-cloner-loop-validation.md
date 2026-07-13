# PPTX Cloner Acceptance Loop Validation

Date: 2026-07-14

## Scope

Implemented the first executable acceptance loop for the PPTX cloner / template abstraction workflow.

This loop is intentionally scoped to the current implemented reverse-compiler slice:

```text
C1 specimen analyzer
→ C2 raw IR decompiler
→ machine-readable gate report
→ optimization_queue for blockers
```

It does **not** claim that C3 diagnostic rebuild, C4 archetype mining, C5 visual DNA extraction, C6 component contracts, or C7 reusable generator are already implemented. Those phases must plug into the same report contract before they can be treated as accepted.

## Implemented Files

- `scripts/run_pptx_cloner_loop.py`
  - Runs specimen analysis and raw IR decompilation.
  - Evaluates C1/C2 gates.
  - Writes `cloner-loop-report.json` with `release_decision`, `blocking_count`, `gates`, `optimization_queue`, `next_phase_allowed`, and `next_phase`.
  - Repeats up to `--max-iterations`, but declares stalled when the same blockers repeat without an engineering change.

- `tests/test_pptx_cloner_loop.py`
  - Verifies the loop passes on a simple generated PPTX.
  - Verifies missing IR produces a failing report with actionable optimization ownership.

- `references/pptx-cloner.md`
  - Adds the acceptance loop principle: fail → diagnose → optimize → rerun.
  - Defines current C1/C2 passing conditions and future C3–C8 plug-in points.

- `SKILL.md`
  - Adds the loop command under Step 2F.
  - Blocks advancement when the current cloner phase report is not `release_decision: pass`.

## Unit Test Verification

```bash
python3 -m unittest \
  tests.test_pptx_specimen_analyzer \
  tests.test_pptx_to_ir_decompiler \
  tests.test_pptx_cloner_loop \
  -v
```

Result:

```text
Ran 5 tests in 3.995s
OK
```

## Real Template Verification

### dark-minimalist-business

Command:

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/dark-minimalist-business.pptx \
  --deck-id dark-minimalist-business \
  --out specimens/dark-minimalist-business \
  --require-render \
  --max-iterations 3
```

Result:

```json
{
  "release_decision": "pass",
  "blocking_count": 0,
  "report": "specimens/dark-minimalist-business/cloner-loop-report.json",
  "next_phase_allowed": true,
  "next_phase": "C3 diagnostic rebuild fidelity"
}
```

### it-software-sales-proposal-slides

Command:

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/it-software-sales-proposal-slides.pptx \
  --deck-id it-software-sales-proposal-slides \
  --out specimens/it-software-sales-proposal-slides \
  --require-render \
  --max-iterations 3
```

Result:

```json
{
  "release_decision": "pass",
  "blocking_count": 0,
  "report": "specimens/it-software-sales-proposal-slides/cloner-loop-report.json",
  "next_phase_allowed": true,
  "next_phase": "C3 diagnostic rebuild fidelity"
}
```

## Current Gate Boundary

Current pass means:

- evidence pack files exist;
- source package unpacks to slide XML;
- renders/contact sheet exist when required;
- raw IR exists;
- slide recall is 100%;
- object recall is 100%;
- text recall is 100%;
- IR object contract fields exist;
- text-bearing objects are marked native/editable priority >= 4.

It does **not** yet mean:

- rebuilt PPTX package passes strict Office gate;
- rebuilt render matches source render;
- reusable template generator exists;
- visual DNA/component contracts have been promoted.

## Next Required Iteration

Implement C3 as the next loop stage:

```text
decompiled.raw.ir.json
→ rebuilt.pptx
→ check_pptx_package.py
→ text/object recall against source
→ render original + rebuilt
→ visual diff report
→ cloner-loop-report.json updated with C3 gates
```

C3 should become blocking before any C4–C7 template abstraction is accepted.
