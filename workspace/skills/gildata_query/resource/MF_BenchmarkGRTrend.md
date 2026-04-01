# MF_BenchmarkGRTrend

**中文名**: 公募基金基准收益走势(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BenchmarkGRTrend` |
| MySQL表名 | `mf_benchmarkgrtrend` |
| 中文名 | 公募基金基准收益走势(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录基金基准的最新趋势表现，包括一个月、三个月、半年、一年、二年、三年、五年、成立以来的回报。
2.数据范围：1998年3月起-至今。
3.信息来源：根据基金基准的行情计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `WeeklyBenchGR` | 一周基金基准增长率(%) | number(18,4) | ✓ | 0.51% |  |
| 5 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 1.93% |  |
| 6 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 5.03% |  |
| 7 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 10.04% |  |
| 8 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 16.13% |  |
| 9 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 18.23% |  |
| 10 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 38.9% |  |
| 11 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 38.29% |  |
| 12 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |
| 16 | `RRInTwoYear` | 二年回报率(%) | number(18,4) | ✓ | 31.16% |  |

## SQL示例

```sql
-- 查询 公募基金基准收益走势(转型) 数据
SELECT *
FROM mf_benchmarkgrtrend
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
