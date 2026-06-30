# Visual Variant Distinctiveness

## Purpose

Visual variants must be **visual-language variants**, not narrative or business-scenario presets.

A visual language describes:

- palette and color logic;
- typography package;
- material and surface treatment;
- light and atmosphere;
- motif system;
- container grammar;
- density and spacing;
- chart/table visual treatment;
- footer/source-band treatment.

A narrative intent describes:

- audience job;
- decision or persuasion task;
- evidence chain;
- risk/turn/contrast;
- closure/action path.

These two axes must remain orthogonal:

```text
Narrative Intent × Visual Language → Deck
```

## Correct Model

Use:

```json
{
  "narrative_intent": "risk_review",
  "visual_language": "terminal-cockpit"
}
```

Do not use:

```json
{
  "visual_variant": "dense-risk-review"
}
```

`risk_review` is a narrative task. `terminal-cockpit` is a visual language.

## Current Controlled Visual Languages

| Visual Language | Visual Meaning | Not Its Meaning |
|---|---|---|
| `matte-institutional` | subdued luminosity, formal grid, matte glass, compact ledger metrics | investment committee only |
| `luminous-glass` | high light energy, spotlight orbs, luminous panels, hero KPI treatment | strategy meeting only |
| `terminal-cockpit` | terminal grid, dense cockpit panels, status chips, monitoring source band | risk review only |

## Blocking Failures

- `VISUAL_NARRATIVE_COUPLING`: visual language name contains business scenario terms.
- `LEGACY_VISUAL_VARIANT`: controlled contract uses `visual_variant` instead of `visual_language`.
- `WEAK_COORDINATE_REALIZATION`: visual coordinates do not materialize into PPTX object roles.
- `COMPONENT_GRAMMAR_UNCHANGED`: visual language does not alter visible component grammar.
- `VISUAL_VARIANT_DISTANCE_TOO_LOW`: pairwise visual grammar signatures are too close.

## Orthogonality Acceptance

Run:

```bash
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
```

Acceptance:

- [ ] Controlled contracts cover all visual languages.
- [ ] Supporting narrative examples may cover multiple narrative intents, but visual-language proof uses a same-content base.
- [ ] Visual-language names and visual coordinates do not contain narrative/business terms.
- [ ] Changing `narrative_intent` on the same contract does not change `visual_grammar` or visual role counts.
- [ ] Changing `visual_language` on the same narrative/content changes `visual_grammar`.
- [ ] `validate_glass_variants.py` uses `examples/variants/glass-fintech-visual-language-base.contract.json` and verifies identical slide/native-text fingerprints across all visual languages.
- [ ] Rendered contact sheets are visibly different at visual-language level.

## Same-Content Visual-Language Proof

A visual-language proof is invalid if each visual language uses a different narrative skeleton. The validation deck must keep these fixed:

- slide count;
- slide topology sequence;
- titles, body text, metrics, charts, source/risk notes;
- `narrative_intent`.

Only these may change:

- `visual_language`;
- visual coordinates such as luminosity, panel density, accent energy, motif variation, formality, and data prominence.

The current executable proof compiles the same base contract into:

```text
matte-institutional × strategy_update
luminous-glass × strategy_update
terminal-cockpit × strategy_update
```

This is deliberately stricter than proving one business scenario per visual language.

## Prevention Rule

Never name a visual language after the meeting, business topic, or narrative task it often serves. If a name answers “what is this deck about?” rather than “what does it look and feel like?”, it belongs in `narrative_intent`, not `visual_language`.
