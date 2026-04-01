# MF_BalanceSheetNew

**中文名**: 公募基金资产负债表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BalanceSheetNew` |
| MySQL表名 | `mf_balancesheetnew` |
| 中文名 | 公募基金资产负债表_新会计准则 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 102 |
| 版本 | 1.02 |

## 表描述

1.包含依据2007年新会计准则披露的基金资产负债表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一基金在报告期末的两种财务报告，即未调整报表和调整后报表。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
4.该表中各财务科目下数据对应的货币单位均为人民币元。
5.历史数据：1998年12月起-至今。
6.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND ... |
| 5 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 6 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 7 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 8 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 9 | `Mark` | 调整标志 | number(10) | ✗ | 100.0% | 调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1... |
| 10 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 11 | `Deposit` | 银行存款 | number(19,4) | ✓ | 68.25% |  |
| 12 | `CashEquivalents` | 货币资金 | number(19,4) | ✓ | 31.73% |  |
| 13 | `SettlementProvi` | 结算备付金 | number(19,4) | ✓ | 81.86% |  |
| 14 | `RefundableDeposit` | 存出保证金 | number(19,4) | ✓ | 82.16% |  |
| 15 | `TradingAssets` | 交易性金融资产 | number(19,4) | ✓ | 98.01% |  |
| 16 | `StockInvestment` | 其中:股票投资 | number(19,4) | ✓ | 67.25% |  |
| 17 | `BondInvestment` | 其中:债券投资(交易性金融资产) | number(19,4) | ✓ | 65.2% |  |
| 18 | `ABSInvestment` | 其中:资产支持证券投资 | number(19,4) | ✓ | 5.66% |  |
| 19 | `FundInvestment` | 其中:基金投资 | number(19,4) | ✓ | 6.63% |  |
| 20 | `WarrentInvestment` | 其中:权证投资 | number(19,4) | ✓ | 0.21% |  |
| 21 | `RMetalInvestment` | 其中:贵金属投资 | number(19,4) | ✓ | 0.18% |  |
| 22 | `DerivativeAssets` | 衍生金融资产 | number(19,4) | ✓ | 0.76% |  |
| 23 | `BoughtSellbackAssets` | 买入返售金融资产 | number(19,4) | ✓ | 23.83% |  |
| 24 | `DebtInvestment` | 债权投资 | number(19,4) | ✓ | 0.77% |  |
| 25 | `BondInvestmentB` | 其中:债券投资 | number(19,4) | ✓ | 0.77% |  |
| 26 | `OthDebtInvestment` | 其他债权投资 | number(19,4) | ✓ | 0.0% |  |
| 27 | `OthEquityInstrument` | 其他权益工具投资 | number(19,4) | ✓ | 0.0% |  |
| 28 | `InterestReceivables` | 应收利息 | number(19,4) | ✓ | 50.12% |  |
| 29 | `SecuSettlementReceivables` | 应收清算款 | number(19,4) | ✓ | 46.05% |  |
| 30 | `DividendReceivables` | 应收股利 | number(19,4) | ✓ | 11.1% |  |
| 31 | `ApplyingReceivables` | 应收申购款 | number(19,4) | ✓ | 70.19% |  |
| 32 | `BillReceivable` | 应收票据 | number(19,4) | ✓ | 0.0% |  |
| 33 | `Inventories` | 存货 | number(19,4) | ✓ | 0.03% |  |
| 34 | `ContractualAssets` | 合同资产 | number(19,4) | ✓ | 0.0% |  |
| 35 | `HoldAndFSAssets` | 持有待售资产 | number(19,4) | ✓ | 0.0% |  |
| 36 | `LongTermEquityInvest` | 长期股权投资 | number(19,4) | ✓ | 0.0% |  |
| 37 | `InvestmentProperty` | 投资性房地产 | number(19,4) | ✓ | 0.09% |  |
| 38 | `FixedAssets` | 固定资产 | number(19,4) | ✓ | 0.12% |  |
| 39 | `ConstruInProcess` | 在建工程 | number(19,4) | ✓ | 0.03% |  |
| 40 | `UsufructAssets` | 使用权资产 | number(19,4) | ✓ | 0.01% |  |
| 41 | `IntangibleAssets` | 无形资产 | number(19,4) | ✓ | 0.07% |  |
| 42 | `DevelopmentExpenditure` | 开发支出 | number(19,4) | ✓ | 0.0% |  |
| 43 | `GoodWill` | 商誉 | number(19,4) | ✓ | 0.05% |  |
| 44 | `DeferredTaxAssets` | 递延所得税资产 | number(19,4) | ✓ | 0.16% |  |
| 45 | `AccountReceivables` | 应收帐款 | number(19,4) | ✓ | 0.22% |  |
| 46 | `OtherReceivables` | 其他应收款 | number(19,4) | ✓ | 0.47% |  |
| 47 | `DeferrredExpense` | 待摊费用 | number(19,4) | ✓ | 0.33% |  |
| 48 | `OtherAssets` | 其他资产 | number(19,4) | ✓ | 10.09% |  |
| 49 | `AExceptionalItems` | ##资产特殊项目 | number(19,4) | ✓ | 0.07% |  |
| 50 | `AAdjustmentItems` | ##资产调整项目 | number(19,4) | ✓ | 0.01% |  |
| 51 | `TotalAssets` | 资产总计 | number(19,4) | ✓ | 100.0% |  |
| 52 | `ShortTermLoan` | 短期借款 | number(19,4) | ✓ | 0.3% |  |
| 53 | `TradingLiability` | 交易性金融负债 | number(19,4) | ✓ | 0.27% |  |
| 54 | `DerivativeLiability` | 衍生金融负债 | number(19,4) | ✓ | 0.24% |  |
| 55 | `SoldBuybackSecuProceeds` | 卖出回购金融资产款 | number(19,4) | ✓ | 31.6% |  |
| 56 | `SecuSettlementPayables` | 应付证券清算款 | number(19,4) | ✓ | 49.36% |  |
| 57 | `RedemptionMoneyPayable` | 应付赎回款 | number(19,4) | ✓ | 68.13% |  |
| 58 | `RedemptionFeePayable` | 应付赎回费 | number(19,4) | ✓ | 0.57% |  |
| 59 | `ManagementFeePayable` | 应付管理人报酬 | number(19,4) | ✓ | 99.71% |  |
| 60 | `TrustFeePayable` | 应付托管费 | number(19,4) | ✓ | 99.9% |  |
| 61 | `SalesFeePayable` | 应付销售服务费 | number(19,4) | ✓ | 50.01% |  |
| 62 | `TransactionFeePayable` | 应付交易费用 | number(19,4) | ✓ | 47.34% |  |
| 63 | `TaxsPayable` | 应交税费 | number(19,4) | ✓ | 43.99% |  |
| 64 | `InterestPayable` | 应付利息 | number(19,4) | ✓ | 14.36% |  |
| 65 | `ProfitPayable` | 应付利润 | number(19,4) | ✓ | 3.97% |  |
| 66 | `InvestAdviserPay` | 应付投资顾问费 | number(19,4) | ✓ | 0.0% |  |
| 67 | `DeferredTaxLiability` | 递延所得税负债 | number(19,4) | ✓ | 0.22% |  |
| 68 | `NotesPayable` | 应付票据 | number(19,4) | ✓ | 0.0% |  |
| 69 | `AccountPayable` | 应付帐款 | number(19,4) | ✓ | 0.21% |  |
| 70 | `SalariesPayable` | 应付职工薪酬 | number(19,4) | ✓ | 0.03% |  |
| 71 | `ContractLiability` | 合同负债 | number(19,4) | ✓ | 0.04% |  |
| 72 | `HoldAndFSLi` | 持有待售负债 | number(19,4) | ✓ | 0.0% |  |
| 73 | `LongTermLoan` | 长期借款 | number(19,4) | ✓ | 0.04% |  |
| 74 | `EstimateLiability` | 预计负债 | number(19,4) | ✓ | 0.01% |  |
| 75 | `LeaseLiabilities` | 租赁负债 | number(19,4) | ✓ | 0.01% |  |
| 76 | `DeferredProceeds` | 递延收益 | number(19,4) | ✓ | 0.02% |  |
| 77 | `OtherPayable` | 其他应付款 | number(19,4) | ✓ | 1.1% |  |
| 78 | `AccruedExpense` | 预提费用 | number(19,4) | ✓ | 1.06% |  |
| 79 | `OtherLiability` | 其他负债 | number(19,4) | ✓ | 98.51% |  |
| 80 | `LExceptionalItems` | ##负债特殊项目 | number(19,4) | ✓ | 0.02% |  |
| 81 | `LAdjustmentItems` | ##负债调整项目 | number(19,4) | ✓ | 0.01% |  |
| 82 | `TotalLiability` | 负债合计 | number(19,4) | ✓ | 100.0% |  |
| 83 | `PaidInCapital` | 实收基金 | number(19,4) | ✓ | 99.98% |  |
| 84 | `RetainedProfit` | 未分配利润 | number(19,4) | ✓ | 95.13% |  |
| 85 | `OtherEquityinstruments` | 其他权益工具 | number(19,4) | ✓ | 0.0% |  |
| 86 | `CapitalReserveFund` | 资本公积 | number(19,4) | ✓ | 0.03% |  |
| 87 | `OtherCompositeIncome` | 其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 88 | `SpecificReserves` | 专项储备 | number(19,4) | ✓ | 0.02% |  |
| 89 | `SurplusReserveFund` | 盈余公积 | number(19,4) | ✓ | 0.0% |  |
| 90 | `OtherEquity` | 其他权益 | number(19,4) | ✓ | 0.0% | 其他权益(OtherEquity)：非标准披露字段，暂停维护。 |
| 91 | `SEExceptionalItems` | ##权益特殊项目 | number(19,4) | ✓ | 0.01% |  |
| 92 | `SEAdjustmentItems` | ##权益调整项目 | number(19,4) | ✓ | 0.01% |  |
| 93 | `TotalShareholderEquity` | 所有者权益合计 | number(19,4) | ✓ | 100.0% |  |
| 94 | `LEExceptionalItems` | ##负债和权益特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 95 | `LEAdjustmentItems` | ##负债和权益调整项目 | number(19,4) | ✓ | 0.0% |  |
| 96 | `TotalLiabilityAndEquity` | 负债和所有者权益总计 | number(19,4) | ✓ | 100.0% |  |
| 97 | `TotalFundShares` | 基金份额总额(份) | number(19,4) | ✓ | 98.7% |  |
| 98 | `UnitNV` | 基金份额净值 | number(19,4) | ✓ | 99.75% |  |
| 99 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 0.09% |  |
| 100 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 101 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 102 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (4,5,6)，得到公告类别的具体描述：4-上市公告书，5-年度报告，6-中期报告。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。

### Mark (调整标志)

调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### OtherEquity (其他权益)

其他权益(OtherEquity)：非标准披露字段，暂停维护。

## SQL示例

```sql
-- 查询 公募基金资产负债表_新会计准则 数据
SELECT *
FROM mf_balancesheetnew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
