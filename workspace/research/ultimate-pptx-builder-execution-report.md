# Ultimate PPTX Builder 执行落地报告

## 结论

已将“终极 PPTX 构建技能”从调研方案推进到一个可验证、可安装、可执行的 MVP skill，并继续按优先级完成了 P0 视觉保真闭环的第一版；随后按“一个视觉风格端到端做到极致”的策略，落地并持续强化首个深度样板 `glass-fintech-pptx`，已支持 priority-5 金融图表、editable vector table，并完成一套模拟真实用户输入的 15 页投委会 benchmark deck。

核心路径从：

```text
Content Contract → Slide IR → HTML Preview → PPTX Export → QA Report
```

升级为：

```text
Content Contract → Slide IR → HTML Preview → PPTX Export → Visual Fidelity → QA Report
```

HTML 只作为预览渲染目标；Slide IR 是唯一源头；PPTX 导出由 IR 直接生成，关键文本保持原生可编辑。视觉保真现在已有真实渲染链：IR reference PNG 对比 LibreOffice 渲染出的 PPTX PNG。

## 产物位置

### 工作区版本

`/home/lixiang/workspace/ultimate-pptx-builder`

### 已安装 Hermes 用户技能版本

`/home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder`

> 当前会话的 skill loader 可能不会立刻列出新 skill；新会话会重新加载磁盘技能。

## 已完成阶段

| Phase | 内容 | 验收 |
|---|---|---|
| Phase 0 | skill 骨架、references、schemas、示例、validator | PASS |
| Phase 1 | content contract → Slide IR 编译器 | PASS |
| Phase 2 | IR → HTML preview renderer + `data-ir-id` traceability | PASS |
| Phase 3 | 无依赖 IR → PPTX 原生文本/形状导出 MVP | PASS |
| Phase 4B | IR reference PNG vs LibreOffice-rendered PPTX PNG 视觉保真闭环 | PASS |
| Phase 4 | QA report 使用实测 fidelity/editability/design/practicality | PASS |
| Style Showcase | `glass-fintech-pptx` 三页端到端样板，含视觉 QA 修复闭环 | PASS |
| Native Chart | priority-5 金融图表以 editable vector chart 输出，不走 raster | PASS |
| Native Table | 高密度金融表格以 editable vector table 输出，不走 raster | PASS |
| 15P Benchmark | 模拟真实用户输入，生成15页投委会资产配置benchmark，覆盖多种内容呈现方式 | PASS |
| Install | 安装到默认 Hermes profile 用户技能目录 | PASS |

## 最终验证命令

```bash
cd /home/lixiang/workspace/ultimate-pptx-builder
python3 scripts/validate_skill.py

cd /home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder
python3 scripts/validate_skill.py
```

两边最终输出均为：

```text
PASS required files: 41 present
PASS skill frontmatter
PASS acceptance criteria present
PASS JSON parseability
PASS minimal IR policy
PASS style policy
PASS Phase 1 compiler output
PASS Phase 2 HTML traceability
PASS Phase 3 PPTX export audit
PASS Phase 4B visual fidelity
PASS Phase 4 QA report
PASS glass-fintech showcase
PASS glass-fintech benchmark
ALL CHECKS PASSED
```

当前基础样例验证指标：

```text
visual_score= 97.26
qa_fidelity= 97.26
qa_has_visual= True
```

当前 glass-fintech 深度样板指标：

```text
glass_visual_score= 95.61
glass_editability= 100.00
glass_qa_fidelity= 95.61
chart_actual= editable-vector-chart
slides=3

benchmark_visual_score= 94.89
benchmark_editability= 100.00
benchmark_release= pass
benchmark_editable_vector_charts= 4
benchmark_editable_vector_tables= 2
benchmark_slides= 15
```

## 当前 MVP 能力

1. **终极转换问题的落地起点**
   - 不承诺任意 HTML 完美转 PPTX。
   - 使用 Slide IR 作为源头，同时生成 HTML preview、PPTX 和视觉对比图。
   - 关键文本以 native PowerPoint text run 导出。
   - 复杂 rasterIsland 先以可替换占位方式处理，并在报告中明确记录。

2. **优秀 PPTX 风格问题**
   - 引入 style program，而不是风格枚举。
   - 要求 Base DNA、SOTA DNA、PPTX material strategy、degradation rules。
   - 已完成首个深度风格：`glass-fintech-pptx`。
   - `glass-fintech-pptx` 不是静态模板，而是一条可验证生成线：style program → contract → IR → HTML → PPTX → visual fidelity → QA。
   - 本轮已加入金融图表与金融表格路径：contract chart/table semantics → IR `type=chart` / `type=table` → HTML/Pillow/PPTX 同构渲染 → export audit `editable-vector-chart` / `editable-vector-table`。
   - 已完成 15 页投委会 benchmark：模拟真实用户输入、真实金融叙事、15 个 slide-level narrative job，并覆盖 table/matrix/process/timeline/scenario/quote/compliance/action 等内容形态。

