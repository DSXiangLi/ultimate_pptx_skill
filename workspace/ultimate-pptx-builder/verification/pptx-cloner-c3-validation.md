# PPTX Cloner C3 Diagnostic Rebuild Validation

Date: 2026-07-14

## Scope

Implemented the first C3 diagnostic rebuild baseline and plugged it into the existing cloner acceptance loop.

The C3 baseline is intentionally honest:

```text
decompiled.raw.ir.json
→ rebuilt.pptx
→ strict Office package check
→ rebuilt slide/text recall
→ rebuilt render baseline
→ source-vs-rebuilt visual diff report
```

This does **not** mean high-fidelity visual cloning is solved. C3 now proves that the system can regenerate a strict, editable, renderable PPTX with 100% critical text recall; visual fidelity upgrades remain the next optimization loop.

## Implemented Files

- `scripts/rebuild_decompiled_ir_pptx.py`
  - Rebuilds raw decompiled IR into `rebuilt.pptx`.
  - Preserves slide count and source slide size.
  - Rebuilds text-bearing objects as native editable text boxes.
  - Rebuilds simple non-text shapes as native PPTX shapes.
  - Materializes images/groups/charts/tables/unsupported classes as classified placeholders in the first baseline.
  - Writes `rebuild-report.json` with unsupported object classifications and critical text failures.

- `scripts/run_pptx_cloner_loop.py`
  - Runs C3 automatically after C1/C2 pass.
  - Adds C3 gates:
    - `C3-REBUILD-PPTX`
    - `C3-STRICT-PACKAGE`
    - `C3-REBUILT-SLIDE-RECALL`
    - `C3-REBUILT-TEXT-RECALL`
    - `C3-REBUILT-RENDER-BASELINE`
  - Merges C1/C2/C3 into one loop report.
  - Advances to `C4 template archetype mining` only after C3 baseline passes.

- `tests/test_pptx_cloner_loop.py`
  - Updated to assert C3 artifacts and gates.

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
Ran 5 tests in 2.219s
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
  "next_phase": "C4 template archetype mining"
}
```

C3 details:

```text
object_count: 165
unsupported_count: 35
critical_failures: 0
visual_score: 23.34
```

C3 gates:

```text
C3-REBUILD-PPTX: pass
C3-STRICT-PACKAGE: pass
C3-REBUILT-SLIDE-RECALL: pass
C3-REBUILT-TEXT-RECALL: pass
C3-REBUILT-RENDER-BASELINE: pass
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
  "next_phase": "C4 template archetype mining"
}
```

C3 details:

```text
object_count: 175
unsupported_count: 58
critical_failures: 0
visual_score: 32.62
```

C3 gates:

```text
C3-REBUILD-PPTX: pass
C3-STRICT-PACKAGE: pass
C3-REBUILT-SLIDE-RECALL: pass
C3-REBUILT-TEXT-RECALL: pass
C3-REBUILT-RENDER-BASELINE: pass
```

## Interpretation

Current C3 pass means:

- rebuilt diagnostic PPTX exists;
- rebuilt PPTX passes strict Office package validation;
- rebuilt PPTX renders through LibreOffice/pdftoppm;
- slide count recall is 100%;
- native text recall is 100%;
- critical text failures are zero;
- visual diff reports are produced.

Current C3 pass does **not** mean:

- high visual fidelity is achieved;
- images are restored natively;
- groups/charts/tables are reconstructed;
- layout/component archetypes are ready for promotion;
- a reusable template generator exists.

The low visual scores are expected for the first baseline because unsupported object classes are intentionally classified as placeholders rather than silently dropped.

## Next Optimization Loop

Before treating C4/C5/C6 promotions as strong evidence, improve C3 fidelity by reducing unsupported placeholders:

1. Resolve image relationships from slide rels/object inventory and rebuild source images with correct crop/box where possible.
2. Improve shape geometry/fill/stroke extraction beyond rectangle placeholders.
3. Classify and flatten groups with child object recovery instead of one placeholder.
4. Add chart/table classification gates that distinguish native reconstruction vs placeholder fallback.
5. Make visual fidelity threshold gradually blocking once unsupported image/group classes are materially reduced.

The acceptance loop should continue to treat package/text/render failures as blocking. Visual score remains a recorded baseline until C3 has enough native object-class coverage to make a threshold fair.
