# HK_ExgIndustry

**中文名**: 港股公司行业划分表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_ExgIndustry` |
| MySQL表名 | `hk_exgindustry` |
| 中文名 | 港股公司行业划分表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.描述香港联交所上市的公司的行业分类，主要有恒生行业分类、恒生聚源行业分类、中国证监会行业分类、申万行业分类等，该表记录港股上市公司的行业分类。
2.信息来源：港交所、恒生聚源等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司内码 | number(10) | ✗ | 100.0% | 公司内码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `Standard` | 行业划分标准 | number(10) | ✗ | 100.0% | 行业划分标准(Standard)的具体描述： 8-聚源行业分类，12-中证指数行业分类，17-聚源全球行业分类B，22-... |
| 4 | `IndustryNum` | 行业编码 | number(10) | ✗ | 100.0% | 行业编码（IndustryNum）：当Standard IN (8,12,22,24,100)时，与港股行业分类表（HK... |
| 5 | `ExcuteDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `CancelDate` | 取消日期 | date | ✓ | 28.15% |  |
| 7 | `IfExecuted` | 是否执行 | number(3) | ✓ | 100.0% | 是否执行（IfExecuted）：该字段固定以下常量1-是，2-否 |
| 8 | `XGRQ` | 修改时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司内码)

公司内码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### Standard (行业划分标准)

行业划分标准(Standard)的具体描述： 8-聚源行业分类，12-中证指数行业分类，17-聚源全球行业分类B，22-证监会行业分类2012版，24-申万行业分类2014版，37-中信行业2019分类，38-申万行业分类(新)，100-恒生行业分类。

### IndustryNum (行业编码)

行业编码（IndustryNum）：当Standard IN (8,12,22,24,100)时，与港股行业分类表（HK_IndustryCategory）中的行业编码（IndustryNum）关联，得到行业的名称及相关信息；当Standard IN (17,37,38)，与行业类别表（CT_IndustryType）中的行业内部编码（IndustryNum）关联，得到行业的名称及相关信息。

### IfExecuted (是否执行)

是否执行（IfExecuted）：该字段固定以下常量1-是，2-否

## SQL示例

```sql
-- 查询 港股公司行业划分表 数据
SELECT *
FROM hk_exgindustry
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
