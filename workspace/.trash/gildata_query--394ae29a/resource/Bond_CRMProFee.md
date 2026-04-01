# Bond_CRMProFee

**中文名**: 信用风险缓释工具信用保护费

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CRMProFee` |
| MySQL表名 | `bond_crmprofee` |
| 中文名 | 信用风险缓释工具信用保护费 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

本表记录信用风险缓释工具（包括信用风险缓释凭证和信用保护凭证）每笔信用保护费的支付日，费率，计费起始日和截止日等信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | “债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等 |
| 3 | `CPFSerial` | 信用保护费序号 | number(10) | ✓ | 100.0% |  |
| 4 | `BillingStartDate` | 计费起始日期 | date | ✗ | 100.0% |  |
| 5 | `BillingEndDate` | 计费截止日期 | date | ✓ | 100.0% |  |
| 6 | `PaymentDate` | 信用保护费支付日 | date | ✗ | 100.0% |  |
| 7 | `RegDate` | 权益登记日 | date | ✓ | 100.0% |  |
| 8 | `ThisPeriodProRate` | 本期信用保护费率(%) | number(18,6) | ✓ | 90.58% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等

## SQL示例

```sql
-- 查询 信用风险缓释工具信用保护费 数据
SELECT *
FROM bond_crmprofee
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
