# MF_NVPerformanceTrans

**中文名**: 公募基金净值最新表现(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NVPerformanceTrans` |
| MySQL表名 | `mf_nvperformancetrans` |
| 中文名 | 公募基金净值最新表现(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金的最新表现，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
【只更新基金的日最新数据】
2.历史数据：1998年3月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 最新单位净值(元) | number(22,8) | ✓ | 100.0% |  |
| 5 | `NVDailyGrowthRate` | 日回报率(%) | number(24,10) | ✓ | 99.7% |  |
| 6 | `RRInSelectedWeek` | 本周以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 7 | `RRInSingleWeek` | 一周回报率(%) | number(24,10) | ✓ | 99.49% |  |
| 8 | `RRInSelectedMonth` | 本月以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 9 | `RRInSingleMonth` | 一个月回报率(%) | number(24,10) | ✓ | 98.66% |  |
| 10 | `RRInThreeMonth` | 三个月回报率(%) | number(24,10) | ✓ | 96.52% |  |
| 11 | `RRInSixMonth` | 六个月回报率(%) | number(24,10) | ✓ | 92.73% |  |
| 12 | `RRSinceThisYear` | 今年以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 13 | `RRInSingleYear` | 一年回报率(%) | number(24,10) | ✓ | 86.23% |  |
| 14 | `RRInTwoYear` | 二年回报率(%) | number(24,10) | ✓ | 73.39% |  |
| 15 | `AnnualizedRRInTwoYear` | 二年年化回报率(%) | number(24,10) | ✓ | 73.39% |  |
| 16 | `RRInThreeYear` | 三年回报率(%) | number(24,10) | ✓ | 60.98% |  |
| 17 | `AnnualizedRRInThreeYear` | 三年年化回报率(%) | number(24,10) | ✓ | 60.98% |  |
| 18 | `RRInFiveYear` | 五年回报率(%) | number(24,10) | ✓ | 35.08% |  |
| 19 | `AnnualizedRRInFiveYear` | 五年年化回报率(%) | number(24,10) | ✓ | 35.08% |  |
| 20 | `RRInTenYear` | 十年回报率(%) | number(24,10) | ✓ | 8.91% |  |
| 21 | `AnnualizedRRInTenYear` | 十年年化回报率(%) | number(24,10) | ✓ | 8.91% |  |
| 22 | `RRSinceStart` | 设立以来回报率(%) | number(24,10) | ✓ | 100.0% |  |
| 23 | `AnnualizedRRSinceStart` | 设立以来年化回报率(%) | number(24,10) | ✓ | 86.26% |  |
| 24 | `RRSinceStartII` | 设立以来回报率II(%) | number(24,10) | ✓ | 100.0% | 设立以来回报率II(%)(RRSinceStartII)：计算方式为(当前复权净值/首日复权净值-1)*100 |
| 25 | `AnnRRSinceStartII` | 设立以来年化回报率II(%) | number(24,10) | ✓ | 86.23% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RRSinceStartII (设立以来回报率II(%))

设立以来回报率II(%)(RRSinceStartII)：计算方式为(当前复权净值/首日复权净值-1)*100

## SQL示例

```sql
-- 查询 公募基金净值最新表现(转型) 数据
SELECT *
FROM mf_nvperformancetrans
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
