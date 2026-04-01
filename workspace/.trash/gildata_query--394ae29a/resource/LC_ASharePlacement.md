# LC_ASharePlacement

**中文名**: A股配股

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ASharePlacement` |
| MySQL表名 | `lc_ashareplacement` |
| 中文名 | A股配股 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 82 |
| 版本 | 1.03 |

## 表描述

1.收录A股历次配股预案及实施进展明细，包括预案有效期、配股价格区间、配股说明书、募集资金和配股交款日等内容。
2.数据范围：1991-03-06至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 100.0% |  |
| 5 | `EventProcedureCode` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 164... |
| 6 | `PlaYear` | 配股年度 | date | ✓ | 100.0% |  |
| 7 | `StockType` | 发行股票类型 | number(10) | ✓ | 100.0% | 发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND D... |
| 8 | `PricingModel` | 配股价格确定方式 | number(10) | ✓ | 84.77% | 配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，... |
| 9 | `PricingDescription` | 配股价格确定方式说明 | varchar2(255) | ✓ | 96.03% |  |
| 10 | `IssueMethod` | 发行方式 | number(10) | ✓ | 17.25% | 发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2375，得到发行方... |
| 11 | `PlaProspectus` | 配股说明 | varchar2(255) | ✓ | 100.0% |  |
| 12 | `AdvanceDate` | 预案公布日 | date | ✓ | 97.81% |  |
| 13 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 91.46% |  |
| 14 | `ExApprovalPublDate` | 交易所审核通过日 | date | ✓ | 0.18% |  |
| 15 | `CSRCIACApprovalDate` | 证监会发审委通过公告日 | date | ✓ | 12.27% |  |
| 16 | `SASACApprovalPublDate` | 国资委通过公告日 | date | ✓ | 3.2% |  |
| 17 | `CSRCApprovalPublDate` | 证监会批准公告日 | date | ✓ | 41.97% |  |
| 18 | `ResultPulbDate` | 配股结果公告日 | date | ✓ | 11.62% |  |
| 19 | `ListAnnounceDate` | 配股上市公告日 | date | ✓ | 40.6% |  |
| 20 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 82.99% |  |
| 21 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 82.75% |  |
| 22 | `PlaPriceCeiling` | 计划配股价格上限(最高价)(元) | number(19,4) | ✓ | 61.53% |  |
| 23 | `PlaPriceFloor` | 计划配股价格下限(最低价)(元) | number(19,4) | ✓ | 60.64% |  |
| 24 | `DeciPublDate` | 决案公布日 | date | ✓ | 91.46% |  |
| 25 | `PlaProspectusPublDate` | 配股说明书刊登日期 | date | ✓ | 69.0% |  |
| 26 | `PlaAbbrName` | 配股简称 | varchar2(20) | ✓ | 63.54% |  |
| 27 | `PlaCode` | 配股代码 | varchar2(10) | ✓ | 66.69% |  |
| 28 | `BaseShares` | 实际配股股本基数(股) | number(16,0) | ✓ | 69.83% |  |
| 29 | `PlannedBaseShares` | 计划配股股本基数(股) | number(16,0) | ✓ | 97.45% |  |
| 30 | `PlaRatioPlanned` | 初始计划配股比例(10配X) | number(9,4) | ✓ | 99.94% |  |
| 31 | `PlannedPlaVol` | 初始计划配股数量(股) | number(16,0) | ✓ | 98.87% |  |
| 32 | `AdjustedPlaRatioPl` | 最新计划配股比例(10配X) | number(9,4) | ✓ | 99.94% |  |
| 33 | `AdjustedPlaVolPl` | 最新计划配股数量(股) | number(16,0) | ✓ | 98.87% |  |
| 34 | `ActualPlaRatio` | 实际配股比例(10配X) | number(9,4) | ✓ | 69.89% |  |
| 35 | `ActualPlaVol` | 实际配股数量(股) | number(16,0) | ✓ | 69.89% |  |
| 36 | `PlaObject` | 配股对象说明 | varchar2(255) | ✓ | 100.0% |  |
| 37 | `PlaObjectCategory` | 配股对象类别 | number(10) | ✓ | 100.0% | 配股对象类别(PlaObjectCategory)与(CT_SystemConst)表中的DM字段关联，令LB=1197... |
| 38 | `ParValue` | 每股面值(元) | number(19,4) | ✓ | 100.0% |  |
| 39 | `PlaPrice` | 每股实际配股价格(元) | number(19,4) | ✓ | 69.35% |  |
| 40 | `PlaBaseDate` | 配股基准日 | date | ✓ | 46.83% |  |
| 41 | `TransferPlaRatio` | 转配比(10转配X) | number(9,4) | ✓ | 11.44% |  |
| 42 | `TransferPlaVol` | 转配股(股) | number(16,0) | ✓ | 9.96% |  |
| 43 | `TransferFeePerShare` | 每股转配费(元) | number(19,4) | ✓ | 11.68% |  |
| 44 | `OddLotsTreatment` | 零股处理方法 | number(10) | ✓ | 67.28% | 零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 121... |
| 45 | `PlannedPlaProceeds` | 计划募集资金总额(元) | number(19,4) | ✓ | 73.33% |  |
| 46 | `PlaProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 69.77% |  |
| 47 | `PlaCost` | 发行费用总额(元) | number(19,4) | ✓ | 58.45% |  |
| 48 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 5.39% |  |
| 49 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 2.73% |  |
| 50 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 0.24% |  |
| 51 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 3.2% |  |
| 52 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 1.6% |  |
| 53 | `AssetAppraisalFee` | 2.2.)资产评估费用(元) | number(19,4) | ✓ | 0.12% |  |
| 54 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.0% |  |
| 55 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 3.14% |  |
| 56 | `TotalAgentFee` | 4)中介机构费合计(元) | number(19,4) | ✓ | 0.71% |  |
| 57 | `OnlineIssueFee` | 5)上网发行费用(元) | number(19,4) | ✓ | 0.59% |  |
| 58 | `ScripFee` | 6)股票登记费用(元) | number(19,4) | ✓ | 2.19% |  |
| 59 | `OtherFee` | 7)其他费用(元) | number(19,4) | ✓ | 0.71% |  |
| 60 | `PlaNetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 59.04% |  |
| 61 | `RightRegDate` | 股权登记日 | date | ✓ | 69.18% |  |
| 62 | `ExRightDate` | 除权日 | date | ✓ | 69.06% |  |
| 63 | `PayStartDate` | 配股交款起始日 | date | ✓ | 69.0% |  |
| 64 | `PayEndDate` | 配股交款截止日 | date | ✓ | 69.41% |  |
| 65 | `DateToAccount` | 资金到帐日 | date | ✓ | 61.71% |  |
| 66 | `MoneyToAccount` | 资金到帐金额(元) | number(19,4) | ✓ | 59.04% |  |
| 67 | `PlaListDate` | 配股上市日 | date | ✓ | 69.41% |  |
| 68 | `LargeSHSubsStatement` | 大股东认配说明 | clob | ✓ | 8.83% |  |
| 69 | `SchemeChange` | 方案是否变更 | number(10) | ✓ | 66.21% | 方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到... |
| 70 | `ChangeStatement` | 方案变动说明 | varchar2(1000) | ✓ | 66.03% |  |
| 71 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 76.29% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，... |
| 72 | `UnderwriterBoughtVol` | 余股包销数量(股) | number(16,0) | ✓ | 5.87% |  |
| 73 | `PublicSHSubscriptionEsti` | 公众股东预计认配股数(股) | number(16,0) | ✓ | 99.41% |  |
| 74 | `PublicSHSubscriptionActu` | 公众股东实际认配股数(股) | number(16,0) | ✓ | 69.65% |  |
| 75 | `LargeSHHoldSum` | 持股5%以上大股东持股数(股) | number(16,0) | ✓ | 94.67% |  |
| 76 | `LargeSHSubscripEsti` | 持股5%以上大股东计划认配股数(股) | number(16,0) | ✓ | 94.67% |  |
| 77 | `LargeSHSubscripActu` | 持股5%以上大股东实际认配股数(股) | number(16,0) | ✓ | 64.85% |  |
| 78 | `NAPSAfterAllotment` | 配股完成后预计每股净资产(元) | number(19,4) | ✓ | 8.06% |  |
| 79 | `EPSAfterAllotment` | 配股完成后预计每股收益(元) | number(19,4) | ✓ | 8.06% |  |
| 80 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 81 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 82 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### EventProcedureCode (事件进程)

事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。

### StockType (发行股票类型)

发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1,3)，得到发行股票类型的具体描述：1-A股，3-H股。

### PricingModel (配股价格确定方式)

配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，得到配股价格确定方式的具体描述：1-设定区间，2-市价折扣。

### IssueMethod (发行方式)

发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2375，得到发行方式的具体描述：1-网上定价，2-无限售流通股网上定价、有限售流通股网下定价，3-其他。

### PlaObjectCategory (配股对象类别)

配股对象类别(PlaObjectCategory)与(CT_SystemConst)表中的DM字段关联，令LB=1197 and DM in (1,7,10) ，得到配股对象类别的具体描述：1-全体股东，7-无限售股东，10-流通股东。

### OddLotsTreatment (零股处理方法)

零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 1218，得到零股处理方法的具体描述：1-不足一股不予配售，2-不足一股四舍五入，3-不足一股累计后随机配售，4-不足一股依据精确算法处理。

### SchemeChange (方案是否变更)

方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案是否变更的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

## SQL示例

```sql
-- 查询 A股配股 数据
SELECT *
FROM lc_ashareplacement
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
