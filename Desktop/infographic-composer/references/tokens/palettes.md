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
