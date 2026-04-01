# LC_AShareSeasonedNewIssue

**中文名**: A股增发

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AShareSeasonedNewIssue` |
| MySQL表名 | `lc_ashareseasonednewissue` |
| 中文名 | A股增发 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 175 |
| 版本 | 1.16 |

## 表描述

1.收录A股增发A股、B股增发A股、H股增发A股等的明细情况，包括历次增发预案、进程日期、预案有效期、发行属性、发行价区间、发行量区间、发行日期、上网发行情况、网下配售申购情况和募集资金与费用等内容。
2.数据范围：1991-08-17至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EventProcedureCode` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 164... |
| 5 | `IssueType` | 增发类别 | number(10) | ✓ | 100.0% | 增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM ... |
| 6 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效（IfEffected）的具体描述：1-是（代表增发处于正常有效状态），2-否（代表增发处于已终止或否决等无效状... |
| 7 | `ProjInfoSource` | 预案信息来源 | varchar2(200) | ✓ | 89.69% |  |
| 8 | `IssueResultInfoSource` | 发行结果信息来源 | varchar2(200) | ✓ | 52.14% |  |
| 9 | `AdvanceDate` | 首次预案公布日期 | date | ✓ | 89.67% |  |
| 10 | `LatestAdvanceDate` | 最新预案公布日期 | date | ✓ | 89.67% |  |
| 11 | `SMDeciPublDate` | 最新股东大会决议公告日期 | date | ✓ | 88.34% |  |
| 12 | `IntentLetterPublDate` | 增发新股意向书发布日期 | date | ✓ | 1.77% |  |
| 13 | `ProspectusPublDate` | 增发新股说明书发布日期 | date | ✓ | 0.2% |  |
| 14 | `SASACApprovalPublDate` | 国资委通过公告日 | date | ✓ | 13.52% |  |
| 15 | `CSRCApprovalPublDate` | 证监会批准公告日 | date | ✓ | 53.68% |  |
| 16 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 86.46% |  |
| 17 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 75.23% |  |
| 18 | `StockType` | 增发A股类型 | number(10) | ✓ | 100.0% | 增发A股类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1239 AND D... |
| 19 | `PriceIntervalStatement` | 发行价区间确定方式说明 | varchar2(255) | ✓ | 99.7% |  |
| 20 | `PricingModel` | 发行价定价方式 | number(10) | ✓ |  |  |
| 21 | `RationModel` | 发行量定量方式 | number(10) | ✓ |  |  |
| 22 | `IssueMethod` | 发行方式 | number(10) | ✓ |  |  |
| 23 | `IssuePurpose` | 增发目的 | varchar2(255) | ✓ | 99.97% |  |
| 24 | `ISOBTypeCode` | 发行对象类型 | number(10) | ✓ |  |  |
| 25 | `IssueObject` | 发行对象 | varchar2(255) | ✓ | 99.96% |  |
| 26 | `SubscribeMethod` | 认购方式 | number(10) | ✓ | 99.95% | 认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得... |
| 27 | `LargeSHSubMethod` | 控股股东认购方式 | number(10) | ✓ | 21.97% | 控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2... |
| 28 | `LargeSHSubsSum` | 控股股东认购数量(股) | number(16,0) | ✓ | 15.68% |  |
| 29 | `LargeSHSubsRatio` | 控股股东认购比例(%) | number(19,8) | ✓ | 17.91% |  |
| 30 | `IssuePriceCeiling` | 发行价上限(最高价)(元) | number(19,4) | ✓ | 42.42% |  |
| 31 | `IssuePriceFloor` | 发行价下限(最低价)(元) | number(19,4) | ✓ | 59.88% |  |
| 32 | `OrgPriceBasePRatio` | 预案价格相对基准价格比例(%) | number(19,8) | ✓ | 95.32% |  |
| 33 | `PricingBaseDate` | 定价基准日 | date | ✓ | 75.21% |  |
| 34 | `PricingBaseDateDesc` | 定价基准日描述 | varchar2(100) | ✓ | 93.21% |  |
| 35 | `AdjustedPriceCeiling` | 最新发行价上限(元) | number(19,4) | ✓ | 16.88% |  |
| 36 | `AdjustedIssuePrice` | 最新发行价下限(元) | number(19,4) | ✓ | 26.36% |  |
| 37 | `PriceAdjustedDate` | 最新发行价调整日 | date | ✓ | 26.36% |  |
| 38 | `IssueVolCeiling` | 发行量上限(不超过)(股) | number(16,0) | ✓ | 77.71% |  |
| 39 | `IssueVolFloor` | 发行量下限(不少于)(股) | number(16,0) | ✓ | 24.93% |  |
| 40 | `PriceVolAdjustedDate` | 最新发行价及发行量调整日 | date | ✓ | 39.68% |  |
| 41 | `AdjustedIssueVol` | 最新发行量上限(股) | number(16,0) | ✓ | 37.24% |  |
| 42 | `AdjustedVolFloor` | 最新发行量下限(股) | number(16,0) | ✓ | 17.16% |  |
| 43 | `IssueStartDate` | 发行日期起始日 | date | ✓ | 52.15% |  |
| 44 | `IssueEndDate` | 发行日期截止日 | date | ✓ | 52.13% |  |
| 45 | `SubscriptionOfferDate` | 认购邀请书发送日 | date | ✓ | 21.32% |  |
| 46 | `AddSubscriptionSDate` | 追加认购起始日 | date | ✓ | 0.81% |  |
| 47 | `AddSubscriptionEDate` | 追加认购截止日 | date | ✓ | 0.78% |  |
| 48 | `UnderwritingStartDate` | 承销期起始日 | date | ✓ | 1.77% |  |
| 49 | `UnderwritingEndDate` | 承销期截止日 | date | ✓ | 1.75% |  |
| 50 | `IfExRightAShare` | A股除权与否 | number(10) | ✓ | 1.88% | A股除权与否（IfExRightAShare）：固定常量：1->是0->否 |
| 51 | `RightRegDate` | 股权登记日 | date | ✓ | 51.98% |  |
| 52 | `ExRightDate` | 除权日 | date | ✓ | 0.25% |  |
| 53 | `SuspendStartDate` | 停牌时间起始日 | date | ✓ | 1.82% |  |
| 54 | `SuspendEndDate` | 停牌时间截止日 | date | ✓ | 1.82% |  |
| 55 | `PrefPlaDateH` | 老股东优先配售日期 | date | ✓ | 1.64% |  |
| 56 | `PrefPlaRatioH` | 老股东优先配售比例(10配X) | number(9,4) | ✓ | 1.8% |  |
| 57 | `PrefPlaApplyCodeH` | 老股东优先配售申购代码 | varchar2(10) | ✓ | 1.38% |  |
| 58 | `PrefPlaApplyAbbrNameH` | 老股东优先配售申购简称 | varchar2(20) | ✓ | 1.38% |  |
| 59 | `IssueDateOnline` | 上网公开发行日期 | date | ✓ | 1.88% |  |
| 60 | `ApplyCodeOnline` | 上网发行申购代码 | varchar2(10) | ✓ | 1.82% |  |
| 61 | `ApplyAbbrNameOnline` | 上网发行申购简称 | varchar2(20) | ✓ | 1.82% |  |
| 62 | `ApplyUnitOnline` | 上网发行申购单位(股) | number(10) | ✓ | 1.77% |  |
| 63 | `ApplyMaxOnline` | 上网发行申购上限(股) | number(16,0) | ✓ | 1.78% |  |
| 64 | `ApplyStartDateLPOffline` | 法人网下配售申购日期起始日 | date | ✓ | 1.6% |  |
| 65 | `ApplyEndDateLPOffline` | 法人网下配售申购日期截止日 | date | ✓ | 1.6% |  |
| 66 | `PayStartDateLPOffline` | 法人网下申购缴款开始日 | date | ✓ | 1.28% |  |
| 67 | `PlaPayEndDateLPOffline` | 法人网下申购缴款截止日 | date | ✓ | 1.33% |  |
| 68 | `ApplyUnitLPOffline` | 法人网下配售认购单位(股) | number(10) | ✓ | 1.52% |  |
| 69 | `ApplyMinLPOffline` | 法人网下配售申购下限(股) | number(10) | ✓ | 1.62% |  |
| 70 | `ApplyMaxLPOffline` | 法人网下配售申购上限(股) | number(16,0) | ✓ | 1.38% |  |
| 71 | `ValidApplyTimesLPOffline` | 法人网下配售有效申购次数限定 | number(10) | ✓ | 1.11% | 法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的... |
| 72 | `OddLotsTreatment` | 零股处理方式 | varchar2(255) | ✓ | 0.77% |  |
| 73 | `ParValue` | 每股面值(元) | number(19,4) | ✓ | 100.0% |  |
| 74 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 100.0% |  |
| 75 | `IssuePrice` | 每股发行价(元) | number(19,4) | ✓ | 52.14% |  |
| 76 | `DiscountRatePerShare` | 每股发行价折扣率(%) | number(19,8) | ✓ | 51.92% |  |
| 77 | `ActPriceBasePRatio` | 实施价格相对基准价格比例(%) | number(19,8) | ✓ | 49.89% |  |
| 78 | `StateSharesIssuePrice` | 国有股存量发行每股发行价(元) | number(19,4) | ✓ | 0.02% |  |
| 79 | `WeightedPERatio` | 加权平均发行市盈率(倍) | float(23) | ✓ | 0.13% |  |
| 80 | `DilutedPERatio` | 全面摊薄发行市盈率(倍) | float(23) | ✓ | 0.1% |  |
| 81 | `PERatioBeforeIssue` | 发行市盈率(按发行前总股本)(倍) | float(23) | ✓ | 0.0% |  |
| 82 | `PERatioAfterIssue` | 发行市盈率(按发行后总股本预测利润)(倍) | float(23) | ✓ | 0.0% |  |
| 83 | `IssueVol` | 发行量(股) | number(16,0) | ✓ | 52.16% |  |
| 84 | `StateSharesIssued` | 其中:国有股存量发行股数(股) | number(16,0) | ✓ | 0.02% |  |
| 85 | `TotalIssueMV` | 发行总市值(元) | number(19,4) | ✓ | 52.14% |  |
| 86 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 38.56% |  |
| 87 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 24.65% |  |
| 88 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 13.92% |  |
| 89 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 2.47% |  |
| 90 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 15.32% |  |
| 91 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 11.58% |  |
| 92 | `AssetAppraisalFee` | 2.2)资产评估费用(元) | number(19,4) | ✓ | 0.89% |  |
| 93 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.06% |  |
| 94 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 15.04% |  |
| 95 | `TotalAgentFee` | 4)中介机构费合计(元) | number(19,4) | ✓ | 0.36% |  |
| 96 | `OnlineIssueFee` | 5)上网发行费用(元) | number(19,4) | ✓ | 0.49% |  |
| 97 | `ScripFee` | 6)股票登记费用(元) | number(19,4) | ✓ | 9.12% |  |
| 98 | `OtherFee` | 7)其他费用(元) | number(19,4) | ✓ | 20.37% |  |
| 99 | `IssueCostPerShare` | 每股发行费用(元) | number(19,4) | ✓ | 38.55% |  |
| 100 | `PlannedProceeds` | 预计募集资金总额(元) | number(19,4) | ✓ | 91.03% |  |
| 101 | `SNIProceeds` | 实际募集资金总额(元) | number(19,4) | ✓ | 52.14% |  |
| 102 | `CurrencyProceeds` | 货币募集资金总额(元) | number(19,4) | ✓ | 37.83% |  |
| 103 | `NonCurrencyProceeds` | 非货币募集资金总额(元) | number(19,4) | ✓ | 14.56% |  |
| 104 | `AssetProceeds` | 其中:资产募集资金总额(元) | number(19,4) | ✓ | 14.37% |  |
| 105 | `DebtProceeds` | 其中:债权募集资金总额(元) | number(19,4) | ✓ | 0.06% |  |
| 106 | `SNINetProceeds` | 实际募集资金净额(元) | number(19,4) | ✓ | 52.12% |  |
| 107 | `StateSharesProceeds` | 国有股存量发行收入总额(元) | number(19,4) | ✓ | 0.02% |  |
| 108 | `StateSharesNetProceeds` | 国有股存量发行收入净额(元) | number(19,4) | ✓ | 0.02% |  |
| 109 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 52.12% |  |
| 110 | `VerificationDate` | 募集资金验资日 | date | ✓ | 12.24% |  |
| 111 | `DateToAccount` | 募集资金到帐时间 | date | ✓ | 52.11% |  |
| 112 | `ListAnnounceDate` | 增发新股上市公告日期 | date | ✓ | 52.14% |  |
| 113 | `NewShareListDate` | 增发股份上市日期 | date | ✓ | 52.12% |  |
| 114 | `OutstandingShares` | 本次上市流通股数(股) | number(16,0) | ✓ | 2.42% |  |
| 115 | `PutBackVol` | 网上网下回拨股数(股) | number(16,0) | ✓ | 0.13% |  |
| 116 | `PrefPlaVolHMax` | 原股东可配售股数(最多)(股) | number(16,0) | ✓ | 0.82% |  |
| 117 | `PrefPlaVolH` | 原股东优先配售股数(股) | number(16,0) | ✓ | 1.7% |  |
| 118 | `PrefPlaVolHOnline` | 原股东网上认购优先配售(股) | number(16,0) | ✓ | 1.63% |  |
| 119 | `PrefPlaVolHOffline` | 原股东网下认购优先配售(股) | number(16,0) | ✓ | 0.42% |  |
| 120 | `ValidApplyHNum` | 原股东有效申购户数(户) | number(10) | ✓ | 0.85% |  |
| 121 | `ValidApplyNumHOnline` | 原股东网上认购有效申购户数(户) | number(10) | ✓ | 0.65% |  |
| 122 | `ValidApplyNumHOffline` | 原股东网下认购有效申购户数(户) | number(10) | ✓ | 0.4% |  |
| 123 | `PublicOfferVolOnline` | 上网公开发行股数(股) | number(16,0) | ✓ | 1.82% |  |
| 124 | `ValidApplyVolOnline` | 上网有效申购总量(股) | number(16,0) | ✓ | 1.77% |  |
| 125 | `ValidApplyNumOnline` | 上网有效申购户数(户) | number(10) | ✓ | 1.58% |  |
| 126 | `OverSubsTimesOnline` | 上网超额认购倍数(倍) | number(9,4) | ✓ | 1.12% |  |
| 127 | `LotRateOnline` | 上网中签率 | number(18,15) | ✓ | 1.54% |  |
| 128 | `PlaVolLPOffline` | 法人网下配售股数(股) | number(16,0) | ✓ | 1.64% |  |
| 129 | `ValidApplyVolLPOffline` | 法人网下配售有效申购总量(股) | number(16,0) | ✓ | 1.57% |  |
| 130 | `ValidApplyNumLPOffline` | 法人网下配售有效申购户数(户) | number(10) | ✓ | 1.37% |  |
| 131 | `OverSubsTimesLPOffline` | 法人网下配售超额认购倍数(倍) | number(9,4) | ✓ | 1.2% |  |
| 132 | `LotRateLPOffline` | 法人网下配售中签率 | number(18,15) | ✓ | 1.33% |  |
| 133 | `APlaVolLPOffline` | A类法人网下配售股数(股) | number(16,0) | ✓ | 0.28% |  |
| 134 | `AValidApplyVolLPOffline` | A类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.28% |  |
| 135 | `AValidApplyNumLPOffline` | A类法人网下配售有效申购户数(户) | number(10) | ✓ | 0.28% |  |
| 136 | `ALotRateLPOffline` | A类法人网下配售中签率 | number(18,15) | ✓ | 0.27% |  |
| 137 | `BPlaVolLPOffline` | B类法人网下配售股数(股) | number(16,0) | ✓ | 0.25% |  |
| 138 | `BValidApplyVolLPOffline` | B类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.25% |  |
| 139 | `BValidApplyNumLPOffline` | B类法人网下配售有效申购户数(户) | number(16,0) | ✓ | 0.25% |  |
| 140 | `BLotRateLPOffline` | B类法人网下配售中签率 | number(18,15) | ✓ | 0.25% |  |
| 141 | `TailoredPlaVolLP` | 法人定向配售股数(股) | number(16,0) | ✓ | 50.25% |  |
| 142 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 2.12% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 ... |
| 143 | `UnderwriterBoughtVol` | 余股包销数量(股) | number(16,0) | ✓ | 1.15% |  |
| 144 | `SchemeChangePublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 145 | `ChangeStatement` | 方案变动说明 | varchar2(2000) | ✓ | 79.16% |  |
| 146 | `ChangeType` | 方案变动类型 | number(10) | ✓ | 79.16% | 方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案... |
| 147 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 148 | `JSID` | JSID | number(19) | ✗ |  |  |
| 149 | `ReferringPrice` | 承销商指导价格(元) | number(19,4) | ✓ | 0.0% |  |
| 150 | `OverAllotmentOption` | 超额配售权(股) | number(16,0) | ✓ | 0.01% |  |
| 151 | `STAQNETPlaStartDate` | STAQ/NET定向配售时间起始日 | date | ✓ | 0.0% |  |
| 152 | `STAQNETPlaEndDate` | STAQ/NET定向配售时间截止日 | date | ✓ | 0.0% |  |
| 153 | `STAQNETPlaRatio` | STAQ/NET定向配售比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 154 | `QuotationUnitOnline` | 网上申购报价单位(元) | number(19,4) | ✓ | 0.55% |  |
| 155 | `QuotationUnitOffline` | 网下申购报价单位(元) | number(19,4) | ✓ | 0.65% |  |
| 156 | `FreezedMoney` | 冻结资金(元) | number(19,4) | ✓ | 0.08% |  |
| 157 | `PlaVolHOffline` | 原股东网下配售股数(股) | number(16,0) | ✓ | 0.02% |  |
| 158 | `ValidPlaVolHOffline` | 原股东网下配售有效申购总量(股) | number(16,0) | ✓ | 0.02% |  |
| 159 | `ValidPlaNumHOffline` | 原股东网下配售有效申购户数(户) | number(10) | ✓ | 0.02% |  |
| 160 | `LotRateHOffline` | 原股东网下配售中签率 | number(18,15) | ✓ | 0.02% |  |
| 161 | `PlaVolF` | 投资基金配售股数(股) | number(16,0) | ✓ | 0.14% |  |
| 162 | `PlaVolSTAQNET` | STAQ/NET定向配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 163 | `EarningForecastYear` | 盈利预测年度 | date | ✓ | 0.36% |  |
| 164 | `MainIncomeForecast` | 主营业务收入预测(元) | number(19,4) | ✓ | 0.35% |  |
| 165 | `NetProfitForecast` | 净利润预测(元) | number(19,4) | ✓ | 0.34% |  |
| 166 | `DilutedEPSForecast` | 全面摊薄每股盈利预测(元) | number(19,4) | ✓ | 0.12% |  |
| 167 | `ApplyStartDateF` | 基金配售申购日期起始日 | date | ✓ | 0.14% |  |
| 168 | `ApplyEndDateF` | 基金配售申购日期截止日 | date | ✓ | 0.15% |  |
| 169 | `PayStartDateF` | 基金配售缴款开始日 | date | ✓ | 0.02% |  |
| 170 | `PayEndDateF` | 基金配售缴款截止日 | date | ✓ | 0.04% |  |
| 171 | `PrefAllotmentF` | 投资基金配售限额(股) | number(16,0) | ✓ | 0.0% |  |
| 172 | `PrefAllotmentSingleF` | 单个基金配售限额(股) | number(16,0) | ✓ | 0.0% |  |
| 173 | `IfSummaryProcedure` | 是否简易程序 | number(10) | ✓ | 11.54% | 是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。 |
| 174 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 175 | `ApplyDate` | 申购日1 | date | ✓ | 0.33% |  |

## 字段说明

### EventProcedureCode (事件进程)

事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。

### IssueType (增发类别)

增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (21,22,23)，得到增发类别的具体描述：21-非公开增发，22-公开增发，23-非公开增发配套融资。

### IfEffected (是否有效)

是否有效（IfEffected）的具体描述：1-是（代表增发处于正常有效状态），2-否（代表增发处于已终止或否决等无效状态）。

### StockType (增发A股类型)

增发A股类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1239 AND DM IN (1,2)，得到增发A股类型的具体描述：1-A股增发A股，2-B股增发A股。

### SubscribeMethod (认购方式)

认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

### LargeSHSubMethod (控股股东认购方式)

控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到控股股东认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

### IfExRightAShare (A股除权与否)

A股除权与否（IfExRightAShare）：固定常量：1->是0->否

### ValidApplyTimesLPOffline (法人网下配售有效申购次数限定)

法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的DM字段关联，令LB = 1195，得到法人网下配售有效申购次数限定的具体描述：1-多次申购，2-一次申购。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 AND DM IN (1,2,3,4)，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销。

### ChangeType (方案变动类型)

方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。

## SQL示例

```sql
-- 查询 A股增发 数据
SELECT *
FROM lc_ashareseasonednewissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
