# 终极 PPTX 构建技能调研与方案设计

> 目标：克服现有 PPTX 技能在 **HTML→PPTX 可编辑转换、优秀 PPTX 视觉创意、风格延展性、自主优化** 四个方面的瓶颈，设计一个真正可积累、可扩展、可验证的“终极 PPTX 构建技能”。
>
> 调研对象：`/home/lixiang/Desktop/huashu-design`、`/home/lixiang/Desktop/html-ppt-skill`、`/home/lixiang/Desktop/guizang-pptx-skill`、`/home/lixiang/Desktop/ppt-builder`、`/home/lixiang/Desktop/infographic-composer`。

---

## 0. 核心结论先行

### 0.1 终极转换问题的真正答案

不要把问题定义成“任意 HTML 自动转 PPTX”。这条路本质上是错的。

更准确的定义应该是：

> **用一个足够自由的创作语法，表达接近 HTML 的视觉能力；再通过一个显式的 PPTX 可编辑语义契约，把其中能编辑的部分转成原生 PPTX，把不可原生表达但必须保真的部分转成受控 raster/vector，并在对象层面标注可替换/可重建关系。**

换句话说：

- **浏览器可以继续作为布局与预览引擎**，因为它处理 flex/grid/absolute/字体测量/层叠很强。
- **但不能把任意 DOM 当作转换源**。必须引入一个中间层：`Slide IR / PPTX Scene Graph`。
- 这个 IR 不是 HTML，也不是 pptxgenjs API，而是“PPTX 可表达对象 + 保真逃生对象 + 编辑语义”的统一表示。
- HTML 只是 IR 的一种作者ing front-end。也可以从 Markdown、JSON DSL、Python 代码、Figma-like spec 生成 IR。

最终转换应该是：

```text
Content/Intent
   ↓
Narrative Plan（叙事拓扑）
   ↓
Style Program（风格程序：tokens × DNA × constraints）
   ↓
Slide IR（语义对象图：text / shape / chart / image / group / raster-island）
   ↓                     ↘
HTML Preview Renderer       PPTX Native Renderer
   ↓                         ↓
Visual QA Screenshot   Editable PPTX
   ↘                         ↙
       Fidelity / Design / Editability Evaluation Loop
```

关键思想：**不是 HTML 转 PPTX，而是同一个 IR 同时渲染成 HTML 预览和 PPTX 成品。**

现有 `ppt-builder` 已经接近这个方向：浏览器布局 + `ppt-*` 标记 + `.ppt-raster` 逃生口。但它仍是“HTML 是源，提取 marked DOM”。终极版应该再往前一步：**IR 是源，HTML/PPTX 都是渲染目标**。

---

## 1. 现有技能调研

### 1.1 `huashu-design`：直接 HTML→pptxgenjs，强调硬约束

相关文件：

- `references/editable-pptx.md`
- `scripts/html2pptx.js`
- `scripts/export_deck_pptx.mjs`

核心做法：

1. 每页独立 HTML。
2. 使用 Playwright 获取元素的 computed layout。
3. 用 `pptxgenjs` 转成 PowerPoint 对象。
4. 要求 HTML 从第一行就遵守 PPTX 约束：
   - `div` 不能直接有裸文字，文字必须包在 `p/h*`。
   - 不支持 CSS 渐变。
   - 背景/边框/阴影只能放在 `div` 上，不能放文字标签上。
   - `div` 不用 `background-image`，用 `<img>`。
5. 用 `data-pptx-merge` 支持多个段落合成一个可编辑文本框。

优点：

- 诚实地承认 PPTX 物理约束。
- 对文本编辑性有清晰追求。
- 有错误提示和转换失败规则。

问题：

- 仍然要求作者手写“PPTX 友好 HTML”。
- 对复杂视觉的策略基本是“放弃可编辑或导出 PDF”。
- 对 flex/grid/复杂相对布局本身没有系统抽象，主要靠 computed bounding box。
- 风格系统与转换系统分离不够。

判断：

> `huashu-design` 是“硬约束路线”的代表。它适合可控 HTML，但不是终极路线。终极路线应继承它的透明边界与文本合并经验，但不能停留在四条硬约束。

---

### 1.2 `ppt-builder`：当前最接近终极转换的雏形

