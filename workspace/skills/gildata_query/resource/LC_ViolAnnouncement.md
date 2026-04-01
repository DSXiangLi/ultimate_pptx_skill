# LC_ViolAnnouncement

**中文名**: 违规公告原文非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ViolAnnouncement` |
| MySQL表名 | `lc_violannouncement` |
| 中文名 | 违规公告原文非文本 |
| 路径 | 聚源新版数据库 > 诚信数据库 |
| 更新频率 | 不定期更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

内容说明：该表记录了监管机构公布的违法违规的公告信息，如行政处罚、纪律处分、问询函、监管函等。
数据范围：2014年-至今
信息来源：交易所、上市公司公告、证监会等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `Media` | 媒体出处 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `MediaCode` | 媒体出处代码 | number(10) | ✓ | 99.96% | 媒体出处代码(MediaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2195 and D... |
| 5 | `InfoTitle` | 信息标题 | varchar2(200) | ✗ | 100.0% |  |
| 6 | `LanguageType` | 语言类别 | number(10) | ✓ | 0.11% |  |
| 7 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 8 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 9 | `AnnouncementLink` | 公告链接 | varchar2(1000) | ✓ | 99.83% |  |
| 10 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `FileSize` | 文件大小(KB) | number(19,3) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MediaCode (媒体出处代码)

媒体出处代码(MediaCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2195 and DM in (100000300,180000100,410000100,410002800,410000300)，得到媒体出处代码的具体描述：100000300-中国人民银行，180000100-中国证券监督管理委员会，410000100-上海证券交易所，410000300-深圳证券交易所，410002800-中国债券信息网。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 违规公告原文非文本 数据
SELECT *
FROM lc_violannouncement
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
