# Text Spacing + Alignment Graph QA Validation

## Scope

This validation records the upgrade from coarse “no obvious overlap” checks to deterministic relational layout QA.

Implemented gates:

- `scripts/check_text_spacing.py`
- `scripts/check_alignment_graph.py`
- `tests/test_text_spacing_and_alignment_gates.py`
- `references/text-spacing-and-alignment-qa.md`

Integrated into:

- `scripts/validate_visual_systems.py`
- `scripts/validate_skill.py`
- `scripts/compile_spec_to_ir.py` via generated `layout_relations`

## Mechanisms Added

### Text Distance Field

The new text spacing gate traverses priority native text blocks pairwise and classifies each pair before applying role-aware spacing thresholds.

It can now block issues such as:

- text boxes colliding after estimated ink extents;
- metric label/value/delta stacks with insufficient breathing room;
- unrelated text modules sitting too close while not overlapping;
- paragraph rhythm that is visually too tight;
- footer/risk notes too close to body content.

### Alignment Graph

The new alignment gate validates explicit `layout_relations` in the IR.

It now blocks:

- slides with no declared layout relations;
- declared left/right/top/bottom/center alignment drift;
- equal width/height violations;
- unequal gutters in rows;
- parent-padding violations where text leaves its component container.

It also emits near-miss alignment warnings for strong anchors that are close but not aligned.

## Bugs Caught During Integration

The new gates caught real problems that previous validators did not block:

1. `market-atlas-infographic` scenario zones had `impact/action` text violating parent padding.
2. Some process/signal/scenario component text needed role-specific spacing classification instead of being treated as unrelated text.
3. Paper analyst scenario/process pages lacked explicit layout relations despite passing previous safety/aesthetic gates.
4. Initial relation inference over-declared table columns for Glass horizontal cards; relation generation was corrected to distinguish tabular rows from horizontal card grammars.

## Verification Commands

Workspace validation:

```bash
python3 tests/test_text_spacing_and_alignment_gates.py
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Final workspace result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=94.95 edit=100.00; paper-analyst-report score=95.46 edit=100.00; market-atlas-infographic score=95.78 edit=100.00
ALL CHECKS PASSED
```

## Acceptance

The release gate is considered upgraded only when:

- both new scripts exist and are listed as required skill files;
- their regression tests run inside `validate_skill.py`;
- `validate_visual_systems.py` runs both gates after layout safety and before visual-layout/aesthetic checks;
- compiler output includes non-empty `layout_relations` for generated visual-system slides;
- workspace and installed skill directories both pass `python3 scripts/validate_skill.py`.

## Learning

The core lesson is that layout QA must validate relationships, not just boxes. A deck can pass collision, editability, and visual-fidelity checks while still failing professional layout standards because text is too close, alignment is nearly-but-not-quite consistent, or children overflow their semantic parent containers.