相关文件：

- `SKILL.md`
- `reference/AUTHORING_CONTRACT.md`
- `reference/CONVERSION_RULES.md`
- `reference/EVOLUTION.md`
- `scripts/extract.js`
- `scripts/html2pptx.py`
- `scripts/qa_render.py`

核心思想：

> **The browser is the layout engine. `ppt-*` classes are the export markers.**

它不把所有 DOM 都转 PPTX，只导出显式标记节点：

| 标记 | PPTX 对象 | 说明 |
|---|---|---|
| `.ppt-text` | 原生文本框 | 可编辑文本，支持 inline runs |
| `.ppt-rect` | 矩形/圆角矩形 | solid fill / border / radius |
| `.ppt-oval` | 椭圆 | 原生 shape |
| `.ppt-line` | 直线 | 原生 connector |
| `.ppt-image` | 图片 | 元素截图或图片对象 |
| `.ppt-raster` | 图片 | 复杂视觉逃生口 |

关键优点：

1. **避免结构猜测**：未标记 DOM 全部是 layout scaffolding，不导出。
2. **保留 HTML 布局能力**：flex/grid/absolute 都可以用，最终只读 marked node 的 bbox。
3. **有复杂视觉逃生口**：gradient/SVG/chart/icon 可以 `.ppt-raster` 保真。
4. **有 conversion rule ledger**：每次遇到 bug，沉淀到 `CONVERSION_RULES.md`。
5. **有 QA loop**：HTML 与 PPTX 渲染成 side-by-side screenshot，用视觉模型比较。

核心局限：

- `.ppt-raster` 牺牲可编辑性。复杂图表、渐变、图标、装饰虽然保真，但无法编辑。
- 仍然依赖作者手动标记 `ppt-*`。
- IR 尚未独立出来；HTML DOM 仍是事实上的源。
- group、mask、gradient、chart、table、icon、smart-art 等 PPTX native 能力没有充分建模。
- “哪些对象必须可编辑，哪些可以 raster”缺少产品级策略。

判断：

> `ppt-builder` 的方向是对的：显式导出契约 + 浏览器布局 + native/raster 混合 + QA 迭代。终极技能应该以它为基座，但升级为 **IR-first、多后端渲染、可编辑性预算、局部反编译 raster island** 的架构。

---

### 1.3 `html-ppt-skill` 与 `guizang-pptx-skill`：风格枚举与 HTML deck 生产

相关观察：

- `html-ppt-skill` 有主题、布局、动画、图表、商务风格等大量枚举。
- `guizang-pptx-skill` 有强风格意识，强调 HTML/CSS 的视觉呈现。
- 它们擅长产出“看起来像网页/海报的 PPT 效果”。

问题：

- 如果最终目标是金融机构标准 PPTX，它们的 HTML-first 路线会卡在可编辑转换。
- 风格多是枚举式：每种风格容易变成一次性模板，复用时“长得太像”。
- 缺少 `infographic-composer` 那样的风格生成语法。

判断：

> 这些技能的价值不在转换技术，而在视觉灵感、版式样式、动效语言与 CSS 表现力。终极技能应把它们当作“视觉语料库/案例库”，不要继承它们的“直接 HTML 作为最终源”的架构。

---

### 1.4 `infographic-composer`：最值得借鉴的风格系统

关键文件：

- `SKILL.md`
- `docs/design/style-parameter-space.md`
- `docs/experiences/extension-principles.md`
- `references/narratives.md`
- `references/protocols.md`

它解决了一个很重要的问题：**风格不是枚举点，而是生成空间。**

核心架构：

```text
业务场景层
  ↓
版式层
  ↓
内容拓扑层
  ↓
枚举层：palette / typography / style / narrative
  ↓
开放层：metaphor / character / subject protocol
```

最重要的思想：

1. **层级纪律**：每层只回答一个问题。
2. **正交维度优先**：不要把密度、节奏、风格、拓扑混在一起。
3. **SOTA DNA**：每个 style 必须包含模型默认不会主动做的高级手法。
4. **生成规则 > 选项库**：隐喻、角色不是穷举，而是协议化生发。
5. **风格晶格**：用张力、语法、世界、DNA 去定位风格，而不是“科技风/商务风/国潮风”这种粗标签。

