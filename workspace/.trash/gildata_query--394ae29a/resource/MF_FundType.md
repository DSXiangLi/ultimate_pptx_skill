# MF_FundType

**中文名**: 公募基金分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundType` |
| MySQL表名 | `mf_fundtype` |
| 中文名 | 公募基金分类表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.本表记录各类型的基金分类标准体系，及发布分类体系的机构。
2.历史数据：2017年6月起-至今。
3.信息来源：证监会官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `Standard` | 分类标准 | number(10) | ✗ | 100.0% | 分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 AND DM I... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 98.88% |  |
| 4 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% | 本表生效日期均依据官网披露，但由于证监会分类并无相关公告，故生效日期给定一个默认值，该默认值并无具体含义。 |
| 5 | `CancelDate` | 取消日期 | date | ✓ | 34.2% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 7 | `PubOrgCode` | 发布机构代码 | number(10) | ✓ | 100.0% | 发布机构代码（PubOrgCode）与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 8 | `PubOrgName` | 发布机构名称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `FundTypeName` | 分类名称 | varchar2(200) | ✗ | 100.0% | 分类名称(FundTypeName)：针对聚源基金分类中的灵活配置型，解释如下，120201-灵活配置型I[灵活配置型基... |
| 10 | `DisclosureCode` | 披露分类代码 | varchar2(20) | ✓ | 79.93% |  |
| 11 | `FundTypeCode` | 分类编码 | number(10) | ✓ | 100.0% |  |
| 12 | `ParentFundTypeCode` | 父级分类编码 | number(10) | ✓ | 91.82% | 父级分类编码(ParentFundTypeCode)：与本表的FundTypeCode进行关联 |
| 13 | `StandardLevel` | 分类级别 | number(10) | ✗ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Standard (分类标准)

分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 AND DM IN (10,11,18,75)，得到分类标准的具体描述：10-证监会基金分类，11-晨星基金分类，18-银河证券分类2017版，75-聚源基金分类。

### EffectiveDate (生效日期)

本表生效日期均依据官网披露，但由于证监会分类并无相关公告，故生效日期给定一个默认值，该默认值并无具体含义。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

### PubOrgCode (发布机构代码)

发布机构代码（PubOrgCode）与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到发布机构的具体信息。

### FundTypeName (分类名称)

分类名称(FundTypeName)：针对聚源基金分类中的灵活配置型，解释如下，120201-灵活配置型I[灵活配置型基金(基准股票比例0-30%)]、120202-灵活配置型II[灵活配置型基金(基准股票比例30%-60%)]、120203-灵活配置型III[灵活配置型基金(基准股票比例60%-100%)]、120204-灵活配置型IV[灵活配置型基金(基准比例：定期存款利率/年化利率等)]

### ParentFundTypeCode (父级分类编码)

父级分类编码(ParentFundTypeCode)：与本表的FundTypeCode进行关联

## SQL示例

```sql
-- 查询 公募基金分类表 数据
SELECT *
FROM mf_fundtype
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
