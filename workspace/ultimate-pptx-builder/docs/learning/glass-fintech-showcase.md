# Glass Fintech Showcase Learnings

## Context

Development focus shifted from adding multiple style presets to making one style, `glass-fintech-pptx`, run end-to-end at high quality.

## Rule

Before modifying glass showcase compiler/render/export logic, read this file and `docs/learning/phase4b-visual-rendering.md`.

## Problem 1: Path formatting precedence can break PNG rendering

### Symptom

`validate_glass_showcase.py` failed inside `render_ir_png.py` with:

```text
TypeError: unsupported operand type(s) for %: 'PosixPath' and 'int'
```

### Root Cause

`outdir / "slide-%02d.png" % idx` is parsed as `(outdir / "slide-%02d.png") % idx`; `Path` does not support `%` formatting.

### Fix

Use explicit parentheses:

```python
path = outdir / ("slide-%02d.png" % idx)
```

### Verification Command

```bash
python3 scripts/validate_glass_showcase.py
```

### Future Prevention

When mixing `Path / ...` and old-style string formatting, format the string first or use an f-string before joining the path.

## Problem 2: Glass blur is not a native MVP feature

### Symptom

A literal glassmorphism design usually assumes CSS backdrop blur or raster effects, but the current MVP exporter only supports native OOXML text and shapes.

### Root Cause

True blur is not uniformly editable in PowerPoint native shapes and cannot be promised without raster/vector fallback logic.

### Fix

Simulate glass using native translucent fills, thin high-contrast strokes, layered accent orbs, and shadows. Critical information remains native text.

### Verification Command

```bash
python3 scripts/validate_glass_showcase.py
python3 scripts/validate_skill.py
```

### Files Affected

- `scripts/compile_spec_to_ir.py`
- `scripts/export_ir_pptx.py`
- `scripts/render_ir_png.py`
- `examples/glass-fintech-showcase.contract.json`
- `examples/glass-fintech-pptx.style.json`

### Future Prevention

Do not add blur claims unless the PPTX exporter and visual validator prove it. Use the phrase "glass simulation" for native translucent shape strategy.

## Problem 3: Editable chart should not mean Office chart XML first

### Symptom

The glass showcase needed a financial chart, but implementing full Office chart XML plus embedded workbook relationships would add a large amount of OOXML complexity to the MVP exporter.

### Root Cause

PowerPoint has two different useful notions of chart editability:

1. data-editable Office chart parts with embedded workbook data;
2. visually editable vector chart groups made from native shapes/text.

For the current no-dependency exporter, option 2 is a better GREEN step because every bar, label, axis and legend remains editable in PowerPoint and can be visually audited.

### Fix

Represent glass charts in IR as `type: chart`, `render_policy: native-vector-group`, priority 5. Export them as grouped native shapes/text semantics in the slide XML and audit them as `editable-vector-chart`, not raster.

### Verification Command

```bash
python3 scripts/validate_glass_showcase.py
python3 scripts/validate_skill.py
```

## Problem 4: SVG percent signs conflict with Python `%` formatting

### Symptom

After adding HTML preview for chart objects, validation failed in `render_ir_html.py` with:

```text
ValueError: unsupported format character '"'
```

### Root Cause

The SVG template contained literal `width="100%" height="100%"` while the whole string used Python `%` formatting.

### Fix

Escape literal percentages as `100%%`, or use f-strings for the template.

## Problem 5: A technically valid chart can still look like a decorative widget

### Symptom

The first chart implementation passed export audit and visual fidelity but visual QA found it too small and under-specified for finance use.

### Root Cause

A financial chart needs semantic affordances beyond colored bars: unit, axis, legend, data labels, source note and non-internal copy.

### Fix

For priority-5 financial charts, include at minimum:

- business-facing title;
- visible unit or axis labels;
- legend;
- key endpoint labels when space is limited;
- formal source/note text;
- no internal production wording on the slide.

### Verification Command

```bash
python3 scripts/validate_glass_showcase.py
```

