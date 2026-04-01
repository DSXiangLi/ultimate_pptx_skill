# MF_REITsIncomeST

**中文名**: REITs项目公司利润分配表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsIncomeST` |
| MySQL表名 | `mf_reitsincomest` |
| 中文名 | REITs项目公司利润分配表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 半年度更新 |
| 字段数量 | 80 |
| 版本 | 1 |

## 表描述

1.内容说明：收录项目公司年报、中报、季报、招募说明书中披露的利润表数据。
2.数据范围：2021-至今
3.信息来源：基金招募说明书、定报等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSourceCode` | 信息来源编码 | varchar2(12) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)：与“指标码表（IndicatorMain）”中的“聚源指标代码（GilCo... |
| 4 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码(CompanyCode)：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 5 | `InnerCode` | 基金内部编码 | number(10) | ✓ | 100.0% | 基金内部编码(InnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB=1188 and DM i... |
| 8 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM IN ... |
| 9 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455... |
| 10 | `IfDisclosure` | 是否披露值 | number(10) | ✗ | 100.0% | 是否披露值(IfDisclosure):1-是；2-否。 |
| 11 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM I... |
| 12 | `TotalOperatingRevenue` | 营业总收入 | number(19,4) | ✓ | 23.45% |  |
| 13 | `OperatingRevenue` | 营业收入 | number(19,4) | ✓ | 88.85% |  |
| 14 | `OtherOperatingRevenue` | 其他业务收入 | number(19,4) | ✓ | 0.0% |  |
| 15 | `SpecialItemsOR` | ##营业收入特殊项目OR营业总收入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 16 | `AdjustmentItemsOR` | ##营业收入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 17 | `TotalOperatingCost` | 营业总成本 | number(19,4) | ✓ | 17.26% |  |
| 18 | `OperatingCost` | 营业成本 | number(19,4) | ✓ | 95.4% |  |
| 19 | `OperatingTaxSurcharges` | 税金及附加 | number(19,4) | ✓ | 95.66% |  |
| 20 | `OperatingExpense` | 销售费用 | number(19,4) | ✓ | 30.18% |  |
| 21 | `AdministrationExpense` | 管理费用 | number(19,4) | ✓ | 89.91% |  |
| 22 | `RAndD` | 研发费用 | number(19,4) | ✓ | 3.01% |  |
| 23 | `FinancialExpense` | 财务费用 | number(19,4) | ✓ | 85.31% |  |
| 24 | `InterestFinExp` | 其中:利息费用 | number(19,4) | ✓ | 51.42% |  |
| 25 | `InterestIncome` | 其中:利息收入 | number(19,4) | ✓ | 47.26% |  |
| 26 | `SpecialItemsTOC` | ##营业支出特殊项目OR营业总成本特殊项目 | number(19,4) | ✓ | 0.62% |  |
| 27 | `AdjustmentItemsTOC` | ##营业总成本调整项目 | number(19,4) | ✓ | 0.0% |  |
| 28 | `OtherRevenue` | 其他收益 | number(19,4) | ✓ | 50.18% |  |
| 29 | `InvestIncome` | 投资收益 | number(19,4) | ✓ | 8.76% |  |
| 30 | `InvestIncomeAssociates` | 其中:对联营企业和合营企业的投资收益 | number(19,4) | ✓ | 0.0% |  |
| 31 | `AmortisedcostIncome` | 其中:以摊余成本计量的金融资产终止确认收益 | number(19,4) | ✓ | 0.35% |  |
| 32 | `NetOpenHedgeIncome` | 净敞口套期收益 | number(19,4) | ✓ | 0.0% |  |
| 33 | `FairValueChangeIncome` | 公允价值变动净收益 | number(19,4) | ✓ | 6.9% |  |
| 34 | `CreditImpairmentL` | 信用减值损失 | number(19,4) | ✓ | 39.29% |  |
| 35 | `AssetImpairmentLoss` | 资产减值损失 | number(19,4) | ✓ | 8.67% |  |
| 36 | `AssetDealIncome` | 资产处置收益 | number(19,4) | ✓ | 11.59% |  |
| 37 | `OperatingProfit` | 营业利润 | number(19,4) | ✓ | 96.64% |  |
| 38 | `NonoperatingIncome` | 加:营业外收入 | number(19,4) | ✓ | 62.48% |  |
| 39 | `NonoperatingExpense` | 减:营业外支出 | number(19,4) | ✓ | 37.17% |  |
| 40 | `NonCurAssDLoss` | 其中:非流动资产处置净损失 | number(19,4) | ✓ | 0.0% |  |
| 41 | `OtherItemsEffectingTP` | ##加:影响利润总额的其他科目 | number(19,4) | ✓ | 0.0% |  |
| 42 | `AdjustItemsEffectingTP` | ##加:影响利润总额的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 43 | `TotalProfit` | 利润总额 | number(19,4) | ✓ | 96.64% |  |
| 44 | `IncomeTaxCost` | 减:所得税费用 | number(19,4) | ✓ | 87.88% |  |
| 45 | `OtherItemsEffectingNP` | ##加:影响净利润的其他科目 | number(19,4) | ✓ | 0.0% |  |
| 46 | `AdjItemsEffNP` | ##加:影响净利润的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 47 | `NetProfit` | 净利润 | number(19,4) | ✓ | 96.64% |  |
| 48 | `OperSustCateg` | (一)按经营持续性分类 | number(19,4) | ✓ | 0.0% |  |
| 49 | `OperSustNetP` | 持续经营净利润 | number(19,4) | ✓ | 29.82% |  |
| 50 | `DisconOperNetP` | 终止经营净利润 | number(19,4) | ✓ | 0.0% |  |
| 51 | `OwnershipCateg` | (二)按所有权归属分类 | number(19,4) | ✓ | 0.0% |  |
| 52 | `NPParentCompanyOwners` | 归属于母公司所有者的净利润 | number(19,4) | ✓ | 6.99% |  |
| 53 | `MinorityProfit` | 少数股东损益 | number(19,4) | ✓ | 0.0% |  |
| 54 | `OtherItemsEffectingNPP` | ##加:影响母公司净利润的特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 55 | `AdjItemsEffNPP` | ##加:影响母公司净利润的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 56 | `OtherCompositeIncome` | 其他综合收益的税后净额 | number(19,4) | ✓ | 4.25% |  |
| 57 | `OCIParentCompanyOwners` | (一)归属于母公司所有者的其他综合收益的税后净额 | number(19,4) | ✓ | 0.0% |  |
| 58 | `OCINotInIS` | 1.不能重分类进损益的其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 59 | `OCIReMearsure` | (1)重新计量设定受益计划变动额 | number(19,4) | ✓ | 0.0% |  |
| 60 | `OCIEquityNotInIS` | (2)权益法下不能转损益的其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 61 | `OthEquFVChange` | (3)其他权益工具投资公允价值变动 | number(19,4) | ✓ | 0.0% |  |
| 62 | `CorporateCRChange` | (4)企业自身信用风险公允价值变动 | number(19,4) | ✓ | 0.0% |  |
| 63 | `OCIInIncomeStatement` | 2.将重分类进损益的其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 64 | `OCIEquityInIS` | (1)权益法下可转损益的其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 65 | `OthDebtInvesChange` | (2)其他债权投资公允价值变动 | number(19,4) | ✓ | 0.0% |  |
| 66 | `FinAssetROtherCI` | (3)金融资产重分类计入其他综合收益的金额 | number(19,4) | ✓ | 0.0% |  |
| 67 | `OtherDebtInvestCIP` | (4)其他债权投资信用减值准备 | number(19,4) | ✓ | 0.0% |  |
| 68 | `OCICFLoss` | (5)现金流量套期储备 | number(19,4) | ✓ | 0.0% |  |
| 69 | `OCIForeignCurrencyFSA` | (6)外币财务报表折算差额 | number(19,4) | ✓ | 0.0% |  |
| 70 | `OCIMinorityOwners` | (二)归属于少数股东的其他综合收益的税后净额 | number(19,4) | ✓ | 0.0% |  |
| 71 | `AdjItemsEffCI` | ##加:影响综合收益总额的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 72 | `TotalCompositeIncome` | 综合收益总额 | number(19,4) | ✓ | 75.22% |  |
| 73 | `CIParentCompanyOwners` | (一)归属于母公司所有者的综合收益总额 | number(19,4) | ✓ | 6.11% |  |
| 74 | `CIMinorityOwners` | (二)归属于少数股东的综合收益总额 | number(19,4) | ✓ | 0.0% |  |
| 75 | `AdjustEffectPCI` | ##加:影响母公司综合收益总额的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 76 | `BasicEPS` | 基本每股收益 | number(19,4) | ✓ | 0.0% |  |
| 77 | `DilutedEPS` | 稀释每股收益 | number(19,4) | ✓ | 0.0% |  |
| 78 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 79 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 80 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)：与“指标码表（IndicatorMain）”中的“聚源指标代码（GilCode）”关联，得到信息来源。

### CompanyCode (公司代码)

公司代码(CompanyCode)：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到公司的交易代码、简称等。

### InnerCode (基金内部编码)

基金内部编码(InnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB=1188 and DM in (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。

### IfMerged (是否合并)

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM IN (1,2,7)，得到是否合并的具体描述：1-合并，2-母公司，7-专项合并。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455 and DM IN (1)，得到会计准则的具体描述：1-新会计准则(2007)。

### IfDisclosure (是否披露值)

是否披露值(IfDisclosure):1-是；2-否。

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM IN (1,2)，得到完整标志的具体描述：1-完整报表，2-简表。

## SQL示例

```sql
-- 查询 REITs项目公司利润分配表 数据
SELECT *
FROM mf_reitsincomest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
