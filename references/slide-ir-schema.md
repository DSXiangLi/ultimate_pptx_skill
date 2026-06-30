# Slide IR Schema

## Minimal Shape

```json
{
  "deck": {
    "id": "demo",
    "size": { "w": 1280, "h": 720 },
    "slides": [
      {
        "id": "s1",
        "objects": []
      }
    ]
  }
}
```

## Common Object Fields

| Field | Required | Meaning |
|---|---:|---|
| `id` | yes | stable object ID |
| `type` | yes | `text`, `shape`, `chart`, `table`, `icon`, `image`, `group`, `rasterIsland`, `vectorIsland` |
| `role` | yes | semantic role: title/body/chart/risk/source/decor/background |
| `box` | yes | `{x,y,w,h}` in CSS px at 1280×720 base |
| `z` | yes | deterministic z-order |
| `editability` | yes | `{level, priority, user_can_edit}` |
| `render_policy` | yes | `native`, `vector`, `raster`, `hybrid` |

## Editability Levels

| Level | Meaning |
|---|---|
| `text` | editable as PowerPoint text |
| `data` | editable chart/table data |
| `style` | editable shape/style/color |
| `replaceable` | replace/regenerate as unit |
| `locked` | not intended to be edited |

## Object Types

### `text`

Required:

- `text`
- `style`
- `editability.level = text`
- priority ≥4 for title/body/risk/source

### `shape`

Required:

- `shape`: `rect`, `roundRect`, `oval`, `line`, `freeform`
- `fill` and/or `stroke`

### `chart`

Required:

- `chart_type`
- `data`
- `editability.level = data` for finance charts

### `table`

Required:

- `columns`
- `rows`

### `rasterIsland`

Required:

- `source.kind`: `html-fragment`, `svg`, `generated-art`, `texture`, `screenshot`
- `source.regenerable`: boolean
- `must_not_contain`: critical roles excluded from rasterization

## Acceptance Mechanism

A valid IR must satisfy:

- unique slide IDs and object IDs
- all object boxes have positive width/height
- priority ≥4 objects cannot have `render_policy: raster` unless `type` is `image` and role is non-critical
- `rasterIsland` has source metadata
- slide object z-order is deterministic
