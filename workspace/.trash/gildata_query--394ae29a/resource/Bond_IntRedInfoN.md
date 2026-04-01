# Bond_IntRedInfoN

**中文名**: 债券付息兑付新表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IntRedInfoN` |
| MySQL表名 | `bond_intredinfon` |
| 中文名 | 债券付息兑付新表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 不定时更新 |
| 字段数量 | 21 |
| 版本 | 1.02 |

## 表描述

1.涵盖全部债券，如ABS、ABN、可转债、私募债，全部付息兑付类型，如一次性还本、提前还本、分期还本等。
2.本表可区分减少持仓和减少面额的还本，包含理论和实际两种日期，其中实际付息(兑付)日为理论付息(兑付)日的假日顺延。
3.违约情况：是否有效为否，则表明此条数据无效。
4.本表还能查询付息兑付是否逾期偿还。
5.数据范围：1986-07-01至今
6.信息来源：所有已披露的债券付息、兑付、行权公告；没有公告披露的付息兑付，ABS、ABN会在本次付息兑付的登记日自动计算生成，其他类型债券会在本次付息兑付的登记日前两个工作日自动计算生成（如果后面公告披露，此条数据会随着公告更改，应注意违约情况）。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 46.05% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 46.0% |  |
| 5 | `IfOverrideRe` | 是否逾期偿还 | number(10) | ✗ | 100.0% | 是否逾期偿还(IfOverrideRe)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and... |
| 6 | `EventType` | 事项类型 | number(10) | ✗ | 100.0% | 事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到事项类型的... |
| 7 | `RegDate` | 债权登记日 | date | ✓ | 99.99% |  |
| 8 | `InterestTaxRate` | 利息税率(%) | number(19,8) | ✓ | 100.0% |  |
| 9 | `PayDatePL` | 理论付息(兑付)日 | date | ✗ | 100.0% |  |
| 10 | `PayDateAct` | 实际付息(兑付)日 | date | ✗ | 100.0% |  |
| 11 | `NetPaidPrincipal` | 提前兑付净价 | number(19,12) | ✓ | 0.12% |  |
| 12 | `PayingInterest` | 每张兑付利息额 | number(19,12) | ✗ | 100.0% |  |
| 13 | `PayingPrincipal` | 每张兑付本金额 | number(19,12) | ✗ | 100.0% |  |
| 14 | `PayingPrice` | 每张兑付本息额 | number(19,12) | ✗ | 100.0% |  |
| 15 | `DeRatio` | 持仓减少比例额 | number(19,12) | ✗ | 100.0% |  |
| 16 | `IfEffected` | 是否有效(针对违约) | number(10) | ✗ | 100.0% | 是否有效(针对违约)(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 a... |
| 17 | `DataMark` | 数据标识 | number(10) | ✗ | 100.0% | 数据标识(DataMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2035，得到数据标识的具... |
| 18 | `OperationMark` | 业务标识 | number(10) | ✓ | 0.71% | 业务标识(OperationMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2098，得到业... |
| 19 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### IfOverrideRe (是否逾期偿还)

是否逾期偿还(IfOverrideRe)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否逾期偿还的具体描述：1-是，2-否。

### EventType (事项类型)

事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到事项类型的具体描述：1-付息，2-中途分期还本(减少面值)，3-中途分期还本(减少持仓)，4-到期分期还本(减少面值)，5-到期分期还本(减少持仓)，6-兑付。

### IfEffected (是否有效(针对违约))

是否有效(针对违约)(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否有效(针对违约)的具体描述：1-是，2-否。

### DataMark (数据标识)

数据标识(DataMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2035，得到数据标识的具体描述：1-过程计算生成，2-公告披露金额指标，3-公告披露非金额指标，4-手工修改。

### OperationMark (业务标识)

业务标识(OperationMark)与(CT_SystemConst)表中的DM字段关联，令LB = 2098，得到业务标识的具体描述：1-中途全部回售。

## SQL示例

```sql
-- 查询 债券付息兑付新表 数据
SELECT *
FROM bond_intredinfon
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
