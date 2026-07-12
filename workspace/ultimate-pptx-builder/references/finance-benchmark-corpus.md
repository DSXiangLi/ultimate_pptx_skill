# Finance PPTX Benchmark Corpus

## Purpose

The benchmark corpus prevents the visual compiler from overfitting to one demo deck or one density level. It defines the minimum regression surface for finance-grade PPTX generation:

```text
3 scenarios × 3 density modes × 3 visual systems
```

It is a corpus contract, not just documentation. The validator checks both static coverage and, when `--build-root` is provided, whether every formal gate report exists and passes for the current real builds.

## Corpus manifest

```text
examples/benchmarks/finance-pptx-benchmark-corpus.json
```

Required scenarios:

- `macro-review`
- `fund-comparison`
- `allocation-decision`

Required density modes:

- `executive`
- `analyst`
- `dense`

Required visual systems:

- `glass-fintech-pptx`
- `paper-analyst-report`
- `market-atlas-infographic`

Required preservation fields:

- every case must preserve `source` and `risk`;
- high-pressure cases must preserve `evidence` and `logic`;
- fund-comparison cases preserve recommendation intent rather than collapsing to neutral education.

## Validator

```bash
python3 scripts/check_finance_benchmark_corpus.py \
  examples/benchmarks/finance-pptx-benchmark-corpus.json \
  --build-root build \
  --report verification/finance-benchmark-corpus-report.json
```

Static blockers:

- `BENCHMARK_REQUIRED_AXES_MISSING`
- `BENCHMARK_DUPLICATE_CASE_ID`
- `BENCHMARK_SCENARIO_DENSITY_COVERAGE_MISSING`
- `BENCHMARK_STYLE_COVERAGE_MISSING`
- `BENCHMARK_CONTENT_PRESSURE_COVERAGE_MISSING`
- `BENCHMARK_REQUIRED_GATE_REPORTS_MISSING`

Build-report blockers:

- `BENCHMARK_BUILD_MISSING`
- `BENCHMARK_GATE_REPORT_MISSING`
- `BENCHMARK_GATE_REPORT_FAILED`

## Required gate reports

The corpus requires every real visual-system build to carry these formal reports:

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

The validator understands heterogeneous report shapes:

- deterministic gates use `release_decision` / `blocking_count`;
- visual fidelity uses `visual_fidelity.overall_score >= threshold` and no blocking issues;
- QA report uses `scores.editability >= 95` and no blocking issues.

## Pipeline integration

`validate_visual_systems.py` now runs the corpus validator after all visual systems are built and after cross-system distance / visual DNA depth checks.

This makes the benchmark corpus a release-level contract rather than a passive list.

## Acceptance

```bash
python3 -m unittest tests/test_finance_benchmark_corpus.py -v
python3 scripts/check_finance_benchmark_corpus.py examples/benchmarks/finance-pptx-benchmark-corpus.json --build-root build --report verification/finance-benchmark-corpus-report.json
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Expected:

```text
PASS finance benchmark corpus cases=9 styles=3 pairs=9
PASS visual systems ...
ALL CHECKS PASSED
```

## Boundary

The corpus does not yet generate all 27 concrete decks. It defines the coverage contract and verifies that the current three real visual-system builds satisfy every formal gate. The next extension is to map each corpus case to generated concrete content contracts and run sampled/parallel builds.
