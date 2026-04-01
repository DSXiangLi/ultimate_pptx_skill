# HK_IndustryCategory

**中文名**: 港股行业分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IndustryCategory` |
| MySQL表名 | `hk_industrycategory` |
| 中文名 | 港股行业分类表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

1.记录香港证券市场主要公司行业分类标准及分类信息，包括行业的历史变更情况，包含的行业分类有恒生行业分类、恒生聚源行业分类、中国证监会行业分类、申万行业分类等。
2.信息来源：港交所、MSCI、中国证监会、申万官网等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `Standard` | 行业分类标准 | number(10) | ✗ | 100.0% | 行业分类标准(Standard)的具体描述： 8-聚源行业分类，12-中证指数行业分类，22-证监会行业分类2012版，... |
| 3 | `InfoPublDate` | 发布日期 | date | ✓ | 100.0% |  |
| 4 | `ExcuteDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `CancelDate` | 取消日期 | date | ✓ | 4.69% |  |
| 6 | `IfExecuted` | 是否有效 | number(3) | ✓ | 100.0% | 是否执行（IfExecuted）：本字段是固定字段1-是，2-否 |
| 7 | `PubOrgCode` | 发布机构代码 | number(10) | ✓ | 100.0% | 发布机构代码（PubOrgCode）：“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 8 | `IndustryNum` | 行业编码 | number(10) | ✗ | 100.0% |  |
| 9 | `IndustryName` | 行业名称 | varchar2(50) | ✓ | 100.0% |  |
| 10 | `IndustryNameFT` | 行业名称(繁体) | varchar2(50) | ✓ | 100.0% |  |
| 11 | `IndustryNameAbbr` | 行业名称简称 | varchar2(50) | ✓ | 15.82% |  |
| 12 | `ChiSpelling` | 行业拼音简称 | varchar2(50) | ✓ | 100.0% |  |
| 13 | `IndustryCode` | 行业代码 | varchar2(10) | ✓ | 100.0% |  |
| 14 | `FatherIndustryCode` | 父类行业代码 | varchar2(10) | ✓ | 96.71% |  |
| 15 | `Classification` | 行业级别 | number(10) | ✓ | 100.0% |  |
| 16 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Standard (行业分类标准)

行业分类标准(Standard)的具体描述： 8-聚源行业分类，12-中证指数行业分类，22-证监会行业分类2012版，24-申万行业分类2014版，100-恒生行业分类。

### IfExecuted (是否有效)

是否执行（IfExecuted）：本字段是固定字段1-是，2-否

### PubOrgCode (发布机构代码)

发布机构代码（PubOrgCode）：“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到发布机构的具体名称、基本信息等。

## SQL示例

```sql
-- 查询 港股行业分类表 数据
SELECT *
FROM hk_industrycategory
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
