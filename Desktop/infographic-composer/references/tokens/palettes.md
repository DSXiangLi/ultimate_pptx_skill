# 调色板包 Palette Packs

调色板从 style 中独立为可组合 token。每包按**语义角色**定义，style 只引用角色名，不直接写色值。

## 语义角色
| 角色 | 用途 |
|---|---|
| base | 画面底色/纸色 |
| surface | 信息面板底色 |
| text_primary / text_secondary | 主/次文字 |
| primary | 风格主题色（主场景/主图场主导色） |
| secondary | 次级主题色 |
| accent | 强调色（关键数据、路线、徽章） |
| accent_alt | 备选强调（角色色/惊喜色），可空 |
| warning | 警示/CAUTION 用色 |
| line | 轮廓线/框线色 |
| extras | 风格专用扩展角色（如拼豆层、类别徽章组），按需定义 |

## 绑定模式（style 在自己文件中声明）
- **locked**：调色板即风格本体，禁止替换（如 classical-oil 的递减彩度逻辑）
- **bound-set**：只能从指定包集合中选（如 perler 的颜色=拼豆层语义）
- **open-with-rules**：可接任何满足该 style 准入规则的包，含未来新增包

## 包目录

### P01 warm-sunny（暖阳）— nature: positive
base #87CEEB→#FFF9E6(渐变) | surface #FFFEF7@80% | text #2C3E50/#7F8C8D | primary #FF6B6B | secondary #4ECDC4 | accent #FFD93D | accent_alt #FF9A8B | warning #E74C3C | line #5D4E37

### P02 calm-paper（静纸）— nature: steady
base #F0EAE4 | surface #FFFFFF@85% | text #2C2C2C/#6C757D | primary #5499C7 | secondary #85929E | accent #E67E22 | accent_alt #3498DB | warning #C0392B | line #34495E

### P03 dusk-grey（暮灰）— nature: adverse
base #B0BEC5→#CFD8DC | surface #F5F5F5@75% | text #2C3E50/#7F8C8D | primary #8E44AD | secondary #95A5A6 | accent #E74C3C(克制) | accent_alt #9B59B6 | warning #E74C3C | line #5D4E37

### P04 mint-peach（薄荷桃）— nature: complex/突破
base #A8E6CF→#FFDAB9 | surface #FFFEF7@80% | text #2C2C2C/#5C5C5C | primary #FF6F61 | secondary #6BCF7F | accent #FFD93D | accent_alt #A78BFA | warning #E74C3C | line #4A4A4A

### P05 parchment-cream（羊皮奶油）— nature: steady/positive
base #F5EDD5 | surface #FAFAF8 | text #1A1A1A/#909090 | primary #1A3A5C | secondary #A0826D | accent #7BA3C0 | accent_alt #D7B3D1 | warning #E63946 | line #1A3A5C@60%
extras.category_badges: 金#F4D03F 蓝#8BD3DD 粉紫#D7B3D1 粉#FF99CC 绿#99CC66 橙#FFB347

### P06 playful-stationery（趣味文具）— nature: positive/投教轻松向
base #FFF9E6 | surface #FFFFFF | text #1A1A1A/#909090 | primary #5C4A72 | secondary #B8860B | accent #F4D03F | accent_alt #FF99CC | warning #E63946 | line #5C4A72@60%
extras.category_badges: #F4D03F #FF99CC #8BD3DD #99CC66 #FFB347 #D7B3D1

### P07 vintage-sepia（复古褪色）— nature: steady/纪念向
base #E8DCC0 | surface #F2EAD6 | text #4A4A4A/#8B7355 | primary #4A4A4A | secondary #A0826D | accent #8B4513 | accent_alt #CD7F32 | warning #8B0000(克制) | line #8B7355

### P08 cool-data（冷数据）｜P09 warm-heritage（暖传承）｜P10 mono-contrast（黑白）｜P11 tech-vivid（科技）
perler-archive 专属（颜色角色映射拼豆层：base=底场豆, primary=主图场豆, accent=info豆, warning=accent豆），色值见 styles/perler-archive.md，不对其他 style 开放。

### P12 classical-gold（古典金褐）— locked
classical-oil 专属，递减彩度体系（米白紫灰底→焦棕黑字→古铜褐→温金），色值见 styles/classical-oil.md。

