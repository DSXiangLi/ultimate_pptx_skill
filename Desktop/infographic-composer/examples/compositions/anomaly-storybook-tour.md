# 配方存档 · 异动解读 × 导览绘本
> 原"导览绘本风金融异动模板"的新架构存档。遇到"向大众解释一次市场/业务异动"类需求可直接复用微调。

```yaml
recipe:
  scenario: S1 解读
  topology: hero
  narrative: N1 guided-tour（立体上升路线）
  style: storybook-guide / preset=bright-optimistic（涨）或 caution-narrative（跌）
  open_elements:
    metaphor: 按 HERO.nature 推理；positive 参考 examples/metaphors/rocket-launch 或 mountain-trail，adverse 参考 roller-coaster
    character: 参考 examples/characters/robot-guide
  contract_fill_pattern:           # 异动类内容的典型契约填法
    TITLE: "<标的>上涨/回调之旅 | <核心概念>"
    HERO: {form: number, value: "<涨跌幅>", support_value: "<偏离值>", nature: 按涨跌定}
    POINTS: [政策面, 基本面, 情绪面]   # 各 15-30 字（本 style 预算紧凑）
    VOICE: 分析师观点 → 角色中途对话气泡
    LIST: 关注标的（名称+代码+趋势+短注）
    ASIDE: 核心概念小百科（如"三底共振"的历史统计）
    CAUTION: 政策落地与持续性风险（必含）
    META: "数据来源 | 风险提示 | 仅供参考 | 日期"
  notes: 站点编号即 POINTS.id；HERO 置于路线高潮点（顶峰/目标轨道）
```
