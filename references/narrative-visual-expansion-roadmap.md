# Narrative Kernel and Visual Anchor Expansion Roadmap

## Purpose

This roadmap guides Phase 1 expansion of `ultimate-pptx-builder` beyond the current `glass-fintech-pptx` benchmark.

The goal is **not** to accumulate more slide templates or style names. The goal is to build a PPTX design compiler that captures superior human presentation patterns:

```text
Narrative Kernel → Narrative Rules → Visual Anchor → Controlled Visual Extension → PPTX Material Policy → QA Gates
```

A mature PPTX system should have an advantage in:

- transmitting content clearly;
- attracting and directing user attention;
- maintaining a complete narrative chain;
- creating strong opening, development, turn, and resolution rhythm;
- preserving editability and Office reliability.

## Core Thesis

Phase 1 expansion should optimize around two ideas:

1. **Narrative layer = kernel + rules**
   - The kernel guides content generation.
   - The rules check whether the generated deck follows superior presentation logic.

2. **Visual layer = anchors + bounded extension space**
   - A visual anchor should generate a family of decks, not one fixed template.
   - Each anchor must define immutable DNA, mutable coordinates, mutation operators, and quality gates.

## 1. Narrative Layer: Kernel, Not Template Enumeration

Narrative topology is useful, but it is not the essence. The essence is a reusable communication kernel that answers:

```text
What should the audience notice first?
What should they believe next?
What evidence earns that belief?
Where is the turn or contrast?
What decision/action should remain after the slide or deck ends?
```

### 1.1 Narrative Kernel

The narrative kernel should guide generation with these principles:

| Kernel Principle | Meaning | PPTX Implication |
|---|---|---|
| Audience job | Every deck serves a decision, understanding, persuasion, or memory task | Define audience, scenario, and desired after-state before layout |
| One-slide one-job | Each slide performs one primary narrative function | Every slide needs `narrative_job`; no mixed-purpose clutter |
| Claim-before-evidence | The title should state the point, not merely name the chart | Prefer conclusion titles over topic labels |
| Attention path | The page must control first/second/third read | Establish dominant object, support, source/risk |
| Cognitive load budget | The deck must reduce interpretation effort | Limit competing focal points; manage density deliberately |
| Evidence sufficiency | Important claims require supporting data, comparison, or rationale | Check claim/evidence link, source, units, assumptions |
| Contrast/turn | Strong decks contain tension: before/after, risk/opportunity, base/stress, trade-off | Encode comparison, scenario, or decision fork when needed |
| Arc continuity | Slides should form a chain, not a pile | Deck has opening, development, turn, resolution/action |
| Formal credibility | Finance decks require professional wording, risk/source visibility, no casual claims | Enforce risk rail, source note, compliance tone |
| Memorable closure | The ending should leave decision/action/monitoring path | Final slides include action plan, owner, next checkpoint, or decision principle |

### 1.2 Narrative Rules

The rules should check the generated deck. These should become `check_narrative_safety.py` gates.

Recommended blocking checks:

| Rule | Blocking Failure |
|---|---|
| `MISSING_AUDIENCE_JOB` | Deck lacks audience/scenario/desired outcome |
| `MISSING_NARRATIVE_JOB` | Slide lacks primary narrative job |
| `TITLE_NOT_CLAIM` | Key slide title is only a topic label, not a conclusion or action-oriented claim |
| `NO_DOMINANT_READ` | Slide has no clear first read |
| `CLAIM_WITHOUT_EVIDENCE` | Slide title asserts a conclusion without data/rationale/source |
| `EVIDENCE_WITHOUT_TAKEAWAY` | Data page shows chart/table but no interpretation |
| `ARC_GAP` | Deck lacks opening, evidence, turn/risk, and resolution/action |
| `BROKEN_TRANSITION` | Adjacent slides do not connect logically |
| `UNRESOLVED_TENSION` | A risk/trade-off/scenario is introduced but never resolved |
| `DUPLICATE_NARRATIVE_JOB` | Consecutive slides repeat the same job without adding information |
| `GENERIC_AI_TITLE` | Title uses empty wording like “市场洞察/核心分析/总结展望” without real claim |
| `MISSING_RISK_OR_SOURCE` | Finance claim lacks source/risk rail when required |
| `WEAK_CLOSURE` | Deck ends without action, decision, or monitoring path |

### 1.3 Narrative Forms as Secondary Layer

Topology still matters, but it should implement the kernel rather than replace it.

Examples:

```text
hero-thesis        = opening attention + thesis
chart-focus        = claim + evidence + interpretation
matrix             = compare + segment + recommendation
scenario-cards     = tension + stress + trade-off
process-roadmap    = resolution + execution path
action-plan        = closure + next step
compliance         = formal constraint + credibility
```

Phase 1 should keep topology compact and strengthen its rules.

## 2. Visual Layer: Anchors, Not One-Off Templates

A visual template is a fixed artifact. A visual anchor is a generative region.

A style anchor must be able to answer:

```text
What cannot change, or the style is lost?
What can vary, so the deck does not look repetitive?
How far can it mutate before leaving the style family?
Which visual moves are allowed for cover, data, appendix, dense table, and closing pages?
Which effects are native/vector/raster under PPTX constraints?
```

### 2.1 Visual Anchor Model

Each visual anchor should define:

| Layer | Purpose |
|---|---|
| Immutable DNA | The minimum features that make the style recognizable |
| Mutable Coordinates | Controlled axes that can vary per deck/page |
| Mutation Operators | Allowed transformations that create variety |
| Density Modes | Rules for low, medium, high, appendix density |
| Page Role Variants | Cover/data/process/table/compliance/closing behavior |
| Material Policy | Native/vector/raster editability strategy |
| Anti-Drift Rules | What would break the style or make it generic |
| QA Rubric | How to judge if the anchor is expressed well |

