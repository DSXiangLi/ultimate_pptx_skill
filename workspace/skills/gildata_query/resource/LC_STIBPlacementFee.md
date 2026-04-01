# LC_STIBPlacementFee

**中文名**: 科创板配股发行费用

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBPlacementFee` |
| MySQL表名 | `lc_stibplacementfee` |
| 中文名 | 科创板配股发行费用 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1、内容说明：收录科创板A股的配股上市实际的发行费用，包括费用总额、承销费用、注册会计师费用、资产评估费用、土地评估费用、律师费用等。
2、数据范围：2019年至今
3、信息来源：配股上市公告书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 0.0% | RID（RID）：与科创板配股(LC_STIBPlacement)的ID字段关联。 |
| 3 | `UWSponFee` | 1)承销保荐费用合计(元) | number(19,4) | ✓ | 0.0% |  |
| 4 | `UnderwritingFee` | 1.1)承销费用(元) | number(19,4) | ✓ | 0.0% |  |
| 5 | `SponsorFee` | 1.2)保荐费用(元) | number(19,4) | ✓ | 0.0% |  |
| 6 | `CPAAppraisalFee` | 2)审计验资及评估费用合计(元) | number(19,4) | ✓ | 0.0% |  |
| 7 | `CPAFee` | 2.1)注册会计师费用(元) | number(19,4) | ✓ | 0.0% |  |
| 8 | `AssetAppraisalFee` | 2.2)资产评估费用(元) | number(19,4) | ✓ | 0.0% |  |
| 9 | `LandEvaluationFee` | 2.3)土地评估费用(元) | number(19,4) | ✓ | 0.0% |  |
| 10 | `AttorneyFee` | 3)律师费用(实际)(元) | number(19,4) | ✓ | 0.0% |  |
| 11 | `DisclosureFee` | 4)信息披露费用(元) | number(19,4) | ✓ | 0.0% |  |
| 12 | `OtherFee` | 5)其他费用(元) | number(19,4) | ✓ | 0.0% |  |
| 13 | `IssueCostPerShare` | 每股发行费用(元/股) | number(19,4) | ✓ | 0.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID（RID）：与科创板配股(LC_STIBPlacement)的ID字段关联。

## SQL示例

```sql
-- 查询 科创板配股发行费用 数据
SELECT *
FROM lc_stibplacementfee
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
