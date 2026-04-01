# Index_RelatedOrg

**中文名**: 指数基本情况-相关机构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_RelatedOrg` |
| MySQL表名 | `index_relatedorg` |
| 中文名 | 指数基本情况-相关机构 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1.03 |

## 表描述

内容说明：收录指数发布和编制机构代码和名称
数据范围：所有指数
信息来源：指数公司官方来源、交易所来源

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数代码 | number(10) | ✗ | 100.0% | 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `OrgCode` | 相关机构代码 | number(10) | ✗ | 100.0% | 相关机构代码（OrgCode）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关... |
| 4 | `OrgName` | 相关机构名称 | varchar2(200) | ✗ | 100.0% |  |
| 5 | `OrgType` | 相关机构类别 | number(10) | ✗ | 100.0% | 相关机构类别（OrgType）：1-发布机构，2-编制机构 |
| 6 | `IfMainOrg` | 是否主要机构 | number(10) | ✓ | 100.0% | 是否主要机构（IfMainOrg）：1-是，0-否 |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数代码)

指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### OrgCode (相关机构代码)

相关机构代码（OrgCode）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联。

### OrgType (相关机构类别)

相关机构类别（OrgType）：1-发布机构，2-编制机构

### IfMainOrg (是否主要机构)

是否主要机构（IfMainOrg）：1-是，0-否

## SQL示例

```sql
-- 查询 指数基本情况-相关机构 数据
SELECT *
FROM index_relatedorg
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
