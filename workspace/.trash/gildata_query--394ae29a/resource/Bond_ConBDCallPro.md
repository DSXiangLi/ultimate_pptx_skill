# Bond_ConBDCallPro

**中文名**: 可转债赎回条款触发进度表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDCallPro` |
| MySQL表名 | `bond_conbdcallpro` |
| 中文名 | 可转债赎回条款触发进度表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 33 |
| 版本 | 1 |

## 表描述

1.业务说明：该表日度展示可转债特定条件下赎回条款的触发价格条件，触发条件满足情况以及行权进度提示。
2.数据范围：2000-02-25 至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `StockInnerCode` | 正股内部编码 | number(10) | ✓ | 100.0% | 正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `IfinCallPeriod` | 当前是否处于赎回区间内 | number(10) | ✓ | 100.0% | 当前是否处于赎回区间内(IfinCallPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 6 | `CallLimit` | 赎回次数限制 | number(10) | ✓ | 78.26% | 赎回次数限制(CallLimit)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到赎回次... |
| 7 | `CallPrice` | 预计赎回价(元/张) | number(19,12) | ✓ | 78.09% |  |
| 8 | `CallPriceInf` | 预计赎回价类型 | number(10) | ✓ | 78.26% | 预计赎回价类型(CallPriceInf)：1-募集说明书中约定具体数值的含息赎回价；2-聚源根据每日应计利息更新计算的... |
| 9 | `CallUnconvertAmount` | 触发赎回未转股余额(万元) | number(18,4) | ✓ | 74.25% |  |
| 10 | `RemainingAmount` | 转债余额(万元) | number(18,4) | ✓ | 100.0% |  |
| 11 | `AmountTermsStatu` | 当日转债余额是否触发赎回条件 | number(10) | ✓ | 100.0% | 当日转债余额是否触发赎回条件(AmountTermsStatu)与(CT_SystemConst)表中的DM字段关联，令... |
| 12 | `CallPeriodStart` | 赎回期起始日 | date | ✓ | 98.52% |  |
| 13 | `TermDirection` | 赎回条件触发方向 | number(10) | ✗ | 100.0% | 赎回条件触发方向(TermDirection)：1-高于较高水平(100%以上)触发；2-低于较低水平(100%以下)触... |
| 14 | `CallConditionDay` | 赎回条件天数 | number(10) | ✓ | 78.26% |  |
| 15 | `CallReachDay` | 赎回条件满足天数 | number(10) | ✓ | 78.26% |  |
| 16 | `CallLevel` | 赎回触发价格比例 | number(19,8) | ✓ | 78.26% |  |
| 17 | `ConvertPrice` | 转股价 | number(19,8) | ✓ | 99.93% |  |
| 18 | `TermTrigStockPrice` | 赎回触发价 | number(19,8) | ✓ | 78.26% |  |
| 19 | `StockClosePrice` | 正股收盘价 | number(19,12) | ✓ | 66.17% |  |
| 20 | `TermsTrigDayCount` | 赎回条件天数内累计触发天数 | number(10) | ✓ | 73.08% |  |
| 21 | `PriceTermsStatu` | 当日正股价格是否触发赎回条件 | number(10) | ✓ | 100.0% | 当日正股价格是否触发赎回条件(PriceTermsStatu)与(CT_SystemConst)表中的DM字段关联，令L... |
| 22 | `ExeReachStartDate` | 触发条件满足区间起始日 | date | ✓ | 0.4% |  |
| 23 | `ExeReachEndDate` | 触发条件满足区间截止日 | date | ✓ | 0.4% |  |
| 24 | `CallExecuteStatu` | 赎回情况 | number(10) | ✓ | 100.0% | 赎回情况(CallExecuteStatu)：101-未触发赎回条款；102-已触发赎回条款；201-公告赎回行权；20... |
| 25 | `ExecuteCallPrice` | 有条件赎回价格(含税) | number(19,8) | ✓ | 0.92% |  |
| 26 | `IfIncludeInterest` | 是否包含应计利息 | number(10) | ✓ | 0.92% | 是否包含应计利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 27 | `Interest` | 利息(元/张) | number(19,8) | ✓ | 0.92% |  |
| 28 | `StopExeStartDate` | 触发不行权区间起始日 | date | ✓ | 5.31% |  |
| 29 | `StopExeEndDate` | 触发不行权区间截止日 | date | ✓ | 5.31% |  |
| 30 | `TriggerRecountDay` | 触发条件重新计算日 | date | ✓ | 5.33% |  |
| 31 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 32 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 33 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### StockInnerCode (正股内部编码)

正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到可转换债券对应正股的交易代码、证券简称等。

### IfinCallPeriod (当前是否处于赎回区间内)

当前是否处于赎回区间内(IfinCallPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当前是否处于赎回区间内的具体描述：1-是，2-否。

### CallLimit (赎回次数限制)

赎回次数限制(CallLimit)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到赎回次数限制的具体描述：1-随时，2-每计息年度1次，3-12月内不超过1次。

### CallPriceInf (预计赎回价类型)

预计赎回价类型(CallPriceInf)：1-募集说明书中约定具体数值的含息赎回价；2-聚源根据每日应计利息更新计算的每日最新赎回价。

### AmountTermsStatu (当日转债余额是否触发赎回条件)

当日转债余额是否触发赎回条件(AmountTermsStatu)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当日转债余额是否触发赎回条件的具体描述：1-是，2-否。

### TermDirection (赎回条件触发方向)

赎回条件触发方向(TermDirection)：1-高于较高水平(100%以上)触发；2-低于较低水平(100%以下)触发；3-不存在触发比例条件。

### PriceTermsStatu (当日正股价格是否触发赎回条件)

当日正股价格是否触发赎回条件(PriceTermsStatu)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当日正股价格是否触发赎回条件的具体描述：1-是，2-否。

### CallExecuteStatu (赎回情况)

赎回情况(CallExecuteStatu)：101-未触发赎回条款；102-已触发赎回条款；201-公告赎回行权；202-公告赎回不行权；301-处于触发不行权区间。

### IfIncludeInterest (是否包含应计利息)

是否包含应计利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含应计利息的具体描述：1-999，2-999。

## SQL示例

```sql
-- 查询 可转债赎回条款触发进度表 数据
SELECT *
FROM bond_conbdcallpro
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