3. **灵活性和延展性**
   - 视觉语言被拆成 tension、grammar、tokens、base_dna、sota_dna、material strategy。
   - 后续可以增加风格程序，而不是复制模板。

4. **自主优化**
   - 已有 `qa-report.json` 标准输出。
   - 已有 editability audit、traceability、practicality/design heuristic。
   - 已接入 Phase 4B 视觉保真分数，QA 的 `scores.fidelity` 来自真实图像对比。
   - 仍需升级为 HTML/browser screenshot vs PPTX render 的更真实对比。

5. **开发学习记录机制**
   - 新增 `docs/learning/README.md`。
   - 新增 `docs/learning/phase4b-visual-rendering.md`。
   - 新增 `docs/learning/glass-fintech-showcase.md`，现包含 glass showcase、native chart/table、15页 benchmark 与视觉 QA 修复闭环。
   - `SKILL.md` 已写入规则：修改已知问题区域前先读 `docs/learning/`。

## 关键文件

- `SKILL.md`：技能入口与工作流。
- `README.md`：验证入口与状态。
- `references/architecture.md`：IR-first 架构。
- `references/acceptance-matrix.md`：分阶段验收矩阵。
- `references/slide-ir-schema.md`：IR 设计。
- `references/style-program.md`：风格程序设计。
- `references/editability-policy.md`：编辑性预算与阻断规则。
- `references/qa-loop.md`：QA 闭环。
- `references/phase4b-visual-fidelity.md`：视觉保真闭环设计。
- `references/style-glass-fintech-pptx.md`：首个深度风格锚点设计与验收标准。
- `docs/learning/phase4b-visual-rendering.md`：Phase 4B 开发中发现并解决的问题。
- `docs/learning/glass-fintech-showcase.md`：glass showcase 开发中发现并解决的问题。
- `scripts/compile_spec_to_ir.py`：Phase 1 编译器。
- `scripts/render_ir_html.py`：Phase 2 HTML preview。
- `scripts/export_ir_pptx.py`：Phase 3 PPTX exporter MVP，含 editable vector chart/table 输出。
- `scripts/render_ir_png.py`：IR reference PNG 渲染器。
- `scripts/render_pptx_png.py`：PPTX → PDF → PNG 渲染器。
- `scripts/compare_slide_images.py`：图像差异比较器。
- `scripts/run_visual_fidelity.py`：Phase 4B 视觉闭环入口。
- `scripts/run_qa.py`：Phase 4 QA report。
- `scripts/validate_glass_showcase.py`：glass-fintech 端到端样板验收。
- `scripts/validate_glass_benchmark.py`：glass-fintech 15页投委会benchmark验收。
- `scripts/validate_skill.py`：统一验收入口。

## 下一步建议

### P0-next：升级为真正 HTML/browser screenshot 对比

当前 Phase 4B 已经有真实 PPTX 渲染和图像 diff，但 reference 仍是 IR/Pillow，不是浏览器截图。下一步应补：

- HTML preview screenshot。
- browser screenshot vs PPTX rendered PNG。
- pixel/SSIM/object-level diff。
- AI 视觉审稿。
- 自动生成 fix list 并回写 IR。

### P1：把 15页 benchmark 接入更强 QA：browser screenshot + AI 审稿闭环

15页投委会 benchmark 已完成。下一步不要急着扩第二风格，应继续提高这一套 benchmark 的评审强度：

- 使用浏览器截图作为 HTML preview reference，替代当前 Pillow reference。
- 加入 object-level diff：标题、表格、chart、风险提示分别打分。
- 固化 AI 视觉审稿 rubric：叙事一致性、数据口径、金融正式感、投屏可读性。
- 生成自动 fix list，并回写 content contract / IR。
- 增加真实用户数据替换模式：从 CSV/JSON 投研数据生成同一 deck。

### P2：升级 PPTX exporter

- rasterIsland 真正图片嵌入。
- SVG/vectorIsland → PPTX freeform 或 EMF/SVG embedding。
- Office chart XML + embedded workbook data（在当前 editable vector chart 基础上升级）。
- native table。
- theme/master/layout support。

### P3：扩展 style program library

只有当 `glass-fintech-pptx` 的真实 benchmark 稳定后，再扩展新风格。候选包括：

- `glass-fintech-pptx`
- `data-news-pptx`
- `institutional-dark-terminal-pptx`

每个风格必须通过 Base DNA + SOTA DNA + material strategy + degradation rules 验收。

### P4：建立更多真实 deck benchmark

用 3 类真实金融材料压测：

- 高密度研究报告摘要。
- 投委会策略汇报。
- 产品/基金月报。

每类至少 5 页，记录 fidelity/editability/design/practicality 分数。
