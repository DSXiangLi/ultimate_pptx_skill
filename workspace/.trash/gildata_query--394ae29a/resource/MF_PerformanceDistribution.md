# MF_PerformanceDistribution

**中文名**: 公募基金经营业绩与收益分配

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PerformanceDistribution` |
| MySQL表名 | `mf_performancedistribution` |
| 中文名 | 公募基金经营业绩与收益分配 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 47 |
| 版本 | 1 |

## 表描述

1.本表记录基金公司披露的定报中基金收入、基金费用、净收益、经营业绩、收益分配等数据。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `SecurityApreadIncome` | 证券买卖价差收入(元) | number(19,4) | ✓ | 99.99% |  |
| 5 | `StockSpreadIncome` |  股票差价收入(元) | number(19,4) | ✓ | 70.15% |  |
| 6 | `BondSpreadIncome` |  债券差价收入(元) | number(19,4) | ✓ | 75.49% |  |
| 7 | `ConvertibleSpreadIncome` |  可转换债券买卖价差收入(元) | number(19,4) | ✓ | 0.01% |  |
| 8 | `WarrantSpreadIncome` |  权证买卖价差收入(元) | number(19,4) | ✓ | 0.5% |  |
| 9 | `OtherSpreadIncome` |  其他价差收入(元) | number(19,4) | ✓ | 0.0% |  |
| 10 | `InvestmentIncome` | 投资收益(元) | number(19,4) | ✓ | 99.99% |  |
| 11 | `BondInterestIncome` |  债券利息收入(元) | number(19,4) | ✓ | 43.23% |  |
| 12 | `ConvertibleInterestIncome` |  可转换债券利息收入(元) | number(19,4) | ✓ | 0.0% |  |
| 13 | `DepositInterestIncome` | 存款利息收入(元) | number(19,4) | ✓ | 99.93% |  |
| 14 | `DividendIncome` |  股利收入(元) | number(19,4) | ✓ | 69.33% |  |
| 15 | `BoughtSellbackSecuIncome` | 买入返售证券收入(元) | number(19,4) | ✓ | 60.72% |  |
| 16 | `OtherInvestmentIncome` |  其他投资收益(元) | number(19,4) | ✓ | 0.0% |  |
| 17 | `OtherIncome` | 其他收入(元) | number(19,4) | ✓ | 79.49% |  |
| 18 | `IssuanceFareBalance` | 额定发行费用余额(元) | number(19,4) | ✓ | 0.01% |  |
| 19 | `TotalIncome` | 收入合计(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `MangementFee` | 基金管理人报酬(元) | number(19,4) | ✓ | 99.87% |  |
| 21 | `PerformanceFee` |  业绩报酬(元) | number(19,4) | ✓ | 0.01% |  |
| 22 | `TrustFee` | 基金托管费(元) | number(19,4) | ✓ | 99.99% |  |
| 23 | `SoldRepoSecuExpense` | 卖出回购证券支出(元) | number(19,4) | ✓ | 46.64% |  |
| 24 | `InterestExpense` | 利息支出(元) | number(19,4) | ✓ | 98.92% |  |
| 25 | `SaleExpense` | 销售费用(元) | number(19,4) | ✓ | 50.86% |  |
| 26 | `OtherExpense` | 其他费用(元) | number(19,4) | ✓ | 100.0% |  |
| 27 | `AnnualListingFee` |  上市年费(元) | number(19,4) | ✓ | 0.47% |  |
| 28 | `InfoDisclosureFee` |  信息披露费(元) | number(19,4) | ✓ | 1.09% |  |
| 29 | `AuditFee` |  审计费用(元) | number(19,4) | ✓ | 1.1% |  |
| 30 | `TotalExpense` | 费用合计(元) | number(19,4) | ✓ | 100.0% |  |
| 31 | `PastProfitAndLoss` | (净收益)以前年度损益调整 | number(19,4) | ✓ | 0.0% |  |
| 32 | `NetProfit` | 基金净收益(元) | number(19,4) | ✓ | 100.0% |  |
| 33 | `UnrealizedProfitChange` | 未实现估值增值变动数(元) | number(19,4) | ✓ | 93.54% |  |
| 34 | `Performance` | 基金经营业绩(元) | number(19,4) | ✓ | 99.95% |  |
| 35 | `RetainedNetProfitAtBegin` | 期初未分配净收益(元) | number(19,4) | ✓ | 0.98% |  |
| 36 | `RetainedProfitBeforeTrans` | 资产移交基准日前未分配收益(元) | number(19,4) | ✓ | 0.0% |  |
| 37 | `RetainedProfitAtBegin` | 期初未分配收益(元) | number(19,4) | ✓ | 0.09% |  |
| 38 | `ApplyingBufferMoney` | 本期申购基金单位的损益平准金(元) | number(19,4) | ✓ | 0.29% |  |
| 39 | `ProfitAndLossBufferMoney` | 本期损益平准金(元) | number(19,4) | ✓ | 0.68% |  |
| 40 | `RedemptionBufferMoney` | 本期赎回基金单位的损益平准金(元) | number(19,4) | ✓ | 0.29% |  |
| 41 | `DistributableNetProfit` | 可供分配基金净收益(元) | number(19,4) | ✓ | 1.1% |  |
| 42 | `DistributedNetProfit` | 本期已分配基金净收益(元) | number(19,4) | ✓ | 0.75% |  |
| 43 | `Others` | 其他(元) | number(19,4) | ✓ | 0.01% |  |
| 44 | `ProfitDistribution` | 收益分配(元) | number(19,4) | ✓ | 0.0% |  |
| 45 | `RetainedProfit` | 期末基金未分配净收益(元) | number(19,4) | ✓ | 1.13% |  |
| 46 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 47 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金经营业绩与收益分配 数据
SELECT *
FROM mf_performancedistribution
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
