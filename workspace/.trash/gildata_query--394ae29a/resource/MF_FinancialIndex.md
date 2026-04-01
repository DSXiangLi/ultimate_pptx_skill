# MF_FinancialIndex

**中文名**: 公募基金财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FinancialIndex` |
| MySQL表名 | `mf_financialindex` |
| 中文名 | 公募基金财务指标 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 45 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金各类聚源自定义财务指标，包括基金单位指标、资产状况指标、收益分析指标、费用分析指标、盈利能力指标。
2.历史数据：1998年12月起-至今。
3.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `UnitNetProfit` | 单位基金净收益(元) | number(19,4) | ✓ | 93.01% |  |
| 5 | `UnitDistributableProfit` | 单位基金可分配净收益(元) | number(19,4) | ✓ | 93.03% |  |
| 6 | `UnitRetainedProfit` | 单位基金未分配收益(元) | number(19,4) | ✓ | 92.9% |  |
| 7 | `UnitNV` | 单位基金净值(元) | number(19,4) | ✓ | 99.88% |  |
| 8 | `UnitAccumulatedNV` | 单位基金累计净值(元) | number(19,4) | ✓ | 99.86% |  |
| 9 | `DiscountRatio` | 基金升贴水率 | number(18,4) | ✓ | 3.04% | 升贴水率=1-收盘价/单位净值 |
| 10 | `TotalAsset` | 基金资产总额(元) | number(19,4) | ✓ | 63.66% |  |
| 11 | `TotalLiability` | 基金负债总额(元) | number(19,4) | ✓ | 63.66% |  |
| 12 | `TotalNetAsset` | 基金净资产值(元) | number(19,4) | ✓ | 63.66% |  |
| 13 | `TotalShares` | 基金单位总额(元) | number(18,4) | ✓ | 64.2% |  |
| 14 | `TotalIncome` | 基金总收入(元) | number(19,4) | ✓ | 63.66% |  |
| 15 | `SecuSpreadIncome` | 证券买卖价差收入(元) | number(19,4) | ✓ | 62.52% | 证券买卖价差收入＝股票差价收入＋债券差价收入 |
| 16 | `InvestIncome` | 投资收益(元) | number(19,4) | ✓ | 62.75% | 投资收益＝债券利息收入＋股利收入 |
| 17 | `UnrealizedProfit` | 基金未实现估值增值(元) | number(19,4) | ✓ | 59.55% |  |
| 18 | `NetProfit` | 本期已实现净收益(元) | number(19,4) | ✓ | 63.66% |  |
| 19 | `Performance` | 基金经营业绩(元) | number(19,4) | ✓ | 63.66% |  |
| 20 | `RetainedProfit` | 期末未分配收益(元) | number(19,4) | ✓ | 60.52% |  |
| 21 | `RealizedProfitRatio` | 已实现收入比率 | number(18,4) | ✓ | 37.02% | 已实现收入比率＝1－未实现估值增值/（经营业绩＋费用） |
| 22 | `MainIncomeRatio` | 主营收入比率 | number(18,4) | ✓ | 45.47% | 主营收入比率＝（证券买卖价差收入＋投资收益＋未实现利得）/（经营业绩＋费用） |
| 23 | `StockInvestIncomeRatio` | 股票收入比率(%) | number(18,6) | ✓ | 22.16% | 股票收入比率＝（股票差价收入+股息收入＋股票投资估值增值）/（经营业绩＋费用）×100%，其中股票投资估值增值＝（本期股... |
| 24 | `BondInvestIncomeRatio` | 债券收入比率(%) | number(18,6) | ✓ | 23.12% | 债券收入比率＝（债券差价收入+债券利息收入+债券投资估值增值）/（经营业绩＋费用）×100%,其中债券投资估值增值＝（本... |
| 25 | `UnrealizedProfitRatio` | 未实现估值增值收入比率(%) | number(18,6) | ✓ | 28.27% | 未实现估值增值收入比率＝（未实现估值增值/基金本期净收益）×100% |
| 26 | `ManagementFeeProportion` | 管理费占总费用的比例 | number(18,6) | ✓ | 63.57% |  |
| 27 | `TrustFeeProportion` | 托管费占总费用的比例 | number(18,6) | ✓ | 63.65% |  |
| 28 | `TradeExpenseProportion` | 交易费占总费用的比例 | number(18,6) | ✓ | 30.66% |  |
| 29 | `OtherExpenseProportion` | 其他费用占总费用的比例 | number(18,6) | ✓ | 63.59% |  |
| 30 | `ManagementFeeProfitRatio` | 管理费用收益比 | number(18,6) | ✓ | 63.57% | 管理费用收益比=总收益/管理费用＝（经营业绩＋费用）/管理费用 |
| 31 | `TrustFeeProfitRatio` | 托管费用收益比 | number(18,6) | ✓ | 63.65% | 托管费用收益比=总收益/托管费用=（经营业绩＋费用）/托管费用 |
| 32 | `TradeExpenseProfitRatio` | 交易费用收益比 | number(18,6) | ✓ | 30.65% | 交易费用收益比=总收益/交易费用=（经营业绩＋费用）/交易费用 |
| 33 | `OtherExpenseProfitRatio` | 其他费用收益比 | number(18,6) | ✓ | 63.59% | 其他费用收益比=总收益/其他费用=（经营业绩＋费用）/其他费用 |
| 34 | `TotalExpenseProfitRatio` | 总费用收益比 | number(18,6) | ✓ | 63.66% | 总费用收益比=总收益/费用=（经营业绩＋费用）/费用 |
| 35 | `NVGrowthRate` | 本期净值增长率 | number(18,6) | ✓ | 93.06% |  |
| 36 | `AccumulatedNVGrowthRate` | 累计净值增长率 | number(18,6) | ✓ | 93.08% |  |
| 37 | `NVYield` | 净值收益率 | number(18,6) | ✓ | 92.98% |  |
| 38 | `TotalAssetGrowthRate` | 总资产增长率(%) | number(18,6) | ✓ | 54.77% | 总资产增长率＝（本期总资产/上期总资产－1）×100% |
| 39 | `PerformanceGrowthRate` | 经营业绩同比增长率(%) | number(18,6) | ✓ | 25.11% |  |
| 40 | `DividendRatio` | 分红率(%) | number(18,6) | ✓ | 8.82% | 分红率＝（收益分配金额/本期可分配收益）×100% |
| 41 | `StockTradeYield` | 股票交易收益率(%) | number(18,6) | ✓ | 32.23% | 股票交易收益率＝{股票差价收入/[(期初净值＋期末净值)/2]×0.8}×100% |
| 42 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 43 | `JSID` | JSID | number(19) | ✗ |  |  |
| 44 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 45 | `InsertTime` | 插入时间 | date | ✓ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### DiscountRatio (基金升贴水率)

升贴水率=1-收盘价/单位净值

### SecuSpreadIncome (证券买卖价差收入(元))

证券买卖价差收入＝股票差价收入＋债券差价收入

### InvestIncome (投资收益(元))

投资收益＝债券利息收入＋股利收入

### RealizedProfitRatio (已实现收入比率)

已实现收入比率＝1－未实现估值增值/（经营业绩＋费用）

### MainIncomeRatio (主营收入比率)

主营收入比率＝（证券买卖价差收入＋投资收益＋未实现利得）/（经营业绩＋费用）

### StockInvestIncomeRatio (股票收入比率(%))

股票收入比率＝（股票差价收入+股息收入＋股票投资估值增值）/（经营业绩＋费用）×100%，其中股票投资估值增值＝（本期股票投资市值－本期股票投资成本）－（上期股票投资市值－上期股票投资成本）

### BondInvestIncomeRatio (债券收入比率(%))

债券收入比率＝（债券差价收入+债券利息收入+债券投资估值增值）/（经营业绩＋费用）×100%,其中债券投资估值增值＝（本期债券投资市值－本期债券投资成本）－（上期债券投资市值－上期债券投资成本）

### UnrealizedProfitRatio (未实现估值增值收入比率(%))

未实现估值增值收入比率＝（未实现估值增值/基金本期净收益）×100%

### ManagementFeeProfitRatio (管理费用收益比)

管理费用收益比=总收益/管理费用＝（经营业绩＋费用）/管理费用

## SQL示例

```sql
-- 查询 公募基金财务指标 数据
SELECT *
FROM mf_financialindex
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
