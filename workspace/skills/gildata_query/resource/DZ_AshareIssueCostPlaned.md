# DZ_AshareIssueCostPlaned

**中文名**: A股拟发行费用

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AshareIssueCostPlaned` |
| MySQL表名 | `dz_ashareissuecostplaned` |
| 中文名 | A股拟发行费用 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录即将上市的A股的招股意向书中的拟发行费用，包括费用总额、承销费用、承销费用比例、保荐费用、注册会计师费用等。
2.数据范围：1990-12-10至今
3.信息来源：招股意向书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与DZ_AShareIPO（A股发行与上市）表ID字段关联。 |
| 3 | `IfOverAllotment` | 是否全额行使超额配售权 | number(10) | ✓ | 100.0% | 是否全额行使超额配售权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 4 | `IPOProceeds` | 募集资金总额(元) | number(19,4) | ✓ | 71.37% |  |
| 5 | `IPONetProceeds` | 募集资金净额(元) | number(19,4) | ✓ | 53.23% |  |
| 6 | `IssueCost` | 费用总额(元) | number(19,4) | ✓ | 81.58% |  |
| 7 | `UnderwritingFee` | 承销费用(元) | number(19,4) | ✓ | 44.84% |  |
| 8 | `UnderwritingFeeRatio` | 承销费用比例(%) | number(6,4) | ✓ | 2.91% |  |
| 9 | `MinUnderwritingFee` | 承销费用下限(元) | number(19,4) | ✓ | 1.5% |  |
| 10 | `SponsorFee` | 保荐费用(元) | number(19,4) | ✓ | 27.08% |  |
| 11 | `CPAFee` | 注册会计师费用(元) | number(19,4) | ✓ | 74.24% |  |
| 12 | `AssetAppraisalFee` | 资产评估费用(元) | number(19,4) | ✓ | 2.71% |  |
| 13 | `AttorneyFee` | 律师费用(元) | number(19,4) | ✓ | 80.54% |  |
| 14 | `DisclosureFee` | 信息披露费用(元) | number(19,4) | ✓ | 68.78% |  |
| 15 | `OtherFee` | 其他费用(元) | number(19,4) | ✓ | 79.26% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与DZ_AShareIPO（A股发行与上市）表ID字段关联。

### IfOverAllotment (是否全额行使超额配售权)

是否全额行使超额配售权(IfOverAllotment)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否全额行使超额配售权的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 A股拟发行费用 数据
SELECT *
FROM dz_ashareissuecostplaned
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
