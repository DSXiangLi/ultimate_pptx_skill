# MF_PriceReturnHisTrans

**中文名**: 上市基金行情历史表现(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PriceReturnHisTrans` |
| MySQL表名 | `mf_pricereturnhistrans` |
| 中文名 | 上市基金行情历史表现(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.本表记录展示在交易所交易的封闭式基金、LOF等基金复权价格回报的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
【对转型基金处理收益率和净值时会将转型前后数据同步计算。】
2.历史数据：1998年3月起-至今。
3.信息来源：聚源计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(后复权) | number(18,4) | ✓ | 100.0% |  |
| 5 | `ValueDailyGrowthRate` | 价格日回报率(%) | number(18,4) | ✓ | 99.92% |  |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,4) | ✓ | 99.76% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(18,4) | ✓ | 99.6% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,4) | ✓ | 99.12% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 98.29% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 94.99% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 90.2% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 89.7% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 81.24% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(18,4) | ✓ | 65.19% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(18,4) | ✓ | 65.19% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 51.18% |  |
| 17 | `AnnualRRInThreeYear` | 三年年化回报率(%) | number(18,4) | ✓ | 51.18% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 29.33% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(18,4) | ✓ | 29.33% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(18,4) | ✓ | 7.86% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(18,4) | ✓ | 7.86% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(18,4) | ✓ | 81.25% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 上市基金行情历史表现(转型) 数据
SELECT *
FROM mf_pricereturnhistrans
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
