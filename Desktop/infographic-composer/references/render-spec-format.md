# 渲染规格格式 Render Spec Format

render spec 是本技能的**最终交付物**：一份可直接送去渲染（图像模型 / SVG / HTML / 设计师）的绘图指令。
设计目标：**任何文字都逐字落在槽位里；文图分层；用户改一处只影响一处。**

## 顶层结构（YAML）

```yaml
render_spec:
  meta:
    project:            # 项目名
    scenario: <S1解读|S2陪伴|S3宣传|S4投教>   # 业务场景，决定必填槽位与合规清单
    topology: <hero|parallel|sequence|causal|contrast>
    contract_version:   # 本次契约摘要的标识/日期
    style: <styles/ 下的包名>
    tokens: {palette: <P 包 id>, typography: <T 包 id>}   # 按 style 的绑定模式选定
    narrative: <N1-N6>
    canvas: {ratio, width, height, orientation}

  # ============ A. 确定层：文字与版式（用户最常修改的部分） ============
  slots:
    - id: TITLE
      position:        # 用相对描述：区域 + 占比，如"顶部居中，宽 60%，高 10%"
      treatment:       # 引用 style 槽位呈现表的形态名，如"导览牌式标题条 + 手绘波浪饰线"
      text:
        main: "……"     # 逐字写明，渲染时原样使用
        sub: "……"
        date: "……"
      typography:      # 字号/字重从 style 槽位表取；族从 tokens.typography 取；色从 tokens.palette 的角色名取
    - id: HERO
      ...
    - id: BODY-01      # BODY 的每个节点/卡片/阶段独立成槽（命名按拓扑：CARD-01/STAGE-01/NODE-01/SIDE-A-01）
      anchor: <隐喻 mapping 中对应的场景锚点>   # 与 B 层的连接点
      ...
    - id: DATA / VOICE / LIST / ASIDE / CAUTION / META
      ...              # 未使用的可选槽位写 `omitted: 用户未提供`

  # ============ B. 生成层：插画与开放元素（重画时不动 A 层） ============
  illustration:
    scene:             # 隐喻卡全文（N1/N4）或主体描述全文（N2）或主图场定义（N3）
    character:         # 角色卡全文（如适用），含各出场点的位置/尺寸/表情
    route:             # 动线描述（如适用）：形态/颜色/宽度/waypoint 规格
    atmosphere:        # 所选 preset 的光照与质感要求，从 style 抄具体值
    note: "插画层不渲染任何文字；所有文字由 A 层槽位承载"

  # ============ C. 负面约束（style 与开放元素的 must_avoid 合并） ============
  must_avoid:
    - ...

  # ============ D. 渲染附注 ============
  render_notes:
    layering: "建议分层渲染：先生成 B 层插画（prompt 中明确'画面中无任何文字'），再以确定方式叠加 A 层文字版式；如一体生成，固定 seed 并整份提交本 spec"
    edit_rules: "改文案→只改 A 层对应槽位；换插画→只改 B 层；换风格→保留 A 层 text 字段，按新 style 重写 treatment/typography"
```

## 硬性规则

1. **text 字段逐字完整**——不写"此处放第一个要点"，写要点本身。
2. **A 层不含画法，B 层不含文案**。两层唯一的连接是 `anchor` 字段（槽位附着在场景的哪个元素旁）。
3. 所有尺寸/字号写**具体值**（从 style 槽位表抄）；颜色写"角色名+色值"双写（如 accent #FFD93F），便于换包时全局替换。
4. 位置用相对语言（区域+百分比），不用绝对像素（除画布本身），便于跨尺寸复用。
5. spec 必须自包含：渲染方不读 style 文件也能照做。
6. 交付时附一段 ≤5 行的"修改指南"：告诉用户最可能想改的 3 个字段在哪。

## 精简示例（节选，展示粒度标准）

```yaml
    - id: POINTS-02
      position: "导览路线第二站，画面中部偏左，信息板宽约 12% 画幅"
      anchor: "登山场景·第一补给站木屋旁"
      treatment: "导览牌：细柱立于场景地面 + 圆角板（panel_bg #FFFEF7 @80%）"
      text:
        badge: "02"
        title: "水温：93°C 黄金区间"
        body: "过高发苦、过低发酸，93°C 能均衡萃取出甜感与香气。"
        data: "建议区间 90-96°C"
      typography: "badge 圆形直径 36px #FFD93D 白字；title 9pt 加粗 #2C3E50；body 7pt；data 7pt Mono #E67E22"
```
