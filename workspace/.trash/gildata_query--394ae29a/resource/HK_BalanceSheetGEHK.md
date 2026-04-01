# HK_BalanceSheetGEHK

**中文名**: 港股资产负债表_一般企业(香港会计准则)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_BalanceSheetGEHK` |
| MySQL表名 | `hk_balancesheetgehk` |
| 中文名 | 港股资产负债表_一般企业(香港会计准则) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 188 |
| 版本 | 1.07 |

## 表描述

1.介绍按香港会计准则、国际会计准则等披露的港股一般企业资产负债表中各项标准化会计指标。该表为港股资产负债表的横表。
2.数据范围:1998年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AN... |
| 6 | `ReportType` | 报表类型 | varchar2(100) | ✓ | 100.0% | 报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年... |
| 7 | `FiscalYear` | 财政年度 | date | ✓ | 100.0% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 8 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与系统常量表中的DM字段关联，令LB = 1314 and DM not in (90)... |
| 9 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 10 | `CompanyNature` | 报表格式类型 | number(10) | ✓ | 100.0% | 报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN... |
| 11 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN ... |
| 12 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 13 | `Gmark` | 聚源转换标识 | number(10) | ✓ | 100.0% | 聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。 |
| 14 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)：1-完整；2-简表。 |
| 15 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 16 | `TotalFixedAsset` | 固定资产合计(元) | number(19,4) | ✓ | 89.46% | 固定资产合计(元)(TotalFixedAsset)：优先取财报披露值，如财报未披露，则固定资产合计=固定资产(元)(F... |
| 17 | `FixedAssets` | 固定资产(元) | number(19,4) | ✓ | 14.94% |  |
| 18 | `WorkshopAndEquipment` | 物业厂房及设备(元) | number(19,4) | ✓ | 74.5% |  |
| 19 | `InvestProperty` | 投资物业(元) | number(19,4) | ✓ | 32.47% |  |
| 20 | `ConstruInProcess` | 在建工程(元) | number(19,4) | ✓ | 9.6% |  |
| 21 | `LandUsufruct` | 土地使用权(元) | number(19,4) | ✓ | 8.93% |  |
| 22 | `AdvancePayment` | 预付款项(元) | number(19,4) | ✓ | 31.63% |  |
| 23 | `PrepaidRentNCA` | 预付租金-非流动资产(元) | number(19,4) | ✓ | 16.55% |  |
| 24 | `LongtermReceivableAccount` | 长期应收款(元) | number(19,4) | ✓ | 5.92% |  |
| 25 | `CWrksCliMonReceNCA` | 应收合约客户款项-非流动资产(元) | number(19,4) | ✓ | 0.12% |  |
| 26 | `InsOtherReceNCA` | 保险及其他应收款项-非流动资产(元) | number(19,4) | ✓ | 0.0% |  |
| 27 | `DevelopmentExpenditure` | 开发支出(元) | number(19,4) | ✓ | 2.2% |  |
| 28 | `SubCompanyEquity` | 联营公司权益(元) | number(19,4) | ✓ | 31.17% |  |
| 29 | `CoBusinessEquity` | 共同控制实体权益(元) | number(19,4) | ✓ | 5.02% |  |
| 30 | `SuppCompEquity` | 附属公司权益(元) | number(19,4) | ✓ | 14.4% |  |
| 31 | `JointVenturesEquity` | 合营公司权益(元) | number(19,4) | ✓ | 11.92% |  |
| 32 | `FixedDepositNCA` | 定期存款-非流动资产(元) | number(19,4) | ✓ | 2.1% |  |
| 33 | `MortagageDepositNCA` | 已抵押存款-非流动资产(元) | number(19,4) | ✓ | 4.4% |  |
| 34 | `LTInvestments` | 长期投资(元) | number(19,4) | ✓ | 9.48% |  |
| 35 | `SecuInvestment` | 证券投资(元) | number(19,4) | ✓ | 4.3% |  |
| 36 | `FinAetAtFValTPLNCA` | 按公平值入损益金融资产-非流动资产(元) | number(19,4) | ✓ | 8.33% |  |
| 37 | `DerFinInstsNCA` | 衍生金融工具-非流动资产(元) | number(19,4) | ✓ | 2.25% |  |
| 38 | `HoldForSaleAssetsNCA` | 可供出售金融资产-非流动资产(元) | number(19,4) | ✓ | 16.07% |  |
| 39 | `DebtInvestment` | 债权投资(元) | number(19,4) | ✓ | 1.47% |  |
| 40 | `OthDebtInvestment` | 其他债权投资(元) | number(19,4) | ✓ | 0.75% |  |
| 41 | `OthEquityInstrument` | 其他权益工具投资(元) | number(19,4) | ✓ | 6.31% |  |
| 42 | `FinAssetsAtFValTOCI` | 按公平值计入其他全面收益的金融资产(元) | number(19,4) | ✓ | 4.64% |  |
| 43 | `OtherFinAssetsNCA` | 其他金融资产(非流动)(元) | number(19,4) | ✓ | 10.75% |  |
| 44 | `UsufructAssets` | 使用权资产(元) | number(19,4) | ✓ | 25.43% |  |
| 45 | `OtherInvestment` | 其他投资(元) | number(19,4) | ✓ | 3.86% |  |
| 46 | `GoodwillIntangibleAssets` | 商誉及无形资产(元) | number(19,4) | ✓ | 57.31% | 商誉及无形资产(元)(GoodwillIntangibleAssets)：优先取财报披露值，如财报未披露，则商誉及无形资... |
| 47 | `IntangibleAssets` | 其中:无形资产(元) | number(19,4) | ✓ | 50.11% |  |
| 48 | `GoodWill` | 其中:商誉(元) | number(19,4) | ✓ | 25.33% |  |
| 49 | `NegaGoodWill` | 负商誉(元) | number(19,4) | ✓ | 0.51% |  |
| 50 | `DeferredTaxAssets` | 递延税项资产(元) | number(19,4) | ✓ | 48.38% |  |
| 51 | `OtherNonCurrentAssets` | 其他非流动资产(元) | number(19,4) | ✓ | 17.87% |  |
| 52 | `NCAExcepItems` | 非流动资产特殊项目(元) | number(19,4) | ✓ | 23.26% |  |
| 53 | `NCAAdjItems` | 非流动资产调整项目(元) | number(19,4) | ✓ | 0.15% |  |
| 54 | `TotalNonCurrentAssets` | 非流动资产合计(元) | number(19,4) | ✓ | 98.07% | 非流动资产合计(元)(TotalNonCurrentAssets)：优先取财报披露值，如财报未披露，则非流动资产合计=固... |
| 55 | `Inventories` | 存货(元) | number(19,4) | ✓ | 66.99% |  |
| 56 | `DeveAndForSalePro` | 发展中及待售物业(元) | number(19,4) | ✓ | 8.62% |  |
| 57 | `AccountReceivables` | 应收帐款(元) | number(19,4) | ✓ | 83.65% |  |
| 58 | `BillReceivable` | 应收票据(元) | number(19,4) | ✓ | 8.22% |  |
| 59 | `ReceivablesFin` | 应收款项融资(元) | number(19,4) | ✓ | 1.86% |  |
| 60 | `AssociateFundRece` | 应收关联方款项(元) | number(19,4) | ✓ | 27.26% |  |
| 61 | `CWrksCliMonReceCA` | 应收合约客户款项-流动资产(元) | number(19,4) | ✓ | 2.8% |  |
| 62 | `OtherReceivable` | 其他应收款(元) | number(19,4) | ✓ | 7.77% |  |
| 63 | `DividendReceivables` | 应收股利(元) | number(19,4) | ✓ | 1.64% |  |
| 64 | `InterestReceivables` | 应收利息(元) | number(19,4) | ✓ | 1.87% |  |
| 65 | `InsOtherReceCA` | 保险及其他应收款项-流动资产(元) | number(19,4) | ✓ | 0.04% |  |
| 66 | `OtherAccounetrece` | 预付款按金及其他应收款(元) | number(19,4) | ✓ | 64.82% |  |
| 67 | `TaxReceivable` | 预缴及应收税项(元) | number(19,4) | ✓ | 22.78% |  |
| 68 | `PrepaidRentCA` | 预付租金-流动资产(元) | number(19,4) | ✓ | 0.86% |  |
| 69 | `Cash` | 现金及等价物(元) | number(19,4) | ✓ | 97.15% |  |
| 70 | `ShortTermDeposit` | 短期存款(元) | number(19,4) | ✓ | 4.48% |  |
| 71 | `FixedDepositCA` | 定期存款-流动资产(元) | number(19,4) | ✓ | 6.99% |  |
| 72 | `DepositInCentralBank` | 存放中央银行款项(元) | number(19,4) | ✓ | 0.05% |  |
| 73 | `MortagageDeposit` | 已抵押存款(元) | number(19,4) | ✓ | 34.79% |  |
| 74 | `AdvancesTCusts` | 客户垫款(元) | number(19,4) | ✓ | 0.02% |  |
| 75 | `LendCapital` | 拆出资金(元) | number(19,4) | ✓ | 0.06% |  |
| 76 | `ShortTermInvest` | 短期投资(元) | number(19,4) | ✓ | 8.29% |  |
| 77 | `HForSaleAssetsCA` | 可供出售金融资产-流动资产(元) | number(19,4) | ✓ | 2.19% |  |
| 78 | `FinAetAtFValTPLCA` | 按公平值入损益金融资产-流动资产(元) | number(19,4) | ✓ | 22.51% |  |
| 79 | `DerFinInstsCA` | 衍生金融工具-流动资产(元) | number(19,4) | ✓ | 6.07% |  |
| 80 | `ContractualAssets` | 合同资产(元) | number(19,4) | ✓ | 8.23% |  |
| 81 | `OtherFinAssetsCA` | 其他金融资产(流动)(元) | number(19,4) | ✓ | 3.59% |  |
| 82 | `OtherCurrentAssets` | 其他流动资产(元) | number(19,4) | ✓ | 8.34% |  |
| 83 | `LoansReceivable` | 应收贷款(元) | number(19,4) | ✓ | 5.6% |  |
| 84 | `HoldAndFSAssets` | 持有待售资产(元) | number(19,4) | ✓ | 4.63% |  |
| 85 | `CAExcepItems` | 流动资产特殊项目(元) | number(19,4) | ✓ | 28.5% |  |
| 86 | `CAAdjItems` | 流动资产调整项目(元) | number(19,4) | ✓ | 0.19% |  |
| 87 | `TotalCurrentAssets` | 流动资产合计(元) | number(19,4) | ✓ | 99.07% | 流动资产合计(元)(TotalCurrentAssets)：优先取财报披露值，如财报未披露，则流动资产合计=存货(元)+... |
| 88 | `OtherAssets` | 资产其他项目 | number(19,4) | ✓ | 0.5% |  |
| 89 | `AAdjItems` | 资产调整项目(元) | number(19,4) | ✓ | 0.04% |  |
| 90 | `TotalAssets` | 总资产(元) | number(19,4) | ✓ | 99.85% | 总资产(元)(TotalAssets)：优先取财报披露值，如财报未披露，则总资产=固定资产合计(元)+投资物业(元)+在... |
| 91 | `AccountsPayable` | 应付帐款(元) | number(19,4) | ✓ | 83.7% |  |
| 92 | `NotesPayable` | 应付票据(元) | number(19,4) | ✓ | 9.06% |  |
| 93 | `TaxesPayable` | 应付税项(元) | number(19,4) | ✓ | 74.51% |  |
| 94 | `DividendPayable` | 应付股利(元) | number(19,4) | ✓ | 6.23% |  |
| 95 | `SalariesPayable` | 应付职工薪酬(元) | number(19,4) | ✓ | 8.72% |  |
| 96 | `InterestPayable` | 应付利息(元) | number(19,4) | ✓ | 2.7% |  |
| 97 | `FAssociateFundRecCL` | 应付关联方款项-流动负债(元) | number(19,4) | ✓ | 32.1% |  |
| 98 | `OtherFeesPayable` | 其他应付款及应计费用(元) | number(19,4) | ✓ | 55.17% |  |
| 99 | `AdvanceReceipts` | 预收款项(元) | number(19,4) | ✓ | 12.0% |  |
| 100 | `CustomerDeposits` | 客户存款(元) | number(19,4) | ✓ | 0.19% |  |
| 101 | `ShortTermLoan` | 短期借款(元) | number(19,4) | ✓ | 11.61% |  |
| 102 | `BankLoansAndOverdraft` | 银行贷款及透支(元) | number(19,4) | ✓ | 53.87% |  |
| 103 | `FOtherLoanCL` | 其他贷款-流动负债(元) | number(19,4) | ✓ | 5.6% |  |
| 104 | `UnearnedPremiumReserve` | 未到期责任准备金(元) | number(19,4) | ✓ | 0.01% |  |
| 105 | `NotDecidedReservesCL` | 未决赔款准备-流动负债(元) | number(19,4) | ✓ | 0.01% |  |
| 106 | `NotMatuRiskReserves` | 未到期风险准备金(元) | number(19,4) | ✓ | 0.01% |  |
| 107 | `DerFinInstsCL` | 衍生金融工具-流动负债(元) | number(19,4) | ✓ | 7.56% |  |
| 108 | `InveContLiaCL` | 投资合同负债-流动负债(元) | number(19,4) | ✓ | 0.02% |  |
| 109 | `BFinInstDepBorMoney` | 同业及其他金融机构存放及拆入款项(元) | number(19,4) | ✓ | 0.0% |  |
| 110 | `LFromOthBanksCL` | 拆入资金-流动负债(元) | number(19,4) | ✓ | 0.6% |  |
| 111 | `SBbSecuProceeds` | 卖出回购金融资产款(元) | number(19,4) | ✓ | 0.69% |  |
| 112 | `FAccruedBadDebtCL` | 拨备-流动负债(元) | number(19,4) | ✓ | 7.24% |  |
| 113 | `FFinanceLeaseOwesCL` | 租赁负债-流动负债(元) | number(19,4) | ✓ | 32.91% |  |
| 114 | `DeferredProceedsCL` | 递延收入-流动负债(元) | number(19,4) | ✓ | 6.6% |  |
| 115 | `FinliabAtFV` | 以公平值计入损益金融负债(元) | number(19,4) | ✓ | 3.35% |  |
| 116 | `OtherFinLiabilityCL` | 其他金融负债(流动)(元) | number(19,4) | ✓ | 1.93% |  |
| 117 | `ContractLiability` | 合同负债(元) | number(19,4) | ✓ | 22.6% |  |
| 118 | `OtherCurrentLiability` | 其他流动负债(元) | number(19,4) | ✓ | 5.94% |  |
| 119 | `HoldAndFSLi` | 持有待售负债(元) | number(19,4) | ✓ | 2.03% |  |
| 120 | `Issuedbond` | 已发行债券(元) | number(19,4) | ✓ | 3.17% |  |
| 121 | `CLExcepItems` | 流动负债特殊项目(元) | number(19,4) | ✓ | 24.39% |  |
| 122 | `CLAdjItems` | 流动负债调整项目(元) | number(19,4) | ✓ | 0.2% |  |
| 123 | `TotalCurrentLiability` | 流动负债合计(元) | number(19,4) | ✓ | 98.98% | 流动负债合计(元)(TotalCurrentLiability)：优先取财报披露值，如财报未披露，则流动负债合计=应付帐... |
| 124 | `NetCurrentLiability` | 净流动资产(元) | number(19,4) | ✓ | 99.37% | 净流动资产(元)(NetCurrentLiability)：优先取财报披露值，如财报未披露，则净流动资产=流动资产合计(... |
| 125 | `AssetLessCLiability` | 总资产减流动负债(元) | number(19,4) | ✓ | 99.98% | 总资产减流动负债(元)(AssetLessCLiability)：优先取财报披露值，如财报未披露，则总资产减流动负债=总... |
| 126 | `LongtermLoan` | 长期银行贷款(元) | number(19,4) | ✓ | 42.87% |  |
| 127 | `NFOtherLoanNCL` | 其他贷款-非流动负债(元) | number(19,4) | ✓ | 3.99% |  |
| 128 | `LFromOthBanksNCL` | 拆入资金-非流动负债(元) | number(19,4) | ✓ | 0.02% |  |
| 129 | `LTAccountPayable` | 长期应付款(元) | number(19,4) | ✓ | 7.54% |  |
| 130 | `LongSalariesPay` | 长期应付职工薪酬(元) | number(19,4) | ✓ | 3.65% |  |
| 131 | `NFAssociateFundRecNCL` | 应付关联方款项-非流动负债(元) | number(19,4) | ✓ | 4.58% |  |
| 132 | `NFFinanceLeaseOwesNCL` | 租赁负债-非流动负债(元) | number(19,4) | ✓ | 33.34% |  |
| 133 | `DeferredTaxLiability` | 递延税项负债(元) | number(19,4) | ✓ | 57.48% |  |
| 134 | `NFDeferredProceedsNCL` | 递延收入-非流动负债(元) | number(19,4) | ✓ | 17.35% |  |
| 135 | `NFAccruedBadDebtNCL` | 拨备-非流动负债(元) | number(19,4) | ✓ | 7.27% |  |
| 136 | `ConBillAndBond` | 可转换票据及债券(元) | number(19,4) | ✓ | 10.55% |  |
| 137 | `DebtInstruIssued` | 已发行债务工具(元) | number(19,4) | ✓ | 0.1% |  |
| 138 | `DerFinInstsNCL` | 衍生金融工具-非流动负债(元) | number(19,4) | ✓ | 3.14% |  |
| 139 | `RetBfitsResp` | 退休福利责任(元) | number(19,4) | ✓ | 2.66% |  |
| 140 | `NotDecidedReservesNCL` | 未决赔款准备-非流动负债(元) | number(19,4) | ✓ | 0.01% |  |
| 141 | `InveContLiaNCL` | 投资合约负债-非流动负债(元) | number(19,4) | ✓ | 0.03% |  |
| 142 | `InsurAccPayableNCL` | 保险应付账款-非流动负债(元) | number(19,4) | ✓ | 0.0% |  |
| 143 | `OtherFinLiabilityNCL` | 其他金融负债(非流动负债)(元) | number(19,4) | ✓ | 0.35% |  |
| 144 | `OtherNonCurrentLiab` | 其他非流动负债(元) | number(19,4) | ✓ | 9.14% |  |
| 145 | `EstimateLiability` | 预计负债(元) | number(19,4) | ✓ | 3.02% |  |
| 146 | `NCLExcepItems` | 非流动负债特殊项目(元) | number(19,4) | ✓ | 21.77% |  |
| 147 | `NCLAdjItems` | 非流动负债调整项目(元) | number(19,4) | ✓ | 0.1% |  |
| 148 | `TotalNonCurrentLiab` | 非流动负债合计(元) | number(19,4) | ✓ | 82.27% | 非流动负债合计(元)(TotalNonCurrentLiab)：优先取财报披露值，如财报未披露，则非流动负债合计=长期银... |
| 149 | `OtherLiability` | 负债其他项目 | number(19,4) | ✓ | 0.53% |  |
| 150 | `LAdjuItems` | 负债调整项目(元) | number(19,4) | ✓ | 0.01% |  |
| 151 | `TotalLiability` | 总负债(元) | number(19,4) | ✓ | 99.62% | 总负债(元)(TotalLiability)：优先取财报披露值，如财报未披露，则总负债=应付帐款(元)+应付票据(元)+... |
| 152 | `AssetLessTLiability` | 总资产减总负债(元) | number(19,4) | ✓ | 99.9% | 总资产减总负债(元)(AssetLessTLiability)：优先取财报披露值，如财报未披露，则总资产减总负债=总资产... |
| 153 | `TotalIntANCTLiability` | 总权益及非流动负债(元) | number(19,4) | ✓ | 82.65% | 总权益及非流动负债(元)(TotalIntANCTLiability)：优先取财报披露值，如财报未披露，则总权益及非流动... |
| 154 | `ShareCapitalAndSharePremium` | 股本及溢价(元) | number(19,4) | ✓ | 0.26% | 股本及溢价(元)(ShareCapitalAndSharePremium)：财报披露值。 |
| 155 | `ShareCapital` | 股本(元) | number(19,4) | ✓ | 95.13% |  |
| 156 | `OtherEquityinstruments` | 其他权益工具(元) | number(19,4) | ✓ | 2.63% |  |
| 157 | `EPreferStock` | 其中:优先股(其他权益工具)(元) | number(19,4) | ✓ | 0.15% |  |
| 158 | `EPerpetualDebt` | 其中:永续债(其他权益工具)(元) | number(19,4) | ✓ | 1.41% |  |
| 159 | `CapitalReserveFund` | 资本公积(元) | number(19,4) | ✓ | 8.66% |  |
| 160 | `StockPremium` | 股本溢价(元) | number(19,4) | ✓ | 9.24% |  |
| 161 | `Reserves` | 公积金(元) | number(19,4) | ✓ | 0.13% | 公积金(元)(Reserves)：财报披露值。 |
| 162 | `SurplusReserveFund` | 盈余公积(元) | number(19,4) | ✓ | 7.55% |  |
| 163 | `Reserve` | 储备(元) | number(19,4) | ✓ | 75.24% |  |
| 164 | `ReserveFund` | 法定储备(元) | number(19,4) | ✓ | 0.43% |  |
| 165 | `RevaluationReserve` | 重估储备(元) | number(19,4) | ✓ | 0.46% |  |
| 166 | `ExchangeReserve` | 汇兑储备(元) | number(19,4) | ✓ | 1.04% |  |
| 167 | `OtherReserve` | 其他储备(元) | number(19,4) | ✓ | 10.35% |  |
| 168 | `HoldProfit` | 保留溢利(元) | number(19,4) | ✓ | 13.18% |  |
| 169 | `RetainedProfit` | 未分配利润(元) | number(19,4) | ✓ | 8.07% |  |
| 170 | `TreasuryStock` | 减:库存股(元) | number(19,4) | ✓ | 3.01% |  |
| 171 | `OtherCompositeIncome` | 其他综合收益(元) | number(19,4) | ✓ | 4.95% |  |
| 172 | `SimulantAllotDividend` | 拟派股息(元) | number(19,4) | ✓ | 6.8% |  |
| 173 | `SEExcepItems` | 股东权益特殊项目(元) | number(19,4) | ✓ | 7.35% |  |
| 174 | `SEAdjItems` | 股东权益调整项目(元) | number(19,4) | ✓ | 0.17% |  |
| 175 | `ShareholderEquity` | 股东权益(元) | number(19,4) | ✓ | 99.84% | 股东权益(元)(ShareholderEquity)：优先取财报披露值，如财报未披露，则股东权益=股本及溢价(元)(Sh... |
| 176 | `SECParentCompanyOwners` | 其中:归属于母公司普通股股东权益(元) | number(19,4) | ✓ | 0.0% |  |
| 177 | `MinorityInterests` | 非控股权益(元) | number(19,4) | ✓ | 52.17% |  |
| 178 | `AddEquityInstruments` | 额外股本工具(元) | number(19,4) | ✓ | 0.93% |  |
| 179 | `TSEExceptionalItems` | 所有者权益(或股东权益)特殊项目(元) | number(19,4) | ✓ | 0.07% |  |
| 180 | `OtherItemsEffectingSE` | 所有者权益(或股东权益)调整项目(元) | number(19,4) | ✓ | 0.01% |  |
| 181 | `TotalInterests` | 总权益(元) | number(19,4) | ✓ | 99.83% | 总权益(元)(TotalInterests)：优先取财报披露值，如财报未披露，则总权益=股东权益(元)(Sharehol... |
| 182 | `LEAdjustmentItems` | 负债和权益调整项目(元) | number(19,4) | ✓ | 0.01% |  |
| 183 | `LEExceptionalItems` | 负债和权益特殊项目(元) | number(19,4) | ✓ | 0.29% |  |
| 184 | `TotalIntATotalLiab` | 总权益及总负债(元) | number(19,4) | ✓ | 99.96% | 总权益及总负债(元)(TotalIntATotalLiab)：优先取财报披露值，如财报未披露，则总权益及总负债=总负债(... |
| 185 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 186 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 187 | `JSID` | JSID | number(19) | ✗ |  |  |
| 188 | `BeginDate` | 开始日期 | date | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSourceCode (信息来源代码)

信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IVALUE IN (1,3)，得到信息来源代码的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，27-配发结果，28-修改已刊发的财务报表及报告，29-修正重大错误而做出的前期调整，30-修订已刊发初步业绩的资料，32-内幕消息-年度报告，33-内幕消息-第一季报，34-内幕消息-第二季报，35-内幕消息-第三季报，36-内幕消息-第四季报，37-内幕消息-中期报告，38-内幕消息-申请版本，39-内幕消息-招股章程，40-内幕消息-聆讯后资料集，41-内幕消息-其他，99-其他。

### ReportType (报表类型)

报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年变更，如年度报告累计报告期是18或15个月，对应披露的12个月中期数据)、第五季报(企业发生财年变更，如年度报告累计报告期是18个月，对应披露的15个月中期数据)、年度报告、其他（企业披露的非标准报告期数据，如1、2、4、5等月，或者非完整累计月度报告数据）等。

### FiscalYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”。

### PeriodMark (日期标志)

日期标志(PeriodMark)与系统常量表中的DM字段关联，令LB = 1314 and DM not in (90)，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，99-其他。
注：1、资产表期末对应报告期的会计期间长度；2、资产表披露的可比时点都是期初（上年年末），也通过日期标志区分是第几季报对应期初；如第一季报对应期初（上年年末）的日期标志是3-3个月；第二季报对应期初（上年年末）的日期标志是6-半年度，依次类推。

### CompanyNature (报表格式类型)

报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN (4,5)，得到报表格式类型的具体描述：1-普通，2-金融，3-保险，6-证券，7-信托。本表报表格式类型(CompanyNature)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，其中证券和信托因披露形式与一般类企业类似，但是又存在一定区别，所以单独分类展示。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，120-澳门会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则(2007)，521-中国会计准则(1993)。

### Gmark (聚源转换标识)

聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。

### IfComplete (完整标志)

完整标志(IfComplete)：1-完整；2-简表。

## SQL示例

```sql
-- 查询 港股资产负债表_一般企业(香港会计准则) 数据
SELECT *
FROM hk_balancesheetgehk
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
