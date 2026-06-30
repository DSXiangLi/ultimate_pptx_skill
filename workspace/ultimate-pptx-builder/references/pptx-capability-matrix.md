# PPTX Capability Matrix

| Visual Feature | Native PPTX | Vector | Raster | Recommendation |
|---|---:|---:|---:|---|
| Plain text | excellent | no | avoid | native text |
| Rich text runs | good | no | avoid | native text runs |
| Rect / round rect / oval | excellent | good | avoid | native shape |
| Simple line/arrow | excellent | good | avoid | native connector |
| Simple icon | limited | good | fallback | SVG path to freeform if possible |
| Complex SVG | limited | partial | good | vector if editable needed, raster if decorative |
| Flat chart | good | good | avoid | native chart for finance data |
| Complex custom chart | limited | partial | good | native/vector for data-critical, raster for decorative |
| Table | good | partial | avoid | native table or grouped text/shapes |
| Gradient | partial via OOXML | no | good | native simple gradient, raster complex gradient |
| Blur/glass/filter | poor | no | excellent | rasterIsland, keep text native above |
| Noise/texture | poor | no | excellent | rasterIsland |
| Mask/clip-path | limited | partial | good | simple crop/path, raster complex mask |
| Blend mode | poor | no | excellent | rasterIsland |
| Animation | partial | no | no | optional future layer, static first |

## Acceptance Mechanism

When implementing a renderer, every feature must be assigned one of:

- `native-supported`
- `native-partial`
- `vector-supported`
- `raster-required`
- `unsupported`

Unsupported or raster-required features cannot carry critical content.
