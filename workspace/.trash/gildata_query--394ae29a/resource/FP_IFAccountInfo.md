# FP_IFAccountInfo

**中文名**: 保险理财产品投资账户基本信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFAccountInfo` |
| MySQL表名 | `fp_ifaccountinfo` |
| 中文名 | 保险理财产品投资账户基本信息 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

收录保险理财投资账户的托管人、投资范围、资产组合比例、业绩比较基准等基本信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `FinProCode` | 账户编码 | varchar2(12) | ✗ | 100.0% | 账户编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）... |
| 3 | `AccountType` | 账户类型 | varchar2(12) | ✓ | 57.46% | 	 账户类型(AccountType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCo... |
| 4 | `InvestAdvisorName` | 管理人 | varchar2(12) | ✓ | 45.14% | 管理人(InvestAdvisorName)：与“企业码表（EP_CompanyMain）”中的“企业编码（Enterp... |
| 5 | `TrusteeName` | 托管人 | varchar2(12) | ✓ | 41.23% | 托管人(TrusteeName)：与“企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCo... |
| 6 | `InceptionDate` | 账户设立日期 | date | ✓ | 72.63% |  |
| 7 | `MaturityDate` | 账户终止日期 | date | ✓ | 6.75% |  |
| 8 | `InvestField` | 投资范围 | clob | ✓ | 70.5% |  |
| 9 | `InvestStrategy` | 投资策略 | clob | ✓ | 56.87% |  |
| 10 | `InvestRisk` | 投资风险 | clob | ✓ | 71.8% |  |
| 11 | `InvestTarget` | 投资目标 | clob | ✓ | 36.49% |  |
| 12 | `InvestType` | 投资对象 | varchar2(12) | ✓ | 68.01% | 投资对象(InvestType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 13 | `InvestDirection` | 投资方向 | varchar2(12) | ✓ | 51.54% | 投资方向(InvestDirection)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 14 | `PerformanceBenchMark` | 业绩比较基准 | varchar2(200) | ✓ | 47.16% |  |
| 15 | `InvestPortfolio` | 资产组合比例 | clob | ✓ | 72.04% |  |
| 16 | `MangementFeeRule` | 资产管理费用 | clob | ✓ | 63.63% |  |
| 17 | `InvestConcept` | 投资理念 | clob | ✓ | 2.49% |  |
| 18 | `ProductFeatures` | 产品特征 | clob | ✓ | 49.29% |  |
| 19 | `MaturityYieldDesc` | 收益说明 | clob | ✓ | 1.18% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (账户编码)

账户编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到账户的名称等信息。

### AccountType (账户类型)

	
账户类型(AccountType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到账户类型的具体描述：FCC000000Y1M-股票型，FCC000000Y1P-混合型，FCC000000Y1O-货币型，FCC000000Y1N-债券型，FCC000000YLL-指数型，FCC000001650-基金型，CC000000Y1R-QDII。

### InvestAdvisorName (管理人)

管理人(InvestAdvisorName)：与“企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到管理人的具体名称、基本信息等。

### TrusteeName (托管人)

托管人(TrusteeName)：与“企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到托管人的具体名称、基本信息等。

### InvestType (投资对象)

投资对象(InvestType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资对象的具体描述：FCC0000001T9-权益类，FCC0000001T8-固定收益类，FCC0000001TB-混合类。

### InvestDirection (投资方向)

投资方向(InvestDirection)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资方向的具体描述：FCC0000001T9-权益类，FCC000000G3T-债券类别，FCC0000001WR-货币市场工具，FCC000001651-平衡混合类，FCC000001652-混合偏股，FCC000001653-混合偏债。

## SQL示例

```sql
-- 查询 保险理财产品投资账户基本信息 数据
SELECT *
FROM fp_ifaccountinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
