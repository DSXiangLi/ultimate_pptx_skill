# 配方存档 · 定投原理投教 × 像素游戏 N4（S4 投教）
> 示范 pixel-game × sequence/任务日志：投教内容装入 RPG 关卡叙事。

```yaml
recipe:
  scenario: S4 投教
  topology: sequence（axis: process）
  narrative: N4 timeline（表现为任务日志）
  style: pixel-game / tokens: {palette: P18 pixel-pastel, typography: T06}
  open_elements:
    ui_metaphor_card:
      system_name: "INVEST_QUEST v1.00"
      ui_era: indie_16bit
      interface_type: RPG任务日志 + 对话框
      concept_to_ui_mapping:
        - {concept: TITLE, ui_element: 游戏窗口标题栏（"INVEST_QUEST"像素字+右上三按钮）}
        - {concept: DATA(认购份额示意), ui_element: RPG属性条（████░░ 格式，每格=1期定投）}
        - {concept: BODY.stages×4, ui_element: 任务日志条目（📜 STAGE 01-04，每条带完成状态像素图标）}
        - {concept: VOICE(可选引用), ui_element: NPC对话框（32×32像素导师头像+对话气泡）}
        - {concept: ASIDE(微笑曲线), ui_element: 像素折线图（独立16×16 tile组成）}
        - {concept: CAUTION, ui_element: ⚠️系统警告框（红色3px边框）}
        - {concept: META, ui_element: 底部系统消息（>>>前缀滚动文字）}
      ui_chrome_elements: ["顶部公告栏（滚动'MARKET ALERT...'）", "CRT扫描线全画面", "像素光标在STAGE入口", "重复★像素分隔线"]
  contract_fill_pattern:
    TITLE: "INVEST_QUEST | 定投通关指南"
    nature: steady
    BODY.sequence.stages:
      - {id: "01", marker: "STAGE 01", title: "设定目标与金额"}
      - {id: "02", marker: "STAGE 02", title: "选定扣款日"}
      - {id: "03", marker: "STAGE 03 ★BOSS", title: "下跌日：份额更多（微笑曲线原理）", climax: true}
      - {id: "04", marker: "STAGE 04 CLEAR", title: "长期复盘节奏"}
    ASIDE: "微笑曲线：低位多买份额→成本摊薄→回升时收益放大"
    CAUTION: "定投不保证盈利。基金有风险，投资须谨慎。"
    META: "仅供投教参考，不构成投资建议 | 日期"
  notes: stage 03 是 climax，像素字加粗 + accent 背景高亮；全图无具体产品代码（投教中立）
```
