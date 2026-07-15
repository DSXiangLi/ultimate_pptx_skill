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
  - C3.1 reconstructs image objects from slide relationship IDs and source package media parts.
  - C3.2 reconstructs solid slide-level backgrounds from `p:cSld/p:bg/p:bgPr` as native slide backgrounds.
  - C3.3 reconstructs picture-fill shapes (`<p:sp>` with `<a:blip>`) as native image material instead of grey native-shape fallbacks.
  - C3.4 recursively emits group children and records child-bearing group containers as structural `expanded-group-container` entries instead of opaque placeholders.
  - C3.5 classifies empty/decorative text containers as metadata and skips materialization instead of drawing diagnostic placeholders.
  - C3.6 reconstructs simple native tables from structured `table_ref` IR as editable PowerPoint tables.
  - C3.7 applies conservative native table styling: solid cell fills, margins, paragraph alignment, and first-run font properties.
  - Materializes charts/unsupported classes as classified placeholders until their object coverage increments land.
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
Ran 7 tests
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
object_count: 234
unsupported_count: 0
unsupported_by_type: none
critical_failures: 0
visual_score: 96.66
native_images: 19
native_slide_backgrounds: 21
expanded_group_containers: 16
skipped_empty_text_containers: 11
native_tables: 0
objects_with_group_id: 69
```

Latest C3.7 visual comparison board:

```text
verification/cloner-visual-compare/dark-minimalist-business-c3-7-triptych.png
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
object_count: 314
unsupported_count: 0
unsupported_by_type: none
critical_failures: 0
visual_score: 88.65
native_images: 8
native_slide_backgrounds: 14
native_picture_fill_shape_images: 24
expanded_group_containers: 64
skipped_empty_text_containers: 37
native_tables: 1
styled_table_cells: 18
objects_with_group_id: 139
```

Latest C3.7 visual comparison board:

```text
verification/cloner-visual-compare/it-software-sales-proposal-slides-c3-7-triptych.png
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
- charts and fully styled tables are reconstructed;
- layout/component archetypes are ready for promotion;
- a reusable template generator exists.

The remaining fidelity gaps are now much more specific. C3.1 proves media relationship recovery works: image objects are now native picture objects, not placeholders. C3.2 proves slide-level solid background recovery works: dark/colored templates no longer collapse to white. C3.3 proves picture-fill shapes can be recovered from `<p:sp>`/`<a:blip>` material instead of becoming grey rectangles. C3.4 proves groups can be opened into traceable child objects instead of opaque placeholders. C3.5 proves empty/decorative text containers can be classified as metadata and skipped. C3.6 proves simple native tables can be rebuilt as editable PowerPoint tables. C3.7 proves conservative table styling can be extracted and applied, but the slight `it-software` score dip shows that border/gradient/theme support must follow; partial native styling is diagnostic progress, not final visual acceptance. Remaining visual misses are concentrated in table borders/gradients/theme styling, shape styling details, gradients/theme references, crop/mask/effect fidelity, and chart support.

## Next Optimization Loop

Before treating C4/C5/C6 promotions as strong evidence, improve C3 fidelity by reducing unsupported placeholders:

1. Improve shape/table geometry, fill, stroke, border, typography, and alignment extraction beyond default native objects.
2. Add crop/mask support for native images where source `a:srcRect`, transparency, or shape masks affect fidelity.
3. Add chart classification gates and first native/vector chart reconstruction for decks with chart objects.
4. Extend background reconstruction from solid RGB to theme references, gradients, image backgrounds, and layout/master inheritance.
5. Make visual fidelity threshold gradually blocking once native visual-property coverage is strong enough to make the threshold fair.

The acceptance loop should continue to treat package/text/render failures as blocking. Visual score remains a recorded baseline until C3 has enough native object-class coverage to make a threshold fair.
