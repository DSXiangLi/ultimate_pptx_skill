# DZ_BalanceSheetAll

**中文名**: 资产负债表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_BalanceSheetAll` |
| MySQL表名 | `dz_balancesheetall` |
| 中文名 | 资产负债表_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 230 |
| 版本 | 1.06 |

## 表描述

1.内容说明：
1.1反映上市、发债、非上市非发债公司依据2007年新会计准则在年报、中报、季报中披露的资产负债表数据；并依据新旧会计准则的科目对应关系，收录主要科目的历史对应数据。
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
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 5 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and ... |
| 6 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 9 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM I... |
| 10 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志... |
| 11 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 12 | `EnterpriseType` | 报表格式类型 | number(10) | ✗ | 100.0% | 报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公... |
| 13 | `CashEquivalents` | 货币资金/现金及存放中央银行款项 | number(19,4) | ✓ | 98.85% |  |
| 14 | `Cash` | 其中:货币资金 | number(19,4) | ✓ | 52.18% |  |
| 15 | `ClientDeposit` | 其中:货币资金:客户资金存款 | number(19,4) | ✓ | 0.89% | 其中:货币资金:客户资金存款（ClientDeposit）：一般为金融类:证券公司披露科目 |
| 16 | `DepositInCentralBank` | 其中:现金及存放中央银行款项 | number(19,4) | ✓ | 1.54% | 其中:现金及存放中央银行款项（DepositInCentralBank）：一般为金融类:银行企业披露科目 |
| 17 | `SettlementProvi` | 结算备付金 | number(19,4) | ✓ | 2.01% | 结算备付金（SettlementProvi）：一般为金融类企业披露科目 |
| 18 | `ClientProvi` | 其中:客户备付金 | number(19,4) | ✓ | 0.88% | 其中:客户备付金（ClientProvi）：一般为金融类:证券公司披露科目 |
| 19 | `LendCapital` | 拆出资金 | number(19,4) | ✓ | 2.27% | 拆出资金（LendCapital）：一般为金融类企业披露科目 |
| 20 | `Financing` | 融出资金 | number(19,4) | ✓ | 0.78% | 融出资金（Financing）：一般为金融类:证券公司披露科目 |
| 21 | `DepositInInterbank` | 存放同业款项 | number(19,4) | ✓ | 2.35% | 存放同业款项（DepositInInterbank）：一般为金融类:银行企业披露科目 |
| 22 | `DepositInAssociate` | 存放联行款项 | number(19,4) | ✓ | 0.24% |  |
| 23 | `RMetal` | 贵金属 | number(19,4) | ✓ | 0.3% | 贵金属（RMetal）：一般为金融类企业披露科目 |
| 24 | `TradingAssets` | 交易性金融资产合计 | number(19,4) | ✓ | 32.8% |  |
| 25 | `AmongTradingAssets` | 其中:交易性金融资产 | number(19,4) | ✓ | 21.05% |  |
| 26 | `AmongFinAetAtFValTPL` | 其中:以公允价值计量且其变动计入当期损益的金融资产 | number(19,4) | ✓ | 2.05% |  |
| 27 | `DerivativeAssets` | 衍生金融资产 | number(19,4) | ✓ | 3.34% |  |
| 28 | `RefundableDeposit` | 存出保证金 | number(19,4) | ✓ | 1.3% |  |
| 29 | `BillAccReceivable` | 应收票据及应收账款 | number(19,4) | ✓ | 87.5% |  |
| 30 | `BillReceivable` | 其中:应收票据 | number(19,4) | ✓ | 57.44% |  |
| 31 | `AccountReceivable` | 其中:应收账款 | number(19,4) | ✓ | 86.0% |  |
| 32 | `ReceivablesFin` | 应收款项融资 | number(19,4) | ✓ | 16.28% |  |
| 33 | `AdvancePayment` | 预付款项 | number(19,4) | ✓ | 88.77% |  |
| 34 | `InsuranceReceivables` | 应收保费 | number(19,4) | ✓ | 1.13% | 应收保费（InsuranceReceivables）：一般为金融类:保险公司披露科目 |
| 35 | `ReceivableSubrogationFee` | 应收代位追偿款 | number(19,4) | ✓ | 0.3% | 应收代位追偿款（ReceivableSubrogationFee）：一般为金融类:保险公司披露科目 |
| 36 | `ReinsuranceReceivables` | 应收分保账款 | number(19,4) | ✓ | 1.06% | 应收分保账款（ReinsuranceReceivables）：一般为金融类:保险公司披露科目 |
| 37 | `ResReiReceContracts` | 应收分保合同准备金 | number(19,4) | ✓ | 0.9% | 应收分保合同准备金（ResReiReceContracts）：一般为金融类:保险公司披露科目 |
| 38 | `ReceivableUnearnedR` | 其中:应收分保未到期责任准备金 | number(19,4) | ✓ | 0.45% | 其中:应收分保未到期责任准备金（ReceivableUnearnedR）：一般为金融类:保险公司披露科目 |
| 39 | `ReceivableClaimsR` | 其中:应收分保未决赔款准备金 | number(19,4) | ✓ | 0.41% | 其中:应收分保未决赔款准备金（ReceivableClaimsR）：一般为金融类:保险公司披露科目 |
| 40 | `ReceivableLifeR` | 其中:应收分保寿险责任准备金 | number(19,4) | ✓ | 0.23% | 其中:应收分保寿险责任准备金（ReceivableLifeR）：一般为金融类:保险公司披露科目 |
| 41 | `ReceivableLTHealthR` | 其中:应收分保长期健康险责任准备金 | number(19,4) | ✓ | 0.23% | 其中:应收分保长期健康险责任准备金（ReceivableLTHealthR）：一般为金融类:保险公司披露科目 |
| 42 | `OtherReceivableED` | 其他应收款(含利息和股利) | number(19,4) | ✓ | 96.16% | 其他应收款(含利息和股利)（OtherReceivableED）：根据财政部2019.1.22发布的《关于修订印发201... |
| 43 | `OtherReceivable` | 其中:其他应收款 | number(19,4) | ✓ | 72.45% |  |
| 44 | `DividendReceivable` | 其中:应收股利 | number(19,4) | ✓ | 16.8% |  |
| 45 | `InterestReceivable` | 其中:应收利息 | number(19,4) | ✓ | 20.02% |  |
| 46 | `FinLeaseReceivable` | 应收融资租赁款 | number(19,4) | ✓ | 0.14% | 应收融资租赁款（FinLeaseReceivable）：一般为金融类企业披露科目 |
| 47 | `Receivables` | 应收款项 | number(19,4) | ✓ | 0.79% | 应收款项（Receivables）：一般为金融类企业披露科目 |
| 48 | `CashDepositReceive` | 应收货币保证金 | number(19,4) | ✓ | 0.08% |  |
| 49 | `PledgDepositReceive` | 应收质押保证金 | number(19,4) | ✓ | 0.06% |  |
| 50 | `SettlementReceive` | 应收结算担保金 | number(19,4) | ✓ | 0.05% |  |
| 51 | `RiskOfLossReceive` | 应收风险损失款 | number(19,4) | ✓ | 0.02% |  |
| 52 | `FeeCommissionReceive` | 应收手续费及佣金 | number(19,4) | ✓ | 0.02% |  |
| 53 | `BoughtSellbackAssets` | 买入返售金融资产 | number(19,4) | ✓ | 4.19% |  |
| 54 | `Inventories` | 存货 | number(19,4) | ✓ | 85.65% |  |
| 55 | `BearerBiologicalAssets` | 其中:消耗性生物资产 | number(19,4) | ✓ | 0.01% |  |
| 56 | `DataResourcesInventory` | 其中:数据资源(存货) | number(19,4) | ✓ | 0.05% |  |
| 57 | `ContractualAssets` | 合同资产 | number(19,4) | ✓ | 9.9% |  |
| 58 | `InsuranceContractAssets` | 保险合同资产 | number(19,4) | ✓ | 0.01% |  |
| 59 | `ReinsuranContractAssets` | 分出再保险合同资产 | number(19,4) | ✓ | 0.03% |  |
| 60 | `AgencyBusAssets` | 代理业务资产 | number(19,4) | ✓ | 0.0% |  |
| 61 | `HoldAndFSAssets` | 持有待售资产 | number(19,4) | ✓ | 2.76% |  |
| 62 | `DeferredExpense` | 待摊费用 | number(19,4) | ✓ | 4.72% |  |
| 63 | `InsurerImpawnLoan` | 保户质押贷款 | number(19,4) | ✓ | 0.24% | 保户质押贷款（InsurerImpawnLoan）：一般为金融类:保险公司披露科目 |
| 64 | `NonCurrentAssetIn1Year` | 一年内到期的非流动资产 | number(19,4) | ✓ | 13.83% |  |
| 65 | `OtherCurrentAssets` | 其他流动资产 | number(19,4) | ✓ | 67.87% |  |
| 66 | `CAExceptionalItems` | ##流动资产特殊项目 | number(19,4) | ✓ | 2.29% |  |
| 67 | `CAAdjustmentItems` | ##流动资产调整项目 | number(19,4) | ✓ | 1.15% |  |
| 68 | `TotalCurrentAssets` | 流动资产合计 | number(19,4) | ✓ | 94.82% |  |
| 69 | `LoanAndAdvance` | 发放贷款和垫款 | number(19,4) | ✓ | 5.46% | 发放贷款和垫款（LoanAndAdvance）：一般为金融类:银行企业披露科目 |
| 70 | `DebtInvestment` | 债权投资合计 | number(19,4) | ✓ | 5.14% |  |
| 71 | `AmongDebtInvestment` | 其中:债权投资 | number(19,4) | ✓ | 4.99% |  |
| 72 | `AmongFinAetAtAmorCost` | 其中:以摊余成本计量的金融资产 | number(19,4) | ✓ | 0.1% |  |
| 73 | `OthDebtInvestment` | 其他债权投资合计 | number(19,4) | ✓ | 2.54% |  |
| 74 | `AmongOthDebtInvest` | 其中:其他债权投资 | number(19,4) | ✓ | 2.48% |  |
| 75 | `AmongFinAetAtFValTOCI` | 其中:以公允价值计量且其变动计入其他综合收益的债务工具投资 | number(19,4) | ✓ | 0.02% |  |
| 76 | `LoanAndAccountReceivables` | 投资-贷款及应收款项(应收款项类投资) | number(19,4) | ✓ | 1.25% |  |
| 77 | `FixedDeposit` | 定期存款 | number(19,4) | ✓ | 0.46% |  |
| 78 | `OthEquityInstrument` | 其他权益工具投资合计 | number(19,4) | ✓ | 21.21% |  |
| 79 | `AmongOthEquInstrument` | 其中:其他权益工具投资 | number(19,4) | ✓ | 21.04% |  |
| 80 | `AmongEquInsAtFValTOCI` | 其中:以公允价值计量且其变动计入其他综合收益的非交易性权益工具投资 | number(19,4) | ✓ | 0.02% |  |
| 81 | `FinAssetsAtFValTOCI` | 以公允价值计量且其变动计入其他综合收益的金融资产 | number(19,4) | ✓ | 0.09% |  |
| 82 | `HoldToMaturityInvestments` | 持有至到期投资 | number(19,4) | ✓ | 6.59% |  |
| 83 | `HoldForSaleAssets` | 可供出售金融资产 | number(19,4) | ✓ | 26.56% |  |
| 84 | `OthNonCurFinAssets` | 其他非流动金融资产 | number(19,4) | ✓ | 12.45% |  |
| 85 | `SubLoan` | 委托贷款 | number(19,4) | ✓ | 0.11% |  |
| 86 | `LongtermReceivableAccount` | 长期应收款 | number(19,4) | ✓ | 18.8% |  |
| 87 | `LongtermEquityInvest` | 长期股权投资 | number(19,4) | ✓ | 80.49% |  |
| 88 | `RefundableCapitalDeposit` | 存出资本保证金 | number(19,4) | ✓ | 0.48% | 存出资本保证金（RefundableCapitalDeposit）：一般为金融类:保险公司披露科目 |
| 89 | `InvestmentProperty` | 投资性房地产 | number(19,4) | ✓ | 42.37% |  |
| 90 | `TotalFixedAsset` | 固定资产合计 | number(19,4) | ✓ | 98.12% | 固定资产合计（TotalFixedAsset）：根据财政部2019.1.22发布的《关于修订印发2018年度合并财务报表... |
| 91 | `FixedAssets` | 其中:固定资产 | number(19,4) | ✓ | 63.59% |  |
| 92 | `FixedAssetsLiquidation` | 其中:固定资产清理 | number(19,4) | ✓ | 9.04% |  |
| 93 | `TConstruInProcess` | 在建工程合计 | number(19,4) | ✓ | 73.0% | 在建工程合计（TConstruInProcess）：根据财政部2019.1.22发布的《关于修订印发2018年度合并财务... |
| 94 | `ConstruInProcess` | 其中:在建工程 | number(19,4) | ✓ | 49.58% |  |
| 95 | `ConstructionMaterials` | 其中:工程物资 | number(19,4) | ✓ | 11.72% |  |
| 96 | `BiologicalAssets` | 生产性生物资产 | number(19,4) | ✓ | 4.17% |  |
| 97 | `PubWBiologicalAssets` | 公益性生物资产 | number(19,4) | ✓ | 0.01% |  |
| 98 | `OilGasAssets` | 油气资产 | number(19,4) | ✓ | 1.03% |  |
| 99 | `UsufructAssets` | 使用权资产 | number(19,4) | ✓ | 19.85% |  |
| 100 | `IntangibleAssets` | 无形资产 | number(19,4) | ✓ | 90.07% |  |
| 101 | `SeatCosts` | 其中:交易席位费 | number(19,4) | ✓ | 0.21% |  |
| 102 | `DataResourcesIntangible` | 其中:数据资源(无形资产) | number(19,4) | ✓ | 0.09% |  |
| 103 | `DevelopmentExpenditure` | 开发支出 | number(19,4) | ✓ | 12.87% |  |
| 104 | `DataResourcesDevExpen` | 其中:数据资源(开发支出) | number(19,4) | ✓ | 0.06% |  |
| 105 | `GoodWill` | 商誉 | number(19,4) | ✓ | 23.54% |  |
| 106 | `LongDeferredExpense` | 长期待摊费用 | number(19,4) | ✓ | 65.71% |  |
| 107 | `IndependenceAccountAssets` | 独立账户资产 | number(19,4) | ✓ | 0.14% | 独立账户资产（IndependenceAccountAssets）：一般为金融类:保险公司披露科目 |
| 108 | `DeferredTaxAssets` | 递延所得税资产 | number(19,4) | ✓ | 78.14% |  |
| 109 | `DebtAssets` | 抵债资产 | number(19,4) | ✓ | 0.52% |  |
| 110 | `FutureMemberInvestment` | 期货会员资格投资 | number(19,4) | ✓ | 0.05% | 期货会员资格投资（FutureMemberInvestment）：一般为金融类:证券公司披露科目 |
| 111 | `OtherNonCurrentAssets` | 其他非流动资产 | number(19,4) | ✓ | 51.44% |  |
| 112 | `NCAExceptionalItems` | ##非流动资产特殊项目 | number(19,4) | ✓ | 2.99% |  |
| 113 | `NCAAdjustmentItems` | ##非流动资产调整项目 | number(19,4) | ✓ | 1.19% |  |
| 114 | `TotalNonCurrentAssets` | 非流动资产合计 | number(19,4) | ✓ | 94.7% |  |
| 115 | `FinancialInvestment` | 金融投资 | number(19,4) | ✓ | 0.35% | 金融投资（FinancialInvestment）：一般为金融类企业披露科目 |
| 116 | `OtherAssets` | 其他资产 | number(19,4) | ✓ | 3.88% | 其他资产（OtherAssets）：一般为金融类企业披露科目 |
| 117 | `AExceptionalItems` | ##资产特殊项目 | number(19,4) | ✓ | 0.29% |  |
| 118 | `AAdjustmentItems` | ##资产调整项目 | number(19,4) | ✓ | 0.93% |  |
| 119 | `TotalAssets` | 资产总计 | number(19,4) | ✓ | 100.0% |  |
| 120 | `ShortTermLoan` | 短期借款 | number(19,4) | ✓ | 73.04% |  |
| 121 | `ImpawnedLoan` | 其中:质押借款 | number(19,4) | ✓ | 0.01% |  |
| 122 | `ShortTermBondPay` | 应付短期融资款 | number(19,4) | ✓ | 0.62% | 应付短期融资款（ShortTermBondPay）：一般为金融类:证券公司披露科目 |
| 123 | `STBondsPayable` | 应付短期债券 | number(19,4) | ✓ | 0.32% | 应付短期债券（STBondsPayable）：一般为金融类企业披露科目 |
| 124 | `BorrowingFromCentralBank` | 向中央银行借款 | number(19,4) | ✓ | 2.37% | 向中央银行借款（BorrowingFromCentralBank）：一般为金融类:银行企业披露科目 |
| 125 | `BorrowingCapital` | 拆入资金 | number(19,4) | ✓ | 3.18% | 拆入资金（BorrowingCapital）：一般为金融类企业披露科目 |
| 126 | `TradingLiability` | 交易性金融负债合计 | number(19,4) | ✓ | 6.08% |  |
| 127 | `AmongTradingLiability` | 其中:交易性金融负债 | number(19,4) | ✓ | 2.85% |  |
| 128 | `AmongFinLiaAtFValTPL` | 其中:以公允价值计量且其变动计入当期损益的金融负债 | number(19,4) | ✓ | 0.4% |  |
| 129 | `DerivativeLiability` | 衍生金融负债 | number(19,4) | ✓ | 3.25% |  |
| 130 | `NotAccountsPayable` | 应付票据及应付账款 | number(19,4) | ✓ | 89.89% |  |
| 131 | `NotesPayable` | 其中:应付票据 | number(19,4) | ✓ | 53.57% |  |
| 132 | `AccountsPayable` | 其中:应付账款 | number(19,4) | ✓ | 86.03% |  |
| 133 | `AdvanceReceipts` | 预收款项 | number(19,4) | ✓ | 65.83% |  |
| 134 | `AdvanceInsurance` | 预收保费 | number(19,4) | ✓ | 0.53% | 预收保费（AdvanceInsurance）：一般为金融类:保险公司披露科目 |
| 135 | `ContractLiability` | 合同负债 | number(19,4) | ✓ | 29.31% |  |
| 136 | `InsContract` | 保险合同负债 | number(19,4) | ✓ | 0.03% |  |
| 137 | `ReinsuranceContractLiab` | 分出再保险合同负债 | number(19,4) | ✓ | 0.01% |  |
| 138 | `SoldBuybackSecuProceeds` | 卖出回购金融资产款 | number(19,4) | ✓ | 4.24% | 卖出回购金融资产款（SoldBuybackSecuProceeds）：一般为金融类企业披露科目 |
| 139 | `AbsInterDeposits` | 吸收存款及同业存款 | number(19,4) | ✓ | 3.8% | 吸收存款及同业存款（AbsInterDeposits）：一般为金融类企业披露科目 |
| 140 | `Deposit` | 其中:吸收存款 | number(19,4) | ✓ | 2.44% | 其中:吸收存款（Deposit）：一般为金融类:银行企业披露科目 |
| 141 | `DepositOfInterbank` | 其中:同业及其他金融机构存放款项 | number(19,4) | ✓ | 1.94% | 其中:同业及其他金融机构存放款项（DepositOfInterbank）：一般为金融类企业披露科目 |
| 142 | `DebitofAssociate` | 联行存放款项 | number(19,4) | ✓ | 0.21% |  |
| 143 | `ProxySecuProceeds` | 代理买卖证券款 | number(19,4) | ✓ | 1.79% | 代理买卖证券款（ProxySecuProceeds）：一般为金融类:证券公司披露科目 |
| 144 | `SubIssueSecuProceeds` | 代理承销证券款 | number(19,4) | ✓ | 0.59% | 代理承销证券款（SubIssueSecuProceeds）：一般为金融类:证券公司披露科目 |
| 145 | `SalariesPayable` | 应付职工薪酬 | number(19,4) | ✓ | 92.05% |  |
| 146 | `TaxsPayable` | 应交税费 | number(19,4) | ✓ | 97.92% |  |
| 147 | `OtherPayableED` | 其他应付款(含利息和股利) | number(19,4) | ✓ | 96.7% | 其他应付款(含利息和股利)（OtherPayableED）：根据财政部2019.1.22发布的《关于修订印发2018年度... |
| 148 | `OtherPayable` | 其中:其他应付款 | number(19,4) | ✓ | 62.23% |  |
| 149 | `DividendPayable` | 其中:应付股利 | number(19,4) | ✓ | 26.67% |  |
| 150 | `InterestPayable` | 其中:应付利息 | number(19,4) | ✓ | 34.8% |  |
| 151 | `Payables` | 应付款项 | number(19,4) | ✓ | 0.74% | 应付款项（Payables）：一般为金融类企业披露科目 |
| 152 | `CommissionPayable` | 应付手续费及佣金 | number(19,4) | ✓ | 1.14% | 应付手续费及佣金（CommissionPayable）：一般为金融类:保险公司披露科目 |
| 153 | `CashDepositPay` | 应付货币保证金 | number(19,4) | ✓ | 0.09% |  |
| 154 | `PledgDepositPay` | 应付质押保证金 | number(19,4) | ✓ | 0.07% |  |
| 155 | `FutureProtectFundPay` | 应付期货投资者保障基金 | number(19,4) | ✓ | 0.05% | 	 应付期货投资者保障基金（FutureProtectFundPay）：一般为金融类:证券公司披露科目 |
| 156 | `ReinsurancePayables` | 应付分保账款 | number(19,4) | ✓ | 1.09% | 应付分保账款（ReinsurancePayables）：一般为金融类:保险公司披露科目 |
| 157 | `AgencyBusLiability` | 代理业务负债 | number(19,4) | ✓ | 0.01% |  |
| 158 | `HoldAndFSLi` | 持有待售负债 | number(19,4) | ✓ | 0.77% |  |
| 159 | `CompensationPayable` | 应付赔付款 | number(19,4) | ✓ | 0.42% | 应付赔付款（CompensationPayable）：一般为金融类:保险公司披露科目 |
| 160 | `PolicyDividendPayable` | 应付保单红利 | number(19,4) | ✓ | 0.25% | 应付保单红利（PolicyDividendPayable）：一般为金融类:保险公司披露科目 |
| 161 | `InsurerDepositInvestment` | 保户储金及投资款 | number(19,4) | ✓ | 0.3% | 保户储金及投资款（InsurerDepositInvestment）：一般为金融类:保险公司披露科目 |
| 162 | `InsContractReserve` | 保险合同准备金 | number(19,4) | ✓ | 0.6% | 保险合同准备金（InsContractReserve）：一般为金融类:保险公司披露科目 |
| 163 | `DepositsReceived` | 存入保证金 | number(19,4) | ✓ | 0.25% | 存入保证金（DepositsReceived）：一般为金融类:担保企业披露科目 |
| 164 | `AccruedExpense` | 预提费用 | number(19,4) | ✓ | 4.98% |  |
| 165 | `DeferredProceeds` | 递延收益 | number(19,4) | ✓ | 0.12% |  |
| 166 | `GuarantCompensateRSRV` | 担保赔偿准备金 | number(19,4) | ✓ | 0.3% | 担保赔偿准备金（GuarantCompensateRSRV）：一般为金融类:担保企业披露科目 |
| 167 | `GuaranteeReserve` | 担保业务准备金 | number(19,4) | ✓ | 0.07% | 担保业务准备金（GuaranteeReserve）：一般为金融类:担保企业披露科目 |
| 168 | `FutureRiskReserve` | 期货风险准备金 | number(19,4) | ✓ | 0.08% | 期货风险准备金（FutureRiskReserve）：一般为金融类:证券公司披露科目 |
| 169 | `NonCurrentLiabilityIn1Year` | 一年内到期的非流动负债 | number(19,4) | ✓ | 60.41% |  |
| 170 | `OtherCurrentLiability` | 其他流动负债 | number(19,4) | ✓ | 45.54% |  |
| 171 | `CLExceptionalItems` | ##流动负债特殊项目 | number(19,4) | ✓ | 1.42% |  |
| 172 | `CLAdjustmentItems` | ##流动负债调整项目 | number(19,4) | ✓ | 1.14% |  |
| 173 | `TotalCurrentLiability` | 流动负债合计 | number(19,4) | ✓ | 94.78% |  |
| 174 | `LTInsContractReserve` | 长期保险合同准备金 | number(19,4) | ✓ | 0.82% | 长期保险合同准备金（LTInsContractReserve）：一般为金融类:保险公司披露科目 |
| 175 | `UnearnedPremiumReserve` | 其中:未到期责任准备金 | number(19,4) | ✓ | 0.57% | 其中:未到期责任准备金（UnearnedPremiumReserve）：一般为金融类:保险公司披露科目 |
| 176 | `OutstandingClaimReserve` | 其中:未决赔款准备金 | number(19,4) | ✓ | 0.43% | 其中:未决赔款准备金（OutstandingClaimReserve）：一般为金融类:保险公司披露科目 |
| 177 | `LifeInsuranceReserve` | 其中:寿险责任准备金 | number(19,4) | ✓ | 0.25% | 其中:寿险责任准备金（LifeInsuranceReserve）：一般为金融类:保险公司披露科目 |
| 178 | `LTHealthInsuranceLR` | 其中:长期健康险责任准备金 | number(19,4) | ✓ | 0.25% | 其中:长期健康险责任准备金（LTHealthInsuranceLR）：一般为金融类:保险公司披露科目 |
| 179 | `LongtermLoan` | 长期借款 | number(19,4) | ✓ | 59.16% |  |
| 180 | `BondsPayable` | 应付债券 | number(19,4) | ✓ | 37.13% |  |
| 181 | `LPreferStock` | 其中:优先股(应付债券) | number(19,4) | ✓ | 0.39% |  |
| 182 | `LPerpetualDebt` | 其中:永续债(应付债券) | number(19,4) | ✓ | 0.44% |  |
| 183 | `LeaseLiabilities` | 租赁负债 | number(19,4) | ✓ | 18.33% |  |
| 184 | `LTAccountPayableTotal` | 长期应付款合计 | number(19,4) | ✓ | 43.87% |  |
| 185 | `LongtermAccountPayable` | 其中:长期应付款 | number(19,4) | ✓ | 23.99% |  |
| 186 | `SpecificAccountPayable` | 其中:专项应付款 | number(19,4) | ✓ | 17.1% |  |
| 187 | `FinLeasesPayable` | 应付融资租赁款 | number(19,4) | ✓ | 0.03% |  |
| 188 | `LongSalariesPay` | 长期应付职工薪酬 | number(19,4) | ✓ | 6.54% |  |
| 189 | `EstimateLiability` | 预计负债 | number(19,4) | ✓ | 21.31% |  |
| 190 | `LongDeferIncome` | 长期递延收益 | number(19,4) | ✓ | 42.68% |  |
| 191 | `IndependenceLiability` | 独立账户负债 | number(19,4) | ✓ | 0.13% | 独立账户负债（IndependenceLiability）：一般为金融类:保险公司披露科目 |
| 192 | `DeferredTaxLiability` | 递延所得税负债 | number(19,4) | ✓ | 45.65% |  |
| 193 | `OtherNonCurrentLiability` | 其他非流动负债 | number(19,4) | ✓ | 22.13% |  |
| 194 | `NCLExceptionalItems` | ##非流动负债特殊项目 | number(19,4) | ✓ | 1.22% |  |
| 195 | `NCLAdjustmentItems` | ##非流动负债调整项目 | number(19,4) | ✓ | 0.47% |  |
| 196 | `TotalNonCurrentLiability` | 非流动负债合计 | number(19,4) | ✓ | 89.25% |  |
| 197 | `OtherLiability` | 其他负债 | number(19,4) | ✓ | 4.04% | 其他负债（OtherLiability）：一般为金融类企业披露科目 |
| 198 | `LExceptionalItems` | ##负债特殊项目 | number(19,4) | ✓ | 0.42% |  |
| 199 | `LAdjustmentItems` | ##负债调整项目 | number(19,4) | ✓ | 0.64% |  |
| 200 | `TotalLiability` | 负债合计 | number(19,4) | ✓ | 99.79% |  |
| 201 | `PaidInCapital` | 实收资本(或股本) | number(19,4) | ✓ | 98.94% |  |
| 202 | `OtherEquityinstruments` | 其他权益工具 | number(19,4) | ✓ | 7.53% |  |
| 203 | `EPreferStock` | 其中:优先股(其他权益工具) | number(19,4) | ✓ | 0.67% |  |
| 204 | `EPerpetualDebt` | 其中:永续债(其他权益工具) | number(19,4) | ✓ | 4.25% |  |
| 205 | `CapitalReserveFund` | 资本公积 | number(19,4) | ✓ | 95.84% |  |
| 206 | `TreasuryStock` | 减:库存股 | number(19,4) | ✓ | 9.45% |  |
| 207 | `SpecificReserves` | 专项储备 | number(19,4) | ✓ | 16.29% |  |
| 208 | `OtherCompositeIncome` | 其他综合收益 | number(19,4) | ✓ | 35.69% |  |
| 209 | `SurplusReserveFund` | 盈余公积 | number(19,4) | ✓ | 94.0% |  |
| 210 | `OrdinaryRiskReserveFund` | 一般风险准备 | number(19,4) | ✓ | 7.34% | 一般风险准备（OrdinaryRiskReserveFund）：一般为金融类企业披露科目 |
| 211 | `TradeRiskRSRVFd` | 交易风险准备 | number(19,4) | ✓ | 0.23% |  |
| 212 | `OtherReserves` | 其他储备(公允价值变动储备) | number(19,4) | ✓ | 0.0% |  |
| 213 | `RetainedProfit` | 未分配利润 | number(19,4) | ✓ | 98.73% |  |
| 214 | `ForeignCurrencyReportConvDiff` | 外币报表折算差额 | number(19,4) | ✓ | 3.7% |  |
| 215 | `UncertainedInvestmentLoss` | 未确认投资损失 | number(19,4) | ✓ | 0.66% |  |
| 216 | `SEExceptionalItems` | ##归属母公司所有者权益(或股东权益)特殊项目 | number(19,4) | ✓ | 0.28% |  |
| 217 | `SEAdjustmentItems` | ##归属母公司所有者权益(或股东权益)调整项目 | number(19,4) | ✓ | 1.18% |  |
| 218 | `SEWithoutMI` | 归属母公司所有者权益(或股东权益)合计 | number(19,4) | ✓ | 99.18% |  |
| 219 | `SECParentCompanyOwners` | 其中:归属于母公司普通股股东权益 | number(19,4) | ✓ | 0.0% |  |
| 220 | `MinorityInterests` | 少数股东权益 | number(19,4) | ✓ | 44.62% |  |
| 221 | `TSEExceptionalItems` | ##所有者权益(或股东权益)特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 222 | `OtherItemsEffectingSE` | ##所有者权益(或股东权益)调整项目 | number(19,4) | ✓ | 0.42% |  |
| 223 | `TotalShareholderEquity` | 所有者权益(或股东权益)合计 | number(19,4) | ✓ | 99.94% |  |
| 224 | `LEExceptionalItems` | ##负债和权益特殊项目 | number(19,4) | ✓ | 0.02% |  |
| 225 | `LEAdjustmentItems` | ##负债和权益调整项目 | number(19,4) | ✓ | 1.03% |  |
| 226 | `TotalLiabilityAndEquity` | 负债和所有者权益(或股东权益)总计 | number(19,4) | ✓ | 100.0% |  |
| 227 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 2.81% |  |
| 228 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 229 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 230 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM NOT IN (110106,110107,110108,110109,110110,110111,110203,110204,110205,120109,120110,120208,120210,120216,120217,130108,130110,130112,130113,140108,140109)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，110201-定期报告:年度报告(关联方)，110202-定期报告:半年度报告(关联方)，120101-临时公告:审计报告(更正后)，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)，120106-临时公告:公开转让说明书(更正后)，120107-临时公告:业绩快报，120108-临时公告:业绩快报(更正后)，120201-临时公告:跟踪评级报告，120202-临时公告:同业存单发行计划，120203-临时公告:比较式财务报表，120204-临时公告:关联方，120205-临时公告:其他，120206-临时公告:前期差错更正，120207-临时公告:第一季度报告，120209-临时公告:第三季度报告，120211-临时公告：年度报告，120212-临时公告：半年度报告，120213-临时公告:受托管理人事务报告，120214-临时公告:资产评估报告，120215-临时公告:资产管理报告，120218-临时公告：主要经营业绩，130101-发行上市书:募集说明书，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130105-发行上市书:审阅报告，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130109-发行上市书:审计报告，130111-发行上市书:其他，140101-发行披露文件:第一季报，140102-发行披露文件:半年度报告，140103-发行披露文件:第三季报，140104-发行披露文件:审计报告，140105-发行披露文件:募集说明书，140106-发行披露文件:跟踪评级报告，140107-发行披露文件:年度报告，140110-发行披露文件:转让服务公告书，140111-发行披露文件:备案登记表，140112-发行披露文件:初始信息披露，150101-发债定期报告:第一季报，150102-发债定期报告:半年度报告，150103-发债定期报告:第三季报，150104-发债定期报告:年度报告，150105-发债:其他报告。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。

### IfMerged (是否合并)

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### EnterpriseType (报表格式类型)

报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业)。 本表报表格式类型(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业性质(CompanyType)。

### ClientDeposit (其中:货币资金:客户资金存款)

其中:货币资金:客户资金存款（ClientDeposit）：一般为金融类:证券公司披露科目

### DepositInCentralBank (其中:现金及存放中央银行款项)

其中:现金及存放中央银行款项（DepositInCentralBank）：一般为金融类:银行企业披露科目

## SQL示例

```sql
-- 查询 资产负债表_新会计准则 数据
SELECT *
FROM dz_balancesheetall
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
