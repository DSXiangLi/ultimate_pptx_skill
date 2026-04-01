# Bond_ConBDChangePro

**中文名**: 可转债修正条款触发进度表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDChangePro` |
| MySQL表名 | `bond_conbdchangepro` |
| 中文名 | 可转债修正条款触发进度表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1 |

## 表描述

1.业务说明：该表日度展示可转债特定条件下修正条款的触发价格条件，触发条件满足情况以及行权进度提示。
2.数据范围：2000-03-15 至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `StockInnerCode` | 正股内部编码 | number(10) | ✓ | 100.0% | 正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `RemainingAmount` | 转债余额(万元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `MultiLevel` | 多个触发比例筛选 | number(10) | ✗ | 100.0% | 多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到... |
| 7 | `MultiAdjMode` | 多个修正方式筛选 | number(10) | ✗ | 100.0% | 多个修正方式筛选(MultiAdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2393，... |
| 8 | `AdjDirection` | 修正方向 | number(10) | ✗ | 100.0% | 修正方向(AdjDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 2366，得到修正... |
| 9 | `AdjLevel` | 修正条件触发比例 | number(19,8) | ✓ | 99.32% |  |
| 10 | `AdjConditionDay` | 修正条件天数 | number(10) | ✓ | 99.36% |  |
| 11 | `AdjReachDay` | 修正条件满足天数 | number(10) | ✓ | 99.36% |  |
| 12 | `StockClosePrice` | 正股收盘价 | number(19,12) | ✓ | 66.17% |  |
| 13 | `ConvertPrice` | 当期转股价 | number(19,8) | ✓ | 99.9% |  |
| 14 | `AdjTrigStockPrice` | 修正触发价 | number(19,8) | ✓ | 99.47% |  |
| 15 | `AdjTrigDayCount` | 修正条件天数内累计触发天数 | number(10) | ✓ | 85.53% |  |
| 16 | `PriceAdjStatu` | 当日股价是否触发修正条件 | number(10) | ✓ | 100.0% | 当日股价是否触发修正条件(PriceAdjStatu)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 17 | `AdjReachStartDate` | 修正条件触发区间起始日 | date | ✓ | 2.48% |  |
| 18 | `AdjReachEndDate` | 修正条件触发区间截止日 | date | ✓ | 2.79% |  |
| 19 | `AdjExecuteStatu` | 修正情况 | number(10) | ✓ | 100.0% | 修正情况(AdjExecuteStatu)与(CT_SystemConst)表中的DM字段关联，令LB=2587，得到修... |
| 20 | `AfterAdjConvertPrice` | 修正后转股价 | number(19,8) | ✓ | 0.28% |  |
| 21 | `StopExeStartDate` | 触发不行权区间起始日 | date | ✓ | 14.66% |  |
| 22 | `StopExeEndDate` | 触发不行权区间截止日 | date | ✓ | 14.68% |  |
| 23 | `TriggerRecountDay` | 触发条件重新计算日 | date | ✓ | 14.68% |  |
| 24 | `StockPB` | 正股PB | number(19,8) | ✓ | 63.53% |  |
| 25 | `IfLowNetAssets` | 能否低于净资产 | number(10) | ✓ | 100.0% | 能否低于净资产(IfLowNetAssets)与(CT_SystemConst)表中的DM字段关联，令LB = 999 ... |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### StockInnerCode (正股内部编码)

正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到可转换债券对应正股的交易代码、证券简称等。

### MultiLevel (多个触发比例筛选)

多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到多个触发比例筛选的具体描述：1-不存在多个，2-触发比例从大到小排序-1，3-触发比例从大到小排序-2。

### MultiAdjMode (多个修正方式筛选)

多个修正方式筛选(MultiAdjMode)与(CT_SystemConst)表中的DM字段关联，令LB = 2393，得到多个修正方式筛选的具体描述：1-不存在多个，2-人为修正，3-自动修正。

### AdjDirection (修正方向)

修正方向(AdjDirection)与(CT_SystemConst)表中的DM字段关联，令LB = 2366，得到修正方向的具体描述：1-向下修正，2-向上修正，3-无确定方向。

### PriceAdjStatu (当日股价是否触发修正条件)

当日股价是否触发修正条件(PriceAdjStatu)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当日股价是否触发修正条件的具体描述：1-是，2-否。

### AdjExecuteStatu (修正情况)

修正情况(AdjExecuteStatu)与(CT_SystemConst)表中的DM字段关联，令LB=2587，得到修正情况的具体描述：101-未触发修正条款，102-已触发修正条款，103-处于触发不行权区间，201-公告修正，202-公告不修正。

### IfLowNetAssets (能否低于净资产)

能否低于净资产(IfLowNetAssets)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到能否低于净资产的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 可转债修正条款触发进度表 数据
SELECT *
FROM bond_conbdchangepro
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
