# Glass Fintech Controlled Variants Validation

## Scope

This validation covers the six-step narrative/visual-anchor expansion and the follow-up fix for underpowered visual variants.

## Six-Step Recheck

| Step | Acceptance recheck | Result | Notes |
|---|---|---|---|
| Step 1 Narrative Kernel | `references/narrative-kernel.md`, schema, finance example exist and parse | PASS | Narrative kernel remains available for rule-driven generation. |
| Step 2 Narrative Safety Checker | `scripts/check_narrative_safety.py` runs in benchmark/variants | PASS | Variants and benchmark include narrative safety reports. |
| Step 3 Visual Anchor Schema/System | `references/visual-anchor-system.md`, schema, anchor example exist | PASS | Updated with grammar-level distinctiveness requirements. |
| Step 4 glass-fintech visual anchor | anchor metadata plus `check_visual_anchor.py` gate | PASS | Checker now blocks weak coordinate realization for controlled variants. |
| Step 5 Controlled Variants | 3 new PPTX mini decks exported and rendered | PASS | `sober-committee`, `luminous-strategy`, `dense-risk-review`. |
| Step 6 Main validation integration | `scripts/validate_skill.py` includes showcase, benchmark, variants | PASS | Full validation passes. |

## Issue Found During Recheck

Human review correctly identified that the first controlled variants were visually underpowered: they changed page selection and decoration but not enough visual grammar.

## Fix

- Added `visual_grammar` to compiled IR.
- Made variant profiles control motif, material, metric grammar, chart/table treatment, risk/footer treatment, and density.
- Added visible PPTX roles: `committee-gridline`, `committee-ruler`, `luminous-ribbon`, `spotlight-orb`, `terminal-gridline`, `status-chip`.
- Added grammar realization and cross-variant distance gates.
- Upgraded `check_visual_anchor.py` with `WEAK_COORDINATE_REALIZATION`, `COMPONENT_GRAMMAR_UNCHANGED`, and `VISUAL_VARIANT_DISTANCE_TOO_LOW`.

## Verification Commands

```bash
python3 scripts/validate_glass_variants.py
python3 scripts/validate_skill.py
```

Latest result:

```text
PASS glass variants count=3 sober-committee score=95.96 edit=100.00; luminous-strategy score=95.56 edit=100.00; dense-risk-review score=95.72 edit=100.00
ALL CHECKS PASSED
```

## Rendered Contact Sheets

- `build/glass-fintech-sober-committee/contact-sheet-sober-committee.png`
- `build/glass-fintech-luminous-strategy/contact-sheet-luminous-strategy.png`
- `build/glass-fintech-dense-risk-review/contact-sheet-dense-risk-review.png`

Visual review result: all three are now accepted as same-family but visually distinguishable variants. Remaining non-blocking concerns are small-font readability in dense/table/footer regions and occasional page-to-page layout similarity inside a variant.
