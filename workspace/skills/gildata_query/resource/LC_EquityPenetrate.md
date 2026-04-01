# LC_EquityPenetrate

**中文名**: 公司股权穿透

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_EquityPenetrate` |
| MySQL表名 | `lc_equitypenetrate` |
| 中文名 | 公司股权穿透 |
| 路径 | 聚源新版数据库 > 机构数据库 > 股权关系 |
| 更新频率 | 不定期更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录上市公司的实际控制人、股东等股权关系；同时记录部分发债人、非上市非发债人的控股股东、实际控制人、股东等信息。
2.数据范围： 2017年-至今
3.信息来源：定期报告、招募说明书、其他数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2181，得到信息来源... |
| 4 | `InfoSourceDes` | 信息来源描述 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `Relationship` | 股权关系 | number(10) | ✗ | 100.0% | 股权关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 2282，得到股权... |
| 8 | `RelatedType` | 关联方类型 | number(10) | ✓ | 100.0% | 关联方类型(RelatedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到关联... |
| 9 | `RelatedPartyName` | 关联方名称 | varchar2(200) | ✗ | 100.0% |  |
| 10 | `RelatedCode` | 关联方编码 | number(10) | ✓ | 79.36% | 关联方编码（RelatedCode）：当关联方类型(RelatedType)=2时，与机构基本资料（LC_InstiAr... |
| 11 | `SerialNumber` | 序号 | number(10) | ✓ | 38.68% |  |
| 12 | `DirectAmount` | 直接持股数(股) | number(16,0) | ✓ | 38.74% |  |
| 13 | `DirectRatio` | 直接持股比例(%) | number(10,6) | ✓ | 70.89% |  |
| 14 | `IndirectAmount` | 间接持股数(股) | number(16,0) | ✓ | 0.23% |  |
| 15 | `IndirectRatio` | 间接持股比例(%) | number(10,6) | ✓ | 20.09% |  |
| 16 | `TotalAmount` | 合计持股数(股) | number(16,0) | ✓ | 1.44% |  |
| 17 | `TotalRatio` | 合计持股比例(%) | number(10,6) | ✓ | 8.16% |  |
| 18 | `InvestCurrency` | 投资币种 | number(10) | ✓ | 19.53% |  |
| 19 | `InvestSum` | 投资金额(元) | number(19,4) | ✓ | 19.54% |  |
| 20 | `HoldRightRemark` | 持股描述 | varchar2(2000) | ✓ | 2.9% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 2181，得到信息来源的具体描述：

### Relationship (股权关系)

股权关系(Relationship)与(CT_SystemConst)表中的DM字段关联，令LB = 2282，得到股权关系的具体描述：1-控股股东，2-实际控制人，3-控股公司，4-参股公司，5-联营企业，6-合营企业，7-分公司，8-子公司，9-孙公司，10-股东，11-最终实际控制人，12-联营或合营企业。

### RelatedType (关联方类型)

关联方类型(RelatedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到关联方类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### RelatedCode (关联方编码)

关联方编码（RelatedCode）：当关联方类型(RelatedType)=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；关联方类型(RelatedType)=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

## SQL示例

```sql
-- 查询 公司股权穿透 数据
SELECT *
FROM lc_equitypenetrate
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
