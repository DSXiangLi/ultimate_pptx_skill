# Bond_ABSTransStructure

**中文名**: ABS交易结构图非文本表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ABSTransStructure` |
| MySQL表名 | `bond_abstransstructure` |
| 中文名 | ABS交易结构图非文本表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 资产支持证券信息 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：用于存放ABS的交易结构图图片。
2.信息来源：募集说明书
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 99.89% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 ... |
| 5 | `EndDate` | 截止日期 | date | ✓ | 99.84% |  |
| 6 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描... |
| 7 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 8 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `FileSize` | 文件大小(KB) | number(19,3) | ✓ | 100.0% |  |
| 10 | `Height` | 高度 | number(10) | ✓ | 99.98% |  |
| 11 | `Width` | 宽度 | number(10) | ✓ | 99.98% |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1734 AND DM IN (200103,200204,600301)，得到信息来源编码的具体描述：200103-募集说明书，200204-受托机构报告，600301-评级公告。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 ABS交易结构图非文本表 数据
SELECT *
FROM bond_abstransstructure
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
