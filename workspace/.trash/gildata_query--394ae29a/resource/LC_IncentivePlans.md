# LC_IncentivePlans

**中文名**: 激励计划

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IncentivePlans` |
| MySQL表名 | `lc_incentiveplans` |
| 中文名 | 激励计划 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 38 |
| 版本 | 1.06 |

## 表描述

1.收录公告中披露的公司实行股权激励计划方案的要素信息，包括股东大会公告日期、授予日、事件进程、方案说明、激励模式、行权条件等指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✓ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `IncentivePlanEventCode` | 激励计划事项编码 | varchar2(30) | ✓ | 100.0% |  |
| 5 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 71.39% |  |
| 7 | `DMAnnounceDate` | 董事会公告日期 | date | ✓ | 98.87% |  |
| 8 | `SMAnnounceDate` | 股东大会公告日期 | date | ✓ | 94.48% |  |
| 9 | `InitialawardPublDate` | 首次授予公告日 | date | ✓ | 90.64% |  |
| 10 | `InitialawardDate` | 首次授予日 | date | ✓ | 90.63% |  |
| 11 | `ReservationawardPublDate` | 预留授予公告日 | date | ✓ | 27.91% |  |
| 12 | `ReservationawardDate` | 预留授予日 | date | ✓ | 27.91% |  |
| 13 | `InitialExerciseStartDate` | 首次行权起始日 | date | ✓ | 7.79% |  |
| 14 | `EventProcedureCode` | 事件进程代码 | number(10) | ✓ | 100.0% | 事件进程代码(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 15 | `EventProcedure` | 事件进程 | varchar2(50) | ✓ | 100.0% |  |
| 16 | `ExpirePublDate` | 终止实施公告日 | date | ✓ | 12.97% |  |
| 17 | `ProjectStatement` | 方案说明 | clob | ✓ | 1.99% |  |
| 18 | `IncentiveModeCode` | 激励模式代码 | number(10) | ✓ | 100.0% | 激励模式代码(IncentiveModeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 19 | `IncentiveMode` | 激励模式 | varchar2(50) | ✓ | 100.0% |  |
| 20 | `StockType` | 股票种类 | varchar2(50) | ✓ | 97.49% |  |
| 21 | `StockSourceCode` | 股票来源代码 | number(10) | ✓ | 97.3% | 股票来源代码(StockSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1402... |
| 22 | `StockSource` | 股票来源 | varchar2(50) | ✓ | 97.3% |  |
| 23 | `PlannedPartiAmount` | 计划参与人数 | number(10) | ✓ | 72.14% |  |
| 24 | `ActualPartiAmount` | 实际参与人数 | number(10) | ✓ | 68.75% |  |
| 25 | `OptionAbbr` | 期权简称 | varchar2(100) | ✓ | 14.21% |  |
| 26 | `OptionCode` | 期权代码 | varchar2(100) | ✓ | 14.53% |  |
| 27 | `IncentivePlansAwardVolume` | 激励计划授予数量(股) | number(19) | ✓ | 70.16% |  |
| 28 | `InitialawardVolume` | 其中:首次授予数量(股) | number(19) | ✓ | 70.09% |  |
| 29 | `ReservationawardVolume` | 其中:预留授予数量(股) | number(19) | ✓ | 37.74% |  |
| 30 | `PCTOfTotalShares` | 激励计划授予数量占总股本比例(%) | number(10,6) | ✓ | 70.16% |  |
| 31 | `AwardPrice` | 激励计划授予价格(元) | number(19,4) | ✓ | 70.04% |  |
| 32 | `PricingMethod` | 价格确定方法 | varchar2(2000) | ✓ | 97.15% |  |
| 33 | `PeriodOfValidity` | 有效期(月) | number(10) | ✓ | 96.55% |  |
| 34 | `AuthorizationTimes` | 授权次数 | number(10) | ✓ | 44.2% |  |
| 35 | `ExercisedCondition` | 行权条件 | varchar2(2000) | ✓ | 96.86% |  |
| 36 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 37 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 38 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### EventProcedureCode (事件进程代码)

事件进程代码(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1000,1001,1004,1016,1019,1022,3125,3304,3305)，得到事件进程代码的具体描述：1000-意向，1001-预案，1004-决案，1016-未实施终止，1019-实施中，1022-实施完成，3125-股东大会否决，3304-提前终止，3305-放弃。

### IncentiveModeCode (激励模式代码)

激励模式代码(IncentiveModeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1400，得到激励模式代码的具体描述：10-限制性股票，11-第一类限制性股票，12-第二类限制性股票，13-业绩股票，15-管理层持股，21-股票期权，23-股票增值权，25-虚拟股票，31-激励基金，90-未明确，99-其他。

### StockSourceCode (股票来源代码)

股票来源代码(StockSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1402，得到股票来源代码的具体描述：11-发行股份，13-回购股份，15-存量股份，99-其他来源。

## SQL示例

```sql
-- 查询 激励计划 数据
SELECT *
FROM lc_incentiveplans
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
