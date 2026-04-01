# MF_InvestIndustry

**中文名**: 公募基金行业投资

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InvestIndustry` |
| MySQL表名 | `mf_investindustry` |
| 中文名 | 公募基金行业投资 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金行业投资分布信息，包括行业的名称、代码、行业市值、该行业市值占基金净资产的比例等。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `InvestType` | 投资类型 | number(10) | ✗ | 100.0% | 投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型... |
| 7 | `InduStandard` | 行业划分标准 | number(10) | ✓ | 100.0% | 行业划分标准(InduStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AN... |
| 8 | `IndustryCode` | 行业代码 | number(10) | ✓ | 100.0% | 行业代码(IndustryCode)：当InduStandard in (6,17)时，与系统常量表的“代码（DM）”关... |
| 9 | `InduDiscCode` | 行业代码(公布) | varchar2(10) | ✓ | 81.07% |  |
| 10 | `IndustryName` | 行业名称 | varchar2(50) | ✗ | 100.0% |  |
| 11 | `MarketValue` | 行业市值(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `RatioInNV` | 占资产净值比例 | number(18,6) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 14 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### InvestType (投资类型)

投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-港股通投资。

### InduStandard (行业划分标准)

行业划分标准(InduStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (1,6,16,17,22)，得到行业划分标准的具体描述：1-CSRC行业分类，6-聚源行业分类(旧)，16-MSCI行业分类，17-聚源全球行业分类B，22-证监会行业分类2012版。

### IndustryCode (行业代码)

行业代码(IndustryCode)：当InduStandard in (6,17)时，与系统常量表的“代码（DM）”关联，“LB=1460”；当InduStandard=16时，与系统常量表的“代码（DM）”关联，“LB=1539”；当InduStandard=22时，与系统常量表的“代码（DM）”关联，“LB=1755”；当InduStandard=1时，和行业表(CT_Industry)中字段行业编码(IndustryNum)关联；当InduStandard=100时，和港股行业分类表(HK_IndustryCategory)的行业编码(IndustryNum)关联，限制Standard=100

## SQL示例

```sql
-- 查询 公募基金行业投资 数据
SELECT *
FROM mf_investindustry
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
