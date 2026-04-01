# LC_STIBNewIssue

**中文名**: 科创板增发

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBNewIssue` |
| MySQL表名 | `lc_stibnewissue` |
| 中文名 | 科创板增发 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 134 |
| 版本 | 1.08 |

## 表描述

1、内容说明：收录科创板增发A股的明细情况，包括历次增发预案、进程日期、预案有效期、发行属性、发行价区间、发行量区间、发行日期、上网发行情况、网下配售申购情况和募集资金与费用等内容。
2、数据范围：2019年至今
3、信息来源：增发股票预案、增发上市公告书等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到... |
| 5 | `IssueType` | 增发类别 | number(10) | ✗ | 100.0% | 增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM ... |
| 6 | `IfSummaryProcedure` | 是否简易程序 | number(10) | ✓ | 62.58% | 是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。 |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)的具体描述: 1-是，2-否。是代表本次增发方案仍在正常实施中或实施完成，否代表本次增发... |
| 8 | `AdvanceDate` | 首次预案公布日期 | date | ✓ | 44.11% |  |
| 9 | `LatestAdvanceDate` | 最新预案公布日期 | date | ✓ | 44.11% |  |
| 10 | `SMDeciPublDate` | 最新股东大会决议公告日期 | date | ✓ | 90.76% |  |
| 11 | `IntentLetterPublDate` | 增发新股意向书发布日期 | date | ✓ | 0.0% |  |
| 12 | `ProspectusPublDate` | 增发新股说明书发布日期 | date | ✓ | 0.0% |  |
| 13 | `SASACApprovalPublD` | 国资委通过公告日 | date | ✓ | 0.8% |  |
| 14 | `ExApprovalPublDate` | 交易所审核通过日 | date | ✓ | 20.86% |  |
| 15 | `CSRCApprovalPublDate` | 证监会批准公告日 | date | ✓ | 20.54% |  |
| 16 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 86.94% |  |
| 17 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 29.3% |  |
| 18 | `IssueStartDate` | 发行日期起始日 | date | ✓ | 19.43% |  |
| 19 | `IssueEndDate` | 发行日期截止日 | date | ✓ | 19.43% |  |
| 20 | `SubscriptionOfferDate` | 认购邀请书发送日 | date | ✓ | 13.38% |  |
| 21 | `AddSubscriptionSDate` | 追加认购起始日 | date | ✓ | 1.11% |  |
| 22 | `AddSubscriptionEDate` | 追加认购截止日 | date | ✓ | 0.8% |  |
| 23 | `RightRegDate` | 股权登记日 | date | ✓ | 19.43% |  |
| 24 | `ExRightDate` | 除权日 | date | ✓ | 0.0% |  |
| 25 | `IssueDateOnline` | 上网公开发行日期 | date | ✓ | 0.0% |  |
| 26 | `ApplyStDateLPOffline` | 法人网下配售申购日期起始日 | date | ✓ | 0.0% |  |
| 27 | `ApplyEndDateLPOffline` | 法人网下配售申购日期截止日 | date | ✓ | 0.0% |  |
| 28 | `PlaPayStDateLPOffline` | 法人网下申购缴款开始日 | date | ✓ | 0.0% |  |
| 29 | `PlaPayEndDateLPOffline` | 法人网下申购缴款截止日 | date | ✓ | 0.0% |  |
| 30 | `ListAnnounceDate` | 增发新股上市公告日期 | date | ✓ | 19.43% |  |
| 31 | `NewShareListDate` | 增发股份上市日期 | date | ✓ | 19.43% |  |
| 32 | `PriceIntervalStatement` | 发行价区间确定方式说明 | varchar2(255) | ✓ | 100.0% |  |
| 33 | `PricingModel` | 发行价定价方式 | number(10) | ✓ |  | 发行价定价方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1019，得... |
| 34 | `RationModel` | 发行量定量方式 | number(10) | ✓ |  | 发行量定量方式(RationModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1020，得到... |
| 35 | `IssueMethod` | 发行方式明细 | number(10) | ✓ |  | 发行方式明细(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1018，得到发... |
| 36 | `IssuePurpose` | 增发目的 | varchar2(255) | ✓ | 100.0% |  |
| 37 | `ISOBTypeCode` | 发行对象类型 | number(10) | ✓ |  | 发行对象类型(ISOBTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1639，得到... |
| 38 | `IssueObject` | 发行对象 | varchar2(255) | ✓ | 100.0% |  |
| 39 | `SubscribeMethod` | 认购方式 | number(10) | ✓ | 100.0% | 认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得... |
| 40 | `LargeSHSubMethod` | 控股股东认购方式 | number(10) | ✓ | 4.14% | 控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2... |
| 41 | `LargeSHSubsSum` | 控股股东认购数量(股) | number(16,0) | ✓ | 2.07% |  |
| 42 | `LargeSHSubsRatio` | 控股股东认购比例(%) | number(19,8) | ✓ | 2.87% |  |
| 43 | `AdjustedPriceCeiling` | 最新发行价上限(元) | number(19,4) | ✓ | 9.08% |  |
| 44 | `AdjustedPriceFloor` | 最新发行价下限(元) | number(19,4) | ✓ | 9.08% |  |
| 45 | `IssuePriceCeiling` | 初始发行价上限(最高价)(元) | number(19,4) | ✓ | 14.17% |  |
| 46 | `IssuePriceFloor` | 初始发行价下限(最低价)(元) | number(19,4) | ✓ | 14.17% |  |
| 47 | `OrgPriceBasePRatio` | 预案价格相对基准价格比例(%) | number(19,8) | ✓ | 100.0% |  |
| 48 | `PricingBaseDate` | 定价基准日 | date | ✓ | 30.1% |  |
| 49 | `PricingBaseDateDesc` | 定价基准日描述 | varchar2(100) | ✓ | 97.93% |  |
| 50 | `AdjustedVolCeiling` | 最新发行量上限(股) | number(16,0) | ✓ | 16.56% |  |
| 51 | `AdjustedVolFloor` | 最新发行量下限(股) | number(16,0) | ✓ | 8.92% |  |
| 52 | `IssueVolCeiling` | 初始发行量上限(不超过)(股) | number(16,0) | ✓ | 25.48% |  |
| 53 | `IssueVolFloor` | 初始发行量下限(不少于)(股) | number(16,0) | ✓ | 1.27% |  |
| 54 | `PrefPlaDateH` | 老股东优先配售日期 | date | ✓ | 0.0% |  |
| 55 | `PrefPlaRatioH` | 老股东优先配售比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 56 | `PrefPlaApplyCodeH` | 老股东优先配售申购代码 | varchar2(10) | ✓ | 0.0% |  |
| 57 | `PrefPlaApplyAbbrNameH` | 老股东优先配售申购简称 | varchar2(20) | ✓ | 0.0% |  |
| 58 | `ApplyCodeOnline` | 上网发行申购代码 | varchar2(10) | ✓ | 0.0% |  |
| 59 | `ApplyAbbrNameOnline` | 上网发行申购简称 | varchar2(20) | ✓ | 0.0% |  |
| 60 | `ApplyUnitOnline` | 上网发行申购单位(股) | number(10) | ✓ | 0.0% |  |
| 61 | `ApplyMaxOnline` | 上网发行申购上限(股) | number(16,0) | ✓ | 0.0% |  |
| 62 | `ApplyUnitLPOffline` | 法人网下配售认购单位(股) | number(10) | ✓ | 0.0% |  |
| 63 | `ApplyMinLPOffline` | 法人网下配售申购下限(股) | number(16,0) | ✓ | 0.0% |  |
| 64 | `ApplyMaxLPOffline` | 法人网下配售申购上限(股) | number(16,0) | ✓ | 0.0% |  |
| 65 | `ValidTimesLPOffline` | 法人网下配售有效申购次数限定 | number(10) | ✓ | 0.0% | 法人网下配售有效申购次数限定(ValidTimesLPOffline)与(CT_SystemConst)表中的DM字段关... |
| 66 | `OddLotsTreatment` | 零股处理方式 | number(10) | ✓ | 0.0% | 零股处理方式(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 121... |
| 67 | `ParValue` | 每股面值(元) | number(19,4) | ✓ | 99.68% |  |
| 68 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 100.0% |  |
| 69 | `IssuePrice` | 每股发行价(元) | number(19,4) | ✓ | 19.43% |  |
| 70 | `DiscountRatePerShare` | 每股发行价折扣率(%) | number(19,8) | ✓ | 19.43% |  |
| 71 | `ActPriceBasePRatio` | 实施价格相对基准价格比例(%) | number(19,8) | ✓ | 19.43% |  |
| 72 | `WeightedPERatio` | 加权平均发行市盈率(倍) | number(19,8) | ✓ | 0.0% |  |
| 73 | `DilutedPERatio` | 全面摊薄发行市盈率(倍) | number(19,8) | ✓ | 0.0% |  |
| 74 | `PERatioBeforeIssue` | 发行市盈率(按发行前总股本)(倍) | number(19,8) | ✓ | 0.0% |  |
| 75 | `PERatioAfterIssue` | 发行市盈率(按发行后总股本预测利润)(倍) | number(19,8) | ✓ | 0.0% |  |
| 76 | `IssueVol` | 发行量(股) | number(16,0) | ✓ | 19.43% |  |
| 77 | `TotalIssueMV` | 发行总市值(元) | number(19,4) | ✓ | 19.43% |  |
| 78 | `PutBackVol` | 网上网下回拨股数(股) | number(16,0) | ✓ | 0.0% |  |
| 79 | `PlannedProceeds` | 预计募集资金总额(元) | number(19,4) | ✓ | 92.2% |  |
| 80 | `SNIProceeds` | 实际募集资金总额(元) | number(19,4) | ✓ | 19.43% |  |
| 81 | `CurrencyProceeds` | 货币募集资金总额(元) | number(19,4) | ✓ | 17.68% |  |
| 82 | `NonCurrencyProceeds` | 非货币募集资金总额(元) | number(19,4) | ✓ | 1.75% |  |
| 83 | `AssetProceeds` | 其中:资产募集资金总额(元) | number(19,4) | ✓ | 1.59% |  |
| 84 | `DebtProceeds` | 其中:债权募集资金总额(元) | number(19,4) | ✓ | 0.0% |  |
| 85 | `IssueCost` | 发行费用总额(含税)(元) | number(19,4) | ✓ | 17.68% |  |
| 86 | `InputTax` | 其中:进项税额(元) | number(19,4) | ✓ | 4.62% |  |
| 87 | `SNINetProceedsVAT` | 实际募集资金净额(含税)(元) | number(19,4) | ✓ | 19.43% |  |
| 88 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 19.43% |  |
| 89 | `VerificationDate` | 募集资金验资日 | date | ✓ | 19.11% |  |
| 90 | `DateToAccount` | 募集资金到帐时间 | date | ✓ | 19.43% |  |
| 91 | `PrefPlaVolHMax` | 原股东可配售股数(最多)(股) | number(16,0) | ✓ | 0.0% |  |
| 92 | `PrefPlaVolH` | 原股东优先配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 93 | `PrefPlaVolHOnline` | 原股东网上认购优先配售(股) | number(16,0) | ✓ | 0.0% |  |
| 94 | `PrefPlaVolHOffline` | 原股东网下认购优先配售(股) | number(16,0) | ✓ | 0.0% |  |
| 95 | `ValidApplyHNum` | 原股东有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 96 | `ValidApplyNumHOnline` | 原股东网上认购有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 97 | `ValidApplyNumHOffline` | 原股东网下认购有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 98 | `PublicOfferVolOnline` | 上网公开发行股数(股) | number(16,0) | ✓ | 0.0% |  |
| 99 | `ValidApplyVolOnline` | 上网有效申购总量(股) | number(16,0) | ✓ | 0.0% |  |
| 100 | `ValidApplyNumOnline` | 上网有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 101 | `OverSubsTimesOnline` | 上网超额认购倍数(倍) | number(9,4) | ✓ | 0.0% |  |
| 102 | `LotRateOnline` | 上网中签率(%) | number(18,15) | ✓ | 0.0% |  |
| 103 | `PlaVolLPOffline` | 法人网下配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 104 | `TailoredPlaVolLP` | 法人定向配售股数(股) | number(16,0) | ✓ | 19.43% |  |
| 105 | `ValidApplyVolLPOffline` | 法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.0% |  |
| 106 | `ValidApplyNumLPOffline` | 法人网下配售有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 107 | `OverSubsTimesLPOffline` | 法人网下配售超额认购倍数(倍) | number(9,4) | ✓ | 0.0% |  |
| 108 | `LotRateLPOffline` | 法人网下配售中签率(%) | number(18,15) | ✓ | 0.0% |  |
| 109 | `APlaVolLPOffline` | A类法人网下配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 110 | `AValidVolLPOffline` | A类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.0% |  |
| 111 | `AValidNumLPOffline` | A类法人网下配售有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 112 | `ALotRateLPOffline` | A类法人网下配售中签率(%) | number(18,15) | ✓ | 0.0% |  |
| 113 | `BPlaVolLPOffline` | B类法人网下配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 114 | `BValidVolLPOffline` | B类法人网下配售有效申购总量(股) | number(16,0) | ✓ | 0.0% |  |
| 115 | `BValidNumLPOffline` | B类法人网下配售有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 116 | `BLotRateLPOffline` | B类法人网下配售中签率(%) | number(18,15) | ✓ | 0.0% |  |
| 117 | `OutstandingShares` | 本次上市流通股数(股) | number(16,0) | ✓ | 0.0% |  |
| 118 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 0.0% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，... |
| 119 | `UnderwriterBoughtVol` | 余股包销数量(股) | number(16,0) | ✓ | 0.0% |  |
| 120 | `SchemeChangePublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 121 | `ChangeStatement` | 方案变动说明 | varchar2(2000) | ✓ | 38.69% |  |
| 122 | `ChangeType` | 方案变动类型 | number(10) | ✓ | 38.69% | 方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 AND ... |
| 123 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 124 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 125 | `JSID` | JSID | number(19) | ✗ |  |  |
| 126 | `IssueOAllOption` | 初始超额配售权(股) | number(16,0) | ✓ | 0.0% |  |
| 127 | `AdjustedOAllOption` | 最新超额配售权(股) | number(16,0) | ✓ | 0.0% |  |
| 128 | `QuotationUnitOnline` | 网上申购报价单位(元) | number(19,4) | ✓ | 0.0% |  |
| 129 | `QuotationUnitOffline` | 网下申购报价单位(元) | number(19,4) | ✓ | 0.0% |  |
| 130 | `PlaVolHOffline` | 原股东网下配售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 131 | `ValidPlaVolHOffline` | 原股东网下配售有效申购总量(股) | number(16,0) | ✓ | 0.0% |  |
| 132 | `ValidPlaNumHOffline` | 原股东网下配售有效申购户数(户) | number(10) | ✓ | 0.0% |  |
| 133 | `LotRateHOffline` | 原股东网下配售中签率(%) | number(18,15) | ✓ | 0.0% |  |
| 134 | `ApplyDate` | 申购日1 | date | ✓ | 1.4% |  |

