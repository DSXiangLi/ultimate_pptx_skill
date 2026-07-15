# PPTX Cloner C3.6 Native Table Reconstruction

Use this reference when C3 rebuild reports `table` placeholders or when a source PPTX contains editable PowerPoint tables that should remain native/editable in the diagnostic rebuild and later generator.

## Durable lesson

A visible table in a high-quality PPTX is often a real native PowerPoint table, not a raster image. Treating it as an opaque placeholder hides business-critical comparison data and prevents later chart/table grammar extraction.

Native tables are part of the reusable PPTX compiler surface, especially for finance/business decks.

## Recognition rule

During C1 specimen analysis, if a shape exposes `has_table` / `.table`, extract structured table metadata:

```json
{
  "row_count": 6,
  "column_count": 3,
  "cells": [
    ["What matters", "Traditional tools", ""],
    ["Setup time", "Weeks", "Days"]
  ]
}
```

This first slice captures geometry and cell text. It does **not** yet preserve full table styling.

## C2 IR pattern

C2 should preserve the extracted table as `table_ref` and classify it as a native reconstruction candidate:

```json
{
  "type": "table",
  "table_ref": {
    "row_count": 2,
    "column_count": 2,
    "cells": [["Driver", "Value"], ["Speed", "High"]]
  },
  "classification": {
    "kind": "native-table-candidate",
    "reason": "source object exposes native table rows, columns, and cell text"
  },
  "render_policy": "native"
}
```

## C3 rebuild rule

During diagnostic rebuild:

1. If `type == table` and `table_ref` has row/column counts, call:

```python
slide.shapes.add_table(rows, cols, x, y, w, h)
```

2. Write every captured cell text into the rebuilt table.
3. Record materialization as:

```json
"produced": "native-table"
```

4. Do not add the table to `unsupported_objects`.
5. Preserve `table_rows`, `table_columns`, source shape metadata, and classification in `rebuild-report.json`.

## Tests to preserve

- C2 decompiler test: sample native table emits `table_ref.row_count`, `table_ref.column_count`, cell text, and `classification.kind == native-table-candidate`.
- C3 loop test: sample native table materializes as `native-table` and no `table` appears in `unsupported_objects`.

## Current limitations

C3.6 restores editable table structure and text, not full visual style. Expected remaining gaps:

- row heights / column widths;
- cell fill colors;
- border color/width/dash;
- font size/color/bold/alignment;
- merged cells;
- margins and vertical alignment;
- theme/table style inheritance.

A small visual-score dip after replacing a placeholder with an unstyled native table is acceptable if object-class coverage improves. The next increment should optimize table visual properties instead of reverting to placeholders.

## Promotion rule

Do not mine chart/table visual grammar from a source deck until native table structure is present in IR. A placeholder or screenshot cannot prove reusable table grammar. After C3.6, C4/C5 may use `table_ref` evidence for table layout/content archetypes, but style DNA claims require table styling reconstruction or explicit degradation notes.
