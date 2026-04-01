# MF_MMPerformanceTrans

**中文名**: 公募基金货币型基金收益表现(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MMPerformanceTrans` |
| MySQL表名 | `mf_mmperformancetrans` |
| 中文名 | 公募基金货币型基金收益表现(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 35 |
| 版本 | 1 |

## 表描述

1.本表记录货币基金的收益表现，包括7日、14日、21日、28日、35日、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的表现。
2.历史数据：2004年1月起-至今。
3.信息来源：根据基金公司披露的万份收益、7日年化收益率数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值 | number(18,10) | ✓ | 100.0% |  |
| 5 | `AccumulatedUnitNV` | 单位累计净值 | number(18,10) | ✓ | 100.0% |  |
| 6 | `DailyProfit` | 每万份基金单位当日收益(元) | number(18,10) | ✓ | 100.0% |  |
| 7 | `LatestWeeklyYield` | 最近7日折算年收益率(%) | number(18,10) | ✓ | 99.5% |  |
| 8 | `InvolvedDays` | 涉及天数 | number(10) | ✓ | 100.0% |  |
| 9 | `DailyProfit1` | 每万元当日收益(元) | number(18,10) | ✓ | 100.0% |  |
| 10 | `AnnualizedRRInSingleWeek` | 7日年收益率(%) | number(18,10) | ✓ | 99.88% |  |
| 11 | `AnnualizedRRInTwoWeek` | 14日年收益率(%) | number(18,10) | ✓ | 99.69% |  |
| 12 | `AnnualizedRRInThreeWeek` | 21日年收益率(%) | number(18,10) | ✓ | 99.49% |  |
| 13 | `AnnualizedRRInFourWeek` | 28日年收益率(%) | number(18,10) | ✓ | 99.27% |  |
| 14 | `AnnualizedRRInFiveWeek` | 35日年收益率(%) | number(18,10) | ✓ | 99.05% |  |
| 15 | `RRInThisWeek` | 本周以来收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 16 | `RRInSingleWeek` | 一周回报率(%) | number(18,10) | ✓ | 99.88% |  |
| 17 | `RRInThisMonth` | 本月以来收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 18 | `RRInSingleMonth` | 一个月收益率(%) | number(18,10) | ✓ | 99.19% |  |
| 19 | `RRInThreeMonth` | 三个月收益率(%) | number(18,10) | ✓ | 97.16% |  |
| 20 | `RRInSixMonth` | 六个月收益率(%) | number(18,10) | ✓ | 94.07% |  |
| 21 | `RRSinceThisYear` | 今年以来收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 22 | `RRInSingleYear` | 一年收益率(%) | number(18,10) | ✓ | 88.05% |  |
| 23 | `RRInTwoYear` | 二年收益率(%) | number(18,10) | ✓ | 76.47% |  |
| 24 | `AnnualizedRRInTwoYear` | 二年年化收益率(%) | number(18,10) | ✓ | 76.47% |  |
| 25 | `RRInThreeYear` | 三年收益率(%) | number(18,10) | ✓ | 66.05% |  |
| 26 | `AnnualizedRRInThreeYear` | 三年年化收益率(%) | number(18,10) | ✓ | 66.05% |  |
| 27 | `RRInFiveYear` | 五年收益率(%) | number(18,10) | ✓ | 48.19% |  |
| 28 | `AnnualizedRRInFiveYear` | 五年年化收益率(%) | number(18,10) | ✓ | 48.19% |  |
| 29 | `RRInTenYear` | 十年收益率(%) | number(18,10) | ✓ | 12.46% |  |
| 30 | `AnnualizedRRInTenYear` | 十年年化收益率(%) | number(18,10) | ✓ | 12.46% |  |
| 31 | `RRSinceStart` | 设立以来收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 32 | `AnnualizedRRSinceStart` | 设立以来年化收益率(%) | number(18,10) | ✓ | 88.05% |  |
| 33 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 34 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 35 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金货币型基金收益表现(转型) 数据
SELECT *
FROM mf_mmperformancetrans
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
