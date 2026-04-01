# Bond_NotTextAnnounce

**中文名**: 债券公告非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_NotTextAnnounce` |
| MySQL表名 | `bond_nottextannounce` |
| 中文名 | 债券公告非文本 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券公告资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1.03 |

## 表描述

1.记录债券的发行公告、募集说明书、上市公告书等公告原文，公司发行可转换债券的可转换债券募集说明书、可转换债券上市公告书等公告原文，以及评级、付息兑付等其他类公告原文。
2.历史数据：1995年01月至今
3.数据来源：中债登、货币网、上清所、上交所、深交所、中证登、评级公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `Media` | 媒体出处 | varchar2(100) | ✓ | 98.7% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `InfoTitle` | 信息标题 | varchar2(200) | ✗ | 100.0% |  |
| 8 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 9 | `LanguageType` | 语言类别 | number(10) | ✓ | 100.0% | 语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言... |
| 10 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 11 | `AnnouncementLink` | 公告链接 | varchar2(1000) | ✓ | 73.23% |  |
| 12 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 13 | `InvolvedBond` | 相关债券 | number(10) | ✓ |  |  |
| 14 | `InfoSource` | 信息来源 | number(10) | ✓ | 91.43% | 信息来源(InfoSource)与系统常量表中的DM字段关联，令LB = 1183，通过MS字段得到信息来源的具体描述。 |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到债券的代码、简称等。

### LanguageType (语言类别)

语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言类别的具体描述：1-简体中文，2-英文，3-简体中文(境外版)，5-繁体中文。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

### InfoSource (信息来源)

信息来源(InfoSource)与系统常量表中的DM字段关联，令LB = 1183，通过MS字段得到信息来源的具体描述。

## SQL示例

```sql
-- 查询 债券公告非文本 数据
SELECT *
FROM bond_nottextannounce
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
