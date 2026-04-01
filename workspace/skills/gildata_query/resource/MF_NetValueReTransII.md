# MF_NetValueReTransII

**中文名**: 公募基金复权净值(转型全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NetValueReTransII` |
| MySQL表名 | `mf_netvalueretransii` |
| 中文名 | 公募基金复权净值(转型全) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金净值 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.本表记录开放式基金每日单位基金净值、封闭式每周单位基金净值，以及基金复权单位净值和净值日增长率。
【转型处理：对转型基金处理收益率和净值时，会将转型前后数据同步计算。
本表与MF_FundNetValueReTrans的不同在于，MF_FundNetValueReTrans对于转型基金，只收录了转型后的内码，而本表既有转型前的内码，也有转型后的内码。】
本表针对分红引起的复权因子的变动，采用加法公式进行计算，即(当日单位净值+单位分红)/当日单位净值。MF_NetValueReTransTwo针对分红采用减法计算，即前一日单位净值/(前一日单位净值-单位分红)
2.历史数据：1998年4月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值 | number(18,6) | ✓ | 100.0% |  |
| 5 | `GrowthRateFactor` | 复权因子 | number(18,15) | ✓ | 91.1% |  |
| 6 | `UnitNVRestored` | 复权单位净值 | number(18,6) | ✓ | 100.0% |  |
| 7 | `NVDailyGrowthRate` | 单位净值日增长率 | number(18,6) | ✓ | 90.92% |  |
| 8 | `NVRDailyGrowthRate` | 复权单位净值日增长率(%) | number(18,6) | ✓ | 99.91% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金复权净值(转型全) 数据
SELECT *
FROM mf_netvalueretransii
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
