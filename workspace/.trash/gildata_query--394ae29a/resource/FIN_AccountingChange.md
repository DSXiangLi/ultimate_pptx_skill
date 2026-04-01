# FIN_AccountingChange

**中文名**: 公司财务会计变更

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FIN_AccountingChange` |
| MySQL表名 | `fin_accountingchange` |
| 中文名 | 公司财务会计变更 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 季更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：记录A股公司会计科目变更事项及影响金额。
2.数据范围：2007-12-31至今
3.信息来源：定期报告、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 86.13% |  |
| 6 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志（Mark），该字段固定以下常量：1-合并报告期调整，2-合并报告期未调整，3-母公司报告期调整，4-母公司... |
| 7 | `ChangeItemCode` | 变更项目代码 | number(10) | ✗ | 100.0% | 变更项目代码(ChangeItemCode)：1-会计估计变更、2-会计政策变更、3-前期会计差错更正。 |
| 8 | `AffectReportPeriod` | 受影响的报告期 | date | ✗ | 100.0% |  |
| 9 | `AffectFinancialItemRe` | 受影响的财务科目(披露) | varchar2(100) | ✗ | 100.0% |  |
| 10 | `AffectFinancialItem` | 受影响的财务科目 | varchar2(200) | ✓ | 84.86% |  |
| 11 | `ChangeReason` | 变更的内容和原因 | varchar2(2000) | ✓ | 99.78% |  |
| 12 | `ApprovalProcedure` | 审批程序 | varchar2(500) | ✓ | 57.38% |  |
| 13 | `CurrencyCode` | 币种 | number(10) | ✓ | 99.78% |  |
| 14 | `InfluIndexAmount` | 影响指标值(元) | number(20,4) | ✓ | 82.63% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志（Mark），该字段固定以下常量：1-合并报告期调整，2-合并报告期未调整，3-母公司报告期调整，4-母公司报告期未调整，5-合并季度调整，6-合并季度未调整，7-母公司季度调整，8-母公司季度未调整。

### ChangeItemCode (变更项目代码)

变更项目代码(ChangeItemCode)：1-会计估计变更、2-会计政策变更、3-前期会计差错更正。

## SQL示例

```sql
-- 查询 公司财务会计变更 数据
SELECT *
FROM fin_accountingchange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