判断：

> 终极 PPTX 技能的风格系统应该直接借鉴 `infographic-composer`：把 PPTX 风格拆成 `Narrative Topology × Layout Grammar × Visual DNA × Tokens × PPTX Material Constraints`，让每个创意成为可延展锚点，而不是模板枚举。

---

## 2. 终极转换问题：为什么任意 HTML→可编辑 PPTX 不成立

### 2.1 HTML 与 PPTX 的表达模型不同

HTML/CSS 是流式、层叠、盒模型、像素渲染系统：

- layout 可以由 flex/grid/inline/block/absolute/transform 共同决定。
- 元素可以嵌套，父子关系影响布局。
- CSS 可以有 mask、filter、blend-mode、clip-path、pseudo element、gradient、background、webfont、canvas、SVG。

PPTX 是对象图系统：

- slide 上是若干 shape/text/image/chart/table/group。
- 文本必须在 text frame。
- shape fill、line、shadow、effect 的表达能力有限且由 OOXML 决定。
- PPTX 没有浏览器 layout engine。
- group、z-order、placeholder、theme、master、animation 的语义与 DOM 完全不同。

因此“任意 HTML→可编辑 PPTX”的本质困难不是工具不够聪明，而是：

> **源语言与目标语言不是同构的。**

如果强行转换，只有三种结局：

1. **全截图**：100% 保真，0% 可编辑。
2. **全 native 猜测**：可编辑，但视觉严重走样，且规则爆炸。
3. **人为约束 HTML**：可编辑，但牺牲 HTML 自由度。

终极方案必须接受三者之间的 trade-off，并做“智能分层”。

---

### 2.2 核心突破：Editable Fidelity Budget

建议引入一个概念：**可编辑性预算（Editable Fidelity Budget）**。

每个视觉对象在生成前就被打上属性：

```yaml
editability:
  level: text | data | style | replaceable | locked
  priority: 1-5
  fallback: native | vector | raster
  user_can_edit:
    - text
    - color
    - position
    - chart_data
```

示例：

| 对象 | 推荐处理 | 原因 |
|---|---|---|
| 标题/正文/脚注 | native text | 必须可编辑 |
| 数据图表 | native chart 或 editable vector group | 金融材料常要改数据 |
| 卡片背景/几何图形 | native shape | 可编辑且成本低 |
| 简单图标 | SVG path→freeform 或 icon font→shape | 可编辑/可换色 |
| 复杂渐变背景 | raster island | 可编辑收益低，保真更重要 |
| 装饰纹理/噪声/毛玻璃 | raster island | PPTX native 难表达 |
| 复杂插画 | raster island + hidden metadata | 保真为主，但可整体替换 |
| 表格 | native table 或 shape+text group | 金融场景高编辑优先级 |

这比“全部可编辑”更现实，也更符合金融机构真实使用：

- 金融机构真正会改的是：文字、数字、图表数据、页码、日期、标题、局部配色。
- 复杂装饰、背景纹理、插画通常不需要逐笔编辑，只需要可替换。

所以终极目标应是：

> **关键业务信息 100% 可编辑；视觉复杂区域可替换、可重建、可追溯；整体效果尽量保真。**

---

## 3. 多种实现方案脑暴

### 方案 A：继续强化 HTML→PPTX 直接转换

做法：

- 沿用 `ppt-builder`。
- 增加更多 `ppt-*` marker。
- 改进 converter，支持更多 CSS 到 PPTX 映射。

可新增 marker：

```text
.ppt-text
.ppt-rich-text
.ppt-rect
.ppt-oval
.ppt-line
.ppt-path
.ppt-icon
.ppt-chart
.ppt-table
.ppt-group
.ppt-raster
.ppt-bg
```

优点：

- 迁移成本最低。
- 预览即 HTML，开发体验好。
- 能快速解决大量实用场景。

缺点：

- HTML 仍是事实源，长期会被 DOM/CSS 细节绑架。
- 作者需要理解 marker 规则。
- IR 不清晰，难以做高级优化和跨后端。

适用定位：

> 作为 v1 工程实现可以采用，但不应作为终局架构。

---

### 方案 B：IR-first 双渲染架构（推荐）

做法：

