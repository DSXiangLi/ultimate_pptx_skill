# Index_SWSCorrIndustry

**中文名**: 申万指数与行业对应

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_SWSCorrIndustry` |
| MySQL表名 | `index_swscorrindustry` |
| 中文名 | 申万指数与行业对应 |
| 路径 | 聚源新版数据库 > 产品代理 > 申万代理数据库 > 申万指数 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

本表收录了申万行业指数与所属行业的对应关系，包括行业分类标准，行业分类信息；通过与行业类别表CT_IndustryType等相关联，能获取具体的行业分类标准和所属行业信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `IndustryStandard` | 指数行业标准 | number(10) | ✗ | 100.0% | 指数行业标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 108... |
| 4 | `IndustryNum` | 行业内部编码 | number(10) | ✗ | 100.0% | 行业内部编码(IndustryNum):与"CT_IndustryType"的"IndustryNum"关联,同时令CT... |
| 5 | `IndustryCode` | 行业代码 | varchar2(50) | ✓ | 100.0% | 行业代码(IndustryCode)：与"CT_IndustryType"的"IndustryCode"关联,同时令CT... |
| 6 | `Classification` | 行业级别 | number(10) | ✓ | 100.0% |  |
| 7 | `EndDate` | 截止日期 | date | ✓ | 58.84% |  |
| 8 | `IndexState` | 指数状态 | number(10) | ✓ | 100.0% | 指数状态（IndexState），该字段定为固定常量：1-新增；2-延用；3-停用 |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### IndustryStandard (指数行业标准)

指数行业标准(IndustryStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (9,24,38)，得到指数行业标准的具体描述：9-申万行业分类，24-申万行业分类2014版，38-申万行业分类(新)。

### IndustryNum (行业内部编码)

行业内部编码(IndustryNum):与"CT_IndustryType"的"IndustryNum"关联,同时令CT_IndustryType.Standard=IndustryStandard

### IndustryCode (行业代码)

行业代码(IndustryCode)：与"CT_IndustryType"的"IndustryCode"关联,同时令CT_IndustryType.Standard=IndustryStandard AND CancelDate IS NULL

### IndexState (指数状态)

指数状态（IndexState），该字段定为固定常量：1-新增；2-延用；3-停用

## SQL示例

```sql
-- 查询 申万指数与行业对应 数据
SELECT *
FROM index_swscorrindustry
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
