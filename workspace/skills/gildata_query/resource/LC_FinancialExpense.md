# LC_FinancialExpense

**中文名**: 利润分配表附注_财务费用

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_FinancialExpense` |
| MySQL表名 | `lc_financialexpense` |
| 中文名 | 利润分配表附注_财务费用 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表附注 |
| 更新频率 | 季更新 |
| 字段数量 | 27 |
| 版本 | 1.01 |

## 表描述

1.本附注描述上市公司(含科创板)、发债人的财务费用的名细，依据所对应的报表，分别存在合并未调整数据，各项目单位均为人民币元。
2.数据范围：1997-12-31至今
3.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM I... |
| 6 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 7 | `InterestExpense` | 利息支出(元) | number(19,4) | ✓ | 87.27% |  |
| 8 | `CapitalOccupationExpense` | 加:资金占用费支出(元) | number(19,4) | ✓ | 0.09% |  |
| 9 | `InterestExpenseOfDiscount` | 加:贴现利息支出(元) | number(19,4) | ✓ | 0.0% |  |
| 10 | `InterestExpenseCapitalized` | 减:资本化利息支出(元) | number(19,4) | ✓ | 3.13% |  |
| 11 | `InterestIncome` | 减:利息收入(元) | number(19,4) | ✓ | 98.98% |  |
| 12 | `CapitalOccupationIncome` | 减:资金占用费收入(元) | number(19,4) | ✓ | 0.11% |  |
| 13 | `InterestSubsidyIncome` | 减:贴息收入(元) | number(19,4) | ✓ | 1.87% |  |
| 14 | `NetInterestExpense` | 利息净支出 | number(19,4) | ✓ | 0.31% |  |
| 15 | `ExchangeLoss` | 加:汇兑损失(元) | number(19,4) | ✓ | 18.76% |  |
| 16 | `ExchangeLossCapitalized` | 减:资本化汇兑损失(元) | number(19,4) | ✓ | 0.12% |  |
| 17 | `ExchangeIncome` | 减:汇兑收益(元) | number(19,4) | ✓ | 10.34% |  |
| 18 | `ExchangeProLoss` | 汇兑损益 | number(19,4) | ✓ | 35.14% |  |
| 19 | `CashDiscount` | 减:现金折扣(元) | number(19,4) | ✓ | 1.69% |  |
| 20 | `OtherFinancialIncome` | 减:其他财务收入(元) | number(19,4) | ✓ | 0.0% |  |
| 21 | `Commission` | 手续费(元) | number(19,4) | ✓ | 73.17% |  |
| 22 | `SecurityExpense` | 担保费(元) | number(19,4) | ✓ | 1.78% |  |
| 23 | `OtherFinancialExpense` | 其他财务费用(元) | number(19,4) | ✓ | 42.68% |  |
| 24 | `Total` | 合计(元) | number(19,4) | ✓ | 99.94% |  |
| 25 | `ChangePublDate` | 更正公告日期 | date | ✓ | 0.0% |  |
| 26 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfMerged (是否合并)

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN(1,2)，得到是否合并的具体描述：1-合并，2-母公司。

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (2)，得到是否调整的具体描述：2-否。

## SQL示例

```sql
-- 查询 利润分配表附注_财务费用 数据
SELECT *
FROM lc_financialexpense
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