定义一个 `deck.ir.yaml/json`，它是唯一真实源：

```yaml
slide:
  size: { w: 1280, h: 720 }
  objects:
    - id: title
      type: text
      role: headline
      box: { x: 80, y: 60, w: 720, h: 90 }
      text: "核心结论写成断言句"
      style: title.large
      editability: { level: text, priority: 5 }

    - id: card_1_bg
      type: shape
      shape: roundRect
      box: { x: 80, y: 190, w: 320, h: 260 }
      fill: token.surface.accent
      radius: token.radius.lg
      editability: { level: style, priority: 3 }

    - id: hero_texture
      type: rasterIsland
      source: "render://style/diffuse-emerge/background"
      box: { x: 0, y: 0, w: 1280, h: 720 }
      locks: ["position"]
      editability: { level: replaceable, priority: 1 }
```

然后写两个 renderer：

```text
IR → HTML preview
IR → PPTX native
```

优点：

- 彻底避免“HTML 转换猜测”。
- 可在 IR 层做 QA、约束、重排、内容校验。
- 可编辑策略可显式声明。
- 后续可以增加 Figma、SVG、PDF、图片等后端。
- 风格系统能以程序方式生成 IR，而不是生成一堆 HTML。

缺点：

- 初期工程量较大。
- 需要设计 DSL/schema。
- 很多 CSS 便利能力要在 IR layout engine 中重建或委托浏览器计算。

折中方式：

- IR 不必自己实现完整 layout。
- 可以允许 `layout: browser` 子树：IR 生成 HTML preview，浏览器计算布局后回填 bbox。
- 但导出对象必须来自 IR object，不从任意 DOM 猜测。

适用定位：

> 终极技能的主架构。

---

### 方案 C：HTML as View, IR as Source 的混合架构（最佳落地路线）

这是推荐的 v1→v2 演进路线。

做法：

1. 作者/AI 写 `deck.spec.yaml`。
2. spec 生成 HTML DOM，每个 DOM 节点都有 `data-ir-id`。
3. 浏览器负责布局，提取每个 `data-ir-id` 的 computed bbox/style。
4. PPTX renderer 根据 IR 类型生成 native/raster 对象。
5. HTML 只是 view，不是 source of truth。

```text
IR object(title) ──render preview──> <div data-ir-id="title" class="...">
       │                                      │
       └──────── PPTX renderer reads IR ◄──── bbox/style feedback from browser
```

关键区别：

- `ppt-builder` 是“HTML marked node → PPTX”。
- 终极版是“IR object → HTML node → layout feedback → PPTX object”。

这可以同时保留 HTML 布局能力与 IR 语义纯度。

适用定位：

> 最实际、最值得先做的路线。

---

### 方案 D：PowerPoint 原生优先，HTML 只做预览

做法：

- 完全以 `python-pptx` / OOXML / pptxgenjs 为主。
- 每个 layout/template 都是原生 PPTX 对象组合。
- HTML 只是把 PPTX 对象模拟出来预览。

优点：

- 可编辑性最强。
- 与 PPTX 文件格式最一致。

缺点：

- 视觉自由度低。
- HTML 的强布局能力用不上。
- 创意探索慢，开发成本高。

适用定位：

> 金融标准报告、数据型 deck 很适合；但不是“HTML 效果呈现到 PPTX”的最佳答案。

---

### 方案 E：借助 LibreOffice/PowerPoint COM/Office.js 做反向增强

做法：

- 先用 HTML/PDF/SVG 等生成视觉稿。
- 通过 LibreOffice 或 PowerPoint automation 插入对象、调整 theme/master、做 post-processing。
- 用 OOXML surgery 补 python-pptx/pptxgenjs 不支持的效果。

可解决：

- gradient fill。
- group shape。
- freeform path。
- theme/master。
- chart XML。
- table style。
- text autofit。
- shadow/effect。

优点：

- 能突破库的限制，直接操作 OOXML。
- 可逐步积累“高级 PPTX 能力”。

缺点：

- OOXML 复杂，调试成本高。
- 跨平台一致性难。
- 不应作为主作者ing模型，只适合作为后处理增强层。

适用定位：

> 作为 `PPTX Native Capability Layer`，不是顶层方案。

---

## 4. 推荐总体架构：Ultimate PPTX Builder

