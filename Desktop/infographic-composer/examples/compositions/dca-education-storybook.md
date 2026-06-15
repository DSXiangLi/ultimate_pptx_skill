# 配方存档 · 定投科普 × 导览绘本（S4 投教）
> 示范契约 v2 的 sequence 拓扑：步骤型投教内容。

```yaml
recipe:
  scenario: S4 投教
  topology: sequence（axis: process）
  narrative: N1 guided-tour（线性路线）或 N4 timeline
  style: storybook-guide / tokens: {palette: P02, typography: T02}
  open_elements:
    metaphor: 基金语义内生——"定投登山营"：固定节奏的补给点=定期扣款，
      坏天气日=下跌日（买入份额更多，站点牌反直觉知识点），山顶=长期目标
    character: 参考 examples/characters/owl-docent
  contract_fill_pattern:
    TITLE: "定投是怎么回事 | 4 步看懂定期定额"
    nature: steady
    BODY.sequence.stages: [设定目标与金额, 选定扣款日, 下跌时发生什么(climax), 长期复盘节奏]
    DATA: 可空（无真实数据则不放示意数字）
    ASIDE: "微笑曲线"小知识
    CAUTION: "定投不保证盈利，市场有风险…"（必填）
    META: "出品方 | 仅供投教参考，不构成投资建议 | 日期"
  notes: climax 站点视觉放大；全图不得出现具体产品代码（投教中立）
```
