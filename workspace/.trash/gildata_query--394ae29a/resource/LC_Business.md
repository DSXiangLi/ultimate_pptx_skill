# LC_Business

**中文名**: 公司经营范围与行业变更

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Business` |
| MySQL表名 | `lc_business` |
| 中文名 | 公司经营范围与行业变更 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.收录上市公司、发债公司的经营范围（包括主营和兼营）以及涉足行业情况。
2.信息来源：公开转让说明书、董事会决议、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.98% |  |
| 5 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 22.05% |  |
| 6 | `IfPassed` | 是否否决 | char(2) | ✓ | 100.0% | 是否否决(IfPassed)，该字段固定以下常量：0-否；1-是 |
| 7 | `BusinessMajor` | 经营范围-主营 | clob | ✓ | 1.14% |  |
| 8 | `BusinessMinor` | 经营范围-兼营 | clob | ✓ | 42.01% |  |
| 9 | `MainBusiness` | 主要业务 | varchar2(2000) | ✓ | 96.68% |  |
| 10 | `MainName` | 主要产品与业务名称 | varchar2(2000) | ✓ | 64.71% |  |
| 11 | `IndustryType` | 行业类别 | number(10) | ✓ | 100.0% | 行业类别(IndustryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 and ... |
| 12 | `CSRCInduCategory` | 行业代码 | number(10) | ✓ | 99.56% | 行业代码（CSRCInduCategory）：当行业类别（IndustryType）=1时，与行业表（CT_Indust... |
| 13 | `InduEngaged` | 涉足行业 | varchar2(100) | ✓ |  |  |
| 14 | `ChangeReason` | 变更原因 | varchar2(255) | ✓ | 0.05% |  |
| 15 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfPassed (是否否决)

是否否决(IfPassed)，该字段固定以下常量：0-否；1-是

### IndustryType (行业类别)

行业类别(IndustryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 and DM in (1,22)，得到行业类别的具体描述：1-CSRC行业分类，22-证监会行业分类2012版。

### CSRCInduCategory (行业代码)

行业代码（CSRCInduCategory）：当行业类别（IndustryType）=1时，与行业表（CT_Industry）中行业编码（IndustryNum）关联，得到CSRC行业分类标准下的行业名称；当行业类别（IndustryType）=22时，与系统常量表(CT_SystemConst)中的DM字段关联，令LB=1755，得到证监会行业分类2012版分类标准下的行业名称。

## SQL示例

```sql
-- 查询 公司经营范围与行业变更 数据
SELECT *
FROM lc_business
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
