# Atlas Route-Map Component Layout Contract

Use this note when a generated PPTX visually shows card/container overlap even though generic bbox, text spacing, alignment graph, fidelity, and editability gates pass.

## Durable lesson

Parent-child containment is not enough for complex PPTX components. A route-map panel can contain all children legally while still being semantically broken: bottom bands can intrude into card bodies, floating badges can cover cards, guardrail notes can become orphaned between panel and footer, and ghost/double panels can pass normal overlap checks.

## Required approach

1. Treat recurring visual defects as generator/IR contract bugs, not as visual-review anecdotes.
2. Add or extend a deterministic component gate before accepting the fix.
3. Model explicit slots for complex components:
   - parent panel
   - card body slot
   - node/path slot
   - status badge/chrome slot
   - bottom rule-band slot
   - guardrail note slot
   - footer/risk rail exclusion zone
4. Define semantic overlap policy per slot. Legal containment does not imply legal overlap.
5. Fix compiler/generator coordinates or component grammar so the gate passes; do not relax the gate to bless a bad layout.
6. After the deterministic gate passes, still review full-size rendered slides for minor density/readability issues.

## Gate placement

For long-form PPTX visual-system validation, run component layout checks after low-level text/alignment gates and before visual-layout/aesthetic gates:

```text
check_layout_safety.py
check_text_spacing.py
check_alignment_graph.py
check_component_layout_contract.py
check_visual_layout_architecture.py
check_visual_aesthetic_contract.py
```

## Acceptance evidence

A real fix should include:

- failing fixture or current-bad report showing the defect was caught;
- regenerated IR/PPTX report showing `release_decision=pass`, `blocking_count=0`;
- false-positive check on other visual systems or representative decks;
- full-size rendered review confirming no blocker/major remains;
- learning note documenting symptom, root cause, fix, verification command, and prevention rule.

## Anti-patterns

- Saying “no obvious overlap” without checking component slots.
- Counting all parent-contained overlaps as legal.
- Using visual fidelity as design acceptance; fidelity can faithfully reproduce a bad IR.
- Shrinking business-critical text below readability gates to make layout fit.
- Waiving blockers instead of fixing the generator/IR contract.
