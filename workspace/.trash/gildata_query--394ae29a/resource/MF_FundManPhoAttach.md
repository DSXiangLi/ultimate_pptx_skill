# MF_FundManPhoAttach

**中文名**: 基金经理照片非文本附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundManPhoAttach` |
| MySQL表名 | `mf_fundmanphoattach` |
| 中文名 | 基金经理照片非文本附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

本表用于存储不同尺寸大小的基金经理照片，可供不同场景的展示需求。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与公募基金经理基本资料(MF_PersonalInfo)表中ID字段关联 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InvalidDate` | 失效时间 | date | ✓ | 0.0% |  |
| 5 | `ImageType` | 图片类型 | number(10) | ✗ | 100.0% | 图片类型(ImageType)与(CT_SystemConst)表中的DM字段关联，令LB=2449，得到图片类型的具体... |
| 6 | `ImagePattern` | 图片样式 | number(10) | ✗ | 100.0% | 图片样式(ImagePattern)与(CT_SystemConst)表中的DM字段关联，令LB=2450，得到图片样式... |
| 7 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描... |
| 8 | `FileSize` | 文件大小(KB) | number(19,3) | ✗ | 100.0% |  |
| 9 | `Height` | 高度 | number(10) | ✓ | 100.0% |  |
| 10 | `Width` | 宽度 | number(10) | ✓ | 100.0% |  |
| 11 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 12 | `HashCode` | MD5校验码 | varchar2(100) | ✗ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与公募基金经理基本资料(MF_PersonalInfo)表中ID字段关联

### ImageType (图片类型)

图片类型(ImageType)与(CT_SystemConst)表中的DM字段关联，令LB=2449，得到图片类型的具体描述：1-小，2-大。

### ImagePattern (图片样式)

图片样式(ImagePattern)与(CT_SystemConst)表中的DM字段关联，令LB=2450，得到图片样式的具体描述：1-半身照，2-大头照。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 基金经理照片非文本附表 数据
SELECT *
FROM mf_fundmanphoattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
