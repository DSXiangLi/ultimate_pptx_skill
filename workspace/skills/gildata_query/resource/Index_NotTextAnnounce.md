# Index_NotTextAnnounce

**中文名**: 指数公告非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_NotTextAnnounce` |
| MySQL表名 | `index_nottextannounce` |
| 中文名 | 指数公告非文本 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数公告资讯 |
| 更新频率 | 滚动更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.收录了指数发布机构发布的指数编制和发布、指数编制方案、指数成份股调整、指数发布状态调整等公告的原文。
2.历史数据：2002年07月至今
3.数据源：中证指数有限公司、上海证券交易所、深圳证券交易所、深圳证券信息有限公司、申银万国研究所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 指数内部编码 | number(10) | ✓ | 100.0% | 指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `Media` | 媒体出处 | varchar2(100) | ✓ | 87.39% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `InfoTitle` | 信息标题 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `Content` | 信息内容 | blob | ✓ | 0.26% |  |
| 9 | `LanguageType` | 语言类别 | number(10) | ✓ | 100.0% | 语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言... |
| 10 | `FileType` | 文件格式 | number(10) | ✓ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 11 | `InvolvedStock` | 相关股票 | number(10) | ✓ |  |  |
| 12 | `AnnouncementLink` | 公告链接 | varchar2(1000) | ✓ | 78.36% |  |
| 13 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (指数内部编码)

指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### LanguageType (语言类别)

语言类别(LanguageType)与(CT_SystemConst)表中的DM字段关联，令LB = 1238，得到语言类别的具体描述：1-简体中文，2-英文，3-简体中文(境外版)，5-繁体中文。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM。

## SQL示例

```sql
-- 查询 指数公告非文本 数据
SELECT *
FROM index_nottextannounce
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
