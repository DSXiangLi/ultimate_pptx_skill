# MF_NetValuePerformanceHis

**中文名**: 公募基金净值历史表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NetValuePerformanceHis` |
| MySQL表名 | `mf_netvalueperformancehis` |
| 中文名 | 公募基金净值历史表现 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 25 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
2.历史数据：1998年3月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 最新单位净值(元) | number(22,8) | ✓ | 100.0% |  |
| 5 | `NVDailyGrowthRate` | 日回报率(%) | number(24,10) | ✓ | 99.9% | 日回报率=（最新复权单位净值/上一个交易日的复权单位净值-1）*100。（上一交易日指基金上一个披露净值的日期） |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(24,10) | ✓ | 99.74% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(24,10) | ✓ | 98.87% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(24,10) | ✓ | 95.83% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(24,10) | ✓ | 90.59% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(24,10) | ✓ | 80.56% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(24,10) | ✓ | 62.56% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(24,10) | ✓ | 62.56% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(24,10) | ✓ | 47.45% |  |
| 17 | `AnnualizedRRInThreeYear` | 三年年化回报率(%) | number(24,10) | ✓ | 47.45% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(24,10) | ✓ | 26.38% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(24,10) | ✓ | 26.38% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(24,10) | ✓ | 6.12% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(24,10) | ✓ | 6.12% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(24,10) | ✓ | 80.6% |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### NVDailyGrowthRate (日回报率(%))

日回报率=（最新复权单位净值/上一个交易日的复权单位净值-1）*100。（上一交易日指基金上一个披露净值的日期）

## SQL示例

```sql
-- 查询 公募基金净值历史表现 数据
SELECT *
FROM mf_netvalueperformancehis
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
