# Index_FinancialData

**中文名**: 指数财务数据

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_FinancialData` |
| MySQL表名 | `index_financialdata` |
| 中文名 | 指数财务数据 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 季度更新 |
| 字段数量 | 109 |
| 版本 | 1 |

## 表描述

内容说明：本表记录常用A股指数的财务报告主要科目数据，收录未调整的合并报表数据，该表中各财务科目的单位均为人民币元。
数据范围：A股指数、2000-03-31至今
信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `IndexNC` | 指数成份数量 | number(10) | ✓ | 100.0% |  |
| 6 | `CalcNC` | 计算用成份股数量 | number(10) | ✓ | 100.0% |  |
| 7 | `Cash` | 货币资金 | number(20,4) | ✓ | 78.13% |  |
| 8 | `BillReceivable` | 应收票据 | number(20,4) | ✓ | 99.56% |  |
| 9 | `AccountReceivable` | 应收账款 | number(20,4) | ✓ | 99.57% |  |
| 10 | `AdvancePayment` | 预付款项 | number(20,4) | ✓ | 99.5% |  |
| 11 | `Inventories` | 存货 | number(20,4) | ✓ | 99.57% |  |
| 12 | `OtherCurrentAssets` | 其他流动资产 | number(20,4) | ✓ | 97.76% |  |
| 13 | `TotalCurrentAssets` | 流动资产合计 | number(20,4) | ✓ | 99.57% |  |
| 14 | `LongtermEquityInvest` | 长期股权投资 | number(20,4) | ✓ | 99.82% |  |
| 15 | `InvestmentProperty` | 投资性房地产 | number(20,4) | ✓ | 95.68% |  |
| 16 | `TotalFixedAsset` | 固定资产合计 | number(20,4) | ✓ | 99.97% |  |
| 17 | `TConstruInProcess` | 在建工程合计 | number(20,4) | ✓ | 99.87% |  |
| 18 | `ConstruInProcess` | 在建工程 | number(20,4) | ✓ | 80.98% |  |
| 19 | `IntangibleAssets` | 无形资产 | number(20,4) | ✓ | 99.92% |  |
| 20 | `LongDeferredExpense` | 长期待摊费用 | number(20,4) | ✓ | 99.54% |  |
| 21 | `DeferredTaxAssets` | 递延所得税资产 | number(20,4) | ✓ | 98.37% |  |
| 22 | `OtherNonCurrentAssets` | 其他非流动资产 | number(20,4) | ✓ | 94.85% |  |
| 23 | `TotalNonCurrentAssets` | 非流动资产合计 | number(20,4) | ✓ | 99.96% |  |
| 24 | `TotalAssets` | 资产总计 | number(20,4) | ✓ | 99.97% |  |
| 25 | `ShortTermLoan` | 短期借款 | number(20,4) | ✓ | 99.52% |  |
| 26 | `NotesPayable` | 应付票据 | number(20,4) | ✓ | 97.19% |  |
| 27 | `AccountsPayable` | 应付账款 | number(20,4) | ✓ | 97.78% |  |
| 28 | `AdvanceReceipts` | 预收款项 | number(20,4) | ✓ | 99.56% |  |
| 29 | `SalariesPayable` | 应付职工薪酬 | number(20,4) | ✓ | 99.95% |  |
| 30 | `TaxsPayable` | 应交税费 | number(20,4) | ✓ | 99.95% |  |
| 31 | `OtherPayableED` | 其他应付款(含利息和股利) | number(20,4) | ✓ | 99.96% |  |
| 32 | `NonCurrentLiabilityIn1Year` | 一年内到期的非流动负债 | number(20,4) | ✓ | 98.57% |  |
| 33 | `OtherCurrentLiability` | 其他流动负债 | number(20,4) | ✓ | 97.24% |  |
| 34 | `TotalCurrentLiability` | 流动负债合计 | number(20,4) | ✓ | 99.57% |  |
| 35 | `LongtermLoan` | 长期借款 | number(20,4) | ✓ | 99.06% |  |
| 36 | `BondsPayable` | 应付债券 | number(20,4) | ✓ | 94.91% |  |
| 37 | `LTAccountPayableTotal` | 长期应付款合计 | number(20,4) | ✓ | 98.38% |  |
| 38 | `DeferredTaxLiability` | 递延所得税负债 | number(20,4) | ✓ | 98.39% |  |
| 39 | `OtherNonCurrentLiability` | 其他非流动负债 | number(20,4) | ✓ | 96.35% |  |
| 40 | `TotalNonCurrentLiability` | 非流动负债合计 | number(20,4) | ✓ | 99.96% |  |
| 41 | `TotalLiability` | 负债合计 | number(20,4) | ✓ | 99.96% |  |
| 42 | `PaidInCapital` | 实收资本(或股本) | number(20,4) | ✓ | 99.96% |  |
| 43 | `CapitalReserveFund` | 资本公积 | number(20,4) | ✓ | 99.95% |  |
| 44 | `OtherCompositeIncome` | 其他综合收益 | number(20,4) | ✓ | 82.61% |  |
| 45 | `SurplusReserveFund` | 盈余公积 | number(20,4) | ✓ | 99.95% |  |
| 46 | `RetainedProfit` | 未分配利润 | number(20,4) | ✓ | 99.95% |  |
| 47 | `SEWithoutMI` | 归属母公司所有者权益(或股东权益)合计 | number(20,4) | ✓ | 99.97% |  |
| 48 | `SECParentCompanyOwners` | 归属于母公司普通股股东权益 | number(20,4) | ✓ | 99.97% |  |
| 49 | `MinorityInterests` | 少数股东权益 | number(20,4) | ✓ | 99.83% |  |
| 50 | `TotalShareholderEquity` | 所有者权益(或股东权益)合计 | number(20,4) | ✓ | 99.96% |  |
| 51 | `TotalOperatingRevenue` | 营业总收入 | number(20,4) | ✓ | 99.99% |  |
| 52 | `OperatingRevenue` | 营业收入 | number(20,4) | ✓ | 99.99% |  |
| 53 | `SalesRevenue` | 主营业务收入 | number(20,4) | ✓ | 65.32% |  |
| 54 | `TotalOperatingCost` | 营业总成本 | number(20,4) | ✓ | 99.59% |  |
| 55 | `OperatingCost` | 营业成本 | number(20,4) | ✓ | 99.59% |  |
| 56 | `SalesCost` | 主营业务成本 | number(20,4) | ✓ | 65.22% |  |
| 57 | `OperatingExpense` | 销售费用 | number(20,4) | ✓ | 99.59% |  |
| 58 | `AdministrationExpense` | 管理费用 | number(20,4) | ✓ | 99.59% |  |
| 59 | `FinancialExpense` | 财务费用 | number(20,4) | ✓ | 99.59% |  |
| 60 | `RAndD` | 研发费用 | number(20,4) | ✓ | 99.59% |  |
| 61 | `AssetImpairmentLoss` | 资产减值损失 | number(20,4) | ✓ | 97.12% |  |
| 62 | `InvestIncome` | 投资净收益 | number(20,4) | ✓ | 100.0% |  |
| 63 | `ExchangeIncome` | 汇兑收益 | number(20,4) | ✓ | 77.64% |  |
| 64 | `FairValueChangeIncome` | 公允价值变动净收益 | number(20,4) | ✓ | 94.93% |  |
| 65 | `OperatingProfit` | 营业利润 | number(20,4) | ✓ | 99.99% |  |
| 66 | `NonoperatingIncome` | 营业外收入 | number(20,4) | ✓ | 100.0% |  |
| 67 | `NonoperatingExpense` | 营业外支出 | number(20,4) | ✓ | 99.99% |  |
| 68 | `TotalProfit` | 利润总额 | number(20,4) | ✓ | 99.99% |  |
| 69 | `IncomeTaxCost` | 所得税费用 | number(20,4) | ✓ | 100.0% |  |
| 70 | `NetProfit` | 净利润 | number(20,4) | ✓ | 100.0% |  |
| 71 | `NPParentCompanyOwners` | 归属于母公司所有者的净利润 | number(20,4) | ✓ | 100.0% |  |
| 72 | `NPCParentCompanyOwners` | 归属于母公司普通股股东的净利润 | number(20,4) | ✓ | 100.0% |  |
| 73 | `GoodsSaleServiceRenderCash` | 销售商品、提供劳务收到的现金 | number(20,4) | ✓ | 99.32% |  |
| 74 | `TaxLevyRefund` | 收到的税费返还 | number(20,4) | ✓ | 98.89% |  |
| 75 | `OtherCashInRelatedOperate` | 收到其他与经营活动有关的现金 | number(20,4) | ✓ | 99.7% |  |
| 76 | `SubtotalOperateCashInflow` | 经营活动现金流入小计 | number(20,4) | ✓ | 99.71% |  |
| 77 | `GoodsServicesCashPaid` | 购买商品、接受劳务支付的现金 | number(20,4) | ✓ | 99.29% |  |
| 78 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金 | number(20,4) | ✓ | 99.71% |  |
| 79 | `AllTaxesPaid` | 支付的各项税费 | number(20,4) | ✓ | 99.71% |  |
| 80 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金 | number(20,4) | ✓ | 99.71% |  |
| 81 | `SubtotalOperateCashOutflow` | 经营活动现金流出小计 | number(20,4) | ✓ | 99.71% |  |
| 82 | `NetOperateCashFlow` | 经营活动产生的现金流量净额 | number(20,4) | ✓ | 99.71% |  |
| 83 | `InvestWithdrawalCash` | 收回投资收到的现金 | number(20,4) | ✓ | 98.76% |  |
| 84 | `Investproceeds` | 取得投资收益收到的现金 | number(20,4) | ✓ | 99.05% |  |
| 85 | `FixIntanOtherAssetDispoCash` | 处置固定资产、无形资产和其他长期资产收回的现金净额 | number(20,4) | ✓ | 99.49% |  |
| 86 | `OtherCashFromInvestAct` | 收到其他与投资活动有关的现金 | number(20,4) | ✓ | 98.47% |  |
| 87 | `SubtotalInvestCashInflow` | 投资活动现金流入小计 | number(20,4) | ✓ | 99.64% |  |
| 88 | `FixIntanOtherAssetAcquiCash` | 购建固定资产、无形资产和其他长期资产支付的现金 | number(20,4) | ✓ | 99.7% |  |
| 89 | `InvestCashPaid` | 投资支付的现金 | number(20,4) | ✓ | 99.12% |  |
| 90 | `OtherCashToInvestAct` | 支付其他与投资活动有关的现金 | number(20,4) | ✓ | 97.84% |  |
| 91 | `SubtotalInvestCashOutflow` | 投资活动现金流出小计 | number(20,4) | ✓ | 99.71% |  |
| 92 | `NetInvestCashFlow` | 投资活动产生的现金流量净额 | number(20,4) | ✓ | 99.71% |  |
| 93 | `CashFromInvest` | 吸收投资收到的现金 | number(20,4) | ✓ | 98.03% |  |
| 94 | `CashFromBorrowing` | 取得借款收到的现金 | number(20,4) | ✓ | 99.24% |  |
| 95 | `CashFromBondsIssue` | 发行债券收到的现金 | number(20,4) | ✓ | 81.46% |  |
| 96 | `OtherFinanceActCash` | 收到其他与筹资活动有关的现金 | number(20,4) | ✓ | 98.3% |  |
| 97 | `OtherFinanceActPayment` | 支付其他与筹资活动有关的现金 | number(20,4) | ✓ | 98.9% |  |
| 98 | `SubtotalFinanceCashInflow` | 筹资活动现金流入小计 | number(20,4) | ✓ | 99.63% |  |
| 99 | `BorrowingRepayment` | 偿还债务支付的现金 | number(20,4) | ✓ | 99.58% |  |
| 100 | `DividendInterestPayment` | 分配股利、利润或偿付利息支付的现金 | number(20,4) | ✓ | 99.67% |  |
| 101 | `SubtotalFinanceCashOutflow` | 筹资活动现金流出小计 | number(20,4) | ✓ | 99.69% |  |
| 102 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额 | number(20,4) | ✓ | 99.69% |  |
| 103 | `CashEquivalentIncrease` | 现金及现金等价物净增加额 | number(20,4) | ✓ | 99.71% |  |
| 104 | `EndPeriodCashEquivalent` | 期末现金及现金等价物余额 | number(20,4) | ✓ | 96.52% |  |
| 105 | `BeginPeriodCash` | 期初现金及现金等价物余额 | number(20,4) | ✓ | 96.52% |  |
| 106 | `ExchanRateChangeEffect` | 汇率变动对现金及现金等价物的影响 | number(20,4) | ✓ | 98.92% |  |
| 107 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 108 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 109 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

## SQL示例

```sql
-- 查询 指数财务数据 数据
SELECT *
FROM index_financialdata
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
