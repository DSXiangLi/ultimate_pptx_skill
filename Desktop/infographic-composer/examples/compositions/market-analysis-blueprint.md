# 配方存档 · 多因素异动解读 × 蓝图 N1（S1 解读·机构版）
> 示范 blueprint-system × causal/等轴测分层剖面：因果机制的最强可视化。

```yaml
recipe:
  scenario: S1 解读（机构/专业受众）
  topology: causal（因果链：政策→基本面→情绪→结论）
  narrative: N1 guided-tour（分支汇聚路线，视觉上即等轴测剖面的层间连线）
  style: blueprint-system / tokens: {palette: P19 blueprint-dark, typography: T07}
  open_elements:
    glow_hierarchy_card:
      level_1_hero: "HERO 结论数值（+2.42%）：outer glow 8px blur 15px #00D9FF opacity 90%"
      level_2_structure: "等轴测剖面轮廓线+面板边框：outer glow 4px blur 10px #00D9FF opacity 70%"
      level_3_label: "callout 标注线+文字框：outer glow 2px blur 5px #9CA3AF opacity 40%"
      level_4_ambient: "背景网格：无发光，仅 #1F2937 颜色区分"
      glow_color_per_element: {surface_layer: "#00D9FF", policy_layer: "#FFD700", fundamental_layer: "#A78BFA", sentiment_layer: "#00D9FF(淡)", conclusion: "#FFD700(强)"}
    isometric_layers:
      - {id: 1, name: "地表层 SURFACE", concept: "DATA涨跌幅", visual: "K线轮廓像素化", glow: "#00D9FF"}
      - {id: 2, name: "政策层 POLICY", concept: "POINTS-01", visual: "文件图标+连线向下", glow: "#FFD700"}
      - {id: 3, name: "基本面层 FUNDAMENTAL", concept: "POINTS-02", visual: "数据流管道", glow: "#A78BFA"}
      - {id: 4, name: "情绪层 SENTIMENT", concept: "POINTS-03", visual: "波动密度线", glow: "#00D9FF淡"}
      - {id: 5, name: "共振层 RESONANCE", concept: "BODY.conclusion", visual: "三层交汇点高亮", glow: "#FFD700强"}
  contract_fill_pattern:
    TITLE: "CS食品饮指数异动解读 | MARKET ANOMALY ATLAS | 2026.05.29"
    nature: positive
    topology: causal
    BODY.causal:
      nodes: [{id:1,title:"促消费政策"}, {id:2,title:"业绩触底修复"}, {id:3,title:"估值历史低位"}]
      links: [{from:1,to:5,relation:"政策催化"}, {from:2,to:5,relation:"基本面支撑"}, {from:3,to:5,relation:"情绪反转"}]
      conclusion: {title:"三底共振", body:"政策底+业绩底+估值底三重确认，配置价值显现"}
    DATA: [{label:"涨幅", value:"+2.42%", direction:"↑", role:"primary"}, {label:"偏离", value:"4.14%", role:"secondary"}]
    VOICE: {quote:"当前是宏观消费、板块业绩、市场情绪的三底共振位置…", attribution:"沙川 | 基金经理"}
    LIST: [{name:"白酒龙头", tag:"600519", status:"↑", note:"流动性修复"}...]
    CAUTION: "市场有风险，投资须谨慎。本内容不构成投资建议。"
    META: "数据来源：Wind | 编制：日期"
  notes: callout标注线 ≥ 8条；左侧图例面板 + 2个小剖面面板（政策传导剖面+估值底部剖面）
```