Then inspect `build/glass-fintech-showcase/visual-fidelity/actual/slide-02.png`.



---

## Problem 8: Long-form benchmark needs narrative QA, not only pixel/editability QA

### Symptom

The first 15-slide benchmark passed the technical pipeline, but visual QA found finance-user problems:

- Allocation-table summary cards disagreed with table rows.
- Matrix summary counts were not clearly derived from matrix cells.
- Process page title said three stages while the body had four steps.
- Risk rail used internal test wording, which weakened formal finance-material tone.
- A table-page subtitle collided visually with metric cards.

### Root Cause

Visual fidelity and editability prove renderer consistency, but they do not prove that the deck would survive a user or investment-committee reading. Long decks need a narrative/practicality QA pass that checks data口径, decision logic, slide-level narrative job, and formal finance wording.

### Fix

- Added `examples/glass-fintech-benchmark.contract.json` with simulated realistic user input, audience, scenario, data assumptions, and per-slide `narrative_job`.
- Added `scripts/validate_glass_benchmark.py` requiring exactly 15 slides, multiple topology coverage, four editable vector charts, two editable vector tables, no raster fallback, and visual/QA gates.
- Rewrote slide 5, 6, and 9 content after visual QA to fix business-logic and professionalism issues.
- Suppressed subtitles for table topology and enlarged matrix metric-card height to avoid visual collisions.

### Verification

```bash
python3 scripts/validate_glass_benchmark.py
python3 scripts/validate_skill.py
```

Expected result:

```text
PASS glass benchmark slides=15 score=94.89 editability=100.00
PASS glass-fintech benchmark
ALL CHECKS PASSED
```

### Prevention Rule

For any benchmark deck longer than 5 slides, run a user-perspective narrative QA pass on at least the densest table, matrix/process, and compliance/risk pages. Do not accept a deck solely because pixel fidelity and editability scores are high.

---

## Problem 9: Editable finance tables can start as vector groups, but must be audited explicitly

### Symptom

The 15-slide benchmark required high-density tables. Compiler could generate `type=table`, but PPTX export initially failed because table objects were unsupported.

### Root Cause

The MVP exporter previously supported native text, shapes, charts as editable vector groups, and raster placeholders. It did not have a table rendering policy or audit kind.

### Fix

- Added IR `type=table` with `render_policy: native-vector-group`.
- Added HTML, Pillow, and PPTX renderers for editable vector tables.
- Export audit now reports `actual=editable-vector-table`.
- Benchmark validator requires at least two editable vector tables and rejects raster fallback.

### Verification

```bash
python3 scripts/validate_glass_benchmark.py
```

### Prevention Rule

Any finance table with priority >=4 must export as editable native/vector text+shape objects and appear in export audit as `editable-vector-table`; do not hide tables inside screenshots.


---

## Problem 10: Automated fidelity/editability PASS can still fail real page design QA

### Symptom

A 15-slide `glass-fintech-benchmark` deck passed automated validation:

```text
PASS glass benchmark slides=15 score=94.89 editability=100.00
```

But user review in PowerPoint found many objects overflowing or nearly overflowing card/page boundaries, and the overall style felt too AI-generated and under-designed.

A rendered contact-sheet review confirmed the critique:

- bottom elements too close to slide edges on slides 04, 07, 11, 12, 13, 14, 15
- title/page-number collisions or tension on many slides, especially 15
- dense tables/matrices with weak readability on slides 05, 06, 10, 14
- large decorative page numbers and repeated glass cards creating obvious AI-template smell
- automated visual fidelity compared PPTX against an IR/Pillow reference that shared the same flawed layout, so it could not catch design-quality failures

### Root Cause

The QA stack measured internal consistency and editability, not independent design quality. If the IR layout itself is flawed, PPTX can faithfully render a bad design and still score highly. Large-deck design QA requires a rendered-page review against human design criteria: safe zones, hierarchy, density, repetition, typography, and anti-template smell.

### Fix Direction

