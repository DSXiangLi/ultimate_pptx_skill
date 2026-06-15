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