### 2.2 Visual Coordinates

Use coordinates instead of style enumeration:

| Coordinate | Example Range |
|---|---|
| Authority tone | institutional / editorial / strategic / tech / luxury |
| Structure | strict grid / modular cards / asymmetrical editorial / radial / timeline |
| Surface | flat paper / glass / terminal / print / dimensional / map-like |
| Depth | flat / layered / volumetric / atmospheric |
| Color logic | monochrome+accent / semantic risk colors / heatmap / brand palette |
| Typography | CN sans / editorial serif / condensed numerals / mono data |
| Data grammar | axis chart / matrix / waterfall / decomposition / sparkline / map |
| Motif | rules / orbs / atlas / seal / node graph / ticker / marginalia |
| Rhythm | steady institutional / dramatic reveal / editorial pacing / dense appendix |
| Density | low / medium / high / appendix |
| Material strategy | native-only / native+vector / decorative raster allowed |

### 2.3 Anchor Extension Example: `glass-fintech-pptx`

Current anchor:

```yaml
id: glass-fintech-pptx
immutable_dna:
  - dark institutional finance surface
  - translucent glass panels
  - cyan/violet/gold accents
  - editable native text
  - editable vector chart/table
  - visible risk/source rail
mutable_coordinates:
  luminosity: [sober, luminous]
  panel_density: [sparse, medium, dense]
  accent_energy: [quiet, balanced, high]
  data_prominence: [metric-led, chart-led, table-led]
  motif_variation: [orb, gridline, terminal, constellation]
mutation_operators:
  - swap panel split direction
  - vary accent orb placement and scale
  - alternate metric band/card treatment
  - shift between chart-led and table-led layouts
  - use stricter compliance mode on formal pages
anti_drift:
  - no random neon poster look
  - no unreadable tiny finance text
  - no screenshot-based critical data
  - no same glass-card motif repeated on every page
```

This means the anchor can create many decks in one family without becoming a fixed template.

## 3. Phase 1 Optimized Implementation Goal

Phase 1 should be renamed from “expand topology/style library” to:

```text
Build Narrative Kernel v1 + Visual Anchor System v1
```

### Goal A — Narrative Kernel v1

Deliverables:

```text
references/narrative-kernel.md
schemas/narrative-kernel.schema.json
scripts/check_narrative_safety.py
examples/narrative-kernel.finance.json
```

Minimum capabilities:

- define audience job;
- define slide narrative job;
- enforce claim/evidence/takeaway/source/risk relationships;
- check deck arc: opening → evidence → contrast/turn → resolution/action;
- detect generic titles, missing takeaways, unsupported claims, weak closure.

Acceptance:

```text
check_narrative_safety.py examples/glass-fintech-benchmark.contract.json -> pass
```

### Goal B — Visual Anchor System v1

Deliverables:

```text
references/visual-anchor-system.md
schemas/visual-anchor.schema.json
examples/visual-anchors/glass-fintech-pptx.anchor.json
scripts/check_visual_anchor.py
```

Minimum capabilities:

- define immutable DNA;
- define mutable coordinates and allowed ranges;
- define mutation operators;
- define page-role variants;
- define PPTX material strategy;
- define anti-drift and anti-template-smell checks.

Acceptance:

```text
check_visual_anchor.py examples/visual-anchors/glass-fintech-pptx.anchor.json build/.../deck.ir.json -> pass
```

### Goal C — Controlled Variation Benchmark

The proof that a visual anchor is not a one-off template is not another style name. The proof is multiple decks in the same anchor with different coordinates.

Create three variants from the same `glass-fintech-pptx` anchor:

| Variant | Use Case | Coordinate Shift |
|---|---|---|
| sober-committee | 投委会正式版 | lower luminosity, stricter grid, higher compliance tone |
| luminous-strategy | 策略会展示版 | stronger accent, chart-led pages, more visual energy |
| dense-risk-review | 风险复盘版 | higher density, table/matrix-led pages, restrained decoration |

All three should still be recognizably `glass-fintech-pptx`, but not look like the same PPT with text swapped.

Acceptance:

```text
same anchor DNA score >= 4
variant distinctiveness score >= 4
layout safety pass
narrative safety pass
editability >= 95
visual fidelity >= 90
```

## 4. What Not To Do

Do not optimize by:

- adding many one-off templates;
- adding style names without anchor grammar;
- calling every topology a template;
- letting arbitrary visual effects override editability;
- relying on visual fidelity as design acceptance;
- fixing narrative problems by making slides prettier;
- fixing visual repetition by randomizing colors only.

## 5. Phase 1 Success Definition

Phase 1 succeeds when the system can say:

```text
I know what makes a PPT narratively strong.
I can check whether this deck follows that logic.
I know what makes this visual anchor recognizable.
I can extend the anchor within safe boundaries.
I can prove the result is editable, readable, visually distinct, and Office-safe.
```

Concrete success target:

```text
1 narrative kernel spec
1 narrative safety checker
1 visual anchor schema
1 visual anchor checker
3 controlled glass-fintech variants
all variants pass layout/text/narrative/visual/editability gates
```

## 6. Ultimate Target

The ultimate target is a finance-grade PPTX design compiler:

```text
business content + audience + scenario + desired action
  → narrative kernel planning
  → deck arc construction
  → visual anchor selection
  → bounded visual variation
  → editable PPTX realization
  → narrative/layout/visual/Office QA
  → self-improving rules
```

This is stronger than a template library because it captures the reason great decks work, not only their surface appearance.
