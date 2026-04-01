# Bond_ConBDPutPro

**中文名**: 可转债回售条款触发进度表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDPutPro` |
| MySQL表名 | `bond_conbdputpro` |
| 中文名 | 可转债回售条款触发进度表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.业务说明：该表日度展示可转债特定条件下有条件回售条款的触发价格条件，触发条件满足情况以及行权进度提示。
2.数据范围：2000-03-15 至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `StockInnerCode` | 正股内部编码 | number(10) | ✓ | 100.0% | 正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `IfinPutPeriod` | 当前是否处于回售区间内 | number(10) | ✓ | 100.0% | 当前是否处于回售区间内(IfinPutPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 9... |
| 6 | `PutLimit` | 回售次数限制 | number(10) | ✓ | 14.77% | 回售次数限制(PutLimit)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到回售次数... |
| 7 | `PutPrice` | 预计回售价(元/张) | number(19,12) | ✓ | 14.72% |  |
| 8 | `PutPriceInf` | 预计回售价类型 | number(10) | ✓ | 14.77% |  预计回售价类型(PutPriceInf)：1-募集说明书中约定具体数值的含息回售价；2-聚源根据每日应计利息更新计算的... |
| 9 | `PutPeriodStart` | 回售期起始日 | date | ✓ | 99.89% |  |
| 10 | `PutConditionDay` | 回售条件天数 | number(10) | ✓ | 14.77% |  |
| 11 | `PutReachDay` | 回售条件满足天数 | number(10) | ✓ | 14.77% |  |
| 12 | `PutLevel` | 回售触发价格比例 | number(19,8) | ✓ | 14.77% |  |
| 13 | `ConvertPrice` | 当期转股价 | number(19,8) | ✓ | 99.93% |  |
| 14 | `TermTrigStockPrice` | 回售触发价 | number(19,8) | ✓ | 14.77% |  |
| 15 | `StockClosePrice` | 正股收盘价 | number(19,12) | ✓ | 66.15% |  |
| 16 | `TermsTrigDayCount` | 回售条件天数内累计触发天数 | number(10) | ✓ | 14.77% |  |
| 17 | `PriceTermsStatu` | 当日正股价格是否触发回售条件 | number(10) | ✓ | 100.0% | 当日正股价格是否触发回售条件(PriceTermsStatu)与(CT_SystemConst)表中的DM字段关联，令L... |
| 18 | `ExeReachStartDate` | 触发条件满足区间起始日 | date | ✓ | 0.08% |  |
| 19 | `ExeReachEndDate` | 触发条件满足区间截止日 | date | ✓ | 0.09% |  |
| 20 | `PutExecuteStatu` | 回售情况 | number(10) | ✓ | 100.0% | 回售情况(PutExecuteStatu)：101-未触发回售条款；102-已触发回售条款；201-公告回售行权；202... |
| 21 | `ExecutePutPrice` | 有条件回售价格(含税) | number(19,8) | ✓ | 0.05% |  |
| 22 | `IfIncludeInterest` | 是否包含应计利息 | number(10) | ✓ | 0.05% | 是否包含应计利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 23 | `Interest` | 利息(元/张) | number(19,8) | ✓ | 0.05% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### StockInnerCode (正股内部编码)

正股内部编码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到可转换债券对应正股的交易代码、证券简称等。

### IfinPutPeriod (当前是否处于回售区间内)

当前是否处于回售区间内(IfinPutPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当前是否处于回售区间内的具体描述：1-是，2-否。

### PutLimit (回售次数限制)

回售次数限制(PutLimit)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到回售次数限制的具体描述：1-随时，2-每计息年度1次，3-12月内不超过1次。

### PutPriceInf (预计回售价类型)


预计回售价类型(PutPriceInf)：1-募集说明书中约定具体数值的含息回售价；2-聚源根据每日应计利息更新计算的每日最新回售价。

### PriceTermsStatu (当日正股价格是否触发回售条件)

当日正股价格是否触发回售条件(PriceTermsStatu)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到当日正股价格是否触发回售条件的具体描述：1-是，2-否。

### PutExecuteStatu (回售情况)

回售情况(PutExecuteStatu)：101-未触发回售条款；102-已触发回售条款；201-公告回售行权；202-公告回售不行权。

### IfIncludeInterest (是否包含应计利息)

是否包含应计利息(IfIncludeInterest)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含应计利息的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 可转债回售条款触发进度表 数据
SELECT *
FROM bond_conbdputpro
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
