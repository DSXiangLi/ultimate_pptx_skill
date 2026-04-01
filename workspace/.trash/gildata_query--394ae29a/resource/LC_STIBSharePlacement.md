# LC_STIBSharePlacement

**中文名**: 科创板配股

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSharePlacement` |
| MySQL表名 | `lc_stibshareplacement` |
| 中文名 | 科创板配股 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 80 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录A股科创板历次配股预案及实施进展明细，包括预案有效期、配股价格区间、配股说明书、募集资金和配股交款日等内容。
2.数据范围：2019年至今
3.信息来源：配股预案、配股上市公告书等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 0.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 0.0% |  |
| 4 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 0.0% |  |
| 5 | `EventProcedureCode` | 事件进程 | number(10) | ✓ | 0.0% | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 164... |
| 6 | `PlaYear` | 配股年度 | date | ✓ | 0.0% |  |
| 7 | `PricingModel` | 配股价格确定方式 | number(10) | ✓ | 0.0% | 配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，... |
| 8 | `PricingDescription` | 配股价格确定方式说明 | varchar2(255) | ✓ | 0.0% |  |
| 9 | `IssueMethod` | 发行方式 | number(10) | ✓ | 0.0% | 发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2375，得到发行方... |
| 10 | `PlaProspectus` | 配股说明 | varchar2(255) | ✓ | 0.0% |  |
| 11 | `AdvanceDate` | 预案公布日 | date | ✓ | 0.0% |  |
| 12 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 0.0% |  |
| 13 | `ExApprovalPublDate` | 交易所审核通过日 | date | ✓ | 0.0% |  |
| 14 | `CSRCIACApprovalDate` | 证监会发审委通过公告日 | date | ✓ | 0.0% |  |
| 15 | `SASACApprovalPublDate` | 国资委通过公告日 | date | ✓ | 0.0% |  |
| 16 | `CSRCApprovalPublDate` | 证监会批准公告日 | date | ✓ | 0.0% |  |
| 17 | `ResultPulbDate` | 配股结果公告日 | date | ✓ | 0.0% |  |
| 18 | `ListAnnounceDate` | 配股上市公告日 | date | ✓ | 0.0% |  |
| 19 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 0.0% |  |
| 20 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 0.0% |  |
| 21 | `PlaPriceCeiling` | 计划配股价格上限(最高价)(元) | number(19,4) | ✓ | 0.0% |  |
| 22 | `PlaPriceFloor` | 计划配股价格下限(最低价)(元) | number(19,4) | ✓ | 0.0% |  |
| 23 | `DeciPublDate` | 决案公布日 | date | ✓ | 0.0% |  |
| 24 | `PlaProspectusPublDate` | 配股说明书公告日 | date | ✓ | 0.0% |  |
| 25 | `PlaAbbrName` | 配股简称 | varchar2(20) | ✓ | 0.0% |  |
| 26 | `PlaCode` | 配股代码 | varchar2(10) | ✓ | 0.0% |  |
| 27 | `PlannedBaseShares` | 计划配股股本基数(股) | number(16,0) | ✓ | 0.0% |  |
| 28 | `BaseShares` | 实际配股股本基数(股) | number(16,0) | ✓ | 0.0% |  |
| 29 | `PlaRatioPlanned` | 初始计划配股比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 30 | `PlannedPlaVol` | 初始计划配股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 31 | `AdjustedPlaRatioPl` | 最新计划配股比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 32 | `AdjustedPlaVolPl` | 最新计划配股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 33 | `ActualPlaRatio` | 实际配股比例(10配X) | number(9,4) | ✓ | 0.0% |  |
| 34 | `ActualPlaVol` | 实际配股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 35 | `PlaObject` | 配股对象说明 | varchar2(255) | ✓ | 0.0% |  |
| 36 | `PlaObjectCategory` | 配股对象类别 | number(10) | ✓ | 0.0% | 配股对象类别(PlaObjectCategory)与(CT_SystemConst)表中的DM字段关联，令LB=1197... |
| 37 | `ParValue` | 每股面值(元) | number(19,4) | ✓ | 0.0% |  |
| 38 | `PlaBaseDate` | 配股基准日 | date | ✓ | 0.0% |  |
| 39 | `PlaPrice` | 每股实际配股价格(元) | number(19,4) | ✓ | 0.0% |  |
| 40 | `OddLotsTreatment` | 零股处理方法 | number(10) | ✓ | 0.0% | 零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 121... |
| 41 | `PlannedPlaProceeds` | 拟募集资金金额(元) | number(19,4) | ✓ | 0.0% |  |
| 42 | `PlaProceeds` | 配股募集资金总额(元) | number(19,4) | ✓ | 0.0% |  |
| 43 | `PlaCost` | 发行费用总额(含税)(元) | number(19,4) | ✓ | 0.0% |  |
| 44 | `InputTax` | 其中:进项税额(元) | number(19,4) | ✓ | 0.0% |  |
| 45 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 0.0% |  |
| 46 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 0.0% |  |
| 47 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 0.0% |  |
| 48 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 0.0% |  |
| 49 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 0.0% |  |
| 50 | `AssetAppraisalFee` | 2.2.)资产评估费用(元) | number(19,4) | ✓ | 0.0% |  |
| 51 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.0% |  |
| 52 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 0.0% |  |
| 53 | `TotalAgentFee` | 4)中介机构费合计(元) | number(19,4) | ✓ | 0.0% |  |
| 54 | `OnlineIssueFee` | 5)上网发行费用(元) | number(19,4) | ✓ | 0.0% |  |
| 55 | `ScripFee` | 6)股票登记费用(元) | number(19,4) | ✓ | 0.0% |  |
| 56 | `OtherFee` | 7)其他费用(元) | number(19,4) | ✓ | 0.0% |  |
| 57 | `PlaNetProceeds` | 配股募集资金净额(含税)(元) | number(19,4) | ✓ | 0.0% |  |
| 58 | `RightRegDate` | 股权登记日 | date | ✓ | 0.0% |  |
| 59 | `ExRightDate` | 除权日 | date | ✓ | 0.0% |  |
| 60 | `PayStartDate` | 配股交款起始日 | date | ✓ | 0.0% |  |
| 61 | `PayEndDate` | 配股交款截止日 | date | ✓ | 0.0% |  |
| 62 | `DateToAccount` | 募集资金到帐日 | date | ✓ | 0.0% |  |
| 63 | `MoneyToAccount` | 募集资金到帐金额(元) | number(19,4) | ✓ | 0.0% |  |
| 64 | `PlaListDate` | 配股上市日 | date | ✓ | 0.0% |  |
| 65 | `LargeSHSubsStatement` | 大股东认配说明 | clob | ✓ | 0.0% |  |
| 66 | `SchemeChange` | 方案是否变更 | number(10) | ✓ | 0.0% | 方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 AN... |
| 67 | `ChangeStatement` | 方案变动说明 | varchar2(1000) | ✓ | 0.0% |  |
| 68 | `UnderwritingMode` | 承销方式 | number(10) | ✓ | 0.0% | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，... |
| 69 | `UnderwriterBoughtVol` | 余股包销数量(股) | number(16,0) | ✓ | 0.0% |  |
| 70 | `PublicSHSubscripEsti` | 公众股东预计认配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 71 | `PublicSHSubscripActu` | 公众股东实际认配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 72 | `LargeSHHoldSum` | 持股5%以上大股东持股数(股) | number(16,0) | ✓ | 0.0% |  |
| 73 | `LargeSHSubscripEsti` | 持股5%以上大股东计划认配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 74 | `LargeSHSubscripActu` | 持股5%以上大股东实际认配股数(股) | number(16,0) | ✓ | 0.0% |  |
| 75 | `NAPSAfterAllotment` | 配股完成后预计每股净资产(元) | number(19,4) | ✓ | 0.0% |  |
| 76 | `EPSAfterAllotment` | 配股完成后预计每股收益(元) | number(19,4) | ✓ | 0.0% |  |
| 77 | `IfEffected` | 是否有效 | number(10) | ✓ | 0.0% | 是否有效(IfEffected)的具体描述: 1-是，2-否。是代表本次配股方案仍在正常实施中或实施完成，否代表本次配股... |
| 78 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 79 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 80 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### EventProcedureCode (事件进程)

事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。

### PricingModel (配股价格确定方式)

配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，得到配股价格确定方式的具体描述：1-设定区间，2-市价折扣。

### IssueMethod (发行方式)

发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2375，得到发行方式的具体描述：1-网上定价，2-无限售流通股网上定价、有限售流通股网下定价，3-其他。

### PlaObjectCategory (配股对象类别)

配股对象类别(PlaObjectCategory)与(CT_SystemConst)表中的DM字段关联，令LB=1197 and DM in (1,7,10)，得到配股对象类别的具体描述：1-全体股东，7-无限售股东，10-流通股东。

### OddLotsTreatment (零股处理方法)

零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 1218，得到零股处理方法的具体描述：1-不足一股不予配售，2-不足一股四舍五入，3-不足一股累计后随机配售，4-不足一股依据精确算法处理。

### SchemeChange (方案是否变更)

方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 AND DM NOT IN (1,2,4,7,17)，得到方案是否变更的具体描述：3-放弃或股东大会否决，5-可转债改配股，6-增发改配股，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，18-未发行，19-宣布发行不成功。

### UnderwritingMode (承销方式)

承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

### IfEffected (是否有效)

是否有效(IfEffected)的具体描述: 1-是，2-否。是代表本次配股方案仍在正常实施中或实施完成，否代表本次配股方案已被否决或停止实施。

## SQL示例

```sql
-- 查询 科创板配股 数据
SELECT *
FROM lc_stibshareplacement
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
