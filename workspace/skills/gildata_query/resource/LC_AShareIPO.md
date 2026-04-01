# LC_AShareIPO

**中文名**: A股发行与上市

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AShareIPO` |
| MySQL表名 | `lc_ashareipo` |
| 中文名 | A股发行与上市 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 285 |
| 版本 | 1.13 |

## 表描述

1.该表包括A股首次发行上市的明细情况。
2.中文名称带*的，表示该字段表述的信息当前已不再披露。
3.2016年1月1日起实行新股发行与上市新规。新规实行前，新股发行的招股说明书发布日期与发行公告日为同一天，新规实行后，出现不同日期的情况。
4.数据范围：1990-12-10至今
5.信息来源：招股意向书、招股说明书、上市公告书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `IntentLetterPublDate` | 招股公告日(招股意向书发布日期) | date | ✓ | 61.96% |  |
| 5 | `IntentLetterSignDate` | 招股意向书签署日期 | date | ✓ | 60.61% |  |
| 6 | `ProspectusPublDate` | 招股说明书发布日期 | date | ✓ | 96.69% |  |
| 7 | `ProspectusSignDate` | 招股说明书签署日期 | date | ✓ | 82.97% |  |
| 8 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 99.87% |  |
| 9 | `IssuePublDate` | 发行公告日 | date | ✓ | 91.51% |  |
| 10 | `IssueStartDate` | 发行日期上限 | date | ✓ | 99.56% |  |
| 11 | `IssueEndDate` | 发行日期下限 | date | ✓ | 99.56% |  |
| 12 | `OnlineStartDate` | 网上申购日期上限 | date | ✓ | 97.98% |  |
| 13 | `OnlineEndDate` | 网上申购日期下限 | date | ✓ | 97.96% |  |
| 14 | `RefundmentDate_Online` | 网上申购资金解冻日 | date | ✓ | 34.31% |  |
| 15 | `PayDateOnline` | 网上申购缴款日期 | date | ✓ | 48.18% |  |
| 16 | `BookingStartDateLP` | 网下申购日期上限 | date | ✓ | 61.71% |  |
| 17 | `BookingEndDateLP` | 网下申购日期下限 | date | ✓ | 61.73% |  |
| 18 | `RefundmentDate_Offline` | 网下申购资金退款日 | date | ✓ | 29.65% |  |
| 19 | `PayDateOffline` | 网下申购缴款日期 | date | ✓ | 60.77% |  |
| 20 | `IssueResultPublDate` | 中签率公告日 | date | ✓ | 89.36% |  |
| 21 | `ResultPulbDate` | 发行结果公告日 | date | ✓ | 43.78% |  |
| 22 | `PayStartDateLP` | *法人配售缴款期上限 | date | ✓ | 1.5% |  |
| 23 | `PayEndDateLP` | *法人配售缴款期下限 | date | ✓ | 1.56% |  |
| 24 | `ApplyStartDateF` | *基金优先配售申购日期上限 | date | ✓ | 0.17% |  |
| 25 | `ApplyEndDateF` | *基金优先配售申购日期下限 | date | ✓ | 0.19% |  |
| 26 | `PayStartDateF` | *基金优先配售缴款期下限 | date | ✓ | 0.06% |  |
| 27 | `PayEndDateF` | *基金优先配售缴款期上限 | date | ✓ | 0.04% |  |
| 28 | `SecMarketPlacingDate` | *二级市场配售日期 | date | ✓ | 5.06% |  |
| 29 | `PayStartDateSM` | *二级市场配售缴款日上限 | date | ✓ | 4.56% |  |
| 30 | `PayEndDateSM` | *二级市场配售缴款日下限 | date | ✓ | 4.56% |  |
| 31 | `ProposedListDate` | 预计上市日期 | date | ✓ | 4.39% |  |
| 32 | `ListAnnouncementDate` | 上市公告日(上市公告书发布日期) | date | ✓ | 99.42% |  |
| 33 | `ListDate` | 上市日期 | date | ✓ | 99.62% |  |
| 34 | `ListStandard` | 上市标准 | number(10) | ✓ | 18.88% | 上市标准(ListStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 2206 AND ... |
| 35 | `OffLineLockPeriod` | 网下配售股票锁定期(月) | number(10) | ✓ | 60.79% |  |
| 36 | `OffLineLockArrange` | 网下配售锁定期安排 | number(10) | ✓ | 18.72% | 网下配售锁定期安排(OffLineLockArrange)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 37 | `NormalLegalPersonShareLD` | 向一般法人配售首次上市日期 | date | ✓ | 63.54% |  |
| 38 | `StrategicInvestorShareLD` | 向战略投资者配售首次上市日期 | date | ✓ | 11.06% |  |
| 39 | `StaffSharesListDate` | *内部职工股上市日期 | date | ✓ | 3.19% |  |
| 40 | `StaffSharesListTerm` | *内部职工股上市期限(年) | number(9,4) | ✓ | 7.79% |  |
| 41 | `IssueMethod` | 发行方式 | number(10) | ✓ |  |  |
| 42 | `RaisingMethod` | 募资方式 | number(10) | ✓ | 100.0% | 募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND... |
| 43 | `StockType` | 发行股票类型 | number(10) | ✓ | 100.0% | 发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND D... |
| 44 | `PricingModel` | 发行价定价方式 | number(10) | ✓ |  |  |
| 45 | `RationModel` | 发行量定量方式 | number(10) | ✓ |  |  |
| 46 | `IssueObject` | 发行对象 | varchar2(255) | ✓ | 99.58% |  |
| 47 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 98.85% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，... |
| 48 | `LeadUnderwriter` | 主承销商 | varchar2(500) | ✓ | 97.9% |  |
| 49 | `ColeadUnderwriter` | 副主承销商 | varchar2(500) | ✓ | 21.03% |  |
| 50 | `ListingSponsor` | 上市推荐人 | varchar2(500) | ✓ | 98.08% |  |
| 51 | `Distributor` | 分销商 | varchar2(2000) | ✓ | 28.36% |  |
| 52 | `UnderwritingSignDate` | *承销协议签署日 | date | ✓ | 0.0% |  |
| 53 | `UnderwritingStartDate` | *承销期上限 | date | ✓ | 12.56% |  |
| 54 | `UnderwritingEndDate` | *承销期下限 | date | ✓ | 12.56% |  |
| 55 | `IssuePriceCeiling` | 发行价上限(最高价)(元) | number(19,4) | ✓ | 74.31% |  |
| 56 | `IssuePriceFloor` | 发行价下限(最低价)(元) | number(19,4) | ✓ | 74.68% |  |
| 57 | `EstiIssuePrice` | 预估发行价(元) | number(19,4) | ✓ | 58.11% | 预估发行价(元)(EstiIssuePrice)：新股发行拟募集资金总额/ 发行量上限（不多于） |
| 58 | `EstiApMaxOnline` | 预估上网发行申购上限(最多)(股)(份) | number(16,0) | ✓ | 72.68% | 预估上网发行申购上限(最多股)(EstiApMaxOnline)=网上发行计划（万股）/ 1000 取整（沪市主板）；网... |
| 59 | `IssueVolCeiling` | 发行量上限(不多于)(股)(份) | number(16,0) | ✓ | 92.84% |  |
| 60 | `OriginalVolCeiling` | 老股转让发行量上限(股) | number(16,0) | ✓ | 1.48% |  |
| 61 | `IssueVolFloor` | 发行量下限(不少于)(股)(份) | number(16,0) | ✓ | 61.13% |  |
| 62 | `PlannedProceeds` | 拟募集资金总额(元) | number(19,4) | ✓ | 52.2% |  |
| 63 | `PlannedNetProceeds` | 拟募集资金净额(元) | number(19,4) | ✓ | 62.84% |  |
| 64 | `PlannedProceedsExGS` | 拟募集资金总额(超额配售全额行使后)(元) | number(19,4) | ✓ | 4.93% |  |
| 65 | `PlannedNProceedsExGS` | 拟募集资金净额(超额配售全额行使后)(元) | number(19,4) | ✓ | 4.93% |  |
| 66 | `OnlineIssueExOver` | 网上发行计划(剔除超额)(股)(份) | number(16,0) | ✓ | 72.75% |  |
| 67 | `OnlineIssuePlan` | 网上发行计划(股)(份) | number(19,2) | ✓ | 72.75% |  |
| 68 | `OfflineApplyPlan` | 网下配售计划(股)(份) | number(19,2) | ✓ | 61.0% |  |
| 69 | `StrategyApplyPlan` | 战略配售计划(股)(份) | number(19,2) | ✓ | 15.76% |  |
| 70 | `CoreStaffsSharePlan` | 其中:高管、员工计划参与战略配售数量(股)(份) | number(19,2) | ✓ | 4.56% |  |
| 71 | `CoreStaffsRatioPlan` | 其中:高管、员工计划参与战略配售占比(%) | number(19,8) | ✓ | 4.19% |  |
| 72 | `SponsorSharePlan` | 其中:保荐机构及相关子公司计划参与战略配售数量(股)(份) | number(19,2) | ✓ | 9.18% |  |
| 73 | `SponsorRatioPlan` | 其中:保荐机构及相关子公司计划参与战略配售占比(%) | number(19,8) | ✓ | 9.04% |  |
| 74 | `OtherStraSHVol` | 其中:其他参与战略配售计划数量(股)(份) | number(19,2) | ✓ | 5.39% |  |
| 75 | `OtherStraSHRat` | 其中:其他计划参与战略配售占比(%) | number(19,8) | ✓ | 4.37% |  |
| 76 | `OverAllotmentOption` | 超额配售权(股)(份) | number(16,0) | ✓ | 4.98% |  |
| 77 | `ApplyCodeOnline` | 上网发行申购代码 | varchar2(10) | ✓ | 85.55% |  |
| 78 | `IssueNameAbbr_Online` | 上网发行申购简称 | varchar2(20) | ✓ | 82.24% |  |
| 79 | `ApplyUnitOnline` | 上网发行认购单位(股)(份) | number(10) | ✓ | 85.36% |  |
| 80 | `ApplyMaxOnline` | 上网发行申购上限(股)(份) | number(16,0) | ✓ | 85.13% |  |
| 81 | `ApplyFloor_Online` | 上网发行申购下限(至少)(股)(份) | number(10) | ✓ | 73.02% |  |
| 82 | `LOAccuApplyCeiling` | 法定机构帐户累计申购上限(股)(份) | number(19,2) | ✓ | 0.69% |  |
| 83 | `ApplyUnitLP` | 网下配售认购单位(股)(份) | number(10) | ✓ | 61.04% |  |
| 84 | `ApplyMaxLP` | 网下配售申购上限(股)(份) | number(16,0) | ✓ | 61.86% |  |
| 85 | `ApplyMinLP` | 网下配售申购下限(股)(份) | number(16,0) | ✓ | 61.92% |  |
| 86 | `OLBefPutBack` | 网上发行量(回拨前)(万股)(万份) | number(19,4) | ✓ | 50.32% |  |
| 87 | `OLBefPutBackExGS` | 网上发行量(回拨前)(超额配售选择权行使后)(万股)(万份) | number(19,4) | ✓ | 4.95% |  |
| 88 | `OffLBefPutBack` | 网下发行量(回拨前)(万股)(万份) | number(19,4) | ✓ | 38.64% |  |
| 89 | `ExAbovePrice` | 剔除高于申购价格(元) | number(19,4) | ✓ | 19.22% |  |
| 90 | `FundPrefAllotment` | *投资基金优先配售限额(占发行量) | number(18,6) | ✓ | 2.62% |  |
| 91 | `SingleFundPrefAllotment` | *单个基金优先配售限额(占发行量) | number(18,6) | ✓ | 2.33% |  |
| 92 | `ApplyCodeSM` | *二级市场配售申购代码 | number(10) | ✓ | 5.06% |  |
| 93 | `ApplyMaxSM` | *二级市场配售申购上限(股) | number(16,0) | ✓ | 4.83% |  |
| 94 | `ApplyUnitSM` | *二级市场配售认购单位(股) | number(10) | ✓ | 4.79% |  |
| 95 | `MarkValueFloor` | 网下发行询价资格所需持有市值下限(元) | number(19,8) | ✓ | 17.88% |  |
| 96 | `CEFundMarkValueFloor` | 其中:创业板主题封闭基金所需持有市值下限(元) | number(19,4) | ✓ | 37.04% |  |
| 97 | `FundMarkValueFloor` | 其中:公募、养老和社保基金所需持有市值下限(元) | number(19,4) | ✓ | 37.04% |  |
| 98 | `OtherMarkValueFloor` | 其中:其他网下投资者所需持有市值下限(元) | number(19,4) | ✓ | 37.04% |  |
| 99 | `MarkValueStatmt` | 网下发行询价资格所需持有市值说明 | varchar2(500) | ✓ | 37.04% |  |
| 100 | `MVApplyRegDateOnline` | 网上市值申购登记日 | date | ✓ | 44.87% |  |
| 101 | `MVCalRefDayOnline` | 网下市值计算参考日 | date | ✓ | 35.89% |  |
| 102 | `DataSubmitEndDateoffline` | 网下核查材料报备截止日期 | date | ✓ | 21.99% |  |
| 103 | `DataSubmitEndTimeoffline` | 网下核查材料报备截止时间 | varchar2(8) | ✓ | 21.99% |  |
| 104 | `PriceNumberPI` | 初步询价价位个数 | number(10) | ✓ | 51.16% |  |
| 105 | `MinProgressivePricePI` | 初步询价最小累进价格(元) | number(9,4) | ✓ | 45.06% |  |
| 106 | `MinApplyingPricePI` | 初步询价最低申购价格(元) | number(9,4) | ✓ | 46.93% |  |
| 107 | `MaxApplyingPricePI` | 初步询价最高申购价格(元) | number(19,4) | ✓ | 46.93% |  |
| 108 | `PriceNumberBB` | 累计询价价位个数 | number(10) | ✓ | 1.27% |  |
| 109 | `MinProgressivePriceBB` | 累计询价最小累进价格(元) | number(9,4) | ✓ | 1.27% |  |
| 110 | `MaxApplyingRatioBB` | 累计询价申购数量上限比例(%) | number(9,6) | ✓ | 0.65% |  |
| 111 | `TimesBB` | 询价累积报价倍数 | number(19,8) | ✓ | 37.23% |  |
| 112 | `QuoteMedian` | 网下投资者全部报价中位数(元/股)(元/份) | number(19,4) | ✓ | 7.89% |  |
| 113 | `WeightedQuotation` | 网下投资者全部加权平均报价(元/股)(元/份) | number(19,4) | ✓ | 7.87% |  |
| 114 | `FundQuoteMedian` | 公募基金报价中位数(元/股)(元/份) | number(19,4) | ✓ | 7.87% |  |
| 115 | `FundWeightedQuotation` | 公募基金加权平均报价(元/股)(元/份) | number(19,4) | ✓ | 7.87% |  |
| 116 | `ExHighPriceMedian` | 剔除最高报价网下投资者报价中位数(元/股)(元/份) | number(19,4) | ✓ | 19.51% |  |
| 117 | `ExHighPriceWQ` | 剔除最高报价网下投资者加权平均报价(元/股)(元/份) | number(19,4) | ✓ | 19.51% |  |
| 118 | `ExHighPriceFundMedian` | 剔除最高报价公募基金报价中位数(元/股)(元/份) | number(19,4) | ✓ | 18.7% |  |
| 119 | `ExHighPriceFundWQ` | 剔除最高报价公募基金加权平均报价(元/股)(元/份) | number(19,4) | ✓ | 18.7% |  |
| 120 | `InitialInvestorNum` | 初步询价投资者家数(家) | number(10) | ✓ | 59.61% |  |
| 121 | `BidderNumberLP` | 初步询价配售对象家数(家) | number(16,0) | ✓ | 60.4% |  |
| 122 | `InitialApplyVol` | 初步询价申报总量(股)(份) | number(16,0) | ✓ | 19.3% |  |
| 123 | `ConformInvestorNum` | 符合规定投资者家数(家) | number(10) | ✓ | 19.15% |  |
| 124 | `ConformBidderNum` | 符合规定询价配售对象家数(家) | number(10) | ✓ | 19.3% |  |
| 125 | `ConformApplyVol` | 符合规定询价申报总量(股)(份) | number(16,0) | ✓ | 19.3% |  |
| 126 | `ValidQuoteInvestorNum` | 有效报价投资者家数(家) | number(10) | ✓ | 40.99% |  |
| 127 | `PlacingNumberLP` | 有效报价配售对象家数(家) | number(10) | ✓ | 60.67% |  |
| 128 | `ApplyVolLP` | 有效报价申购总量(股)(份) | number(16,0) | ✓ | 60.71% |  |
| 129 | `ValidApplyInvestorNum` | 法人配售有效申购投资者家数(家) | number(10) | ✓ | 19.18% |  |
| 130 | `ValidApplyNumLP` | 法人配售有效申购配售对象家数(家) | number(10) | ✓ | 61.36% |  |
| 131 | `ValidApplyVolLP` | 法人配售有效申购总量(股)(份) | number(16,0) | ✓ | 61.71% |  |
| 132 | `ExAbandonApplyNumLP` | 剔除放弃认购后有效申购配售对象家数(家) | number(10) | ✓ | 27.42% |  |
| 133 | `ExAbandonApplyVolLP` | 剔除放弃认购后有效申购总量(股)(份) | number(16,0) | ✓ | 27.42% |  |
| 134 | `ValidApplyVolOnline` | 网上发行有效申购总量(股)(份) | number(16,0) | ✓ | 85.43% |  |
| 135 | `ValidApplyNumOnline` | 网上发行有效申购户数(户) | number(10) | ✓ | 84.68% |  |
| 136 | `OverSubsTimesOnline` | 网上发行超额认购倍数(倍) | number(18,6) | ✓ | 85.41% |  |
| 137 | `NumAllotedOnline` | 网上发行配号总数(个) | number(10) | ✓ | 70.62% |  |
| 138 | `FreezedMoneyOnline` | 网上发行冻结资金(元) | number(19,4) | ✓ | 40.58% |  |
| 139 | `LotRateOnline` | 网上发行中签率(%) | number(18,15) | ✓ | 89.96% |  |
| 140 | `LotNumOnline` | 网上发行中签号 | varchar2(2000) | ✓ | 78.39% |  |
| 141 | `PlacingNumberOnline` | 网上发行获配户数(户) | number(16,0) | ✓ | 5.56% |  |
| 142 | `PlacingSharesOnline` | 网上发行获配股数(股)(份) | number(16,0) | ✓ | 5.56% |  |
| 143 | `PlacingRateOnline` | 网上发行获配比例(%) | number(19,8) | ✓ | 5.56% |  |
| 144 | `SharesOnline` | 网上实际发行股数(股)(份) | number(16,0) | ✓ | 91.34% |  |
| 145 | `SubsShareOL` | 投资者缴款认购股数(网上)(股)(份) | number(19,4) | ✓ | 91.34% |  |
| 146 | `SubsMoneyOL` | 投资者缴款认购金额(网上)(元) | number(19,4) | ✓ | 91.34% |  |
| 147 | `AbandonSubsSOL` | 投资者放弃认购股数(网上)(股)(份) | number(19,2) | ✓ | 43.06% |  |
| 148 | `AbandonSubsMOL` | 投资者放弃认购金额(网上)(元) | number(19,4) | ✓ | 43.06% |  |
| 149 | `UnderwritSOL` | 包销股数(网上放弃)(股)(份) | number(19,2) | ✓ | 43.06% |  |
| 150 | `UnderwritMOL` | 包销金额(网上放弃)(元) | number(19,4) | ✓ | 43.06% |  |
| 151 | `UnderwritPOL` | 包销比例(网上放弃)(股)(份) | number(19,4) | ✓ | 38.77% |  |
| 152 | `UnderwritAOL` | 包销股数(未达网上申购单位余股)(股)(份) | number(19,2) | ✓ | 0.85% |  |
| 153 | `AValidApplyVolLP` | 其中:A类有效申购总量(股)(份) | number(16,0) | ✓ | 36.27% |  |
| 154 | `BValidApplyVolLP` | 其中:B类有效申购总量(股)(份) | number(16,0) | ✓ | 36.44% |  |
| 155 | `CValidApplyVolLP` | 其中:C类有效申购总量(股)(份) | number(16,0) | ✓ | 31.75% |  |
| 156 | `OverSubsTimesLP` | 配售超额认购倍数(倍) | number(9,4) | ✓ | 61.04% |  |
| 157 | `ApplyMoneyLP` | 配售申购资金(元) | number(19,4) | ✓ | 28.98% |  |
| 158 | `LotRateLP` | 配售中签率(%) | number(18,15) | ✓ | 61.32% |  |
| 159 | `ALotRateLP` | 其中:A类投资者配售中签率(%) | number(12,10) | ✓ | 37.0% | 其中:A类投资者配售中签率(ALotRateLP)：A类投资者一般情况下代表公募基金和社保基金 |
| 160 | `BLotRateLP` | 其中:B类投资者配售中签率(%) | number(12,10) | ✓ | 37.29% | 其中:B类投资者配售中签率(BLotRateLP)：B类投资者一般情况下代表年金、保险资金 |
| 161 | `CLotRateLP` | 其中:C类投资者配售中签率(%) | number(12,10) | ✓ | 31.92% | 其中:C类投资者配售中签率(CLotRateLP)：C类投资者一般情况下代表除A类、B类以外的其他网下投资者 |
| 162 | `PlacingSharesLP` | 网下实际配售股数(股)(份) | number(16,0) | ✓ | 61.88% |  |
| 163 | `APlacingSharesLP` | 其中:A类实际配售股数(股)(份) | number(16,0) | ✓ | 37.06% |  |
| 164 | `BPlacingSharesLP` | 其中:B类实际配售股数(股)(份) | number(16,0) | ✓ | 37.35% |  |
| 165 | `CPlacingSharesLP` | 其中:C类实际配售股数(股)(份) | number(16,0) | ✓ | 32.0% |  |
| 166 | `NormalLegalPersonShare` | 向一般法人配售数量(股)(份) | number(16,0) | ✓ | 61.27% |  |
| 167 | `StrategicInvestorShare` | 向战略投资者配售数量(股)(份) | number(16,0) | ✓ | 11.08% |  |
| 168 | `CoreStaffsShare` | 其中:向高管、员工战略配售数量(股)(份) | number(16,0) | ✓ | 4.73% |  |
| 169 | `SponsorShare` | 其中:向保荐机构及相关子公司战略配售数量(股)(份) | number(16,0) | ✓ | 0.79% |  |
| 170 | `OtherShare` | 其中:向其他参与战略配售股数(股)(份) | number(16,0) | ✓ | 7.83% |  |
| 171 | `PlacingShareProportion` | 网下申购配售比例 | number(18,6) | ✓ | 61.88% |  |
| 172 | `SubsShareFL` | 投资者缴款认购股数(网下)(股)(份) | number(19,4) | ✓ | 61.88% |  |
| 173 | `SubsMoneyFL` | 投资者缴款认购金额(网下)(元) | number(19,4) | ✓ | 61.88% |  |
| 174 | `AbandonSubsSFL` | 投资者放弃认购股数(网下)(股)(份) | number(19,2) | ✓ | 40.06% |  |
| 175 | `AbandonSubsMFL` | 投资者放弃认购金额(网下)(元) | number(19,4) | ✓ | 40.06% |  |
| 176 | `ExAbandonOverSubsTLP` | 法人配售(剔除放弃认购)超额认购倍数 | number(9,4) | ✓ | 27.42% |  |
| 177 | `ExAbandonLotRateLP` | 法人配售(剔除放弃认购)中签率(%) | number(12,10) | ✓ | 27.42% |  |
| 178 | `UnderwritSFL` | 包销股数(网下放弃)(股)(份) | number(19,2) | ✓ | 39.72% |  |
| 179 | `UnderwritMFL` | 包销金额(网下放弃)(元) | number(19,4) | ✓ | 39.72% |  |
| 180 | `UnderwritPFL` | 包销比例(网下放弃) | number(19,4) | ✓ | 39.66% |  |
| 181 | `TailoredPlaVolLP` | 法人定向配售股数/战略定向配售(股)(份) | number(16,0) | ✓ | 11.26% |  |
| 182 | `STAQNETAllotment` | STAQ/NET拟定向配售股数(股) | number(16,0) | ✓ | 0.12% |  |
| 183 | `STAQNETSubscription` | STAQ/NET定向配售实际认购数(股) | number(16,0) | ✓ | 0.12% |  |
| 184 | `StaffAllotment` | 公司职工配售股数(股) | number(16,0) | ✓ | 8.47% |  |
| 185 | `UnderwriterBoughtVol` | 余股包销数量(股)(份) | number(16,0) | ✓ | 51.3% |  |
| 186 | `OverSubSum` | 发行时超额配售股数(股)(份) | number(19,2) | ✓ | 4.98% |  |
| 187 | `ExGSOptionPublDate` | 绿鞋行使情况公告日 | date | ✓ | 4.81% |  |
| 188 | `ExGSOptionEndDate` | 绿鞋行使截止日 | date | ✓ | 4.81% |  |
| 189 | `SLBuySum` | 二级买入股数(股) | number(19,2) | ✓ | 2.46% |  |
| 190 | `GSBuyMaxPriceSM` | 二级买入每股最高价(元) | number(19,8) | ✓ | 2.25% |  |
| 191 | `GSBuyMinPriceSM` | 二级买入每股最低价(元) | number(19,8) | ✓ | 2.25% |  |
| 192 | `GSBuyAvgPriceSM` | 二级买入每股平均价(元) | number(19,8) | ✓ | 2.31% |  |
| 193 | `GSTotalConsiderationSM` | 二级买入支付对价总额(元) | number(19,4) | ✓ | 2.19% |  |
| 194 | `ExGsOptionOverSubSum` | 绿鞋行使超额配售股数(股) | number(19,2) | ✓ | 3.08% |  |
| 195 | `GSDateToAccount` | 绿鞋行使募集资金到帐时间 | date | ✓ | 2.85% |  |
| 196 | `GSMoneyToAccount` | 绿鞋行使募集资金到帐金额(元) | number(19,4) | ✓ | 2.96% |  |
| 197 | `FunPrefAllotmentShares` | *投资基金优先配售股数(股) | number(16,0) | ✓ | 2.56% |  |
| 198 | `FunPrefAllotmentHoldTerm` | *投资基金优先配售持股期限(月) | number(9,4) | ✓ | 2.64% |  |
| 199 | `ValidApplyVolSM` | *二级市场配售有效申购总量(股) | number(16,0) | ✓ | 5.04% |  |
| 200 | `ValidApplyNumSM` | *二级市场配售有效申购户数(户) | number(10) | ✓ | 0.69% |  |
| 201 | `OverSubsTimesSM` | *二级市场配售超额认购倍数(倍) | number(9,4) | ✓ | 0.33% |  |
| 202 | `NumAllotedSM` | *二级市场配售配号总数(个) | number(10) | ✓ | 4.6% |  |
| 203 | `LotRateSM` | *二级市场配售中签率(%) | number(18,15) | ✓ | 5.04% |  |
| 204 | `PlacingSharesSM` | *二级市场实际配售股数(股) | number(16,0) | ✓ | 5.06% |  |
| 205 | `ParValue` | 每股面值(元) | number(25,10) | ✓ | 99.96% |  |
| 206 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 99.96% | 每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 207 | `IssuePrice` | 每股发行价(元) | number(19,4) | ✓ | 99.9% |  |
| 208 | `IssueVol` | 发行量(股)(份) | number(16,0) | ✓ | 99.92% |  |
| 209 | `IssueVolExGS` | 发行量(超额配售选择权行使后)(股)(份) | number(16,0) | ✓ | 3.08% |  |
| 210 | `OriginalVol` | 其中老股转让发行量(股) | number(16,0) | ✓ | 1.46% |  |
| 211 | `TotalSharesListDate` | 首发后总股本_上市日(股) | number(16,0) | ✓ | 99.62% |  |
| 212 | `TotalSharesBeforeIssue` | 首发前总股本(股) | number(16,0) | ✓ | 80.93% |  |
| 213 | `TotalIssueMV` | 发行总市值(元) | number(19,4) | ✓ | 99.87% |  |
| 214 | `TotalIssueMVExGS` | 发行总市值(超额配售选择权行使后)(元) | number(19,4) | ✓ | 3.08% |  |
| 215 | `StateSharesIssuePrice` | *国有股存量发行每股发行价(元) | number(19,4) | ✓ | 0.25% |  |
| 216 | `StateSharesIssued` | *国有股存量发行股数(股) | number(16,0) | ✓ | 0.25% |  |
| 217 | `CallBackVol` | 回拨股数(股) | number(19,2) | ✓ | 40.75% |  |
| 218 | `CallBackRatio` | 回拨比例(%) | number(9,4) | ✓ | 60.63% |  |
| 219 | `CallBackDirection` | 回拨方向 | number(10) | ✓ | 40.74% | 回拨方向(CallBackDirection)与(CT_SystemConst)表中的DM字段关联，令LB=2522，得... |
| 220 | `EstiPERatio` | 预估市盈率(倍) | number(19,8) | ✓ | 55.32% | 预估市盈率(倍)(EstiPERatio)=预估发行价/(上年净利润/发行后总股本(预披露))，招股意向书或发行公告公布... |
| 221 | `PERatioBeforeIssue` | 发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 72.39% |  |
| 222 | `PERBeforeIssueNCutNP` | ##扣非净利润前发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 18.7% |  |
| 223 | `PERBeforeIssueCutNP` | ##扣非净利润后发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 18.7% |  |
| 224 | `DilutedPERatio` | 发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 82.57% |  |
| 225 | `PERAfterIssueNCutNP` | ##扣非净利润前发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 18.74% |  |
| 226 | `PERAfterIssueCutNP` | ##扣非净利润后发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 18.78% |  |
| 227 | `DilutedPERatioFExGS` | 发行市盈率(按全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 4.91% |  |
| 228 | `PERAIssueNCutNPFExGS` | ##扣非净利润前发行市盈率(全额行使超额配售后)(倍) | number(19,8) | ✓ | 4.77% |  |
| 229 | `PERAIssueCutNPFExGS` | ##扣非净利润后发行市盈率(全额行使超额配售后)(倍) | number(19,8) | ✓ | 4.77% |  |
| 230 | `PBRatioBeforeIssue` | 发行市净率(按发行前总股本)(倍) | number(19,8) | ✓ | 4.27% |  |
| 231 | `PBRatioAfterIssue` | 发行市净率(按发行后总股本)(倍) | number(19,8) | ✓ | 11.74% |  |
| 232 | `PBRatioAfterIssueFExGS` | 发行市净率(按全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 3.43% |  |
| 233 | `AverageStaticPE` | 中证行业平均静态市盈率 | number(19,8) | ✓ | 50.95% |  |
| 234 | `PEEffectiveDate` | 行业市盈率生效日期 | date | ✓ | 25.96% |  |
| 235 | `WeightedPERatio` | *发行市盈率(加权平均)(倍) | number(19,8) | ✓ | 14.01% |  |
| 236 | `PERatioAfterIssue` | *发行市盈率(按发行后总股本预测利润)(倍) | number(19,8) | ✓ | 1.0% |  |
| 237 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 99.5% |  |
| 238 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 93.9% |  |
| 239 | `DateToAccount` | 募集资金到帐时间 | date | ✓ | 86.55% |  |
| 240 | `StateSharesProceeds` | *国有股存量发行收入总额(元) | number(19,4) | ✓ | 0.25% |  |
| 241 | `StateSharesNetProceeds` | *国有股存量发行收入净额(元) | number(19,4) | ✓ | 0.25% |  |
| 242 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 94.05% |  |
| 243 | `UnderwritingFee` | 承销费用(元) | number(19,4) | ✓ | 51.11% |  |
| 244 | `CPAFee` | 注册会计师费用(元) | number(19,4) | ✓ | 69.27% |  |
| 245 | `AssetAppraisalFee` | 资产评估费用(元) | number(19,4) | ✓ | 7.64% |  |
| 246 | `LandEvaluationFee` | *土地评估费用(元) | number(19,4) | ✓ | 0.89% |  |
| 247 | `AttorneyFee` | 律师费用(元) | number(19,4) | ✓ | 73.75% |  |
| 248 | `TotalAgentFee` | *中介机构费合计(元) | number(19,4) | ✓ | 0.98% |  |
| 249 | `OnlineIssueFee` | 上网发行费用(元) | number(19,4) | ✓ | 5.52% |  |
| 250 | `ScripFee` | 股票登记费用(元) | number(19,4) | ✓ | 16.12% |  |
| 251 | `SponsorFee` | 上市推荐费用(元) | number(19,4) | ✓ | 10.24% |  |
| 252 | `OtherFee` | 其他费用(元) | number(19,4) | ✓ | 72.23% |  |
| 253 | `IssueCostPerShare` | 每股发行费用(元/股) | number(18,6) | ✓ | 91.57% |  |
| 254 | `PreparedListExchange` | 上市地 | number(10) | ✓ | 100.0% | 上市地(PreparedListExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 20... |
| 255 | `OutstandingShares` | 本次上市流通股数(股)(份) | number(16,0) | ✓ | 97.88% |  |
| 256 | `NumOver1000Shares` | 持1000股以上股东户数(户) | number(10) | ✓ | 14.07% |  |
| 257 | `FirstOpenPrice` | 上市首日开盘价(元) | number(19,4) | ✓ | 99.54% |  |
| 258 | `FirstHighPrice` | 上市首日最高价(元) | number(19,4) | ✓ | 99.54% |  |
| 259 | `FirstLowPrice` | 上市首日最低价(元) | number(19,4) | ✓ | 99.54% |  |
| 260 | `FirstClosePrice` | 上市首日收盘价(元) | number(19,4) | ✓ | 99.58% |  |
| 261 | `FirstAvgPrice` | 上市首日成交均价(元) | number(19,4) | ✓ | 99.42% |  |
| 262 | `FirstTurnoverVolume` | 上市首日成交量(股) | number(16,0) | ✓ | 99.58% |  |
| 263 | `FirstTurnoverValue` | 上市首日成交额(元) | number(19,4) | ✓ | 99.58% |  |
| 264 | `FirstChangePCT` | 上市首日涨跌幅(%) | number(18,6) | ✓ | 99.58% |  |
| 265 | `FirstTurnover` | 上市首日换手率(%) | number(18,6) | ✓ | 99.6% |  |
| 266 | `SecuCode` | 上市时交易代码(正股代码) | varchar2(20) | ✓ | 100.0% |  |
| 267 | `SecurityAbbr` | 上市时证券简称(正股交易简称) | varchar2(100) | ✓ | 100.0% |  |
| 268 | `IssueProcessCode` | 发行进程 | number(10) | ✓ | 100.0% | 发行进程(IssueProcessCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1722 ... |
| 269 | `NAPSBeforeIssue` | 发行前每股净资产 | number(19,4) | ✓ | 92.53% |  |
| 270 | `NAPSAfterIssue` | 发行后每股净资产 | number(19,4) | ✓ | 93.23% |  |
| 271 | `NAPSAfterIssueFExGS` | 发行后每股净资产(超额配售选择权全额行使后) | number(19,8) | ✓ | 4.93% |  |
| 272 | `EarningForecastYear` | *盈利预测年度 | date | ✓ | 8.24% |  |
| 273 | `MainIncomeForecast` | *主营业务收入预测(元) | number(19,4) | ✓ | 19.34% |  |
| 274 | `NetProfitForecast` | *净利润预测(元) | number(19,4) | ✓ | 20.38% |  |
| 275 | `DilutedEPSForecast` | *全面摊薄每股盈利预测(元) | number(19,4) | ✓ | 5.52% |  |
| 276 | `DividendPolicy` | 股利分配政策 | varchar2(255) | ✓ | 92.82% |  |
| 277 | `EstimatedFirstDiviDate` | 预计首次分配时间 | varchar2(100) | ✓ | 16.55% |  |
| 278 | `ComparableCompany` | 可比上市公司 | number(10) | ✓ |  |  |
| 279 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 280 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 281 | `JSID` | JSID | number(19) | ✗ |  |  |
| 282 | `InternationalCoordinator` | 国际协调人 | varchar2(500) | ✓ | 0.0% |  |
| 283 | `ApplyPERatio` | 申购市盈率(倍) | number(19,8) | ✓ | 0.0% |  |
| 284 | `OtherPlacingShare` | 其他发行数量(股)(份) | number(16,0) | ✓ | 61.88% |  |
| 285 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 86.3% |  |

## 字段说明

### ListStandard (上市标准)

上市标准(ListStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 2206 AND DM IN (1,2,3,4,5,6,7,8,21,22,29,31,30,32,33,34,35,36,101,102)，得到上市标准的具体描述：1-预计市值不低于10亿，近两年净利润为正且不低于5000万或近一年净利润为正且营业收入不低于1亿，2-预计市值不低于15亿，近一年营业收入不低于2亿且近三年研发投入占营业收入比例15%，3-预计市值不低于20亿，近一年营业收入不低于3亿且近三年经营活动现金流量净额不低于1亿，4-预计市值不低于30亿，近一年营业收入不低于3亿，5-预计市值不低于40亿，主营业务或产品需经国家批准，市场空间大，已有阶段性成果和知名机构投资，具有明显技术优势，6-预计市值不低于人民币50亿元，且近一年营业收入不低于人民币5亿元，7-预计市值不低于人民币100亿元，8-最近3年净利润均为正，且最近3年净利润累计不低于1.5亿元，最近一年净利润不低于6000万元，最近3年经营活动产生的现金流量净额累计不低于1亿元或营业收入累计不低于10亿元，21-最近两年净利润均为正，且累计净利润不低于5000万元，22-预计市值不低于10亿元，最近一年净利润为正且营业收入不低于1亿元，29-预计市值不低于50亿元，且最近一年净利润为正，最近一年营业收入不低于6亿元，最近3年经营活动产生的现金流量净额累计不低于2.5亿元，30-预计市值不低于100亿元，且最近一年净利润为正，最近一年营业收入不低于10亿元，31-预计市值不低于2亿元，最近两年净利润均不低于1500万元且加权平均净资产收益率平均不低于8%，或者最近一年净利润不低于2500万元且加权平均净资产收益率不低于8%，32-预计市值不低于4亿元，最近两年营业收入平均不低于1亿元，且最近一年营业收入增长率不低于30%，最近一年经营活动产生的现金流量净额为正，33-预计市值不低于8亿元，最近一年营业收入不低于2亿元，最近两年研发投入合计占最近两年营业收入合计比例不低于8%，34-预计市值不低于15亿元，最近两年研发投入合计不低于5000万元，35-最近两年净利润均为正，累计净利润不低于1亿元，且最近一年净利润不低于6000万元，36-预计市值不低于15亿元，最近一年净利润为正且营业收入不低于4亿元，101-市值不低于2000亿元，102-市值200亿元以上，且拥有自主研发、国际领先技术，科技创新能力较强，同行业竞争中处于相对优势地位。

### OffLineLockArrange (网下配售锁定期安排)

网下配售锁定期安排(OffLineLockArrange)与(CT_SystemConst)表中的DM字段关联，令LB = 2284，得到网下配售锁定期安排的具体描述：1-无流通限制及锁定安排，2-每个配售对象30%的股份无锁定期,70%的股份锁定期为6个月，3-每个配售对象30%的股份无锁定期,70%的股份锁定期为12个月，4-10%参与网下配售摇号最终获配账户锁定期不低于6个月，5-无锁定(自愿锁定期0个月)和自愿锁定12个月，6-配售对象参与本次网下发行获配股票的锁定期为3个月，7-其他，8-网下投资者最终获配股票数量的10%锁定不低于6个月，9-每个配售对象50%的股份锁定3个月,50%的股份锁定期为6个月，10-每个配售对象50%的股份无锁定期,50%的股份锁定期为6个月，11-每个配售对象70%的股份无锁定期,30%的股份锁定期为6个月。

### RaisingMethod (募资方式)

募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM IN (1,2,10,99)，得到募资方式的具体描述：1-新股发行，2-历史遗留，10-吸收合并，99-其他。

### StockType (发行股票类型)

发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1,41)，得到发行股票类型的具体描述：1-A股，41-中国存托凭证。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

### EstiIssuePrice (预估发行价(元))

预估发行价(元)(EstiIssuePrice)：新股发行拟募集资金总额/ 发行量上限（不多于）

### EstiApMaxOnline (预估上网发行申购上限(最多)(股)(份))

预估上网发行申购上限(最多股)(EstiApMaxOnline)=网上发行计划（万股）/ 1000 取整（沪市主板）；网上发行计划（万股）/ 500 取整（深市及沪市科创板）

### ALotRateLP (其中:A类投资者配售中签率(%))

其中:A类投资者配售中签率(ALotRateLP)：A类投资者一般情况下代表公募基金和社保基金

### BLotRateLP (其中:B类投资者配售中签率(%))

其中:B类投资者配售中签率(BLotRateLP)：B类投资者一般情况下代表年金、保险资金

### CLotRateLP (其中:C类投资者配售中签率(%))

其中:C类投资者配售中签率(CLotRateLP)：C类投资者一般情况下代表除A类、B类以外的其他网下投资者

## SQL示例

```sql
-- 查询 A股发行与上市 数据
SELECT *
FROM lc_ashareipo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
