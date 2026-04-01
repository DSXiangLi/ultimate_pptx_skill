# LC_AshareIssueCostPlaned

**中文名**: A股拟发行费用

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AshareIssueCostPlaned` |
| MySQL表名 | `lc_ashareissuecostplaned` |
| 中文名 | A股拟发行费用 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 23 |
| 版本 | 1.03 |

## 表描述

1.收录即将上市的A股的招股意向书中的拟发行费用，包括费用总额、承销费用、承销费用比例、保荐费用、注册会计师费用等。
2.信息来源：招股意向书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与LC_AShareIPO（A股发行与上市）表ID字段关联。 |
| 3 | `IfOverAllotment` | 是否行使超额配售权 | number(10) | ✓ | 100.0% | 是否行使超额配售权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 9... |
| 4 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 67.34% |  |
| 5 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 46.28% |  |
| 6 | `IssueCost` | 费用总额(元) | number(19,4) | ✓ | 78.68% |  |
| 7 | `UWSponFeePlaned` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 75.36% |  |
| 8 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 43.67% |  |
| 9 | `IssueVolUWFeePlaned` | 其中:新股承销费用(元) | number(19,4) | ✓ | 0.05% |  |
| 10 | `OrigiVolUWFeePlaned` | 其中:老股承销费用(元) | number(19,4) | ✓ | 0.03% |  |
| 11 | `UnderwritingFeeRatio` | 承销费用比例(%) | number(6,4) | ✓ | 2.22% |  |
| 12 | `MinUnderwritingFee` | 承销费用下限(元) | number(19,4) | ✓ | 1.03% |  |
| 13 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 22.59% |  |
| 14 | `CPAApprFeePlaned` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 76.23% |  |
| 15 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 71.61% |  |
| 16 | `AssetAppraisalFee` | 2.2)资产评估费用(元) | number(19,4) | ✓ | 2.66% |  |
| 17 | `LandApprFeePlaned` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.08% |  |
| 18 | `AttorneyFee` | 3)律师费用(元) | number(19,4) | ✓ | 77.47% |  |
| 19 | `DisclosureFee` | 4)信息披露费用(元) | number(19,4) | ✓ | 64.09% |  |
| 20 | `OtherFee` | 5)其他费用(元) | number(19,4) | ✓ | 75.99% |  |
| 21 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与LC_AShareIPO（A股发行与上市）表ID字段关联。

### IfOverAllotment (是否行使超额配售权)

是否行使超额配售权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行使超额配售权的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 A股拟发行费用 数据
SELECT *
FROM lc_ashareissuecostplaned
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
