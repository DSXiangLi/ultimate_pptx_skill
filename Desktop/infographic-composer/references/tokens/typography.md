# 字体包 Typography Packs

字体从 style 中独立为 token。包只定**家族与气质**；具体字号/字重预算仍由 style 的槽位呈现表规定。

## 通用硬规则（所有包）
- 单图字体家族 ≤3（标题族+正文族+数据族）
- 数据/代码一律等宽（Mono）族
- 中文手写/书法体仅限标题与批注，**正文禁用**（可读性）
- 正文中文字号 ≥6pt（移动端阅读下限随 style 预算）

## 包目录

### T01 handwritten-warm（手写温暖）
标题：中文手写/毛笔书法感（如站酷快乐体/演示春风楷气质）｜正文：圆润无衬线（思源黑体 Normal/苹方）｜数据：JetBrains Mono / Roboto Mono
气质：日记、手账、陪伴信 ｜ 适配：sketchbook-journal、storybook-guide

### T02 rounded-friendly（圆润友好）
标题：圆体（如思源圆体/汉仪润圆）｜正文：圆体细字重或思源黑体｜数据：Roboto Mono
气质：绘本、投教、儿童友好 ｜ 适配：storybook-guide

### T03 serif-classic（古典衬线）— classical-oil locked
标题：衬线（思源宋体/Noto Serif），可小型大写+字距加宽｜正文：衬线常规｜数据：衬线数字或 Mono 细体
气质：铜版印刷、档案、郑重 ｜ 适配：classical-oil 专属

### T04 condensed-data（窄身数据）— perler-archive 默认
标题/正文：Roboto Condensed / Helvetica Neue Condensed｜数据：Roboto Mono
气质：档案、理性、数据密集 ｜ 适配：perler-archive

## 新增包规则
注明三族构成、气质关键词、适配 style；手写族必须声明"仅标题批注"；存入本文件 T05 起递增。

### T05 display-editorial（杂志展示体）
标题：超大 Display 衬线（Didot/Bodoni 气质：纤细笔画+粗笔画极端对比）或几何无衬线（Futura/Avant Garde 气质）；**全大写+字距加宽（letter-spacing 0.2-0.4em）**；副题：极细字重（100-200）无衬线，字距加宽；正文：易读衬线（Garamond 气质）或人文无衬线（Helvetica Neue Light）行距 1.6；数据：超大细线数字（font-weight 100，字号是正文 6-10×）；标注：斜体小字（caption）。
核心原则：字号跨度≥8×，字重跨度≥6×（100→900），留白是版面的主动设计元素。
气质：Vogue/Elle/Kinfolk｜适配：magazine-editorial

### T06 pixel-8bit（像素点阵体）
标题/正文：像素字体（Press Start 2P / Silkscreen 气质），**所有字号为基准像素单位的整数倍（8/16/24/32px）**；中文：融合像素点阵（Fusion Pixel Font 气质），正文最小 16px（点阵对齐）；数据：等宽像素字，闪烁效果作为设计语言；所有文字带 1-2px 深色像素描边。
核心原则：禁止抗锯齿；所有字号对齐像素网格；字距为像素单位整数。
气质：Game Boy/FC/像素论坛｜适配：pixel-game

### T07 technical-mono（技术等宽体）
标题：粗黑无衬线全大写（字距加宽）；正文/注解：等宽字体（JetBrains Mono / Roboto Mono）；层级标签：小型大写+字距加宽；数据：等宽大号，正文 2-4×；标注线文字：6-8pt 等宽细字。
核心原则：对齐感优先（等宽确保数据列对齐）；字号层级：6/7/8/10/12pt 严格五档。
气质：工程图纸/Bloomberg终端/指挥中心｜适配：blueprint-system
