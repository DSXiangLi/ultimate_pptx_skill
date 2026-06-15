# 内容契约 v2 Content Contract

与风格无关的信息结构层。**v2 核心变化：先判定信息拓扑，BODY 结构随拓扑而变——不再假设一切内容都有"一个主角+若干支撑"。**

## 第一步：判定信息拓扑 topology

| topology | 信息形态 | 判定线索 |
|---|---|---|
| hero 中心放射 | 一个主角（数字/事件/对象/主张）+ 若干支撑解释 | "为什么涨/跌"、单一异动、单一产品发布 |
| parallel 并列 | 4-12 个等权信息点，互不隶属 | "N 个要点/误区/技巧"、清单、陪伴信里的几句话 |
| sequence 时序 | 按时间或步骤推进 | 历程、流程、复盘、定投步骤、"从…到…" |
| causal 因果 | 节点间有传导/推导关系 | "A 带动 B"、传导机制、链条、闭环 |
| contrast 对照 | 两方比较 | 正误、新旧、多空、两种策略 |

混合内容取**主拓扑**，次级结构降级进节点/卡片内部（如时序中某节点内含因果，写进该节点 body）。

## 第二步：填写槽位

### 顶层字段（必填）
- `topology`：上表五选一
- `nature`：positive / steady / adverse / complex —— 整体基调，驱动开放层场景选择
- `scenario`：S1解读 / S2陪伴 / S3宣传 / S4投教（见 fund-scenarios.md）

### TITLE（必填）
`main`（6-14字）+ `sub`（可空）+ `date`（可空）

### DATA（可选，0-4 项）—— 关键数据条
每项：`label` + `value` + `direction`（↑/↓/→，可空）+ `role`（primary/secondary）。
并列拓扑下各项可全为 secondary（不分主次）；hero 拓扑下 primary 项即主角数值。

### BODY（必填，结构按 topology 五选一）

**hero**：
```yaml
hero: {form: number|claim|object|event, value: "…", support_value: "…"}
points: [{id, title(4-10字), body(按style预算), keywords[0-3], data(可空)}]  # 2-5个
```

**parallel**：
```yaml
cards:  # 4-12 张等权卡
  - {id, category: "政策面/风险/机遇/误区…", title, body, keywords[0-3], data(可空)}
category_legend: [{label, hint}]  # 类别清单（≤6类），供色编码/参考色板用
```

**sequence**：
```yaml
axis: time | process          # 时间轴 or 步骤轴
stages:  # 3-7 个
  - {id, marker: "2024Q1/第1步…", title, body, data(可空)}
climax: <某 stage.id，可空>    # 需要视觉放大的节点
```

**causal**：
```yaml
nodes: [{id, title, body}]    # 3-6 个
links: [{from, to, relation: "带动/抑制/反馈…"}]
conclusion: {title, body}      # 链条汇聚出的结论（可空）
```

**contrast**：
```yaml
axis_label: "误区 vs 正解 / 策略A vs 策略B"
side_a: {label, points: [{title, body}]}   # 两侧 points 数量一致、一一对应
side_b: {label, points: [...]}
verdict: {body}                # 可空；S4投教正误对照时建议填
```

### VOICE / LIST / ASIDE / CAUTION / META
同 v1：VOICE=引用（quote+attribution+emphasis，无真实来源禁填）；LIST=条目清单；ASIDE=小知识；CAUTION=风险提示（**scenario 要求必填时不得省略**）；META=页脚（来源|免责|日期|出品）。

## 填写规则（不变项）
只搬运不创作；缺槽不补；数字原样；判断性措辞按 fund-scenarios 规范软化（"或/有望"）。

## 校验清单（Step 5）
- [ ] topology 判定与内容形态相符（并列内容未被强行塞进 hero 结构，反之亦然）
- [ ] spec 中每个数字可溯源到用户输入
- [ ] TITLE/BODY/META 落位；scenario 的必填槽位（多数场景含 CAUTION）全部在场
- [ ] 各槽位字数在所选 style 预算内
- [ ] 合规红线逐条核对（fund-scenarios.md 第 1-6 条），尤其：必现声明在场、无禁止表述、CAUTION/META 未被装饰遮挡
- [ ] VOICE.attribution 真实；nature 与场景基调一致
- [ ] contrast 两侧 points 一一对应；causal 每条 link 的 from/to 均存在
