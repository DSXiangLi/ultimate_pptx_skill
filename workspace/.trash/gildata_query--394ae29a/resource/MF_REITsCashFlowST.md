# MF_REITsCashFlowST

**中文名**: REITs项目公司现金流量表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsCashFlowST` |
| MySQL表名 | `mf_reitscashflowst` |
| 中文名 | REITs项目公司现金流量表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 半年度更新 |
| 字段数量 | 70 |
| 版本 | 1 |

## 表描述

1.内容说明：收录项目公司年报、中报、季报、招募说明书中披露的现金流量表数据。
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
| 7 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB=1188 and DM I... |
| 8 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM in ... |
| 9 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455... |
| 10 | `IfDisclosure` | 是否披露值 | number(10) | ✗ | 100.0% | 是否披露值(IfDisclosure):1-是；2-否。 |
| 11 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM I... |
| 12 | `GdSaSeReCash` | 销售商品、提供劳务收到的现金 | number(19,4) | ✓ | 94.46% |  |
| 13 | `TaxLevyRefund` | 收到的税费返还 | number(19,4) | ✓ | 26.75% |  |
| 14 | `OthCashInRelOpe` | 收到其他与经营活动有关的现金 | number(19,4) | ✓ | 96.68% |  |
| 15 | `SpecialItemsOCIF` | ##经营活动现金流入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 16 | `AdjustmentItemsOCIF` | ##经营活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 17 | `SuOpCashInflow` | 经营活动现金流入小计 | number(19,4) | ✓ | 96.86% |  |
| 18 | `GoodsServicesCashPaid` | 购买商品、接受劳务支付的现金 | number(19,4) | ✓ | 94.83% |  |
| 19 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金 | number(19,4) | ✓ | 63.1% |  |
| 20 | `AllTaxesPaid` | 支付的各项税费 | number(19,4) | ✓ | 96.68% |  |
| 21 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金 | number(19,4) | ✓ | 97.23% |  |
| 22 | `SpecialItemsOCOF` | ##经营活动现金流出特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 23 | `AdjustmentItemsOCOF` | ##经营活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 24 | `SubOpCOutflow` | 经营活动现金流出小计 | number(19,4) | ✓ | 97.23% |  |
| 25 | `AdjustmentItemsNOCF` | ##经营活动现金流量净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 26 | `NetOperateCashFlow` | 经营活动产生的现金流量净额 | number(19,4) | ✓ | 97.23% |  |
| 27 | `InvestWithdrawalCash` | 收回投资收到的现金 | number(19,4) | ✓ | 11.81% |  |
| 28 | `Investproceeds` | 取得投资收益收到的现金 | number(19,4) | ✓ | 11.99% |  |
| 29 | `FixInOtADisCash` | 处置固定资产、无形资产和其他长期资产收回的现金净额 | number(19,4) | ✓ | 30.81% |  |
| 30 | `NetCashDealSubCompany` | 处置子公司及其他营业单位收到的现金净额 | number(19,4) | ✓ | 0.74% |  |
| 31 | `OtherCashFromInvestAct` | 收到其他与投资活动有关的现金 | number(19,4) | ✓ | 35.61% |  |
| 32 | `SpecialItemsICIF` | ##投资活动现金流入特殊项目 | number(19,4) | ✓ | 2.03% |  |
| 33 | `AdjustmentItemsICIF` | ##投资活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 34 | `SubInvCaInflow` | 投资活动现金流入小计 | number(19,4) | ✓ | 62.55% |  |
| 35 | `FixInOAsAcCash` | 购建固定资产、无形资产和其他长期资产支付的现金 | number(19,4) | ✓ | 87.45% |  |
| 36 | `InvestCashPaid` | 投资支付的现金 | number(19,4) | ✓ | 11.99% |  |
| 37 | `NetCashFromSubCompany` | 取得子公司及其他营业单位支付的现金净额 | number(19,4) | ✓ | 0.0% |  |
| 38 | `OtherCashToInvestAct` | 支付其他与投资活动有关的现金 | number(19,4) | ✓ | 24.91% |  |
| 39 | `SpecialItemsICOF` | ##投资活动现金流出特殊项目 | number(19,4) | ✓ | 1.85% |  |
| 40 | `AdjustmentItemsICOF` | ##投资活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 41 | `SubInvCashOflow` | 投资活动现金流出小计 | number(19,4) | ✓ | 90.77% |  |
| 42 | `AdjustmentItemsNICF` | ##投资活动现金流量净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 43 | `NetInvestCashFlow` | 投资活动产生的现金流量净额 | number(19,4) | ✓ | 92.44% |  |
| 44 | `CashFromInvest` | 吸收投资收到的现金 | number(19,4) | ✓ | 10.33% |  |
| 45 | `CashFromMinoSInvestSub` | 其中:子公司吸收少数股东投资收到的现金 | number(19,4) | ✓ | 0.0% |  |
| 46 | `CashFromBorrowing` | 取得借款收到的现金 | number(19,4) | ✓ | 37.82% |  |
| 47 | `OtherFinanceActCash` | 收到其他与筹资活动有关的现金 | number(19,4) | ✓ | 35.24% |  |
| 48 | `SpecialItemsFCIF` | ##筹资活动现金流入特殊项目 | number(19,4) | ✓ | 2.58% |  |
| 49 | `AdjustmentItemsFCIF` | ##筹资活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 50 | `SubFinCashInfl` | 筹资活动现金流入小计 | number(19,4) | ✓ | 59.59% |  |
| 51 | `BorrowingRepayment` | 偿还债务支付的现金 | number(19,4) | ✓ | 68.82% |  |
| 52 | `DivIntPayment` | 分配股利、利润或偿付利息支付的现金 | number(19,4) | ✓ | 84.5% |  |
| 53 | `ProceedsFromSubToMinoS` | 其中:子公司支付给少数股东的股利、利润 | number(19,4) | ✓ | 0.0% |  |
| 54 | `OtherFinanceActPayment` | 支付其他与筹资活动有关的现金 | number(19,4) | ✓ | 47.23% |  |
| 55 | `SpecialItemsFCOF` | ##筹资活动现金流出特殊项目 | number(19,4) | ✓ | 1.11% |  |
| 56 | `AdjustmentItemsFCOF` | ##筹资活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 57 | `SubFinCOflow` | 筹资活动现金流出小计 | number(19,4) | ✓ | 92.25% |  |
| 58 | `AdjustmentItemsNFCF` | ##筹资活动流量现金净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 59 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额 | number(19,4) | ✓ | 93.17% |  |
| 60 | `ExchanRateChangeEffect` | 汇率变动对现金及现金等价物的影响 | number(19,4) | ✓ | 7.75% |  |
| 61 | `OtherItemsEffectingCE` | ##影响现金及现金等价物的其他科目 | number(19,4) | ✓ | 0.0% |  |
| 62 | `AdjustmentItemsCE` | ##影响现金及现金等价物的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 63 | `CashEquivalentIncrease` | 现金及现金等价物净增加额 | number(19,4) | ✓ | 95.76% |  |
| 64 | `BeginPeriodCash` | 加:期初现金及现金等价物余额 | number(19,4) | ✓ | 96.13% |  |
| 65 | `OtherItemsEffectingCEI` | ##现金及现金等价物净增加额的特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 66 | `AdjustmentItemsCEI` | ##现金及现金等价物净增加额的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 67 | `EndPerCEqu` | 期末现金及现金等价物余额 | number(19,4) | ✓ | 98.15% |  |
| 68 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 69 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 70 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)：与“指标码表（IndicatorMain）”中的“聚源指标代码（GilCode）”关联，得到信息来源。

### CompanyCode (公司代码)

公司代码(CompanyCode)：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到公司的交易代码、简称等。

### InnerCode (基金内部编码)

基金内部编码(InnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB=1188 and DM IN (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。

### IfMerged (是否合并)

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM in (1,2,7)，得到是否合并的具体描述：1-合并，2-母公司，7-专项合并。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455 and DM in (1)，得到会计准则的具体描述：1-新会计准则(2007)。

### IfDisclosure (是否披露值)

是否披露值(IfDisclosure):1-是；2-否。

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM IN (1,2)，得到完整标志的具体描述：1-完整报表，2-简表。

## SQL示例

```sql
-- 查询 REITs项目公司现金流量表 数据
SELECT *
FROM mf_reitscashflowst
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