### 4.1 五层架构

```text
L0 Content Contract
  输入内容、数据、金融合规、叙事目标

L1 Narrative Topology
  hero / sequence / contrast / matrix / ranking / composition / causal / dialogue

L2 Layout Grammar
  grid / editorial / dashboard / specimen / timeline / quadrant / radial / cards / stage

L3 Visual Style Program
  tokens × typography × visual DNA × material constraints × SOTA moves

L4 PPTX Scene IR
  text / richText / shape / chart / table / icon / path / image / group / rasterIsland

L5 Render + QA Loop
  HTML preview / PPTX export / screenshot comparison / editability audit / design critique
```

### 4.2 Slide IR 对象类型建议

```yaml
object_types:
  text:
    editable: true
    supports: [runs, paragraph_spacing, bullets, alignment, vertical_anchor]

  shape:
    editable: true
    supports: [rect, roundRect, oval, line, freeform_path, fill, stroke, shadow]

  image:
    editable: replaceable
    supports: [crop, transparency, alt_text]

  icon:
    editable: partial
    supports: [svg_to_freeform, recolor, fallback_png]

  chart:
    editable: data
    supports: [bar, line, area, scatter, doughnut, combo]

  table:
    editable: data_text
    supports: [cell_text, fills, borders, merged_cells]

  group:
    editable: grouped
    supports: [children, transform, z_order]

  rasterIsland:
    editable: replaceable
    supports: [html_fragment, svg_fragment, generated_art, background_texture]
    metadata: [source_prompt, style_dna, regeneration_params]

  vectorIsland:
    editable: partial
    supports: [svg_paths_to_freeforms]
```

### 4.3 复杂 HTML 效果的处理策略

| HTML/CSS 效果 | PPTX 策略 | 可编辑性 |
|---|---|---|
| flex/grid 相对布局 | 浏览器计算 bbox，IR object native 输出 | 对象可编辑 |
| 多层 absolute 叠加 | 保留 z-order，native/raster 混合 | 部分可编辑 |
| text span 样式 | rich text runs | 可编辑 |
| gradient 背景 | 优先 PPTX gradient OOXML；复杂则 rasterIsland | 部分/不可编辑 |
| box-shadow | native shadow；复杂阴影 raster | 部分可编辑 |
| blur/glass/filter | rasterIsland | 可替换 |
| SVG icon | path→freeform；复杂 SVG raster | 部分可编辑 |
| chart canvas/svg | native chart 或 editable vector chart；复杂图 raster + data sidecar | 数据可编辑优先 |
| pseudo elements | 禁止承载关键信息；编译成真实 IR decoration | 可编辑 |
| mask/clip-path | 简单 clip 用 crop/path；复杂 mask raster | 部分可编辑 |
| blend-mode | rasterIsland | 不可编辑 |
| CSS animation | 静态关键帧 + 可选 PPT animation metadata | 静态可编辑 |

关键原则：

> 每个对象都要在生成时选择 `native / vector / raster`，而不是转换失败后临时降级。

---

## 5. 优秀 PPTX 风格问题：从“风格枚举”升级为“风格程序”

### 5.1 PPTX 视觉创意的可编程语法

一个优秀 PPTX 视觉风格不应该只是：

```yaml
style: fintech-blue
```

而应该是：

```yaml
style_program:
  tension:
    order_emergence: order
    surface_structure: structure
    authority_access: authority

  grammar:
    line: mechanical
    color_application: flat_plus_accent
    space: grid
    information_encoding: chart_typography
    depth: layered_flat

  tokens:
    palette: institutional_cool
    typography: cn_sans_serif_report
    radius: low
    density: medium_high

  sota_dna:
    - giant_thin_numeral_as_structure
    - controlled_grid_break
    - monochrome_value_ladder

  pptx_material_constraints:
    prefer_native: [text, charts, shapes, tables]
    allow_raster: [background_texture, hero_illustration]
    forbidden: [tiny_low_contrast_text, decorative_risk_warning]
```

这就是 `infographic-composer` 的思想迁移到 PPTX。

---

### 5.2 PPTX 专属的风格维度

PPTX 与海报/信息图不同，它有更强的“会议、汇报、可编辑、投屏”属性。因此风格系统应增加 PPTX 专属维度：

