# LC_TrustAssetPortfolio

**中文名**: 信托公司资产分布

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_TrustAssetPortfolio` |
| MySQL表名 | `lc_trustassetportfolio` |
| 中文名 | 信托公司资产分布 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 半年度更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.反映信托类企业年度报告中特有的指标数据，包括资产分布、资产运用、固有业务投资情况等内容。
2.数据范围：2013-12-31至今。
3.信息来源：信托公司年度报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码(CompanyCode)：与“证券主表(SecuMain)”中的“公司代码(CompanyCode)”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 99.99% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)：1-合并未调整，2-母公司未调整。 |
| 7 | `IndiCategory` | 指标类别 | number(10) | ✓ | 100.0% | 指标类别(IndiCategory)与(LC_BankIndiConst)表中的ConstantCode字段关联，令Co... |
| 8 | `IndexName` | 指标名称 | varchar2(150) | ✗ | 100.0% |  |
| 9 | `IndicatorCode` | 指标代码 | number(10) | ✓ | 100.0% | 指标代码(IndicatorCode)与(LC_BankIndiConst)表中的ConstantCode字段关联，令C... |
| 10 | `OpeningValue` | 期初值 | number(19,4) | ✓ | 38.68% |  |
| 11 | `CurrentAccrual` | 本期计提 | number(19,4) | ✓ | 0.0% |  |
| 12 | `CurrentWriteBack` | 本期转回 | number(19,4) | ✓ | 0.0% |  |
| 13 | `CurrentWriteoff` | 本期核销 | number(19,4) | ✓ | 0.0% |  |
| 14 | `EndingValue` | 期末值 | number(19,4) | ✓ | 97.99% |  |
| 15 | `Ratio` | 资产占比(%) | number(19,4) | ✓ | 19.93% |  |
| 16 | `IndicatorUnit` | 指标单位 | number(10) | ✓ | 100.0% | 指标单位(IndicatorUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1890 and... |
| 17 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and ... |
| 18 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码(CompanyCode)：与“证券主表(SecuMain)”中的“公司代码(CompanyCode)”关联，得到上市公司的交易代码、简称等。非上市非发债的公司与“机构基本资料(LC_InstiArchive)”中的“公司代码(CompanyCode)”关联，得到对应公司的基本信息。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 and DM = 110101，得到信息来源编码的具体描述：110101-定期报告:年度报告。

### Mark (合并调整标志)

合并调整标志(Mark)：1-合并未调整，2-母公司未调整。

### IndiCategory (指标类别)

指标类别(IndiCategory)与(LC_BankIndiConst)表中的ConstantCode字段关联，令ConstantCategoryCode = 20 and ConstantCode in (2001,2002,2005,2007,2009)，得到指标类别的具体描述：2001-资产分布，2002-信托项目资产负债汇总及利润分配，2005-固有业务投资情况，2007-信托财产管理情况，2009-资产运用。

### IndicatorCode (指标代码)

指标代码(IndicatorCode)与(LC_BankIndiConst)表中的ConstantCode字段关联，令ConstantCategoryCode in (21,22,25,27,30)，得到指标代码的具体描述。

### IndicatorUnit (指标单位)

指标单位(IndicatorUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1890 and DM in (1,2,3,6,13,14)，得到指标单位的具体描述：1-元，2-千元，3-万元，6-亿元，13-个，14-%。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM = 1420，得到货币单位的具体描述：1420-人民币元。

## SQL示例

```sql
-- 查询 信托公司资产分布 数据
SELECT *
FROM lc_trustassetportfolio
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
