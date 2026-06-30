# Glass Fintech Visual-Language Validation

## Scope

This validation covers the six-step narrative/visual-anchor expansion, the fix for underpowered visual variants, and the later correction that visual-language proof must be independent from narrative/business scenario differences.

## Six-Step Recheck

| Step | Acceptance recheck | Result | Notes |
|---|---|---|---|
| Step 1 Narrative Kernel | `references/narrative-kernel.md`, schema, finance example exist and parse | PASS | Narrative kernel remains independent from visual style. |
| Step 2 Narrative Safety Checker | `scripts/check_narrative_safety.py` runs in benchmark and visual-language validation | PASS | Same-content visual-language runs keep one `narrative_intent=strategy_update`. |
| Step 3 Visual Anchor Schema/System | `references/visual-anchor-system.md`, schema, anchor example exist | PASS | Updated with `controlled_visual_languages` and orthogonality rules. |
| Step 4 glass-fintech visual anchor | anchor metadata plus `check_visual_anchor.py` gate | PASS | Checker blocks weak coordinate realization for controlled visual languages. |
| Step 5 Controlled Visual Languages | same-content mini deck exported/rendered under 3 visual languages | PASS | `matte-institutional`, `luminous-glass`, `terminal-cockpit`. |
| Step 6 Main validation integration | `scripts/validate_skill.py` includes showcase, benchmark, orthogonality, and same-content visual-language validation | PASS | Full validation passes. |

## Issues Found During Recheck

1. Human review identified that the first controlled variants were visually underpowered: they changed page selection and decoration but not enough visual grammar.
2. A later review identified a deeper architecture error: `sober-committee`, `luminous-strategy`, and `dense-risk-review` coupled visual style with narrative/business scenario.
3. Even after adding `visual_language` and `narrative_intent` fields, validation was still contaminated because each visual language used a different contract/narrative skeleton.

## Fix

- Replaced scenario-style visual variant naming with pure visual-language naming:
  - `matte-institutional`
  - `luminous-glass`
  - `terminal-cockpit`
- Added `narrative_intent` as a separate contract field.
- Added `examples/variants/glass-fintech-visual-language-base.contract.json` as the same-content proof base.
- Reworked `scripts/validate_glass_variants.py` so visual-language proof holds slides/content/native-text fingerprints and `narrative_intent` fixed, changing only `visual_language` and visual coordinates.
- Added `scripts/check_narrative_visual_orthogonality.py` to block `VISUAL_NARRATIVE_COUPLING` and legacy `visual_variant` usage.
- Strengthened component-level grammar in `scripts/compile_spec_to_ir.py`, especially for `terminal-cockpit`: terminal status bar, NODE page label, rectangular status chips, stronger grid/rail treatment, and profile-driven panel palette.

## Verification Commands

```bash
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
python3 scripts/validate_skill.py
```

Latest result:

```text
PASS narrative/visual orthogonality visual_languages=3 narrative_intents=3
PASS glass visual languages same_content=1 count=3 matte-institutional score=96.15 edit=100.00; luminous-glass score=95.55 edit=100.00; terminal-cockpit score=95.79 edit=100.00
ALL CHECKS PASSED
```

## Rendered Contact Sheets

- `build/glass-fintech-matte-institutional/contact-sheet-matte-institutional.png`
- `build/glass-fintech-luminous-glass/contact-sheet-luminous-glass.png`
- `build/glass-fintech-terminal-cockpit/contact-sheet-terminal-cockpit.png`
- `build/visual-language-same-content-comparison.png`

Visual review result: same-content comparison is valid. The three rows share the same five-slide strategy-update narrative, so differences mainly come from visual language. `luminous-glass` is strongest; `terminal-cockpit` is now visibly distinct from `matte-institutional` through HUD/grid/status treatment, though future work can further differentiate composition grammar, typography, and chart semantics.

## Remaining Non-Blocking Risks

- `terminal-cockpit` is improved but still shares the same underlying slide geometry with `matte-institutional`; future versions should vary composition grammar, not only component styling.
- `luminous-glass` has strong identity but large translucent blobs can create visual pressure near content.
- All three same-content decks retain the same information density, so contact-sheet thumbnails still have small-text readability limits.
