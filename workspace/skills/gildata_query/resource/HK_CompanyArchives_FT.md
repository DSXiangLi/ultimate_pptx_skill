# HK_CompanyArchives_FT

**中文名**: 港股企业概况表附表_繁体版

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CompanyArchives_FT` |
| MySQL表名 | `hk_companyarchives_ft` |
| 中文名 | 港股企业概况表附表_繁体版 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1.01 |

## 表描述

1.记录香港证券相关的企业基本信息。
2.数据来源：港交所、香港公司注册处综合资讯系统等。
3.作为港股企业概况表的繁体版。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `ChiName` | 中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `ChiNameAbbr` | 中文简称 | varchar2(100) | ✓ | 68.82% |  |
| 6 | `RegAddr` | 注册地址 | varchar2(400) | ✓ | 81.86% |  |
| 7 | `HeadOfficeAddress` | 总部地址 | varchar2(400) | ✓ | 46.67% |  |
| 8 | `Chairman` | 主席 | varchar2(100) | ✓ | 23.61% |  |
| 9 | `BriefIntroText` | 公司简介 | clob | ✓ | 33.89% |  |
| 10 | `MainBusiness` | 主营业务 | clob | ✓ | 50.9% |  |
| 11 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 港股企业概况表附表_繁体版 数据
SELECT *
FROM hk_companyarchives_ft
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
