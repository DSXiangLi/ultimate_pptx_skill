# Phase 4: QA Report MVP

## Purpose

Turn the acceptance philosophy into a machine-readable `qa-report.json` so the system can iterate rather than rely on taste-only judgment.

## Current Scope

Supported now:

- aggregate export editability audit
- score editability for critical objects
- score design using structural heuristics
- score practicality using source/risk presence, font sizes, and file size
- consume Phase 4B visual fidelity report when available
- output report matching `schemas/qa-report.schema.json`

Explicitly not solved yet:

- browser-rendered HTML screenshot comparison
- AI visual critique from rendered slide images
- automatic issue fixing

## Deliverables

- `scripts/run_qa.py`
- generated output: `build/validation-qa-report.json`
- optional input: `build/validation-visual-fidelity-report.json`

## Acceptance Criteria

- QA script runs with `python3` and no third-party dependencies.
- Report includes `deck_id`, `scores`, `blocking_issues`, `objects_audited`, and `release_decision`.
- Scores include `fidelity`, `editability`, `design`, and `practicality`.
- When a visual report exists, `scores.fidelity` must equal Phase 4B `visual_fidelity.overall_score`.
- Critical editability failures become blocking issues.
- Finance practicality blockers become blocking issues.
- MVP limitations are explicitly recorded in `notes`.

## Command

```bash
python3 scripts/validate_skill.py
```

## Blocking Failures

- Missing required QA report fields.
- Score outside 0-100.
- Release decision is `pass` while blocking issues exist.
- Critical object audit missing.
- Visual report exists but QA does not include `visual_fidelity`.
- Visual report exists but fidelity score is not derived from the visual report.
