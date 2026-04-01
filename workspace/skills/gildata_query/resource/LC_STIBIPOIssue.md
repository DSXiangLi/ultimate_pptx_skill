# LC_STIBIPOIssue

**中文名**: 科创板IPO发行上市

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBIPOIssue` |
| MySQL表名 | `lc_stibipoissue` |
| 中文名 | 科创板IPO发行上市 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 205 |
| 版本 | 1.11 |

## 表描述

1.内容说明：该表包括A股科创板首次发行上市的明细情况。
2.数据范围：2019年-至今
3.信息来源：招股意向书、招股说明书、上市公告书等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `IntentLetterPublDate` | 招股意向书发布日期 | date | ✓ | 99.83% |  |
| 5 | `IntentLetterSignDate` | 招股意向书签署日期 | date | ✓ | 99.83% |  |
| 6 | `ProspectusPublDate` | 招股说明书发布日期 | date | ✓ | 99.34% |  |
| 7 | `ProspectusSignDate` | 招股说明书签署日期 | date | ✓ | 99.34% |  |
| 8 | `IssuePublDate` | 发行公告日 | date | ✓ | 99.83% |  |
| 9 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 100.0% |  |
| 10 | `IssueStartDate` | 发行日期起始 | date | ✓ | 99.83% |  |
| 11 | `IssueEndDate` | 发行日期截止 | date | ✓ | 99.83% |  |
| 12 | `OnlineStartDate` | 网上申购日期起始 | date | ✓ | 99.83% |  |
| 13 | `OnlineEndDate` | 网上申购日期截止 | date | ✓ | 99.83% |  |
| 14 | `PayDateOnline` | 网上申购缴款日期 | date | ✓ | 99.83% |  |
| 15 | `OfflineStartDate` | 网下申购日期起始 | date | ✓ | 99.83% |  |
| 16 | `OfflineEndDate` | 网下申购日期截止 | date | ✓ | 99.83% |  |
| 17 | `PayDateOffline` | 网下申购缴款日期 | date | ✓ | 99.83% |  |
| 18 | `LotRatePublDate` | 中签率公告日 | date | ✓ | 99.83% |  |
| 19 | `IssueResultPublDate` | 发行结果公告日 | date | ✓ | 99.67% |  |
| 20 | `ProposedListDate` | 预计上市日期 | date | ✓ | 0.17% |  |
| 21 | `ListAnnouncementDate` | 上市公告书发布日期 | date | ✓ | 99.0% |  |
| 22 | `ListedDate` | 上市日期 | date | ✓ | 99.0% |  |
| 23 | `NLPShareLD` | 向一般法人配售首次上市日期 | date | ✓ | 98.84% |  |
| 24 | `SIShareLD` | 向战略投资者配售首次上市日期 | date | ✓ | 98.84% |  |
| 25 | `IssueMethod` | 发行方式 | number(10) | ✓ |  | 发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1018 AND D... |
| 26 | `IssueSecuType` | 发行证券类型 | number(10) | ✓ | 100.0% | 发行证券类型(IssueSecuType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 A... |
| 27 | `RaisingMethod` | 募资方式 | number(10) | ✓ | 100.0% | 募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND... |
| 28 | `PricingModel` | 发行价定价方式 | number(10) | ✓ |  | 发行价定价方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1019 A... |
| 29 | `RationModel` | 发行量定量方式 | number(10) | ✓ |  | 发行量定量方式(RationModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1020，得到... |
| 30 | `IssueObject` | 发行对象 | varchar2(255) | ✓ | 99.83% |  |
| 31 | `ListStandard` | 上市标准 | number(10) | ✓ | 100.0% | 上市标准(ListStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 2206 AND ... |
| 32 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 99.83% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 ... |
| 33 | `IssuePriceCeiling` | 发行价上限(最高价)(元) | number(19,4) | ✓ | 99.67% |  |
| 34 | `IssuePriceFloor` | 发行价下限(最低价)(元) | number(19,4) | ✓ | 99.67% |  |
| 35 | `EstiIssuePrice` | 预估发行价(元) | number(19,4) | ✓ | 99.5% | 预估发行价(元)(EstiIssuePrice)：拟募集资金金额(PlannedProceeds)/ 发行量上限(Iss... |
| 36 | `EstiPERatio` | 预估市盈率(倍) | number(19,8) | ✓ | 99.34% | 预估市盈率(倍)(EstiPERatio)=预估发行价/(上年净利润/发行后总股本(预披露))，招股意向书或发行公告公布... |
| 37 | `EstiApMaxOnline` | 预估上网发行申购上限(最多)(股/份) | number(16,0) | ✓ | 99.83% | 预估上网发行申购上限(最多股)(EstiApMaxOnline)=网上发行计划(万股)/500取整，且不超过9999.9... |
| 38 | `IssueVolCeiling` | 发行量上限(不多于)(股/份) | number(16,0) | ✓ | 99.5% |  |
| 39 | `OriginalVolCeiling` | 其中:老股转让发行量上限(股/份) | number(16,0) | ✓ | 0.0% |  |
| 40 | `IssueVolFloor` | 发行量下限(不少于)(股/份) | number(16,0) | ✓ | 77.41% |  |
| 41 | `PlannedProceeds` | 拟募集资金金额(元) | number(19,4) | ✓ | 99.67% |  |
| 42 | `PlannedNetProceeds` | 拟募集资金净额(元) | number(19,4) | ✓ | 99.67% |  |
| 43 | `OnlineIssueExOver` | 网上发行计划(剔除超额)(股/份) | number(16,0) | ✓ | 99.83% |  |
| 44 | `OnlineIssuePlan` | 网上发行计划(股/份) | number(16,0) | ✓ | 99.83% |  |
| 45 | `OfflineApplyPlan` | 网下配售计划(股/份) | number(16,0) | ✓ | 99.83% |  |
| 46 | `StrategyApplyPlan` | 战略配售计划(股/份) | number(16,0) | ✓ | 99.83% |  |
| 47 | `CoreStaffsSharePlan` | 其中:高管、员工计划参与战略配售数量(股/份) | number(16,0) | ✓ | 55.98% |  |
| 48 | `CoreStaffsRatioPlan` | 其中:高管、员工计划参与战略配售占比(%) | number(9,4) | ✓ | 56.81% |  |
| 49 | `SponsorSharePlan` | 其中:保荐机构及相关子公司计划参与战略配售数量(股/份) | number(16,0) | ✓ | 99.67% |  |
| 50 | `SponsorRatioPlan` | 其中:保荐机构及相关子公司计划参与战略配售占比(%) | number(9,4) | ✓ | 99.67% |  |
| 51 | `OtherStraSHVol` | 其中:其他参与战略配售计划数量(股/份) | number(19,2) | ✓ | 1.83% |  |
| 52 | `OtherStraSHRat` | 其中:其他计划参与战略配售占比(%) | number(19,8) | ✓ | 0.33% |  |
| 53 | `CommissionRate` | 新股配售经纪佣金费率(%) | number(9,4) | ✓ | 84.55% |  |
| 54 | `OverAllotmentOption` | 超额配售权(股/份) | number(16,0) | ✓ | 1.83% |  |
| 55 | `ApplyCodeOnline` | 上网发行申购代码 | varchar2(10) | ✓ | 99.83% |  |
| 56 | `ApplyAbbrNameOnline` | 上网发行申购简称 | varchar2(12) | ✓ | 99.83% |  |
| 57 | `ApplyUnitOnline` | 上网发行认购单位(股/份) | number(16,0) | ✓ | 99.83% |  |
| 58 | `ApplyMaxOnline` | 上网发行申购上限(股/份) | number(16,0) | ✓ | 99.83% |  |
| 59 | `ApplyFloorOnline` | 上网发行申购下限(股/份) | number(16,0) | ✓ | 99.83% |  |
| 60 | `ApplyUnitLP` | 网下配售认购单位(股/份) | number(16,0) | ✓ | 99.83% |  |
| 61 | `ApplyMaxLP` | 网下配售申购上限(股/份) | number(16,0) | ✓ | 99.83% |  |
| 62 | `ApplyMinLP` | 网下配售申购下限(股/份) | number(16,0) | ✓ | 99.83% |  |
| 63 | `OLBefPutBack` | 网上发行量(回拨前)(股/份) | number(16,0) | ✓ | 99.67% |  |
| 64 | `OffLBefPutBack` | 网下发行量(回拨前)(股/份) | number(16,0) | ✓ | 99.67% |  |
| 65 | `OLBefPutBackExGS` | 网上发行量(回拨前)(超额配售选择权行使后)(股/份) | number(16,0) | ✓ | 1.83% |  |
| 66 | `OffLineLockArrange` | 网下配售锁定期安排 | number(10) | ✓ | 99.83% | 网下配售锁定期安排(OffLineLockArrange)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 67 | `ExAbovePrice` | 申购价格(元) | number(19,4) | ✓ | 99.5% |  |
| 68 | `MarkValueFloor` | 网下询价所需市值下限(元) | number(19,4) | ✓ | 0.0% |  |
| 69 | `CEFundMarkValueFloor` | 其中:科创主题封闭基金所需持有市值下限(元) | number(19,4) | ✓ | 99.83% |  |
| 70 | `FundMarkValueFloor` | 其中:公募养老社保所需市值下限(元) | number(19,4) | ✓ | 99.83% |  |
| 71 | `OtherMarkValueFloor` | 其中:其他投资者所需市值下限(元) | number(19,4) | ✓ | 99.83% |  |
| 72 | `MarkValueStatmt` | 网下询价所需市值说明 | varchar2(1000) | ✓ | 99.83% |  |
| 73 | `MVApplyRegDateOnline` | 网上市值申购登记日 | date | ✓ | 99.83% |  |
| 74 | `MVCalRefDayOnline` | 网下市值计算参考日 | date | ✓ | 99.83% |  |
| 75 | `DataSubmitEndDateoffline` | 网下核查材料报备截止日期 | date | ✓ | 99.83% |  |
| 76 | `DataSubmitEndTimeoffline` | 网下核查材料报备截止时间 | varchar2(8) | ✓ | 99.83% |  |
| 77 | `PriceNumberPI` | 初步询价价位个数 | number(10) | ✓ | 99.83% |  |
| 78 | `MinProgressivePricePI` | 初步询价最小累进价格(元) | number(9,4) | ✓ | 99.83% |  |
| 79 | `MinApplyingPricePI` | 初步询价最低申购价格(元) | number(9,4) | ✓ | 99.5% |  |
| 80 | `MaxApplyingPricePI` | 初步询价最高申购价格(元) | number(19,4) | ✓ | 99.5% |  |
| 81 | `TimesBB` | 询价累积报价倍数 | number(19,8) | ✓ | 99.5% |  |
| 82 | `QuoteMedian` | 每股/份网下投资者全部报价中位数(元) | number(19,4) | ✓ | 0.0% |  |
| 83 | `WeightedQuotation` | 每股/份网下投资者全部加权平均报价(元) | number(19,4) | ✓ | 0.0% |  |
| 84 | `FundQuoteMedian` | 每股/份公募基金报价中位数(元) | number(19,4) | ✓ | 0.0% |  |
| 85 | `FundWeightedQuotation` | 每股/份公募基金加权平均报价(元) | number(19,4) | ✓ | 0.0% |  |
| 86 | `ExHighPriceMedian` | 每股/份剔除最高报价网下投资者报价中位数(元) | number(19,4) | ✓ | 99.67% |  |
| 87 | `ExHighPriceWQ` | 每股/份剔除最高报价网下投资者加权平均报价(元) | number(19,4) | ✓ | 99.67% |  |
| 88 | `ExHighPriceFundMedian` | 每股/份剔除最高报价公募基金报价中位数(元) | number(19,4) | ✓ | 99.67% |  |
| 89 | `ExHighPriceFundWQ` | 每股/份剔除最高报价公募基金加权平均报价(元) | number(19,4) | ✓ | 99.67% |  |
| 90 | `InitialInvestorNum` | 初步询价投资者家数(家) | number(10) | ✓ | 99.67% |  |
| 91 | `BidderNumberLP` | 初步询价配售对象家数(家) | number(10) | ✓ | 99.67% |  |
| 92 | `InitialApplyVol` | 初步询价申报总量(股/份) | number(16,0) | ✓ | 99.67% |  |
| 93 | `ConformInvestorNum` | 符合规定投资者家数(家) | number(10) | ✓ | 99.67% |  |
| 94 | `ConformBidderNum` | 符合规定询价配售对象家数(家) | number(10) | ✓ | 99.67% |  |
| 95 | `ConformApplyVol` | 符合规定询价申报总量(股/份) | number(16,0) | ✓ | 99.67% |  |
| 96 | `ValidQuoteInvestorNum` | 有效报价投资者家数(家) | number(10) | ✓ | 99.67% |  |
| 97 | `PlacingNumberLP` | 有效报价配售对象家数(家) | number(10) | ✓ | 99.67% |  |
| 98 | `ApplyVolLP` | 有效报价申购总量(股/份) | number(16,0) | ✓ | 99.67% |  |
| 99 | `ValidApplyInvestorNum` | 法人配售有效申购投资者家数(家) | number(10) | ✓ | 99.5% |  |
| 100 | `ValidApplyNumLP` | 法人配售有效申购配售对象家数(家) | number(10) | ✓ | 99.5% |  |
| 101 | `ValidApplyVolLP` | 法人配售有效申购总量(股/份) | number(16,0) | ✓ | 99.5% |  |
| 102 | `ExAbandonApplyNumLP` | 剔除放弃认购后有效申购配售对象家数(家) | number(10) | ✓ | 99.34% |  |
| 103 | `ExAbandonApplyVolLP` | 剔除放弃认购后有效申购总量(股/份) | number(16,0) | ✓ | 99.34% |  |
| 104 | `ExAbandonOverSubsTLP` | 法人配售(剔除放弃认购)超额认购倍数 | number(9,4) | ✓ | 99.34% |  |
| 105 | `ExAbandonLotRateLP` | 法人配售(剔除放弃认购)中签率(%) | number(12,10) | ✓ | 99.34% |  |
| 106 | `ValidApplyVolOnline` | 网上发行有效申购总量(股/份) | number(16,0) | ✓ | 99.5% |  |
| 107 | `ValidApplyNumOnline` | 网上发行有效申购户数(户) | number(10) | ✓ | 99.5% |  |
| 108 | `OverSubsTimesOnline` | 网上发行超额认购倍数(倍) | number(18,6) | ✓ | 99.5% |  |
| 109 | `NumAllotedOnline` | 网上发行配号总数(个) | number(10) | ✓ | 99.5% |  |
| 110 | `LotRateOnline` | 网上发行中签率(%) | number(18,15) | ✓ | 99.5% |  |
| 111 | `LotNumOnline` | 网上发行中签号 | varchar2(2000) | ✓ | 99.5% |  |
| 112 | `SharesOnline` | 网上实际发行股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 113 | `SubsShareOL` | 网上投资者缴款认购股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 114 | `SubsMoneyOL` | 网上投资者缴款认购金额(元) | number(19,4) | ✓ | 99.5% |  |
| 115 | `AbandonSubsSOL` | 网上投资者放弃认购股数(股/份) | number(19,2) | ✓ | 99.34% |  |
| 116 | `AbandonSubsMOL` | 网上投资者放弃认购金额(元) | number(19,4) | ✓ | 99.34% |  |
| 117 | `UnderwritSOL` | 包销股数(网上放弃)(股/份) | number(19,2) | ✓ | 99.34% |  |
| 118 | `UnderwritMOL` | 包销金额(网上放弃)(元) | number(19,4) | ✓ | 99.34% |  |
| 119 | `UnderwritPOL` | 包销比例(网上放弃)(%) | number(18,6) | ✓ | 99.34% |  |
| 120 | `UnderwritAOL` | 包销股数(未达网上申购单位余股)(股/份) | number(19,2) | ✓ | 0.17% |  |
| 121 | `AValidApplyVolLP` | 其中:A类有效申购总量(股/份) | number(16,0) | ✓ | 99.5% | 其中:A类有效申购总量(股)：A类投资者一般情况下代表公募基金和社保基金 |
| 122 | `BValidApplyVolLP` | 其中:B类有效申购总量(股/份) | number(16,0) | ✓ | 99.5% | 其中:B类有效申购总量(股)：B类投资者一般情况下代表年金、保险资金 |
| 123 | `CValidApplyVolLP` | 其中:C类有效申购总量(股/份) | number(16,0) | ✓ | 84.55% | 其中:C类有效申购总量(股)：C类投资者一般情况下代表除A类、B类以外的其他网下投资者 |
| 124 | `OverSubsTimesLP` | 配售超额认购倍数(倍) | number(18,6) | ✓ | 99.5% |  |
| 125 | `LotRateLP` | 配售中签率(%) | number(18,15) | ✓ | 99.5% |  |
| 126 | `ALotRateLP` | 其中:A类中签率(%) | number(12,10) | ✓ | 99.5% |  |
| 127 | `BLotRateLP` | 其中:B类中签率(%) | number(12,10) | ✓ | 99.5% |  |
| 128 | `CLotRateLP` | 其中:C类中签率(%) | number(12,10) | ✓ | 84.55% |  |
| 129 | `PlacingSharesLP` | 网下实际配售股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 130 | `APlacingSharesLP` | 其中:A类实际配售股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 131 | `BPlacingSharesLP` | 其中:B类实际配售股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 132 | `CPlacingSharesLP` | 其中:C类实际配售股数(股/份) | number(16,0) | ✓ | 84.55% |  |
| 133 | `NLPShare` | 向一般法人配售数量(股/份) | number(16,0) | ✓ | 99.5% |  |
| 134 | `SIShare` | 向战略投资者配售数量(股/份) | number(16,0) | ✓ | 99.5% |  |
| 135 | `CoreStaffsShare` | 其中:向高管、员工战略配售数量(股/份) | number(16,0) | ✓ | 57.31% |  |
| 136 | `SponsorShare` | 其中:向保荐机构及相关子公司战略配售数量(股/份) | number(16,0) | ✓ | 99.67% |  |
| 137 | `OtherShare` | 其中:向其他参与战略配售股数(股/份) | number(16,0) | ✓ | 20.27% |  |
| 138 | `PlacingShareProportion` | 网下申购配售比例 | number(18,6) | ✓ | 99.5% |  |
| 139 | `Commission` | 新股配售经纪佣金(元) | number(19,4) | ✓ | 84.39% |  |
| 140 | `SubsShareFL` | 网下投资者缴款认购股数(股/份) | number(16,0) | ✓ | 99.5% |  |
| 141 | `SubsMoneyFL` | 网下投资者缴款认购金额(元) | number(19,4) | ✓ | 99.5% |  |
| 142 | `AbandonSubsSFL` | 网下投资者放弃认购股数(股/份) | number(16,0) | ✓ | 99.34% |  |
| 143 | `AbandonSubsMFL` | 网下投资者放弃认购金额(元) | number(19,4) | ✓ | 99.34% |  |
| 144 | `UnderwritSFL` | 包销股数(网下放弃)(股/份) | number(16,0) | ✓ | 99.34% |  |
| 145 | `UnderwritMFL` | 包销金额(网下放弃)(元) | number(19,4) | ✓ | 99.34% |  |
| 146 | `UnderwritPFL` | 包销比例(网下放弃)(%) | number(18,6) | ✓ | 99.34% |  |
| 147 | `UnderwriterBoughtVol` | 余股包销数量(股/份) | number(16,0) | ✓ | 99.34% |  |
| 148 | `OverSubSum` | 发行时超额配售股数(股/份) | number(16,0) | ✓ | 1.83% |  |
| 149 | `ExGSOptionPublDate` | 绿鞋行使情况公告日 | date | ✓ | 1.66% |  |
| 150 | `ExGSOptionEndDate` | 绿鞋行使截止日 | date | ✓ | 1.66% |  |
| 151 | `SLBuySum` | 二级买入股数(股/份) | number(19,2) | ✓ | 0.5% |  |
| 152 | `GSBuyMaxPriceSM` | 二级买入每股/份最高价(元) | number(19,8) | ✓ | 0.5% |  |
| 153 | `GSBuyMinPriceSM` | 二级买入每股/份最低价(元) | number(19,8) | ✓ | 0.5% |  |
| 154 | `GSBuyAvgPriceSM` | 二级买入每股/份平均价(元) | number(19,8) | ✓ | 0.5% |  |
| 155 | `GSTotalConsiderationSM` | 二级买入支付对价总额(元) | number(19,4) | ✓ | 0.5% |  |
| 156 | `ExGsOptionOverSubSum` | 绿鞋行使超额配售股数(股/份) | number(16,0) | ✓ | 1.16% |  |
| 157 | `GSDateToAccount` | 绿鞋行使募集资金到帐时间 | date | ✓ | 1.0% |  |
| 158 | `GSMoneyToAccount` | 绿鞋行使募集资金到帐金额(元) | number(19,4) | ✓ | 1.16% |  |
| 159 | `ParValue` | 每股/份面值(元) | number(25,10) | ✓ | 99.67% |  |
| 160 | `ParValueCurrencyUnit` | 每股/份面值货币单位 | number(10) | ✓ | 99.67% | 每股/份面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令... |
| 161 | `IssuePrice` | 每股/份发行价(元) | number(19,4) | ✓ | 99.83% |  |
| 162 | `IssueVol` | 发行量(股/份) | number(16,0) | ✓ | 99.83% |  |
| 163 | `IssueVolExGS` | 发行量(超额配售选择权行使后)(股/份) | number(16,0) | ✓ | 1.16% |  |
| 164 | `OriginalVol` | 其中:老股转让发行量(股/份) | number(16,0) | ✓ | 0.0% |  |
| 165 | `TotalSharesListDate` | 首发后总股本_上市日(股/份) | number(16,0) | ✓ | 99.0% |  |
| 166 | `TotalSharesBeforeIssue` | 首发前总股本(股/份) | number(16,0) | ✓ | 99.83% |  |
| 167 | `TotalIssueMV` | 发行总市值(元) | number(19,4) | ✓ | 99.67% |  |
| 168 | `TotalIssueMVExGS` | 发行总市值(超额配售选择权行使后)(元) | number(19,4) | ✓ | 1.16% |  |
| 169 | `CallBackRatio` | 回拨比例(%) | number(9,4) | ✓ | 99.5% |  |
| 170 | `CallBackVol` | 回拨股数(股/份) | number(19,2) | ✓ | 99.5% |  |
| 171 | `CallBackDirection` | 回拨方向 | number(10) | ✓ | 99.5% | 回拨方向(CallBackDirection)与(CT_SystemConst)表中的DM字段关联，令LB=2522，得... |
| 172 | `PERatioBeforeIssue` | 发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 89.7% |  |
| 173 | `PERBeforeIssueNCutNP` | ##扣非净利润前发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 89.53% |  |
| 174 | `PERBeforeIssueCutNP` | ##扣非净利润后发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 89.37% |  |
| 175 | `DilutedPERatio` | 发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 89.87% |  |
| 176 | `PERAfterIssueNCutNP` | ##扣非净利润前发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 89.53% |  |
| 177 | `PERAfterIssueCutNP` | ##扣非净利润后发行市盈率(按发行后总股本)(倍) | number(19,8) | ✓ | 89.53% |  |
| 178 | `DilutedPERatioFExGS` | 发行市盈率(按全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 1.16% |  |
| 179 | `PERAIssueNCutNPFExGS` | ##扣非净利润前发行市盈率(按全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 1.0% |  |
| 180 | `PERAIssueCutNPFExGS` | ##扣非净利润后发行市盈率(全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 1.0% |  |
| 181 | `PBRatioBeforeIssue` | 发行市净率(按发行前总股本)(倍) | number(19,8) | ✓ | 3.99% |  |
| 182 | `PBRatioAfterIssue` | 发行市净率(按发行后总股本)(倍) | number(19,8) | ✓ | 28.24% |  |
| 183 | `PBRatioAfterIssueFExGS` | 发行市净率(按全额行使超额配售后总股本)(倍) | number(19,8) | ✓ | 1.5% |  |
| 184 | `WeightedPERatio` | 发行市盈率(加权平均)(倍) | number(19,8) | ✓ | 0.0% |  |
| 185 | `PERatioAfterIssue` | 发行市盈率(按发行后总股本预测利润)(倍) | number(19,8) | ✓ | 0.0% |  |
| 186 | `AverageStaticPE` | 中证行业平均静态市盈率 | number(19,8) | ✓ | 97.18% |  |
| 187 | `PEEffectiveDate` | 行业市盈率生效日期 | date | ✓ | 97.18% |  |
| 188 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 99.67% |  |
| 189 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 98.84% |  |
| 190 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 99.0% |  |
| 191 | `DateToAccount` | 募集资金到帐时间 | date | ✓ | 98.84% |  |
| 192 | `OutstandingShares` | 本次上市流通股数(股/份) | number(16,0) | ✓ | 99.0% |  |
| 193 | `SecuCode` | 上市时交易代码(正股代码) | varchar2(20) | ✓ | 100.0% |  |
| 194 | `SecurityAbbr` | 上市时证券简称(正股交易简称) | varchar2(100) | ✓ | 100.0% |  |
| 195 | `IssueProcess` | 发行进程 | number(10) | ✓ | 100.0% | 发行进程(IssueProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 1722 AND ... |
| 196 | `NAPSBeforeIssue` | 发行前每股/份净资产 | number(19,4) | ✓ | 99.67% |  |
| 197 | `NAPSAfterIssue` | 发行后每股/份净资产 | number(19,4) | ✓ | 99.5% |  |
| 198 | `NAPSAfterIssueFExGS` | 发行后每股/份净资产(超额配售选择权全额行使后) | number(19,8) | ✓ | 1.66% |  |
| 199 | `DividendPolicy` | 股利分配政策 | varchar2(255) | ✓ | 99.83% |  |
| 200 | `ApplyPERatio` | 申购市盈率(倍) | number(19,8) | ✓ | 0.17% |  |
| 201 | `OtherPlacingShare` | 其他发行数量(股/份) | number(16,0) | ✓ | 99.5% |  |
| 202 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 98.84% |  |
| 203 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 204 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 205 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IssueMethod (发行方式)

发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1018 AND DM IN (7,9,13)，得到发行方式的具体描述：7-上网定价，9-法人配售，13-法人定向配售。

### IssueSecuType (发行证券类型)

发行证券类型(IssueSecuType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1,41)，得到发行证券类型的具体描述：1-A股，41-中国存托凭证。

### RaisingMethod (募资方式)

募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM IN (1,10,99)，得到募资方式的具体描述：1-新股发行，10-吸收合并，99-其他。

### PricingModel (发行价定价方式)

发行价定价方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1019 AND DM IN (1,15,17)，得到发行价定价方式的具体描述：1-发行人与承销商协商定价，15-初步询价，17-发行人直接定价。

### RationModel (发行量定量方式)

发行量定量方式(RationModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1020，得到发行量定量方式的具体描述：1-发行额度，2-设定上限，3-设定下限，4-设定区间。

### ListStandard (上市标准)

上市标准(ListStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 2206 AND DM NOT IN (11,12,17,26)，得到上市标准的具体描述：1-预计市值不低于10亿，近两年净利润为正且不低于5000万或近一年净利润为正且营业收入不低于1亿，2-预计市值不低于15亿，近一年营业收入不低于2亿且近三年研发投入占营业收入比例15%，3-预计市值不低于20亿，近一年营业收入不低于3亿且近三年经营活动现金流量净额不低于1亿，4-预计市值不低于30亿，近一年营业收入不低于3亿，5-预计市值不低于40亿，主营业务或产品需经国家批准，市场空间大，已有阶段性成果和知名机构投资，具有明显技术优势，6-预计市值不低于人民币50亿元，且近一年营业收入不低于人民币5亿元，7-预计市值不低于人民币100亿元，8-最近3年净利润均为正，且最近3年净利润累计不低于1.5亿元，最近一年净利润不低于6000万元，最近3年经营活动产生的现金流量净额累计不低于1亿元或营业收入累计不低于10亿元，9-预计市值不低于50亿元，且最近一年净利润为正，最近一年营业收入不低于6亿元，最近3年经营活动产生的现金流量净额累计不低于1.5亿元，10-预计市值不低于80亿元，且最近一年净利润为正，最近一年营业收入不低于8亿元，13-预计市值不低于200亿元，且最近一年营业收入不低于30亿元，14-营业收入快速增长，拥有自主研发、国际领先技术，在同行业竞争中处于相对优势地位，且预计市值不低于100亿元，15-营业收入快速增长，拥有自主研发、国际领先技术，在同行业竞争中处于相对优势地位，且预计市值不低于50亿元，最近一年营业收入不低于5亿元，16-预计市值不低于200亿元，且最近一年净利润为正，21-最近两年净利润均为正，且累计净利润不低于5000万元，22-预计市值不低于10亿元，最近一年净利润为正且营业收入不低于1亿元，23-预计市值不低于50亿元，且最近一年营业收入不低于3亿元，24-预计市值不低于100亿元，且最近一年净利润为正，25-预计市值不低于50亿元，最近一年净利润为正且营业收入不低于5亿元，27-预计市值不低于50 亿元，且最近一年营业收入不低于 5 亿元，28-最近3年净利润均为正，且最近3年净利润累计不低于2亿元，最近一年净利润不低于1亿元，最近3年经营活动产生的现金流量净额累计不低于2亿元或者营业收入累计不低于15亿元，29-预计市值不低于50亿元，且最近一年净利润为正，最近一年营业收入不低于6亿元，最近3年经营活动产生的现金流量净额累计不低于2.5亿元，30-预计市值不低于100亿元，且最近一年净利润为正，最近一年营业收入不低于10亿元，31-预计市值不低于2亿元，最近两年净利润均不低于1500万元且加权平均净资产收益率平均不低于8%，或者最近一年净利润不低于2500万元且加权平均净资产收益率不低于8%，32-预计市值不低于4亿元，最近两年营业收入平均不低于1亿元，且最近一年营业收入增长率不低于30%，最近一年经营活动产生的现金流量净额为正，33-预计市值不低于8亿元，最近一年营业收入不低于2亿元，最近两年研发投入合计占最近两年营业收入合计比例不低于8%，34-预计市值不低于15亿元，最近两年研发投入合计不低于5000万元，35-最近两年净利润均为正，累计净利润不低于1亿元，且最近一年净利润不低于6000万元，36-预计市值不低于15亿元，最近一年净利润为正且营业收入不低于4亿元，101-市值不低于2000亿元，102-市值200亿元以上，且拥有自主研发、国际领先技术，科技创新能力较强，同行业竞争中处于相对优势地位。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 AND DM = 2，得到承销方式的具体描述：2-余额包销。

### EstiIssuePrice (预估发行价(元))

预估发行价(元)(EstiIssuePrice)：拟募集资金金额(PlannedProceeds)/ 发行量上限(IssueVolCeiling)

### EstiPERatio (预估市盈率(倍))

预估市盈率(倍)(EstiPERatio)=预估发行价/(上年净利润/发行后总股本(预披露))，招股意向书或发行公告公布计划发行量上下限时，再根据发行前股本加计划发行量（优先使用计划发行量上限，计划上限为空使用计划发行量下限）更新预估市盈率。

### EstiApMaxOnline (预估上网发行申购上限(最多)(股/份))

预估上网发行申购上限(最多股)(EstiApMaxOnline)=网上发行计划(万股)/500取整，且不超过9999.95万股

## SQL示例

```sql
-- 查询 科创板IPO发行上市 数据
SELECT *
FROM lc_stibipoissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
