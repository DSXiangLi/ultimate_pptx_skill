# LC_StructureChart

**中文名**: 公司股权结构图

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_StructureChart` |
| MySQL表名 | `lc_structurechart` |
| 中文名 | 公司股权结构图 |
| 路径 | 聚源新版数据库 > 机构数据库 > 股权关系 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

内容说明：本表收录上市公司、发债人定期披露的公司与控股股东/实际控制人之间的产权及控制关系的方框图。
数据范围：2018-12-31至今
信息来源：定报及募集说明书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `InfoSourceCode` | 信息来源编码 | number(10) | ✗ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `Content` | 股权结构图 | blob | ✓ | 0.0% |  |
| 7 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 ，得到文件格式的... |
| 8 | `HashCode` | MD5校验码 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关公司的具体名称、基本信息等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (130102,110102,130103,130104,140105,110101)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，140105-发行披露文件:募集说明书。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 ，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 公司股权结构图 数据
SELECT *
FROM lc_structurechart
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