#### 1. Presentation Rhythm（整 deck 节奏）

- cover impact
- agenda calm
- body alternation
- data climax
- summary closure

不能每页都像海报。PPTX 需要“呼吸节奏”。

#### 2. Corporate Editability（企业可编辑性）

- 字体是否 Office 可用。
- 色板是否主题化。
- 图表是否可改数据。
- 页脚/免责声明是否 master 化。

#### 3. Slide Furniture（页内家具）

来自 `ppt-builder` 的好经验：footer rail、section tag、page index、corner motif 能让页面读起来像“完整作品”。

#### 4. Information Density（信息密度）

金融机构 PPTX 常常不可能像海报一样低密度。风格必须声明适配密度：

```yaml
supported_density:
  low: true
  medium: true
  high: conditional
rules:
  high_density:
    min_font: 10pt
    use_table_grid: true
    decoration_budget: <=12%
```

#### 5. Compliance Visibility（合规可见性）

风险提示、数据来源、免责声明不能是视觉残渣。应作为布局语法的一部分。

---

## 6. 风格延展性：如何让每种创意成为锚点，而不是一次性模板

### 6.1 借鉴 `infographic-composer` 的正交拆分

建议把 PPTX 创意拆成五个正交层：

```text
Narrative Topology：这页讲什么关系
Layout Grammar：信息如何占据空间
Visual DNA：这套视觉为什么一眼可辨
Token Pack：颜色、字体、圆角、线宽、阴影、图标风格
PPTX Material Strategy：哪些 native，哪些 raster，哪些 vector
```

同一个视觉 DNA 可以变出很多 deck：

```text
swiss-grid DNA
  × ranking topology → 排名页
  × matrix topology → 象限页
  × timeline topology → 时间轴页
  × contrast topology → 对照页
  × dashboard layout → 指标页
```

同一个 layout 也可以被不同 DNA 重皮肤：

```text
quadrant-map
  × swiss-grid → 机构策略象限
  × blueprint → 精密坐标蓝图
  × ink-wash → 山水方位图
  × glass-fintech → app 面板坐标
```

这才是可延展。

---

### 6.2 Style DNA 的准入标准

每个风格都必须回答：

1. **Base DNA**：去掉它，风格就不成立的最低特征是什么？
2. **SOTA DNA**：模型默认不会主动做、但顶级设计师会做的高级手法是什么？
3. **PPTX Translation DNA**：这些手法如何落到 PPTX 对象？
4. **Degradation Rule**：如果必须可编辑，哪些效果如何降级？
5. **Density Adaptation**：低/中/高密度下分别怎么变？
6. **Deck Rhythm Role**：它适合封面、正文、数据页、结尾，还是全 deck？

示例：`glass-fintech` PPTX 版。

```yaml
style: glass-fintech-pptx
base_dna:
  - translucent layered panels
  - soft luminous gradient background

sota_dna:
  - edge chromatic dispersion on glass borders
  - single consistent light source
  - background refraction offset behind panels
  - fine frosted grain at 3-5%

pptx_translation:
  native:
    - panel rectangles with transparency
    - text and numbers
    - simple charts
  raster_islands:
    - background light field
    - frosted grain overlay
    - complex refraction texture
  ooxml_enhancement:
    - optional gradient fill
    - soft shadow/effects

degradation:
  editable_mode:
    - replace refraction with translucent solid panels
    - keep text/chart native
  fidelity_mode:
    - rasterize full background and panel glow, keep text native
```

---

### 6.3 防止风格用一次就腻的机制

1. **每次生成随机化的不是主题名，而是参数**：
   - grid columns
   - motif placement
   - accent usage
   - density
   - hero scale
   - texture intensity
   - rhythm role

2. **每个 style 至少有 3 个 mode**：
   - restrained / expressive / data-heavy
   - light / dark / print-safe
   - cover / body / appendix

3. **每个 style 有 forbidden sameness checklist**：
   - 禁止每页同样三卡片。
   - 禁止每页同样大标题位置。
   - 禁止 accent 色每页同面积使用。
   - 禁止所有页面同一种背景纹理。

4. **Deck-level rhythm planner**：
   - 不是逐页孤立生成，而是先规划全 deck 节奏。

