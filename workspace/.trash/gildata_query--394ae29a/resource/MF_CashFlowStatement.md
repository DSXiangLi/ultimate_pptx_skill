# MF_CashFlowStatement

**中文名**: 公募基金现金流量表_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CashFlowStatement` |
| MySQL表名 | `mf_cashflowstatement` |
| 中文名 | 公募基金现金流量表_新会计准则 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 季更新 |
| 字段数量 | 117 |
| 版本 | 1 |

## 表描述

1.包含依据2007年新会计准则披露的基金现金流量表数据；并跟据新旧会计准则的科目对应关系，收录了主要科目的历史对应数据。
2.收录同一基金在报告期末的两种财务报告，即未调整报表和调整后报表。若某个报告期的数据有多次调整，则该表展示最新调整数据；若某报告期暂未披露调整后数据，则已调整类别下的数据与调整前的数据一致。
3.带“##”的特殊项目为单个基金披露的非标准化的科目，对应的“特殊字段说明”字段将对其作出说明；带“##”的调整项目是为了让报表的各个小项借贷平衡而设置的，便于客户对报表的遗漏和差错进行判断。
4.该表中各财务科目下数据对应的货币单位均为人民币元。
5.历史数据：2021-06-30-至今。
6.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND ... |
| 6 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 7 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 8 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 9 | `Mark` | 调整标志 | number(10) | ✗ | 100.0% | 调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1... |
| 10 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 11 | `GdSaSeReCash` | 销售商品、提供劳务收到的现金 | number(19,4) | ✓ | 99.81% |  |
| 12 | `NetCashRecInDSI` | 处置证券投资收到的现金净额 | number(19,4) | ✓ | 7.29% |  |
| 13 | `NetDecBSbackAssets` | 买入返售金融资产净减少额 | number(19,4) | ✓ | 0.77% |  |
| 14 | `NetIncSBbackSecuPros` | 卖出回购金融资产款净增加额 | number(19,4) | ✓ | 0.0% |  |
| 15 | `CashFromInterest` | 取得利息收入收到的现金 | number(19,4) | ✓ | 95.78% |  |
| 16 | `TaxLevyRefund` | 收到的税费返还 | number(19,4) | ✓ | 19.19% |  |
| 17 | `OthCashInRelOpe` | 收到其他与经营活动有关的现金 | number(19,4) | ✓ | 95.97% |  |
| 18 | `SpecialItemsOCIF` | ##经营活动现金流入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 19 | `AdjustmentItemsOCIF` | ##经营活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 20 | `SuOpCashInflow` | 经营活动现金流入小计 | number(19,4) | ✓ | 100.0% |  |
| 21 | `GoodsServicesCashPaid` | 购买商品、接受劳务支付的现金 | number(19,4) | ✓ | 90.79% |  |
| 22 | `NetCashFromSecuInv` | 取得证券投资支付的现金净额 | number(19,4) | ✓ | 5.76% |  |
| 23 | `NetIncBSbackAssets` | 买入返售金融资产净增加额 | number(19,4) | ✓ | 1.54% |  |
| 24 | `NetDecSBbackSecuPros` | 卖出回购金融资产款净减少额 | number(19,4) | ✓ | 0.0% |  |
| 25 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金 | number(19,4) | ✓ | 26.87% |  |
| 26 | `AllTaxesPaid` | 支付的各项税费 | number(19,4) | ✓ | 98.85% |  |
| 27 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金 | number(19,4) | ✓ | 99.81% |  |
| 28 | `SpecialItemsOCOF` | ##经营活动现金流出特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 29 | `AdjustmentItemsOCOF` | ##经营活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 30 | `SubOpCOutflow` | 经营活动现金流出小计 | number(19,4) | ✓ | 100.0% |  |
| 31 | `AdjustmentItemsNOCF` | ##经营活动现金流量净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 32 | `NetOperateCashFlow` | 经营活动产生的现金流量净额 | number(19,4) | ✓ | 100.0% |  |
| 33 | `FixInOtADisCash` | 处置固定资产、无形资产和其他长期资产收到的现金净额 | number(19,4) | ✓ | 11.13% |  |
| 34 | `NetCashDealSubCompany` | 处置子公司及其他营业单位收到的现金净额 | number(19,4) | ✓ | 0.0% |  |
| 35 | `OtherCashFromInvestAct` | 收到其他与投资活动有关的现金 | number(19,4) | ✓ | 19.0% |  |
| 36 | `SpecialItemsICIF` | ##投资活动现金流入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 37 | `AdjustmentItemsICIF` | ##投资活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 38 | `SubInvCaInflow` | 投资活动现金流入小计 | number(19,4) | ✓ | 27.64% |  |
| 39 | `FixInOAsAcCash` | 购建固定资产、无形资产和其他长期资产支付的现金 | number(19,4) | ✓ | 62.76% |  |
| 40 | `NetCashFromSubCompany` | 取得子公司及其他营业单位支付的现金净额 | number(19,4) | ✓ | 34.55% |  |
| 41 | `OtherCashToInvestAct` | 支付其他与投资活动有关的现金 | number(19,4) | ✓ | 23.03% |  |
| 42 | `SpecialItemsICOF` | ##投资活动现金流出特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 43 | `AdjustmentItemsICOF` | ##投资活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 44 | `SubInvCashOflow` | 投资活动现金流出小计 | number(19,4) | ✓ | 80.81% |  |
| 45 | `AdjustmentItemsNICF` | ##投资活动现金流量净额调整项目 | number(19,4) | ✓ | 0.19% |  |
| 46 | `NetInvestCashFlow` | 投资活动产生的现金流量净额 | number(19,4) | ✓ | 83.3% |  |
| 47 | `CashFromSubscription` | 认购/申购收到的现金 | number(19,4) | ✓ | 16.51% |  |
| 48 | `CashFromBorrowing` | 取得借款收到的现金 | number(19,4) | ✓ | 10.36% |  |
| 49 | `OtherFinanceActCash` | 收到其他与筹资活动有关的现金 | number(19,4) | ✓ | 2.88% |  |
| 50 | `SpecialItemsFCIF` | ##筹资活动现金流入特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 51 | `AdjustmentItemsFCIF` | ##筹资活动现金流入调整项目 | number(19,4) | ✓ | 0.0% |  |
| 52 | `SubFinCashInfl` | 筹资活动现金流入小计 | number(19,4) | ✓ | 27.06% |  |
| 53 | `RedemptionCashPaid` | 赎回支付的现金 | number(19,4) | ✓ | 0.0% |  |
| 54 | `BorrowingRepayment` | 偿还借款支付的现金 | number(19,4) | ✓ | 40.12% |  |
| 55 | `InterestPayment` | 偿付利息支付的现金 | number(19,4) | ✓ | 38.39% |  |
| 56 | `DistributionCashPaid` | 分配支付的现金 | number(19,4) | ✓ | 80.61% |  |
| 57 | `OtherFinanceActPayment` | 支付其他与筹资活动有关的现金 | number(19,4) | ✓ | 19.58% |  |
| 58 | `SpecialItemsFCOF` | ##筹资活动现金流出特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 59 | `AdjustmentItemsFCOF` | ##筹资活动现金流出调整项目 | number(19,4) | ✓ | 0.0% |  |
| 60 | `SubFinCOflow` | 筹资活动现金流出小计 | number(19,4) | ✓ | 93.28% |  |
| 61 | `AdjustmentItemsNFCF` | ##筹资活动流量现金净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 62 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额 | number(19,4) | ✓ | 96.93% |  |
| 63 | `ExchanRateChangeEffect` | 汇率变动对现金及现金等价物的影响 | number(19,4) | ✓ | 1.34% |  |
| 64 | `OtherItemsEffectingCE` | ##影响现金及现金等价物的特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 65 | `AdjustmentItemsCE` | ##影响现金及现金等价物的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 66 | `CashEquivalentIncrease` | 现金及现金等价物净增加额 | number(19,4) | ✓ | 100.0% |  |
| 67 | `BeginPeriodCash` | 加:期初现金及现金等价物余额 | number(19,4) | ✓ | 87.33% |  |
| 68 | `OtherItemsEffectingCEI` | ##现金及现金等价物净增加额的特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 69 | `AdjustmentItemsCEI` | ##现金及现金等价物净增加额的调整项目 | number(19,4) | ✓ | 0.0% |  |
| 70 | `EndPerCEqu` | 期末现金及现金等价物余额 | number(19,4) | ✓ | 100.0% |  |
| 71 | `NetProfit` | 净利润 | number(19,4) | ✓ | 84.64% |  |
| 72 | `CreditImpairmentL` | 加:信用减值损失 | number(19,4) | ✓ | 37.81% |  |
| 73 | `AssetImpairmentLoss` | 资产减值损失 | number(19,4) | ✓ | 11.52% |  |
| 74 | `FixedAssetDepreciation` | 固定资产折旧 | number(19,4) | ✓ | 62.57% |  |
| 75 | `InvestPropertyDA` | 投资性房地产折旧 | number(19,4) | ✓ | 47.98% |  |
| 76 | `UsufructAssetsDA` | 使用权资产折旧 | number(19,4) | ✓ | 8.83% |  |
| 77 | `IntAAmort` | 无形资产摊销 | number(19,4) | ✓ | 42.03% |  |
| 78 | `DeferredExpenseAmort` | 长期待摊费用摊销 | number(19,4) | ✓ | 23.99% |  |
| 79 | `FixInOthADLoss` | 处置固定资产、无形资产和其他长期资产的损失(收益以"-"号填列) | number(19,4) | ✓ | 6.91% |  |
| 80 | `FixedAssetScrapLoss` | 固定资产报废损失(收益以"-"号填列) | number(19,4) | ✓ | 5.18% |  |
| 81 | `LFromFValueChg` | 公允价值变动损失(收益以"-"号填列) | number(19,4) | ✓ | 1.73% |  |
| 82 | `FinancialExpense` | 财务费用(收益以"-"号填列) | number(19,4) | ✓ | 24.38% |  |
| 83 | `InvestLoss` | 投资损失(收益以"-"号填列) | number(19,4) | ✓ | 20.54% |  |
| 84 | `DefProceedsAmo` | 递延收益摊销 | number(19,4) | ✓ | 0.96% |  |
| 85 | `IncEstLiability` | 预计负债的增加(减:减少) | number(19,4) | ✓ | 2.88% |  |
| 86 | `DefTaxAssetDec` | 递延所得税资产减少(增加以"-"号填列) | number(19,4) | ✓ | 23.8% |  |
| 87 | `DefTaxLiaInc` | 递延所得税负债增加(减少以"-"号填列) | number(19,4) | ✓ | 40.88% |  |
| 88 | `InventoryDecrease` | 存货的减少(增加以"-"号填列) | number(19,4) | ✓ | 15.36% |  |
| 89 | `OpeRecDec` | 经营性应收项目的减少(增加以"-"号填列) | number(19,4) | ✓ | 84.64% |  |
| 90 | `OperatePayableIncrease` | 经营性应付项目的增加(减少以"-"号填列) | number(19,4) | ✓ | 84.64% |  |
| 91 | `IntAScrapGain` | 无形资产报废收益(收益以"-"号填列) | number(19,4) | ✓ | 0.77% |  |
| 92 | `NetInterestIncome` | 利息净收入(收益以"-"号填列) | number(19,4) | ✓ | 0.38% |  |
| 93 | `InterestExpense` | 利息支出 | number(19,4) | ✓ | 14.01% |  |
| 94 | `RelToFixedAssetSub` | 收到的固定资产相关的政府补助 | number(19,4) | ✓ | 0.38% |  |
| 95 | `DecreaseTradeAssets` | 交易性金融资产的减少(增加以"-"号填列) | number(19,4) | ✓ | 1.34% |  |
| 96 | `DecreaseBSbackAssets` | 买入返售金融资产的减少(增加以"-"号填列) | number(19,4) | ✓ | 0.19% |  |
| 97 | `Others` | 其他 | number(19,4) | ✓ | 7.1% |  |
| 98 | `SpecialItemsNOCF1` | ##(附注)经营活动现金流量净额特殊项目 | number(19,4) | ✓ | 1.15% |  |
| 99 | `AdjustmentItemsNOCF1` | ##(附注)经营活动现金流量净额调整项目 | number(19,4) | ✓ | 0.0% |  |
| 100 | `NetOpeCFNotes` | (附注)经营活动产生的现金流量净额 | number(19,4) | ✓ | 84.64% |  |
| 101 | `ContrastAdjutmentNOCF` | ##加:经营流量净额前后对比调整项目 | number(19,4) | ✓ | 0.0% |  |
| 102 | `LongtermAssetsFromDebt` | 以债务构建的长期资产 | number(19,4) | ✓ | 0.19% |  |
| 103 | `DebtToCaptical` | 债务转为资本 | number(19,4) | ✓ | 0.38% |  |
| 104 | `CBsExpiringWithin1Y` | 一年内到期的可转换公司债券 | number(19,4) | ✓ | 0.0% |  |
| 105 | `FixedAFinLeases` | 融资租入固定资产 | number(19,4) | ✓ | 0.0% |  |
| 106 | `CashAtEndOfYear` | 现金的期末余额 | number(19,4) | ✓ | 84.64% |  |
| 107 | `CashAtBeginningOfYear` | 减:现金的期初余额 | number(19,4) | ✓ | 73.9% |  |
| 108 | `CEquAtEOfYear` | 加:现金等价物的期末余额 | number(19,4) | ✓ | 1.34% |  |
| 109 | `CEquAtBeginning` | 减:现金等价物的期初余额 | number(19,4) | ✓ | 0.38% |  |
| 110 | `SpecialItemsC` | ##(附注)现金特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 111 | `AdjustmentItemsC` | ##(附注)现金调整项目 | number(19,4) | ✓ | 0.0% |  |
| 112 | `NetIncrInCEqu` | (附注)现金及现金等价物净增加额 | number(19,4) | ✓ | 84.64% |  |
| 113 | `ContrastAdjutmentNC` | ##加:现金净额前后对比调整项目 | number(19,4) | ✓ | 0.0% |  |
| 114 | `SpecialFieldRemark` | 特殊字段说明 | varchar2(1000) | ✓ | 0.77% |  |
| 115 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 116 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 117 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (4,5,6)，得到公告类别的具体描述：4-上市公告书，5-年度报告，6-中期报告。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到基金公司的交易代码、简称等。

### Mark (调整标志)

调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2)，得到调整标志的具体描述：1-是，2-否。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

## SQL示例

```sql
-- 查询 公募基金现金流量表_新会计准则 数据
SELECT *
FROM mf_cashflowstatement
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
