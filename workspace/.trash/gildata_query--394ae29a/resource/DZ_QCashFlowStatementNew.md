# DZ_QCashFlowStatementNew

**中文名**: 单季现金流量表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_QCashFlowStatementNew` |
| MySQL表名 | `dz_qcashflowstatementnew` |
| 中文名 | 单季现金流量表_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务报表 |
| 更新频率 | 季更新 |
| 字段数量 | 154 |
| 版本 | 1.03 |

## 表描述

1.本表收录自公布季报以来上市、发债、非上市非发债公司的单季现金流量表情况，数据单位均为人民币元。
2.科目的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）。
3.由于会计期间可能发生同一控制下企业合并、企业自身错报漏报、企业列报项目变化等问题，将会导致二、四季度的单季数据的可靠性下降。
4.带“##”的特殊项目为单个公司披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
5.因简表数据原文披露不完整，且披露的数据量有限，通过简表计算的数据，不能真实反应企业单季度现金情况，所以不予以展示，本表展示完整标志（IfComplete）=1-完整的单季度数据。
6.因集团类企业涉及金融类业务，在财报中会披露金融类科目数据，所以本表在计算时，不区分金融/非金融字段，如定期报告中披露原始数据，则都计算单季度数据。
7.数据范围：2000-12-31至今
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
| 9 | `CompanyType` | 公司类别 | number(10) | ✓ | 100.0% | 公司类别(CompanyType)：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融... |
| 10 | `IfRecalculated` | 是否计算 | number(10) | ✓ | 100.0% | 是否计算(IfRecalculated)：1-是，0-否；其中：1-是（为依据本期和前一期计算的单季度数据），0-否（为... |
| 11 | `GoodsSaleServiceRenderCash` | 销售商品、提供劳务收到的现金(非金融类) | number(19,4) | ✓ | 94.14% |  |
| 12 | `TaxLevyRefund` | 收到的税费返还(非金融类) | number(19,4) | ✓ | 57.16% |  |
| 13 | `NetDecFinancialAsset` | 融出资金净减少额 | number(19,4) | ✓ | 0.3% |  |
| 14 | `NetDepositIncrease` | 客户存款和同业存放款项净增加额(金融类) | number(19,4) | ✓ | 3.17% |  |
| 15 | `NetBorrowingFromCentralBank` | 向中央银行借款净增加额(金融类) | number(19,4) | ✓ | 1.66% |  |
| 16 | `NetBorrowingFromFinanceCo` | 向其他金融机构拆入资金净增加额(金融类) | number(19,4) | ✓ | 1.79% |  |
| 17 | `NetDecLoanAndAdvance` | 客户贷款及垫款净减少额 | number(19,4) | ✓ | 0.15% |  |
| 18 | `NetDecreaseInCBAndIB` | 存放中央银行和同业款项净减少额 | number(19,4) | ✓ | 0.45% |  |
| 19 | `DrawBackLoansCanceled` | 收回已核销贷款(金融类) | number(19,4) | ✓ | 0.05% |  |
| 20 | `InterestAndCommissionCashIn` | 收取利息、手续费及佣金的现金(金融类) | number(19,4) | ✓ | 6.81% |  |
| 21 | `NetDealTradingAssets` | 处置交易性金融资产净增加额(金融类) | number(19,4) | ✓ | 1.39% |  |
| 22 | `NetBuyBack` | 回购业务资金净增加额(金融类) | number(19,4) | ✓ | 2.39% |  |
| 23 | `NetOriginalInsuranceCash` | 收到原保险合同保费取得的现金(金融类) | number(19,4) | ✓ | 1.31% |  |
| 24 | `NetReinsuranceCash` | 收到再保业务现金净额(金融类) | number(19,4) | ✓ | 0.97% |  |
| 25 | `NetInsurerDepositInvestment` | 保户储金及投资款净增加额(金融类) | number(19,4) | ✓ | 0.78% |  |
| 26 | `NetIncBorFunds` | 拆入资金净增加额 | number(19,4) | ✓ | 1.46% |  |
| 27 | `NetDecFundLending` | 拆出资金净减少额 | number(19,4) | ✓ | 0.19% |  |
| 28 | `NetDecCapResBusOper` | 返售业务资金净减少额(经营) | number(19,4) | ✓ | 0.29% |  |
| 29 | `NetCashRecInVTS` | 代理买卖证券收到的现金净额 | number(19,4) | ✓ | 0.9% |  |
| 30 | `NetCashRecAgeUTS` | 代理承销证券收到的现金净额 | number(19,4) | ✓ | 0.04% |  |
| 31 | `OtherCashInRelatedOperate` | 收到其他与经营活动有关的现金 | number(19,4) | ✓ | 99.52% |  |
| 32 | `SpecialItemsOCIF` | ##经营活动现金流入特殊项目 | number(19,4) | ✓ | 0.87% |  |
| 33 | `AdjustmentItemsOCIF` | ##经营活动现金流入调整项目 | number(19,4) | ✓ | 1.1% |  |
| 34 | `SubtotalOperateCashInflow` | 经营活动现金流入小计 | number(19,4) | ✓ | 99.96% |  |
| 35 | `GoodsServicesCashPaid` | 购买商品、接受劳务支付的现金(非金融类) | number(19,4) | ✓ | 92.74% |  |
| 36 | `BFLAFValOnPLChange` | 客户存款和同业存放款项净减少额 | number(19,4) | ✓ | 0.23% |  |
| 37 | `NetDecBorrowFromCB` | 向中央银行借款净减少额 | number(19,4) | ✓ | 0.25% |  |
| 38 | `NetDecBorFromFinanceCo` | 向其他金融机构拆入资金净减少额 | number(19,4) | ✓ | 0.14% |  |
| 39 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金 | number(19,4) | ✓ | 99.31% |  |
| 40 | `AllTaxesPaid` | 支付的各项税费 | number(19,4) | ✓ | 99.24% |  |
| 41 | `NetIncFinancialAsset` | 融出资金净增加额 | number(19,4) | ✓ | 0.42% |  |
| 42 | `NetLoanAndAdvanceIncrease` | 客户贷款及垫款净增加额(金融类) | number(19,4) | ✓ | 4.6% |  |
| 43 | `NetDepositInCBAndIB` | 存放中央银行和同业款项净增加额(金融类) | number(19,4) | ✓ | 3.05% |  |
| 44 | `NetLendCapital` | 拆出资金净增加额(金融类) | number(19,4) | ✓ | 0.79% |  |
| 45 | `CommissionCashPaid` | 支付手续费及佣金的现金(金融类) | number(19,4) | ✓ | 5.95% |  |
| 46 | `OriginalCompensationPaid` | 支付原保险合同赔付款项的现金(金融类) | number(19,4) | ✓ | 1.19% |  |
| 47 | `NetCashForReinsurance` | 支付再保业务现金净额(金融类) | number(19,4) | ✓ | 0.14% |  |
| 48 | `PolicyDividendCashPaid` | 支付保单红利的现金(金融类) | number(19,4) | ✓ | 0.83% |  |
| 49 | `NetDecBorrowingCapital` | 拆入资金净减少额 | number(19,4) | ✓ | 0.43% |  |
| 50 | `NetIncFinAssTraPurp` | 为交易目的而持有的金融资产净增加额 | number(19,4) | ✓ | 0.9% |  |
| 51 | `NetIncCapResBusOper` | 返售业务资金净增加额(经营) | number(19,4) | ✓ | 0.32% |  |
| 52 | `NetDecOfBuyBack` | 回购业务资金净减少额 | number(19,4) | ✓ | 0.56% |  |
| 53 | `NetCashPaidInVTS` | 代理买卖证券支付的现金净额 | number(19,4) | ✓ | 0.31% |  |
| 54 | `NetCashPayAgeUTS` | 代理承销证券支付的现金净额 | number(19,4) | ✓ | 0.02% |  |
| 55 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金 | number(19,4) | ✓ | 99.83% |  |
| 56 | `SpecialItemsOCOF` | ##经营活动现金流出特殊项目 | number(19,4) | ✓ | 0.93% |  |
| 57 | `AdjustmentItemsOCOF` | ##经营活动现金流出调整项目 | number(19,4) | ✓ | 1.8% |  |
| 58 | `SubtotalOperateCashOutflow` | 经营活动现金流出小计 | number(19,4) | ✓ | 99.99% |  |
| 59 | `AdjustmentItemsNOCF` | ##经营活动现金流量净额调整项目 | number(19,4) | ✓ | 1.29% |  |
| 60 | `NetOperateCashFlow` | 经营活动产生的现金流量净额 | number(19,4) | ✓ | 99.99% |  |
| 61 | `InvestWithdrawalCash` | 收回投资收到的现金 | number(19,4) | ✓ | 53.45% |  |
| 62 | `Investproceeds` | 取得投资收益收到的现金 | number(19,4) | ✓ | 66.69% |  |
| 63 | `FixIntanOtherAssetDispoCash` | 处置固定资产、无形资产和其他长期资产收回的现金净额 | number(19,4) | ✓ | 64.78% |  |
| 64 | `NetCashDealSubCompany` | 处置子公司及其他营业单位收到的现金净额 | number(19,4) | ✓ | 14.09% |  |
| 65 | `OtherCashFromInvestAct` | 收到其他与投资活动有关的现金 | number(19,4) | ✓ | 44.69% |  |
| 66 | `SpecialItemsICIF` | ##投资活动现金流入特殊项目 | number(19,4) | ✓ | 0.45% |  |
| 67 | `AdjustmentItemsICIF` | ##投资活动现金流入调整项目 | number(19,4) | ✓ | 0.54% |  |
| 68 | `SubtotalInvestCashInflow` | 投资活动现金流入小计 | number(19,4) | ✓ | 89.01% |  |
| 69 | `FixIntanOtherAssetAcquiCash` | 购建固定资产、无形资产和其他长期资产支付的现金 | number(19,4) | ✓ | 96.13% |  |
| 70 | `InvestCashPaid` | 投资支付的现金 | number(19,4) | ✓ | 69.42% |  |
| 71 | `NetCashFromSubCompany` | 取得子公司及其他营业单位支付的现金净额 | number(19,4) | ✓ | 15.59% |  |
| 72 | `ImpawnedLoanNetIncrease` | 质押贷款净增加额 | number(19,4) | ✓ | 0.99% |  |
| 73 | `NetIncCapResBusInv` | 返售业务资金净增加额(投资) | number(19,4) | ✓ | 0.07% |  |
| 74 | `OtherCashToInvestAct` | 支付其他与投资活动有关的现金 | number(19,4) | ✓ | 42.96% |  |
| 75 | `SpecialItemsICOF` | ##投资活动现金流出特殊项目 | number(19,4) | ✓ | 0.42% |  |
| 76 | `AdjustmentItemsICOF` | ##投资活动现金流出调整项目 | number(19,4) | ✓ | 0.51% |  |
| 77 | `SubtotalInvestCashOutflow` | 投资活动现金流出小计 | number(19,4) | ✓ | 98.18% |  |
| 78 | `AdjustmentItemsNICF` | ##投资活动现金流量净额调整项目 | number(19,4) | ✓ | 0.55% |  |
| 79 | `NetInvestCashFlow` | 投资活动产生的现金流量净额 | number(19,4) | ✓ | 98.85% |  |
| 80 | `CashFromInvest` | 吸收投资收到的现金 | number(19,4) | ✓ | 36.92% |  |
| 81 | `CashFromMinoSInvestSub` | 其中:子公司吸收少数股东投资收到的现金 | number(19,4) | ✓ | 8.58% |  |
| 82 | `CashFromBondsIssue` | 发行债券收到的现金 | number(19,4) | ✓ | 11.5% |  |
| 83 | `CashFromBorrowing` | 取得借款收到的现金 | number(19,4) | ✓ | 79.85% |  |
| 84 | `CashRecIssOthEquIns` | 发行其他权益工具收到的现金 | number(19,4) | ✓ | 0.08% |  |
| 85 | `NetBuyBackFin` | 回购业务资金净增加额(筹资) | number(19,4) | ✓ | 0.12% |  |
| 86 | `OtherFinanceActCash` | 收到其他与筹资活动有关的现金 | number(19,4) | ✓ | 48.44% |  |
| 87 | `SpecialItemsFCIF` | ##筹资活动现金流入特殊项目 | number(19,4) | ✓ | 0.24% |  |
| 88 | `AdjustmentItemsFCIF` | ##筹资活动现金流入调整项目 | number(19,4) | ✓ | 0.35% |  |
| 89 | `SubtotalFinanceCashInflow` | 筹资活动现金流入小计 | number(19,4) | ✓ | 88.36% |  |
| 90 | `BorrowingRepayment` | 偿还债务支付的现金 | number(19,4) | ✓ | 82.98% |  |
| 91 | `DividendInterestPayment` | 分配股利、利润或偿付利息支付的现金 | number(19,4) | ✓ | 93.09% |  |
| 92 | `ProceedsFromSubToMinoS` | 其中:子公司支付给少数股东的股利、利润或偿付的利息 | number(19,4) | ✓ | 7.64% |  |
| 93 | `NetDecBuyBackFin` | 回购业务资金净减少额(筹资) | number(19,4) | ✓ | 0.11% |  |
| 94 | `OtherFinanceActPayment` | 支付其他与筹资活动有关的现金 | number(19,4) | ✓ | 68.01% |  |
| 95 | `SpecialItemsFCOF` | ##筹资活动现金流出特殊项目 | number(19,4) | ✓ | 0.67% |  |
| 96 | `AdjustmentItemsFCOF` | ##筹资活动现金流出调整项目 | number(19,4) | ✓ | 0.76% |  |
| 97 | `SubtotalFinanceCashOutflow` | 筹资活动现金流出小计 | number(19,4) | ✓ | 96.09% |  |
| 98 | `AdjustmentItemsNFCF` | ##筹资活动流量现金净额调整项目 | number(19,4) | ✓ | 0.55% |  |
| 99 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额 | number(19,4) | ✓ | 96.84% |  |
| 100 | `ExchanRateChangeEffect` | 汇率变动对现金及现金等价物的影响 | number(19,4) | ✓ | 52.13% |  |
| 101 | `OtherItemsEffectingCE` | ##影响现金及现金等价物的其他科目 | number(19,4) | ✓ | 0.06% |  |
| 102 | `AdjustmentItemsCE` | ##影响现金及现金等价物的调整项目 | number(19,4) | ✓ | 1.82% |  |
| 103 | `CashEquivalentIncrease` | 现金及现金等价物净增加额 | number(19,4) | ✓ | 99.99% |  |
| 104 | `BeginPeriodCash` | 加:期初现金及现金等价物余额 | number(19,4) | ✓ | 95.16% |  |
| 105 | `OtherItemsEffectingCEI` | ##现金及现金等价物净增加额的特殊项目 | number(19,4) | ✓ | 0.02% |  |
| 106 | `AdjustmentItemsCEI` | ##现金及现金等价物净增加额的调整项目 | number(19,4) | ✓ | 12.9% |  |
| 107 | `EndPerCEqu` | 期末现金及现金等价物余额 | number(19,4) | ✓ | 95.77% |  |
| 108 | `NetProfit` | 净利润 | number(19,4) | ✓ | 5.61% |  |
| 109 | `NPParentCompanyOwners` | 其中:归属于母公司所有者的净利润 | number(19,4) | ✓ | 3.36% |  |
| 110 | `MinorityProfit` | 其中:少数股东损益 | number(19,4) | ✓ | 1.44% |  |
| 111 | `ADepreReserves` | 加:资产减值准备 | number(19,4) | ✓ | 4.05% |  |
| 112 | `FixedAssetDepreciation` | 固定资产折旧、油气资产折耗、生产性生物资产等资产折旧/摊销 | number(19,4) | ✓ | 5.59% |  |
| 113 | `UsufructAssetsDA` | 使用权资产摊销/折旧 | number(19,4) | ✓ | 0.26% |  |
| 114 | `InvestPropertyDA` | 投资性房地产折旧/摊销 | number(19,4) | ✓ | 0.07% |  |
| 115 | `IntAAmort` | 无形资产摊销 | number(19,4) | ✓ | 4.88% |  |
| 116 | `DeferredExpenseAmort` | 长期待摊费用摊销 | number(19,4) | ✓ | 3.7% |  |
| 117 | `DefExpDecd` | 待摊费用减少(减:增加) | number(19,4) | ✓ | 2.71% |  |
| 118 | `AccruedExpenseAdded` | 预提费用增加(减:减少) | number(19,4) | ✓ | 2.84% |  |
| 119 | `FixInOthADLoss` | 处置固定资产、无形资产和其他长期资产的损失 | number(19,4) | ✓ | 3.74% |  |
| 120 | `FixedAssetScrapLoss` | 固定资产报废损失 | number(19,4) | ✓ | 1.95% |  |
| 121 | `LFromFValueChg` | 公允价值变动损失 | number(19,4) | ✓ | 0.63% |  |
| 122 | `FinancialExpense` | 财务费用 | number(19,4) | ✓ | 5.34% |  |
| 123 | `InvestLoss` | 投资损失 | number(19,4) | ✓ | 4.57% |  |
| 124 | `InterestExpense` | 利息支出 | number(19,4) | ✓ | 0.05% |  |
| 125 | `IncResFunding` | 受限资金的增加 | number(19,4) | ✓ | 0.01% |  |
| 126 | `IncSpeReserves` | 专项储备增加 | number(19,4) | ✓ | 0.02% |  |
| 127 | `CreditImpairmentL` | 信用减值损失 | number(19,4) | ✓ | 0.5% |  |
| 128 | `DefProceedsAmo` | 递延收益的增加/(减少) | number(19,4) | ✓ | 0.05% |  |
| 129 | `IncEstLiability` | 预计负债的增加(减:减少) | number(19,4) | ✓ | 0.02% |  |
| 130 | `DeferredTaxCredit` | 递延税款贷项(减:借项) | number(19,4) | ✓ | 0.51% |  |
| 131 | `DefTaxAssetDec` | 递延所得税资产减少 | number(19,4) | ✓ | 1.55% |  |
| 132 | `DefTaxLiaInc` | 递延所得税负债增加 | number(19,4) | ✓ | 0.81% |  |
| 133 | `InventoryDecrease` | 存货的减少 | number(19,4) | ✓ | 5.26% |  |
| 134 | `OpeRecDec` | 经营性应收项目的减少 | number(19,4) | ✓ | 5.6% |  |
| 135 | `OperatePayableIncrease` | 经营性应付项目的增加 | number(19,4) | ✓ | 5.6% |  |
| 136 | `Others` | 其他 | number(19,4) | ✓ | 2.02% |  |
| 137 | `SpecialItemsNOCF1` | ##(附注)经营活动现金流量净额特殊项目 | number(19,4) | ✓ | 0.48% |  |
| 138 | `AdjustmentItemsNOCF1` | ##(附注)经营活动现金流量净额调整项目 | number(19,4) | ✓ | 0.31% |  |
| 139 | `NetOpeCFNotes` | (附注)经营活动产生的现金流量净额 | number(19,4) | ✓ | 5.61% |  |
| 140 | `ContrastAdjutmentNOCF` | ##加:经营流量净额前后对比调整项目 | number(19,4) | ✓ | 0.15% |  |
| 141 | `DebtToCaptical` | 债务转为资本 | number(19,4) | ✓ | 0.03% |  |
| 142 | `CBsExpiringWithin1Y` | 一年内到期的可转换公司债券 | number(19,4) | ✓ | 0.02% |  |
| 143 | `FixedAFinLeases` | 融资租入固定资产 | number(19,4) | ✓ | 0.04% |  |
| 144 | `CashAtEndOfYear` | 现金的期末余额 | number(19,4) | ✓ | 35.88% |  |
| 145 | `CashAtBeginningOfYear` | 减:现金的期初余额 | number(19,4) | ✓ | 17.41% |  |
| 146 | `CEquAtEOfYear` | 加:现金等价物的期末余额 | number(19,4) | ✓ | 1.82% |  |
| 147 | `CEquAtBeginning` | 减:现金等价物的期初余额 | number(19,4) | ✓ | 0.92% |  |
| 148 | `SpecialItemsC` | ##(附注)现金特殊项目 | number(19,4) | ✓ | 0.01% |  |
| 149 | `AdjustmentItemsC` | ##(附注)现金调整项目 | number(19,4) | ✓ | 0.82% |  |
| 150 | `NetIncrInCEqu` | (附注)现金及现金等价物净增加额 | number(19,4) | ✓ | 5.65% |  |
| 151 | `ContrastAdjutmentNC` | ##加:现金净额前后对比调整项目 | number(19,4) | ✓ | 0.12% |  |
| 152 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 153 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 154 | `JSID` | JSID | number(19) | ✗ |  |  |

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

### CompanyType (公司类别)

公司类别(CompanyType)：13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业。 本表企业性质(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业类别(CompanyType)。

### IfRecalculated (是否计算)

是否计算(IfRecalculated)：1-是，0-否；其中：1-是（为依据本期和前一期计算的单季度数据），0-否（为原文披露的单季度数据）

## SQL示例

```sql
-- 查询 单季现金流量表_新会计准则 数据
SELECT *
FROM dz_qcashflowstatementnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