- Add a rendered contact-sheet audit before declaring any long benchmark complete.
- Treat page-edge safety, object/card overflow, and title/page-number collision as blocking visual QA issues.
- Reduce or remove giant decorative page numbers on content-heavy slides.
- Add a stricter anti-AI-style rubric: vary page rhythm, reduce glow/card repetition, replace generic slogan titles with direct investment judgments, and make data visualizations the visual hero.
- Do not allow `validate_skill.py` alone to mean design acceptance for decks longer than 5 slides.

### Verification Artifact

```text
build/glass-fintech-benchmark/audit-contact-sheet.png
```

### Prevention Rule

For long-form PPTX output, automated fidelity/editability is necessary but insufficient. Before final delivery, render the actual PPTX pages, inspect a contact sheet, then zoom into all flagged pages. A deck can only be called visually accepted after this independent rendered-page design QA pass is clean or accepted by the user.


## Problem 11: Layout safety needs executable separation and density gates, not only edge margins

**Symptom:** After adding a 64px bottom safe zone, rendered contact-sheet review still showed footer crowding and dense table/compliance pages. Objects were technically outside the slide edge danger zone, but visually sat too close to the footer rail; Slide 05 also carried six core table columns, and compliance pages could become document-like.

**Root cause:** A single bottom-edge rule does not model real PPT layout. Finance decks also need a separation band between content and footer, table field-count limits, and compliance density limits. Pixel fidelity cannot catch this because it faithfully compares against the same flawed IR.

**Fix:** `scripts/check_layout_safety.py` now enforces:

- 64px bottom safe zone
- 16px footer separation band above the risk/source rail
- CJK-aware priority text capacity
- table max 5 core columns
- compliance/suitability max 4 body paragraphs
- title/page-number collision and oversized repeated page-number checks

The glass-fintech benchmark layout was adjusted accordingly: footer rail is thinner/lower, risk note uses the finance footer threshold, and the allocation table was reduced from six core fields to five by merging rationale/trigger.

**Verification:**

```bash
python3 scripts/check_layout_safety.py build/glass-fintech-benchmark/glass-fintech-benchmark.ir.json --report build/glass-fintech-benchmark/glass-fintech-benchmark-layout-safety-report.json
python3 scripts/validate_glass_benchmark.py
python3 scripts/validate_skill.py
```

Expected result: layout report has `blocking_count=0`; benchmark reports `layout=pass`; main validator passes.


## 2026-06-29 — Layout Fidelity Is Not Layout Correctness

### Problem

The 15-slide benchmark initially passed visual fidelity and QA while still containing obvious layout defects:

- metric card value/delta text overlapped;
- table pages had title/metric-band visual collisions;
- high-density tables passed because the checker only looked at editability and renderer consistency;
- compliance wording contained internal benchmark/test language.

### Root Cause

The previous validation stack compared Pillow reference rendering against LibreOffice-rendered PPTX. That proves the PPTX faithfully matches the generated IR, but it does **not** prove the IR layout is reasonable. If the IR contains overlapping text, both expected and actual renders can contain the same defect and still receive a high fidelity score.

The first layout-safety gate was also insufficient: it checked safe zones, footer separation, text capacity, and table row height, but did not check pairwise text collisions or metric-card internal stacking.

### Fix

`check_layout_safety.py` now blocks on:

- estimated text-box collisions;
- metric-card label/value/delta stack gaps;
- metric child padding inside the card;
- table cell density and row height;
- footer separation and page-number/title proximity.

`compile_spec_to_ir.py` now uses intrinsic metric-card layout instead of fixed y offsets, and content-heavy pages use smaller title typography plus safer vertical bands.

### Prevention Rule

Never accept a deck only because visual fidelity is high. Fidelity answers “did export preserve the IR?” not “is the layout sane?”. Every long-form finance deck must pass a separate layout/text safety gate before HTML/PPTX export is considered releasable.


## Problem 12: Text leading and visual containers need their own gates

### Symptom

After metric-card text collision was fixed, user review still found two visual defects:

- wrapped text lines could appear nearly overlapped or too tight in dense native PPTX objects;
- containers could overlap or double-frame each other even when text objects did not geometrically collide.

