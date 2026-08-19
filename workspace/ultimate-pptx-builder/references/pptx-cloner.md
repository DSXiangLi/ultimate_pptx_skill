# PPTX Cloner / Reverse Compiler Contract

## 适用范围

用户提供 `.pptx` 样本，目标是提取可复用、可编辑的视觉系统、布局语法、组件契约或模板生成器时，使用本文件。源 PPTX 是证据；最终产物是可复用生成能力，不是复制文件。

## 输入

```text
single deck: <source.pptx>
collection:  samples/<collection>/*.pptx
library:     research/pptx-template-library/files/<template-id>.pptx
notes:       purpose, must-match pages, must-remain-editable fields
```

## 证据包

每个样本输出到：

```text
specimens/<deck_id>/
  original.pptx
  provenance.json
  unpacked/
  rendered/slide-01.png
  rendered/contact-sheet.png
  extracted-text.md
  object-inventory.json
  theme-inventory.json
  master-layout-inventory.json
  asset-inventory.json
  decompiled.raw.ir.json
  rebuilt.pptx
  rebuilt-rendered/
  rebuild-fidelity-report.json
  cloner-loop-report.json
```

`rebuilt.pptx` 是内部诊断产物；不要把它当作最终模板系统。

## 主命令

```bash
python3 scripts/run_pptx_cloner_loop.py \
  <source.pptx> \
  --deck-id <deck-id> \
  --out specimens/<deck-id> \
  --require-render \
  --max-iterations 3
```

模板库样本示例：

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/<template-id>.pptx \
  --deck-id <template-id> \
  --out specimens/<template-id> \
  --require-render \
  --max-iterations 3
```

`--skip-render` 只用于单元测试或渲染不可用环境；跳过渲染不能作为视觉抽象质量证据。

## Loop Report Schema

每轮循环输出 `specimens/<deck-id>/cloner-loop-report.json`：

```yaml
release_decision: pass | fail
blocking_count: integer
gates:
  - id: string
    status: pass | fail
    evidence: string
optimization_queue:
  - gate: string
    owner: analyzer | decompiler | rebuilder | renderer | validator | generator
    action: string
    evidence_path: string
next_phase_allowed: boolean
next_phase: C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | null
```

如果 `release_decision != pass`，修复 `optimization_queue` 中最高优先级阻断项，并重跑同一命令；不要推进下一阶段。

## 阶段契约

| Phase | 产物 | 发布门禁 |
|---|---|---|
| C0 sample selection | selected deck ids + provenance | 样本覆盖不同语法家族；来源/许可/SHA256 记录 |
| C1 specimen analysis | unpacked package, inventories, renders, extracted text | slide/render/text/object inventory 存在且可追踪 |
| C2 OOXML → raw IR | `decompiled.raw.ir.json` | slide count、关键文本、对象、坐标、z、source refs 达到召回阈值 |
| C3 diagnostic rebuild | `rebuilt.pptx`, rendered rebuild, fidelity report | Office package、关键文本、对象类别、渲染差异报告通过 |
| C4 archetype mining | layout/component archetypes | 组件由重复证据支持，单例不提升为通用组件 |
| C5 visual DNA | visual DNA program + PPTX material policy | DNA 绑定对象证据，不只是颜色/背景 |
| C6 component contracts | `component-contracts/*.contract.json` | slot、密度、overlap、fallback 均可验证 |
| C7 generator | new-content generated deck | 新内容仍保留家族特征且关键对象可编辑 |
| C8 promotion | tests/schemas/gates/docs updated | 发现被转为脚本、schema、fixture 或 contract |

## Raw IR 最小字段

```yaml
id: stable clone object id
type: text | shape | image | chart | table | group | vectorIsland | rasterIsland
role_guess: conservative semantic role
box: {x, y, w, h}
z: object order
text: extracted text if any
style: fill/stroke/shadow/effect summary
font: family/size/weight/color/paragraph rules
image_ref: media relationship if any
chart_ref: chart XML relationship if any
group_id: source group if any
source_xml_path: ppt/slides/slideN.xml
source_shape_id: original cNvPr id/name
editability: guessed priority
render_policy: native | vector | raster | hybrid
```

## Cloner QA Gates

| Gate | 阻断条件 |
|---|---|
| provenance | 缺少来源、SHA256、slide count、theme/master/layout counts |
| package parse | PPTX 不能解包或关键 XML 不可解析 |
| render evidence | `--require-render` 时缺少原始全尺寸渲染和 contact sheet |
| text recall | 源关键文本未进入 IR 或 rebuild |
| object recall | shape/text/image/chart/table/group 召回不足或 source refs 丢失 |
| editability | title/body/data/source/risk 被 rasterized |
| package validity | rebuilt PPTX 不符合 Office package 结构 |
| visual fidelity | rendered rebuild 无 diff/report 或阻断差异未归因 |
| archetype evidence | 组件/布局无重复证据却被提升 |
| promotion | 学习只写在 prose，没有进入脚本/schema/fixture/contract |

## Object Coverage References

| 问题 | 参考文件 |
|---|---|
| 图片占位符 | `references/pptx-cloner-c3-image-reconstruction.md` |
| 背景/母版材质丢失 | `references/pptx-cloner-c3-background-reconstruction.md` |
| picture fill shape | `references/pptx-cloner-c3-picture-fill-shapes.md` |
| group 子对象不透明 | `references/pptx-cloner-c3-group-recursion.md` |
| 空文本容器 | `references/pptx-cloner-c3-empty-text-containers.md` |
| 原生表格 | `references/pptx-cloner-c3-native-table-reconstruction.md` |
| 表格样式 | `references/pptx-cloner-c3-table-styling.md` |
| 材质应用会降低保真 | `references/pptx-cloner-c3-materialization-policy.md` |

## 修复路径

- C1/C2 失败：修复 analyzer/decompiler，重跑 cloner loop。
- C3 package/text/render 失败：修复 rebuilder/exporter，不推进 DNA 抽象。
- fidelity 受未支持对象影响：先补 object coverage，再抽象组件。
- 可复用生成器失败：回到 visual DNA、layout archetypes 或 component contracts，补 fixture 与 gate。
- 新发现重复出现：进入 C8，把规则沉淀为脚本、schema、fixture 或 validator。
