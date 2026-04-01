# Bond_ConBDIssue

**中文名**: 可转债发行信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDIssue` |
| MySQL表名 | `bond_conbdissue` |
| 中文名 | 可转债发行信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 96 |
| 版本 | 1.08 |

## 表描述

1.包含可转换债券的发行要素、发债担保、承销情况、网下配售、网上发行、发行结果、上市情况、主要财务指标预测等信息。
2.数据范围：1991-08-11 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `Issuer` | 发行人 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `BondNature` | 债券性质 | number(10) | ✓ | 100.0% | 债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM... |
| 5 | `ProspectusIssueDate` | 募集说明书发布日 | date | ✓ | 97.16% |  |
| 6 | `IssueMethod` | 发行方式 | varchar2(500) | ✓ | 100.0% |  |
| 7 | `IssueObject` | 发行对象(文字) | varchar2(500) | ✓ | 98.74% |  |
| 8 | `ParValue` | 债券面值(元/张) | number(19,4) | ✓ | 100.0% |  |
| 9 | `IssuePrice` | 发行价格(元/张) | number(19,4) | ✓ | 100.0% |  |
| 10 | `IssueStartDate` | 发行期起始日 | date | ✓ | 99.56% |  |
| 11 | `IssueEndDate` | 发行期截止日 | date | ✓ | 99.56% |  |
| 12 | `ProjectChangingDes` | 方案变动说明 | varchar2(255) | ✓ | 8.01% |  |
| 13 | `ProjectChangingType` | 方案变动类型 | number(10) | ✓ | 8.08% | 方案变动类型(ProjectChangingType)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 14 | `Guarantor` | 担保人 | varchar2(1000) | ✓ | 41.64% |  |
| 15 | `LeadUnderwriter` | 主承销商 | varchar2(1000) | ✓ | 98.49% |  |
| 16 | `CRAs` | 评级人 | varchar2(1000) | ✓ | 74.2% |  |
| 17 | `CreditRating` | 债券信用级别(字母) | varchar2(50) | ✓ | 74.2% |  |
| 18 | `UnderwritingMethod` | 承销方式 | number(10) | ✓ | 95.71% | 承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 101... |
| 19 | `UnderwritingStartDate` | 承销期起始日 | date | ✓ | 64.35% |  |
| 20 | `UnderwritingEndDate` | 承销期截止日 | date | ✓ | 63.97% |  |
| 21 | `PrefAltCodeH` | 老股东优先配售代码 | varchar2(10) | ✓ | 65.49% |  |
| 22 | `PrefAltNameH` | 老股东优先配售名称 | varchar2(20) | ✓ | 65.49% |  |
| 23 | `PrefAltRegDateH` | 老股东优先配售股权登记日 | date | ✓ | 65.43% |  |
| 24 | `PrefAltPayStartDateH` | 老股东优先配售日 | date | ✓ | 65.43% |  |
| 25 | `PrefAltPayEndDateH` | 老股东优先配售缴款日 | date | ✓ | 65.43% |  |
| 26 | `PrefAltPayRefundDateH` | 老股东优先配售申购资金退款日(有限售) | date | ✓ | 12.62% |  |
| 27 | `PrefAltProportionH` | 老股东优先配售比例(每100股配X张) | number(9,4) | ✓ | 65.49% |  |
| 28 | `PrefAltUnitH` | 老股东优先配售单位(张) | number(10) | ✓ | 65.49% |  |
| 29 | `PrefAltSizeH` | 老股东优先配售总额(元) | number(19,4) | ✓ | 65.05% |  |
| 30 | `PrefAltValidApplyVolH` | 老股东优先配售有效申购张数(张) | number(19) | ✓ | 64.92% |  |
| 31 | `PrefAltOfflValidApplyVolH` | 有限售股东优先配售有效申购张数(张) | number(19) | ✓ | 16.47% |  |
| 32 | `PrefAltOnlValidApplyVolH` | 无限售股东优先配售有效申购张数(张) | number(19) | ✓ | 17.41% |  |
| 33 | `PrefAltValidApplyNumH` | 老股东优先有效申购户数(户) | number(10) | ✓ | 2.4% |  |
| 34 | `PrefAltOverSubsTimeH` | 老股东优先超额认购倍数(倍) | number(12,4) | ✓ | 61.89% |  |
| 35 | `PrefAltRatioH` | 老股东优先配售中签率(%) | number(18,15) | ✓ | 64.98% |  |
| 36 | `AltSizeF` | 基金配售总额(元) | number(19,4) | ✓ | 0.06% |  |
| 37 | `AltPayStartDateF` | 基金配售缴款起始日 | date | ✓ | 0.06% |  |
| 38 | `AltPayEndDateF` | 基金配售缴款截止日 | date | ✓ | 0.06% |  |
| 39 | `AltSizeI` | 网下配售总额(元) | number(19,4) | ✓ | 46.94% |  |
| 40 | `OffLineIssueDateI` | 网下配售发行日期 | date | ✓ | 39.81% |  |
| 41 | `OffLineRFQDateI` | 网下配售询价(簿记建档)日期 | date | ✓ | 12.18% |  |
| 42 | `AltPayStartDateI` | 网下配售缴款起始日 | date | ✓ | 27.51% |  |
| 43 | `AltPayEndDateI` | 网下配售缴款截止日 | date | ✓ | 27.57% |  |
| 44 | `OffLinePayEdTimeI` | 网下配售缴款截止时间 | varchar2(8) | ✓ | 22.65% |  |
| 45 | `OffLinePayRefundDateI` | 网下配售申购资金退款日 | date | ✓ | 14.76% |  |
| 46 | `OffLineAddAltStDateI` | 网下追加配售起始日 | date | ✓ | 0.06% |  |
| 47 | `OffLineAddAltEdDateI` | 网下追加配售截止日 | date | ✓ | 0.06% |  |
| 48 | `OffLineAddAltPaEdDateI` | 网下追加配售缴款截止日 | date | ✓ | 0.13% |  |
| 49 | `OffLineAddAltPaEdTimeI` | 网下追加配售缴款截止时间 | varchar2(8) | ✓ | 0.13% |  |
| 50 | `OffLineAddAltReDateI` | 网下追加配售资金退款日 | date | ✓ | 0.13% |  |
| 51 | `OffLinePubOffValidApplyVolI` | 网下机构配售有效申购张数(张) | number(19) | ✓ | 13.12% |  |
| 52 | `OffLinePubOffValidApplyNumI` | 网下机构配售有效申购户数(户) | number(10) | ✓ | 12.56% |  |
| 53 | `OffLinePubOffValidPayNumI` | 网下机构配售有效申购缴款户数(户) | number(10) | ✓ | 12.56% |  |
| 54 | `OffLinePubOffOverSubsTimeI` | 网下机构配售超额认购倍数(倍) | number(12,4) | ✓ | 13.12% |  |
| 55 | `OffLinePubOffRatioI` | 网下机构配售中签率(%) | number(18,15) | ✓ | 13.12% |  |
| 56 | `OnLinePubOffCode` | 网上申购代码 | varchar2(10) | ✓ | 66.56% |  |
| 57 | `OnLinePubOffName` | 网上申购名称 | varchar2(20) | ✓ | 66.56% |  |
| 58 | `OnLinePubOffDate` | 网上发行日期 | date | ✓ | 66.5% |  |
| 59 | `OnLinePubOffPayEndDate` | 网上发行缴款截止日 | date | ✓ | 56.91% |  |
| 60 | `OnLinePubOffSize` | 网上发行总额(元) | number(19,4) | ✓ | 66.12% |  |
| 61 | `OnLinePubOffUnit` | 网上申购单位(张) | number(10) | ✓ | 66.56% |  |
| 62 | `OnLinePubOffApplyCap` | 网上申购上限(张) | number(10) | ✓ | 65.99% |  |
| 63 | `OnLinePubOffApplyMin` | 网上申购下限(张) | number(10) | ✓ | 60.5% |  |
| 64 | `OnLinePubOffValidApplyVol` | 网上发行有效申购张数(张) | number(19) | ✓ | 65.68% |  |
| 65 | `OnLinePubOffValidApplyNum` | 网上发行有效申购户数(户) | number(10) | ✓ | 25.17% |  |
| 66 | `OnLinePubOffOverSubsTime` | 网上发行超额认购倍数(倍) | number(12,4) | ✓ | 65.74% |  |
| 67 | `OnLinePubOffRatio` | 网上发行中签率(%) | number(18,15) | ✓ | 65.74% | 网上发行中签率(%)(OnLinePubOffRatio)：《中签率及结果公告》披露网上发行中签率。 |
| 68 | `OnLinePubOffRatioAct` | 实际网上发行中签率(%) | number(18,15) | ✓ | 65.74% | 实际网上发行中签率(%)(OnLinePubOffRatioAct)：根据《发行结果公告》剔除弃购部分后计算值。 |
| 69 | `OnLinePubOffRatioDate` | 网上中签率公告日 | date | ✓ | 65.17% |  |
| 70 | `OnLinePubOffResultDate` | 网上中签结果公告日 | date | ✓ | 65.17% |  |
| 71 | `OffLineApplyUnit` | 网下申购单位(张) | number(10) | ✓ | 22.65% |  |
| 72 | `OffLineApplyMax` | 网下申购上限(张) | number(10) | ✓ | 20.88% |  |
| 73 | `OffLineApplyMin` | 网下申购下限(张) | number(10) | ✓ | 22.71% |  |
| 74 | `DepositRatio` | 缴纳定金比例(%) | number(9,6) | ✓ | 7.76% |  |
| 75 | `DepositNum` | 定金数量(元) | number(19,4) | ✓ | 7.19% |  |
| 76 | `DepositEndDate` | 缴纳申购定金截止日 | date | ✓ | 14.89% |  |
| 77 | `DepositEndTime` | 缴纳申购定金截止时间 | varchar2(8) | ✓ | 14.32% |  |
| 78 | `OffLineApplyMaEndDate` | 网下申购材料提交截止日 | date | ✓ | 14.89% |  |
| 79 | `OffLineApplyMaEndTime` | 网下申购材料提交截止时间 | varchar2(8) | ✓ | 19.87% |  |
| 80 | `IssueResultPublDate` | 发行结果公告日 | date | ✓ | 98.04% |  |
| 81 | `PlanIssueSize` | 计划发行规模(元) | number(19,2) | ✓ | 99.94% |  |
| 82 | `ActualIssueSize` | 实际发行规模(元) | number(19,4) | ✓ | 99.94% |  |
| 83 | `IssueVol` | 发行张数(张) | number(16,0) | ✓ | 99.94% |  |
| 84 | `Proceeds` | 募集资金总额(元) | number(19,4) | ✓ | 67.7% | 募集资金总额(元)(Proceeds)：募集资金总额 = 发行费用总额 + 募集资金净额 |
| 85 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 66.06% |  |
| 86 | `NetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 66.75% |  |
| 87 | `UnderwriterboughtVolume` | 余额包销数量(张) | number(16,0) | ✓ | 59.94% |  |
| 88 | `ListAnnouncementDate` | 上市公告书发布日 | date | ✓ | 67.07% |  |
| 89 | `ExchangeDay` | 上市日期 | date | ✓ | 97.29% |  |
| 90 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 91 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 92 | `JSID` | JSID | number(19) | ✗ |  |  |
| 93 | `ProfitForecastYear` | 盈利预测年度 | date | ✓ | 0.0% |  |
| 94 | `RevenueForecast` | 主营业务收入预测(元) | number(19,4) | ✓ | 0.0% |  |
| 95 | `NetProfitForecast` | 净利润预测(元) | number(19,4) | ✓ | 0.0% |  |
| 96 | `DiluteEPSForecast` | 全面摊薄每股盈利预测 | number(19,4) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### BondNature (债券性质)

债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM NOT IN (3)，得到债券性质的具体描述：1-常规债券，2-分离交易可转债，4-可交换公司债券。

### ProjectChangingType (方案变动类型)

方案变动类型(ProjectChangingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。

### UnderwritingMethod (承销方式)

承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

### OnLinePubOffRatio (网上发行中签率(%))

网上发行中签率(%)(OnLinePubOffRatio)：《中签率及结果公告》披露网上发行中签率。

### OnLinePubOffRatioAct (实际网上发行中签率(%))

实际网上发行中签率(%)(OnLinePubOffRatioAct)：根据《发行结果公告》剔除弃购部分后计算值。

### Proceeds (募集资金总额(元))

募集资金总额(元)(Proceeds)：募集资金总额 = 发行费用总额 + 募集资金净额

## SQL示例

```sql
-- 查询 可转债发行信息 数据
SELECT *
FROM bond_conbdissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
