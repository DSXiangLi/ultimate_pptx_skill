# Finance Benchmark Corpus Validation

Date: 2026-07-10

## Scope

Phase D adds a finance PPTX benchmark corpus contract and validator. The corpus prevents overfitting to one demo deck by requiring coverage across:

```text
3 finance scenarios × 3 density modes × 3 visual systems
```

## Files

- `examples/benchmarks/finance-pptx-benchmark-corpus.json`
- `scripts/check_finance_benchmark_corpus.py`
- `tests/test_finance_benchmark_corpus.py`
- `references/finance-benchmark-corpus.md`
- `scripts/validate_visual_systems.py`
- `scripts/validate_skill.py`
- `SKILL.md`

## Coverage

Scenarios:

- macro-review
- fund-comparison
- allocation-decision

Density modes:

- executive
- analyst
- dense

Visual systems:

- glass-fintech-pptx
- paper-analyst-report
- market-atlas-infographic

Required formal gate reports:

- layout-safety
- text-spacing
- alignment-graph
- component-layout-contract
- visual-layout-architecture
- visual-aesthetic-contract
- visual-dna-realization
- ooxml-visual-properties
- rendered-perceptual-layout
- visual-fidelity
- qa-report

## RED

Initial test failed because `scripts/check_finance_benchmark_corpus.py` did not exist.

## GREEN: unit regression

Command:

```bash
python3 -m unittest tests/test_finance_benchmark_corpus.py -v
```

Result:

```text
Ran 2 tests
OK
```

Coverage:

- missing scenario/density/style coverage fails;
- valid corpus passes static coverage.

## Real build-root validation

Command:

```bash
python3 scripts/check_finance_benchmark_corpus.py examples/benchmarks/finance-pptx-benchmark-corpus.json --build-root build --report verification/finance-benchmark-corpus-report.json
```

Result:

```text
PASS finance benchmark corpus cases=9 styles=3 pairs=9
```

Report:

```text
verification/finance-benchmark-corpus-report.json
```

## Formal visual-system validation

Command:

```bash
python3 scripts/validate_visual_systems.py
```

Result:

```text
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=94.95 edit=100.00; paper-analyst-report score=95.46 edit=100.00; market-atlas-infographic score=95.65 edit=100.00
```

## Full skill validation

Command:

```bash
python3 scripts/validate_skill.py
```

Result includes:

```text
PASS finance benchmark corpus regression tests
ALL CHECKS PASSED
```

## Fixes during implementation

The first real build-root run incorrectly failed `qa-report` because the corpus validator treated every report as a `release_decision`/`blocking_count` gate. It now handles heterogeneous report shapes:

- deterministic gates: `release_decision` and `blocking_count`;
- visual fidelity: `visual_fidelity.overall_score >= threshold` and no blocking issues;
- QA report: `scores.editability >= 95` and no blocking issues.

## Release decision

Accepted for workspace. Phase A-D are now complete at workspace level.
