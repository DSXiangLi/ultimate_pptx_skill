# MF_IndexReturnHis

**中文名**: 公募基金指数回报历史表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IndexReturnHis` |
| MySQL表名 | `mf_indexreturnhis` |
| 中文名 | 公募基金指数回报历史表现 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

1.本表记录基金投资目标与标的相关指数回报的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
2.历史数据：2009年11月起-至今。
3.信息来源：聚源计算而得。
4.备注：申万二三级指数&外汇债券指数的点位数据由于授权原因不展示，相关的收益率数据会进行展示。如已有授权，申万指数点位数据可以查看QT_SYWGIndexQuote，外汇债券指数点位数据可以查看QT_CFETBondIndexQuote。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `IndexValue` | 最新指数值 | number(18,4) | ✓ | 99.55% |  |
| 5 | `ValueDailyGrowthRate` | 日回报率(%) | number(18,4) | ✓ | 99.97% | 日回报率=（最新指数值/上一个交易日的指数值-1）*100。 |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,4) | ✓ | 99.93% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(18,4) | ✓ | 99.86% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,4) | ✓ | 99.78% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 99.44% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 98.42% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 96.84% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 97.7% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 93.61% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(18,4) | ✓ | 87.3% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(18,4) | ✓ | 87.3% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 81.05% |  |
| 17 | `AnnualizedRRInThreeYear` | 三年年化回报率(%) | number(18,4) | ✓ | 81.05% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 68.82% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(18,4) | ✓ | 68.82% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(18,4) | ✓ | 40.5% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(18,4) | ✓ | 40.5% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(18,4) | ✓ | 93.61% |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的交易代码、简称等。

### ValueDailyGrowthRate (日回报率(%))

日回报率=（最新指数值/上一个交易日的指数值-1）*100。

## SQL示例

```sql
-- 查询 公募基金指数回报历史表现 数据
SELECT *
FROM mf_indexreturnhis
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
