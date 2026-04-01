# LC_BankLoan

**中文名**: 银行贷款类细分指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_BankLoan` |
| MySQL表名 | `lc_bankloan` |
| 中文名 | 银行贷款类细分指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 金融公司专项指标 |
| 更新频率 | 季更新 |
| 字段数量 | 19 |
| 版本 | 1.03 |

## 表描述

1.本表记录银行各类贷款余额，包括按产品分、按行业分、按地区、按期限分等细项。
2.数据范围：2011-12-31至今
3.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(300) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志（Mark）：1-合并调整；2-合并未调整；3-母公司调整；4-母公司未调整 |
| 8 | `IndicatorType` | 指标类别 | number(10) | ✓ | 100.0% | 指标类别（IndicatorType）：1002-贷款类、1006-贷款及不良贷款、1005005-流动性风险_资产负债... |
| 9 | `IndicatorName` | 指标名称 | varchar2(200) | ✓ | 100.0% | 数据源披露的原始名称  |
| 10 | `IndicatorCode` | 标准指标代码 | number(10) | ✓ | 100.0% | 进行标准化后的科目名称，代码对应的标准名称参看LC_BankIndiConst |
| 11 | `DataDimension` | 数据维度 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `DataDimensionCode` | 数据维度编码 | number(10) | ✓ | 100.0% | 数据维度编码（DataDimensionCode）固定常量：10001-本期_指标金额，10002-本期_占总额比例(%... |
| 13 | `DataValue` | 指标数据 | number(19,4) | ✗ | 100.0% |  |
| 14 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 15 | `Unit` | 指标单位 | number(10) | ✓ | 100.0% | 指标单位（Unit）：1-元；3-千元；4-万元；6-百万元；8-亿 |
| 16 | `Remark` | 备注说明 | varchar2(1000) | ✓ | 0.0% |  |
| 17 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 18 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### Mark (合并调整标志)

合并调整标志（Mark）：1-合并调整；2-合并未调整；3-母公司调整；4-母公司未调整

### IndicatorType (指标类别)

指标类别（IndicatorType）：1002-贷款类、1006-贷款及不良贷款、1005005-流动性风险_资产负债到期日分析、1005001-市场风险_利率风险、1005006-流动性风险_合同现金流到期日分析。

### IndicatorName (指标名称)

数据源披露的原始名称 

### IndicatorCode (标准指标代码)

进行标准化后的科目名称，代码对应的标准名称参看LC_BankIndiConst

### DataDimensionCode (数据维度编码)

数据维度编码（DataDimensionCode）固定常量：10001-本期_指标金额，10002-本期_占总额比例(%),10003-本期_不良贷款金额，10004-本期_不良贷款率(%)，10005-本期_较上年末增减变动(%)。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM=1420，得到货币单位的具体描述：1420-人民币元。

### Unit (指标单位)

指标单位（Unit）：1-元；3-千元；4-万元；6-百万元；8-亿

## SQL示例

```sql
-- 查询 银行贷款类细分指标 数据
SELECT *
FROM lc_bankloan
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
