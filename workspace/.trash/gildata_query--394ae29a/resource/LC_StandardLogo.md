# LC_StandardLogo

**中文名**: 标准企业LOGO

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_StandardLogo` |
| MySQL表名 | `lc_standardlogo` |
| 中文名 | 标准企业LOGO |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

内容说明：收录企业的logo标准化后的图片
数据范围：现有国内A\B上市公司
信息来源：各上市公司官网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `ChiName` | 公司中文名称 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% | 序号（SerialNumber）：为不同标准的识别。序号1，为第一种标准格式：高300*宽400 |
| 6 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 7 | `PictureURL` | 图片链接 | varchar2(400) | ✓ | 84.89% | 图片链接（PictureURL）：自2023年7月20日停止维护。 |
| 8 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM I... |
| 9 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### SerialNumber (序号)

序号（SerialNumber）：为不同标准的识别。序号1，为第一种标准格式：高300*宽400

### PictureURL (图片链接)

图片链接（PictureURL）：自2023年7月20日停止维护。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM IN (10,21,26,27,28)，得到文件格式的具体描述：10-JPG，21-GIF，26-BMP，27-SWF，28-PNG。

## SQL示例

```sql
-- 查询 标准企业LOGO 数据
SELECT *
FROM lc_standardlogo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