Rendered review confirmed examples: table pages still needed stronger title-to-metric spacing; chart/table/action topologies contained visual double panels or overlapping panel/card zones.

### Root Cause

The layout gate was still mostly object/text-box oriented. It did not model:

- PowerPoint paragraph leading for wrapped Chinese/native text;
- container-container collisions and unapproved nested panels;
- title band to first content container breathing room as a blocking rule.

The PPTX exporter also relied on default renderer line spacing, which is not stable across LibreOffice/PowerPoint and can make dense CJK text feel collapsed.

### Fix

- `export_ir_pptx.py` now writes explicit `<a:lnSpc><a:spcPct .../></a:lnSpc>` paragraph spacing for native text.
- `check_layout_safety.py` now blocks container overlap, unapproved nested double panels, and title-content gaps below the finance-deck threshold.
- `compile_spec_to_ir.py` now removes redundant outer table panels, separates action-page KPI cards from body panels, reduces chart-focus note panel height, and gives table pages a larger title-to-metric gap.

### Verification

```bash
python3 scripts/validate_glass_benchmark.py
python3 scripts/validate_skill.py
```

Expected result: benchmark reports `layout=pass`, fidelity remains above threshold, and focused visual review of Slides 05/06/09/10/11/12/15 has no blockers for text leading or container overlap.

### Prevention Rule

Do not treat text-box non-overlap as typographic acceptance. Long-form editable PPTX needs explicit native text leading plus a separate visual-container collision model. Containers should be laid out as zones, not allowed to accidentally press into or wrap each other.


---

## Problem 12: CJK line-capacity and protected-term wraps can pass box checks but fail rendered review

### Symptom

User review found that the rendered PPTX still had title/body crowding, text-container alignment defects, and Chinese terms split across line breaks even after earlier overlap/container gates passed. Examples included title orphan wraps, `评审版本` being split, body text splitting `形成`, and matrix labels splitting terms like `先进制造` / `AI算力`.

### Root Cause

The layout checker's CJK estimate was still too optimistic for Office/LibreOffice native text. It treated CJK width as roughly `font_size * 1.0`, while the rendered PPTX behaved closer to `font_size * 1.30` for these Chinese fonts and OOXML text boxes. The old gate also checked box capacity, but not whether a line break lands inside a protected Chinese phrase.

### Fix

- Added `TEXT_RENDER_SCALE = 1.30` to compiler/checker line-capacity estimates.
- Added `PROTECTED_TERM_WRAP_RISK` for key Chinese terms that should not be split across lines.
- Added title orphan-wrap, title-to-text gap, chart-focus row alignment, card-row baseline, and action card/body edge-alignment gates.
- Shortened benchmark labels/copy where the content itself was too dense for a PPT component.

### Verification

```bash
python3 scripts/validate_glass_benchmark.py
# PASS glass benchmark slides=15 score=96.01 editability=100.00 layout=pass
python3 scripts/validate_skill.py
```

### Prevention Rule

For Chinese finance decks, do not accept a box-level text-capacity pass as typography acceptance. Treat Office-rendered CJK widths, protected-term wrapping, title orphan lines, and component-grid alignment as executable gates plus rendered contact-sheet review.


---

## Problem 13: A visual anchor must prove variation, not just declare coordinates

### Symptom

The first controlled-variant validation failed with:

```text
TEMPLATE_SMELL: Slide role signatures are too repetitive for an anchor family.
```

`sober-committee` originally selected two table-heavy pages plus an action fallback page; `luminous-strategy` originally selected cover/hero/action plus two similar chart pages. Both were valid decks, but their slide-role signatures were too repetitive to prove that `glass-fintech-pptx` is a reusable visual anchor rather than a one-off template.

### Root Cause

Visual-anchor coordinates such as luminosity, accent energy, motif, and compliance tone are insufficient if the underlying page-role sequence repeats the same object grammar. A style anchor must preserve immutable DNA while varying page roles and rhythm; otherwise it becomes a template with parameter changes.

