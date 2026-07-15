# PPTX Cloner C3.7 Native Table Styling First Slice

Use this reference after C3.6 native table reconstruction when a table is editable but visually weaker than the source because it uses PowerPoint defaults.

## Durable lesson

Object-class coverage and visual fidelity are separate gates. Rebuilding a table as native PowerPoint proves editability and structured data recall, but default table styles can still hurt visual fidelity. The correct next step is to reconstruct table visual properties incrementally, not to revert to placeholders or raster images.

## First supported style fields

C1 extracts conservative cell-level style fields from native tables:

```json
{
  "fill_rgb": "1A2B3C",
  "alignment": "CENTER",
  "margin_left_emu": 91440,
  "margin_right_emu": 91440,
  "margin_top_emu": 45720,
  "margin_bottom_emu": 45720,
  "font": {
    "name": "Aptos Display",
    "size_pt": 14,
    "bold": true,
    "italic": false,
    "color_rgb": "FFFFFF"
  }
}
```

The extraction is intentionally conservative:

- only solid cell fills become `fill_rgb`;
- gradient/theme fills are not coerced into fake solid colors;
- the first non-empty run supplies the first-slice font style;
- unsupported properties remain absent rather than guessed.

## C2 IR pattern

`table_ref` should include a `cell_styles` matrix parallel to `cells`:

```json
{
  "table_ref": {
    "row_count": 2,
    "column_count": 2,
    "cells": [["Driver", "Value"], ["Speed", "High"]],
    "cell_styles": [[{"fill_rgb": "1A2B3C"}, {"fill_rgb": "1A2B3C"}], [{"fill_rgb": "DDEEFF"}, {"fill_rgb": "DDEEFF"}]]
  }
}
```

## C3 rebuild rule

When materializing native tables:

1. Write cell text first.
2. Apply conservative cell style fields:
   - `fill_rgb` → `cell.fill.solid()` / `fore_color.rgb`;
   - margins → `text_frame.margin_*`;
   - `alignment` → first paragraph alignment;
   - font name/size/bold/italic/color → first run font.
3. Record style coverage in `rebuild-report.json`:

```json
"styled_table_cells": 18
```

## Current limitations

C3.7 first slice does not yet reconstruct:

- gradient fills;
- theme fills;
- table borders/gridlines;
- row heights and column widths;
- merged cells;
- vertical alignment;
- per-run mixed typography;
- table style inheritance.

A visual score may stay flat or dip slightly when partial native styling exposes missing gradient/border/theme support. Treat this as a more precise diagnostic signal, not a failure of the native-table strategy.

## Tests to preserve

- C2 decompiler test: fixture table emits `cell_styles` with solid fill, font, alignment, and margins.
- C3 loop test: rebuilt PPTX table cell preserves header fill, font name, size, bold, and color; `rebuild-report.json` records styled cells.

## Next increments

Prioritize in this order:

1. table borders/gridlines;
2. row/column dimensions;
3. theme/gradient fill classification and approximation policy;
4. merged cells;
5. chart/table grammar mining only after style coverage is sufficient.
