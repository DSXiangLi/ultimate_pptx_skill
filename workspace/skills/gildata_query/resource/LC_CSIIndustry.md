# LC_CSIIndustry

**中文名**: 公司行业分类_中证发布

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_CSIIndustry` |
| MySQL表名 | `lc_csiindustry` |
| 中文名 | 公司行业分类_中证发布 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.收录了证券的中证行业分类及证监会行业分类（中证披露）等，中证行业分类涵盖四级分类，证监会行业分类涵盖二级分类。。
2.数据范围：2012-11-13至今
3.信息来源：中证指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 生效日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `FstIndustryCSI` | 中证一级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 5 | `FstIndNameCSI` | 中证一级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `SndIndustryCSI` | 中证二级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 7 | `SndIndNameCSI` | 中证二级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `TrdIndustryCSI` | 中证三级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 9 | `TrdIndNameCSI` | 中证三级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `FthIndustryCSI` | 中证四级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 11 | `FthIndNameCSI` | 中证四级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `IndexCodeHS300I` | 沪深300行业指数代码 | number(10) | ✓ | 6.84% | 沪深300行业指数代码（IndexCodeHS300I）：与“证券主表（SecuMain）”中的“证券内部编码（Inne... |
| 13 | `FstIndustryCSRS` | 证监会一级行业代码 | varchar2(20) | ✓ | 99.81% |  |
| 14 | `FstIndNameCSRS` | 证监会一级行业名称 | varchar2(100) | ✓ | 99.2% |  |
| 15 | `SndIndustryCSRS` | 证监会二级行业代码 | varchar2(20) | ✓ | 99.81% |  |
| 16 | `SndIndNameCSRS` | 证监会二级行业名称 | varchar2(100) | ✓ | 98.9% |  |
| 17 | `Remark` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### IndexCodeHS300I (沪深300行业指数代码)

沪深300行业指数代码（IndexCodeHS300I）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到成份股所属沪深300行业指数的交易代码、简称等。

## SQL示例

```sql
-- 查询 公司行业分类_中证发布 数据
SELECT *
FROM lc_csiindustry
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
