# Market Atlas Layout Grammar Validation

## Scope

This record covers the Market Atlas layout-grammar hardening pass after rendered review showed that a technically passing deck could still have institution-level layout weaknesses.

## New Blocking Gate Coverage

Added to `scripts/check_visual_layout_architecture.py`:

- `ATLAS_TITLE_ZONE_OVERWEIGHT`
- `ATLAS_TITLE_ZONE_MASK_INTRUSION`
- `ATLAS_RIGHT_PANEL_FLOATING`
- `ATLAS_FOOTER_DOMINANCE`
- `ATLAS_DENSITY_PARITY_FAILURE`

The RED run on the previous Atlas IR produced 19 blocking issues, including title-zone overweight, title/content-mask intrusion, right-panel drift, footer dominance, and business microtext density failures.

## Compiler Changes

Updated `scripts/compile_spec_to_ir.py` for `market-atlas-infographic`:

- light header band with title/subtitle ending by the gate threshold;
- content masks moved below the title band;
- right decision/signal rail anchored to a stable x-grid;
- footer rail weakened and shortened;
- Atlas semantic business text raised out of 6–7px microtype;
- macro decision matrix enlarged instead of shrinking text;
- process state-machine page moved upward for better slide-05 visual balance.

## Verification

Workspace validation passed:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=94.95 edit=100.00; paper-analyst-report score=95.46 edit=100.00; market-atlas-infographic score=95.78 edit=100.00
PASS required files: 73 present
...
ALL CHECKS PASSED
```

Manual rendered review artifact:

```text
build/visual-system-market-atlas-infographic/market-atlas-infographic-actual-contact-sheet-grammar-final.png
```

Rendered contact-sheet review found no blocker/major after the final pass. Remaining right-side density is minor/acceptable.
