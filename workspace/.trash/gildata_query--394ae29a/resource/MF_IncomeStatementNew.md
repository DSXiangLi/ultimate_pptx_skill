# MF_IncomeStatementNew

**中文名**: 公募基金利润表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IncomeStatementNew` |
| MySQL表名 | `mf_incomestatementnew` |
| 中文名 | 公募基金利润表_新会计准则 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 77 |
| 版本 | 1.04 |

## 表描述

1.包含依据2007年新会计准则披露的基金利润表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
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
| 8 | `StartDate` | 开始日期 | date | ✓ | 100.0% |  |
| 9 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 10 | `Mark` | 调整标志 | number(10) | ✗ | 100.0% | 调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1... |
| 11 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 12 | `OperatingRevenue` | 营业收入 | number(19,4) | ✓ | 0.16% |  |
| 13 | `InterestIncome` | 利息收入 | number(19,4) | ✓ | 100.0% |  |
| 14 | `DepositInterestIncome` | 其中:存款利息收入 | number(19,4) | ✓ | 99.78% |  |
| 15 | `BondInterestIncome` | 债券利息收入 | number(19,4) | ✓ | 43.13% |  |
| 16 | `ABSInterestIncome` | 资产支持证券利息收入 | number(19,4) | ✓ | 5.06% |  |
| 17 | `SellbackAssetsIncome` | 买入返售金融资产收入 | number(19,4) | ✓ | 60.75% |  |
| 18 | `SLInterestIncome` | 证券出借利息收入 | number(19,4) | ✓ | 0.74% |  |
| 19 | `OtherInterestIncome` | 其他利息收入 | number(19,4) | ✓ | 1.43% |  |
| 20 | `InvestmentIncome` | 投资收益 | number(19,4) | ✓ | 97.89% |  |
| 21 | `FundInvestIncome` | 其中:基金投资收益 | number(19,4) | ✓ | 6.84% |  |
| 22 | `StockInvestmentIncome` | 股票投资收益 | number(19,4) | ✓ | 69.53% |  |
| 23 | `BondInvestmentIncome` | 债券投资收益 | number(19,4) | ✓ | 74.63% |  |
| 24 | `ABSInvestmentIncome` | 资产支持证券投资收益 | number(19,4) | ✓ | 5.46% |  |
| 25 | `RmetalInvestmentIncome` | 贵金属投资收益 | number(19,4) | ✓ | 0.39% |  |
| 26 | `DerivativeInvestIncome` | 衍生工具收益 | number(19,4) | ✓ | 8.34% |  |
| 27 | `DividendIncome` | 股利收益 | number(19,4) | ✓ | 68.56% |  |
| 28 | `AmortisedcostIncome` | 以摊余成本计量的金融资产终止确认产生的收益 | number(19,4) | ✓ | 0.05% |  |
| 29 | `OtherInvestmentIncome` | 其他投资收益 | number(19,4) | ✓ | 0.19% |  |
| 30 | `FairValueChangeIncome` | 公允价值变动收益 | number(19,4) | ✓ | 93.18% |  |
| 31 | `ExchangeIncome` | 汇兑收益 | number(19,4) | ✓ | 2.59% |  |
| 32 | `AssetDealIncome` | 资产处置收益 | number(19,4) | ✓ | 0.01% |  |
| 33 | `OtherRevenue` | 其他收益 | number(19,4) | ✓ | 0.07% |  |
| 34 | `OtherIncome` | 其他收入 | number(19,4) | ✓ | 78.76% |  |
| 35 | `IncomeExceptionalItems` | ##收入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 36 | `IncomeAdjustmentItems` | ##收入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 37 | `TotalRevenue` | 收入合计 | number(19,4) | ✓ | 100.0% |  |
| 38 | `OperatingCost` | 营业成本 | number(19,4) | ✓ | 0.16% |  |
| 39 | `MangementExpense` | 管理人报酬 | number(19,4) | ✓ | 99.85% |  |
| 40 | `TrusteeExpense` | 托管费 | number(19,4) | ✓ | 99.97% |  |
| 41 | `SaleExpense` | 销售服务费 | number(19,4) | ✓ | 50.77% |  |
| 42 | `InvestAdviserFees` | 投资顾问费 | number(19,4) | ✓ | 0.01% |  |
| 43 | `TransactionExpense` | 交易费用 | number(19,4) | ✓ | 43.63% |  |
| 44 | `CreditImpairmentL` | 信用减值损失 | number(19,4) | ✓ | 0.67% |  |
| 45 | `AssetImpairmentLoss` | 资产减值损失 | number(19,4) | ✓ | 0.02% |  |
| 46 | `InterestExpense` | 利息支出 | number(19,4) | ✓ | 46.45% |  |
| 47 | `SoldRepoSecuExpense` | 其中:卖出回购金融资产支出 | number(19,4) | ✓ | 46.16% |  |
| 48 | `TaxSurcharges` | 税金及附加 | number(19,4) | ✓ | 50.45% |  |
| 49 | `OtherExpense` | 其他费用 | number(19,4) | ✓ | 99.77% |  |
| 50 | `OperatingExpense` | 销售费用 | number(19,4) | ✓ | 0.01% |  |
| 51 | `AdministrationExpense` | 管理费用 | number(19,4) | ✓ | 0.13% |  |
| 52 | `RAndD` | 研发费用 | number(19,4) | ✓ | 0.0% |  |
| 53 | `FinancialExpense` | 财务费用 | number(19,4) | ✓ | 0.15% |  |
| 54 | `ExpenseExceptionalItems` | ##费用特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 55 | `ExpenseAdjustmentItems` | ##费用调整项目 | number(19,4) | ✓ | 0.02% |  |
| 56 | `TotalExpense` | 费用合计 | number(19,4) | ✓ | 100.0% |  |
| 57 | `OtherItemsEffectingOP` | ##营业利润特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 58 | `AdjustEffectOP` | ##营业利润调整项目 | number(19,4) | ✓ | 0.0% |  |
| 59 | `OperatingProfit` | 营业利润 | number(19,4) | ✓ | 0.16% |  |
| 60 | `NonoperatingIncome` | 加:营业外收入 | number(19,4) | ✓ | 0.11% |  |
| 61 | `NonoperatingExpense` | 减:营业外支出 | number(19,4) | ✓ | 0.05% |  |
| 62 | `PastProfitAndLoss` | 以前年度损益调整 | number(19,4) | ✓ | 0.0% |  |
| 63 | `ProfitExceptionalItems` | ##利润特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 64 | `ProfitAdjustmentItems` | ##利润调整项目 | number(19,4) | ✓ | 0.01% |  |
| 65 | `TotalProfit` | 利润总额 | number(19,4) | ✓ | 100.0% |  |
| 66 | `IncomeTaxCost` | 减:所得税费用 | number(19,4) | ✓ | 0.19% |  |
| 67 | `OtherItemsEffectingNP` | ##净利润特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 68 | `AdjustEffectNP` | ##净利润调整项目 | number(19,4) | ✓ | 0.0% |  |
| 69 | `NetProfit` | 净利润 | number(19,4) | ✓ | 100.0% |  |
| 70 | `OperSustNetP` | 持续经营净利润 | number(19,4) | ✓ | 0.15% |  |
| 71 | `DisconOperNetP` | 终止经营净利润 | number(19,4) | ✓ | 0.0% |  |
| 72 | `OtherCompositeIncome` | 其他综合收益的税后净额 | number(19,4) | ✓ | 0.0% |  |
| 73 | `TotalCompositeIncome` | 综合收益总额 | number(19,4) | ✓ | 41.08% |  |
| 74 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 0.0% |  |
| 75 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 76 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 77 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (5,6)，得到公告类别的具体描述：5-年度报告，6-中期报告。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。

### Mark (调整标志)

调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

## SQL示例

```sql
-- 查询 公募基金利润表_新会计准则 数据
SELECT *
FROM mf_incomestatementnew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
