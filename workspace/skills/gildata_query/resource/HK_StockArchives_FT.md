# HK_StockArchives_FT

**中文名**: 港股公司概况附表_繁体版

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_StockArchives_FT` |
| MySQL表名 | `hk_stockarchives_ft` |
| 中文名 | 港股公司概况附表_繁体版 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1. 内容说明：收录港股上市公司的基础信息繁体版，包括名称、成立日期、注册地点、注册资本、公司业务、所属行业分类、主席、公司秘书、联系方式等信息。
2. 数据范围：全部港股上市公司。
3. 信息来源：港交所等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“港股公司概况（HK_StockArchives）”表的ID字段关联，获取港股上市公司的基础信息简体版。 |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 4 | `CompanyName` | 公司名称 | varchar2(200) | ✓ | 99.98% |  |
| 5 | `BriefIntroText` | 公司简介 | clob | ✓ | 98.46% |  |
| 6 | `Business` | 公司业务 | varchar2(1000) | ✓ | 99.98% |  |
| 7 | `Chairman` | 主席 | varchar2(100) | ✓ | 93.74% |  |
| 8 | `CompanySecretary` | 公司秘书 | varchar2(100) | ✓ | 97.63% |  |
| 9 | `CertifiedAccountant` | 合资格会计师 | varchar2(100) | ✓ | 21.55% |  |
| 10 | `RegisteredOffice` | 注册办事处 | varchar2(200) | ✓ | 99.83% |  |
| 11 | `GeneralOffice` | 总办事处及主要营业地点 | varchar2(200) | ✓ | 99.53% |  |
| 12 | `Registrars` | 股份过户处(香港) | varchar2(200) | ✓ | 18.47% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“港股公司概况（HK_StockArchives）”表的ID字段关联，获取港股上市公司的基础信息简体版。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股公司概况附表_繁体版 数据
SELECT *
FROM hk_stockarchives_ft
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
