# LC_AShareIPO_Fee

**中文名**: A股IPO费用关联表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AShareIPO_Fee` |
| MySQL表名 | `lc_ashareipo_fee` |
| 中文名 | A股IPO费用关联表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 24 |
| 版本 | 1.03 |

## 表描述

1.收录IPO的发行费用以及募资类型，包括费用总额、承销费用、注册会计师费用、资产评估费用、土地评估费用、律师费用、中介机构费合计等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IPOID` | A股IPOID | number(19) | ✗ | 100.0% | A股IPOID（IPOID）：与LC_AShareIPO表的ID字段关联。 |
| 3 | `IfOverAllotment` | 是否行使超额配售选择权 | number(10) | ✓ | 100.0% | 是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 4 | `RaisingMethod` | 募资类型 | number(10) | ✗ | 100.0% | 募资类型(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND... |
| 5 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 99.63% |  |
| 6 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 93.8% |  |
| 7 | `IssueCost` | 费用总额(元) | number(19,4) | ✓ | 93.93% |  |
| 8 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 74.51% |  |
| 9 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 49.95% |  |
| 10 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 10.41% |  |
| 11 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 71.61% |  |
| 12 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 69.46% |  |
| 13 | `AssetAppraisalFee` | 2.2)资产评估费用(元) | number(19,4) | ✓ | 7.35% |  |
| 14 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.86% |  |
| 15 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 73.87% |  |
| 16 | `TotalAgentFee` | 4)中介机构费合计(元) | number(19,4) | ✓ | 0.95% |  |
| 17 | `OnlineIssueFee` | 5)上网发行费用(元) | number(19,4) | ✓ | 5.37% |  |
| 18 | `ScripFee` | 6)股票登记费用(元) | number(19,4) | ✓ | 15.54% |  |
| 19 | `PublishFee` | 7)信息披露费用(元) | number(19,4) | ✓ | 24.44% |  |
| 20 | `OtherFee` | 8)其他费用(元) | number(19,4) | ✓ | 72.17% |  |
| 21 | `IssueCostPerShare` | 每股发行费用(元/股) | number(18,6) | ✓ | 91.48% |  |
| 22 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IPOID (A股IPOID)

A股IPOID（IPOID）：与LC_AShareIPO表的ID字段关联。

### IfOverAllotment (是否行使超额配售选择权)

是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行使超额配售选择权的具体描述：1-是，2-否。

### RaisingMethod (募资类型)

募资类型(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM IN (1,13,14)，得到募资类型的具体描述：1-新股发行，13-老股转让，14-老股转让+新股发行。

## SQL示例

```sql
-- 查询 A股IPO费用关联表 数据
SELECT *
FROM lc_ashareipo_fee
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
