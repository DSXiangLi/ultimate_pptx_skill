# FP_IFDemonstrationCase

**中文名**: 保险理财产品利益演示案例-非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFDemonstrationCase` |
| MySQL表名 | `fp_ifdemonstrationcase` |
| 中文名 | 保险理财产品利益演示案例-非文本 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1.01 |

## 表描述

以图片的形式记录投资型保险产品的利益演示以及投保示例。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `FinProCode` | 保险产品编码 | varchar2(12) | ✗ | 100.0% | 保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 6 | `FileType` | 文件格式 | number(10) | ✓ | 99.99% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描... |
| 7 | `HashCode` | 文件校验码 | varchar2(100) | ✓ | 99.99% |  |
| 8 | `FielSize` | 图片大小(KB) | number(19,3) | ✓ | 99.99% |  |
| 9 | `Height` | 高度 | number(10) | ✓ | 99.99% |  |
| 10 | `Width` | 宽度 | number(10) | ✓ | 99.99% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (保险产品编码)

保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 保险理财产品利益演示案例-非文本 数据
SELECT *
FROM fp_ifdemonstrationcase
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
