# MF_NVPerformTransHTwo

**中文名**: 公募基金复权净值历史表现二(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NVPerformTransHTwo` |
| MySQL表名 | `mf_nvperformtranshtwo` |
| 中文名 | 公募基金复权净值历史表现二(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.本表记录基金的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报，采用与公募基金净值历史表现(转型)（MF_NVPerformanceTransH）中不同的另一套复权方式，即复权因子 =前一日单位净值*拆分折算比例/[前一日单位净值-分红]，计算中使用的复权单位净值来自于公募基金复权净值二(转型)（MF_NetValueReTransTwo）。
2.历史数据：1998年3月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 最新单位净值(元) | number(18,4) | ✓ | 100.0% |  |
| 5 | `NVDailyGrowthRate` | 日回报率(%) | number(18,4) | ✓ | 99.91% |  |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,4) | ✓ | 99.8% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(18,4) | ✓ | 99.75% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,4) | ✓ | 99.46% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 98.93% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 96.01% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 90.94% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 91.04% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 81.21% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(18,4) | ✓ | 63.7% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(18,4) | ✓ | 63.7% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 48.96% |  |
| 17 | `AnnualizedRRInThreeYear` | 三年年化回报率(%) | number(18,4) | ✓ | 48.96% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 28.24% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(18,4) | ✓ | 28.24% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(18,4) | ✓ | 6.75% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(18,4) | ✓ | 6.75% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(18,4) | ✓ | 81.21% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金复权净值历史表现二(转型) 数据
SELECT *
FROM mf_nvperformtranshtwo
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
