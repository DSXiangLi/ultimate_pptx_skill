# Visual-System Generalization Validation

## Scope

Validates that the PPTX builder is not overfit to a single dark-glass finance style. The same content contract and same `narrative_intent=strategy_update` are compiled through three full style anchors:

- `glass-fintech-pptx`
- `paper-analyst-report`
- `market-atlas-infographic`

## Commands

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/validate_visual_systems.py
python3 scripts/validate_visual_systems.py
```

Latest observed result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=96.15 edit=100.00; paper-analyst-report score=96.58 edit=100.00; market-atlas-infographic score=96.74 edit=100.00
```

## Artifacts

- `build/visual-system-glass-fintech-pptx/glass-fintech-pptx.pptx`
- `build/visual-system-paper-analyst-report/paper-analyst-report.pptx`
- `build/visual-system-market-atlas-infographic/market-atlas-infographic.pptx`
- `build/visual-system-same-content-comparison.png`
- `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-05.png`

## Visual Review

- The three visual systems are first-glance distinct: dark glass dashboard, warm paper analyst report, and market atlas/data-map infographic.
- Differences cover surface, material, container grammar, layout rhythm, and information organization, not just color.
- A full-size review initially found overlap on Market Atlas Slide 05 between a right-side metric tile and the fourth process card.
- The process-page metric tile positions were adjusted and full-size review confirmed no blocking overlap remains.
- The contact sheet label column was widened and labels wrapped so `Market Atlas Infographic` displays fully.

## Decision

Accepted as the first multi-visual-system generalization proof, with the caveat that future visual systems must include both automated validation and at least one full-size rendered-page review for their densest page.
