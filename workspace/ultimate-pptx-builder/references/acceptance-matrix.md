# Acceptance Matrix

This matrix is the execution guardrail for Ultimate PPTX Builder. Work advances only when the current phase passes its acceptance gate.

## Global Rule

No phase may claim completion without:

1. an explicit deliverable,
2. an automated or inspectable validation step,
3. defined blocking failures,
4. a recorded pass/fail result.

## Phase Gates

| Phase | Deliverable | Entry Condition | Validation | Exit Condition | Blocking Failures |
|---|---|---|---|---|---|
| 0 Skill Skeleton | `SKILL.md`, references, schemas, examples, validator | Research document exists | `python3 scripts/validate_skill.py` | All checks pass | missing required file, invalid JSON, missing acceptance criteria, invalid IR policy |
| 1 IR Compiler MVP | content contract → Slide IR compiler | Phase 0 pass | compiler emits IR; validator passes on output | sample content produces valid IR | critical content missing, priority rules absent, duplicate IDs |
| 2 HTML Preview | IR → HTML renderer | Phase 1 pass | trace every `data-ir-id` back to IR | preview has zero missing exportable objects | DOM-only critical content, missing traceability, wrong slide size |
| 3 PPTX Export | IR → `.pptx` renderer | Phase 2 pass | export report + editability audit | priority ≥4 text native; raster islands documented | title/body/risk rasterized, missing metadata, non-deterministic z-order |
| 4 QA Automation | screenshots, audits, `qa-report.json`, layout safety report | Phase 3 pass | qa report + `scripts/check_layout_safety.py` | no blocking issue; at least one fix-reverify cycle for real output | fidelity drift, unreadable risk/source, chart/table flattened against policy, bottom overflow, text capacity failure, title/decor collision |
| 5 Style Library | reusable PPTX style programs | Phase 4 pass | style schema + visual rubric + 3 layout variants | each style has Base DNA, ≥2 SOTA DNA, material/degradation rules | average/generic style, no PPTX translation, unsupported density |

## Per-Object Acceptance

| Object Kind | Must Validate | Blocking Failure |
|---|---|---|
| text | native text for priority ≥4 | rasterized critical text |
| chart | data-editable or justified fallback | finance chart screenshot without approval |
| table | editable cells or grouped text/shapes | finance table rasterized |
| rasterIsland | source metadata + critical-role exclusion | contains title/body/risk/source text |
| layout/text safety | safe-zone, footer separation, text-capacity, table-density, and compliance-density report | bottom overflow, footer separation, priority text overflow, title/decor collision, table-density, or compliance-density issue |
| style program | Base DNA + SOTA DNA + PPTX material strategy | generic style label without generative rules |

## Release Gate

A deck is releasable only when all are true:

- Layout/text safety report passes with zero blocking issues.
- Fidelity score ≥90 or accepted exceptions are documented.
- Editability score ≥90 for business-critical objects.
- No compliance/practicality blocker.
- Visual quality average ≥4/5 on key slides.
- Real output has completed a fix-and-reverify cycle.
