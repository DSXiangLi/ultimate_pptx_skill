# PPTX Template Research Library

## Purpose

Use `research/pptx-template-library/` as the curated specimen pool for PPTX cloning, visual DNA extraction, layout grammar mining, and benchmark corpus expansion.

This library is **research input**, not a runtime template picker. Do not directly apply downloaded templates to user content. Every useful template must first be decompiled into evidence-backed style tokens, visual DNA, layout archetypes, component contracts, and QA cases.

## Library Location

```text
research/pptx-template-library/
  README.md
  index.json
  candidates.finance-upgrade.json
  files/*.pptx
  previews/contact-sheet-first-slides.png
  previews/first-slide/*.png
```

Read the README and `index.json` before selecting specimens. Keep attribution/license/source-page metadata with every specimen.

## Current Selection Policy

The current library has already been narrowed for finance-compatible PPTX learning:

- direct `.pptx` files verified as valid OOXML packages;
- public source pages retained;
- CC BY 4.0 attribution notes captured;
- people/portrait/photography/portfolio-dependent templates removed;
- preferred scenarios: finance, technology, risk/compliance, data strategy, information graphics, business dashboards, institutional proposals.

## First-Batch Clone Candidates

Prioritize a small, diverse first batch rather than cloning all templates equally. The goal is to cover distinct reusable grammar families.

| Priority | Template ID | Why it matters | Clone focus |
|---|---|---|---|
| P0 | `dark-minimalist-business` | Premium dark executive visual system with low noise and strong title hierarchy. | cover/section architecture, dark surface, typography/numeral voice, executive rhythm |
| P0 | `it-software-sales-proposal-slides` | High-quality dark gradient enterprise proposal with strong commercial narrative. | proposal structure, value cards, gradient geometry, CTA/summary pages |
| P0 | `data-privacy-training-gradient` | Risk/compliance-compatible gradient tech system. | compliance/training page roles, security motif, source/risk treatment, dense explanatory pages |
| P0 | `digital-transformation-journey-infographic` | Compact journey/route-map information graphic. | roadmap arcs, milestone nodes, process sequencing, icon-card semantics |
| P0 | `data-strategy-roadmap-infographic` | Data strategy roadmap grammar; highly relevant to algorithm/data-platform decks. | stage timeline, capability map, milestone labels, planning hierarchy |
| P0 | `difference-between-saving-and-investment-slides` | Direct finance education/comparison structure. | comparison layouts, explainer typography, finance-safe illustration abstraction |
| P0 | `dark-modern-tech-startup-brand` | Strong dark 3D tech brand system; useful if de-startupified. | brand-system pages, token boards, product capability pages, 3D/vector fallback policy |
| P0/P1 | `business-scorecard-infographic` | KPI/dashboard component value is high, but cover has visual/photo residue. | scorecards, KPI grids, progress meters, dashboard density, photo replacement |

## Deprioritize for First Batch

Do not start with templates whose cover or core identity depends heavily on hard-to-license or hard-to-generalize imagery unless the user explicitly asks for that style:

- `blockchain-cryptocurrency-investment-slides` — useful theme, but coin/photo dependency is high.
- `blockchain-company-pitch-deck` — fintech theme is useful, but photo/coin imagery can dominate.
- `stocks-trading-business-plan` — finance structure is relevant, but city/building photography is not the desired core grammar.
- `ethics-of-artificial-intelligence` — AI governance is relevant, but robot/person-like hero imagery should not become the system anchor.
- `blue-connections` — useful network metaphor, but illustrated people/avatar dependency needs abstraction first.

## Specimen Intake Rules

For every selected template:

1. Copy the original PPTX into a specimen workspace without modifying it.
2. Preserve `source_url`, license/attribution, original filename, SHA256, slide count, theme/master/layout counts, and known embedded-media caveats.
3. Render original slides to PNG contact sheets and full-size images.
4. Extract text and OOXML inventories before assigning semantics.
5. Mark photo/illustration/3D dependencies explicitly as either:
   - **core DNA**: must be translated or regenerated carefully;
   - **replaceable atmosphere**: can become abstract texture/vector/raster background;
   - **discarded dependency**: should not enter the reusable generator.

## Promotion Rule

A template can influence the forward compiler only after it has gone through the PPTX cloner loop in `references/pptx-cloner.md`:

```text
specimen → inventory → raw IR → 1:1 rebuild → fidelity report
         → archetype mining → visual DNA → component contracts
         → generalized generator → benchmark/gate/learning note
```

A single attractive cover is not enough. Promote only patterns backed by repeated slides, OOXML evidence, and successful re-generation with new content.
