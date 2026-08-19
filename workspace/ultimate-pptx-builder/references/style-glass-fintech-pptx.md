# Glass Fintech PPTX 样式程序

## 目的

`glass-fintech-pptx` 是 `ultimate-pptx-builder` 的第一个端到端样式锚点。它聚焦于把一种样式做深，而不是许多浅层预设。

## 视觉论点

金融级驾驶舱：深色机构画布、半透明原生玻璃面板、青色/紫色光效强调、指标卡片，以及持久的原生风险栏。

## 可编程语法

- 画布：深海军蓝全幻灯片原生形状。
- 深度：内容背后的低不透明度强调光球，导出为原生形状。
- 玻璃：带高光描边和微妙阴影的半透明圆角矩形。
- 信息：指标卡片、行动栏、来源/风险文本和正文叙事块。
- 约束：任何业务关键内容都不得进入栅格。

## PPTX 材料策略

| Material | PPTX representation | Notes |
|---|---|---|
| Background | 原生矩形 | MVP 中不栅格化 |
| Glow orb | 带不透明度的原生椭圆/矩形替代物 | 模拟模糊，不承诺真实模糊 |
| Glass card | 带不透明度 + 描边 + 阴影的原生 roundRect | 可编辑填充/描边/位置 |
| Metric value | 原生文本 | priority 5 |
| Risk rail | 原生形状 + 原生文本 | priority 5 文本 |
| Financial chart | 原生形状/文本组成的可编辑矢量组 | MVP 路径；尚非 Office chart XML，但不是栅格 |

## 接受标准

- `examples/glass-fintech-pptx.style.json` 具有 Base DNA 和至少两个 SOTA DNA 动作。
- `examples/glass-fintech-showcase.contract.json` 编译为至少三张幻灯片。
- 已编译 IR 对该 showcase 不包含 `rasterIsland` 对象。
- 所有标题/正文/指标/风险文本保持原生，priority >= 4。
- 至少一个金融图表保持 priority 5 并导出为 `editable-vector-chart`。
- 生成 HTML 预览、PPTX 导出、视觉保真度报告和 QA 报告。
- showcase 的视觉保真度分数必须 >= 88。
- QA 可编辑性分数必须 >= 95。

## 运行命令

```bash
python3 scripts/validate_glass_showcase.py
python3 scripts/validate_glass_benchmark.py
```

## 发布与阻断

发布条件：两个命令均返回 pass，且 `export-report.json`、`qa-report.json`、视觉保真报告存在。

阻断条件：关键文本进入 raster、金融图表未按 priority 5 物化、视觉保真或可编辑性低于接受标准、showcase/benchmark 缺少正式报告。
