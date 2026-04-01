# Bond_EmbeddedCashFlow

**中文名**: 含权债券现金流表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_EmbeddedCashFlow` |
| MySQL表名 | `bond_embeddedcashflow` |
| 中文名 | 含权债券现金流表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 不定期更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：该表包含（除ABS、ABN外）所有含回售、赎回等权利的债券，在存续期内约定行权条件下的现金流数据。
2.数据范围：1981-07-01 至今 至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% | 截止日期（EndDate）：现金流生效日期. |
| 4 | `PeriodRate` | 区间利率 | number(19,6) | ✓ | 86.63% |  |
| 5 | `CashFlowType` | 现金流类型 | number(10) | ✓ | 100.0% | 现金流类型(CashFlowType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到现... |
| 6 | `ValueBeginDate` | 计息起始日期 | date | ✓ | 100.0% |  |
| 7 | `ValueEndDate` | 计息截止日期 | date | ✓ | 100.0% |  |
| 8 | `PaymentDate` | 理论付息(兑付)日期 | date | ✗ | 100.0% |  |
| 9 | `InterestPer` | 每张利息 | number(19,12) | ✓ | 100.0% |  |
| 10 | `PaymentPer` | 每张本金 | number(19,12) | ✓ | 100.0% |  |
| 11 | `CashFlow` | 每百元现金流(元) | number(19,12) | ✓ | 100.0% |  |
| 12 | `OpType` | 行权类型 | number(10) | ✗ | 100.0% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN ... |
| 13 | `ExpectedExerciseDate` | 最近可能行权日 | date | ✗ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### EndDate (截止日期)

截止日期（EndDate）：现金流生效日期.

### CashFlowType (现金流类型)

现金流类型(CashFlowType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到现金流类型的具体描述：1-付息，2-中途分期还本(减少面值)，3-中途分期还本(减少持仓)，4-到期分期还本(减少面值)，5-到期分期还本(减少持仓)，6-兑付。

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN (101,201,203)，得到行权类型的具体描述：101-发行人赎回权，201-持有人回售权，203-持有人定向转让权。

## SQL示例

```sql
-- 查询 含权债券现金流表 数据
SELECT *
FROM bond_embeddedcashflow
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
