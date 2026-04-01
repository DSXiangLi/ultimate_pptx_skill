# LC_CorrIndexIndustry

**中文名**: 指数与行业对应

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_CorrIndexIndustry` |
| MySQL表名 | `lc_corrindexindustry` |
| 中文名 | 指数与行业对应 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录了行业指数与所属行业的对应关系，包括行业分类标准，行业分类信息；通过与系统常量表等相关联，能获取具体的行业分类标准和所属行业信息。
2.数据源：申银万国研究所、中证指数有限公司、中信证券股份有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内码 | number(10) | ✗ | 100.0% | 指数内码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指... |
| 3 | `IndustryStandard` | 行业分类标准 | number(10) | ✗ | 100.0% | 行业分类标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 108... |
| 4 | `IndustryCode` | 所属行业 | number(10) | ✓ | 100.0% | 所属行业(IndustryCode)：当IndustryStandard in (1,3,5,6,7,9,12,20,2... |
| 5 | `EndDate` | 行业停用日期 | date | ✓ | 16.84% |  |
| 6 | `IndexState` | 指数状态 | number(10) | ✓ | 100.0% | 指数状态（IndexState），该字段定为固定常量：1-新增；2-延用；3-停用 |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内码)

指数内码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### IndustryStandard (行业分类标准)

行业分类标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (1,3,5,6,7,9,12,14,20,22,23,24,28,30,37,38,40,44,49,100)，得到行业分类标准的具体描述：1-CSRC行业分类，3-中信行业分类，5-SSE行业分类，6-聚源行业分类(旧)，7-SSE-GICS行业分类，9-申万行业分类，12-中证指数行业分类，14-新华ICB行业分类，20-国证行业分类，22-证监会行业分类2012版，23-证监会行业分类2012版(中证披露)，24-申万行业分类2014版，28-中证指数行业分类(2016版)，30-聚源行业分类2016，37-中信行业2019分类，38-申万行业分类(新)，40-中证指数行业分类(2021版)，44-中国上市公司协会上市公司行业统计分类指引，49-长江行业分类，100-恒生行业分类。

### IndustryCode (所属行业)

所属行业(IndustryCode)：当IndustryStandard in (1,3,5,6,7,9,12,20,22,24,28,30,33,37,44,46) 时,"IndustryCode"与"CT_IndustryType"的"IndustryNum"关联,同时令CT_IndustryType.Standard=IndustryStandard;当IndustryStandard=23时,"IndustryCode"与"CT_IndustryType"的"IndustryNum"关联,同时令CT_IndustryType.Standard=22;当IndustryStandard=13时,"IndustryCode"与"CT_IndustryType"的"IndustryNum"关联,同时令CT_IndustryType.Standard=6;当IndustryStandard in (38,40) 时,"IndustryCode"与"CT_IndustryType"的"IndustryCode"关联,同时令CT_IndustryType.Standard=IndustryStandard;当IndustryStandard=14时,"IndustryCode"与"CT_SystemConst"的"DM"关联,"LB=1529";当IndustryStandard=100时,"IndustryCode"与"HK_IndustryCategory"的"IndustryNum"关联,Standard=100

### IndexState (指数状态)

指数状态（IndexState），该字段定为固定常量：1-新增；2-延用；3-停用

## SQL示例

```sql
-- 查询 指数与行业对应 数据
SELECT *
FROM lc_corrindexindustry
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
