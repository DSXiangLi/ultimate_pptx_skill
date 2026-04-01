# DZ_EnterpriseLogo

**中文名**: 企业标志

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_EnterpriseLogo` |
| MySQL表名 | `dz_enterpriselogo` |
| 中文名 | 企业标志 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

内容说明：收录企业（包括科创板）的logo、更新日期、图片链接、图片格式等信息。
数据范围：国内上市公司
信息来源：官网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `ListedCode` | 上市公司代码 | number(10) | ✓ | 99.64% | 上市公司代码（ListedCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，... |
| 4 | `ChiName` | 公司中文名称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `UpdateDate` | 更新日期 | date | ✗ | 100.0% |  |
| 6 | `LOGO` | logo | blob | ✓ | 6.06% |  |
| 7 | `PictureURL` | 图片链接 | varchar2(200) | ✓ | 97.19% | 图片链接（PictureURL）：自2023年7月20日停止维护。 |
| 8 | `PictureType` | 图片格式 | number(10) | ✓ | 99.99% | 图片格式(PictureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1388，得到图片格... |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### ListedCode (上市公司代码)

上市公司代码（ListedCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到相应的上市公司的交易代码、证券简称等信息。

### PictureURL (图片链接)

图片链接（PictureURL）：自2023年7月20日停止维护。

### PictureType (图片格式)

图片格式(PictureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1388，得到图片格式的具体描述：

## SQL示例

```sql
-- 查询 企业标志 数据
SELECT *
FROM dz_enterpriselogo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