```yaml
deck_rhythm:
  01: impact_cover
  02: quiet_context
  03: data_density
  04: contrast_break
  05: visual_metaphor
  06: dashboard
  07: summary_closure
```

---

## 7. 自主优化：构建 PPTX 效果检验标准

### 7.1 四个评价门

#### Gate 1：Conversion Fidelity

问题：PPTX 是否忠实复现预览？

检测：

- HTML preview screenshot vs PPTX render screenshot。
- 元素是否移动、丢失、变色、字体变粗/变细。
- 文本是否换行变化、截断、溢出。

输出：

```yaml
fidelity_score: 0-100
issues:
  - object_id: title
    type: text_wrap_changed
    severity: high
    fix: widen_box_or_disable_wrap
```

#### Gate 2：Editability Audit

问题：该可编辑的是否真的可编辑？

检测：

- 标题/正文是否为 text frame，不是图片。
- 图表是否有 chart data，还是截图。
- 表格是否可编辑。
- 风险提示是否可编辑。
- rasterIsland 是否有 metadata，可重建/替换。

输出：

```yaml
editability_score: 0-100
critical_objects:
  title: native_text
  chart_1: native_chart
  caution: native_text
  background: raster_replaceable
```

#### Gate 3：Design Quality

问题：这是不是一页好 PPT？

维度：

- 信息层级：第一眼看什么？第二眼看什么？
- 叙事清晰：这页是在讲对比、流程、因果还是结论？
- 视觉张力：是否有一个 dominant element？
- 呼吸感：边距、留白、元素间距。
- 一致性：字体、色板、页脚、母版、节奏。
- 金融气质：是否克制、可信、专业。

#### Gate 4：PPTX Practicality

问题：金融机构真的能用吗？

检查：

- Office 字体可用。
- 16:9 标准尺寸。
- 投屏可读，最小字号不低于阈值。
- 打印/PDF 不丢失。
- 风险提示/数据来源在场。
- 文件大小可接受。
- 对象数量不过度爆炸。

---

### 7.2 自动迭代 loop

```text
1. Generate IR
2. Render HTML preview
3. Export PPTX
4. Render PPTX to PNG
5. Compare screenshot
6. Run editability audit on PPTX XML
7. Run visual critique prompt
8. Patch IR/style/layout
9. Repeat up to N rounds
10. Accept only if all gates pass
```

建议每轮输出 `qa_report.json`：

```yaml
scores:
  fidelity: 92
  editability: 88
  design: 84
  practicality: 95
blocking_issues:
  - slide 3 title wraps differently in PPTX
  - slide 5 chart is raster but marked priority 5 editable
non_blocking:
  - slide 2 footer too close to edge
next_patch:
  - widen title box by 6%
  - convert chart_5 to native chart
```

---

## 8. 终极技能目录建议

```text
ultimate-pptx-builder/
  SKILL.md

  references/
    architecture.md
    authoring-contract.md
    slide-ir-schema.md
    conversion-rules.md
    editability-policy.md
    visual-quality-rubric.md
    pptx-capability-matrix.md
    narrative-topologies.md
    layout-grammars.md
    style-lattice.md
    deck-rhythm.md
    financial-compliance.md

  styles/
    swiss-grid-pptx.md
    glass-fintech-pptx.md
    data-news-pptx.md
    archive-editorial-pptx.md
    ink-wash-pptx.md
    blueprint-system-pptx.md

  tokens/
    palettes.md
    typography.md
    office-fonts.md
    theme-mapping.md

  schemas/
    deck.schema.json
    slide-ir.schema.json
    style-program.schema.json
    qa-report.schema.json

  scripts/
    compile_spec_to_ir.py
    render_ir_html.py
    export_ir_pptx.py
    render_pptx_png.py
    compare_screenshots.py
    audit_pptx_editability.py
    evolve_deck.py

  templates/
    html_preview/
    pptx_master/

  examples/
    decks/
    styles/
    qa_reports/
```

---

## 9. 分阶段实现路线

### Phase 1：在 `ppt-builder` 上做增强，不重写一切

目标：快速形成可用 v1。

任务：

1. 扩展 authoring contract：
   - `.ppt-chart`
   - `.ppt-table`
   - `.ppt-icon`
   - `.ppt-group`
   - `.ppt-bg`