### Fix

- Added `references/visual-anchor-system.md` and `schemas/visual-anchor.schema.json`.
- Added `examples/visual-anchors/glass-fintech-pptx.anchor.json` with immutable DNA, mutable coordinates, mutation operators, page-role variants, material policy, and anti-drift rules.
- Added `scripts/check_visual_anchor.py` to block weak DNA evidence, critical rasterization, missing risk/data DNA, and repeated slide-role signatures.
- Added three controlled variants under `examples/variants/`:
  - `sober-committee`
  - `luminous-strategy`
  - `dense-risk-review`
- Revised variant slide selections so each mini deck includes distinct roles such as cover, chart/dashboard, table/matrix/scenario/compliance, and process/action instead of repeating the same page grammar.
- Added `scripts/validate_glass_variants.py` and integrated it into `scripts/validate_skill.py`.

### Verification

```bash
python3 scripts/validate_glass_variants.py
# PASS glass variants count=3 sober-committee score=95.75 edit=100.00; luminous-strategy score=95.70 edit=100.00; dense-risk-review score=95.60 edit=100.00
python3 scripts/validate_skill.py
# ALL CHECKS PASSED
```

### Prevention Rule

Do not accept a new visual anchor or variant by visual-token changes alone. Each anchor family must prove: immutable DNA evidence, bounded coordinate variation, page-role rhythm variation, no critical rasterization, narrative/layout safety, and no `TEMPLATE_SMELL` blocker.

---

## Problem 14: Visual variants can pass structural gates while remaining visually underpowered

### Symptom

Rendered controlled variants passed narrative, layout, editability, visual-fidelity, and role-signature checks, but human review found that `sober-committee`, `luminous-strategy`, and `dense-risk-review` still looked almost identical. The visible differences were mostly content selection, small layout changes, orb position/opacity, hairline opacity, and a few decorative toggles.

### Root Cause

The compiler realized visual coordinates only at the decoration layer. Variant profiles changed glow/orb parameters and page selections, but did not materially alter visual grammar: typography scale, panel material, metric-card grammar, chart/table treatment, footer/risk-rail behavior, or motif roles. The old gate checked structural distinctiveness but not grammar-level visual distinctiveness.

### Fix

- Upgraded `VARIANT_PROFILES` in `scripts/compile_spec_to_ir.py` from decorative settings to grammar-bearing profiles:
  - `sober-committee`: `strict-grid`, `matte-glass`, `formal-compact`, `committee-footer`.
  - `luminous-strategy`: `spotlight-orb`, `luminous-glass`, `hero-kpi`, `presentation-footer`.
  - `dense-risk-review`: `terminal-grid`, `dense-cockpit`, `status-chip`, `monitoring-status-bar`.
- Added visible variant-specific PPTX roles such as `committee-gridline`, `committee-ruler`, `luminous-ribbon`, `spotlight-orb`, `terminal-gridline`, and `status-chip`.
- Added `visual_grammar` to compiled IR deck metadata.
- Upgraded `scripts/validate_glass_variants.py` with grammar realization and cross-variant distance checks.
- Upgraded `scripts/check_visual_anchor.py` to block `WEAK_COORDINATE_REALIZATION`, `COMPONENT_GRAMMAR_UNCHANGED`, and `VISUAL_VARIANT_DISTANCE_TOO_LOW` for controlled variants.
- Re-rendered the three PPTX variants and reviewed contact sheets. The updated variants are now visually distinct while retaining glass-fintech DNA.

### Verification

```bash
python3 scripts/validate_glass_variants.py
# PASS glass variants count=3 sober-committee score=95.96 edit=100.00; luminous-strategy score=95.56 edit=100.00; dense-risk-review score=95.72 edit=100.00
python3 scripts/validate_skill.py
# ALL CHECKS PASSED
```

Rendered contact sheets:

- `build/glass-fintech-sober-committee/contact-sheet-sober-committee.png`
- `build/glass-fintech-luminous-strategy/contact-sheet-luminous-strategy.png`
- `build/glass-fintech-dense-risk-review/contact-sheet-dense-risk-review.png`

