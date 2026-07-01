# Layout Architecture Diagnosis Validation

## Purpose

Validate the principle that generated PPTX defects are architecture diagnostics, not only local slide polish tasks.

## Initial Diagnosis

The three hardened visual systems passed geometric layout safety, but visual review found classes of failures that the old gate could not block:

| System | Slide | Symptom | Class | Root cause |
|---|---|---|---|---|
| glass-fintech-pptx | ls02 | chart area too small for readable editable labels | C systemic gate gap | geometric safety checked outer boxes, not chart readability budget |
| market-atlas-infographic | ls01-ls05 | decorative route entered title safe area | B style-DNA adaptation bug | fixed atlas route DNA did not adapt to title zone |
| market-atlas-infographic | ls05 | process page had too many route/card layers | C systemic gate gap | no process-page content budget / route complexity gate |

## Skill Upgrade

Added:

```text
references/layout-defect-taxonomy.md
scripts/check_visual_layout_architecture.py
```

The new gate blocks:

- route/title safe-area intrusion;
- editable chart area below readable threshold;
- process pages with too many process/card objects;
- atlas process route complexity overload;
- microtext role warnings.

`validate_visual_systems.py` now runs this gate after geometric layout safety and before export/render/QA.

## Repair From Upgraded Skill

Repairs were made at compiler grammar level:

- enlarged Glass dashboard chart slot;
- moved Atlas decorative routes below title safe zones;
- suppressed global decorative routes on process pages;
- demoted Atlas process metrics from full map tiles to compact native signal chips;
- enlarged Atlas process cards and text budget;
- reduced Atlas process-page grid opacity.

## Verification Commands

```bash
python3 -m py_compile   scripts/compile_spec_to_ir.py   scripts/check_visual_layout_architecture.py   scripts/validate_visual_systems.py   scripts/validate_skill.py
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

## Result

Cross-visual-system validation passed under the upgraded gates:

```text
PASS visual systems same_content=1 count=3
```

Full-size visual review of Market Atlas slide 05 returned PASS:

- process sequence is clear;
- process body text is readable;
- bottom safe area is improved;
- no blocking overlap, clipping, or overflow remains;
- remaining issues are local polish, not systemic architecture defects.

## Acceptance Criteria

- [x] Current layout problem is classified before repair.
- [x] A systemic/gate issue fails a new executable gate before repair.
- [x] Compiler/layout grammar is fixed instead of only local coordinates.
- [x] Repaired output passes geometric layout safety and visual-layout architecture gates.
- [x] Full-size rendered slide review confirms no blocking visual defect remains.
