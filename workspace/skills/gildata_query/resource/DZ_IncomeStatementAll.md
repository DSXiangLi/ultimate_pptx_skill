# DZ_IncomeStatementAll

**中文名**: 利润分配表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_IncomeStatementAll` |
| MySQL表名 | `dz_incomestatementall` |
| 中文名 | 利润分配表_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 165 |
| 版本 | 1.06 |

## 表描述

1.内容说明：
1.1反映上市、发债、非上市非发债公司依据2007年新会计准则在在年报、中报、季报中披露的利润表数据；并依据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
1.2收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报表以及调整后的母公司报表。
1.3若某个报告期的数据有多次调整，则该表展示历次调整数据。
1.4该表中各财务科目的单位均为人民币元。
1.5带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
2.数据范围：1989-12-31至今
3.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 94.2% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 5 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311  and... |
| 6 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并（IfMerged），该字段固定以下常量：1-合并报表；2-母公司报表 |
| 9 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整（IfAdjusted），该字段固定以下常量：1-调整；2-未调整；4-季度未调整；5-季度调整 注：季度数据是... |
| 10 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志... |
| 11 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 12 | `EnterpriseType` | 报表格式类型 | number(10) | ✗ | 100.0% | 报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公... |
| 13 | `TotalOperatingRevenue` | 一、营业总收入 | number(19,4) | ✓ | 99.43% | 营业总收入（TotalOperatingRevenue）：对非金融类公司（报表披露类型=99），营业总收入=营业收入＋金... |
| 14 | `OperatingRevenue` | 营业收入 | number(19,4) | ✓ | 98.73% |  |
| 15 | `SalesRevenue` | 其中:主营业务收入 | number(19,4) | ✓ | 45.89% |  |
| 16 | `OtherOperatingIncome` | 其中:其他业务收入 | number(19,4) | ✓ | 45.65% |  |
| 17 | `NetInterestIncome` | 利息净收入 | number(19,4) | ✓ | 6.64% | 利息净收入（NetInterestIncome）：一般为金融类企业披露科目；本字段优先展示收入模块披露的“利息净收入”，... |
| 18 | `InterestIncome` | 其中:利息收入 | number(19,4) | ✓ | 6.01% | 其中:利息收入（InterestIncome）：一般为金融类企业披露科目 |
| 19 | `InterestExpense` | 其中:利息支出 | number(19,4) | ✓ | 3.0% | 其中:利息支出（InterestExpense）：一般为金融类企业披露科目，本字段展示收入模块的利息支出； |
| 20 | `PremiumsEarned` | 已赚保费 | number(19,4) | ✓ | 1.36% | 已赚保费（PremiumsEarned）：一般为金融类:保险公司披露科目 |
| 21 | `PremiumsIncome` | 其中:保费业务收入 | number(19,4) | ✓ | 0.51% | 其中:保费业务收入（PremiumsIncome）：一般为金融类:保险公司/担保公司披露科目 |
| 22 | `ReinsuranceIncome` | 其中:保险业务收入:分保费收入 | number(19,4) | ✓ | 0.2% | 其中:保险业务收入:分保费收入（ReinsuranceIncome）：一般为金融类:保险公司披露科目 |
| 23 | `Reinsurance` | 其中:减:分出保费 | number(19,4) | ✓ | 0.41% | 其中:减:分出保费（Reinsurance）：一般为金融类:保险公司披露科目 |
| 24 | `UnearnedPremiumReserve` | 其中:减:提取未到期责任准备金 | number(19,4) | ✓ | 0.45% | 其中:减:提取未到期责任准备金（UnearnedPremiumReserve）：一般为金融类:保险公司披露科目 |
| 25 | `GuaranteeIncome` | 担保业务收入 | number(19,4) | ✓ | 0.06% | 担保业务收入（GuaranteeIncome）：一般为金融类:担保公司披露科目 |
| 26 | `NetCommissionIncome` | 手续费及佣金净收入 | number(19,4) | ✓ | 5.5% | 手续费及佣金净收入（NetCommissionIncome）：一般为金融类企业披露科目;本字段优先展示收入模块披露的“手... |
| 27 | `CommissionIncome` | 其中:手续费及佣金收入 | number(19,4) | ✓ | 4.57% | 其中:手续费及佣金收入（CommissionIncome）：一般为金融类企业披露科目 |
| 28 | `BrokerageIncome` | 其中:手续费及佣金收入:经纪业务手续费收入 | number(19,4) | ✓ | 0.12% | 其中:手续费及佣金收入:经纪业务手续费收入（BrokerageIncome）：一般为金融类:证券公司披露科目 |
| 29 | `InvestBankIncome` | 其中:手续费及佣金收入:投资银行业务手续费收入 | number(19,4) | ✓ | 0.12% | 其中:手续费及佣金收入:投资银行业务手续费收入（InvestBankIncome）：一般为金融类企业披露科目 |
| 30 | `AssetManageIncome` | 其中:手续费及佣金收入:资产管理业务手续费收入 | number(19,4) | ✓ | 0.11% | 其中:手续费及佣金收入:资产管理业务手续费收入（AssetManageIncome）：一般为金融类:证券公司披露科目 |
| 31 | `FundManageIncome` | 其中:手续费及佣金收入:基金管理业务手续费收入 | number(19,4) | ✓ | 0.05% | 其中:手续费及佣金收入:基金管理业务手续费收入（FundManageIncome）：一般为金融类:证券公司披露科目 |
| 32 | `InvestConsultIncome` | 其中:手续费及佣金收入:投资咨询业务收入 | number(19,4) | ✓ | 0.12% | 其中:手续费及佣金收入:投资咨询业务收入（InvestConsultIncome）：一般为金融类:证券公司披露科目 |
| 33 | `RiskManageIncome` | 其中:手续费及佣金收入:风险管理业务收入 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金收入:风险管理业务收入（RiskManageIncome）：一般为金融类:证券公司披露科目 |
| 34 | `InvestManageIncome` | 其中:手续费及佣金收入:投资管理业务收入 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金收入:投资管理业务收入（InvestManageIncome）：一般为金融类:证券公司披露科目 |
| 35 | `OtherAgencyIncome` | 其中:手续费及佣金收入:其他代理业务收入 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金收入:其他代理业务收入（OtherAgencyIncome）：一般为金融类:证券公司披露科目 |
| 36 | `CommissionExpense` | 其中:手续费及佣金支出 | number(19,4) | ✓ | 2.59% | 其中:手续费及佣金支出（CommissionExpense）：一般为金融类企业披露科目，本字段展示收入模块的手续费及佣金... |
| 37 | `BrokerageExpense` | 其中:手续费及佣金支出:经纪业务手续费支出 | number(19,4) | ✓ | 0.12% | 其中:手续费及佣金支出:经纪业务手续费支出（BrokerageExpense）：一般为金融类:证券公司披露科目；本字段展... |
| 38 | `InvestBankExpense` | 其中:手续费及佣金支出:投资银行业务手续费支出 | number(19,4) | ✓ | 0.11% | 其中:手续费及佣金支出:投资银行业务手续费支出（InvestBankExpense）：一般为金融类企业披露科目；本字段展... |
| 39 | `AssetManageExpense` | 其中:手续费及佣金支出:资产管理业务手续费支出 | number(19,4) | ✓ | 0.07% | 其中:手续费及佣金支出:资产管理业务手续费支出（AssetManageExpense）：一般为金融类:证券公司披露科目；... |
| 40 | `FundManageExpense` | 其中:手续费及佣金支出:基金管理业务手续费支出 | number(19,4) | ✓ | 0.02% | 其中:手续费及佣金收入:基金管理业务手续费支出（FundManageExpense）：一般为金融类:证券公司披露科目；本... |
| 41 | `InvestConsultExpense` | 其中:手续费及佣金支出:投资咨询业务支出 | number(19,4) | ✓ | 0.03% | 其中:手续费及佣金支出:投资咨询业务支出（InvestConsultExpense）：一般为金融类:证券公司披露科目；本... |
| 42 | `RiskManageExpense` | 其中:手续费及佣金支出:风险管理业务支出 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金支出:风险管理业务支出（RiskManageExpense）：一般为金融类:证券公司披露科目；本字段展... |
| 43 | `InvestManageExpense` | 其中:手续费及佣金支出:投资管理业务支出 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金支出:投资管理业务支出（InvestManageExpense）：一般为金融类:证券公司披露科目；本字... |
| 44 | `OtherAgencyExpense` | 其中:手续费及佣金支出:其他代理业务支出 | number(19,4) | ✓ | 0.0% | 其中:手续费及佣金支出:其他代理业务支出（OtherAgencyExpense）：一般为金融类:证券公司披露科目；本字段... |
| 45 | `NetProxySecuIncome` | 其中:代理买卖证券业务净收入 | number(19,4) | ✓ | 0.85% | 其中:代理买卖证券业务净收入（NetProxySecuIncome）：一般为金融类:证券公司披露科目 |
| 46 | `NetSubIssueSecuIncome` | 其中:证券承销业务净收入 | number(19,4) | ✓ | 0.83% | 其中:证券承销业务净收入（NetSubIssueSecuIncome）：一般为金融类:证券公司披露科目 |
| 47 | `NetTrustIncome` | 其中:受托客户资产管理业务净收入 | number(19,4) | ✓ | 0.74% | 其中:受托客户资产管理业务净收入（NetTrustIncome）：一般为金融类:证券公司披露科目 |
| 48 | `NetFundMgtIncome` | 其中:基金管理业务手续费净收入 | number(19,4) | ✓ | 0.01% | 其中:基金管理业务手续费净收入（NetFundMgtIncome）：一般为金融类:证券公司披露科目 |
| 49 | `OtherOperatingRevenue` | 其他收入 | number(19,4) | ✓ | 3.56% |  |
| 50 | `SpecialItemsOR` | ##营业收入OR营业总收入特殊项目 | number(19,4) | ✓ | 0.44% |  |
| 51 | `AdjustmentItemsOR` | ##营业收入OR营业总收入调整项目 | number(19,4) | ✓ | 0.21% |  |
| 52 | `TotalOperatingCost` | 二、营业总成本 | number(19,4) | ✓ | 98.59% | 营业总成本（TotalOperatingCost）：对非金融类公司（企业性质=99），营业总成本=营业成本＋营业税金及附... |
| 53 | `OperatingPayout` | 营业支出 | number(19,4) | ✓ | 4.15% |  |
| 54 | `InsuranceCommissionExpense` | 保险手续费及佣金支出 | number(19,4) | ✓ | 0.38% | 保险手续费及佣金支出（InsuranceCommissionExpense）：一般为金融类:保险公司披露科目 |
| 55 | `RefundedPremiums` | 退保金 | number(19,4) | ✓ | 0.67% | 退保金（RefundedPremiums）：一般为金融类:保险公司披露科目 |
| 56 | `PreInsurRSRV` | 提取保费准备金 | number(19,4) | ✓ | 0.08% | 提取保费准备金（PreInsurRSRV）：一般为金融类:保险公司披露科目 |
| 57 | `ExtractFutureRisk` | 提取期货风险准备金 | number(19,4) | ✓ | 0.04% | 提取期货风险准备金（ExtractFutureRisk）：一般为金融类:期货公司披露科目 |
| 58 | `WithdrawGuaranteeReser` | 提取担保业务准备金 | number(19,4) | ✓ | 0.04% | 提取担保业务准备金（WithdrawGuaranteeReser）：一般为金融类:担保公司披露科目 |
| 59 | `GuarantCompRSRV` | 提取担保赔偿准备金 | number(19,4) | ✓ | 0.13% | 提取担保赔偿准备金（GuarantCompRSRV）：一般为金融类:担保公司披露科目 |
| 60 | `NetClaimIncurred` | 赔付支出净额 | number(19,4) | ✓ | 0.85% | 赔付支出净额（NetClaimIncurred）：一般为金融类:保险公司披露科目 |
| 61 | `CompensationExpense` | 其中:赔付支出 | number(19,4) | ✓ | 0.55% | 其中:赔付支出（CompensationExpense）：一般为金融类:保险公司披露科目 |
| 62 | `AmortizationExpense` | 其中:减:摊回赔付支出 | number(19,4) | ✓ | 0.37% | 其中:减:摊回赔付支出（AmortizationExpense）：一般为金融类:保险公司披露科目 |
| 63 | `NetPremiumReserve` | 提取保险责任准备金净额 | number(19,4) | ✓ | 1.21% | 提取保险责任准备金净额（NetPremiumReserve）：一般为金融类:保险公司披露科目 |
| 64 | `PremiumReserve` | 其中:提取保险责任准备金 | number(19,4) | ✓ | 0.63% | 其中:提取保险责任准备金（PremiumReserve）：一般为金融类:保险公司披露科目 |
| 65 | `AmortizationPremiumReserve` | 其中:减:摊回保险责任准备金 | number(19,4) | ✓ | 0.38% | 其中:减:摊回保险责任准备金（AmortizationPremiumReserve）：一般为金融类:保险公司披露科目 |
| 66 | `PolicyDividendPayout` | 保单红利支出 | number(19,4) | ✓ | 0.64% | 保单红利支出（PolicyDividendPayout）：一般为金融类:保险公司披露科目 |
| 67 | `InsuranceServiceExpen` | 保险服务费用 | number(19,4) | ✓ | 0.02% |  |
| 68 | `ReinsAllocationPaid` | 分出保费的分摊 | number(19,4) | ✓ | 0.02% |  |
| 69 | `ReinsRecovered` | 减:摊回保险服务费用 | number(19,4) | ✓ | 0.02% |  |
| 70 | `InsNetInsFinanceExpen` | 承保财务损失 | number(19,4) | ✓ | 0.02% |  |
| 71 | `ReinHeldNetInsFinIncome` | 减:分出再保险财务收益 | number(19,4) | ✓ | 0.02% |  |
| 72 | `ReinsuranceCost` | 分保费用 | number(19,4) | ✓ | 0.73% | 分保费用（ReinsuranceCost）：一般为金融类:保险公司披露科目 |
| 73 | `OtherOperatingCost` | 其他成本 | number(19,4) | ✓ | 2.6% |  |
| 74 | `OperatingCost` | 营业成本 | number(19,4) | ✓ | 90.63% |  |
| 75 | `SalesCost` | 其中:主营业务成本 | number(19,4) | ✓ | 44.49% |  |
| 76 | `OtherOperationalCost` | 其中:其他业务成本 | number(19,4) | ✓ | 44.43% |  |
| 77 | `OperatingTaxSurcharges` | 营业税金及附加 | number(19,4) | ✓ | 95.95% |  |
| 78 | `OperatingExpense` | 销售费用 | number(19,4) | ✓ | 78.29% |  |
| 79 | `TotalAdminExpense` | 管理费用合计 | number(19,4) | ✓ | 98.41% |  |
| 80 | `AdministrationExpense` | 其中:管理费用 | number(19,4) | ✓ | 94.47% |  |
| 81 | `OperatingAndAdminExpense` | 其中:业务及管理费 | number(19,4) | ✓ | 4.1% | 其中:业务及管理费（OperatingAndAdminExpense）：一般为金融类企业披露科目 |
| 82 | `AmortizationReinsuranceCost` | 其中:减:摊回分保费用 | number(19,4) | ✓ | 0.37% | 其中:减:摊回分保费用（AmortizationReinsuranceCost）：一般为金融类:保险公司披露科目 |
| 83 | `RAndD` | 研发费用 | number(19,4) | ✓ | 29.62% |  |
| 84 | `FinancialExpense` | 财务费用 | number(19,4) | ✓ | 94.63% |  |
| 85 | `InterestFinExp` | 其中:利息费用(财务费用) | number(19,4) | ✓ | 37.27% |  |
| 86 | `InterestIncomeFin` | 其中:利息收入(财务费用) | number(19,4) | ✓ | 41.96% | 其中:利息收入(财务费用)(InterestIncomeFin)： 1、当原文披露的实际数值为收入项，则统一展示为“负值... |
| 87 | `ExplorationCost` | 勘探费用 | number(19,4) | ✓ | 0.03% |  |
| 88 | `CreditImpairmentL` | 信用减值损失(成本) | number(19,4) | ✓ | 1.94% | 信用减值损失（CreditImpairmentL）：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的通知... |
| 89 | `AssetImpairmentLoss` | 资产减值损失(成本) | number(19,4) | ✓ | 38.9% | 资产减值损失（AssetImpairmentLoss）：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的... |
| 90 | `SpecialItemsTOC` | ##营业支出OR营业总成本特殊项目 | number(19,4) | ✓ | 0.54% |  |
| 91 | `AdjustmentItemsTOC` | ##营业支出OR营业总成本调整项目 | number(19,4) | ✓ | 0.82% |  |
| 92 | `OtherNetRevenue` | 三、非经营性净收益 | number(19,4) | ✓ | 95.54% | 非经营性净收益（OtherNetRevenue）：聚源计算合计项，仅针对非金融类公司。计算公式=其他收益＋投资净收益＋汇... |
| 93 | `OtherRevenue` | 其他收益 | number(19,4) | ✓ | 46.95% |  |
| 94 | `InvestIncome` | 投资净收益 | number(19,4) | ✓ | 79.57% |  |
| 95 | `InvestIncomeAssociates` | 其中:对联营合营企业的投资收益 | number(19,4) | ✓ | 35.99% |  |
| 96 | `AmortisedcostIncome` | 其中:以摊余成本计量的金融资产终止确认收益 | number(19,4) | ✓ | 1.78% |  |
| 97 | `ExchangeIncome` | 汇兑收益 | number(19,4) | ✓ | 4.25% |  |
| 98 | `NetOpenHedgeIncome` | 净敞口套期收益 | number(19,4) | ✓ | 0.38% |  |
| 99 | `FairValueChangeIncome` | 公允价值变动净收益 | number(19,4) | ✓ | 28.87% |  |
| 100 | `CreditImpairmentP` | 信用减值损失(利润) | number(19,4) | ✓ | 29.68% |  |
| 101 | `AssetImpairmentLossP` | 资产减值损失(利润) | number(19,4) | ✓ | 24.01% |  |
| 102 | `AssetDealIncome` | 资产处置收益 | number(19,4) | ✓ | 28.96% |  |
| 103 | `OtherItemsEffectingOP` | ##营业利润特殊项目 | number(19,4) | ✓ | 6.8% |  |
| 104 | `AdjustedItemsEffectingOP` | ##营业利润调整项目 | number(19,4) | ✓ | 1.54% |  |
| 105 | `OperatingProfit` | 四、营业利润 | number(19,4) | ✓ | 99.02% |  |
| 106 | `NonoperatingIncome` | 加:营业外收入 | number(19,4) | ✓ | 89.49% |  |
| 107 | `NonoperatingExpense` | 减:营业外支出 | number(19,4) | ✓ | 88.45% |  |
| 108 | `NonCurrentAssetssDealLoss` | 其中:非流动资产处置净损失 | number(19,4) | ✓ | 17.09% |  |
| 109 | `OtherItemsEffectingTP` | ##利润总额特殊项目 | number(19,4) | ✓ | 3.19% |  |
| 110 | `AdjustedItemsEffectingTP` | ##利润总额调整项目 | number(19,4) | ✓ | 0.73% |  |
| 111 | `TotalProfit` | 五、利润总额 | number(19,4) | ✓ | 99.71% |  |
| 112 | `IncomeTaxCost` | 减:所得税费用 | number(19,4) | ✓ | 86.12% |  |
| 113 | `UncertainedInvestmentLosses` | 加:未确认的投资损失 | number(19,4) | ✓ | 0.67% |  |
| 114 | `OtherItemsEffectingNP` | ##净利润特殊项目 | number(19,4) | ✓ | 0.16% |  |
| 115 | `AdjustedItemsEffectingNP` | ##净利润调整项目 | number(19,4) | ✓ | 0.76% |  |
| 116 | `NetProfit` | 六、净利润 | number(19,4) | ✓ | 99.87% |  |
| 117 | `OperSustCateg` | (一)按经营持续性分类 | number(19,4) | ✓ | 1.45% |  |
| 118 | `OperSustNetP` | 持续经营净利润 | number(19,4) | ✓ | 49.36% |  |
| 119 | `DisconOperNetP` | 终止经营净利润 | number(19,4) | ✓ | 1.1% |  |
| 120 | `OwnershipCateg` | (二)按所有权归属分类 | number(19,4) | ✓ | 1.28% |  |
| 121 | `NPParentCompanyOwners` | 归属于母公司所有者的净利润 | number(19,4) | ✓ | 99.35% |  |
| 122 | `NPCParentCompanyOwners` | 其中:归属于母公司普通股股东的净利润 | number(19,4) | ✓ | 0.02% |  |
| 123 | `NPOtherEqinstruments` | 其中:归属于母公司其他权益工具持有者的净利润 | number(19,4) | ✓ | 0.02% |  |
| 124 | `MinorityProfit` | 少数股东损益 | number(19,4) | ✓ | 43.57% |  |
| 125 | `OtherItemsEffectingNPP` | ##母公司净利润特殊项目 | number(19,4) | ✓ | 0.02% |  |
| 126 | `AdjustedItemsEffectingNPP` | ##母公司净利润调整项目 | number(19,4) | ✓ | 0.6% |  |
| 127 | `OtherCompositeIncome` | 七、其他综合收益的税后净额 | number(19,4) | ✓ | 29.9% |  |
| 128 | `OCIParentCompanyOwners` | 归属于母公司所有者的其他综合收益的税后净额 | number(19,4) | ✓ | 17.1% |  |
| 129 | `OCINotInIncomeStatement` | (一)以后不能重分类进损益的其他综合收益 | number(19,4) | ✓ | 7.96% |  |
| 130 | `OCIReMearsure` | 1.1重新计量设定受益计划净负债或净资产的变动 | number(19,4) | ✓ | 1.57% |  |
| 131 | `OCIEquityNotInIS` | 1.2权益法下在被投资单位不能重分类进损益的其他综合收益 | number(19,4) | ✓ | 1.58% |  |
| 132 | `OthEquFVChange` | 1.3其他权益工具投资公允价值变动 | number(19,4) | ✓ | 6.38% |  |
| 133 | `CorporateCRChange` | 1.4企业自身信用风险公允价值变动 | number(19,4) | ✓ | 0.28% |  |
| 134 | `FinVarInConNotReProLoss` | 1.5不能转损益的保险合同金融变动 | number(19,4) | ✓ | 0.01% |  |
| 135 | `OCIInIncomeStatement` | (二)以后将重分类进损益的其他综合收益 | number(19,4) | ✓ | 20.34% |  |
| 136 | `OCIEquityInIS` | 2.1权益法下在被投资单位以后将重分类进损益的其他综合收益 | number(19,4) | ✓ | 5.23% |  |
| 137 | `OthDebtInvesChange` | 2.2其他债权投资公允价值变动 | number(19,4) | ✓ | 1.72% |  |
| 138 | `FinAssetROtherCI` | 2.3金融资产重分类计入其他综合收益的金额 | number(19,4) | ✓ | 0.42% |  |
| 139 | `OtherDebtInvestCIP` | 2.4其他债权投资信用减值准备 | number(19,4) | ✓ | 1.36% |  |
| 140 | `OCICFLoss` | 2.5现金流量套期损益的有效部分 | number(19,4) | ✓ | 1.67% |  |
| 141 | `OCIForeignCurrencyFSA` | 2.6外币财务报表折算差额 | number(19,4) | ✓ | 12.97% |  |
| 142 | `OCIFairValue` | 2.7可供出售金融资产公允价值变动损益 | number(19,4) | ✓ | 5.81% |  |
| 143 | `OCIToMaturityFA` | 2.8持有至到期投资重分类为可供出售金融资产损益 | number(19,4) | ✓ | 0.19% |  |
| 144 | `FinVarInConReProLoss` | 2.9可转损益的保险合同金融变动 | number(19,4) | ✓ | 0.02% |  |
| 145 | `FinVarReinConReProLoss` | 3.0可转损益的分出再保险合同金融变动 | number(19,4) | ✓ | 0.01% |  |
| 146 | `OCIOthers` | 3.1其他(以后能重分类进损益表的其他综合收益) | number(19,4) | ✓ | 1.47% |  |
| 147 | `OCIMinorityOwners` | 归属于少数股东的其他综合收益的税后净额 | number(19,4) | ✓ | 6.27% |  |
| 148 | `OtherItemsEffectingCI` | ##综合收益总额特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 149 | `AdjustedItemsEffectingCI` | ##综合收益总额调整项目 | number(19,4) | ✓ | 0.52% |  |
| 150 | `TotalCompositeIncome` | 八、综合收益总额 | number(19,4) | ✓ | 80.9% |  |
| 151 | `CIParentCompanyOwners` | 归属于母公司所有者的综合收益总额 | number(19,4) | ✓ | 48.02% |  |
| 152 | `CICParentCompanyOwners` | 其中:归属于母公司普通股股东的综合收益 | number(19,4) | ✓ | 0.02% |  |
| 153 | `CIOtherEqinstruments` | 其中:归属于母公司其他权益工具持有者的综合收益 | number(19,4) | ✓ | 0.01% |  |
| 154 | `CIMinorityOwners` | 归属于少数股东的综合收益总额 | number(19,4) | ✓ | 34.92% |  |
| 155 | `AdjustedItemsEffectingPCI` | ##母公司综合收益总额调整项目 | number(19,4) | ✓ | 0.48% |  |
| 156 | `BasicEPS` | 基本每股收益 | number(19,4) | ✓ | 38.78% |  |
| 157 | `DilutedEPS` | 稀释每股收益 | number(19,4) | ✓ | 37.25% |  |
| 158 | `TotalInterestExpense` | 利息支出合计 | number(19,4) | ✓ | 5.14% | 利息支出合计(TotalInterestExpense)：一般为金融类企业披露科目，本字段展示收入模块、成本模块披露的“... |
| 159 | `TotalCommExpense` | 手续费及佣金支出合计 | number(19,4) | ✓ | 5.02% | 手续费及佣金支出合计(TotalCommExpense)：一般为金融类企业披露科目，本字段展示收入模块、成本模块“其中:... |
| 160 | `TotalOCInImpairLoss` | 营业总成本(含减值损失) | number(19,4) | ✓ | 98.59% | 营业总成本(含减值损失)(TotalOCInImpairLoss)=营业总成本-资产减值损失(利润)- 信用减值损失(利... |
| 161 | `TotalOCNoInImpairLoss` | 营业总成本(不含减值损失) | number(19,4) | ✓ | 98.59% | 营业总成本(不含减值损失)(TotalOCNoInImpairLoss)=营业总成本-资产减值损失(成本)-信用减值损失... |
| 162 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 0.97% |  |
| 163 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 164 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 165 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM NOT IN (110106,110107,110108,110109,110110,110111,110203,110204,110205,120109,120110,120204,120208,120210,120216,120217,130108,130110,130112,130113,140108,140109)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，110201-定期报告:年度报告(关联方)，110202-定期报告:半年度报告(关联方)，120101-临时公告:审计报告(更正后)，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)，120106-临时公告:公开转让说明书(更正后)，120107-临时公告:业绩快报，120108-临时公告:业绩快报(更正后)，120201-临时公告:跟踪评级报告，120202-临时公告:同业存单发行计划，120203-临时公告:比较式财务报表，120205-临时公告:其他，120206-临时公告:前期差错更正，120207-临时公告:第一季度报告，120209-临时公告:第三季度报告，120211-临时公告：年度报告，120212-临时公告：半年度报告，120213-临时公告:受托管理人事务报告，120214-临时公告:资产评估报告，120215-临时公告:资产管理报告，120218-临时公告：主要经营业绩，130101-发行上市书:募集说明书，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130105-发行上市书:审阅报告，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130109-发行上市书:审计报告，130111-发行上市书:其他，140101-发行披露文件:第一季报，140102-发行披露文件:半年度报告，140103-发行披露文件:第三季报，140104-发行披露文件:审计报告，140105-发行披露文件:募集说明书，140106-发行披露文件:跟踪评级报告，140107-发行披露文件:年度报告，140110-发行披露文件:转让服务公告书，140111-发行披露文件:备案登记表，140112-发行披露文件:初始信息披露，150101-发债定期报告:第一季报，150102-发债定期报告:半年度报告，150103-发债定期报告:第三季报，150104-发债定期报告:年度报告，150105-发债:其他报告。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311  and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfMerged (是否合并)

是否合并（IfMerged），该字段固定以下常量：1-合并报表；2-母公司报表

### IfAdjusted (是否调整)

是否调整（IfAdjusted），该字段固定以下常量：1-调整；2-未调整；4-季度未调整；5-季度调整 注：季度数据是第三季度财务数据

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### EnterpriseType (报表格式类型)

报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业)。 本表报表格式类型(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业性质(CompanyType)。

### TotalOperatingRevenue (一、营业总收入)

营业总收入（TotalOperatingRevenue）：对非金融类公司（报表披露类型=99），营业总收入=营业收入＋金融类特殊收入项目＋其他业务收入，注：“金融类特殊收入项目”包括：利息收入、手续费及佣金收入、已赚保费、营业收入特殊项目、调整项目

### NetInterestIncome (利息净收入)

利息净收入（NetInterestIncome）：一般为金融类企业披露科目；本字段优先展示收入模块披露的“利息净收入”，当原文未披露时，且IfComplete=1时，则通过收入模块披露的“其中:利息收入”、“其中:利息支出”计算得出，计算公式=其中:利息收入-其中:利息支出；

## SQL示例

```sql
-- 查询 利润分配表_新会计准则 数据
SELECT *
FROM dz_incomestatementall
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
