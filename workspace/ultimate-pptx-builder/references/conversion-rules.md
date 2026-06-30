# Conversion Rules Ledger

This ledger records conversion decisions and bugs. Add a new rule whenever a defect is found.

## Rule Format

```yaml
- id: CR-001
  symptom: Single-line title wraps in PPTX but not HTML.
  cause: PowerPoint text metrics differ from Chromium.
  rule: For source single-line text, disable wrap and widen box by 4-8%.
  acceptance: Rendered PPTX title remains one line and does not collide with next object.
```

## Seed Rules

### CR-001 — Single-line text wrapping

- **Symptom:** Chrome fits one-line text; PowerPoint wraps it.
- **Rule:** Mark source single-line text; disable word wrap in PPTX and add width tolerance.
- **Acceptance:** PPTX render keeps line count stable.

### CR-002 — Complex background effects

- **Symptom:** Gradient/blur/glass effects become ugly native approximations.
- **Rule:** Use rasterIsland for complex background; keep text/charts native above it.
- **Acceptance:** Background fidelity preserved and all critical text remains editable.

### CR-003 — Pseudo-elements carrying content

- **Symptom:** CSS `::before`/`::after` text disappears or rasterizes.
- **Rule:** Pseudo-elements may only be decorative; meaningful content must become IR object.
- **Acceptance:** IR contains all visible meaningful text.
