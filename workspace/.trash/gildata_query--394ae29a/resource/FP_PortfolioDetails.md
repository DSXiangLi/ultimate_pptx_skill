# FP_PortfolioDetails

**中文名**: 金融产品投资组合明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_PortfolioDetails` |
| MySQL表名 | `fp_portfoliodetails` |
| 中文名 | 金融产品投资组合明细 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品投资组合 |
| 更新频率 | 季度更新 |
| 字段数量 | 24 |
| 版本 | 1.05 |

## 表描述

1.内容说明：本表收录银行理财、券商资管、保险资管和养老金产品的投资类型，投资对象，投资对象持仓市值，占净值比等信息，本表币种单位为金融产品概况表的币种（FP_BasicInfo表单CurrencyUnit字段）。
注：产品若存在多份额情况，会多次存储，可通过限制FP_BasicInfo表单IfInitialShare='FCC000000005'，每个产品仅取一次数据。
2.信息来源：银行、证券公司、资产管理公司、保险公司官方的定期报告等。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ReportType` | 报告类型 | varchar2(12) | ✗ | 100.0% | 报告类型(ReportType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `AdjustMark` | 调整标志 | varchar2(12) | ✓ | 100.0% | 调整标志(AdjustMark)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 9 | `InvestType` | 投资类型 | varchar2(12) | ✓ | 100.0% | 投资类型(InvestType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 10 | `PenetrationType` | 穿透类型 | varchar2(12) | ✓ | 96.87% | 穿透类型（PenetrationType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（Gil... |
| 11 | `InvestObject` | 投资对象 | varchar2(12) | ✓ | 99.63% | 投资对象(InvestObject)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 12 | `IfNonStandardAssets` | 是否非标资产 | varchar2(12) | ✓ | 96.53% | 是否非标资产（IfNonStandardAssets）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标... |
| 13 | `DetailType` | 投资明细类别 | varchar2(12) | ✓ | 99.1% | 投资明细类别(DetailType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 14 | `SerialNumber` | 序号 | number(10) | ✓ | 90.0% |  |
| 15 | `SecuCode` | 证券代码(披露) | varchar2(50) | ✓ | 47.32% |  |
| 16 | `SecuName` | 证券名称 | varchar2(200) | ✗ | 100.0% |  |
| 17 | `InnerCode` | 证券内部编码 | varchar2(12) | ✓ | 66.38% | 证券内部编码(InnerCode)：与“证券码表总表(SecuMainAll) ”中的“聚源代码（GilCode）”关联... |
| 18 | `SharesHolding` | 持仓数量(股) | number(19,2) | ✓ | 13.91% |  |
| 19 | `MarketValue` | 持仓市值(元) | number(19,4) | ✓ | 99.32% |  |
| 20 | `RatioInNV` | 占净值比 | number(18,6) | ✓ | 50.45% |  |
| 21 | `Remark` | 备注说明 | varchar2(500) | ✓ | 4.88% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### ReportType (报告类型)

报告类型(ReportType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到信息来源代码的具体描述：FCC00000005E-定期报告:年度报告，FCC00000005F-定期报告:半年度报告，FCC000000YHK-定期报告:季度报告，FCC0000014SJ-定期报告:月度报告，FCC0000019BW-定期报告:周度报告，FCC000000YHL-临时报告，FCC0000002PW-成立公告，FCC000001CSB-到期清算公告，FIC0000000XS-其他公告分类。

### AdjustMark (调整标志)

调整标志(AdjustMark)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到调整标志的具体描述：FCC000000YHJ-调整前，FCC000000YHI-最新调整。

### InvestType (投资类型)

投资类型(InvestType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资类型的具体描述：FCC000000YHM-综合投资，FCC000000YHN-积极投资，FCC000000YHO-指数投资。

### PenetrationType (穿透类型)

穿透类型（PenetrationType）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到穿透类型的具体描述：FCC0000019PK-穿透前，FCC0000019PL-穿透后。

### InvestObject (投资对象)

投资对象(InvestObject)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资对象的具体描述：FCC0000001WJ-股票，FCC000000YHP-港股，FCC0000001WL-债券，CFN0000001H1-转股期可转债，FCC0000001WQ-资产支持证券，CFN0000008TM-资产证券化产品，FCC0000001WK-基金，FCC000000HE-权证，FCC000000SO6-远期外汇合约，FCC00000139U-期权，FCC000000YHQ-期货，CFN000000274-理财产品/信托计划及资产管理计划，FCC0000001D1-其他资产，FCC000000CIH-现金及银行存款，FCC000000N3P-买入返售金融资产，FCC0000001WP-同业存单，FCC0000001WV-同业借款，CFN0000002IA-股权投资，FCC000001E94-收/受益权，FCC000001E95-债权投资计划和资产支持计划，FCC0000001WS-理财直接融资工具，FCC000001EA2-收益凭证，CFN0000002NK-信托贷款，CBS000000055-委托贷款，CFN0000008MT-委托债权，CBS000000009-应收账款，CFN0000001E5-债权融资计划，FCC000001E97-信贷资产流转，CFN0000009IH-资产转让。

### IfNonStandardAssets (是否非标资产)

是否非标资产（IfNonStandardAssets）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否非标资产的具体描述：FCC000000005-是，FCC000000006-否。

### DetailType (投资明细类别)

投资明细类别(DetailType)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到投资明细类别的具体描述：FCC000000YHR-重仓，FCC0000001S3-全部。

### InnerCode (证券内部编码)

证券内部编码(InnerCode)：与“证券码表总表(SecuMainAll) ”中的“聚源代码（GilCode）”关联，得到证券内部编码的中文简称。

## SQL示例

```sql
-- 查询 金融产品投资组合明细 数据
SELECT *
FROM fp_portfoliodetails
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