## 新增包规则（创意积累入口）
1. 填满全部语义角色（extras 可空）
2. 自查：text_primary 在 base 与 surface 上对比度充分；accent 与 warning 可区分
3. 注明适配 nature 与适配 style（须通过目标 style 的准入规则）
4. 命名 P13 起递增，存入本文件

### P13 editorial-luxury（杂志奢华）— nature: any / 高端向
base #FFFFFF | surface #FFFFFF | text_primary #000000 / text_secondary #6B6B6B | primary #000000 | secondary #722F37 | accent #D4AF37 | accent_alt #D4AF37 | warning #722F37 | line #000000
extras.metallic: 香槟金#D4AF37 / 银#C0C0C0 / 玫瑰金#B76E79（三选一，同版只用一种）
extras.rules: base=大量留白承载；字号跨度≥8×（最小/最大）；accent仅用于数字与金属线

### P14 editorial-minimal（杂志极简）— nature: steady/complex
base #F8F8F5 | surface #F8F8F5 | text_primary #2C2C2C / text_secondary #7A7A7A | primary #2C2C2C | secondary #A45A52 | accent #6B705C | accent_alt #A45A52 | warning #A45A52 | line #2C2C2C
extras.rules: 同 P13 字号跨度规则；accent 仅装饰线与引文

### P15 editorial-avant（杂志先锋）— nature: complex/突破
base #FAFAFA | surface #FAFAFA | text_primary #1A1D2E / text_secondary #6B6B8A | primary #1A1D2E | secondary #FF006E | accent #00D9FF | accent_alt #FF006E | warning #FF006E | line #1A1D2E
extras.rules: 仅 avant 氛围允许 accent+accent_alt 双色同时出现；文字才是主视觉

### P16 pixel-retro（像素复古）— nature: positive/steady
base #E8DCD0 | surface #3B2D1F | text_primary #E8DCD0 / text_secondary #A09080 | primary #3B2D1F | secondary #1A1423 | accent #E63946 | accent_alt #06FFA5 | warning #E63946 | line #3B2D1F
extras.crt_scanline: 深色横线 10% 透明度覆盖全画面；色数上限 32 色

### P17 pixel-cyber（像素赛博）— nature: complex/adverse
base #0D0D1E | surface #1A1030 | text_primary #00FFFF / text_secondary #FF00FF | primary #00FFFF | secondary #FF00FF | accent #FFFF00 | accent_alt #FF00FF | warning #FF0000 | line #00FFFF
extras.crt_scanline: 同 P16；neon_glow: 文字与线条带 4-6px 外发光

### P18 pixel-pastel（像素马卡龙）— nature: positive/投教
base #FFF8E7 | surface #3D2E4F | text_primary #FFF8E7 / text_secondary #C8A8C8 | primary #5C4A72 | secondary #3D2E4F | accent #F4A261 | accent_alt #8BD3DD | warning #E63946 | line #5C4A72

### P19 blueprint-dark（蓝图暗色发光）— nature: complex/causal
base #0D1117 | surface #1A1F2E@80% | text_primary #F0F0F0 / text_secondary #9CA3AF | primary #00D9FF | secondary #A78BFA | accent #FFD700 | accent_alt #39FF14 | warning #FF3B30 | line #1F2937
extras.glow: 结构线外发光 3-5px blur 10px opacity 70%；grid: 50px主/10px细 opacity 20%/8%

### P20 blueprint-classic（蓝图经典）— nature: complex/causal
base #003A70 | surface #00508C@80% | text_primary #FFFFFF / text_secondary #B0E0E6 | primary #FFFFFF | secondary #00CED1 | accent #FFEB3B | accent_alt #00CED1 | warning #FF6B35 | line #FFFFFF
extras.grid: 同 P19 比例，白线

### P21 blueprint-light（蓝图浅色）— nature: complex/steady
base #F5F5F5 | surface #FFFFFF | text_primary #2C2C2C / text_secondary #7F8C8D | primary #2C3E50 | secondary #3498DB | accent #E67E22 | accent_alt #3498DB | warning #E74C3C | line #CCCCCC
extras.grid: 同 P19，灰线

### P22 blueprint-cyber（蓝图赛博）— nature: complex/adverse
base #0A0E1A | surface #1A1533@80% | text_primary #E0E7FF / text_secondary #A78BFA | primary #A78BFA | secondary #00FFFF | accent #FF006E | accent_alt #39FF14 | warning #FF006E | line #1E1B3C
extras.glow: 多色叠加外发光；grid: 同 P19
