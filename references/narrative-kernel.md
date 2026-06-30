# Narrative Kernel

## Purpose

`ultimate-pptx-builder` should not only arrange slides. It should preserve the strongest known human presentation patterns: content transmission, attention control, complete narrative chain, and formal decision rhythm.

The narrative layer has two parts:

```text
Narrative Kernel -> guides generation
Narrative Rules  -> checks generated decks
```

Topology is an implementation detail. The kernel is the reason a deck works.

## Kernel Principles

| Principle | Meaning | Generation Requirement |
|---|---|---|
| Audience job | The deck serves a decision, understanding, persuasion, or memory task | Define audience, scenario, desired after-state |
| One-slide one-job | Each slide does one primary narrative job | Every slide must declare `narrative_job` |
| Claim-before-evidence | Title states the point before showing proof | Key page titles should be conclusion/action titles, not topic labels |
| Attention path | The page controls first, second, and third read | One dominant read, then support, then source/risk |
| Cognitive load budget | Reduce interpretation effort | Avoid competing focal points and unnecessary density |
| Evidence sufficiency | Important claims need data/rationale/source | Bind claims to metrics, chart, table, body evidence, or source |
| Contrast/turn | Strong decks contain tension | Use risk/opportunity, base/stress, before/after, trade-off, or scenario |
| Arc continuity | Slides form a chain, not a pile | Opening -> evidence -> turn/risk -> resolution/action |
| Formal credibility | Finance decks require professional language and compliance visibility | Risk/source rail and formal wording are mandatory |
| Memorable closure | The ending leaves action, decision, or monitoring path | Last section should provide next steps or decision frame |

## Narrative Rule Families

### Deck-Level Rules

- `MISSING_AUDIENCE_JOB`: no audience/scenario/desired outcome.
- `ARC_GAP`: deck lacks opening, evidence, risk/turn, or resolution/action.
- `WEAK_CLOSURE`: final slide does not leave action, decision, or monitoring path.

### Slide-Level Rules

- `MISSING_NARRATIVE_JOB`: slide lacks primary job.
- `TITLE_NOT_CLAIM`: title is a topic label rather than a conclusion/action-oriented claim.
- `GENERIC_AI_TITLE`: title is empty or generic.
- `CLAIM_WITHOUT_EVIDENCE`: title asserts a claim without evidence/takeaway/source.
- `EVIDENCE_WITHOUT_TAKEAWAY`: chart/table/metrics page lacks interpretation.
- `MISSING_RISK_OR_SOURCE`: finance slide lacks risk/source rail.
- `DUPLICATE_NARRATIVE_JOB`: consecutive slides repeat the same job without adding information.

## Acceptance

A finance benchmark deck is narratively acceptable when:

- audience, scenario, and desired after-state are explicit;
- each slide has one narrative job;
- key titles are claim/action titles;
- every chart/table/metric page has a takeaway;
- the deck arc includes opening, evidence, risk/turn, and action/closure;
- finance slides have visible source/risk wording;
- `scripts/check_narrative_safety.py` returns `release_decision=pass`.
