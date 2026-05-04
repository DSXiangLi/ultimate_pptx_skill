# TOOLS.md - 本地笔记

技能定义了工具怎么用。这个文件记的是你的环境独有的东西。

## 这里记什么

比如：

- 相机名称和位置
- SSH 主机和别名
- 偏好的 TTS 语音
- 音箱 / 房间名称
- 设备昵称
- 任何环境相关的信息

## 天气查询

- **API**: wttr.in（免费，无需 key，限流 ~1次/秒）
- **默认城市**: 北京（Beijing）
- **Skill**: `daily-weather`（位于 `~/skills/daily-weather/`）
- **脚本**: `~/skills/daily-weather/scripts/weather.sh [city]`
- **Cron 任务**: "每日天气" — 每天 07:00 触发，查询北京天气
- **常用命令**:
  - `curl -s "wttr.in/CITY?format=%l:+%C+%t+%h+%w+%p&lang=zh"` → 一行摘要
  - `curl -s "wttr.in/CITY?n&lang=zh&0"` → 今天预报
  - `curl -s "wttr.in/CITY?n&lang=zh&1"` → 明天预报
- **注意**: 中文城市名可能不稳定，优先用拼音/英文名

## 为什么分开？

技能是共享的。你的环境是你自己的。分开意味着你可以更新技能而不丢失笔记，也可以分享技能而不泄露你的基础设施。

---

加入任何能帮你工作的内容。这是你的速查表。