2. 引入 `data-editability-priority`。
3. 增加 `editability audit`。
4. 增加 `conversion policy`：哪些对象 native，哪些 raster。
5. 加强 QA report。

收益：

- 立即提升现有 HTML→PPTX 能力。
- 保持现有工具链可跑。

风险：

- 仍有 HTML-first 技术债。

---

### Phase 2：引入 IR，但 HTML 仍承担布局

目标：进入推荐混合架构。

任务：

1. 定义 `slide-ir.schema.json`。
2. 写 `IR → HTML` preview renderer。
3. 每个 HTML 节点带 `data-ir-id`。
4. 浏览器回填 bbox。
5. `IR + bbox → PPTX`。
6. 让现有 `ppt-*` contract 逐步变成 IR type。

收益：

- 语义源独立。
- 风格程序可以生成 IR。
- 转换更可控。

---

### Phase 3：风格程序化

目标：解决创意延展性。

任务：

1. 建 `style-lattice.md`。
2. 每个 style 拆成：
   - tension
   - grammar
   - tokens
   - base DNA
   - SOTA DNA
   - PPTX translation
   - degradation rules
3. 建 `layout-grammars.md`。
4. 建 `deck-rhythm.md`。
5. 用 `style_program + topology + content` 生成 IR。

收益：

- 不再陷入风格枚举。
- 同一风格能生成丰富变体。

---

### Phase 4：自主优化闭环

目标：让技能越用越强。

任务：

1. `evolve_deck.py` 一键循环。
2. 自动 screenshot comparison。
3. 自动 XML editability audit。
4. 视觉质量 rubric prompt。
5. 每次 bug 自动追加 conversion rule proposal。
6. 每次优秀风格实践沉淀 style recipe。

收益：

- 技能具备自我改进机制。
- 每次项目都积累规则，而不是一次性生产。

---

## 10. 最重要的设计原则

### 原则 1：不要承诺“任意 HTML 完美可编辑转换”

正确承诺是：

> **通过 IR 与可编辑性预算，实现关键业务信息可编辑、复杂视觉保真可替换、整体效果高一致。**

这是可信的，也是可落地的。

### 原则 2：HTML 不是敌人，但不能是唯一真相

HTML 的优势是布局与预览。PPTX 的优势是交付与编辑。IR 才是两者之间的共同真相。

### 原则 3：复杂视觉不要硬 native 化

有些效果就应该 raster：毛玻璃、噪声、复杂插画、blend-mode。问题不是 raster，而是：

- 是否把关键文字也 raster 了？不能。
- 是否有 metadata 可重建？必须有。
- 是否用户真的需要编辑它？多数不需要。

### 原则 4：风格是生成程序，不是模板列表

每个 style 必须有：

- Base DNA
- SOTA DNA
- tokens
- layout compatibility
- density modes
- PPTX translation strategy
- degradation rule

否则它只是一个名字。

### 原则 5：QA 不只是看像不像，还要看能不能改

终极 PPTX 的质量分数必须同时包含：

```text
视觉保真 × 可编辑性 × 叙事质量 × 金融可用性
```

---

## 11. 推荐的最终答案

如果要创建“终极 PPTX 构建技能”，我建议不要把它命名为 `html-to-pptx`。那会把问题锁死在错误层级。

更好的定位是：

> **Ultimate PPTX Builder: IR-first editable presentation system**

一句话描述：

> 用叙事拓扑与风格程序生成 PPTX Scene IR，以 HTML 做高保真预览，以 PowerPoint 原生对象做可编辑导出；通过 native/vector/raster 混合策略、可编辑性预算和自动 QA 闭环，在金融机构可用的标准 PPTX 中尽可能复现高级视觉设计。

最小可行版本不需要一步到位。可以从 `ppt-builder` 出发，但路线要明确：

```text
ppt-builder marker contract
  → typed IR objects
  → dual renderer
  → programmable style system
  → autonomous QA/evolution
```

这条路比“继续修 HTML 转换规则”更难，但它是对的。继续在任意 HTML→PPTX 上打补丁，只会得到越来越厚的例外规则；引入 IR 与可编辑性预算，才有可能形成真正可复利的技能。
