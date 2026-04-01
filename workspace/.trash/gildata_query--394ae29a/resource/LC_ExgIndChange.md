# LC_ExgIndChange

**中文名**: 公司行业变更表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ExgIndChange` |
| MySQL表名 | `lc_exgindchange` |
| 中文名 | 公司行业变更表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

内容说明：
本表记录上市公司从上市至今，由于主营业务变更导致的所属行业变化情况，采用同一行业分类标准，对其历史变更进行人为追溯，以便投资者进行公司数据回测，或开展行业估值、财务等数据的计算。
本表对公司所属行业的变更情况尽量参照原行业分类发布公司的披露数据，并对其新旧分类标准的不同之处加以判断，结合公司实际业务的变化，逐一进行人工比对，用最新的行业标准反映公司历史上的行业变更情况。
数据范围：A股上市公司
信息来源：公司公告、聚源整理。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `Standard` | 行业划分标准 | number(10) | ✗ | 100.0% | 41-申万行业分类(2021版) |
| 6 | `Industry` | 所属行业 | number(10) | ✗ | 100.0% | 当Standard=41时，与“行业类别表”的“行业内部编码（IndustryNum）”关联 |
| 7 | `IfExecuted` | 是否执行 | number(10) | ✗ | 100.0% | 是否执行（IfExecuted），该字段固定以下常量：1-是；2-否 |
| 8 | `CancelDate` | 取消日期 | date | ✓ | 41.51% |  |
| 9 | `FirstIndustryCode` | 一级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 10 | `FirstIndustryName` | 一级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `SecondIndustryCode` | 二级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 12 | `SecondIndustryName` | 二级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 13 | `ThirdIndustryCode` | 三级行业代码 | varchar2(20) | ✓ | 100.0% |  |
| 14 | `ThirdIndustryName` | 三级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 15 | `FourthIndustryCode` | 四级行业代码 | varchar2(20) | ✓ | 0.0% |  |
| 16 | `FourthIndustryName` | 四级行业名称 | varchar2(100) | ✓ | 0.0% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 修改日期 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Standard (行业划分标准)

41-申万行业分类(2021版)

### Industry (所属行业)

当Standard=41时，与“行业类别表”的“行业内部编码（IndustryNum）”关联

### IfExecuted (是否执行)

是否执行（IfExecuted），该字段固定以下常量：1-是；2-否

## SQL示例

```sql
-- 查询 公司行业变更表 数据
SELECT *
FROM lc_exgindchange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
