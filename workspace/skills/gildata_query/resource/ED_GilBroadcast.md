# ED_GilBroadcast

**中文名**: 聚源播报

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `ED_GilBroadcast` |
| MySQL表名 | `ed_gilbroadcast` |
| 中文名 | 聚源播报 |
| 路径 | 聚源新版数据库 > 产品代理 > 新闻代理数据库 > 其它资讯 |
| 更新频率 | 滚动更新 |
| 字段数量 | 12 |
| 版本 | 1.01 |

## 表描述

1.收录了每日市场重要资讯信息。
2.数据范围：2008-至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InfoTitle` | 标题 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 5 | `Content` | 信息内容 | blob | ✓ | 0.07% |  |
| 6 | `Writer` | 撰写机构 | varchar2(200) | ✓ | 0.72% |  |
| 7 | `Author` | 作者 | varchar2(100) | ✓ | 9.61% |  |
| 8 | `Media` | 媒体出处 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `MediaCode` | 媒体出处代码 | number(10) | ✓ | 80.56% | 媒体出处代码(MediaCode)与(NI_NewsConst)表中的DM字段关联，令LB = 4，得到媒体出处代码的具... |
| 10 | `InfoPublTime` | 发布时间 | date | ✓ | 94.36% |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

### MediaCode (媒体出处代码)

媒体出处代码(MediaCode)与(NI_NewsConst)表中的DM字段关联，令LB = 4，得到媒体出处代码的具体描述

## SQL示例

```sql
-- 查询 聚源播报 数据
SELECT *
FROM ed_gilbroadcast
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
