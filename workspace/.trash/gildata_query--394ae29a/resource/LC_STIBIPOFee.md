# LC_STIBIPOFee

**中文名**: 科创板IPO发行费用

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBIPOFee` |
| MySQL表名 | `lc_stibipofee` |
| 中文名 | 科创板IPO发行费用 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 37 |
| 版本 | 1.02 |

## 表描述

1、内容说明：收录即将上市的A股的招股意向书中的拟发行费用以及IPO上市各募资类型的实际的发行费用，包括费用总额、承销费用、承销费用比例、注册会计师费用、资产评估费用、土地评估费用、律师费用等。
2、数据范围：2019年至今
3、信息来源：招股意向书、上市公告书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 科创板IPOID | number(19) | ✗ | 100.0% | 科创板IPOID(RID)：与 科创板IPO发行上市(LC_STIBIPOIssue)表的ID字段关联。 |
| 3 | `IfOverAllotment` | 是否行使超额配售选择权 | number(10) | ✓ | 100.0% | 是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 4 | `IssueCostPlaned` | 一、费用总额(预计)(元) | number(19,4) | ✓ | 99.67% |  |
| 5 | `UWSponFeePlaned` | 1)承销保荐费用合计(预计)(元) | number(19,4) | ✓ | 91.61% |  |
| 6 | `UWFeePlaned` | 1.1)承销费用(预计)(元) | number(19,4) | ✓ | 52.14% |  |
| 7 | `IssueVolUWFeePlaned` | 其中:新股承销费用(预计)(元) | number(19,4) | ✓ | 0.33% |  |
| 8 | `OrigiVolUWFeePlaned` | 其中:老股承销费用(预计)(元) | number(19,4) | ✓ | 0.0% |  |
| 9 | `UWFeeRatioPlaned` | 承销费用比例(预计)(%) | number(6,4) | ✓ | 7.24% |  |
| 10 | `MinUWFeePlaned` | 承销费用下限(预计)(元) | number(19,4) | ✓ | 4.44% |  |
| 11 | `SponsorFeePlaned` | 1.2)保荐费用(预计)(元) | number(19,4) | ✓ | 55.1% |  |
| 12 | `CPAApprFeePlaned` | 2)审计验资及评估费用合计(预计)(元) | number(19,4) | ✓ | 99.67% |  |
| 13 | `CPAFeePlaned` | 2.1)注册会计师费用(预计)(元) | number(19,4) | ✓ | 90.63% |  |
| 14 | `AssetApprFeePlaned` | 2.2)资产评估费用(预计)(元) | number(19,4) | ✓ | 2.96% |  |
| 15 | `LandApprFeePlaned` | 2.3)土地评估费用(预计)(元) | number(19,4) | ✓ | 0.0% |  |
| 16 | `AttorneyFeePlaned` | 3)律师费用(预计)(元) | number(19,4) | ✓ | 99.67% |  |
| 17 | `PublishFeePlaned` | 4)信息披露费用(预计)(元) | number(19,4) | ✓ | 98.03% |  |
| 18 | `OtherFeePlaned` | 5)其他费用(预计)(元) | number(19,4) | ✓ | 99.67% |  |
| 19 | `IssueCost` | 二、费用总额(实际)(元) | number(19,4) | ✓ | 98.85% |  |
| 20 | `UWSponFee` | 1)承销保荐费用合计(实际)(元) | number(19,4) | ✓ | 98.03% |  |
| 21 | `UnderwritingFee` | 1.1)承销费用(实际)(元) | number(19,4) | ✓ | 12.66% |  |
| 22 | `IssueVolUWFee` | 其中:新股承销费用(实际)(元) | number(19,4) | ✓ | 12.5% |  |
| 23 | `OriginalVolUWFee` | 其中:老股承销费用(实际)(元) | number(19,4) | ✓ | 0.0% |  |
| 24 | `SponsorFee` | 1.2)保荐费用(实际)(元) | number(19,4) | ✓ | 11.84% |  |
| 25 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(实际)(元) | number(19,4) | ✓ | 98.03% |  |
| 26 | `CPAFee` | 2.1)注册会计师费用(实际)(元) | number(19,4) | ✓ | 91.78% |  |
| 27 | `AssetAppraisalFee` | 2.2)资产评估费用(实际)(元) | number(19,4) | ✓ | 2.8% |  |
| 28 | `LandAppraisalFee` | 2.3)土地评估费用(实际)(元) | number(19,4) | ✓ | 0.0% |  |
| 29 | `AttorneyFee` | 3)律师费用(实际)(元) | number(19,4) | ✓ | 98.03% |  |
| 30 | `PublishFee` | 4)信息披露费用(实际)(元) | number(19,4) | ✓ | 96.38% |  |
| 31 | `OtherFee` | 5)其他费用(实际)(元) | number(19,4) | ✓ | 0.0% |  |
| 32 | `IssueCostPerShare` | 每股/份发行费用(实际)(元) | number(19,4) | ✓ | 98.85% |  |
| 33 | `IssueVolCostPS` | 新股每股/份发行费用(实际)(元) | number(19,4) | ✓ | 98.85% |  |
| 34 | `OrigiVolCostPS` | 老股每股/份发行费用(实际)(元) | number(19,4) | ✓ | 0.0% |  |
| 35 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 36 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 37 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (科创板IPOID)

科创板IPOID(RID)：与 科创板IPO发行上市(LC_STIBIPOIssue)表的ID字段关联。

### IfOverAllotment (是否行使超额配售选择权)

是否行使超额配售选择权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行使超额配售选择权的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 科创板IPO发行费用 数据
SELECT *
FROM lc_stibipofee
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
