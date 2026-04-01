# LC_CashFlowStatementAll

**中文名**: 现金流量表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_CashFlowStatementAll` |
| MySQL表名 | `lc_cashflowstatementall` |
| 中文名 | 现金流量表_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 173 |
| 版本 | 1.07 |

## 表描述

1.反映企业依据2007年新会计准则在年报、中报、季报中披露的现金流量表数据；并依据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报表以及调整后的母公司报表。
3.若某个报告期的数据有多次调整，则该表展示历次调整数据。
4.该表中各财务科目的单位均为人民币元。
5.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
6.数据范围：1998-06-30至今
7.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 97.88% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 5 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and ... |
| 6 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM I... |
| 9 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 10 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志... |
| 11 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 12 | `EnterpriseType` | 报表格式类型 | number(10) | ✗ | 100.0% |  报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券... |
| 13 | `GoodsSaleServiceRenderCash` | 销售商品、提供劳务收到的现金 | number(19,4) | ✓ | 91.66% |  |
| 14 | `NetDepositIncrease` | 客户存款和同业存放款项净增加额 | number(19,4) | ✓ | 3.28% | 客户存款和同业存放款项净增加额（NetDepositIncrease）：一般为金融类:银行企业披露科目 |
| 15 | `NetBorrowingFromCentralBank` | 向中央银行借款净增加额 | number(19,4) | ✓ | 1.72% | 	 向中央银行借款净增加额（NetBorrowingFromCentralBank）：一般为金融类:银行企业披露科目 |
| 16 | `NetBorrowingFromFinanceCo` | 向其他金融机构拆入资金净增加额 | number(19,4) | ✓ | 1.63% | 向其他金融机构拆入资金净增加额（NetBorrowingFromFinanceCo）：一般为金融类:银行企业披露科目 |
| 17 | `NetDecLoanAndAdvance` | 客户贷款及垫款净减少额 | number(19,4) | ✓ | 0.15% | 客户贷款及垫款净减少额（NetDecLoanAndAdvance）：一般为金融类:银行企业披露科目 |
| 18 | `NetDecreaseInCBAndIB` | 存放中央银行和同业款项净减少额 | number(19,4) | ✓ | 0.53% | 存放中央银行和同业款项净减少额（NetDecreaseInCBAndIB）：一般为金融类:银行企业披露科目 |
| 19 | `NetOriginalInsuranceCash` | 收到原保险合同保费取得的现金 | number(19,4) | ✓ | 1.18% | 收到原保险合同保费取得的现金（NetOriginalInsuranceCash）：一般为金融类:保险公司披露科目 |
| 20 | `NetReinsuranceCash` | 收到再保业务现金净额 | number(19,4) | ✓ | 0.71% | 收到再保业务现金净额（NetReinsuranceCash）：一般为金融类:保险公司披露科目 |
| 21 | `NetInsurerDepositInvestment` | 保户储金及投资款净增加额 | number(19,4) | ✓ | 0.56% | 保户储金及投资款净增加额（NetInsurerDepositInvestment）：一般为金融类:保险公司披露科目 |
| 22 | `NetIncBorFunds` | 拆入资金净增加额 | number(19,4) | ✓ | 1.19% | 拆入资金净增加额（NetIncBorFunds）：一般为金融类企业披露科目 |
| 23 | `NetDecFundLending` | 拆出资金净减少额 | number(19,4) | ✓ | 0.21% | 拆出资金净减少额（NetDecFundLending）：一般为金融类企业披露科目 |
| 24 | `NetDecCapResBusOper` | 返售业务资金净减少额(经营) | number(19,4) | ✓ | 0.3% | 返售业务资金净减少额(经营)（NetDecCapResBusOper）：一般为金融类企业披露科目 |
| 25 | `NetBuyBack` | 回购业务资金净增加额 | number(19,4) | ✓ | 2.12% | 回购业务资金净增加额（NetBuyBack）：一般为金融类企业披露科目 |
| 26 | `NetCashRecInVTS` | 代理买卖证券收到的现金净额 | number(19,4) | ✓ | 0.8% | 代理买卖证券收到的现金净额（NetCashRecInVTS）：一般为金融类:证券公司披露科目 |
| 27 | `NetCashRecAgeUTS` | 代理承销证券收到的现金净额 | number(19,4) | ✓ | 0.04% | 代理承销证券收到的现金净额（NetCashRecAgeUTS）：一般为金融类:证券公司披露科目 |
| 28 | `NetDealTradingAssets` | 处置交易性金融资产净增加额 | number(19,4) | ✓ | 0.99% |  |
| 29 | `NetDecFinAssTraPurp` | 为交易目的而持有的金融资产净减少额 | number(19,4) | ✓ | 0.21% |  |
| 30 | `NetIncFinLiaTraPurp` | 为交易目的而持有的金融负债净增加额 | number(19,4) | ✓ | 0.08% |  |
| 31 | `InterestAndCommissionCashIn` | 收取利息、手续费及佣金的现金 | number(19,4) | ✓ | 6.96% |  |
| 32 | `TaxLevyRefund` | 收到的税费返还 | number(19,4) | ✓ | 50.73% |  |
| 33 | `DrawBackLoansCanceled` | 收回已核销贷款 | number(19,4) | ✓ | 0.06% |  |
| 34 | `NetDecFinancialAsset` | 融出资金净减少额 | number(19,4) | ✓ | 0.28% | 融出资金净减少额（NetDecFinancialAsset）：一般为金融类企业披露科目 |
| 35 | `OtherCashInRelatedOperate` | 收到其他与经营活动有关的现金 | number(19,4) | ✓ | 98.77% |  |
| 36 | `SpecialItemsOCIF` | ##经营活动现金流入特殊项目 | number(19,4) | ✓ | 1.1% |  |
| 37 | `AdjustmentItemsOCIF` | ##经营活动现金流入调整项目 | number(19,4) | ✓ | 0.79% |  |
| 38 | `SubtotalOperateCashInflow` | 经营活动现金流入小计 | number(19,4) | ✓ | 99.37% |  |
| 39 | `GoodsServicesCashPaid` | 购买商品、接受劳务支付的现金 | number(19,4) | ✓ | 90.14% |  |
| 40 | `BFLAFValOnPLChange` | 客户存款和同业存放款项净减少额 | number(19,4) | ✓ | 0.23% | 客户存款和同业存放款项净减少额（BFLAFValOnPLChange）：一般为金融类:银行企业披露科目 |
| 41 | `NetDecBorrowFromCB` | 向中央银行借款净减少额 | number(19,4) | ✓ | 0.27% | 向中央银行借款净减少额（NetDecBorrowFromCB）：一般为金融类:银行企业披露科目 |
| 42 | `NetDecBorFromFinanceCo` | 向其他金融机构拆入资金净减少额 | number(19,4) | ✓ | 0.16% | 向其他金融机构拆入资金净减少额（NetDecBorFromFinanceCo）：一般为金融类:银行企业披露科目 |
| 43 | `NetLoanAndAdvanceIncrease` | 客户贷款及垫款净增加额 | number(19,4) | ✓ | 4.51% | 客户贷款及垫款净增加额（NetLoanAndAdvanceIncrease）：一般为金融类:银行企业披露科目 |
| 44 | `NetDepositInCBAndIB` | 存放中央银行和同业款项净增加额 | number(19,4) | ✓ | 3.04% | 存放中央银行和同业款项净增加额（NetDepositInCBAndIB）：一般为金融类:银行企业披露科目 |
| 45 | `OriginalCompensationPaid` | 支付原保险合同赔付款项的现金 | number(19,4) | ✓ | 1.07% | 支付原保险合同赔付款项的现金（OriginalCompensationPaid）：一般为金融类:保险公司披露科目 |
| 46 | `PolicyDividendCashPaid` | 支付保单红利的现金 | number(19,4) | ✓ | 0.6% | 支付保单红利的现金（PolicyDividendCashPaid）：一般为金融类:保险公司披露科目 |
| 47 | `NetCashForReinsurance` | 支付再保业务现金净额 | number(19,4) | ✓ | 0.28% | 支付再保业务现金净额（NetCashForReinsurance）：一般为金融类:保险公司披露科目 |
| 48 | `NetIncPledgedPolicyLoan` | 保单质押贷款净增加额 | number(19,4) | ✓ | 0.01% |  |
| 49 | `NetDecInsurDPSTInvest` | 保户储金及投资款净减少额 | number(19,4) | ✓ | 0.07% | 保户储金及投资款净减少额（NetDecInsurDPSTInvest）：一般为金融类:保险公司披露科目 |
| 50 | `NetDecBorrowingCapital` | 拆入资金净减少额 | number(19,4) | ✓ | 0.4% | 拆入资金净减少额（NetDecBorrowingCapital）：一般为金融类企业披露科目 |
| 51 | `NetLendCapital` | 拆出资金净增加额 | number(19,4) | ✓ | 0.78% | 拆出资金净增加额（NetLendCapital）：一般为金融类企业披露科目 |
| 52 | `NetIncCapResBusOper` | 返售业务资金净增加额(经营) | number(19,4) | ✓ | 0.34% | 返售业务资金净增加额(经营)（NetIncCapResBusOper）：一般为金融类企业披露科目 |
| 53 | `NetDecOfBuyBack` | 回购业务资金净减少额 | number(19,4) | ✓ | 0.6% | 回购业务资金净减少额（NetDecOfBuyBack）：一般为金融类企业披露科目 |
| 54 | `NetCashPaidInVTS` | 代理买卖证券支付的现金净额 | number(19,4) | ✓ | 0.38% | 代理买卖证券支付的现金净额（NetCashPaidInVTS）：一般为金融类:证券公司披露科目 |
| 55 | `NetCashPayAgeUTS` | 代理承销证券支付的现金净额 | number(19,4) | ✓ | 0.02% | 代理承销证券支付的现金净额（NetCashPayAgeUTS）：一般为金融类:证券公司披露科目 |
| 56 | `NetDecDealTradeAssets` | 处置交易性金融资产净减少额 | number(19,4) | ✓ | 0.42% |  |
| 57 | `NetIncFinAssTraPurp` | 为交易目的而持有的金融资产净增加额 | number(19,4) | ✓ | 0.55% |  |
| 58 | `NetDecFinLiaTraPurp` | 为交易目的而持有的金融负债净减少额 | number(19,4) | ✓ | 0.07% |  |
| 59 | `CommissionCashPaid` | 支付利息、手续费及佣金的现金 | number(19,4) | ✓ | 6.45% |  |
| 60 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金 | number(19,4) | ✓ | 98.14% |  |
| 61 | `AllTaxesPaid` | 支付的各项税费 | number(19,4) | ✓ | 98.15% |  |
| 62 | `OpeAndAdmExpForCash` | 以现金支付的业务及管理费 | number(19,4) | ✓ | 0.07% |  |
| 63 | `NetIncFinancialAsset` | 融出资金净增加额 | number(19,4) | ✓ | 0.47% | 融出资金净增加额（NetIncFinancialAsset）：一般为金融类企业披露科目 |
| 64 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金 | number(19,4) | ✓ | 99.15% |  |
| 65 | `SpecialItemsOCOF` | ##经营活动现金流出特殊项目 | number(19,4) | ✓ | 1.13% |  |
| 66 | `AdjustmentItemsOCOF` | ##经营活动现金流出调整项目 | number(19,4) | ✓ | 1.3% |  |
| 67 | `SubtotalOperateCashOutflow` | 经营活动现金流出小计 | number(19,4) | ✓ | 99.4% |  |
| 68 | `AdjustmentItemsNOCF` | ##经营活动现金流量净额调整项目 | number(19,4) | ✓ | 0.88% |  |
| 69 | `NetOperateCashFlow` | 经营活动产生的现金流量净额 | number(19,4) | ✓ | 99.97% |  |
| 70 | `InvestWithdrawalCash` | 收回投资收到的现金 | number(19,4) | ✓ | 49.36% |  |
| 71 | `Investproceeds` | 取得投资收益收到的现金 | number(19,4) | ✓ | 62.87% |  |
| 72 | `FixIntanOtherAssetDispoCash` | 处置固定资产、无形资产和其他长期资产收回的现金净额 | number(19,4) | ✓ | 60.21% |  |
| 73 | `NetCashDealSubCompany` | 处置子公司及其他营业单位收到的现金净额 | number(19,4) | ✓ | 10.88% |  |
| 74 | `OtherCashFromInvestAct` | 收到其他与投资活动有关的现金 | number(19,4) | ✓ | 39.44% |  |
| 75 | `SpecialItemsICIF` | ##投资活动现金流入特殊项目 | number(19,4) | ✓ | 0.43% |  |
| 76 | `AdjustmentItemsICIF` | ##投资活动现金流入调整项目 | number(19,4) | ✓ | 0.38% |  |
| 77 | `SubtotalInvestCashInflow` | 投资活动现金流入小计 | number(19,4) | ✓ | 86.24% |  |
| 78 | `FixIntanOtherAssetAcquiCash` | 购建固定资产、无形资产和其他长期资产支付的现金 | number(19,4) | ✓ | 94.79% |  |
| 79 | `InvestCashPaid` | 投资支付的现金 | number(19,4) | ✓ | 66.0% |  |
| 80 | `ImpawnedLoanNetIncrease` | 质押贷款净增加额 | number(19,4) | ✓ | 0.68% |  |
| 81 | `NetCashFromSubCompany` | 取得子公司及其他营业单位支付的现金净额 | number(19,4) | ✓ | 12.16% |  |
| 82 | `NetIncCapResBusInv` | 返售业务资金净增加额(投资) | number(19,4) | ✓ | 0.07% |  |
| 83 | `OtherCashToInvestAct` | 支付其他与投资活动有关的现金 | number(19,4) | ✓ | 36.9% |  |
| 84 | `SpecialItemsICOF` | ##投资活动现金流出特殊项目 | number(19,4) | ✓ | 0.37% |  |
| 85 | `AdjustmentItemsICOF` | ##投资活动现金流出调整项目 | number(19,4) | ✓ | 0.35% |  |
| 86 | `SubtotalInvestCashOutflow` | 投资活动现金流出小计 | number(19,4) | ✓ | 97.18% |  |
| 87 | `AdjustmentItemsNICF` | ##投资活动现金流量净额调整项目 | number(19,4) | ✓ | 0.44% |  |
| 88 | `NetInvestCashFlow` | 投资活动产生的现金流量净额 | number(19,4) | ✓ | 98.35% |  |
| 89 | `CashFromInvest` | 吸收投资收到的现金 | number(19,4) | ✓ | 35.13% |  |
| 90 | `CashFromMinoSInvestSub` | 其中:子公司吸收少数股东投资收到的现金 | number(19,4) | ✓ | 11.99% |  |
| 91 | `CashFromBorrowing` | 取得借款收到的现金 | number(19,4) | ✓ | 77.4% |  |
| 92 | `CashFromBondsIssue` | 发行债券收到的现金 | number(19,4) | ✓ | 9.56% |  |
| 93 | `CashRecIssOthEquIns` | 发行其他权益工具收到的现金 | number(19,4) | ✓ | 0.07% |  |
| 94 | `NetBuyBackFin` | 回购业务资金净增加额(筹资) | number(19,4) | ✓ | 0.17% |  |
| 95 | `OtherFinanceActCash` | 收到其他与筹资活动有关的现金 | number(19,4) | ✓ | 44.1% |  |
| 96 | `SpecialItemsFCIF` | ##筹资活动现金流入特殊项目 | number(19,4) | ✓ | 0.21% |  |
| 97 | `AdjustmentItemsFCIF` | ##筹资活动现金流入调整项目 | number(19,4) | ✓ | 0.19% |  |
| 98 | `SubtotalFinanceCashInflow` | 筹资活动现金流入小计 | number(19,4) | ✓ | 87.09% |  |
| 99 | `BorrowingRepayment` | 偿还债务支付的现金 | number(19,4) | ✓ | 81.17% |  |
| 100 | `DividendInterestPayment` | 分配股利、利润或偿付利息支付的现金 | number(19,4) | ✓ | 91.87% |  |
| 101 | `ProceedsFromSubToMinoS` | 其中:子公司支付给少数股东的股利、利润或偿付的利息 | number(19,4) | ✓ | 10.74% |  |
| 102 | `NetDecBuyBackFin` | 回购业务资金净减少额(筹资) | number(19,4) | ✓ | 0.14% | 回购业务资金净减少额(筹资)（NetDecBuyBackFin）：一般为金融类企业披露科目 |
| 103 | `OtherFinanceActPayment` | 支付其他与筹资活动有关的现金 | number(19,4) | ✓ | 63.12% |  |
| 104 | `SpecialItemsFCOF` | ##筹资活动现金流出特殊项目 | number(19,4) | ✓ | 0.8% |  |
| 105 | `AdjustmentItemsFCOF` | ##筹资活动现金流出调整项目 | number(19,4) | ✓ | 0.49% |  |
| 106 | `SubtotalFinanceCashOutflow` | 筹资活动现金流出小计 | number(19,4) | ✓ | 95.19% |  |
| 107 | `AdjustmentItemsNFCF` | ##筹资活动流量现金净额调整项目 | number(19,4) | ✓ | 0.35% |  |
| 108 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额 | number(19,4) | ✓ | 96.65% |  |
| 109 | `ExchanRateChangeEffect` | 汇率变动对现金及现金等价物的影响 | number(19,4) | ✓ | 47.27% |  |
| 110 | `OtherItemsEffectingCE` | ##影响现金及现金等价物的其他科目 | number(19,4) | ✓ | 0.04% |  |
| 111 | `AdjustmentItemsCE` | ##影响现金及现金等价物的调整项目 | number(19,4) | ✓ | 1.22% |  |
| 112 | `CashEquivalentIncrease` | 现金及现金等价物净增加额 | number(19,4) | ✓ | 99.57% |  |
| 113 | `BeginPeriodCash` | 加:期初现金及现金等价物余额 | number(19,4) | ✓ | 94.22% |  |
| 114 | `OtherItemsEffectingCEI` | ##现金及现金等价物净增加额的特殊项目 | number(19,4) | ✓ | 0.01% |  |
| 115 | `AdjustmentItemsCEI` | ##现金及现金等价物净增加额的调整项目 | number(19,4) | ✓ | 0.7% |  |
| 116 | `EndPeriodCashEquivalent` | 期末现金及现金等价物余额 | number(19,4) | ✓ | 94.53% |  |
| 117 | `NetProfit` | 净利润 | number(19,4) | ✓ | 39.05% |  |
| 118 | `NPParentCompanyOwners` | 其中:归属于母公司所有者的净利润 | number(19,4) | ✓ | 4.36% |  |
| 119 | `MinorityProfit` | 其中:少数股东损益 | number(19,4) | ✓ | 2.07% |  |
| 120 | `AssetsDepreciationReserves` | 加:资产减值准备 | number(19,4) | ✓ | 32.44% |  |
| 121 | `FixedAssetDepreciation` | 固定资产折旧、油气资产折耗、生产性生物资产等资产折旧/摊销 | number(19,4) | ✓ | 38.73% |  |
| 122 | `ProductBioAssetsDep` | 其中:生产性生物资产折旧 | number(19,4) | ✓ | 0.02% |  |
| 123 | `InvestPropertyDA` | 投资性房地产折旧/摊销 | number(19,4) | ✓ | 0.87% |  |
| 124 | `UsufructAssetsDA` | 使用权资产摊销/折旧 | number(19,4) | ✓ | 5.77% |  |
| 125 | `IntangibleAssetAmortization` | 无形资产摊销 | number(19,4) | ✓ | 35.65% |  |
| 126 | `DeferredExpenseAmort` | 长期待摊费用摊销 | number(19,4) | ✓ | 27.98% |  |
| 127 | `DeferredExpenseDecreased` | 待摊费用减少(减:增加) | number(19,4) | ✓ | 2.9% |  |
| 128 | `AccruedExpenseAdded` | 预提费用增加(减:减少) | number(19,4) | ✓ | 2.83% |  |
| 129 | `FixIntanOtherAssetDispoLoss` | 处置固定资产、无形资产和其他长期资产的损失 | number(19,4) | ✓ | 28.11% |  |
| 130 | `FixedAssetScrapLoss` | 固定资产报废损失 | number(19,4) | ✓ | 14.92% |  |
| 131 | `LossFromFairValueChanges` | 公允价值变动损失 | number(19,4) | ✓ | 13.07% |  |
| 132 | `FinancialExpense` | 财务费用 | number(19,4) | ✓ | 34.77% |  |
| 133 | `InterestIncome` | 利息收入 | number(19,4) | ✓ | 0.4% |  |
| 134 | `InterestExpense` | 利息支出 | number(19,4) | ✓ | 1.03% |  |
| 135 | `LeaseLiaIntExp` | 其中:租赁负债利息支出 | number(19,4) | ✓ | 0.17% |  |
| 136 | `BondIssueExpense` | 其中:发行债券利息支出 | number(19,4) | ✓ | 0.34% |  |
| 137 | `ExchangeLoss` | 汇兑损失(收益以"-"号填列) | number(19,4) | ✓ | 0.84% |  |
| 138 | `InvestLoss` | 投资损失 | number(19,4) | ✓ | 32.04% |  |
| 139 | `IncResFunding` | 受限资金的增加 | number(19,4) | ✓ | 0.15% |  |
| 140 | `IncSpeReserves` | 专项储备增加 | number(19,4) | ✓ | 0.15% |  |
| 141 | `CreditImpairmentL` | 信用减值损失 | number(19,4) | ✓ | 7.7% |  |
| 142 | `DefProceedsAmo` | 递延收益的增加/(减少) | number(19,4) | ✓ | 0.32% |  |
| 143 | `IncEstLiability` | 预计负债的增加(减:减少) | number(19,4) | ✓ | 0.1% |  |
| 144 | `DeferredTaxCredit` | 递延税款贷项(减:借项) | number(19,4) | ✓ | 0.59% |  |
| 145 | `DeferedTaxAssetDecrease` | 递延所得税资产减少 | number(19,4) | ✓ | 29.27% |  |
| 146 | `DeferedTaxLiabilityIncrease` | 递延所得税负债增加 | number(19,4) | ✓ | 15.93% |  |
| 147 | `InventoryDecrease` | 存货的减少 | number(19,4) | ✓ | 34.91% |  |
| 148 | `SharePayment` | 股份支付费用 | number(19,4) | ✓ | 0.2% |  |
| 149 | `DecreaseTradeAssets` | 交易性金融资产的减少 | number(19,4) | ✓ | 0.24% |  |
| 150 | `DecAvailableSaleAssets` | 可供出售金融资产的减少 | number(19,4) | ✓ | 0.06% |  |
| 151 | `DecreaseLoan` | 贷款的减少 | number(19,4) | ✓ | 0.1% |  |
| 152 | `OperateReceivableDecrease` | 经营性应收项目的减少 | number(19,4) | ✓ | 38.98% |  |
| 153 | `OperatePayableIncrease` | 经营性应付项目的增加 | number(19,4) | ✓ | 38.99% |  |
| 154 | `Others` | 其他 | number(19,4) | ✓ | 10.5% |  |
| 155 | `SpecialItemsNOCF1` | ##(附注)经营活动现金流量净额特殊项目 | number(19,4) | ✓ | 1.98% |  |
| 156 | `AdjustmentItemsNOCF1` | ##(附注)经营活动现金流量净额调整项目 | number(19,4) | ✓ | 1.34% |  |
| 157 | `NetOperateCashFlowNotes` | (附注)经营活动产生的现金流量净额 | number(19,4) | ✓ | 39.07% |  |
| 158 | `ContrastAdjutmentNOCF` | ##加:经营流量净额前后对比调整项目 | number(19,4) | ✓ | 0.95% |  |
| 159 | `DebtToCaptical` | 债务转为资本 | number(19,4) | ✓ | 0.37% |  |
| 160 | `CBsExpiringWithin1Y` | 一年内到期的可转换公司债券 | number(19,4) | ✓ | 0.23% |  |
| 161 | `FixedAssetsFinanceLeases` | 融资租入固定资产 | number(19,4) | ✓ | 0.71% |  |
| 162 | `CashAtEndOfYear` | 现金的期末余额 | number(19,4) | ✓ | 37.79% |  |
| 163 | `CashAtBeginningOfYear` | 减:现金的期初余额 | number(19,4) | ✓ | 37.7% |  |
| 164 | `CashEquivalentsAtEndOfYear` | 加:现金等价物的期末余额 | number(19,4) | ✓ | 2.01% |  |
| 165 | `CashEquivalentsAtBeginning` | 减:现金等价物的期初余额 | number(19,4) | ✓ | 2.0% |  |
| 166 | `SpecialItemsC` | ##(附注)现金特殊项目 | number(19,4) | ✓ | 0.05% |  |
| 167 | `AdjustmentItemsC` | ##(附注)现金调整项目 | number(19,4) | ✓ | 0.2% |  |
| 168 | `NetIncrInCashAndEquivalents` | (附注)现金及现金等价物净增加额 | number(19,4) | ✓ | 37.99% |  |
| 169 | `ContrastAdjutmentNC` | ##加:现金净额前后对比调整项目 | number(19,4) | ✓ | 0.52% |  |
| 170 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 3.27% |  |
| 171 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 172 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 173 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM NOT IN (110106,110107,110108,110109,110110,110111,110203,110204,110205,120109,120110,120204,120208,120210,120216,120217,130108,130110,130112,130113,140108,140109,150104)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，110201-定期报告:年度报告(关联方)，110202-定期报告:半年度报告(关联方)，120101-临时公告:审计报告(更正后)，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)，120106-临时公告:公开转让说明书(更正后)，120107-临时公告:业绩快报，120108-临时公告:业绩快报(更正后)，120201-临时公告:跟踪评级报告，120202-临时公告:同业存单发行计划，120203-临时公告:比较式财务报表，120205-临时公告:其他，120206-临时公告:前期差错更正，120207-临时公告:第一季度报告，120209-临时公告:第三季度报告，120211-临时公告：年度报告，120212-临时公告：半年度报告，120213-临时公告:受托管理人事务报告，120214-临时公告:资产评估报告，120215-临时公告:资产管理报告，120218-临时公告：主要经营业绩，130101-发行上市书:募集说明书，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130105-发行上市书:审阅报告，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130109-发行上市书:审计报告，130111-发行上市书:其他，140101-发行披露文件:第一季报，140102-发行披露文件:半年度报告，140103-发行披露文件:第三季报，140104-发行披露文件:审计报告，140105-发行披露文件:募集说明书，140106-发行披露文件:跟踪评级报告，140107-发行披露文件:年度报告，140110-发行披露文件:转让服务公告书，140111-发行披露文件:备案登记表，140112-发行披露文件:初始信息披露，150101-发债定期报告:第一季报，150102-发债定期报告:半年度报告，150103-发债定期报告:第三季报，150105-发债:其他报告。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfMerged (是否合并)

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,4,5)，得到是否调整的具体描述：1-是，2-否，4-否(7-9月)，5-是(7-9月)。

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### EnterpriseType (报表格式类型)


报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业)。 本表报表格式类型(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业性质(CompanyType)。
本表企业性质(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业类别(CompanyType)。

### NetDepositIncrease (客户存款和同业存放款项净增加额)

客户存款和同业存放款项净增加额（NetDepositIncrease）：一般为金融类:银行企业披露科目

### NetBorrowingFromCentralBank (向中央银行借款净增加额)

	
向中央银行借款净增加额（NetBorrowingFromCentralBank）：一般为金融类:银行企业披露科目

## SQL示例

```sql
-- 查询 现金流量表_新会计准则 数据
SELECT *
FROM lc_cashflowstatementall
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
