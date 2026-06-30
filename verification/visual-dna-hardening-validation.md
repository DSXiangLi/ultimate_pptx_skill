# Visual DNA Hardening Validation

## Scope

This validation records the hardening pass after the user rejected first-glance-only visual-system differences. The goal was to prove that three visual systems differ in information-bearing DNA, not only background/skin.

## Systems

- `glass-fintech-pptx`
- `paper-analyst-report`
- `market-atlas-infographic`

## Hardened DNA layers

- Chart palette and chart treatment are now system-specific.
- Typography roles are system-specific for title/body/metric/caption.
- Metric cards and containers have system-specific shape/opacity/stroke/node treatments.
- `paper-analyst-report` adds research memo evidence language: institutional header, exhibit labels, analyst note, scenario assumption table, execution checklist.
- `market-atlas-infographic` adds route/node page structure and reduced background noise.
- `glass-fintech-pptx` improves terminal/dashboard contrast and chart signal palette.

## Automated validation

Latest validated command:

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/render_ir_html.py scripts/export_ir_pptx.py scripts/validate_visual_systems.py
python3 scripts/validate_visual_systems.py
```

Observed result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=95.50 edit=100.00; paper-analyst-report score=95.88 edit=100.00; market-atlas-infographic score=96.63 edit=100.00
```

## Visual review

Rendered contact sheet:

```text
build/visual-system-hardened-dna-comparison.png
```

Final visual review verdict: `PASS`.

Review conclusions:

- The systems are no longer simple background/color swaps.
- Differences are visible in chart palette, typography rhythm, card/container grammar, component structure, and layout skeleton.
- `paper-analyst-report` now reads as an institutional research memo / analyst report rather than only a beige template.
- `market-atlas-infographic` route/grid language is present but not blocking readability.
- `glass-fintech-pptx` has no blocking low-contrast issue; remaining microtext risk is non-blocking.
- No blocking overlap, clipping, or overflow was observed.

## Remaining non-blocking improvements

- Dark Glass can still brighten microtext and axis labels.
- Market Atlas can reduce route/grid opacity another 5-10% on dense pages.
- Paper Analyst can continue adding methodology/source/section-label details for deeper institutional flavor.
