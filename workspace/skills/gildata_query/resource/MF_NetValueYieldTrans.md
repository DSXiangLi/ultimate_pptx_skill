# MF_NetValueYieldTrans

**中文名**: 公募基金收益率走势(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NetValueYieldTrans` |
| MySQL表名 | `mf_netvalueyieldtrans` |
| 中文名 | 公募基金收益率走势(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.本表记录基金的最新趋势表现，包括一个月、三个月、半年、一年、二年、三年、五年、成立以来的回报走势。可用于基金走势的展示。
【转型处理：与表公募基金收益率走势MF_NetValueYieldTrend不同的是，本表对于基金发生转型，仍将转型前后当作一只基金考虑。】
2.历史数据：1998年3月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值(元) | number(18,4) | ✓ | 100.0% |  |
| 5 | `RRInSingleMonth` | 一个月回报率(%) | number(18,4) | ✓ | 1.98% |  |
| 6 | `RRInThreeMonth` | 三个月回报率(%) | number(18,4) | ✓ | 5.14% |  |
| 7 | `RRInSixMonth` | 六个月回报率(%) | number(18,4) | ✓ | 10.26% |  |
| 8 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,4) | ✓ | 16.53% |  |
| 9 | `RRInSingleYear` | 一年回报率(%) | number(18,4) | ✓ | 18.6% |  |
| 10 | `RRInThreeYear` | 三年回报率(%) | number(18,4) | ✓ | 39.65% |  |
| 11 | `RRInFiveYear` | 五年回报率(%) | number(18,4) | ✓ | 38.69% |  |
| 12 | `RRSinceStart` | 设立以来回报率(%) | number(18,4) | ✓ | 100.0% | 设立以来回报率(%)(RRSinceStart)：计算区间起始日净值取转型前后最早交易日复权净值。 |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RRSinceStart (设立以来回报率(%))

设立以来回报率(%)(RRSinceStart)：计算区间起始日净值取转型前后最早交易日复权净值。

## SQL示例

```sql
-- 查询 公募基金收益率走势(转型) 数据
SELECT *
FROM mf_netvalueyieldtrans
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
