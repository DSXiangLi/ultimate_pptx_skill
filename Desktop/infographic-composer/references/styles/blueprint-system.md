# 视觉语言包 · blueprint-system 系统蓝图风

城市系统剖面图 × 工程技术蓝图：因果机制被"切开"显示内部多层结构，发光线条是信息层级语言。
**视觉冲击来源：等轴测立体剖面 × 系统化发光层级 × 工程标注密度。**
场景适配：S1 解读（机构/复杂多因素，首选）、S4 投教（机制科普，因果拓扑）。

## 画布
16:9 横版（1920×1080）默认——监控大屏/横向剖面图；4:3 亦可。

## tokens 绑定
- 调色板：**bound-set → {P19 blueprint-dark, P20 blueprint-classic, P21 blueprint-light, P22 blueprint-cyber}**。
  按氛围选：科技监控→P19 / 工程专业→P20 / 现代日间→P21 / 赛博未来→P22。
  四包共享规则：extras.glow 的发光规格（P21 无发光，以 line 替代）；extras.grid 的网格规格必须应用。
- 字体：**locked → T07 technical-mono**。对齐感与技术权威是风格本体。

## 工艺约束（不可替换部分）

**背景网格（所有 preset 必须）**：
- 主网格：50px × 50px，grid_lines 色，opacity 20-30%，0.5px 细线
- 细分网格：10px × 10px，opacity 5-10%（P21 浅色版中此网格主要靠颜色区分）
- P19/P20/P22 发光版：网格线本身**不发光**（靠颜色区分即可，避免背景发光噪声）

**发光层级（P19/P20/P22 必须按 §7 协议定义四级；P21 以线宽替代发光）**：
- Level 1 hero：HERO 数值/中心主剖面顶部，outer glow 6-10px blur 15px
- Level 2 structure：所有结构轮廓线，outer glow 3-5px blur 10px opacity 70%
- Level 3 label：标注线与注释文字框，outer glow 1-2px blur 5px opacity 40%
- Level 4 ambient：背景网格，无发光

**等轴测剖面（causal 拓扑必须；其他拓扑可选）**：
- 30° 等轴测投影，层数 3-7 层，每层代表一个因果节点/驱动层
- 层内半透明填充 10-20%，边缘 structure_glow
- 层间距均等，用细线或阴影分隔（不发光）
- 中心剖面占画面 35-45% 宽，60-70% 高
- 每层至少 1 条 callout 标注线

**测量标注系统（所有模式必须，是风格识别度的关键）**：
- 画面边缘标尺：顶部 + 左侧，刻度线 0.5px，标度数字 6pt T07 等宽
- callout 标注：0.5px 细线从结构引出 → 箭头或圆点 → 文字框（半透明 surface 底）
- 坐标标记：关键节点处十字准线（4px × 4px）+ 编号（A-01 格式）6pt
- 比例尺：右下角 "SCALE 1:100 | 编制日期"，6pt

**数据面板系统**：
- 所有面板：surface 色半透明（opacity 70-80%）+ 1px line 色边框 + 小标题栏（深色底 + text_primary）
- 面板切角：可选右上 8-12px 切角（工程切角感）
- 内边距：8-12px
- 分隔线：0.5px，面板内行间

## must_avoid
全画面等强度发光（Level 1-4 必须有明显差级）；发光色超过 palette 中定义的 3 种；
网格线发光（背景网格只靠色区分）；无任何标注线（标注是本风格必要元素，≥8 条）；
手绘/水彩/卡通元素混入；sans-serif 常规字体用于数据（必须等宽）；
P19/P22 等暗色包使用浅色背景（锁定 base 色）；等轴测角度不是 30°。

## 视觉冲击构建流程
Step 1：读 protocols §7，填写 glow_hierarchy_card（四级发光规划 + 各层用色）。
Step 2：若 causal 拓扑，规划等轴测层：每层名称 + 代表的因果节点 + 发光色 + callout 标注文字。
Step 3：render spec B 层写"系统构成说明"——剖面层清单、面板位置、标注线条数。

## 槽位呈现表（契约 v2）
| 槽位 | 呈现 | 规格与预算 |
|---|---|---|
| TITLE | 顶部横条面板（全宽，占 3-5% 高）：左=罗盘图标+系统名；中=主题；右=编号+日期 | 10-12pt T07；底部 1px structure_glow 线；半透明 surface |
| DATA | 右上数据表面板：行列对齐表格，每行 label（左对齐）+value（右对齐）+direction 符号 | label 8pt；value 8pt T07 Mono accent/warning 色；分隔 0.5px；行数 5-10 |
| BODY·causal（N1 分支 or 等轴测剖面）| 中央等轴测剖面：N 层结构，每层带 callout；中心标注汇聚点=conclusion | 层标签 8pt 全大写；callout 6pt；正文 **30-60 字/层**（写进 callout 文字框）|
| BODY·sequence（N4）| 时间轴面板：横向或纵向轴线（2px structure_glow）+ 节点铭牌（切角面板）| marker 8pt；节点正文 30-60 字 |
| BODY·parallel（N6）| 多个等大剖面分析面板并排或网格 | 题 10pt；正文 40-80 字/面板 |
| BODY·contrast（N5）| 左右对称剖面图（共享中轴线） | 每侧正文 30-50 字 |
| VOICE | 分析引文面板：左侧 3px accent 竖条 + 大号引号（Level 1 glow）+ 引文 | 引文 8-9pt，**60-100 字**；attribution 7pt 细线上方 |
| LIST | 底部横向 watch list 面板（全宽或 60% 宽）：产品切角卡并列 | code 12pt T07 Mono Bold accent；name 7pt；note 6pt |
| 左侧图例面板（本风格特有，建议保留）| 竖排层级图例：编号圆点（glow 色）+ 层名 + 说明 | 7-8pt；占左侧 12-15% 宽；图例色=对应层发光色 |
| 小剖面面板（2-3 个，本风格特有）| 底部或侧边：关键驱动因素的 2D 简化剖面图 + 图例 | 每个占 15% 宽；正文融入 callout 标注；图例 3-5 项 |
| CAUTION | 独立横条面板，warning 色左竖条 | 7pt T07；**周边 20px 内禁止 callout 线穿入** |
| META | 最底 2-3%：数据来源\|风险提示\|编制日期\|比例参考 | 6pt T07 text_secondary；居中；左侧可加比例尺图形 |

## quality checklist
背景网格均匀在场（主+细，各自透明度正确）；发光四级层次分明（Level 1 最强，网格无发光）；
等轴测剖面（causal 时）占 35-45% 画面、层数 ≥ 3；callout 标注线 ≥ 8 条；
所有面板半透明+切角/圆角一致；数据表列对齐；比例尺/坐标标记在场；
glow_hierarchy_card 已填；CAUTION 独立面板清晰可读；文字与契约逐字一致；
整体气质：打开这张图像像进入指挥中心或工程监控室，信息有深度、有层次、有精确感。
