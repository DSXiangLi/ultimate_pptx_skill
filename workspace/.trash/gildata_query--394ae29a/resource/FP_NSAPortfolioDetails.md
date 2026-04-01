# FP_NSAPortfolioDetails

**中文名**: 金融产品投资组合非标明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_NSAPortfolioDetails` |
| MySQL表名 | `fp_nsaportfoliodetails` |
| 中文名 | 金融产品投资组合非标明细 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品投资组合 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录金融产品的投资类型，投资对象，投资对象持仓市值，占净值比等信息
2.信息来源：银行、信托、证券公司官网披露的季报等
3.数据范围：2024-12-1-至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% |  |
| 3 | `SecuCategory` | 证券类别 | varchar2(12) | ✗ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 7 | `TradingDirection` | 交易方向 | varchar2(12) | ✗ | 100.0% | 交易方向(TradingDirection)：FCC000000FJP-买入,FCC000000E56-卖出,FCC00... |
| 8 | `EnterpriseCode` | 融资企业编码 | varchar2(12) | ✗ | 100.0% | 融资企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（Enter... |
| 9 | `CompanyCode` | 融资公司代码 | number(10) | ✓ | 90.76% | 融资公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compan... |
| 10 | `ProjectName` | 项目名称 | varchar2(150) | ✗ | 100.0% |  |
| 11 | `ProjectDesc` | 项目说明 | varchar2(1000) | ✓ | 0.0% |  |
| 12 | `ObtainPrice` | 项目购入金额(元) | number(19,6) | ✓ | 36.97% |  |
| 13 | `TradingValue` | 项目交易金额(元) | number(19,6) | ✓ | 39.78% |  |
| 14 | `RemainFinMaturity` | 剩余融资期限 | number(10,2) | ✓ | 79.55% |  |
| 15 | `RemainFinMaturityUnit` | 剩余融资期限单位 | varchar2(12) | ✓ | 51.82% |  |
| 16 | `MaturityDate` | 到期日期 | date | ✓ | 90.2% |  |
| 17 | `Yield` | 资产收益率 | number(18,9) | ✓ | 42.86% |  |
| 18 | `IfAnnualized` | 是否年化 | varchar2(12) | ✓ | 22.41% |  |
| 19 | `InvestObject` | 交易结构类型 | varchar2(12) | ✓ | 79.55% | 交易结构类型(InvestObject)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilC... |
| 20 | `InvestObjectDesc` | 交易结构描述 | varchar2(50) | ✓ | 90.48% |  |
| 21 | `RatioInNV` | 占投资组合净资产比例 | number(18,6) | ✓ | 0.0% |  |
| 22 | `RiskDesc` | 风险状况 | varchar2(200) | ✓ | 57.42% |  |
| 23 | `Remark` | 备注说明 | varchar2(500) | ✓ | 0.28% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### TradingDirection (交易方向)

交易方向(TradingDirection)：FCC000000FJP-买入,FCC000000E56-卖出,FCC000001IFX-持有

### EnterpriseCode (融资企业编码)

融资企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyCode (融资公司代码)

融资公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### InvestObject (交易结构类型)

交易结构类型(InvestObject)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资对象的具体描述：FCC0000001WV-同业借款，CFN0000002IA-股权投资，FCC000001E94-收/受益权，FCC000001E95-债权投资计划和资产支持计划，FCC0000001WS-理财直接融资工具，FCC000001EA2-收益凭证，CFN0000002NK-信托贷款，CBS000000055-委托贷款，CFN0000008MT-委托债权，CBS000000009-应收账款，CFN0000001E5-债权融资计划，FCC000001E97-信贷资产流转，CFN0000009IH-资产转让。

## SQL示例

```sql
-- 查询 金融产品投资组合非标明细 数据
SELECT *
FROM fp_nsaportfoliodetails
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
