# MF_REITsProjects

**中文名**: 基础设施基金(REITs)-项目公司信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsProjects` |
| MySQL表名 | `mf_reitsprojects` |
| 中文名 | 基础设施基金(REITs)-项目公司信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：收录基础设施公募REITs与项目公司间的交易架构信息，包括资产支持证券、新设SPV等。
2.数据范围：2021年4月起-至今。
3.信息来源：上交所、深交所和证监会官网公布的基金招募说明书、基金合同等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ProjectCompanyCode` | 项目公司 | number(10) | ✗ | 100.0% | 项目公司（ProjectCompanyCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（... |
| 4 | `IFSPV` | 是否新设SPV公司 | number(10) | ✓ | 97.18% | 是否新设SPV公司(IFSPV)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN... |
| 5 | `SPVCompanyCode` | SPV公司 | number(10) | ✓ | 53.52% | SPV公司（SPVCompanyCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（Com... |
| 6 | `IFMerge` | 是否计划反向吸收合并 | number(10) | ✓ | 57.75% | 是否计划反向吸收合并(IFMerge)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM... |
| 7 | `MergeDate` | 反向吸收合并完成日期 | date | ✓ | 45.07% |  |
| 8 | `ABSInnerCode` | 资产支持专项计划内部编码 | number(10) | ✓ | 100.0% | 资产支持专项计划内部编码(ABSInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 9 | `ABSManagerCode` | 资产支持专项计划管理人 | number(10) | ✓ | 100.0% | 资产支持专项计划管理人（ABSManagerCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业... |
| 10 | `ABSTrusteeCode` | 资产支持专项计划托管人 | number(10) | ✓ | 100.0% | 资产支持专项计划托管人（ABSTrusteeCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业... |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ProjectCompanyCode (项目公司)

项目公司（ProjectCompanyCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（CompanyCode）”关联，得到项目公司基本信息。

### IFSPV (是否新设SPV公司)

是否新设SPV公司(IFSPV)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否新设SPV公司的具体描述：1-是，2-否。

### SPVCompanyCode (SPV公司)

SPV公司（SPVCompanyCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（CompanyCode）”关联，得到SPV公司基本信息。						

### IFMerge (是否计划反向吸收合并)

是否计划反向吸收合并(IFMerge)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否计划反向吸收合并的具体描述：1-是，2-否。

### ABSInnerCode (资产支持专项计划内部编码)

资产支持专项计划内部编码(ABSInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到资产支持专项计划的交易代码、简称等。

### ABSManagerCode (资产支持专项计划管理人)

资产支持专项计划管理人（ABSManagerCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（CompanyCode）”关联，得到资产支持专项计划管理人基本信息。						

### ABSTrusteeCode (资产支持专项计划托管人)

资产支持专项计划托管人（ABSTrusteeCode）：与“机构基本资料表(LC_InstiArchive)”中的“企业编号（CompanyCode）”关联，得到资产支持专项计划托管人基本信息。

## SQL示例

```sql
-- 查询 基础设施基金(REITs)-项目公司信息 数据
SELECT *
FROM mf_reitsprojects
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
