# DZ_Business

**中文名**: 公司经营范围与行业变更

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_Business` |
| MySQL表名 | `dz_business` |
| 中文名 | 公司经营范围与行业变更 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

内容说明：收录上市公司（包括科创板）、发债公司的经营范围（包括主营和兼营）以及涉足行业情况。
数据范围：国内上市公司、发债公司
信息来源：招股说明书、董事会决议、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.98% |  |
| 5 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 21.7% |  |
| 6 | `IfPassed` | 是否否决 | number(10) | ✓ | 100.0% | 是否否决(IfPassed)，该字段固定以下常量：0-否；1-是 |
| 7 | `BusinessMajor` | 经营范围-主营 | clob | ✓ | 1.41% |  |
| 8 | `BusinessMinor` | 经营范围-兼营 | clob | ✓ | 41.66% |  |
| 9 | `MainBusiness` | 主要业务 | varchar2(2000) | ✓ | 96.75% |  |
| 10 | `MainName` | 主要产品与业务名称 | clob | ✓ | 29.63% |  |
| 11 | `IndustryType` | 行业类别 | number(10) | ✓ | 100.0% | 行业类别(IndustryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 and ... |
| 12 | `CSRCInduCategory` | 行业代码 | number(10) | ✓ | 99.59% |  |
| 13 | `InduEngaged` | 涉足行业 | number(10) | ✓ |  |  |
| 14 | `ChangeReason` | 变更原因 | varchar2(255) | ✓ | 0.05% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfPassed (是否否决)

是否否决(IfPassed)，该字段固定以下常量：0-否；1-是

### IndustryType (行业类别)

行业类别(IndustryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 and DM in (1,22)，得到行业类别的具体描述：

## SQL示例

```sql
-- 查询 公司经营范围与行业变更 数据
SELECT *
FROM dz_business
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
