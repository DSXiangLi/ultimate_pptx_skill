# OOXML + Rendered Perceptual QA Validation

Date: 2026-07-10

## Scope

Phase C adds two deterministic gates:

1. `check_ooxml_visual_properties.py` — verifies exported PPTX XML preserves native visual properties and critical native text evidence.
2. `check_rendered_perceptual_layout.py` — inspects rendered slide PNGs for real edge/bottom pressure after PowerPoint/LibreOffice rendering.

## Files

- `scripts/check_ooxml_visual_properties.py`
- `scripts/check_rendered_perceptual_layout.py`
- `tests/test_ooxml_and_rendered_qa.py`
- `references/ooxml-and-rendered-perceptual-qa.md`
- `scripts/validate_visual_systems.py`
- `scripts/validate_skill.py`
- `SKILL.md`

## RED

Initial test run failed because both scripts were absent:

```text
check_ooxml_visual_properties.py missing
check_rendered_perceptual_layout.py missing
```

## GREEN: unit regression

Command:

```bash
python3 -m unittest tests/test_ooxml_and_rendered_qa.py -v
```

Result:

```text
Ran 3 tests
OK
```

Coverage:

- synthetic missing-alpha PPTX fails with `PPTX_ALPHA_MISSING`;
- synthetic bottom-edge pressure PNG fails with `RENDERED_BOTTOM_EDGE_PRESSURE`;
- synthetic safe PNG passes.

## Real-system validation

Command:

```bash
python3 scripts/validate_visual_systems.py
```

Result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=94.95 edit=100.00; paper-analyst-report score=95.46 edit=100.00; market-atlas-infographic score=95.65 edit=100.00
```

Manual C-gate check during implementation:

```text
Glass: OOXML pass; rendered perceptual pass with side-edge warnings only
Paper: OOXML pass; rendered perceptual pass with zero warnings
Atlas: OOXML pass; rendered perceptual pass with side-edge warnings only
```

## Full skill validation

Command:

```bash
python3 scripts/validate_skill.py
```

Result includes:

```text
PASS OOXML/rendered perceptual QA regression tests
ALL CHECKS PASSED
```

## Fixes during implementation

- XML text matching initially false-positive failed on strings like `PMI>50` because PPTX OOXML escapes them as `PMI&gt;50`. The audit now uses HTML entity unescape and whitespace normalization.
- Rendered bottom pressure initially false-positive failed on full-canvas antialiasing/background pixels. The blocker now requires both insufficient bottom gap and meaningful bottom-band density (`>0.03`).

## Release decision

Accepted for workspace. Next phase: finance PPTX benchmark corpus.
