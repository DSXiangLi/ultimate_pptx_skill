# LC_Mshareholder

**中文名**: 大股东介绍

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Mshareholder` |
| MySQL表名 | `lc_mshareholder` |
| 中文名 | 大股东介绍 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 25 |
| 版本 | 1.02 |

## 表描述

1.收录上市公司及发债企业大股东的基本资料，包括直接持股和间接持股，以及持股比例、背景介绍等内容。
2.数据范围：2004-12-31至今
3.信息来源：募集说明书、招股说明书、定报、临时公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✓ | 66.66% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 97.61% |  |
| 6 | `BulletinType` | 公告类别 | number(10) | ✓ | 31.4% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 7 | `MSHName` | 股东名称 | varchar2(120) | ✗ | 100.0% |  |
| 8 | `SHAttribute` | 股东性质 | number(10) | ✓ | 100.0% | 股东性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东性... |
| 9 | `GDID` | 股东ID | number(10) | ✓ | 79.88% | 股东ID（GDID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企... |
| 10 | `MSHPercentage` | 持股比例 | number(9,6) | ✓ | 81.74% |  |
| 11 | `MSHNumber` | 股东地位 | number(10) | ✓ | 100.0% | 股东地位(MSHNumber)与(CT_SystemConst)表中的DM字段关联，令LB = 1198，得到股东地位的... |
| 12 | `GetMethod` | 股权获取方式 | number(10) | ✓ | 25.77% | 股权获取方式(GetMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1200，得到股权获... |
| 13 | `LegalRepr` | 法人代表 | varchar2(50) | ✓ | 9.24% |  |
| 14 | `RegCapital` | 注册资本(元) | number(19,4) | ✓ | 10.11% |  |
| 15 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 10.1% | 货币单位（CurrencyUnit）与（CT_SystemConst）中的DM字段关联，令LB=1068，得到注册资本的... |
| 16 | `MainBusiness` | 主营业务 | varchar2(255) | ✓ | 9.05% |  |
| 17 | `EconomicNature` | 经济性质 | number(10) | ✓ |  |  |
| 18 | `NationalityDesc` | 国籍描述 | varchar2(256) | ✓ | 9.93% |  |
| 19 | `PermanentResidency` | 永久其他国家或地区居留权 | varchar2(256) | ✓ | 6.92% |  |
| 20 | `BackgroundIntr` | 背景介绍 | clob | ✓ | 26.38% |  |
| 21 | `IfExisted` | 存在与否 | number(10) | ✓ | 100.0% | 存在与否（IfExisted）)，该字段固定以下常量：1-有；0-无 |
| 22 | `StructureChart` | 实际控制人结构图 | blob | ✓ | 0.46% |  |
| 23 | `FileType` | 文件格式 | number(10) | ✓ | 6.68% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具... |
| 24 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### SHAttribute (股东性质)

股东性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### GDID (股东ID)

股东ID（GDID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

### MSHNumber (股东地位)

股东地位(MSHNumber)与(CT_SystemConst)表中的DM字段关联，令LB = 1198，得到股东地位的具体描述：1-第1大股东，2-第2大股东，3-第3大股东，4-其他股东，5-潜在第1大股东，6-其他潜在股东，9-实际控制人，10-潜在实际控制人。

### GetMethod (股权获取方式)

股权获取方式(GetMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1200，得到股权获取方式的具体描述：1-上市前股东，2-受让股权，3-股东重组，4-股权受托，5-其他。

### CurrencyUnit (货币单位)

货币单位（CurrencyUnit）与（CT_SystemConst）中的DM字段关联，令LB=1068，得到注册资本的货币单位具体描述：
1000-美元 1100-港元 1420-人民币元 3000-欧元 

### IfExisted (存在与否)

存在与否（IfExisted）)，该字段固定以下常量：1-有；0-无

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309，得到文件格式的具体描述：1-PDF，2-DOC，3-TXT，4-XLS，5-HTML，6-RTF，7-MHT，8-RAR，9-PPT，10-JPG，11-DOCX，12-XLSX，13-PPTX，14-EML，15-ZIP，16-DOCM，17-XLSM，18-XLSB，19-DOTX，20-XML，21-GIF，22-PAPER，23-FIL，24-XSD，25-HTM，26-BMP，27-SWF，28-PNG，29-JSON，30-TIFF，31-TIF，32-WPS，33-GD，34-ET，35-SHTML，36-WEBP，37-7Z，38-CUR，39-SVG，40-ETT，41-OFD，42-JPEG，43-MP3，44-MP4，45-CEB，46-GZ。

## SQL示例

```sql
-- 查询 大股东介绍 数据
SELECT *
FROM lc_mshareholder
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
