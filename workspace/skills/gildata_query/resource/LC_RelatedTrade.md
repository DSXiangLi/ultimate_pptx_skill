# LC_RelatedTrade

**中文名**: 公司关联交易明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_RelatedTrade` |
| MySQL表名 | `lc_relatedtrade` |
| 中文名 | 公司关联交易明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定时更新 |
| 字段数量 | 25 |
| 版本 | 1.03 |

## 表描述

1.收录上市公司中披露的与关联企业之间的各类关联交易，包括购买商品、接受劳务、销售商品、应收帐款、支付费用、支付利息、租赁、资产重组、提供担保等等30多个类型。
2.数据范围：2002年-至今
3.信息来源：上市公司临时公告、定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 98.75% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoSourceType` | 信息来源类型 | number(10) | ✓ | 99.28% | 信息来源类型(InfoSourceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1039，... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `RelatedParty` | 关联方名称 | varchar2(120) | ✗ | 100.0% |  |
| 8 | `Association` | 关联关系 | number(10) | ✓ | 100.0% | 关联关系(Association)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到关联关... |
| 9 | `TradeType` | 交易类型 | number(10) | ✓ | 99.99% | 交易类型(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB=1038，得到交易类型的具体... |
| 10 | `TradeSum` | 交易金额(元) | number(19,4) | ✓ | 96.4% |  |
| 11 | `TradeContent` | 具体交易内容 | varchar2(255) | ✓ | 23.21% |  |
| 12 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |
| 14 | `RatioInProject` | 占项目总额比例 | number(9,6) | ✓ | 5.86% | 占项目总额比例（RatioInProject）：该字段已停止维护。 |
| 15 | `PricingMethod` | 定价原则 | number(10) | ✓ | 1.67% | 定价原则（PricingMethod）：该字段已停止维护。 |
| 16 | `PaymentMeans` | 支付方式 | varchar2(100) | ✓ | 0.15% | 支付方式（PaymentMeans）：该字段已停止维护。 |
| 17 | `ConfirmedDate` | 确定时间 | date | ✓ | 0.17% | 确定时间（ConfirmedDate）：该字段已停止维护。 |
| 18 | `IndeFinaAdvisor` | 独立财务顾问 | varchar2(255) | ✓ | 0.26% | 独立财务顾问（IndeFinaAdvisor）：该字段已停止维护。 |
| 19 | `FinancialEffect` | 财务影响 | varchar2(255) | ✓ | 0.01% | 财务影响（FinancialEffect）：该字段已停止维护。 |
| 20 | `TradeChangeInfo` | 交易变更情况 | number(10) | ✓ | 0.01% | 交易变更情况（TradeChangeInfo）：该字段已停止维护。 |
| 21 | `TradeChangeDate` | 交易变更公告日期 | date | ✓ | 0.01% | 交易变更公告日期（TradeChangeDate）：该字段已停止维护。 |
| 22 | `Media` | 媒体出处 | varchar2(80) | ✓ | 13.01% | 媒体出处（Media）：该字段已停止维护。 |
| 23 | `RelatedPartyCode` | 关联方代码 | number(10) | ✓ | 86.17% |  |
| 24 | `CurrencyCode` | 币种 | number(10) | ✓ | 97.99% |  |
| 25 | `SettlemtMethod` | 结算方式 | varchar2(300) | ✓ | 32.4% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoSourceType (信息来源类型)

信息来源类型(InfoSourceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1039，得到信息来源类型的具体描述：1-定期报告，2-临时公告，3-招股上市书。

### Association (关联关系)

关联关系(Association)与(CT_SystemConst)表中的DM字段关联，令LB = 1036，得到关联关系的具体描述：1-本公司，2-母公司，3-控股股东，4-非控股股东，5-兄弟企业，8-间接非控股股东，9-同一领导人、亲属关系，10-下属子公司、参股公司，11-项目合作合资方，12-其他关联关系，51-间接兄弟企业，80-间接控股股东，83-潜在控股股东，84-潜在非控股股东，86-转让前控股股东，87-转让前非控股股东，121-股权受托管理人，122-受同一方控制，999-无关联关系。

### TradeType (交易类型)

交易类型(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB=1038，得到交易类型的具体描述：1-销售商品，2-购买商品，3-提供资金，4-接受资金，5-提供担保，6-接受担保，7-租赁专利、土地、商标，8-租赁有形资产，9-购买无形资产，10-购买有形资产，11-资产与股权转让，12-资产置换-置入资产，13-提供劳务，14-接受劳务，15-应收帐款，16-其它应收款项，17-应付帐款，18-其它应付款，19-支付费用，20-收取费用，21-支付利息，22-收取利息，23-代收货款，24-其他，25-预付帐款，26-预收帐款，27-资产置换-置出资产，28-短期投资，29-长期投资，30-应付票据，31-应收票据，32-资产委托管理，33-接受资产托管，34-债务重组，35-委托投资，36-长期应付款，38-合资合作，39-工程承包，40-采购商品或接受劳务，41-销售商品或提供劳务。

### RatioInProject (占项目总额比例)

占项目总额比例（RatioInProject）：该字段已停止维护。

### PricingMethod (定价原则)

定价原则（PricingMethod）：该字段已停止维护。

### PaymentMeans (支付方式)

支付方式（PaymentMeans）：该字段已停止维护。

### ConfirmedDate (确定时间)

确定时间（ConfirmedDate）：该字段已停止维护。

### IndeFinaAdvisor (独立财务顾问)

独立财务顾问（IndeFinaAdvisor）：该字段已停止维护。

### FinancialEffect (财务影响)

财务影响（FinancialEffect）：该字段已停止维护。

## SQL示例

```sql
-- 查询 公司关联交易明细 数据
SELECT *
FROM lc_relatedtrade
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
