# 视觉语言包 · magazine-editorial 简约时尚杂志风

VOGUE/ELLE/Kinfolk 的版式美学：留白是主动设计、字号跨度是主视觉、金属细线是唯一装饰。
**视觉冲击来源：排版张力，而非插画或隐喻。**
场景适配：S3 宣传（品牌/新发/获奖，首选）、S1 高端解读（致机构/高净值）。

## 画布
9:16 竖版（1080×1920）默认——杂志封面/社交竖屏；横版用于 N5 双联画展开页。

## tokens 绑定
- 调色板：**bound-set → {P13 editorial-luxury, P14 editorial-minimal, P15 editorial-avant}**。
  按氛围选：奢华精致→P13 / 极简高冷→P14 / 艺术先锋→P15。
  三包共享准入规则：base≥95% 明度（近白/纸白）；text_primary 为接近黑的深色；accent 仅用于金属线与数据强调；extras.metallic 三选一同版只用一种。
- 字体：**locked → T05 display-editorial**。字号跨度是风格本体，不可替换。

## 工艺约束（不可替换部分）

**留白纪律（本风格最高约束）**：
- 版面留白率 ≥ 40%（不含 base 底色，指主动空置的栏/区）
- 禁止"填满思维"：每增加一个元素，先问"去掉它版面是否更好"
- 不对称留白：某列/某区域的留白是故意的，不是遗漏

**字号-字重张力系统（第二约束）**：
- 同版字号跨度 ≥ 8×（如 caption 6pt → hero_data 80pt）
- 超大 Display 标题：纤细字重（100-200）**与**粗体数字（900）并置，制造最大字重跨度
- 全大写 + 字距加宽（0.2-0.4em）用于所有栏标签与 kicker

**金属元素纪律**：
- 金属线宽度：0.5-1px，装饰细线；**禁止粗金线、大面积金色底**
- 出现位置：标题下分隔线、数据强调色、封面大标题下划线；全版覆盖 ≤ 3%
- 烫金/metallic 效果：微弱阴影或双色（#D4AF37 + #FFF8DC 双色模拟）

**光线/质感**：
- 摄影棚顶光→均匀无阴影；窗光→单侧来光轻阴影；两者不混用
- 纸张：高光铜版纸（surface 高明度）/ 哑光艺术纸（surface 轻微纹理 2-3%）/ 压纹特种纸（全页轻微几何压纹 1%）
- 禁止任何水彩、手绘、粗粝质感（杂志是印刷精确感）

## must_avoid
留白率 < 40%；字号跨度 < 6×；插画/隐喻/角色（此风格无场景隐喻，版式即主视觉）；
粗金线或大面积金色；任何水彩/手绘/拼豆/像素混入；高饱和辅助色（accent 只能是克制的金/绿/蓝）；
信息填满每个角落；居中对齐用于正文（正文一律左对齐或不对称分栏）。

## 视觉冲击构建流程（替代"选隐喻"步骤）
Step 1：读 protocols §5，填写 typography_impact_card（字号规划+留白率+不对称规则）。
Step 2：在 render spec B 层写"版式构成说明"而非"插画描述"——写明哪个区域留白、文字如何穿越区域、大字如何裁切出血（标题字可从版面边缘被裁切，如杂志封面）。

## 槽位呈现表（契约 v2）
| 槽位 | 呈现 | 规格与预算 |
|---|---|---|
| TITLE | 杂志 masthead 条：左上品牌/出品小 logo（极细线）+ 右上期号/日期 | logo 字 8pt 极细全大写字距加宽；期号 7pt；顶部 2% |
| DATA（hero 拓扑 primary）| 超大数字（hero_size，如 80-120pt）+ 极小标注（8pt），不对称布局 | primary 值字重 100 或 900（选一极端）；accent 色或黑；下方 0.5px metallic 线 |
| BODY·封面大标题（headline） | 占版面 20-30% 的超大 Display 文字，可断行，关键词变字重/变色 | headline_size 50-80pt；全大写；可跨栏出血到边缘 |
| BODY·导语 standfirst | 窄栏居中（60% 宽）或偏左对齐，灰色 2-3 行 | kicker：10pt 全大写字距加宽；standfirst：11pt text_secondary 行距 1.6 |
| BODY·editorial sections（N2 环绕或竖向栏）| 不对称分栏（如 70%文字+30%留白）；栏标签全大写细字距 | 题：14pt 全大写 text_secondary；正文：10pt 行距 1.6，**50-100字/段** |
| BODY·pullout quote（穿插）| 超大斜体引号装饰（200pt 轻描，opacity 10%）+ 中号引文 | 引文：18-22pt 细字重衬线；attribution：8pt 细线上方 |
| VOICE | 同 pullout quote | 引文 **60-120 字**；attribution 署名 |
| LIST | 底部网格产品展示：浅色块+细线框 | name 11pt 粗；tag 10pt Mono accent；note 8pt；卡间距 12px |
| ASIDE | 细线框 kicker 小框，通常嵌在正文栏侧边 | 7-8pt，**20-40 字** |
| CAUTION | 独立行，细字，细线上下夹注 | 7pt text_secondary；**装饰性细线/metallic 线禁止靠近** |
| META | 最底 5%，极小极细，credits 式排列 | 6pt text_secondary，居中或两端对齐 |

## quality checklist
留白率 ≥ 40%；字号跨度 ≥ 8×；无插画/隐喻；metallic 线 ≤ 1px 全版 ≤ 3% 覆盖；
typography_impact_card 各字段已填；不对称布局成立；CAUTION/META 独立可读；
整体气质：冷静克制，高端印刷质感，版式本身令人屏息。
