# DZ_AShareSeasonedNewIssue

**中文名**: A股增发

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AShareSeasonedNewIssue` |
| MySQL表名 | `dz_ashareseasonednewissue` |
| 中文名 | A股增发 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 175 |
| 版本 | 1.12 |

## 表描述

1.收录A股增发A股、B股增发A股、H股增发A股等的明细情况，包括历次增发预案、进程日期、预案有效期、发行属性、发行价区间、发行量区间、发行日期、上网发行情况、网下配售申购情况和募集资金与费用等内容。
2.数据范围：1991-08-17至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EventProcedureCode` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 164... |
| 5 | `IssueType` | 增发类别 | number(10) | ✗ | 100.0% | 增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM ... |
| 6 | `IfSummaryProcedure` | 是否简易程序 | number(10) | ✓ | 14.05% | 是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。 |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 	 是否有效（IfEffected）的具体描述：1-是（代表增发处于正常有效状态），2-否（代表增发处于已终止或否决等无... |
| 8 | `ProjInfoSource` | 预案信息来源 | varchar2(200) | ✓ | 87.45% |  |
| 9 | `IssueResultInfoSource` | 发行结果信息来源 | varchar2(200) | ✓ | 50.54% |  |
| 10 | `AdvanceDate` | 首次预案公布日期 | date | ✓ | 87.44% |  |
| 11 | `LatestAdvanceDate` | 最新预案公布日期 | date | ✓ | 87.44% |  |
| 12 | `SMDeciPublDate` | 最新股东大会决议公告日期 | date | ✓ | 88.46% |  |
| 13 | `IntentLetterPublDate` | 增发新股意向书发布日期 | date | ✓ | 1.68% |  |
| 14 | `ProspectusPublDate` | 增发新股说明书发布日期 | date | ✓ | 0.19% |  |
| 15 | `SASACApprovalPublDate` | 国资委通过公告日 | date | ✓ | 12.89% |  |
| 16 | `CSRCApprovalPublDate` | 证监会批准公告日 | date | ✓ | 52.06% |  |
| 17 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 86.48% |  |
| 18 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 72.97% |  |
| 19 | `StockType` | 增发A股类型 | number(10) | ✗ | 100.0% | 增发A股类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1239 AND D... |
| 20 | `PriceIntervalStatement` | 发行价区间确定方式说明 | varchar2(255) | ✓ | 99.72% |  |
| 21 | `PricingModel` | 发行价定价方式 | number(10) | ✓ |  |  |
| 22 | `RationModel` | 发行量定量方式 | number(10) | ✓ |  |  |
| 23 | `IssueMethod` | 发行方式 | number(10) | ✓ |  |  |
| 24 | `IssuePurpose` | 增发目的 | varchar2(255) | ✓ | 99.97% |  |
| 25 | `IssueObject` | 发行对象 | varchar2(255) | ✓ | 99.96% |  |
| 26 | `ISOBTypeCode` | 发行对象类型 | number(10) | ✓ |  |  |
| 27 | `SubscribeMethod` | 认购方式 | number(10) | ✓ | 99.95% | 认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得... |
| 28 | `LargeSHSubMethod` | 控股股东认购方式 | number(10) | ✓ | 21.1% | 控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2... |
| 29 | `LargeSHSubsSum` | 控股股东认购数量(股) | number(16,0) | ✓ | 15.01% |  |
| 30 | `LargeSHSubsRatio` | 控股股东认购比例(%) | number(19,8) | ✓ | 17.17% |  |
| 31 | `IssuePriceCeiling` | 发行价上限(最高价)(元) | number(19,4) | ✓ | 41.03% |  |
| 32 | `IssuePriceFloor` | 发行价下限(最低价)(元) | number(19,4) | ✓ | 57.64% |  |
| 33 | `OrgPriceBasePRatio` | 预案价格相对基准价格比例(%) | number(19,8) | ✓ | 95.55% |  |
| 34 | `PricingBaseDate` | 定价基准日 | date | ✓ | 73.0% |  |
| 35 | `PricingBaseDateDesc` | 定价基准日描述 | varchar2(100) | ✓ | 93.44% |  |
| 36 | `AdjustedPriceCeiling` | 最新发行价上限(元) | number(19,4) | ✓ | 16.5% |  |
| 37 | `AdjustedIssuePrice` | 最新发行价下限(元) | number(19,4) | ✓ | 25.51% |  |
| 38 | `PriceAdjustedDate` | 最新发行价调整日 | date | ✓ | 25.51% |  |
| 39 | `IssueVolCeiling` | 发行量上限(不超过)(股) | number(16,0) | ✓ | 75.15% |  |
| 40 | `IssueVolFloor` | 发行量下限(不少于)(股) | number(16,0) | ✓ | 23.77% |  |
| 41 | `AdjustedIssueVol` | 最新发行量上限(股) | number(16,0) | ✓ | 36.22% |  |
| 42 | `AdjustedVolFloor` | 最新发行量下限(股) | number(16,0) | ✓ | 16.76% |  |
| 43 | `PriceVolAdjustedDate` | 最新发行价及发行量调整日 | date | ✓ | 38.56% |  |
| 44 | `IssueStartDate` | 发行日期起始日 | date | ✓ | 50.54% |  |
| 45 | `IssueEndDate` | 发行日期截止日 | date | ✓ | 50.53% |  |
| 46 | `SubscriptionOfferDate` | 认购邀请书发送日 | date | ✓ | 20.93% |  |
| 47 | `AddSubscriptionSDate` | 追加认购起始日 | date | ✓ | 0.83% |  |
| 48 | `AddSubscriptionEDate` | 追加认购截止日, | date | ✓ | 0.78% |  |
| 49 | `UnderwritingStartDate` | 承销期起始日 | date | ✓ | 1.68% |  |
| 50 | `UnderwritingEndDate` | 承销期截止日 | date | ✓ | 1.66% |  |
| 51 | `IfExRightAShare` | A股除权与否 | number(10) | ✓ | 1.79% | A股除权与否（IfExRightAShare）：固定常量：1-是;0-否 |
| 52 | `RightRegDate` | 股权登记日 | date | ✓ | 50.39% |  |
| 53 | `ExRightDate` | 除权日 | date | ✓ | 0.24% |  |
| 54 | `SuspendStartDate` | 停牌时间起始日 | date | ✓ | 1.73% |  |
| 55 | `SuspendEndDate` | 停牌时间截止日 | date | ✓ | 1.73% |  |
| 56 | `PrefPlaDateH` | 老股东优先配售日期 | date | ✓ | 1.56% |  |
| 57 | `PrefPlaRatioH` | 老股东优先配售比例(10配X) | number(9,4) | ✓ | 1.71% |  |
| 58 | `PrefPlaApplyCodeH` | 老股东优先配售申购代码 | varchar2(10) | ✓ | 1.31% |  |
| 59 | `PrefPlaApplyAbbrNameH` | 老股东优先配售申购简称 | varchar2(20) | ✓ | 1.31% |  |
| 60 | `IssueDateOnline` | 上网公开发行日期 | date | ✓ | 1.79% |  |
| 61 | `ApplyCodeOnline` | 上网发行申购代码 | varchar2(10) | ✓ | 1.73% |  |
| 62 | `ApplyAbbrNameOnline` | 上网发行申购简称 | varchar2(20) | ✓ | 1.73% |  |
| 63 | `ApplyUnitOnline` | 上网发行申购单位(股) | number(10) | ✓ | 1.68% |  |
| 64 | `ApplyMaxOnline` | 上网发行申购上限(股) | number(16,0) | ✓ | 1.7% |  |
| 65 | `ApplyStartDateLPOffline` | 法人网下配售申购日期起始日 | date | ✓ | 1.52% |  |
| 66 | `ApplyEndDateLPOffline` | 法人网下配售申购日期截止日 | date | ✓ | 1.52% |  |
| 67 | `PayStartDateLPOffline` | 法人网下申购缴款开始日 | date | ✓ | 1.22% |  |
| 68 | `PlaPayEndDateLPOffline` | 法人网下申购缴款截止日 | date | ✓ | 1.27% |  |
| 69 | `ApplyUnitLPOffline` | 法人网下配售认购单位(股) | number(10) | ✓ | 1.45% |  |
| 70 | `ApplyMinLPOffline` | 法人网下配售申购下限(股) | number(10) | ✓ | 1.54% |  |
| 71 | `ApplyMaxLPOffline` | 法人网下配售申购上限(股) | number(16,0) | ✓ | 1.31% |  |
| 72 | `ValidApplyTimesLPOffline` | 法人网下配售有效申购次数限定 | number(10) | ✓ | 1.05% | 法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的... |
| 73 | `OddLotsTreatment` | 零股处理方式 | varchar2(255) | ✓ | 0.73% |  |
| 74 | `ParValue` | 每股面值(元) | number(19,4) | ✓ | 99.98% |  |
| 75 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 100.0% |  |
| 76 | `IssuePrice` | 每股发行价(元) | number(19,4) | ✓ | 50.54% |  |
| 77 | `DiscountRatePerShare` | 每股发行价折扣率(%) | number(19,8) | ✓ | 50.32% |  |
| 78 | `ActPriceBasePRatio` | 实施价格相对基准价格比例(%) | number(19,8) | ✓ | 48.39% |  |
| 79 | `StateSharesIssuePrice` | 国有股存量发行每股发行价(元) | number(19,4) | ✓ | 0.02% |  |
| 80 | `WeightedPERatio` | 加权平均发行市盈率(倍) | number(19,8) | ✓ | 0.13% |  |
| 81 | `DilutedPERatio` | 全面摊薄发行市盈率(倍) | number(19,8) | ✓ | 0.09% |  |
| 82 | `PERatioBeforeIssue` | 发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 0.0% |  |
| 83 | `PERatioAfterIssue` | 发行市盈率(按发行后总股本预测利润)(倍) | number(19,8) | ✓ | 0.0% |  |
| 84 | `IssueVol` | 发行量(股) | number(16,0) | ✓ | 50.55% |  |
| 85 | `StateSharesIssued` | 其中:国有股存量发行股数(股) | number(16,0) | ✓ | 0.02% |  |
| 86 | `TotalIssueMV` | 发行总市值(元) | number(19,4) | ✓ | 50.54% |  |
| 87 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 37.53% |  |
| 88 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 24.3% |  |
| 89 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 13.35% |  |
| 90 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 2.44% |  |
| 91 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 15.4% |  |
| 92 | `AssetAppraisalFee` | 2.1)资产评估费用(元) | number(19,4) | ✓ | 0.87% |  |
| 93 | `CPAFee` | 2.2)注册会计师费用(元) | number(19,4) | ✓ | 11.75% |  |
| 94 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.05% |  |
| 95 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 15.13% |  |
| 96 | `TotalAgentFee` | 4)中介机构费合计(元) | number(19,4) | ✓ | 0.34% |  |
| 97 | `OnlineIssueFee` | 5)上网发行费用(元) | number(19,4) | ✓ | 0.48% |  |
| 98 | `ScripFee` | 6)股票登记费用(元) | number(19,4) | ✓ | 8.86% |  |
| 99 | `OtherFee` | 7)其他费用(元) | number(19,4) | ✓ | 20.15% |  |
| 100 | `IssueCostPerShare` | 每股发行费用(元) | number(19,4) | ✓ | 37.53% |  |
| 101 | `PlannedProceeds` | 预计募集资金总额(元) | number(19,4) | ✓ | 91.09% |  |
| 102 | `SNIProceeds` | 增发新股募集资金总额(元) | number(19,4) | ✓ | 50.54% |  |
| 103 | `SNINetProceeds` | 增发新股募集资金净额(元) | number(19,4) | ✓ | 50.51% |  |
| 104 | `CurrencyProceeds` | 货币募集资金总额(元) | number(19,4) | ✓ | 36.84% |  |
| 105 | `NonCurrencyProceeds` | 非货币募集资金总额(元) | number(19,4) | ✓ | 13.93% |  |
| 106 | `AssetProceeds` | 其中:资产募集资金总额(元) | number(19,4) | ✓ | 13.74% |  |
| 107 | `DebtProceeds` | 其中:债权募集资金总额(元) | number(19,4) | ✓ | 0.05% |  |
| 108 | `StateSharesProceeds` | 国有股存量发行收入总额(元) | number(19,4) | ✓ | 0.02% |  |
| 109 | `StateSharesNetProceeds` | 国有股存量发行收入净额(元) | number(19,4) | ✓ | 0.02% |  |
| 110 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 50.51% |  |
| 111 | `DateToAccount` | 募集资金到帐时间 | date | ✓ | 50.5% |  |
| 112 | `VerificationDate` | 募集资金验资日 | date | ✓ | 12.58% |  |
| 113 | `ListAnnounceDate` | 增发新股上市公告日期 | date | ✓ | 50.54% |  |
| 114 | `NewShareListDate` | 增发股份上市日期 | date | ✓ | 50.51% |  |
| 115 | `OutstandingShares` | 本次上市流通股数(股) | number(16,0) | ✓ | 2.3% |  |
| 116 | `PutBackVol` | 网上网下回拨股数(股) | number(16,0) | ✓ | 0.13% |  |
| 117 | `PrefPlaVolHMax` | 原股东可配售股数(最多)(股) | number(16,0) | ✓ | 0.78% |  |
| 118 | `PrefPlaVolH` | 原股东优先配售股数(股) | number(16,0) | ✓ | 1.62% |  |
| 119 | `PrefPlaVolHOnline` | 原股东网上认购优先配售(股) | number(16,0) | ✓ | 1.55% |  |
| 120 | `PrefPlaVolHOffline` | 原股东网下认购优先配售(股) | number(16,0) | ✓ | 0.4% |  |
| 121 | `ValidApplyHNum` | 原股东有效申购户数(户) | number(10) | ✓ | 0.8% |  |
| 122 | `ValidApplyNumHOnline` | 原股东网上认购有效申购户数(户) | number(10) | ✓ | 0.62% |  |
| 123 | `ValidApplyNumHOffline` | 原股东网下认购有效申购户数(户) | number(10) | ✓ | 0.38% |  |
| 124 | `PublicOfferVolOnline` | 上网公开发行股数(股) | number(16,0) | ✓ | 1.73% |  |
| 125 | `ValidApplyVolOnline` | 上网有效申购总量(股) | number(16,0) | ✓ | 1.69% |  |
| 126 | `ValidApplyNumOnline` | 上网有效申购户数(户) | number(10) | ✓ | 1.5% |  |
| 127 | `OverSubsTimesOnline` | 上网超额认购倍数(倍) | number(9,4) | ✓ | 1.06% |  |
| 128 | `LotRateOnline` | 上网中签率 | number(18,15) | ✓ | 1.47% |  |
| 129 | `PlaVolLPOffline` | 法人网下配售股数(股) | number(16,0) | ✓ | 1.56% |  |
| 130 | `ValidApplyVolLPOffline` | 法人网下配售有效申购总量(股) | number(16,0) | ✓ | 1.49% |  |
| 131 | `ValidApplyNumLPOffline` | 法人网下配售有效申购户数(户) | number(10) | ✓ | 1.3% |  |
| 132 | `OverSubsTimesLPOffline` | 法人网下配售超额认购倍数(倍) | number(9,4) | ✓ | 1.14% |  |
| 133 | `LotRateLPOffline` | 法人网下配售中签率 | number(18,15) | ✓ | 1.27% |  |
| 134 | `APlaVolLPOffline` | A类法人网下配售股数(股) | number(16,0) | ✓ | 0.27% |  |
| 135 | `AValidApplyVolLPOffline` | A类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.27% |  |
| 136 | `AValidApplyNumLPOffline` | A类法人网下配售有效申购户数(户) | number(10) | ✓ | 0.27% |  |
| 137 | `ALotRateLPOffline` | A类法人网下配售中签率 | number(18,15) | ✓ | 0.26% |  |
| 138 | `BPlaVolLPOffline` | B类法人网下配售股数(股) | number(16,0) | ✓ | 0.24% |  |
| 139 | `BValidApplyVolLPOffline` | B类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.24% |  |
| 140 | `BValidApplyNumLPOffline` | B类法人网下配售有效申购户数(户) | number(16,0) | ✓ | 0.24% |  |
| 141 | `BLotRateLPOffline` | B类法人网下配售中签率 | number(18,15) | ✓ | 0.23% |  |
| 142 | `TailoredPlaVolLP` | 法人定向配售股数(股) | number(16,0) | ✓ | 48.74% |  |
| 143 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 2.02% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 ... |
| 144 | `UnderwriterBoughtVol` | 余股包销数量(股) | number(16,0) | ✓ | 1.09% |  |
| 145 | `SchemeChangePublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 146 | `ChangeStatement` | 方案变动说明 | varchar2(2000) | ✓ | 77.18% |  |
| 147 | `ChangeType` | 方案变动类型 | number(10) | ✓ | 77.18% | 方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案... |
| 148 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 149 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 150 | `JSID` | JSID | number(19) | ✗ |  |  |
| 151 | `ReferringPrice` | 承销商指导价格(元) | number(19,4) | ✓ | 0.0% |  |
| 152 | `OverAllotmentOption` | 超额配售权(股) | number(16,0) | ✓ | 0.01% |  |
| 153 | `STAQNETPlaStartDate` | STAQ/NET定向配售时间起始日 | date | ✓ | 0.0% |  |
| 154 | `STAQNETPlaEndDate` | STAQ/NET定向配售时间截止日 | date | ✓ | 0.0% |  |
| 155 | `STAQNETPlaRatio` | STAQ/NET定向配售比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 156 | `QuotationUnitOnline` | 网上申购报价单位(元) | number(19,4) | ✓ | 0.52% |  |
| 157 | `QuotationUnitOffline` | 网下申购报价单位(元) | number(19,4) | ✓ | 0.62% |  |
| 158 | `FreezedMoney` | 冻结资金(元) | number(19,4) | ✓ | 0.08% |  |
| 159 | `PlaVolHOffline` | 原股东网下配售股数(股) | number(16,0) | ✓ | 0.02% |  |
| 160 | `ValidPlaVolHOffline` | 原股东网下配售有效申购总量(股) | number(16,0) | ✓ | 0.02% |  |
| 161 | `ValidPlaNumHOffline` | 原股东网下配售有效申购户数(户) | number(10) | ✓ | 0.02% |  |
| 162 | `LotRateHOffline` | 原股东网下配售中签率 | number(18,15) | ✓ | 0.02% |  |
| 163 | `PlaVolF` | 投资基金配售股数(股) | number(16,0) | ✓ | 0.13% |  |
| 164 | `PlaVolSTAQNET` | STAQ/NET定向配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 165 | `EarningForecastYear` | 盈利预测年度 | date | ✓ | 0.34% |  |
| 166 | `MainIncomeForecast` | 主营业务收入预测(元) | number(19,4) | ✓ | 0.34% |  |
| 167 | `NetProfitForecast` | 净利润预测(元) | number(19,4) | ✓ | 0.32% |  |
| 168 | `DilutedEPSForecast` | 全面摊薄每股盈利预测(元) | number(19,4) | ✓ | 0.11% |  |
| 169 | `ApplyStartDateF` | 基金配售申购日期起始日 | date | ✓ | 0.13% |  |
| 170 | `ApplyEndDateF` | 基金配售申购日期截止日 | date | ✓ | 0.14% |  |
| 171 | `PayStartDateF` | 基金配售缴款开始日 | date | ✓ | 0.02% |  |
| 172 | `PayEndDateF` | 基金配售缴款截止日 | date | ✓ | 0.04% |  |
| 173 | `PrefAllotmentF` | 投资基金配售限额(股) | number(16,0) | ✓ | 0.0% |  |
| 174 | `PrefAllotmentSingleF` | 单个基金配售限额(股) | number(16,0) | ✓ | 0.0% |  |
| 175 | `ApplyDate` | 申购日1 | date | ✓ | 0.38% |  |

## 字段说明

### EventProcedureCode (事件进程)

事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。

### IssueType (增发类别)

增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (21,22,23)，得到增发类别的具体描述：21-非公开增发，22-公开增发，23-非公开增发配套融资。

### IfSummaryProcedure (是否简易程序)

是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。

### IfEffected (是否有效)

	
是否有效（IfEffected）的具体描述：1-是（代表增发处于正常有效状态），2-否（代表增发处于已终止或否决等无效状态）。

### StockType (增发A股类型)

增发A股类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1239 AND DM IN (1,2)，得到增发A股类型的具体描述：1-A股增发A股，2-B股增发A股。

### SubscribeMethod (认购方式)

认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

### LargeSHSubMethod (控股股东认购方式)

控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到控股股东认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

### IfExRightAShare (A股除权与否)

A股除权与否（IfExRightAShare）：固定常量：1-是;0-否

### ValidApplyTimesLPOffline (法人网下配售有效申购次数限定)

法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的DM字段关联，令LB = 1195，得到法人网下配售有效申购次数限定的具体描述：1-多次申购，2-一次申购。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 AND DM IN (1,2,3,4)，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销。

## SQL示例

```sql
-- 查询 A股增发 数据
SELECT *
FROM dz_ashareseasonednewissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
