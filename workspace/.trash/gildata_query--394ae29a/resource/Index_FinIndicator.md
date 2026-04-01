# Index_FinIndicator

**中文名**: 指数财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_FinIndicator` |
| MySQL表名 | `index_finindicator` |
| 中文名 | 指数财务指标 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 季度更新 |
| 字段数量 | 121 |
| 版本 | 1.06 |

## 表描述

1.内容说明：本表记录主要A股、港股指数的财务分析衍生指标，包括净资产收益率、总资产净利率、销售净利率等指标。本表币种为人民币。
2.数据范围：2000-01-01至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=Inne... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `IndexNC` | 指数成份股数量 | number(10) | ✓ | 100.0% |  |
| 6 | `CalcNC` | 计算用成份股数量 | number(10) | ✓ | 100.0% |  |
| 7 | `LossNC` | 指数亏损成份股数量 | number(10) | ✓ | 100.0% |  |
| 8 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(12,4) | ✓ | 100.0% | 每股收益_期末股本摊薄(元/股) = ∑归母净利润 / ∑期末总股本 |
| 9 | `NAPS` | 每股净资产(元/股) | number(12,4) | ✓ | 99.95% | 每股净资产(元/股) = ∑归母所有者权益 / ∑期末总股本 |
| 10 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(19,4) | ✓ | 82.6% |  |
| 11 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 99.8% |  |
| 12 | `OperCashFlowPSTTM` | 每股经营活动产生的现金流量净额TTM(元/股) | number(19,4) | ✓ | 99.93% |  |
| 13 | `CashFlowPS` | 每股现金流量净额(元/股) | number(19,4) | ✓ | 82.47% |  |
| 14 | `CashFlowPSTTM` | 每股现金流量净额TTM(元/股) | number(19,4) | ✓ | 82.6% |  |
| 15 | `ROE` | 净资产收益率_摊薄(%) | number(12,4) | ✓ | 99.95% | 净资产收益率_摊薄(%) = ∑归母净利润 / ∑归母股东权益MRQ |
| 16 | `ROEAvg` | 净资产收益率_平均(%) | number(12,4) | ✓ | 99.95% | 净资产收益率_平均(%) = ∑归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益） |
| 17 | `ROETTM` | 净资产收益率_TTM(%) | number(12,4) | ✓ | 99.99% | 净资产收益率_TTM(%) = ∑归母净利润TTM / ∑归母股东权益MRQ |
| 18 | `WROECut` | 净资产收益率_扣除,平均(%) | number(12,4) | ✓ | 81.79% | 净资产收益率_扣除,平均(%) = ∑扣非归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益） |
| 19 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(12,4) | ✓ | 81.79% | 净资产收益率_扣除,摊薄(%) = ∑扣非归母净利润 / ∑归母股东权益MRQ |
| 20 | `ROA` | 总资产净利率(%) | number(12,4) | ✓ | 99.95% | 总资产净利率(%) = ∑净利润*2 / ∑（总资产+期初总资产） |
| 21 | `DilutedROA` | 总资产净利率_摊薄(%) | number(12,4) | ✓ | 99.95% | 总资产净利率_摊薄(%) = ∑净利润 / ∑期末总资产 |
| 22 | `ROATTM` | 总资产净利率_TTM(%) | number(12,4) | ✓ | 99.99% | 总资产净利率_TTM(%) = ∑净利润TTM / ∑期末总资产 |
| 23 | `GrossIncomeRatio` | 销售毛利率(%) | number(12,4) | ✓ | 82.43% | 销售毛利率(%) = ∑毛利润 / ∑营业收入，金融企业不适用 |
| 24 | `GrossIncomeRatioTTM` | 销售毛利率_TTM(%) | number(12,4) | ✓ | 82.43% | 销售毛利率_TTM(%) = ∑毛利润TTM / ∑营业收入TTM，金融企业不适用 |
| 25 | `NetProfitRatio` | 销售净利率(%) | number(12,4) | ✓ | 99.99% | 销售净利率(%) = ∑净利润 / ∑营业收入 |
| 26 | `NetProfitRatioTTM` | 销售净利率_TTM(%) | number(12,4) | ✓ | 100.0% | 销售净利率_TTM(%) = ∑净利润TTM / ∑营业收入TTM |
| 27 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(12,4) | ✓ | 82.43% | 销售费用/营业总收入(%) = ∑销售费用 / ∑营业总收入，金融企业不适用 |
| 28 | `OperatExpenseRateTTM` | 销售费用/营业总收入_TTM(%) | number(12,4) | ✓ | 82.43% | 销售费用/营业总收入_TTM(%) = ∑销售费用TTM / ∑营业总收入TTM，金融企业不适用 |
| 29 | `PeriodCostsRate` | 销售期间费用率(%) | number(12,4) | ✓ | 82.43% | 销售期间费用率(%) = ∑销售期间费用 / ∑营业收入，销售期间费用=销售费用+管理费用+财务费用+研发费用，金融企业... |
| 30 | `TOperatingCostToTOR` | 营业总成本/营业总收入(%) | number(12,4) | ✓ | 82.43% | 营业总成本/营业总收入(%) = ∑营业总成本 / ∑营业总收入，金融企业不适用 |
| 31 | `ROIC` | 投入资本回报率(%) | number(12,4) | ✓ | 82.4% | 投入资本回报率(%) = ∑息税前利润（1-有效税率）2 / ∑（期末全部投入资本+期初全部投入资本），金融企业不适用 |
| 32 | `OperatingProfitToTOR` | 营业利润/营业总收入(%) | number(12,4) | ✓ | 82.6% |  |
| 33 | `OperatProfitToTORTTM` | 营业利润/营业总收入_TTM(%) | number(12,4) | ✓ | 82.6% |  |
| 34 | `NPToTOR` | 净利润/营业总收入(%) | number(12,4) | ✓ | 82.6% |  |
| 35 | `NPToTORTTM` | 净利润/营业总收入_TTM(%) | number(12,4) | ✓ | 82.6% |  |
| 36 | `AdminiExpenseRate` | 管理费用/营业总收入(%) | number(12,4) | ✓ | 82.43% |  |
| 37 | `AdminiExpenseRateTTM` | 管理费用/营业总收入_TTM(%) | number(12,4) | ✓ | 82.43% |  |
| 38 | `FinancialExpenseRate` | 财务费用/营业总收入(%) | number(12,4) | ✓ | 82.43% |  |
| 39 | `FinanceExpenseRateTTM` | 财务费用/营业总收入_TTM(%) | number(12,4) | ✓ | 82.43% |  |
| 40 | `CurrentRatio` | 流动比率(%) | number(12,4) | ✓ | 82.41% | 流动比率(%) = ∑流动资产 / ∑流动负债，金融企业不适用 |
| 41 | `QuickRatio` | 速动比率(%) | number(12,4) | ✓ | 82.41% |  |
| 42 | `SEWithoutMIToTL` | 归属母公司股东的权益/负债合计(%) | number(12,4) | ✓ | 82.58% |  |
| 43 | `OperCashFlowToTL` | 经营活动产生的现金流量净额/负债合计(%) | number(12,4) | ✓ | 82.47% |  |
| 44 | `GrossProfitYOY` | 毛利润同比增长率(%) | number(12,4) | ✓ | 82.34% | 毛利润同比增长率(%) = （∑毛利率-∑上年同期毛利率） / \|∑上年同期毛利率\|，金融企业不适用 |
| 45 | `GrossProfitAdjYOY` | 毛利润(调整)同比增长率(%) | number(19,4) | ✓ | 91.47% |  |
| 46 | `NetProfitYOY` | 净利润同比增长率(%) | number(12,4) | ✓ | 99.9% |  |
| 47 | `NetProfitAdjYOY` | 净利润(调整)同比增长率(%) | number(19,4) | ✓ | 91.7% |  |
| 48 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长(%) | number(12,4) | ✓ | 81.5% |  |
| 49 | `NPParentCompanyCutAdjYOY` | 归属母公司股东的净利润(扣除)(调整)同比增长(%) | number(19,4) | ✓ | 90.72% |  |
| 50 | `NPParentComOwnersYOY` | 归属母公司股东的净利润(同比增长率)(%) | number(12,4) | ✓ | 99.91% | 归属母公司股东的净利润(同比增长率) = （∑归母净利润-∑上年同期归母净利润） / \|∑上年同期归母净利润\| |
| 51 | `NPParentComOwnersAdjYOY` | 归属母公司普通股东的净利润(调整)同比增长率(%) | number(19,4) | ✓ | 91.7% |  |
| 52 | `OperatingRevenueYOY` | 营业收入同比增长率(%) | number(12,4) | ✓ | 99.91% |  |
| 53 | `OperatingRevenueAdjYOY` | 营业收入(调整)同比增长率(%) | number(19,4) | ✓ | 91.7% |  |
| 54 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长(%) | number(12,4) | ✓ | 99.66% |  |
| 55 | `NetOperateCashFlowAdjYOY` | 经营活动产生的现金流量净额(调整)同比增长(%) | number(19,4) | ✓ | 91.54% |  |
| 56 | `CashEqIncreaseYOY` | 现金净流量同比增长(%) | number(12,4) | ✓ | 82.33% |  |
| 57 | `CashEqIncreaseAdjYOY` | 现金净流量(调整)同比增长(%) | number(19,4) | ✓ | 91.54% |  |
| 58 | `TotalAssetGrowRate` | 总资产同比增长(%) | number(12,4) | ✓ | 99.82% |  |
| 59 | `ToLiabGrowRate` | 总负债同比增长(%) | number(12,4) | ✓ | 82.46% |  |
| 60 | `SEWithoutMIYOY` | 归属母公司股东权益合计同比增长(%) | number(12,4) | ✓ | 99.82% |  |
| 61 | `TAGrowRateYTD` | 资产总计相对年初增长率(%) | number(12,4) | ✓ | 99.96% |  |
| 62 | `TLGrowRateYTD` | 负债合计相对年初增长率(%) | number(12,4) | ✓ | 82.58% |  |
| 63 | `SEWithoutMIGrowRateYTD` | 归属母公司股东的权益相对年初增长率(%) | number(12,4) | ✓ | 99.95% |  |
| 64 | `EPSGrowRateYTD` | 每股净资产相对年初增长率(%) | number(12,4) | ✓ | 99.95% |  |
| 65 | `NAORYOY` | 净资产收益率(摊薄)同比增长(%) | number(12,4) | ✓ | 99.82% |  |
| 66 | `NPParentComOwnersTTMYOY` | 归属母公司股东的净利润TTM同比增长(%) | number(19,4) | ✓ | 99.89% |  |
| 67 | `NPParentComOwnersTTMAdjYOY` | 归属母公司股东的净利润TTM(调整)同比增长(%) | number(19,4) | ✓ | 91.79% |  |
| 68 | `OperatingIncomeTTMYOY` | 营业收入_TTM同比增长(%) | number(19,4) | ✓ | 99.89% |  |
| 69 | `OperatingIncomeTTMAdjYOY` | 营业收入TTM(调整)同比增长(%) | number(19,4) | ✓ | 91.79% |  |
| 70 | `NetOpeCashFlowTTMYOY` | 经营活动产生的现金流量净额TTM同比增长(%) | number(19,4) | ✓ | 99.82% |  |
| 71 | `NetOpeCashFlowTTMAdjYOY` | 经营活动产生的现金流量净额TTM(调整)同比增长(%) | number(19,4) | ✓ | 91.79% |  |
| 72 | `InventoryGrowRateYTD` | 存货相对年初增长率(%) | number(19,4) | ✓ | 82.41% |  |
| 73 | `ARGrowRateYTD` | 应收账款相对年初增长率(%) | number(19,4) | ✓ | 82.26% |  |
| 74 | `OperCycle` | 营业周期(天/次) | number(12,4) | ✓ | 82.3% | 营业周期(天/次) = 存货周转天数+应收账款周转天数，金融类企业不计算。 |
| 75 | `NetOperCycle` | 净营业周期(天/次) | number(19,4) | ✓ | 79.92% | 净营业周期(天/次) =存货周转天数+应收账款周转天数-应付账款周转天数,金融类企业不计算。 |
| 76 | `InventoryTDays` | 存货周转天数 | number(12,4) | ✓ | 82.37% | 存货周转天数 = 周期天数 / 存货周转率，存货周转率=∑营业成本*2 / ∑（存货+期初存货），金融企业不适用 |
| 77 | `ARTDays` | 应收账款周转天数 | number(12,4) | ✓ | 82.34% | 应收账款周转天数 = 周期天数 / 应收账款周转率，应收账款周转率=∑营业收入*2 / ∑（应收账款+期初应收账款），金... |
| 78 | `CurrentTRate` | 流动资产周转率(次) | number(12,4) | ✓ | 82.44% |  |
| 79 | `FixedAssetTRate` | 固定资产周转率(次) | number(12,4) | ✓ | 82.6% |  |
| 80 | `TotalAssetTRate` | 总资产周转率(次) | number(12,4) | ✓ | 82.58% | 总资产周转率(次) = ∑营业总收入*2 / ∑（总资产+期初总资产），金融企业用营业收入 |
| 81 | `NetAssetTRate` | 净资产周转率 | number(19,4) | ✓ | 82.57% |  |
| 82 | `SaleServiceCashToOR` | 销售商品提供劳务收到的现金/营业收入(%) | number(12,4) | ✓ | 82.31% |  |
| 83 | `SaleServiceCashToORTTM` | 销售商品提供劳务收到的现金/营业收入_TTM(%) | number(12,4) | ✓ | 82.43% |  |
| 84 | `NetOperCFToToOperReve` | 经营现金净流量/营业总收入(%) | number(12,4) | ✓ | 82.47% | 经营现金净流量/营业总收入(%) = ∑经营现金净流量 / ∑营业总收入，金融企业用营业收入 |
| 85 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(12,4) | ✓ | 99.8% |  |
| 86 | `NetOpeCashFlowToNPPC` | 经营活动产生的现金流量净额/归属母公司股东的净利润(%) | number(19,4) | ✓ | 98.0% |  |
| 87 | `CashRateOfSalesTTM` | 经营活动产生的现金流量净额/营业收入_TTM(%) | number(12,4) | ✓ | 99.92% |  |
| 88 | `OperCashFlowToNetIncre` | 经营活动产生的现金流量净额/现金流量净增加额(%) | number(12,4) | ✓ | 45.8% |  |
| 89 | `DebtAssetsRatio` | 资产负债率(%) | number(12,4) | ✓ | 82.58% | 资产负债率(%) = ∑期末总负债 / ∑期末总资产 |
| 90 | `CurrentAssetsToTA` | 流动资产/总资产(%) | number(12,4) | ✓ | 82.42% |  |
| 91 | `NonCurrentAssetsToTA` | 非流动资产/总资产(%) | number(12,4) | ✓ | 82.41% |  |
| 92 | `NetTangibleAssetsTA` | 有形资产净值/总资产(%) | number(12,4) | ✓ | 82.42% | 有形资产净值/总资产(%) = （归母股东权益-（无形资产+开发支出+商誉+长期待摊费用+递延所得税资产）） / 总资产... |
| 93 | `CurrentLiabilityToTL` | 流动负债/负债合计(%) | number(12,4) | ✓ | 82.41% |  |
| 94 | `NonCurrLiabilityToTL` | 非流动负债/负债合计(%) | number(12,4) | ✓ | 82.41% |  |
| 95 | `TotalNonCurLiaToSEWMI` | 长期资本负债率(%) | number(12,4) | ✓ | 82.58% |  |
| 96 | `OutInvestOwnersEquity` | 对外投资/所有者权益(%) | number(12,4) | ✓ | 82.57% | 对外投资/所有者权益(%) = ∑（交易性金融资产+可供出售金融资产+持有至到期投资+长期股权投资+债权投资+其他债权投... |
| 97 | `EquityMultipler` | 权益乘数(%) | number(12,4) | ✓ | 99.94% |  |
| 98 | `OperatingIncome` | 营业收入(万元) | number(19,4) | ✓ | 99.99% |  |
| 99 | `OperatingIncomeTTM` | 营业收入TTM(万元) | number(19,4) | ✓ | 100.0% |  |
| 100 | `NPParentComOwners` | 归属母公司股东的净利润(万元) | number(19,4) | ✓ | 100.0% |  |
| 101 | `NPParentComOwnersTTM` | 归属母公司股东的净利润TTM(万元) | number(19,4) | ✓ | 100.0% |  |
| 102 | `NonRecurringProfitLoss` | 非经常性损益(万元) | number(19,4) | ✓ | 90.38% |  |
| 103 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(万元) | number(19,4) | ✓ | 90.99% |  |
| 104 | `NetProfitCutTTM` | 扣除非经常性损益后的归母净利润TTM(万元) | number(19,4) | ✓ | 91.53% |  |
| 105 | `NetOperateCashFlow` | 经营活动产生的现金流量净额(万元) | number(19,4) | ✓ | 99.8% |  |
| 106 | `NetOpeCashFlowTTM` | 经营现金净流量TTM(万元) | number(19,4) | ✓ | 99.93% |  |
| 107 | `NetCashFlow` | 现金及现金等价物净增加额(万元) | number(19,4) | ✓ | 91.66% |  |
| 108 | `NetCashFlowTTM` | 现金及现金等价物净增加额TTM(万元) | number(19,4) | ✓ | 82.6% |  |
| 109 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(12,4) | ✓ | 81.22% |  |
| 110 | `OperatingMIToTPTTM` | 经营活动净收益/利润总额_TTM(%) | number(12,4) | ✓ | 80.7% |  |
| 111 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(12,4) | ✓ | 81.22% |  |
| 112 | `ValueChangeNIToTPTTM` | 价值变动净收益/利润总额_TTM(%) | number(12,4) | ✓ | 80.7% |  |
| 113 | `TaxesToTP` | 所得税/利润总额(%) | number(12,4) | ✓ | 81.22% |  |
| 114 | `InvestRToTP` | 投资收益/利润总额(%) | number(12,4) | ✓ | 81.22% |  |
| 115 | `InvestRToTPTTM` | 投资收益/利润总额_TTM(%) | number(12,4) | ✓ | 80.7% |  |
| 116 | `NetNonOperaIncomeToTP` | 营业外收支净额/利润总额(%) | number(12,4) | ✓ | 81.22% |  |
| 117 | `NetNonOIToTPTTM` | 营业外收支净额/利润总额_TTM(%) | number(12,4) | ✓ | 80.7% |  |
| 118 | `NPCutToTP` | 扣除非经常损益后的净利润/净利润(%) | number(12,4) | ✓ | 80.15% |  |
| 119 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 120 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 121 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=InnerCode，得到指数内部编码的具体描述：

### EPS (每股收益_期末股本摊薄(元/股))

每股收益_期末股本摊薄(元/股) = ∑归母净利润 / ∑期末总股本

### NAPS (每股净资产(元/股))

每股净资产(元/股) = ∑归母所有者权益 / ∑期末总股本

### ROE (净资产收益率_摊薄(%))

净资产收益率_摊薄(%) = ∑归母净利润 / ∑归母股东权益MRQ

### ROEAvg (净资产收益率_平均(%))

净资产收益率_平均(%) = ∑归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益）

### ROETTM (净资产收益率_TTM(%))

净资产收益率_TTM(%) = ∑归母净利润TTM / ∑归母股东权益MRQ

### WROECut (净资产收益率_扣除,平均(%))

净资产收益率_扣除,平均(%) = ∑扣非归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益）

### ROECut (净资产收益率_扣除,摊薄(%))

净资产收益率_扣除,摊薄(%) = ∑扣非归母净利润 / ∑归母股东权益MRQ

### ROA (总资产净利率(%))

总资产净利率(%) = ∑净利润*2 / ∑（总资产+期初总资产）

### DilutedROA (总资产净利率_摊薄(%))

总资产净利率_摊薄(%) = ∑净利润 / ∑期末总资产

## SQL示例

```sql
-- 查询 指数财务指标 数据
SELECT *
FROM index_finindicator
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
