# MF_PriceReturn

**中文名**: 上市基金行情最新表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PriceReturn` |
| MySQL表名 | `mf_pricereturn` |
| 中文名 | 上市基金行情最新表现 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

1.本表记录展示在交易所交易的封闭式基金、LOF等基金复权价格回报的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
【只更新基金的日最新数据】
2.历史数据：各基金最新数据。
3.信息来源：由聚源计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(后复权) | number(18,4) | ✓ | 100.0% |  |
| 5 | `ValueDailyGrowthRate` | 日回报率(%) | number(18,4) | ✓ | 99.84% | 日回报率=（最新基金复权价格/上一个交易日的基金复权价格-1）*100。 |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,4) | ✓ | 99.73% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(18,4) | ✓ | 99.73% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,4) | ✓ | 99.65% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 98.83% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 95.97% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 91.32% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 85.02% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 83.65% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(18,4) | ✓ | 73.45% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(18,4) | ✓ | 73.45% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 62.3% |  |
| 17 | `AnnualizedRRInThreeYear` | 三年年化回报率(%) | number(18,4) | ✓ | 62.3% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 36.96% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(18,4) | ✓ | 36.96% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(18,4) | ✓ | 9.97% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(18,4) | ✓ | 9.97% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(18,4) | ✓ | 83.69% |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (指数内部编码)

指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ValueDailyGrowthRate (日回报率(%))

日回报率=（最新基金复权价格/上一个交易日的基金复权价格-1）*100。

## SQL示例

```sql
-- 查询 上市基金行情最新表现 数据
SELECT *
FROM mf_pricereturn
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
