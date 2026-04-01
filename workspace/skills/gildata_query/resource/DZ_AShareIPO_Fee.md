# DZ_AShareIPO_Fee

**中文名**: A股IPO费用关联表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AShareIPO_Fee` |
| MySQL表名 | `dz_ashareipo_fee` |
| 中文名 | A股IPO费用关联表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.03 |

## 表描述

1.内容说明：收录IPO的发行费用以及募资类型，包括费用总额、承销费用、注册会计师费用、资产评估费用、土地评估费用、律师费用、中介机构费合计等。
2.数据范围：1990-12-10至今
3.信息来源：上市公告书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IPOID` | A股IPOID | number(19) | ✗ | 100.0% | A股IPOID（IPOID）：与DZ_AShareIPO表的ID字段关联。 |
| 3 | `IfOverAllotment` | 是否行使超额配售选择权 | number(10) | ✓ | 100.0% | 是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 4 | `RaisingMethod` | 募资类型 | number(10) | ✗ | 100.0% | 募资类型(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND... |
| 5 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 99.65% |  |
| 6 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 94.38% |  |
| 7 | `IssueCost` | 费用总额(元) | number(19,4) | ✓ | 94.51% |  |
| 8 | `UnderwritingFee` | 承销费用(元) | number(19,4) | ✓ | 46.19% |  |
| 9 | `CPAFee` | 注册会计师费用(元) | number(19,4) | ✓ | 71.75% |  |
| 10 | `AssetAppraisalFee` | 资产评估费用(元) | number(19,4) | ✓ | 6.89% |  |
| 11 | `LandEvaluationFee` | 土地评估费用(元) | number(19,4) | ✓ | 0.77% |  |
| 12 | `AttorneyFee` | 律师费用(元) | number(19,4) | ✓ | 76.34% |  |
| 13 | `TotalAgentFee` | 中介机构费合计(元) | number(19,4) | ✓ | 0.85% |  |
| 14 | `OnlineIssueFee` | 上网发行费用(元) | number(19,4) | ✓ | 4.83% |  |
| 15 | `ScripFee` | 股票登记费用(元) | number(19,4) | ✓ | 13.97% |  |
| 16 | `SponsorFee` | 上市推荐费用(元) | number(19,4) | ✓ | 10.6% |  |
| 17 | `PublishFee` | 信息披露费用(元) | number(19,4) | ✓ | 31.73% |  |
| 18 | `OtherFee` | 其他费用(元) | number(19,4) | ✓ | 74.79% |  |
| 19 | `IssueCostPerShare` | 每股/份发行费用(元) | number(18,6) | ✓ | 92.3% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IPOID (A股IPOID)

A股IPOID（IPOID）：与DZ_AShareIPO表的ID字段关联。

### IfOverAllotment (是否行使超额配售选择权)

是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行使超额配售选择权的具体描述：1-是，2-否。

### RaisingMethod (募资类型)

募资类型(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1021 AND DM IN (1,13,14)，得到募资类型的具体描述：1-新股发行，13-老股转让，14-老股转让+新股发行。

## SQL示例

```sql
-- 查询 A股IPO费用关联表 数据
SELECT *
FROM dz_ashareipo_fee
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
