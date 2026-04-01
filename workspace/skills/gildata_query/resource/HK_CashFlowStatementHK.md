# HK_CashFlowStatementHK

**中文名**: 港股现金流量表(香港会计准则)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CashFlowStatementHK` |
| MySQL表名 | `hk_cashflowstatementhk` |
| 中文名 | 港股现金流量表(香港会计准则) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 137 |
| 版本 | 1.05 |

## 表描述

1.内容说明：介绍按香港会计准则、国际会计准则等披露的港股企业现金流量表中各项标准化财务指标。该表为港股现金流量表的横表。
2.表内“减项”类字段统一以负数形式展示；
3.数据范围：1999年至今。
4.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IV... |
| 5 | `InfoSourceDes` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ReportType` | 报表类型 | varchar2(100) | ✓ | 100.0% | 报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年... |
| 7 | `FiscalYear` | 财政年度 | date | ✓ | 100.0% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 8 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM... |
| 9 | `BeginDate` | 开始日期 | date | ✓ | 100.0% |  |
| 10 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 11 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN... |
| 12 | `CompanyType` | 报表格式类型 | number(10) | ✗ | 100.0% | 报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN... |
| 13 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 14 | `Gmark` | 聚源转换标识 | number(10) | ✓ | 100.0% | 聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。 |
| 15 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)：1-完整；2-简表。 |
| 16 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 17 | `EarningBeforeTax` | 除税前溢利(元) | number(19,4) | ✓ | 60.19% | 除税前溢利(元)(EarningBeforeTax)：非中国会计准则下，企业多数披露除税前溢利，少数企业未披露除税前溢利... |
| 18 | `InterestIncomeAD` | 利息(收入)-调整(元) | number(19,4) | ✓ | 47.65% | 利息(收入)-调整（InterestIncomeAD）：以该字段说明本表处理的一些规则，（收入）代表数值为负数时为利息收... |
| 19 | `InterestExpAD` | 利息支出-调整(元) | number(19,4) | ✓ | 16.46% |  |
| 20 | `DividendIncomeAD` | 股息(收入)-调整(元) | number(19,4) | ✓ | 10.47% |  |
| 21 | `InvestProfAloss` | 投资损(益)(元) | number(19,4) | ✓ | 9.03% | 投资损(益)（InvestProfAloss）：以该字段说明本表处理的一些规则，（益）代表数值为负数时为投资收益，数值为... |
| 22 | `AffilCompProfAloss` | 应占附属公司(盈)亏(元) | number(19,4) | ✓ | 22.86% |  |
| 23 | `DevalAndAccBadDebt` | 减值与拨备(元): | number(19,4) | ✓ | 44.34% | 减值与拨备(元):(DevalAndAccBadDebt)：优先取财报披露值，如财报未披露，则减值与拨备=物业、厂房及设... |
| 24 | `DevalofProPlEquip` | ###其中:物业、厂房及设备减值(回拨)(元) | number(19,4) | ✓ | 7.96% |  |
| 25 | `DevalofAvaForSaleInv` | ###其中:可供出售投资减值(回拨)(元) | number(19,4) | ✓ | 1.81% |  |
| 26 | `DevalofInventories` | ###其中:存货减值(回拨)(元) | number(19,4) | ✓ | 14.88% |  |
| 27 | `DevalofTradeRece` | ###其中:应收贸易账款减值(回拨)(元) | number(19,4) | ✓ | 18.78% |  |
| 28 | `DevalofGoodwill` | ###其中:商誉减值(元) | number(19,4) | ✓ | 3.82% |  |
| 29 | `DevalofOthers` | ###其中:其他减值与拨备(元) | number(19,4) | ✓ | 29.94% |  |
| 30 | `RevaluationSurplus` | 重估盈余(元): | number(19,4) | ✓ | 31.36% | 重估盈余(元):(RevaluationSurplus)：优先取财报披露值，如财报未披露，则重估盈余=投资物业公平值(增... |
| 31 | `CInFVofInvPropert` | ###其中:投资物业公平值(增)减(元) | number(19,4) | ✓ | 12.21% |  |
| 32 | `CInFVofDerFinInst` | ###其中:衍生金融工具公平值(增)减(元) | number(19,4) | ✓ | 5.94% |  |
| 33 | `CInFVofOtherAssets` | ###其中:其他公平值变动(元) | number(19,4) | ✓ | 21.0% |  |
| 34 | `ProfitDispOfAssets` | 出售资产损(益)(元): | number(19,4) | ✓ | 45.8% | 出售资产损(益)(元):(ProfitDispOfAssets)：优先取财报披露值，如财报未披露，则出售资产损(益)=出... |
| 35 | `ProfDispOfAFSaleInv` | ###其中:出售可供出售投资损(益)(元) | number(19,4) | ✓ | 3.74% |  |
| 36 | `ProfDispOfAffCEqu` | ###其中:出售附属公司权益损(益)(元) | number(19,4) | ✓ | 11.13% |  |
| 37 | `ProfDispOfProPlEquip` | ###其中:出售物业、机器及设备损(益)(元) | number(19,4) | ✓ | 41.19% |  |
| 38 | `ProfDispOfOthAssets` | ###其中:出售其他资产损(益)(元) | number(19,4) | ✓ | 10.33% |  |
| 39 | `DepDividerSale` | 折旧及摊销(元): | number(19,4) | ✓ | 58.18% | 折旧及摊销(元):(DepDividerSale)：优先取财报披露值，如财报未披露，则折旧及摊销=折旧(元)(Depre... |
| 40 | `Depreciation` | ###其中:折旧(元) | number(19,4) | ✓ | 28.42% |  |
| 41 | `FixedAssetDepreciation` | ###其中:固定资产折旧、油气资产折耗、生产性生物资产折旧(元) | number(19,4) | ✓ | 29.52% |  |
| 42 | `UsufructAssetsDA` | ###其中:使用权资产摊销/折旧(元) | number(19,4) | ✓ | 15.16% |  |
| 43 | `InvestPropertyDA` | ###其中:投资性房地产折旧/摊销(元) | number(19,4) | ✓ | 3.62% |  |
| 44 | `IntangibleAssetAmort` | ###其中:无形资产摊销(元) | number(19,4) | ✓ | 25.95% |  |
| 45 | `OtherDepDividerSale` | ###其中:其他折旧及摊销(元) | number(19,4) | ✓ | 16.37% |  |
| 46 | `FinancialExpense` | 财务费用(元) | number(19,4) | ✓ | 34.63% |  |
| 47 | `ExchangeIncome` | 汇兑损(益)(元) | number(19,4) | ✓ | 14.16% |  |
| 48 | `UnrealExchangeIncome` | 未实现汇兑损(益)(元) | number(19,4) | ✓ | 2.91% |  |
| 49 | `DeferredRevenueAmortization` | 递延收入摊销(元) | number(19,4) | ✓ | 2.39% |  |
| 50 | `SpeItemsManageAdj` | 经营调整特殊项目(元) | number(19,4) | ✓ | 36.44% |  |
| 51 | `AdjItemsManageAdj` | 经营调整调整项目(元) | number(19,4) | ✓ | 2.13% |  |
| 52 | `OpeProBefChgInOpeCap` | 经营资金变动前经营溢利(元) | number(19,4) | ✓ | 58.09% | 经营资金变动前经营溢利(元)(OpeProBefChgInOpeCap)：优先取财报披露值，如财报未披露，完整报表（If... |
| 53 | `InventoryChange` | 存货(增加)减少(元) | number(19,4) | ✓ | 43.2% |  |
| 54 | `ProUnderDevelChange` | 发展中物业(增)减(元) | number(19,4) | ✓ | 3.84% |  |
| 55 | `AccReceivChange` | 应收帐款(增加)减少(元) | number(19,4) | ✓ | 55.37% |  |
| 56 | `AccPayableChange` | 应付帐款增加(减少)(元) | number(19,4) | ✓ | 56.58% |  |
| 57 | `AdvReceiptsChange` | 预收款项增(减)(元) | number(19,4) | ✓ | 5.36% |  |
| 58 | `AdvPaymentChange` | 预付款项(增)减(元) | number(19,4) | ✓ | 24.94% |  |
| 59 | `FAAFValOnPLChange` | 按公平值计入损益的金融资产(增)减(非银)(元) | number(19,4) | ✓ | 4.02% |  |
| 60 | `FLAFValOnPLChange` | 按公平值计入损益的金融负债增(减)(非银)(元) | number(19,4) | ✓ | 0.37% |  |
| 61 | `DerFinInstChange` | 衍生金融工具(增)减(元) | number(19,4) | ✓ | 1.77% |  |
| 62 | `InsuReceivChange` | 保险业务应收款(增)减(元) | number(19,4) | ✓ | 0.08% |  |
| 63 | `InsuContLiabChange` | 保险合同负债增(减)(元) | number(19,4) | ✓ | 0.11% |  |
| 64 | `AccRePayableChange` | 应付分保帐款增(减)(元) | number(19,4) | ✓ | 0.04% |  |
| 65 | `BBackSFAssetsChange` | 买入返售金融资产(增)减(元) | number(19,4) | ✓ | 1.09% |  |
| 66 | `BankDepositChange` | 银行存款(增)减(元) | number(19,4) | ✓ | 0.41% |  |
| 67 | `LoansAAdvanChange` | 发放贷款及垫款(增)减(元) | number(19,4) | ✓ | 1.76% |  |
| 68 | `BFAAFValOnPLChange` | 按公平值计入损益的金融资产(增)减(元) | number(19,4) | ✓ | 0.71% |  |
| 69 | `SpeItemsOpeAchange` | 经营资产变动特殊项目(元) | number(19,4) | ✓ | 1.89% |  |
| 70 | `BorFromCBChange` | 向中央银行借款增(减)(元) | number(19,4) | ✓ | 0.95% |  |
| 71 | `CusDepositsChange` | 客戶存款增(减)(元) | number(19,4) | ✓ | 1.65% |  |
| 72 | `BFLAFValOnPLChange` | 按公平值计入损益的金融负债增(减)(元) | number(19,4) | ✓ | 0.38% |  |
| 73 | `SpeItemsOpeLchange` | 经营负债变动特殊项目(元) | number(19,4) | ✓ | 1.89% |  |
| 74 | `SpeItemsWCapChange` | 营运资金变动特殊项目(元) | number(19,4) | ✓ | 33.23% |  |
| 75 | `AdjItemsWCapChange` | 营运资本变动调整项目(元) | number(19,4) | ✓ | 0.19% |  |
| 76 | `SpeItemsCashReceiptsFOpe` | 经营产生现金特殊项目(元) | number(19,4) | ✓ | 0.17% |  |
| 77 | `CashReceiptsFOpe` | 经营产生现金(元) | number(19,4) | ✓ | 67.0% | 经营产生现金(元)(CashReceiptsFOpe)：优先取财报披露值，如财报未披露，完整报表（IfComplete=... |
| 78 | `HKProfitsTaxPaid` | 已缴香港利得税(元) | number(19,4) | ✓ | 9.67% |  |
| 79 | `ChinaIncomeTaxPaid` | 已缴中国所得税(元) | number(19,4) | ✓ | 7.39% |  |
| 80 | `OtherTaxes` | 其他税项(元) | number(19,4) | ✓ | 46.79% |  |
| 81 | `DividendsRecBO` | 已收股息-经营(元) | number(19,4) | ✓ | 1.99% |  |
| 82 | `DividendPaidBO` | 己付股息-经营(元) | number(19,4) | ✓ | 0.4% |  |
| 83 | `InterestRecBO` | 已收利息-经营(元) | number(19,4) | ✓ | 15.72% |  |
| 84 | `InterestPaidBO` | 已付利息-经营(元) | number(19,4) | ✓ | 17.9% |  |
| 85 | `SpeItemsOpeBusi` | 经营业务特殊项目(元) | number(19,4) | ✓ | 32.96% |  |
| 86 | `AdjItemsOpeBusi` | 经营业务调整项目(元) | number(19,4) | ✓ | 9.11% |  |
| 87 | `NetOpeCFlow` | 经营业务现金净额(元) | number(19,4) | ✓ | 99.99% | 经营业务现金净额(元)(NetOpeCFlow)：优先取财报披露值，如财报未披露，当完整报表（IfComplete=1）... |
| 88 | `FinanceAndSpeItems` | 融资费用及投资回报等特殊项目(元) | number(19,4) | ✓ | 2.14% |  |
| 89 | `InterestRecIB` | 已收利息-投资(元) | number(19,4) | ✓ | 46.11% |  |
| 90 | `DividendsRecIB` | 已收股息-投资(元) | number(19,4) | ✓ | 24.62% |  |
| 91 | `RestrictCashChange` | 受限制现金(增)减(元) | number(19,4) | ✓ | 3.11% |  |
| 92 | `LoanReceivableChange` | 应收贷款(增)减(元) | number(19,4) | ✓ | 18.88% |  |
| 93 | `DepositChange` | 存款减少(增加)(元) | number(19,4) | ✓ | 29.18% |  |
| 94 | `VendCapitalAssents` | 出售固定资产(元) | number(19,4) | ✓ | 51.85% |  |
| 95 | `PurCapitalAssents` | 购买固定资产(元)(减项) | number(19,4) | ✓ | 78.25% |  |
| 96 | `VendIntassets` | 出售无形资产及其他资产(元) | number(19,4) | ✓ | 2.09% |  |
| 97 | `PurIntassets` | 购买无形资产及其他资产(元)(减项) | number(19,4) | ✓ | 23.12% |  |
| 98 | `VendAffCompanies` | 出售附属公司及其他营业单位(元) | number(19,4) | ✓ | 16.32% |  |
| 99 | `PurAffCompanies` | 收购附属公司及其他营业单位(元)(减项) | number(19,4) | ✓ | 18.26% |  |
| 100 | `DisinvestmentCash` | 收回投资所得现金(元) | number(19,4) | ✓ | 32.11% |  |
| 101 | `InvestPaymentCash` | 投资支付现金(元)(减项) | number(19,4) | ✓ | 45.06% |  |
| 102 | `InvestAdjustedOther` | 投资业务特殊项目(元) | number(19,4) | ✓ | 49.24% |  |
| 103 | `InvestAdjustedItems` | 投资业务调整项目(元) | number(19,4) | ✓ | 0.27% |  |
| 104 | `NetInvbusiCFlow` | 投资业务现金净额(元) | number(19,4) | ✓ | 98.99% | 投资业务现金净额(元)(NetInvbusiCFlow)：优先取财报披露值，如财报未披露，投资业务现金净额=已收利息-投... |
| 105 | `CashAndOtherBefFin` | 融资前现金其他项目(元) | number(19,4) | ✓ | 0.04% |  |
| 106 | `NetCashBeforFinance` | 融资前现金净额(元) | number(19,4) | ✓ | 99.93% | 融资前现金净额(元)(NetCashBeforFinance)：优先取财报披露值，如财报未披露，融资前现金净额=经营业务... |
| 107 | `NewLoan` | 新增借款(元) | number(19,4) | ✓ | 58.25% |  |
| 108 | `Refund` | 偿还借款(元)(减项) | number(19,4) | ✓ | 61.74% |  |
| 109 | `IssuanceSharesandBonds` | 发行股份及债券(元) | number(19,4) | ✓ | 26.76% | 发行股份及债券(元)(IssuanceSharesandBonds)：优先取财报披露值，如财报未披露，发行股份及债券=发... |
| 110 | `IssueShares` | 其中:发行股份(元) | number(19,4) | ✓ | 21.49% |  |
| 111 | `IssueBonds` | 其中:发行债券(元) | number(19,4) | ✓ | 6.96% |  |
| 112 | `InterestPaidFB` | 已付利息-融资(元)(减项) | number(19,4) | ✓ | 42.52% |  |
| 113 | `DividendPaidFB` | 已付股息-融资(元)(减项) | number(19,4) | ✓ | 41.91% |  |
| 114 | `AbsorbInvestIncome` | 吸收投资所得(元) | number(19,4) | ✓ | 16.64% |  |
| 115 | `IssExpAPayOfRedSecu` | 发行费用及赎回证券支出(元)(减项) | number(19,4) | ✓ | 19.02% |  |
| 116 | `PledgedDepositChange` | 已抵押银行存款(增)减(元)(减项) | number(19,4) | ✓ | 3.29% |  |
| 117 | `LeaseLiabilitiesPaid` | 偿还租赁负债(元)(减项) | number(19,4) | ✓ | 32.82% |  |
| 118 | `FinanceAdjustedOther` | 融资业务其他项目(元) | number(19,4) | ✓ | 52.29% |  |
| 119 | `FinanceAdjustedItems` | 融资业务调整项目(元) | number(19,4) | ✓ | 0.56% |  |
| 120 | `NetCashFromFinance` | 融资业务现金净额(元) | number(19,4) | ✓ | 96.5% | 融资业务现金净额(元)(NetCashFromFinance)：优先取财报披露值，如财报未披露，融资业务现金净额=新增借... |
| 121 | `OtherItemsAffectNC` | 影响现金净额其他项目(元) | number(19,4) | ✓ | 0.58% |  |
| 122 | `AdjustmentItemsCE` | 影响现金净额调整项目(元) | number(19,4) | ✓ | 0.45% |  |
| 123 | `NetCash` | 现金净额(元) | number(19,4) | ✓ | 99.96% | 现金净额(元)(NetCash)：优先取财报披露值，如财报未披露，现金净额=融资前现金净额(元)(NetCashBefo... |
| 124 | `EffectOfRate` | 汇率影响(元) | number(19,4) | ✓ | 70.43% |  |
| 125 | `CashEquivalentIncreaseEX` | 现金及现金等价物净增加额(含汇率影响)(元) | number(19,4) | ✓ | 99.96% | 现金及现金等价物净增加额(含汇率影响)(元)(CashEquivalentIncreaseEX)：优先取财报披露值，如财... |
| 126 | `BeginPeriodCash` | 期初现金(元) | number(19,4) | ✓ | 99.58% |  |
| 127 | `ItemsPeriod` | 期间变动其他项目(元) | number(19,4) | ✓ | 0.74% |  |
| 128 | `AdjustedItemsPeriod` | 期间变动调整项目(元) | number(19,4) | ✓ | 0.24% |  |
| 129 | `CashEndPer` | 期末现金(元) | number(19,4) | ✓ | 99.95% | 期末现金(元)(CashEndPer)：优先取财报披露值，如财报未披露，期末现金=现金及现金等价物净增加额(含汇率影响)... |
| 130 | `CashABankBalances` | 现金及银行结余(元) | number(19,4) | ✓ | 11.39% |  |
| 131 | `BankDeposits` | 银行存款(元) | number(19,4) | ✓ | 1.88% |  |
| 132 | `InterestRecCB` | 收取利息-现金结存(元) | number(19,4) | ✓ | 0.19% |  |
| 133 | `InterestPaidCB` | 支付利息-现金结存(元) | number(19,4) | ✓ | 0.29% |  |
| 134 | `CashCashEquival` | 现金及现金等值项目结余(元) | number(19,4) | ✓ | 14.41% | 现金及现金等值项目结余的值如果财报没有披露，则以现金及银行结余+银行存款+（收取利息-现金结存）+（支付利息-现金结存）... |
| 135 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 136 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 137 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSource (信息来源代码)

信息来源代码(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IVALUE IN (1,3)，得到信息来源代码的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，27-配发结果，28-修改已刊发的财务报表及报告，29-修正重大错误而做出的前期调整，30-修订已刊发初步业绩的资料，32-内幕消息-年度报告，33-内幕消息-第一季报，34-内幕消息-第二季报，35-内幕消息-第三季报，36-内幕消息-第四季报，37-内幕消息-中期报告，38-内幕消息-申请版本，39-内幕消息-招股章程，40-内幕消息-聆讯后资料集，41-内幕消息-其他，99-其他。

### ReportType (报表类型)

报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年变更，如年度报告累计报告期是18或15个月，对应披露的12个月中期数据)、第五季报(企业发生财年变更，如年度报告累计报告期是18个月，对应披露的15个月中期数据)、年度报告、其他（企业披露的非标准报告期数据，如1、2、4、5等月，或者非完整累计月度报告数据）等。

### FiscalYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”。

### PeriodMark (日期标志)

日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM not in (90)，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，99-其他。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整。

### CompanyType (报表格式类型)

报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN (4,5)，得到报表格式类型的具体描述：1-普通，2-金融，3-保险，6-证券，7-信托。本表报表格式类型(CompanyNature)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，其中证券和信托因披露形式与一般类企业类似，但是又存在一定区别，所以单独分类展示。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，120-澳门会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则(2007)，521-中国会计准则(1993)。

### Gmark (聚源转换标识)

聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。

### IfComplete (完整标志)

完整标志(IfComplete)：1-完整；2-简表。

## SQL示例

```sql
-- 查询 港股现金流量表(香港会计准则) 数据
SELECT *
FROM hk_cashflowstatementhk
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
