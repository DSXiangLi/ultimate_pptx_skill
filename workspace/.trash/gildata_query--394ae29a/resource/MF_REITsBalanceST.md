# MF_REITsBalanceST

**中文名**: REITs项目公司资产负债表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsBalanceST` |
| MySQL表名 | `mf_reitsbalancest` |
| 中文名 | REITs项目公司资产负债表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 半年度更新 |
| 字段数量 | 109 |
| 版本 | 1 |

## 表描述

1.内容说明：收录项目公司年报、中报、季报、招募说明书中披露的资产负债表数据。
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
| 8 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM IN ... |
| 9 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455... |
| 10 | `IfDisclosure` | 是否披露值 | number(10) | ✗ | 100.0% | 是否披露值(IfDisclosure):1-是；2-否。 |
| 11 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM I... |
| 12 | `CashEquivalents` | 货币资金 | number(19,4) | ✓ | 67.98% |  |
| 13 | `TradingAssets` | 交易性金融资产 | number(19,4) | ✓ | 0.34% |  |
| 14 | `DerivativeAssets` | 衍生金融资产 | number(19,4) | ✓ | 0.0% |  |
| 15 | `BillReceivable` | 应收票据 | number(19,4) | ✓ | 2.74% |  |
| 16 | `AccountReceivable` | 应收账款 | number(19,4) | ✓ | 86.9% |  |
| 17 | `ReceivablesFin` | 应收款项融资 | number(19,4) | ✓ | 0.34% |  |
| 18 | `AdvancePayment` | 预付款项 | number(19,4) | ✓ | 55.65% |  |
| 19 | `OtherReceivables` | 其他应收款 | number(19,4) | ✓ | 75.17% |  |
| 20 | `Inventories` | 存货 | number(19,4) | ✓ | 23.2% |  |
| 21 | `ContractualAssets` | 合同资产 | number(19,4) | ✓ | 0.0% |  |
| 22 | `HoldAndFSAssets` | 持有待售资产 | number(19,4) | ✓ | 0.0% |  |
| 23 | `NonCurrentAssetIn1Year` | 一年内到期的非流动资产 | number(19,4) | ✓ | 4.54% |  |
| 24 | `OtherCurrentAssets` | 其他流动资产 | number(19,4) | ✓ | 40.15% |  |
| 25 | `CAExceptionalItems` | ##流动资产特殊项目 | number(19,4) | ✓ | 2.4% |  |
| 26 | `CAAdjustmentItems` | ##流动资产调整项目 | number(19,4) | ✓ | 0.0% |  |
| 27 | `TotalCurrentAssets` | 流动资产合计 | number(19,4) | ✓ | 94.09% |  |
| 28 | `DebtInvestment` | 债权投资 | number(19,4) | ✓ | 0.51% |  |
| 29 | `OthDebtInvestment` | 其他债权投资 | number(19,4) | ✓ | 0.0% |  |
| 30 | `LtermReceAcc` | 长期应收款 | number(19,4) | ✓ | 3.42% |  |
| 31 | `LongTermEquityInvest` | 长期股权投资 | number(19,4) | ✓ | 0.68% |  |
| 32 | `OthEquityInstrument` | 其他权益工具投资 | number(19,4) | ✓ | 2.05% |  |
| 33 | `OthNonCurFinAssets` | 其他非流动金融资产 | number(19,4) | ✓ | 0.0% |  |
| 34 | `InvestmentProperty` | 投资性房地产 | number(19,4) | ✓ | 58.48% |  |
| 35 | `FixedAssets` | 固定资产 | number(19,4) | ✓ | 69.52% |  |
| 36 | `ConstruInProcess` | 在建工程 | number(19,4) | ✓ | 23.97% |  |
| 37 | `BiologicalAssets` | 生产性生物资产 | number(19,4) | ✓ | 0.26% |  |
| 38 | `OilGasAssets` | 油气资产 | number(19,4) | ✓ | 0.26% |  |
| 39 | `UsufructAssets` | 使用权资产 | number(19,4) | ✓ | 6.76% |  |
| 40 | `IntangibleAssets` | 无形资产 | number(19,4) | ✓ | 46.75% |  |
| 41 | `DevelopmentExpenditure` | 开发支出 | number(19,4) | ✓ | 0.68% |  |
| 42 | `GoodWill` | 商誉 | number(19,4) | ✓ | 0.0% |  |
| 43 | `LongDeferredExpense` | 长期待摊费用 | number(19,4) | ✓ | 31.42% |  |
| 44 | `DeferredTaxAssets` | 递延所得税资产 | number(19,4) | ✓ | 43.41% |  |
| 45 | `OtherNonCurrentAssets` | 其他非流动资产 | number(19,4) | ✓ | 21.32% |  |
| 46 | `NCAExceptionalItems` | ##非流动资产特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 47 | `NCAAdjustmentItems` | ##非流动资产调整项目 | number(19,4) | ✓ | 0.0% |  |
| 48 | `TotalNonCurrentAssets` | 非流动资产合计 | number(19,4) | ✓ | 94.78% |  |
| 49 | `AExceptionalItems` | ##资产特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 50 | `AAdjustmentItems` | ##资产调整项目 | number(19,4) | ✓ | 0.0% |  |
| 51 | `TotalAssets` | 资产总计 | number(19,4) | ✓ | 94.18% |  |
| 52 | `ShortTermLoan` | 短期借款 | number(19,4) | ✓ | 9.08% |  |
| 53 | `TradingLiability` | 交易性金融负债 | number(19,4) | ✓ | 0.0% |  |
| 54 | `DerivativeLiability` | 衍生金融负债 | number(19,4) | ✓ | 0.0% |  |
| 55 | `NotesPayable` | 应付票据 | number(19,4) | ✓ | 1.37% |  |
| 56 | `AccountsPayable` | 应付账款 | number(19,4) | ✓ | 82.19% |  |
| 57 | `AdvanceReceipts` | 预收款项 | number(19,4) | ✓ | 59.59% |  |
| 58 | `ContractLiability` | 合同负债 | number(19,4) | ✓ | 23.29% |  |
| 59 | `SalariesPayable` | 应付职工薪酬 | number(19,4) | ✓ | 37.24% |  |
| 60 | `DeferredProceeds` | 递延收益 | number(19,4) | ✓ | 16.78% |  |
| 61 | `TaxsPayable` | 应交税费 | number(19,4) | ✓ | 77.05% |  |
| 62 | `OtherPayable` | 其他应付款 | number(19,4) | ✓ | 88.78% |  |
| 63 | `HoldAndFSLi` | 持有待售负债 | number(19,4) | ✓ | 0.0% |  |
| 64 | `NonCurLiaInOY` | 一年内到期的非流动负债 | number(19,4) | ✓ | 50.6% |  |
| 65 | `OtherCurrentLiability` | 其他流动负债 | number(19,4) | ✓ | 17.55% |  |
| 66 | `CLExceptionalItems` | ##流动负债特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 67 | `CLAdjustmentItems` | ##流动负债调整项目 | number(19,4) | ✓ | 0.0% |  |
| 68 | `TotalCurrentLiability` | 流动负债合计 | number(19,4) | ✓ | 94.43% |  |
| 69 | `LongTermLoan` | 长期借款 | number(19,4) | ✓ | 49.4% |  |
| 70 | `BondsPayable` | 应付债券 | number(19,4) | ✓ | 0.0% |  |
| 71 | `LPreferStock` | #优先股(应付债券) | number(19,4) | ✓ | 0.0% |  |
| 72 | `LPerpetualDebt` | #永续债(应付债券) | number(19,4) | ✓ | 0.0% |  |
| 73 | `LeaseLiabilities` | 租赁负债 | number(19,4) | ✓ | 5.14% |  |
| 74 | `LongtermAccountPayable` | 长期应付款 | number(19,4) | ✓ | 18.66% |  |
| 75 | `EstimateLiability` | 预计负债 | number(19,4) | ✓ | 6.93% |  |
| 76 | `LongDeferIncome` | 长期递延收益 | number(19,4) | ✓ | 2.83% |  |
| 77 | `DeferredTaxLiability` | 递延所得税负债 | number(19,4) | ✓ | 14.81% |  |
| 78 | `LongSalariesPay` | 长期应付职工薪酬 | number(19,4) | ✓ | 0.68% |  |
| 79 | `OtherNonCurLia` | 其他非流动负债 | number(19,4) | ✓ | 6.25% |  |
| 80 | `NCLExceptionalItems` | ##非流动负债特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 81 | `NCLAdjustmentItems` | ##非流动负债调整项目 | number(19,4) | ✓ | 0.0% |  |
| 82 | `TotalNonCurLia` | 非流动负债合计 | number(19,4) | ✓ | 71.06% |  |
| 83 | `LExceptionalItems` | ##负债特殊项目 | number(19,4) | ✓ | 0.09% |  |
| 84 | `LAdjustmentItems` | ##负债调整项目 | number(19,4) | ✓ | 0.0% |  |
| 85 | `TotalLiability` | 负债合计 | number(19,4) | ✓ | 94.61% |  |
| 86 | `PaidInCapital` | 实收资本(或股本) | number(19,4) | ✓ | 45.55% |  |
| 87 | `OtherEquityinstruments` | 其他权益工具 | number(19,4) | ✓ | 0.0% |  |
| 88 | `EPreferStock` | #优先股(其他权益工具) | number(19,4) | ✓ | 0.0% |  |
| 89 | `EPerpetualDebt` | #永续债(其他权益工具) | number(19,4) | ✓ | 0.0% |  |
| 90 | `CapitalReserveFund` | 资本公积 | number(19,4) | ✓ | 20.21% |  |
| 91 | `TreasuryStock` | 减:库存股 | number(19,4) | ✓ | 0.26% |  |
| 92 | `OtherCompositeIncome` | 其他综合收益 | number(19,4) | ✓ | 0.0% |  |
| 93 | `SpecificReserves` | 专项储备 | number(19,4) | ✓ | 6.34% |  |
| 94 | `OtherReserve` | 其他储备 | number(19,4) | ✓ | 0.0% |  |
| 95 | `SurplusReserveFund` | 盈余公积 | number(19,4) | ✓ | 35.87% |  |
| 96 | `RetainedProfit` | 未分配利润 | number(19,4) | ✓ | 45.8% |  |
| 97 | `OrdRiskResFund` | 一般风险准备 | number(19,4) | ✓ | 0.0% |  |
| 98 | `SEExceptionalItems` | ##归属母公司所有者权益特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 99 | `SEAdjustmentItems` | ##归属母公司所有者权益调整项目 | number(19,4) | ✓ | 0.0% |  |
| 100 | `SEWithoutMI` | 归属母公司所有者权益(或股东权益)合计 | number(19,4) | ✓ | 3.42% |  |
| 101 | `MinorityInterests` | 少数股东权益 | number(19,4) | ✓ | 0.0% |  |
| 102 | `OtherItemsEffectingSE` | ##所有者权益调整项目 | number(19,4) | ✓ | 0.0% |  |
| 103 | `TotalShareholderEquity` | 所有者权益(或股东权益)合计 | number(19,4) | ✓ | 94.09% |  |
| 104 | `LEExceptionalItems` | ##负债和权益特殊项目 | number(19,4) | ✓ | 0.0% |  |
| 105 | `LEAdjustmentItems` | ##负债和权益调整项目 | number(19,4) | ✓ | 0.0% |  |
| 106 | `TotalLiaAndEquity` | 负债和所有者权益(或股东权益)总计 | number(19,4) | ✓ | 88.87% |  |
| 107 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 108 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 109 | `JSID` | JSID | number(19) | ✗ |  |  |

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

是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB=1189 and DM IN (1,2,7)，得到是否合并的具体描述：1-合并，2-母公司，7-专项合并。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB=1455 and DM IN (1)，得到会计准则的具体描述：1-新会计准则(2007)。

### IfDisclosure (是否披露值)

是否披露值(IfDisclosure):1-是；2-否。

### IfComplete (完整标志)

完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB=1444 and DM IN (1,2)，得到完整标志的具体描述：1-完整报表，2-简表。

## SQL示例

```sql
-- 查询 REITs项目公司资产负债表 数据
SELECT *
FROM mf_reitsbalancest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
