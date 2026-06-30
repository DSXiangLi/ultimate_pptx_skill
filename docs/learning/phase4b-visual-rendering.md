# Phase 4B Visual Rendering Learnings

## Context

We started P0 visual fidelity development for `ultimate-pptx-builder`.

## Environment Facts

Available:

- `libreoffice` / `soffice`
- `pdftoppm`
- Python `Pillow`

Unavailable:

- Node
- Chromium/Chrome CLI
- Playwright/Selenium Python packages
- `python-pptx`

## Problem 1: Browser screenshot path is not locally available

### Symptom

The desired future pipeline is:

```text
HTML preview → browser screenshot
PPTX → rendered PNG
visual diff
```

But there is no browser automation runtime in the environment.

### Root Cause

The machine has LibreOffice and Poppler but no Chromium/Node/Playwright stack.

### Fix

Phase 4B uses a deterministic IR/Pillow reference renderer instead:

```text
IR → reference PNG
PPTX → LibreOffice PDF → pdftoppm PNG
reference vs actual PNG diff
```

### Verification

```bash
python3 scripts/validate_skill.py
```

### Future Prevention

Before changing render strategy, inspect this file and re-check tool availability. Do not assume browser tooling exists.

## Problem 2: Older Pillow may not support `ImageDraw.rounded_rectangle`

### Symptom

`render_ir_png.py` failed with:

```text
AttributeError: 'ImageDraw' object has no attribute 'rounded_rectangle'
```

### Root Cause

The installed Pillow exposes `Image`, `ImageDraw`, and fonts, but lacks newer rounded rectangle drawing APIs.

### Fix

`render_ir_png.py` now checks `hasattr(draw, "rounded_rectangle")`. If unavailable, it degrades `roundRect` to a normal rectangle for the visual reference MVP.

### Verification

```bash
python3 scripts/render_ir_png.py build/phase4b.ir.json build/phase4b-visual-fidelity/expected
```

### Future Prevention

Avoid assuming modern Pillow drawing APIs. Feature-detect optional methods and degrade deterministically.

## Problem 3: Older Pillow may not support `ImageDraw.textbbox`

### Symptom

`render_ir_png.py` failed with:

```text
AttributeError: 'ImageDraw' object has no attribute 'textbbox'
```

### Root Cause

The installed Pillow predates `textbbox` even though it supports basic text drawing.

### Fix

`render_ir_png.py` now uses a compatibility helper:

1. `draw.textbbox` when available.
2. `draw.textsize` when available.
3. `font.getsize` fallback.
4. approximate character width as last resort.

### Verification

```bash
python3 scripts/render_ir_png.py build/phase4b.ir.json build/phase4b-visual-fidelity/expected
```

### Future Prevention

All reference-renderer text measurement must go through the compatibility helper, not direct Pillow APIs.

## Problem 4: Destructive shell cleanup is unnecessary and can be blocked

### Symptom

A smoke command using project directory cleanup was blocked by safety approval.

### Root Cause

The command combined validation with destructive cleanup. Even if the target was `build/`, bundling cleanup into the smoke command is unnecessary.

### Fix

Render scripts now use Python `tempfile.TemporaryDirectory` for LibreOffice intermediates and write deterministic output files without project-directory deletion.

### Verification

```bash
python3 scripts/run_visual_fidelity.py build/validation-phase1.ir.json build/validation-deck.pptx build/visual-fidelity-report.json
```

### Future Prevention

Avoid `rm -rf` in validation/smoke commands. Prefer controlled temp dirs or explicit overwrite of generated files.
