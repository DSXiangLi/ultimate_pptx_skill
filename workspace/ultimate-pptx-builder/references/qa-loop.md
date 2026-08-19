# QA 发布循环契约

## 适用范围

本文件定义 PPTX 产物发布前的 QA 命令、报告和阻断条件。发布判定来自脚本报告，不来自人工 checklist。

## 输入产物

```text
<workdir>/build/deck.ir.json
<workdir>/build/deck.pptx
<workdir>/verification/export-report.json
<workdir>/verification/visual-fidelity-report.json
<workdir>/verification/layout-report.json
<workdir>/verification/qa-report.json
```

## 必跑命令

```bash
python3 scripts/check_pptx_package.py <workdir>/build/deck.pptx

python3 scripts/run_visual_fidelity.py \
  <workdir>/build/deck.ir.json \
  <workdir>/build/deck.pptx \
  <workdir>/verification/visual-fidelity-report.json \
  --workdir <workdir>/visual-fidelity

python3 scripts/check_layout_safety.py \
  <workdir>/build/deck.ir.json \
  --report <workdir>/verification/layout-report.json

python3 scripts/run_qa.py \
  <workdir>/build/deck.ir.json \
  <workdir>/verification/export-report.json \
  <workdir>/verification/qa-report.json \
  --pptx <workdir>/build/deck.pptx \
  --visual-report <workdir>/verification/visual-fidelity-report.json
```

复杂组件页追加：

```bash
python3 scripts/check_component_layout_contract.py \
  <workdir>/build/deck.ir.json \
  --report <workdir>/verification/component-layout-report.json
```

## QA 报告字段

`qa-report.json` 必须匹配 `schemas/qa-report.schema.json`，至少包含：

```yaml
deck_id: string
scores:
  fidelity: number
  editability: number
  design: number
  practicality: number
blocking_issues: []
objects_audited: []
release_decision: pass | fail | pass_with_accepted_exceptions
```

## 发布门禁

| Gate | 发布条件 |
|---|---|
| package | Office package 结构通过 |
| fidelity | 视觉保真报告存在，分数达到当前阈值或例外已记录 |
| editability | priority>=4 文本和关键数据不被 rasterized |
| layout/text | `layout-report.json.release_decision == pass` 且 `blocking_count == 0` |
| design | 无阻断级视觉层级、拥挤、遮挡、组件错位问题 |
| practicality | 来源/风险存在，字号、文件大小、对象数量适合 Office 工作流 |
| manifest | final manifest 写入 PPTX、IR、render、report 路径和 release decision |

## 阻断代码族

| Code family | 处理方式 |
|---|---|
| package/XML failure | 修复 exporter/package 关系后重跑全部 QA |
| critical text rasterized | 修复 render policy/exporter，禁止用截图保真掩盖 |
| visual fidelity drift | 读取 diff/crops，定位 IR/HTML/PPTX renderer 责任 |
| layout/text blocker | 修复 IR/layout grammar 或对应 checker，不只改当前坐标 |
| component contract failure | 修复 component contract、slot 或 density fallback |
| missing source/risk | 回到 content contract 补齐业务字段 |

## 修复并重新验证

每次修复后只接受同一命令链重新通过的产物。若修复改动影响 style program、IR schema、exporter、QA gate 或 runtime 文档，最后运行：

```bash
python3 scripts/validate_skill.py
```
