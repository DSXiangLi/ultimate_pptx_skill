# CJK Office Typesetting and Alignment Gates

## When to Use

Use this reference when generating or reviewing Chinese/finance PPTX decks, especially when native editable text is exported to PowerPoint/LibreOffice. It captures a failure mode where a deck passed visual fidelity, editability, and coarse layout checks but still had professional typography defects in rendered screenshots.

## Failure Pattern

A deck can pass box-level checks while still failing real PPT review due to:

- Chinese title orphan wraps: the last line contains only 1-3 weighted characters.
- Protected terms split across native PowerPoint line breaks, e.g. `评审版本`, `风险预算`, `现金流`, `触发器`, `先进制造`, `AI算力`.
- Title-to-body visual crowding even when bounding boxes do not geometrically overlap.
- Card rows, chart-focus panels, or action-page card/body spans that are close but not aligned to a professional grid.
- Text containers that look technically valid but visually “hard-coded” instead of designed.

## Root Cause

For Chinese text in native PPTX text boxes, Office/LibreOffice rendering can be materially wider than a naive IR estimate. A practical conservative heuristic observed in the benchmark is:

```text
CJK measured width ≈ font_size × 1.30
ASCII measured width ≈ font_size × 0.55 × 1.30
available line width ≈ 88% of text-box width
```

A standard text-capacity check only asks “does the string fit in N lines?” It does not ask whether the line break falls inside a semantically protected term. That second question must be a separate gate.

## Required Gate Behavior

For Chinese finance decks, layout safety should block on:

- `TEXT_OVERFLOW_RISK`: priority text needs more lines than the box budget allows.
- `PROTECTED_TERM_WRAP_RISK`: estimated line break falls inside a protected Chinese term.
- `TITLE_ORPHAN_WRAP`: the title’s final estimated line is too short.
- `TITLE_TEXT_GAP_TOO_SMALL`: estimated title hitbox crowds subtitle/body text.
- `CONTENT_ROW_TOP_MISALIGNMENT`: paired panels in a row do not share top alignment.
- `CARD_ROW_EDGE_MISALIGNMENT`: same-row cards or card/body spans do not share intended left/right edges.

## Protected-Term Strategy

Start with domain phrases the user or rendered QA identifies as visually unacceptable when split. Examples:

```text
风险预算
评审版本
投委会
形成
现金流
稳定器
触发器
出海链条
承担
红利拥挤
先进制造
AI算力
```

Do not overfit by only shortening the current sentence. If a term split exposes a reusable class of risk, add the term/pattern to the gate and then adjust the content or component sizing.

## Review Workflow

1. Render the actual PPTX to PNG using the same pipeline that validates fidelity.
2. Build a contact sheet for all pages, not just sampled pages.
3. Review every page for title/content crowding, container alignment, CJK short-term splitting, truncation, and squeezed text.
4. When a defect is found, convert it into an executable gate before or alongside fixing the one slide.
5. Re-run the benchmark and verify `issue_count=0`, `blocking_count=0`, and rendered contact-sheet review has no blocking defects.

## Anti-Pattern

Do not conclude “software rendering difference” when the user's PowerPoint view matches the LibreOffice-rendered screenshot. That means the defect is in the generated PPTX/layout model, not the user's local editor.
