# Component Layout Contract Gate Validation

## Purpose

Validate whether container-level layout defects in Market Atlas pages can be detected deterministically instead of relying only on full-size visual-model review.

The immediate regression target is the latest Atlas rebuild where page2/page3 visibly contain container grammar defects:

- page2: route-map bottom band intrudes into node cards; NOW badge covers the CONFIRM card body.
- page3: guardrail note is orphaned outside the route-map panel and too close to the footer/risk rail.

## Implemented Gate

Script:

```text
scripts/check_component_layout_contract.py
```

Regression tests:

```text
tests/test_component_layout_contract.py
```

Validated blocker codes:

```text
ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION
ATLAS_FLOATING_BADGE_COVERS_CARD
ATLAS_GUARDRAIL_TEXT_ORPHANED
ATLAS_FOOTER_GUARDRAIL_COLLISION
```

## TDD Evidence

Initial RED state:

```text
python3 -m unittest tests/test_component_layout_contract.py -v
```

Failed because `scripts/check_component_layout_contract.py` did not exist. This proved the test was covering a missing capability rather than existing behavior.

After implementation:

```text
python3 -m unittest tests/test_component_layout_contract.py -v
```

Result:

```text
Ran 3 tests ... OK
```

## Current Atlas Red-Light Report

Command:

```bash
python3 scripts/check_component_layout_contract.py \
  release/latest-atlas/market-atlas-infographic.ir.json \
  --report verification/atlas-component-layout-contract-current-fail-report.json
```

Expected result for the current known-bad Atlas output:

```text
release_decision: fail
blocking_count: 4
```

Detected issues:

```text
ls02 ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION
ls02 ATLAS_FLOATING_BADGE_COVERS_CARD
ls03 ATLAS_GUARDRAIL_TEXT_ORPHANED
ls03 ATLAS_FOOTER_GUARDRAIL_COLLISION
```

This confirms the page2/page3 defects are now machine-detectable from IR geometry and component semantics.

## False Positive Check

The gate was also run against Glass and Paper visual-system IRs:

```text
glass-fintech-pptx: pass, blocking_count=0
paper-analyst-report: pass, blocking_count=0
latest-atlas: fail, blocking_count=4
```

A first implementation incorrectly flagged a Glass metric delta containing “偏离” as an Atlas guardrail. The rule was tightened so guardrail/footer checks only apply when a route-map panel exists and the note is spatially near the route-map bottom.

## Skill Validation

`validate_skill.py` now includes:

- required file check for `scripts/check_component_layout_contract.py`
- required test check for `tests/test_component_layout_contract.py`
- `PASS component layout contract regression tests`

Workspace validation command:

```bash
python3 scripts/validate_skill.py
```

Result:

```text
ALL CHECKS PASSED
```

## Release Gate Status

The new component layout contract is intentionally not yet wired into `validate_visual_systems.py` release validation, because the current Atlas output is known-bad and should fail this gate. The correct next step is:

1. fix Atlas page2/page3 generator layout;
2. rerun `check_component_layout_contract.py` until Atlas passes;
3. then promote `check_component_layout_contract.py` into `validate_visual_systems.py` as a formal release gate.

This avoids falsely declaring the current Atlas PPTX as release-ready while still preserving the deterministic regression capability.

## 2026-07-09 Generator Fix Validation

After hardening `scripts/compile_spec_to_ir.py`, the same component gate was rerun on the regenerated Market Atlas IR:

```bash
python3 scripts/validate_visual_systems.py
python3 scripts/check_component_layout_contract.py \
  build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json \
  --report verification/atlas-component-layout-contract-fixed-report.json
```

Result:

```text
PASS component layout contract
release_decision=pass
blocking_count=0
issues=[]
```

The previous deterministic blockers are fixed in generated IR, not waived:

- `ls02 ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION`
- `ls02 ATLAS_FLOATING_BADGE_COVERS_CARD`
- `ls03 ATLAS_GUARDRAIL_TEXT_ORPHANED`
- `ls03 ATLAS_FOOTER_GUARDRAIL_COLLISION`

`validate_visual_systems.py` now runs `check_component_layout_contract.py` as a formal release gate after text spacing/alignment graph and before visual layout architecture. Full-size rendered review of page2/page3 found no blocker/major container overlap; remaining notes are minor density/spacing polish.

