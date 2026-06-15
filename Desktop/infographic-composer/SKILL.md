---
name: infographic-composer
description: 公募基金叙事信息图/海报创作系统，覆盖陪伴、解读、宣传、投教四大业务场景。将任意结构化内容（市场解读、持有人信、产品宣传、投教科普、复盘总结等）转化为格式化、可稳定修改、合规的绘图指令（渲染规格）。Use this skill whenever the user wants to create an infographic, poster, visual explainer, 信息图, 海报, 陪伴手记, 投教图文, or turn fund/market content into an illustrated visual — even without naming a style. Also use when modifying a previously generated render spec or contributing new styles/palettes/metaphors to the library.
---

# Infographic Composer 叙事信息图创作系统（公募基金版）

把内容转化为**格式化绘图指令（render spec）**：布局明确、每段文字逐字落槽、改任何一处稳定生效、合规底线内置。

## 架构总览

```
业务场景层 fund-scenarios.md —— 陪伴/解读/宣传/投教，领域锚定 + 合规红线
     │
内容契约 content-contract.md —— 拓扑驱动（hero/parallel/sequence/causal/contrast），结构中性
     │
     ├── 枚举层（试错积累的工艺知识，照抄不改）
     │     ├── tokens/palettes.md + typography.md   可组合的调色板包与字体包
     │     ├── styles/                              视觉语言包：质感/氛围/光线/工艺约束/must_avoid
     │     │                                        + tokens 绑定声明（locked / bound-set / open-with-rules）
     │     └── narratives.md                        组织模式 N1-N6 + 拓扑映射 + 兼容矩阵
     │
     └── 开放层（依赖当次内容语义，现场推理）
           protocols.md —— 隐喻/角色/中央主体的描述协议（基金语义优先生发）
           examples/   —— 推理成功后归档为 few-shot 范例（非选项库）
```

知识归属判据：试错换来的工艺数值（金色≤12%、拼豆间距2px）→ 枚举层；依赖内容语义的具象选择（画雪球还是画灯塔）→ 开放层协议。

## 工作流

### Step 0 — 识别业务场景
读 `references/fund-scenarios.md`，判定 S1解读 / S2陪伴 / S3宣传 / S4投教（拿不准问一次用户）。取出该场景的：典型拓扑、推荐搭配、语气规范、**必填槽位与合规红线**——红线凌驾于后续一切创意决策。

### Step 1 — 判定拓扑，填写内容契约
读 `references/content-contract.md`。先判定信息拓扑（hero/parallel/sequence/causal/contrast——不要把并列内容硬塞进"主角+支撑"结构），再按对应 BODY 结构填槽。通用槽位：TITLE / DATA / VOICE / LIST / ASIDE / CAUTION / META。
用户没给的可选槽位留空，**禁止编造**（数据、引用、署名）；scenario 要求必填的槽位（多为 CAUTION/META）缺失时向用户索取。

### Step 2 — 选定 narrative × style × tokens
读 `references/narratives.md`：由拓扑查"拓扑→模式"映射圈定候选，再按兼容矩阵与场景推荐定夺。
**完整读取选中的 style 文件**，按其 tokens 绑定声明选调色板包与字体包：
- locked → 用指定包，不可换（classical-oil）
- bound-set → 从专属集合中按 nature/气质选（perler；storybook/sketchbook 默认集）
- open-with-rules → 可用任何满足该 style 准入规则的包，含用户自定义新包（需先按 `tokens/palettes.md` 的新增规则补全角色并校验）

### Step 3 — 推理开放元素
读 `references/protocols.md`，浏览 `examples/metaphors|characters/` 下 2-3 个范例作 few-shot。
隐喻/主体**优先从基金与投资语义生发**（净值、定投、复利、配置、波动）；为当次内容填满隐喻卡全部字段，映射表填不满即换隐喻。每句描述必须在成品图上可验证。遵守合规画面约束（无收益承诺意象、无恐慌意象、曲线必有波动）。
N3/N6 等不需要隐喻的模式按协议对应小节执行（主图场形态/装饰主题词表）。

