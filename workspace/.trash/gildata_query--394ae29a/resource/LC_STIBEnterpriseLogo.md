# LC_STIBEnterpriseLogo

**中文名**: 科创板企业LOGO

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBEnterpriseLogo` |
| MySQL表名 | `lc_stibenterpriselogo` |
| 中文名 | 科创板企业LOGO |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：收录科创板企业的logo、更新日期、图片链接、图片格式等信息。
2.数据范围：2019年至今
3.信息来源：官网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `ChangeDate` | 变动日期 | date | ✗ | 100.0% |  |
| 4 | `LOGO` | logo | blob | ✓ | 14.08% |  |
| 5 | `PictureURL` | 图片链接 | varchar2(200) | ✓ | 88.12% | 图片链接（PictureURL）：自2023年7月20日停止维护。 |
| 6 | `PictureType` | 图片格式 | number(10) | ✓ | 100.0% | 图片格式(PictureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1388 ，得到图片... |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### PictureURL (图片链接)

图片链接（PictureURL）：自2023年7月20日停止维护。

### PictureType (图片格式)

图片格式(PictureType)与(CT_SystemConst)表中的DM字段关联，令LB = 1388 ，得到图片格式的具体描述：1-JPG，2-BMP，3-GIF，4-SWF，5-JPEG，6-PNG。

## SQL示例

```sql
-- 查询 科创板企业LOGO 数据
SELECT *
FROM lc_stibenterpriselogo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