### Prevention Rule

Do not accept a visual-anchor variant because it declares coordinates or passes role-signature variation. A variant must materialize coordinate changes into grammar-level visible differences: motif, material, component grammar, layout rhythm, risk/footer treatment, and content-bearing PPTX roles. Automated gates must fail variants that only alter decoration.

---

## Problem 15: Visual-language proof requires same content, not just separate fields

### Symptom

After splitting `visual_language` from `narrative_intent`, rendered comparisons still partially reflected different business/narrative skeletons. A reviewer could still read the variants as meeting/scenario presets rather than pure visual-language programs.

### Root Cause

Field-level orthogonality is necessary but insufficient. If each visual language is validated with a different contract, slide sequence, topology, or business use case, narrative differences can still create perceived visual differences. The validation sample itself couples visual proof to narrative content.

### Fix

- Added `examples/variants/glass-fintech-visual-language-base.contract.json` as the same-content validation base.
- Reworked `scripts/validate_glass_variants.py` so every controlled visual-language run uses the same slides, same text, same charts, and the same `narrative_intent=strategy_update`.
- The validator now changes only `visual_language` and visual coordinates, then checks identical compiled native-text fingerprints across visual languages.
- Strengthened component-level grammar so `terminal-cockpit` is not just a darker `matte-institutional`: terminal status bar, NODE page label, rectangular status chips, stronger grid/rail treatment, and profile-driven panel palette.

### Verification

```bash
python3 scripts/check_narrative_visual_orthogonality.py
# PASS narrative/visual orthogonality visual_languages=3 narrative_intents=3
python3 scripts/validate_glass_variants.py
# PASS glass visual languages same_content=1 count=3 matte-institutional score=96.15 edit=100.00; luminous-glass score=95.55 edit=100.00; terminal-cockpit score=95.79 edit=100.00
python3 scripts/validate_skill.py
# ALL CHECKS PASSED
```

Rendered same-content comparison:

- `build/visual-language-same-content-comparison.png`

### Prevention Rule

Never validate a visual language by giving it its own narrative skeleton. Visual-language acceptance must hold content and `narrative_intent` fixed; otherwise, the test proves scenario-template diversity, not visual-language extensibility.

---

## Problem 16: Multi-visual-system validation must include full-size visual review

### Symptom

The new multi-visual-system validator passed for `glass-fintech-pptx`, `paper-analyst-report`, and `market-atlas-infographic`, but full-size review of `market-atlas-infographic` Slide 05 revealed a visible overlap between the right-side `对冲 / 再平衡（月度）` metric tile and the fourth process card.

### Root Cause

Automated layout and fidelity gates estimate object geometry and rendered similarity, but they do not fully capture perceived collisions between dense visual-system decorations, route lines, metric tiles, and process-card clusters. Contact-sheet thumbnails can also hide subtle overlap; full-size slide review is still required for dense pages.

### Fix

- Adjusted `market-atlas-infographic` process-page metric tile positions in `scripts/compile_spec_to_ir.py` so the third/right metric tile no longer overlaps the fourth process card.
- Regenerated `build/visual-system-same-content-comparison.png` with wider/wrapped left labels so the validation artifact itself does not introduce misleading truncation.
- Re-ran `scripts/validate_visual_systems.py` and full-size visual review for `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-05.png`.

