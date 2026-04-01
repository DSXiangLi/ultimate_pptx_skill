# DZ_QIncomeStatementNew

**中文名**: 单季利润表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_QIncomeStatementNew` |
| MySQL表名 | `dz_qincomestatementnew` |
| 中文名 | 单季利润表_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 129 |
| 版本 | 1.03 |

## 表描述

1.本表收录自公布季报以来上市、发债、非上市非发债公司的单季利润表情况，数据单位均为人民币元。
2.科目的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有多条调整，取最新调整数据，有多条未调整，取最新未调整数据）。
3.由于会计期间可能发生同一控制下企业合并、企业自身错报漏报、企业列报项目变化等问题，将会导致二、四季度的单季数据的可靠性下降。
4.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明” 字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
5.因简表数据原文披露不完整，且披露的数据量有限，通过简表计算的数据，不能真实反应企业单季度现金情况，所以本表展示完整标志（IfComplete）=1-完整的单季度数据。
6.因集团类企业涉及金融类业务，在财报中会披露金融类科目数据，本表在计算时，不区分金融/非金融字段，如定期报告中披露原始数据，则都计算单季度数据。
7.数据范围：2000-03-31至今
8.信息来源：定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% | 信息来源（InfoSource）：根据报告期区分为：第一季度、第二季度、第三季度、第四季度； |
| 4 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 5 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN ... |
| 8 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 9 | `CompanyType` | 企业类别 | number(10) | ✓ | 100.0% | 公司类别(CompanyType)：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融... |
| 10 | `IfRecalculated` | 是否计算 | number(10) | ✓ | 100.0% | 是否计算(IfRecalculated)：1-是，0-否；其中：1-是（为依据本期和前一期计算的单季度数据），0-否（为... |
| 11 | `TotalOperatingRevenue` | 一、营业总收入(非金融类) | number(19,4) | ✓ | 99.97% |  |
| 12 | `OperatingRevenue` | 营业收入 | number(19,4) | ✓ | 99.4% |  |
| 13 | `NetInterestIncome` | 利息净收入(金融类) | number(19,4) | ✓ | 6.83% |  |
| 14 | `InterestIncome` | 其中:利息收入(金融类) | number(19,4) | ✓ | 5.32% |  |
| 15 | `InterestExpense` | 其中:利息支出(金融类) | number(19,4) | ✓ | 2.11% |  |
| 16 | `NetCommissionIncome` | 手续费及佣金净收入(金融类) | number(19,4) | ✓ | 5.34% |  |
| 17 | `CommissionIncome` | 其中:手续费及佣金收入(金融类) | number(19,4) | ✓ | 3.71% |  |
| 18 | `CommissionExpense` | 其中:手续费及佣金支出(金融类) | number(19,4) | ✓ | 1.75% |  |
| 19 | `NetProxySecuIncome` | 其中:代理买卖证券业务净收入(金融类) | number(19,4) | ✓ | 0.6% |  |
| 20 | `NetSubIssueSecuIncome` | 其中:证券承销业务净收入(金融类) | number(19,4) | ✓ | 0.59% |  |
| 21 | `NetTrustIncome` | 其中:受托客户资产管理业务净收入(金融类) | number(19,4) | ✓ | 0.53% |  |
| 22 | `PremiumsEarned` | 已赚保费(金融类) | number(19,4) | ✓ | 1.61% |  |
| 23 | `PremiumsIncome` | 其中:保险业务收入(金融类) | number(19,4) | ✓ | 0.33% |  |
| 24 | `ReinsuranceIncome` | 其中:保险业务收入:分保费收入(金融类) | number(19,4) | ✓ | 0.08% |  |
| 25 | `Reinsurance` | 其中:减:分出保费(金融类) | number(19,4) | ✓ | 0.23% |  |
| 26 | `UnearnedPremiumReserve` | 其中:减:提取未到期责任准备金(金融类) | number(19,4) | ✓ | 0.28% |  |
| 27 | `GuaranteeIncome` | 担保业务收入 | number(19,4) | ✓ | 0.09% |  |
| 28 | `OtherOperatingIncome` | 其他收入 | number(19,4) | ✓ | 2.57% |  |
| 29 | `SpecialItemsOR` | ##营业收入OR营业总收入特殊项目 | number(19,4) | ✓ | 0.39% |  |
| 30 | `AdjustmentItemsOR` | ##营业收入OR营业总收入调整项目 | number(19,4) | ✓ | 0.37% |  |
| 31 | `OtherOperatingRevenue` | 其他营业收入(非金融类)(废弃) | number(19,4) | ✓ | 0.0% | OtherOperatingRevenue	其他营业收入(非金融类)：该字段已废弃 |
| 32 | `TotalOperatingCost` | 二、营业总成本(非金融类) | number(19,4) | ✓ | 100.0% |  |
| 33 | `OperatingCost` | 营业成本(非金融类) | number(19,4) | ✓ | 93.53% |  |
| 34 | `OperatingExpense` | 销售费用(非金融类) | number(19,4) | ✓ | 81.95% |  |
| 35 | `TotalAdminExpense` | 管理费用合计 | number(19,4) | ✓ | 99.77% |  |
| 36 | `AdministrationExpense` | 其中:管理费用(非金融类) | number(19,4) | ✓ | 96.91% |  |
| 37 | `OperatingAndAdminExpense` | 其中:业务及管理费(金融类) | number(19,4) | ✓ | 2.73% |  |
| 38 | `AmortizationReinsuranceCost` | 其中:减:摊回分保费用(金融类) | number(19,4) | ✓ | 0.18% |  |
| 39 | `FinancialExpense` | 财务费用(非金融类) | number(19,4) | ✓ | 97.21% |  |
| 40 | `InterestFinExp` | 其中:利息费用(财务费用) | number(19,4) | ✓ | 34.08% |  |
| 41 | `InterestIncomeFin` | 其中:利息收入(财务费用) | number(19,4) | ✓ | 38.39% |  |
| 42 | `RAndD` | 研发费用 | number(19,4) | ✓ | 31.16% |  |
| 43 | `OperatingPayout` | 营业支出(金融类) | number(19,4) | ✓ | 2.76% |  |
| 44 | `RefundedPremiums` | 退保金(金融类) | number(19,4) | ✓ | 0.86% |  |
| 45 | `PreInsurRSRV` | 提取保费准备金 | number(19,4) | ✓ | 0.05% |  |
| 46 | `NetClaimIncurred` | 赔付支出净额 | number(19,4) | ✓ | 0.92% |  |
| 47 | `CompensationExpense` | 其中:赔付支出(金融类) | number(19,4) | ✓ | 0.33% |  |
| 48 | `AmortizationExpense` | 其中:减:摊回赔付支出(金融类) | number(19,4) | ✓ | 0.18% |  |
| 49 | `NetPremiumReserve` | 提取保险责任准备金净额 | number(19,4) | ✓ | 1.41% |  |
| 50 | `PremiumReserve` | 其中:提取保险责任准备金(金融类) | number(19,4) | ✓ | 0.4% |  |
| 51 | `AmortizationPremiumReserve` | 其中:减:摊回保险责任准备金(金融类) | number(19,4) | ✓ | 0.18% |  |
| 52 | `PolicyDividendPayout` | 保单红利支出(金融类) | number(19,4) | ✓ | 0.85% |  |
| 53 | `ReinsuranceCost` | 分保费用(金融类) | number(19,4) | ✓ | 0.91% |  |
| 54 | `InsuranceCommissionExpense` | 保险手续费及佣金支出(金融类) | number(19,4) | ✓ | 0.2% |  |
| 55 | `OperatingTaxAndSurcharges` | 营业税金及附加 | number(19,4) | ✓ | 97.5% | 营业税金及附加(OperatingTaxAndSurcharges)：对于非金融类企业，该科目属于营业总成本的子项；对于... |
| 56 | `ExplorationCost` | 勘探费用 | number(19,4) | ✓ | 0.06% |  |
| 57 | `CreditImpairmentC` | 信用减值损失(成本) | number(19,4) | ✓ | 2.14% | 信用减值损失(成本)(CreditImpairmentC)：对于非金融类企业，该科目属于营业总成本的子项；对于金融类企业... |
| 58 | `AssetImpairmentLossC` | 资产减值损失(成本) | number(19,4) | ✓ | 40.69% | 资产减值损失(成本)(AssetImpairmentLossC)：对于非金融类企业，该科目属于营业总成本的子项；对于金融... |
| 59 | `OtherOperatingCost` | 其他成本 | number(19,4) | ✓ | 1.95% |  |
| 60 | `SpecialItemsOP` | ##营业支出OR营业总成本特殊项目 | number(19,4) | ✓ | 0.7% |  |
| 61 | `AdjustmentItemsOP` | ##营业支出OR营业总成本调整项目 | number(19,4) | ✓ | 1.4% |  |
| 62 | `OtherRevenue` | 其他收益 | number(19,4) | ✓ | 48.36% |  |
| 63 | `InvestIncome` | 投资净收益 | number(19,4) | ✓ | 82.26% |  |
| 64 | `InvestIncomeFromAssociates` | 其中:对联营合营企业的投资收益 | number(19,4) | ✓ | 32.06% |  |
| 65 | `AmortisedcostIncome` | 其中:以摊余成本计量的金融资产终止确认收益 | number(19,4) | ✓ | 1.25% |  |
| 66 | `FairValueChangeIncome` | 公允价值变动净收益 | number(19,4) | ✓ | 32.39% |  |
| 67 | `NetOpenHedgeIncome` | 净敞口套期收益 | number(19,4) | ✓ | 0.55% |  |
| 68 | `ExchangeIncome` | 汇兑收益(金融类) | number(19,4) | ✓ | 4.19% |  |
| 69 | `AssetDealIncome` | 资产处置收益 | number(19,4) | ✓ | 31.12% |  |
| 70 | `CreditImpairmentP` | 信用减值损失(利润) | number(19,4) | ✓ | 31.18% |  |
| 71 | `AssetImpairmentLossP` | 资产减值损失(利润) | number(19,4) | ✓ | 24.88% |  |
| 72 | `OtherItemsEffectingOP` | ##营业利润特殊项目 | number(19,4) | ✓ | 6.08% |  |
| 73 | `AdjustedItemsEffectingOP` | ##营业利润调整项目 | number(19,4) | ✓ | 2.42% |  |
| 74 | `OperatingProfit` | 四、营业利润 | number(19,4) | ✓ | 100.0% |  |
| 75 | `NonoperatingIncome` | 加:营业外收入 | number(19,4) | ✓ | 91.24% |  |
| 76 | `NonoperatingExpense` | 减:营业外支出 | number(19,4) | ✓ | 89.75% |  |
| 77 | `NonCurrentAssetssDealLoss` | 其中:非流动资产处置净损失 | number(19,4) | ✓ | 13.33% |  |
| 78 | `OtherItemsEffectingTP` | ##利润总额特殊项目 | number(19,4) | ✓ | 2.47% |  |
| 79 | `AdjustedItemsEffectingTP` | ##利润总额调整项目 | number(19,4) | ✓ | 0.97% |  |
| 80 | `TotalProfit` | 五、利润总额 | number(19,4) | ✓ | 100.0% |  |
| 81 | `IncomeTaxCost` | 减:所得税费用 | number(19,4) | ✓ | 87.0% |  |
| 82 | `UncertainedInvestmentLosses` | 加:未确认的投资损失 | number(19,4) | ✓ | 0.74% |  |
| 83 | `OtherItemsEffectingNP` | ##净利润特殊项目 | number(19,4) | ✓ | 0.19% |  |
| 84 | `AdjustedItemsEffectingNP` | ##净利润调整项目 | number(19,4) | ✓ | 1.11% |  |
| 85 | `NetProfit` | 六、净利润 | number(19,4) | ✓ | 100.0% |  |
| 86 | `OperSustCateg` | (一)按经营持续性分类 | number(19,4) | ✓ | 1.0% | (一)按经营持续性分类(OperSustCateg)：原文披露频率低，2024-06-20停止维护 |
| 87 | `OperSustNetP` | 持续经营净利润 | number(19,4) | ✓ | 46.04% |  |
| 88 | `DisconOperNetP` | 终止经营净利润 | number(19,4) | ✓ | 0.64% |  |
| 89 | `OwnershipCateg` | (二)按所有权归属分类 | number(19,4) | ✓ | 1.02% | (二)按所有权归属分类(OwnershipCateg)：原文披露频率低，2024-06-20停止维护 |
| 90 | `NPFromParentCompanyOwners` | 归属于母公司所有者的净利润 | number(19,4) | ✓ | 100.0% |  |
| 91 | `NPCParentCompanyOwners` | 其中:归属于母公司普通股股东的净利润 | number(19,4) | ✓ | 0.02% |  |
| 92 | `NPOtherEqinstruments` | 其中:归属于母公司其他权益工具持有者的净利润 | number(19,4) | ✓ | 0.02% |  |
| 93 | `MinorityProfit` | 少数股东损益 | number(19,4) | ✓ | 50.17% |  |
| 94 | `OthItemsEffNPP` | ##母公司净利润特殊项目 | number(19,4) | ✓ | 0.03% |  |
| 95 | `AdjItemsEffNPP` | ##母公司净利润调整项目 | number(19,4) | ✓ | 1.3% |  |
| 96 | `OtherCompositeIncome` | 七、其他综合收益的税后净额 | number(19,4) | ✓ | 34.52% |  |
| 97 | `OCIParentCompanyOwners` | 归属于母公司所有者的其他综合收益的税后净额 | number(19,4) | ✓ | 17.27% |  |
| 98 | `OCINotInIS` | (一)以后不能重分类进损益的其他综合收益 | number(19,4) | ✓ | 6.09% |  |
| 99 | `OCIReMearsure` | 1.1重新计量设定受益计划净负债或净资产的变动 | number(19,4) | ✓ | 0.76% |  |
| 100 | `OCIEquityNotInIS` | 1.2权益法下在被投资单位不能重分类进损益的其他综合收益 | number(19,4) | ✓ | 0.91% |  |
| 101 | `OthEquFVChange` | 1.3其他权益工具投资公允价值变动 | number(19,4) | ✓ | 5.19% |  |
| 102 | `CorporateCRChange` | 1.4企业自身信用风险公允价值变动 | number(19,4) | ✓ | 0.18% |  |
| 103 | `OCIInIncomeStatement` | (二)以后将重分类进损益的其他综合收益 | number(19,4) | ✓ | 19.54% |  |
| 104 | `OCIEquityInIS` | 2.1权益法下在被投资单位以后将重分类进损益的其他综合收益 | number(19,4) | ✓ | 3.68% |  |
| 105 | `OthDebtInvesChange` | 2.2其他债权投资公允价值变动 | number(19,4) | ✓ | 1.46% |  |
| 106 | `FinAssetROtherCI` | 2.3金融资产重分类计入其他综合收益的金额 | number(19,4) | ✓ | 0.27% |  |
| 107 | `OtherDebtInvestCIP` | 2.4其他债权投资信用减值准备 | number(19,4) | ✓ | 1.1% |  |
| 108 | `OCICFLoss` | 2.5现金流量套期损益的有效部分 | number(19,4) | ✓ | 1.44% |  |
| 109 | `OCIForeignCurrencyFSA` | 2.6外币财务报表折算差额 | number(19,4) | ✓ | 13.84% |  |
| 110 | `OCIFairValue` | 2.7可供出售金融资产公允价值变动损益 | number(19,4) | ✓ | 4.31% |  |
| 111 | `OCIToMaturityFA` | 2.8持有至到期投资重分类为可供出售金融资产损益 | number(19,4) | ✓ | 0.13% |  |
| 112 | `OCIOthers` | 2.9其他(以后能重分类进损益表的其他综合收益) | number(19,4) | ✓ | 0.67% |  |
| 113 | `OCIMinorityOwners` | 归属于少数股东的其他综合收益的税后净额 | number(19,4) | ✓ | 6.17% |  |
| 114 | `AdjustEffectCI` | ##综合收益总额调整项目 | number(19,4) | ✓ | 0.24% |  |
| 115 | `TotalCompositeIncome` | 八、综合收益总额 | number(19,4) | ✓ | 82.66% |  |
| 116 | `CIParentCompanyOwners` | 归属于母公司所有者的综合收益总额 | number(19,4) | ✓ | 48.76% |  |
| 117 | `CIMinorityOwners` | 归属于少数股东的综合收益总额 | number(19,4) | ✓ | 36.77% |  |
| 118 | `AdjustEffectPCI` | ##母公司综合收益总额调整项目 | number(19,4) | ✓ | 0.19% |  |
| 119 | `BasicEPS` | 基本每股收益 | number(19,4) | ✓ | 20.06% |  |
| 120 | `DilutedEPS` | 稀释每股收益 | number(19,4) | ✓ | 19.01% |  |
| 121 | `TotalInterestExpense` | 利息支出合计 | number(19,4) | ✓ | 5.41% | 利息支出合计(TotalInterestExpense)：本字段展示收入模块、成本模块披露的“其中：利息支出”合计值； |
| 122 | `TotalCommExpense` | 手续费及佣金支出合计 | number(19,4) | ✓ | 5.16% | 手续费及佣金支出合计(TotalCommExpense)：本字段展示收入模块、成本模块“其中:手续费及佣金支出”、保险手... |
| 123 | `TotalOCInImpairLoss` | 营业总成本(含减值损失) | number(19,4) | ✓ | 100.0% | 营业总成本(含减值损失)(TotalOCInImpairLoss)=营业总成本-资产减值损失(利润)- 信用减值损失(利... |
| 124 | `TotalOCNoInImpairLoss` | 营业总成本(不含减值损失) | number(19,4) | ✓ | 100.0% | 营业总成本(不含减值损失)(TotalOCNoInImpairLoss)=营业总成本-资产减值损失(成本)-信用减值损失... |
| 125 | `CreditImpairmentL` | 信用减值损失合计 | number(19,4) | ✓ | 33.0% | 信用减值损失(CreditImpairmentL)：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的通知... |
| 126 | `AssetImpairmentLoss` | 资产减值损失合计 | number(19,4) | ✓ | 64.23% | 资产减值损失（AssetImpairmentLoss）：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的... |
| 127 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 128 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 129 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSource (信息来源)

信息来源（InfoSource）：根据报告期区分为：第一季度、第二季度、第三季度、第四季度；

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### CompanyType (企业类别)

公司类别(CompanyType)：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业。 本表企业性质(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业类别(CompanyType)。

### IfRecalculated (是否计算)

是否计算(IfRecalculated)：1-是，0-否；其中：1-是（为依据本期和前一期计算的单季度数据），0-否（为原文披露的单季度数据）

### OtherOperatingRevenue (其他营业收入(非金融类)(废弃))

OtherOperatingRevenue	其他营业收入(非金融类)：该字段已废弃

### OperatingTaxAndSurcharges (营业税金及附加)

营业税金及附加(OperatingTaxAndSurcharges)：对于非金融类企业，该科目属于营业总成本的子项；对于金融类企业，则属于营业支出的子项。

### CreditImpairmentC (信用减值损失(成本))

信用减值损失(成本)(CreditImpairmentC)：对于非金融类企业，该科目属于营业总成本的子项；对于金融类企业，则属于营业支出的子项。

## SQL示例

```sql
-- 查询 单季利润表_新会计准则 数据
SELECT *
FROM dz_qincomestatementnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
