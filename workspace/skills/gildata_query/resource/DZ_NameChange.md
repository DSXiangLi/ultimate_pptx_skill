# DZ_NameChange

**中文名**: 公司名称更改状况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_NameChange` |
| MySQL表名 | `dz_namechange` |
| 中文名 | 公司名称更改状况 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

内容说明：收录上市公司（包括科创板）名称历次变更情况，包括：中英文名称、中英文缩写名称、更改日期等内容。
数据范围：国内上市公司
信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 20.67% |  |
| 5 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 19.02% |  |
| 6 | `IfPassed` | 是否否决 | number(10) | ✓ | 100.0% | 是否否决(IfPassed)，该字段固定以下常量：1-是；0-否 |
| 7 | `ChangeDate` | 全称更改日期 | date | ✓ | 19.82% |  |
| 8 | `ChiName` | 中文名称 | varchar2(200) | ✗ | 100.0% |  |
| 9 | `ChiNameAbbr` | 中文名称缩写 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `EngName` | 英文名称 | varchar2(200) | ✓ | 92.31% |  |
| 11 | `EngNameAbbr` | 英文名称缩写 | varchar2(50) | ✓ | 53.46% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfPassed (是否否决)

是否否决(IfPassed)，该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 公司名称更改状况 数据
SELECT *
FROM dz_namechange
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
