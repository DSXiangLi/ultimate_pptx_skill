# Bond_CashFlow

**中文名**: 债券现金流

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CashFlow` |
| MySQL表名 | `bond_cashflow` |
| 中文名 | 债券现金流 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 不定时更新 |
| 字段数量 | 19 |
| 版本 | 1.03 |

## 表描述

1.记录全市场债券在每个付息兑付时的每百元利息、债权登记除权信息。
2.若违约、递延付息等日常公告明确说明下述情况：a.理论付息日不进行付息；b.兑付日不进行兑付；则本表不展示此条无效数据。
3.数据范围：1981-07-01 至今
4.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `CashFlowType` | 现金流类型 | number(10) | ✗ | 100.0% | 现金流类型（CashFlowType），该字段固定以下常量：1-付息；2-还本付息；3-分期还本 |
| 4 | `CashFlowTypeDesc` | 现金流类型描述 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `InstalmentRepayType` | 分期偿还类型 | number(10) | ✓ | 8.67% | 分期偿还类型(InstalmentRepayType)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 6 | `ValueBeginDate` | 计息起始日期 | date | ✗ | 100.0% |  |
| 7 | `ValueEndDate` | 计息截止日期 | date | ✓ | 100.0% |  |
| 8 | `PaymentDate` | 理论付息(兑付)日 | date | ✓ | 100.0% | 理论付息(兑付)日（PaymentDate）：为推算的理论付息兑付日期，如遇假日，不跳过假日。 |
| 9 | `RegDate` | 债权登记日 | date | ✓ | 99.99% |  |
| 10 | `ExDiviDate` | 除息基准日(废) | date | ✓ | 1.13% |  |
| 11 | `NetPaidPrincipal` | 兑付净价 | number(19,12) | ✓ | 0.07% | 本字段用于维护由于提前兑付、可转债到期赎回等原因导致的兑付金额大于原定本金的情况，由于多出来的补偿部分既不属于利息也不属... |
| 12 | `InterestPer` | 每张付息额(元) | number(27,12) | ✓ | 100.0% |  |
| 13 | `PaymentPer` | 每张兑付本金 | number(27,12) | ✓ | 100.0% |  |
| 14 | `InterestTaxRate` | 利息税率(%) | number(18,6) | ✓ | 100.0% |  |
| 15 | `TotalSize` | 债券总规模(亿元) | number(18,6) | ✓ | 100.0% | 债券总规模(亿元)（TotalSize）：每次付息兑付行为发生前的现存总规模，可用于计算本次付息兑付应付的本金和利息总额 |
| 16 | `CashFlow` | 每张现金流(元) | number(27,12) | ✓ | 100.0% |  |
| 17 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✓ |  |  |
| 19 | `JSID` | JSID | number(19) | ✓ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### CashFlowType (现金流类型)

现金流类型（CashFlowType），该字段固定以下常量：1-付息；2-还本付息；3-分期还本

### InstalmentRepayType (分期偿还类型)

分期偿还类型(InstalmentRepayType)与(CT_SystemConst)表中的DM字段关联，令LB = 1829，得到分期偿还类型的具体描述：1-减少面值，2-减少持仓。

### PaymentDate (理论付息(兑付)日)

理论付息(兑付)日（PaymentDate）：为推算的理论付息兑付日期，如遇假日，不跳过假日。

### NetPaidPrincipal (兑付净价)

本字段用于维护由于提前兑付、可转债到期赎回等原因导致的兑付金额大于原定本金的情况，由于多出来的补偿部分既不属于利息也不属于本金，故补偿部分和本金合并在本字段维护。

### TotalSize (债券总规模(亿元))

债券总规模(亿元)（TotalSize）：每次付息兑付行为发生前的现存总规模，可用于计算本次付息兑付应付的本金和利息总额

## SQL示例

```sql
-- 查询 债券现金流 数据
SELECT *
FROM bond_cashflow
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
