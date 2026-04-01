# LC_InvestorRa

**中文名**: 投资者关系活动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_InvestorRa` |
| MySQL表名 | `lc_investorra` |
| 中文名 | 投资者关系活动 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 不定时更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.收录各调研机构对上市公司调研的详情，包括调研日期、参与单位、调研人员、调研主要内容等信息。
2.数据范围：2012-至今
3.信息来源：巨潮，上交所互动易和深交所互动易

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `Nbcode` | 编号 | varchar2(40) | ✓ | 85.98% |  |
| 5 | `ReceptionDate` | 接待日期 | date | ✗ | 100.0% |  |
| 6 | `ReceptionDateE` | 接待日期截止日 | date | ✗ | 100.0% |  |
| 7 | `ReceptionDaTime` | 接待时间 | varchar2(100) | ✓ | 57.53% |  |
| 8 | `SerialNb` | 序号 | number(10) | ✓ | 100.0% |  |
| 9 | `ActivitiesCate` | 活动类别 | number(10) | ✓ |  |  |
| 10 | `Participant` | 参与单位及人员 | varchar2(4000) | ✓ | 96.73% |  |
| 11 | `Place` | 地点 | varchar2(500) | ✓ | 94.55% |  |
| 12 | `ListingCreper` | 上市公司接待人员 | varchar2(4000) | ✓ | 98.17% |  |
| 13 | `TmainContent` | 主要内容 | clob | ✓ | 2.24% |  |
| 14 | `ArticleFile` | 附件 | blob | ✓ | 6.38% |  |
| 15 | `FileType` | 附件格式 | number(10) | ✓ | 100.0% | 附件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到附件格式的具... |
| 16 | `InfoTitle` | 标题 | varchar2(200) | ✓ | 100.0% |  |
| 17 | `LinkAddress` | 链接地址 | varchar2(500) | ✓ | 91.11% |  |
| 18 | `UpdateTime` | 更新时间 | date | ✓ |  |  |
| 19 | `JSID` | JSID | number(19) | ✓ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### FileType (附件格式)

附件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到附件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 投资者关系活动 数据
SELECT *
FROM lc_investorra
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
