# MF_FundNetValueRe

**中文名**: 公募基金复权净值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundNetValueRe` |
| MySQL表名 | `mf_fundnetvaluere` |
| 中文名 | 公募基金复权净值 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金净值 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.本表记录开放式基金每日单位基金净值、封闭式每周单位基金净值，以及基金复权单位净值和净值日增长率。
【复权因子： 复权因子 =（分红除息日单位净值+分红除息日分红金额）÷分红除息日单位净值×拆分折算比例】
2.历史数据：1998年4月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✓ | 100.0% |  |
| 4 | `UnitNV` | 单位净值 | number(18,6) | ✓ | 100.0% |  |
| 5 | `GrowthRateFactor` | 复权因子 | float | ✓ | 91.32% |  |
| 6 | `UnitNVRestored` | 复权单位净值 | number(18,6) | ✓ | 100.0% |  |
| 7 | `NVDailyGrowthRate` | 单位净值日增长率 | number(18,6) | ✓ | 91.13% |  |
| 8 | `NVRDailyGrowthRate` | 复权单位净值日增长率(%) | number(18,6) | ✓ | 99.91% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等

## SQL示例

```sql
-- 查询 公募基金复权净值 数据
SELECT *
FROM mf_fundnetvaluere
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
