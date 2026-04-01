# MF_ExchangeShare

**中文名**: 公募基金场内份额

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ExchangeShare` |
| MySQL表名 | `mf_exchangeshare` |
| 中文名 | 公募基金场内份额 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

本表记录公募基金的场内份额信息，主要包含ETF、LOF和REITs等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 	信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `ExchangeShares` | 场内份额(份)1 | number(18,4) | ✓ | 100.0% |  |
| 8 | `ExFloatShares` | 场内流通份额(份) | number(18,4) | ✓ | 100.0% |  |
| 9 | `ExRestrictedShares` | 场内限售份额(份) | number(18,4) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金场内份额 数据
SELECT *
FROM mf_exchangeshare
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
