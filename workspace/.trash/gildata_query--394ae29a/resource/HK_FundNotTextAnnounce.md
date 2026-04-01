# HK_FundNotTextAnnounce

**中文名**: 香港基金公告原文非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundNotTextAnnounce` |
| MySQL表名 | `hk_fundnottextannounce` |
| 中文名 | 香港基金公告原文非文本 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录了香港互认基金、港交所ETF的招募说明书、基金上市公告书、基金扩募说明书、基金契约、基金招募说明书更新摘要、基金招募说明书更新、基金契约修正、基金托管协议、年报、中报、季报等定期公告、临时公告。
2.信息来源：证监会、港交所、基金公司
3.数据范围：1999年至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码(InnerCode): 与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublTime` | 信息发布时间点 | varchar2(8) | ✓ | 56.41% |  |
| 6 | `Media` | 媒体出处 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `EndDate` | 截止日期 | date | ✓ | 2.95% |  |
| 8 | `ContentType` | 内容类别 | number(10) | ✓ | 78.86% | 内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1033，得到内容类... |
| 9 | `InfoTitle` | 信息标题 | nvarchar2(2000) | ✓ | 100.0% |  |
| 10 | `SerialNumber` | 序号 | number(10) | ✓ | 0.23% |  |
| 11 | `SubTitle` | 小标题 | nvarchar2(400) | ✓ | 0.26% |  |
| 12 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 13 | `LanguageType` | 语言类别 | number(10) | ✓ | 100.0% | 语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言... |
| 14 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 15 | `FileName` | 文件名 | nvarchar2(2000) | ✓ | 100.0% |  |
| 16 | `InfoType` | 信息类别 | number(10) | ✓ | 78.86% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到信息类别的具... |
| 17 | `HashCode` | MD5校验码 | varchar2(100) | ✗ | 100.0% |  |
| 18 | `Website` | 网页地址 | varchar2(500) | ✓ | 50.3% |  |
| 19 | `FileSize` | 文件大小(KB) | number(19,3) | ✗ | 100.0% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码(InnerCode): 与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的证券代码、基金简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司代码、简称等。

### ContentType (内容类别)

内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1033，得到内容类别的具体描述：1-招股文件，4-基础上市文件，5-业绩公告，53-财务报表，55-公司简介(创业板)，131-公告，134-新上市股份配发结果，137-证券回购，140-信息表，143-交易安排，146-更改董事\监事\公司管理层人员，149-股东大会通告，152-委任表格，155-股东大会结果，158-外汇基金债券_投标通告，161-通函，199-其它，200-股东特别大会结果，201-股东特别大会通告。

### LanguageType (语言类别)

语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言类别的具体描述：1-简体中文，2-英文，3-简体中文(境外版)，5-繁体中文。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到信息类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

## SQL示例

```sql
-- 查询 香港基金公告原文非文本 数据
SELECT *
FROM hk_fundnottextannounce
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