## 字段说明

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。

### IssueType (增发类别)

增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (21,22,23)，得到增发类别的具体描述：21-非公开增发，22-公开增发，23-非公开增发配套融资。

### IfSummaryProcedure (是否简易程序)

是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。

### IfEffected (是否有效)

是否有效(IfEffected)的具体描述: 1-是，2-否。是代表本次增发方案仍在正常实施中或实施完成，否代表本次增发方案已被否决或停止实施。

### PricingModel (发行价定价方式)

发行价定价方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1019，得到发行价定价方式的具体描述：1-发行人与承销商协商定价，2-市盈率定价，3-网上区间询价，4-网下区间询价，5-市场竞价，6-类比定价，7-现金流折现法，8-设定下限，9-设定上限，10-预路演，11-设定区间，12-市价折扣，13-市价平均，14-证券面值，15-初步询价，16-发行人与各方协商定价，17-发行人直接定价，18-累计投标询价。

### RationModel (发行量定量方式)

发行量定量方式(RationModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1020，得到发行量定量方式的具体描述：1-发行额度，2-设定上限，3-设定下限，4-设定区间。

### IssueMethod (发行方式明细)

发行方式明细(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1018，得到发行方式明细的具体描述：1-内部发行，2-认购证，3-专项存单，4-全额预交款、比例配售、余额转存，5-全额预交款、比例配售、余额即退，6-上网竞价，7-上网定价，8-基金配售，9-法人配售，10-二级市场配售，11-STAQ/NET定向配售，12-自办发行，13-法人定向配售，14-老股东优先配售，15-基金公众持有人配售，16-基金发起人配售，17-私募配售，18-公募发行，19-国有股存量发行，20-派送，21-非公开发行，22-比例换股，23-非公开发行配套融资，24-直接定价，25-重新上市，26-三板精选层转板上市，27-公开发行，28-转板上市。

### ISOBTypeCode (发行对象类型)

发行对象类型(ISOBTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1639，得到发行对象类型的具体描述：1-大股东及大股东关联方，2-机构投资者，3-自然人，4-全体投资者，5-公司股东。

### SubscribeMethod (认购方式)

认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

### LargeSHSubMethod (控股股东认购方式)

控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到控股股东认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。

## SQL示例

```sql
-- 查询 科创板增发 数据
SELECT *
FROM lc_stibnewissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
