# CS_StkOpStatusNotText

**中文名**: 股票定报经营情况述评-非文本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StkOpStatusNotText` |
| MySQL表名 | `cs_stkopstatusnottext` |
| 中文名 | 股票定报经营情况述评-非文本 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：收录公司第一季度、半年度、第三季度和年度报告中“其他重要事项”、“管理层讨论与分析”、'公司治理'、'环境与社会责任'等章节内容，以html文件格式呈现。
2.数据范围：截止日期由2021-12-31至今。
3.信息来源：上交所、深交所、北交所、全国股转系统的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 6 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 7 | `HashCode` | 文件校验码 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `FileSize` | 文件大小(KB) | number(19,3) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 股票定报经营情况述评-非文本 数据
SELECT *
FROM cs_stkopstatusnottext
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
