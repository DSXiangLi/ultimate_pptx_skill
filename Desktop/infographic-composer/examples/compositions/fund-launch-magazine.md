# 配方存档 · 新基金发行 × 杂志风 N2（S3 宣传）
> 示范 magazine-editorial × specimen-portrait：版式张力作为主视觉，无隐喻无角色。

```yaml
recipe:
  scenario: S3 宣传（新发）
  topology: hero（object：基金产品为主角）
  narrative: N2 specimen-portrait
  style: magazine-editorial / tokens: {palette: P13 editorial-luxury, typography: T05}
  open_elements:
    typography_impact_card:
      hero_size: 96pt     # 基金名称超大显示
      headline_size: 64pt # 发行主题行
      section_size: 12pt  # 栏标签全大写
      body_size: 10pt
      caption_size: 6pt
      weight_contrast_anchors: ["基金名 font-weight 100 极细衬线", "核心数据 font-weight 900 粗黑并置"]
      whitespace_plan: ["封面右侧 40% 纯留白（主动设计）", "正文栏宽 60%，右侧留白率约 35%"]
      asymmetry_rule: "文字栏偏左，数据牌居中偏右，两者之间 metallic 细线分隔"
      accent_discipline: "accent #D4AF37 仅用于：基金代码下划线、数据分隔细线"
  contract_fill_pattern:
    TITLE: masthead 小 logo + 期号（如"新发特辑 Vol.01"）
    DATA: {primary: 基金份额/认购期, secondary: 最低认购金额, form: object}
    BODY.points: [策略方向（2行）, 拟任基金经理（1行简介）, 目标客群（1行）] # ≤3项保持留白
    VOICE: 基金经理一句话（<30字，真实提供才填）
    LIST: 可选：同系列已发产品（name+code+成立以来表现+说明"过往业绩不代表未来"）
    CAUTION: "基金有风险，投资须谨慎。本材料不构成投资建议。" # 必填完整
    META: "出品方 | 销售机构请查阅基金合同 | 日期"
  notes: 合规最严；产品名称须与基金合同完全一致；不得出现收益预期数字
```
