# MF_BalanceSheet

**中文名**: 公募基金资产负债表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BalanceSheet` |
| MySQL表名 | `mf_balancesheet` |
| 中文名 | 公募基金资产负债表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 60 |
| 版本 | 1 |

## 表描述

1.收录基金定报中披露的资产负债表中的相关数据，该表中各财务科目下数据对应的货币单位均为人民币元。
2.历史数据：1998年12月起-至今。
3.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `Cash` | 现金 | number(19,4) | ✓ | 0.0% |  |
| 5 | `Deposit` | 银行存款 | number(19,4) | ✓ | 71.25% |  |
| 6 | `SettlementproviDealCover` | 清算备付金及交易保证金 | number(19,4) | ✓ | 88.78% |  |
| 7 | `Settlementprovi` |   清算备付金 | number(19,4) | ✓ | 82.3% |  |
| 8 | `DealCover` |   交易保证金 | number(19,4) | ✓ | 82.78% |  |
| 9 | `SecuSettlementReceivables` | 应收证券清算款 | number(19,4) | ✓ | 46.27% |  |
| 10 | `DividendReceivables` | 应收股利 | number(19,4) | ✓ | 11.2% |  |
| 11 | `Receivables` | 应收帐款 | number(19,4) | ✓ | 0.08% |  |
| 12 | `InterestReceivables` | 应收利息 | number(19,4) | ✓ | 52.68% |  |
| 13 | `ApplyingReceivables` | 应收申购款 | number(19,4) | ✓ | 70.78% |  |
| 14 | `OtherReceivables` | 其他应收款 | number(19,4) | ✓ | 0.5% |  |
| 15 | `StockInvestMarketValue` | 股票投资－市值 | number(19,4) | ✓ | 67.54% |  |
| 16 | `StockInvestCost` | 股票投资－成本 | number(19,4) | ✓ | 1.09% |  |
| 17 | `ShareInvestValueAdded` | 股票投资－估值增值 | number(19,4) | ✓ | 1.07% |  |
| 18 | `BondInvestMarketValue` | 债券投资－市值 | number(19,4) | ✓ | 65.47% |  |
| 19 | `BondInvestCost` | 债券投资－成本 | number(19,4) | ✓ | 1.12% |  |
| 20 | `BondInvestValueAdded` | 债券投资－估值增值 | number(19,4) | ✓ | 1.09% |  |
| 21 | `WarrantInvestMarketValue` | 权证投资-市值 | number(19,4) | ✓ | 0.25% |  |
| 22 | `WarrantInvestCost` | 权证投资-成本 | number(19,4) | ✓ | 0.24% |  |
| 23 | `WarrantInvestValueAdded` | 权证投资-估值增值 | number(19,4) | ✓ | 0.22% |  |
| 24 | `OtherInvestMarketValue` | 其他投资-市值 | number(19,4) | ✓ | 0.0% |  |
| 25 | `OtherInvestCost` | 其他投资-成本 | number(19,4) | ✓ | 0.0% |  |
| 26 | `OtherInvestValueAdded` | 其他投资-估值增值 | number(19,4) | ✓ | 0.01% |  |
| 27 | `StockOption` | 配股权证 | number(19,4) | ✓ | 0.04% |  |
| 28 | `BoughtSellbackSecu` | 买入返售证券 | number(19,4) | ✓ | 23.58% |  |
| 29 | `DeferredExpense` | 待摊费用 | number(19,4) | ✓ | 0.31% |  |
| 30 | `OtherAsset` | 其他资产 | number(19,4) | ✓ | 7.43% |  |
| 31 | `TotalAsset` | 资产合计 | number(19,4) | ✓ | 100.0% |  |
| 32 | `SecuSettlementPayables` | 应付证券清算款 | number(19,4) | ✓ | 49.53% |  |
| 33 | `RedemptionMoneyPayable` | 应付赎回款 | number(19,4) | ✓ | 68.71% |  |
| 34 | `RedemptionFeePayable` | 应付赎回费 | number(19,4) | ✓ | 0.64% |  |
| 35 | `ManagementFeePayable` | 应付管理人报酬 | number(19,4) | ✓ | 99.72% |  |
| 36 | `TrustFeePayable` | 应付托管费 | number(19,4) | ✓ | 99.91% |  |
| 37 | `PerformancePayment` | 业绩报酬 | number(19,4) | ✓ | 0.0% |  |
| 38 | `ProfitPayable` | 应付收益 | number(19,4) | ✓ | 4.01% |  |
| 39 | `AccountPayable` | 应付帐款 | number(19,4) | ✓ | 0.07% |  |
| 40 | `CommisionPayable` | 应付佣金 | number(19,4) | ✓ | 49.88% |  |
| 41 | `AllocationFundPayable` | 应付配股款 | number(19,4) | ✓ | 0.0% |  |
| 42 | `TaxPayable` | ***未交税金 | number(19,4) | ✓ | 44.1% |  |
| 43 | `BondDistributionPayable` | ***应付债券分销款 | number(19,4) | ✓ | 0.0% |  |
| 44 | `InterestPayable` | 应付利息 | number(19,4) | ✓ | 15.33% |  |
| 45 | `SaleFeePayable` | 应付销售费用 | number(19,4) | ✓ | 50.06% |  |
| 46 | `OtherPayable` | 其他应付款 | number(19,4) | ✓ | 1.18% |  |
| 47 | `SoldRepoSecuProceeds` | 卖出回购证券款 | number(19,4) | ✓ | 31.83% |  |
| 48 | `ShortTermLoan` | ***短期借款 | number(19,4) | ✓ | 0.31% |  |
| 49 | `AccruedExpense` | 预提费用 | number(19,4) | ✓ | 1.14% |  |
| 50 | `OtherDebts` | 其他负债 | number(19,4) | ✓ | 98.74% |  |
| 51 | `TotalLiability` | 负债合计 | number(19,4) | ✓ | 100.0% |  |
| 52 | `Capital` | 实收基金 | number(19,4) | ✓ | 99.99% |  |
| 53 | `UnrealizedProfit` | 未实现利得 | number(19,4) | ✓ | 1.14% |  |
| 54 | `RetainedProfit` | 未分配收益 | number(19,4) | ✓ | 95.1% |  |
| 55 | `OtherEquity` | 其他权益 | number(19,4) | ✓ | 0.0% |  |
| 56 | `TotalShareHolderEquity` | 持有人权益合计 | number(19,4) | ✓ | 100.0% |  |
| 57 | `TotalLiabilityAndEquity` | 负债和所有者权益合计 | number(19,4) | ✓ | 100.0% |  |
| 58 | `UnitNV` | 基金单位净值 | number(19,4) | ✓ | 0.94% |  |
| 59 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 60 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金资产负债表 数据
SELECT *
FROM mf_balancesheet
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