### Step 4 — 组装渲染规格
读 `references/render-spec-format.md` 输出完整 spec：
- meta 记录 scenario/topology/style/tokens/narrative
- A 层（确定层）：BODY 每个节点独立成槽（CARD-01/STAGE-01/NODE-01…），文字**逐字写明**；颜色"角色名+色值"双写
- B 层（生成层）：插画/隐喻/角色描述，不含任何文案；与 A 层仅靠 anchor 连接
- C 层：style 与开放元素的 must_avoid 合并
- **不包含**：颜色图例/配色角色表（系统内部参考，不是给读者看的）、渲染附注/修改指南（仅供用户参考，不出现在交付物中）

### Step 5 — 自动校验（不过就修）
跑 content-contract 校验清单 + style 的 quality checklist + **fund-scenarios 合规红线逐条核对**。重点：数字可溯源、必现声明在场、无禁止表述、CAUTION/META 可读且装饰安全距达标、拓扑与结构相符。

### Step 6 — 写出文件，人工确认（生成图片前必须通过）
将完整 spec 写入文件，文件命名格式：`<场景编号>-<拓扑>-<风格>-<日期>`（如 `S1-hero-perler-20260612.md`）。写出后**必须向用户逐项确认以下内容**，用户确认后方可进入图片生成：

| 确认项 | 确认内容 | 目的 |
|---|---|---|
| **风格搭配** | scenario / topology / narrative / style / tokens 选择是否合适 | 保障视觉方向正确 |
| **标题文字** | TITLE.main / TITLE.sub 是否准确、措辞合规 | 标题是第一眼信息 |
| **正文文字** | 每个 BODY 槽位的 text 字段逐字是否正确、数据是否可溯源 | **文字是信息图的核心价值，必须逐字确认** |
| **风险提示** | CAUTION 文案是否完整合规、是否涵盖该 scenario 的必填声明 | **合规底线，遗漏即违规** |
| **页脚信息** | META 数据来源、免责声明、出品方是否完整 | 信息溯源与合规闭环 |

用户修改后回到 Step 4 重新组装，重跑 Step 5-6，直到确认通过。**未经用户确认的 spec 不得送入图片生成环节。**

### Step 7 — 归档（创意积累双轨）
- 开放层：新隐喻/角色经用户认可 → 按 protocols §4 卡片格式泛化后存入 `examples/`；好的整体搭配存 `examples/compositions/` 配方
- 枚举层：新调色板/字体包按 tokens 文件的新增规则补录；新 style 按现有 style 文件结构（工艺约束+must_avoid+槽位表+tokens绑定声明）起草并标注"未验证"

## 修改请求处理
改文字→只改 A 层对应槽位 text；换插画→只改 B 层；换调色板包→全局替换角色色值（双写格式使此操作机械可靠）；换风格→保留 A 层 text，按新 style 重写 treatment/typography。任何修改后输出**完整** spec 并重跑 Step 5 → Step 6 重新确认。

## 文件索引
| 文件 | 何时读 |
|---|---|
| references/fund-scenarios.md | Step 0 必读 |
| references/content-contract.md | Step 1 必读；Step 5 再读校验清单 |
| references/narratives.md | Step 2 必读 |
| references/tokens/palettes.md / typography.md | Step 2 选包时；新增包时读末尾规则 |
| references/styles/<选中包>.md | Step 2 完整读取 |
| references/protocols.md | Step 3 必读 |
| references/render-spec-format.md | Step 4 必读 |
| examples/* | Step 3 浏览 few-shot；同类需求直接复用 compositions |

## 四条底线（贯穿所有步骤）
1. **合规红线**：fund-scenarios.md 第 1-6 条，凌驾于视觉与创意决策。
2. **信息保真**：不发明数据/引用，不裁剪风险提示；拿不准标注 `[待用户确认]`。
3. **可验证描述**：spec 中每句视觉描述都能在成品图上检查真伪。
4. **文图分离**：文字永远逐字写在 A 层槽位，永不交给插画层生成。
