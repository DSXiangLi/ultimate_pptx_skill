# Strict Visual and Office Compatibility Validation

## Trigger

User reported that the repaired PPTX still had fine-grained text overlap, chaotic container arrangement, and that opening PPTX still displayed a repair/problem warning.

## Root-cause Classification

| Symptom | Classification | Root Cause | Fix |
|---|---|---|---|
| PowerPoint/WPS reports a problem opening PPTX | T conversion/export compatibility | Previous exporter hand-wrote a minimal OOXML package that passed LibreOffice/python-pptx reading but remained risky for stricter Office/WPS repair logic | Replaced default exporter with `python-pptx` package generation and strengthened `check_pptx_package.py` with relationship resolution + python-pptx roundtrip |
| Fine text collisions / KPI rail conflicts | L local compiler layout + S gate gap | Paper title column and right KPI rail were not enforced as mutually exclusive editorial columns | Narrowed Paper title column; kept KPI rail in a separate right column |
| Atlas looked like unclean helper lines | S style-DNA/gate gap + V visual acceptance gap | Map grid/routes/nodes had too much visual weight; previous visual gate blocked large issues but not decorative hierarchy noise | Added stricter visual-layout checks; lowered grid/route/node opacity; made map nodes semantically distinct from route lines; strengthened content-card isolation |
| Dark Glass decoration/footers felt crowded | S/V | Decorative glow and risk footer were still too close to edge/content hierarchy | Shrunk/faded right glow; moved footer upward |
| Protected Chinese term wrap risk | L compiler text budget | Atlas process card text width allowed a line break inside `风险预算` | Changed Atlas process to wider 2x2 cards and widened text budget |

## Verification Commands

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/check_visual_layout_architecture.py scripts/export_ir_pptx.py scripts/check_pptx_package.py scripts/validate_visual_systems.py
python3 scripts/validate_visual_systems.py
python3 scripts/check_pptx_package.py build/visual-system-glass-fintech-pptx/glass-fintech-pptx.pptx build/visual-system-paper-analyst-report/paper-analyst-report.pptx build/visual-system-market-atlas-infographic/market-atlas-infographic.pptx
```

Observed result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=93.84 edit=100.00; paper-analyst-report score=95.25 edit=100.00; market-atlas-infographic score=94.11 edit=100.00
PASS pptx package: build/visual-system-glass-fintech-pptx/glass-fintech-pptx.pptx
PASS pptx package: build/visual-system-paper-analyst-report/paper-analyst-report.pptx
PASS pptx package: build/visual-system-market-atlas-infographic/market-atlas-infographic.pptx
```

## Visual Review

Final strict visual audit contact sheet:

```text
build/strict-visual-audit-final.png
```

Final visual-review decision: `PASS`. No blocking text overlap, container disorder, or Office package issue remains in the current validation artifacts.

## Prevention Rule

Do not accept PPTX output based on coarse fidelity/editability scores alone. Fine-grained professional acceptance requires:

1. Office-compatible package generation and roundtrip checks.
2. Geometric layout safety.
3. Visual-layout architecture checks for decorative hierarchy, footer safety, chart/text budget, and page-role density.
4. Strict rendered visual review after the automated gates.