### Verification

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/validate_visual_systems.py
python3 scripts/validate_visual_systems.py
# PASS visual systems same_content=1 count=3 glass-fintech-pptx score=96.15 edit=100.00; paper-analyst-report score=96.58 edit=100.00; market-atlas-infographic score=96.74 edit=100.00
```

Rendered review artifacts:

- `build/visual-system-same-content-comparison.png`
- `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-05.png`

### Prevention Rule

Do not accept a new visual system solely because automated gates pass. For each new visual system, review at least the densest full-size rendered page plus the contact sheet. If full-size review finds overlap, treat it as a generation/layout bug even when layout safety, visual fidelity, and editability scores pass.

## Problem 17: Visual DNA hardening must change information-bearing components

**Symptom.** A multi-system deck can pass first-glance review while still feeling like one template with different backgrounds. The failure shows up in shared chart palettes, identical typography rhythm, reused metric cards, similar footer/header treatment, and nearly identical page-role skeletons.

**Root cause.** The compiler treated `visual_system_grammar` as mostly surface/background grammar. Chart rendering, typography, container geometry, metric cards, analyst/report components, and process/scenario page structures still shared one implementation path.

**Fix.** Visual DNA hardening must alter real editable IR/PPTX objects, not only declared metadata:

- chart `series_palette`, axis/grid style, value label color, and bar geometry;
- text font roles for title/body/metric/caption;
- metric-card and container geometry by visual system;
- research memo components such as exhibit labels, analyst notes, assumption tables, execution checklists;
- atlas route/node layout for process pages;
- fintech dashboard contrast and signal-card treatment.

**Acceptance rule.** A visual system is not release-ready if chart, font, card/container, component, and layout signatures remain substantially shared. The same-content contact sheet must show visual DNA differences in information-bearing regions, not just background texture or accent color.

## Problem 18: Layout defects are architecture diagnostics

**Context:** Multi-visual-system PPTX outputs passed geometric layout safety, visual fidelity, editability, and QA, but review still found style-specific layout failures: chart undersizing, atlas route/title intrusion, and process-page route/card density overload.

**Symptom:** The defect was tempting to fix with local coordinate edits. That would have left the skill vulnerable because each generated PPTX was actually a diagnostic sample for the architecture.

**Root cause:** Existing gates checked object overlap, text capacity, safe zones, and visual fidelity, but did not classify visible layout defects as local slide bugs, style-DNA adaptation bugs, or systemic gate gaps. They also lacked visual-layout architecture rules for route/title safe areas, chart minimum area, process-page content budgets, and page-role hierarchy.

**Fix:** Added `references/layout-defect-taxonomy.md` and `scripts/check_visual_layout_architecture.py`. Integrated the new gate into cross-visual-system validation before PPTX export. Repaired the compiler grammar instead of patching one slide: enlarged Glass chart-led dashboard chart slot, moved/suppressed Atlas decorative routes around title/process pages, demoted Atlas process metrics to signal chips, enlarged process cards, raised process text size, and reduced process-page grid noise.

**Verification:**

```bash
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Full-size visual review of `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-05.png` returned PASS: process order is clear, text is readable, bottom safety improved, and no blocking overlap/overflow remains.

**Prevention rule:** If a rendered PPTX has a visible layout defect after automated PASS, treat it as a validation-system bug first. Classify A local / B style-DNA / C systemic before fixing. A class-C issue blocks release until the skill reference or executable gate is upgraded.

## Problem 19: Strict visual acceptance must catch decorative hierarchy noise and Office package compatibility

**Symptom:** A deck can pass coarse layout/fidelity/editability gates while still showing fine text crowding, chaotic-looking containers, noisy decorative map lines, and PowerPoint/WPS repair warnings.

**Root cause:** The old validation was too broad: it checked large overlaps and package presence, but not strict Office compatibility, decorative hierarchy, protected-term wrapping, or professional layout order at detail level. The hand-written OOXML exporter also created a stricter-Office compatibility risk.

**Fix:** Use `python-pptx` for default PPTX package generation, strengthen `check_pptx_package.py` with relationship resolution and roundtrip checks, tighten `check_visual_layout_architecture.py`, reduce Atlas grid/route/node noise, separate Paper title and KPI rails, and shrink/fade Dark Glass edge decoration.

**Verification:** `python3 scripts/validate_visual_systems.py` passes with editability 100; strict visual audit final decision is PASS; `check_pptx_package.py` passes all three generated PPTX files.

**Prevention:** Treat user-visible fine overlap/noise and Office repair prompts as release blockers. Do not call a PPTX final until strict visual review and Office package compatibility pass together.
