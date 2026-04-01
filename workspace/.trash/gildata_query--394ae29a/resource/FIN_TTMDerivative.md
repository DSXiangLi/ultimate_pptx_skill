# FIN_TTMDerivative

**中文名**: 公司财务TTM衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FIN_TTMDerivative` |
| MySQL表名 | `fin_ttmderivative` |
| 中文名 | 公司财务TTM衍生指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务衍生指标 |
| 更新频率 | 季更新 |
| 字段数量 | 191 |
| 版本 | 1 |

## 表描述

1.内容说明：根据上市企业(含科创板)、发债企业披露的财务数据，基于2018年新会计准则衍生计算的TTM维度财务指标，反映公司每股指标、资本结构情况以及盈利、偿债、成长、营运、分红、现金流等能力的指标。
2.本表汇总了原有的指标表所有TTM维度指标，且在指标数量和计算公式上进行了迭代更新。
3.本表针对历史数据进行了留痕：若某个报告期存在多次更正，则更正前及历次更正数据均保留。
4. TTM指标为滚动计算的指标，即最近四个季度的数据之和。
(1)最新报告期（EndDate）是年报，则TTM=年报数据；
(2)最新报告期（EndDate）非年报，则TTM=本期数据+(上年年报数据-上年同期合并数据)，上年年度值和上年同期值的取值条件为：公布时间早于等于本期且最新；
如果本期、上年年报、上年同期(合并数)存在任一报告期公告未披露，或只披露非完整公告，则返回上年年报。
5.数据范围：1989-12-31至今
6.信息来源：招股说明书、定报、审计报告等
7.数据维度：均展示人民币元。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)：1-合并调整；2-合并未调整 |
| 6 | `TotalOperatingRevenue` | 营业总收入(元) | number(19,4) | ✓ | 99.83% |  |
| 7 | `OperatingRevenue` | 营业收入(元) | number(19,4) | ✓ | 99.64% |  |
| 8 | `OperatingCost` | 营业成本-非金融类(元) | number(19,4) | ✓ | 93.3% |  |
| 9 | `OperatingPayout` | 营业支出-金融类(元) | number(19,4) | ✓ | 5.56% |  |
| 10 | `TotalOperatingCost` | 营业总成本(元) | number(19,4) | ✓ | 99.37% |  |
| 11 | `GrossProfit` | 毛利(元) | number(19,4) | ✓ | 93.83% | 毛利(元)（GrossProfit）＝营业收入－营业成本，金融类公司不计算。 |
| 12 | `OperatingExpense` | 销售费用(元) | number(19,4) | ✓ | 87.15% |  |
| 13 | `AdministrationExpense` | 管理费用(元) | number(19,4) | ✓ | 99.07% |  |
| 14 | `FinancialExpense` | 财务费用(元) | number(19,4) | ✓ | 93.84% |  |
| 15 | `RAndD` | 研发费用(元) | number(19,4) | ✓ | 33.72% |  |
| 16 | `PeriodExpense` | 期间费用(元) | number(19,4) | ✓ | 99.06% | 期间费用(元)(PeriodExpense)=销售费用+管理费用+研发费用+财务费用。 |
| 17 | `TotalCostExpense` | 成本费用总额(元) | number(19,4) | ✓ | 93.8% | 成本费用总额(元)(TotalCostExpense)=营业成本+销售费用+管理费用+研发费用+财务费用，金融类企业不计... |
| 18 | `OperatingTaxSurcharges` | 营业税金及附加(元) | number(19,4) | ✓ | 98.69% |  |
| 19 | `InvestIncome` | 投资收益(元) | number(19,4) | ✓ | 88.73% |  |
| 20 | `InvestIncomeAssociates` | 对联营合营公司投资收益(元) | number(19,4) | ✓ | 48.86% |  |
| 21 | `FairValueChangeIncome` | 公允价值变动损益(元) | number(19,4) | ✓ | 43.43% |  |
| 22 | `AssetImpairmentLoss` | 资产减值损失(元) | number(19,4) | ✓ | 81.6% |  |
| 23 | `OperatingProfit` | 营业利润(元) | number(19,4) | ✓ | 99.45% |  |
| 24 | `NonoperatingIncome` | 营业外收入(元) | number(19,4) | ✓ | 97.42% |  |
| 25 | `TotalProfit` | 利润总额(元) | number(19,4) | ✓ | 99.72% |  |
| 26 | `IncomeTaxCost` | 所得税(元) | number(19,4) | ✓ | 97.31% |  |
| 27 | `NetProfit` | 净利润(元) | number(19,4) | ✓ | 99.89% |  |
| 28 | `NPParentCompanyOwners` | 归属母公司股东的净利润(元) | number(19,4) | ✓ | 99.36% |  |
| 29 | `NPCParentCompanyOwners` | 归属母公司普通股股东的净利润(元) | number(19,4) | ✓ | 0.02% |  |
| 30 | `MinorityProfit` | 少数股东损益(元) | number(19,4) | ✓ | 75.4% |  |
| 31 | `NonRecurringProfitLoss` | 非经常性损益(元) | number(19,4) | ✓ | 52.4% | 非经常性损益(元)（NonRecurringProfitLoss）：取定期报告公布值。 若未披露，则：非经常性损益=母公... |
| 32 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(元) | number(19,4) | ✓ | 52.4% | 扣除非经常性损益后的归母净利润(元)（NetProfitCut）：取公布值。 若未披露，则：扣除非经常性损益后的净利润=... |
| 33 | `NetIncomeFromOperating` | 经营活动净收益(元) | number(19,4) | ✓ | 99.07% | 经营活动净收益(元)（NetIncomeFromOperating）：对于非金融类企业，经营活动净收益＝营业总收入－营业... |
| 34 | `NetIncFromValueChange` | 价值变动净收益(元) | number(19,4) | ✓ | 87.5% | 价值变动净收益(元)(NetIncFromValueChange)=投资净收益+公允价值变动净收益+汇兑收益。 |
| 35 | `NetInterestExpense` | 净利息费用(元) | number(19,4) | ✓ | 75.26% | 净利息费用(元)(NetInterestExpense)=利息支出（不含资本化利息）-利息收入，金融类企业不计算。 |
| 36 | `EBIT` | 息税前利润(反推)(元) | number(19,4) | ✓ | 93.98% | 息税前利润(反推)(元)（EBIT）＝利润总额＋利息费用, 其中，利息费用优先取NetInterestExpense[净... |
| 37 | `EBITDA` | 息税折旧摊销前利润(反推)(元) | number(19,4) | ✓ | 88.53% | 息税折旧摊销前利润(反推)(元)（EBITDA）＝息税前利润EBIT+当期计提折旧和摊销，其中，"息税前利润"计算方法详... |
| 38 | `EBIT_Positive` | 息税前利润(正向)(元) | number(19,4) | ✓ | 99.19% | 息税前利润(正向)(元)(EBIT_Positive)：非银行类公司：营业总收入-(营业总成本-财务费用)+(资产减值损... |
| 39 | `EBITDA_Positive` | 息税折旧摊销前利润(正向)(元) | number(19,4) | ✓ | 92.29% | 息税折旧摊销前利润(正向)(元)(EBITDA_Positive)=息税前利润(正向）+当期计提折旧和摊销，其中，"息税... |
| 40 | `EBIAT` | 息前税后利润(反推)(元) | number(19,4) | ✓ | 93.98% | 息前税后利润(反推)(元)（EBIAT）=EBIT*(1-有效税率），其中，当所得税，利润总额均大于0时，有效税率=所得... |
| 41 | `PreFinExpOP` | 扣除财务费用前营业利润(元) | number(19,4) | ✓ | 93.82% | 扣除财务费用前营业利润(元)(PreFinExpOP)=营业利润+财务费用，金融类企业不计算。 |
| 42 | `NonOperatingProfit` | 非营业利润(元) | number(19,4) | ✓ | 99.27% | 非营业利润(元)(NonOperatingProfit)=利润总额-营业利润。 |
| 43 | `NetNonoperating` | 营业外收支净额(元) | number(19,4) | ✓ | 98.05% | 营业外收支净额(元)(NetNonoperating)=营业外收入-营业外支出。 |
| 44 | `GoodsSaleServRendCash` | 销售商品提供劳务收到的现金(元) | number(19,4) | ✓ | 92.76% |  |
| 45 | `OthCashInRelOpe` | 收到其他与经营活动有关的现金(元) | number(19,4) | ✓ | 97.46% |  |
| 46 | `SuOpCashInflow` | 经营活动现金流入小计(元) | number(19,4) | ✓ | 97.77% |  |
| 47 | `GoodsServicesCashPaid` | 购买商品接受劳务支付的现金(元) | number(19,4) | ✓ | 92.37% |  |
| 48 | `StaffBehalfPaid` | 支付给职工以及为职工支付的现金(元) | number(19,4) | ✓ | 97.35% |  |
| 49 | `OtherOperateCashPaid` | 支付其他与经营活动有关的现金(元) | number(19,4) | ✓ | 97.64% |  |
| 50 | `NetOperateCashFlow` | 经营活动产生的现金净流量(元) | number(19,4) | ✓ | 97.95% |  |
| 51 | `FixInOAsAcCash` | 购建固定资产、无形资产和其他长期资产支付的现金(元) | number(19,4) | ✓ | 97.08% |  |
| 52 | `FixInOtADisCash` | 处置固定资产、无形资产和其他长期资产收回的现金净额(元) | number(19,4) | ✓ | 82.07% |  |
| 53 | `NetCashFromSubCompany` | 取得子公司及其他营业单位支付的现金净额(元) | number(19,4) | ✓ | 25.52% |  |
| 54 | `NetInvestCashFlow` | 投资活动产生的现金流量净额(元) | number(19,4) | ✓ | 97.69% |  |
| 55 | `NetFinanceCashFlow` | 筹资活动产生的现金流量净额(元) | number(19,4) | ✓ | 97.33% |  |
| 56 | `CashEquivalentIncrease` | 现金净流量(元) | number(19,4) | ✓ | 97.83% |  |
| 57 | `CurrentAccruedDA` | 当期计提折旧与摊销(元) | number(19,4) | ✓ | 92.35% | 当期计提折旧与摊销(元)（CurrentAccruedDA）=固定资产折旧＋投资性房地产折旧/摊销+无形资产摊销＋长期待... |
| 58 | `EnterpriseFCF` | 企业自由现金流量(元) | number(19,4) | ✓ | 88.53% | 企业自由现金流量(元)(EnterpriseFCF)：息税前利润*(1-有效税率)+当期计提折旧和摊销-期末净营运资本+... |
| 59 | `ShareHolderFCF` | 股权自由现金流量(元) | number(19,4) | ✓ | 88.53% | 股权自由现金流量(元)(ShareHolderFCF)=企业自由现金流量-偿还债务支付的现金+取得借款收到的现金+发行债... |
| 60 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(19,4) | ✓ | 97.42% | 每股收益_期末股本摊薄(元/股)（EPS）=归属于母公司普通股股东的净利润（若为空，则取“归属于母公司所有者的净利润”）... |
| 61 | `EPSCut` | 每股收益(扣除)(元/股) | number(19,4) | ✓ | 52.31% | 每股收益(扣除)(元/股)（EPSCut）：每股收益=扣除非经常性损益后普通股股东的净利润(元)(若为空，则取“扣除非经... |
| 62 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(19,4) | ✓ | 97.53% | 每股营业总收入(元/股)(TotalOperateRevenuePS)=营业总收入/期末总股本。 |
| 63 | `MainIncomePS` | 每股营业收入(元/股) | number(19,4) | ✓ | 97.36% | 每股营业收入(元/股)（MainIncomePS）＝营业收入/期末总股本。 |
| 64 | `OperProfitPS` | 每股营业利润(元/股) | number(19,4) | ✓ | 97.45% | 每股营业利润(元/股)（OperProfitPS）＝营业利润/期末总股本。 |
| 65 | `EBITPS` | 每股息税前利润(反推)(元/股) | number(19,4) | ✓ | 92.3% | 每股息税前利润(反推)(元/股)（EBITPS）＝息税前利润/期末总股本；“息税前利润”计算方法见EBIT[息税前利润(... |
| 66 | `EBITDAPS` | 每股息税折旧摊销前利润(反推)(元/股) | number(19,4) | ✓ | 87.3% | 每股息税折旧摊销前利润(反推)(元/股)(EBITDAPS)＝息税折旧摊销前利润(反推)/期末总股本；“息税折旧摊销前利... |
| 67 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 96.12% | 每股经营活动产生的现金流量净额(元/股)（OperCashFlowPS）：经营活动产生的现金流量净额/期末总股本。 |
| 68 | `CashFlowPS` | 每股现金流量净额(元/股) | number(19,4) | ✓ | 96.09% | 每股现金流量净额(元/股)（CashFlowPS）=现金及现金等价物净增加额/期末总股本。 |
| 69 | `EnterpriseFCFPS` | 每股企业自由现金流量(元/股) | number(19,4) | ✓ | 87.3% | 每股企业自由现金流量（EnterpriseFCFPS）=企业自由现金流量/期末总股本，其中，"企业自由现金流量"计算方法... |
| 70 | `ShareHolderFCFPS` | 每股股权自由现金流量(元/股) | number(19,4) | ✓ | 87.3% | 每股股东自由现金流量（ShareholderFCFPS）=股权自由现金流量/期末总股本，其中，"股权自由现金流量"计算方... |
| 71 | `ROE` | 净资产收益率_摊薄(%) | number(19,4) | ✓ | 95.62% | 净资产收益率_摊薄(%)（ROE）=归属于母公司所有者的净利润/期末归属母公司所有者权益(或股东权益)合计*100%。 |
| 72 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(19,4) | ✓ | 50.84% | 净资产收益率_扣除,摊薄(%)（ROECut）=扣除非经常性损益后的归母净利润/该报告期期末归属母公司所有者权益(或股东... |
| 73 | `ROA_EBIT` | 总资产报酬率(%) | number(19,4) | ✓ | 91.82% | 总资产报酬率（ROA_EBIT）＝息税前利润/期末资产总计*100% 其中，“息税前利润”计算方法见EBIT[息税前利润... |
| 74 | `ROA` | 总资产净利率(%) | number(19,4) | ✓ | 97.61% | 总资产净利率（ROA）＝净利润/期末资产总计*100%。 |
| 75 | `ROACut` | 总资产净利率_不含少数股东损益(%) | number(19,4) | ✓ | 97.1% | 总资产净利率_不含少数股东损益(%)(ROACut)＝归属于母公司所有者的净利润/期末总资产总计*100%。 |
| 76 | `ROIC` | 投入资本回报率(%) | number(19,4) | ✓ | 91.22% | 投入资本回报率（ROIC）=息前税后净利润/期末全部投入资本*100% ,金融类企业不计算。 |
| 77 | `GrossIncomeRatio` | 销售毛利率(%) | number(19,4) | ✓ | 93.16% | 销售毛利率(%)(GrossIncomeRatio)=（营业收入-营业成本）/营业收入*100%，金融类企业不计算。 |
| 78 | `NetProfitRatio` | 销售净利率(%) | number(19,4) | ✓ | 99.32% | 销售净利率（NetProfitRatio）＝净利润/营业收入*100%。 |
| 79 | `SalesCostRatio` | 销售成本率(%) | number(19,4) | ✓ | 93.16% | 销售成本率（SalesCostRatio）＝营业成本/营业收入*100%，金融类企业不计算。 |
| 80 | `TOperatingCostToTOR` | 营业总成本/营业总收入(%) | number(19,4) | ✓ | 99.01% | 营业总成本/营业总收入(%)(TOperatingCostToTOR)=营业总成本(含减值损失）／营业总收入*100%。 |
| 81 | `TotalProfitCostRatio` | 成本费用利润率(%) | number(19,4) | ✓ | 93.64% | 成本费用利润率(%)（TotalProfitCostRatio）＝利润总额/(营业成本+财务费用+销售费用+管理费用+研... |
| 82 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(19,4) | ✓ | 86.86% | 销售费用/营业总收入(%)( OperatingExpenseRate)=销售费用/营业总收入*100%，金融类企业不计... |
| 83 | `AdminiExpenseRate` | 管理费用/营业总收入(%) | number(19,4) | ✓ | 98.78% | 管理费用/营业总收入(%)(AdminiExpenseRate)=管理费用/营业总收入*100%，金融类企业不计算。 |
| 84 | `FinancialExpenseRate` | 财务费用/营业总收入(%) | number(19,4) | ✓ | 93.34% | 财务费用/营业总收入(%)( FinancialExpenseRate)=财务费用/营业总收入*100%，金融类企业不计... |
| 85 | `RAndDExpenseRate` | 研发费用/营业总收入(%) | number(19,4) | ✓ | 33.69% | 研发费用/营业总收入(%)(RAndDExpenseRate)=研发费用/营业总收入*100%。 |
| 86 | `PeriodCostsRate` | 销售期间费用率(%) | number(19,4) | ✓ | 98.62% | 销售期间费用率（PeriodCostsRate）＝期间费用/营业收入*100%。 |
| 87 | `AssetImpaLossToTOR` | 资产减值损失/营业总收入(%) | number(19,4) | ✓ | 81.48% | 资产减值损失/营业总收入(%)(AssetImpaLossToTOR)=资产减值损失/营业总收入*100%。 |
| 88 | `AssetILossToOProfit` | 资产减值损失/营业利润(%) | number(19,4) | ✓ | 69.48% | 资产减值损失/营业利润(%)(AssetILossToOProfit)=资产减值损失/营业利润*100%。 |
| 89 | `TaxRatio` | 销售税金率(%) | number(19,4) | ✓ | 98.35% | 销售税金率(%)（TaxRatio）=营业税金及附加/营业收入*100%。 |
| 90 | `OperatingProfitMargin` | 营业利润率(%) | number(19,4) | ✓ | 99.02% | 营业利润率(%)(OperatingProfitMargin)=营业利润/营业收入*100%。 |
| 91 | `OperatingProfitToTOR` | 营业利润/营业总收入(%) | number(19,4) | ✓ | 99.16% | 营业利润/营业总收入(%)(OperatingProfitToTOR)=营业利润/营业总收入*100%。 |
| 92 | `PreFinExpOPToOR` | 扣除财务费用前营业利润/营业收入(%) | number(19,4) | ✓ | 93.42% | 扣除财务费用前营业利润/营业收入(%)(PreFinExpOPToOR)=扣除融资费用前营业利润/营业收入*100%,金... |
| 93 | `ToProfToOperRevenue` | 利润总额/营业收入(%) | number(19,4) | ✓ | 99.19% | 利润总额/营业收入(%)(ToProfToOperRevenue)=利润总额/营业收入*100%。 |
| 94 | `NPToTOR` | 净利润/营业总收入(%) | number(19,4) | ✓ | 99.48% | 净利润/营业总收入(%)(NPToTOR)：=净利润/营业总收入*100%。 |
| 95 | `NPPCToOR` | 归属于母公司股东的净利润/营业收入(%) | number(19,4) | ✓ | 98.85% | 归属于母公司股东的净利润/营业收入(%)(NPPCToOR)=归属于母公司股东的净利润/营业收入*100%。 |
| 96 | `EBITToTOR` | 息税前利润(反推)/营业总收入(%) | number(19,4) | ✓ | 93.55% | 息税前利润(反推)/营业总收入(%)(EBITToTOR)=息税前利润(反推)/营业总收入*100%，其中，"息税前利润... |
| 97 | `EBITDAToTOR` | 息税折旧摊销前利润(反推)/营业总收入(%) | number(19,4) | ✓ | 88.26% | 息税折旧摊销前利润(反推)/营业总收入(%)(EBITDAToTOR)=息税折旧摊销前利润(反推)/营业总收入*100%... |
| 98 | `OperCashInToDueDebt` | 现金到期债务比 | number(19,4) | ✓ | 85.0% | 现金到期债务比(OperCashInToDueDebt)=经营活动产生的现金流量净额／（短期借款+一年内到期的非流动负债... |
| 99 | `EntireliabToEBITDA` | 全部债务/息税折旧摊销前利润(反推) | number(19,4) | ✓ | 78.03% | 全部债务/息税折旧前利润(EntireliabToEBITDA)=全部债务/息税折旧前利润，其中,"息税折旧摊销前利润(... |
| 100 | `OperProfitToCL` | 营业利润/流动负债(%) | number(19,4) | ✓ | 91.39% | 营业利润/流动负债(%)(OperProfitToCL)=营业利润/流动负债合计*100%。 |
| 101 | `OperProfitToTL` | 营业利润/负债合计(%) | number(19,4) | ✓ | 96.97% | 营业利润/负债合计(%)(OperProfitToTL)=营业利润/负债总计*100%。 |
| 102 | `EBITToInteBearDebt` | 息税前利润(反推)/带息债务(%) | number(19,4) | ✓ | 84.97% | 息税前利润(反推)/带息债务(%)(EBITToInteBearDebt)=息税前利润/带息债务*100%，"息税前利润... |
| 103 | `EBITDAToIntBearDebt` | 息税折旧摊销前利润(反推)/带息债务(%) | number(19,4) | ✓ | 80.3% | 息税折旧前利润/带息债务(%)(EBITDAToIntBearDebt)=息税折旧摊销前利润(反推)/带息债务*100%... |
| 104 | `EBITDAToFinExp` | 息税折旧摊销前利润(反推)/财务费用 | number(19,4) | ✓ | 68.85% | 息税折旧摊销前利润(反推)/财务费用(EBITDAToFinExp)=息税折旧摊销前利润(反推)/财务费用，金融企业不计... |
| 105 | `OperCashToCurrentDebt` | 现金流动负债比(%) | number(19,4) | ✓ | 90.22% | 现金流动负债比(%)(OperCashToCurrentDebt)=经营活动产生的现金净流入/流动负债合计，金融类企业不... |
| 106 | `OperCashFlowToTL` | 经营活动产生的现金流量净额/负债合计 | number(19,4) | ✓ | 95.63% | 经营活动产生的现金流量净额/负债合计(OperCashFlowToTL)=经营活动产生的现金流量净额/负债总计。 |
| 107 | `NOCFToInterestBearDebt` | 经营活动产生的现金流量净额/带息债务 | number(19,4) | ✓ | 84.17% | 经营活动产生现金流量净额/带息债务（NOCFToInterestBearDebt）=经营活动产生的现金流量净额/带息债务... |
| 108 | `OperCashFlowToCL` | 经营活动产生的现金流量净额/流动负债 | number(19,4) | ✓ | 90.28% | 经营活动产生的现金流量净额/流动负债(OperCashFlowToCL)=经营活动产生的现金流量净额/流动负债合计。 |
| 109 | `NOCFToNetDebt` | 经营活动产生的现金流量净额/净债务 | number(19,4) | ✓ | 61.49% | 经营活动产生现金流量净额/净债务（NOCFToNetDebt）=经营活动产生的现金流量净额/净债务，其中，金融类企业不计... |
| 110 | `NOCFToTotalNonCurLia` | 经营活动产生的现金流量净额/非流动负债 | number(19,4) | ✓ | 85.86% | 经营活动产生现金流量净额/非流动负债(%)(NOCFToTotalNonCurLia)=经营活动产生现金流量净额/非流动... |
| 111 | `NetNoFCFToCLiability` | 非筹资性现金净流量/流动负债 | number(19,4) | ✓ | 90.39% | 非筹资性现金净流量与流动负债的比率(NetNoFCFToCLiability)=（经营活动产生的现金流量净额+投资活动产... |
| 112 | `NetNoFCFToTLiability` | 非筹资性现金净流量/负债合计 | number(19,4) | ✓ | 95.64% | 非筹资性现金净流量与负债总额的比率(NetNoFCFToTLiability)=（经营活动产生的现金流量净额+投资活动产... |
| 113 | `OperCashPSGrowRate` | 每股经营活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 87.35% | 每股经营活动产生的现金流量净额同比增长(%)(OperCashPSGrowRate)=（本期每股经营活动产生的现金流量净... |
| 114 | `TORGrowRate` | 营业总收入同比增长率(%) | number(19,4) | ✓ | 91.78% | 营业总收入同比增长率(%)(TORGrowRate)=（本期营业总收入-上年同期营业总收入）/ABS(上年同期营业总收入... |
| 115 | `OperatingRevenueYOY` | 营业收入同比增长率(%) | number(19,4) | ✓ | 91.72% | 营业收入同比增长率(%)(OperatingRevenueYOY)=(本期营业收入-上年同期营业收入)/NULLIF(A... |
| 116 | `OperatingCostGrowRate` | 营业成本同比增长率(%) | number(19,4) | ✓ | 86.14% | 营业成本同比增长率(%)(OperatingCostGrowRate)=(本期营业成本-上年同期营业成本)/NULLIF... |
| 117 | `ToOpCostGrowRate` | 营业总成本同比增长率(%) | number(19,4) | ✓ | 91.68% | 营业总成本同比增长(%)(ToOpCostGrowRate)=（本期营业总成本-上年同期营业总成本）/ABS(上年同期营... |
| 118 | `RAndDExpenseGrowRate` | 研发费用同比增长率(%) | number(19,4) | ✓ | 29.46% | 研发费用同比增长率(%)(RAndDExpenseGrowRate)=(本期研发费用-上年同期研发费用)/NULLIF(... |
| 119 | `GrossProfitGrowRate` | 毛利同比增长率(%) | number(19,4) | ✓ | 86.48% | 毛利同比增长率(%)(GrossProfitGrowRate)=(本期毛利-上年同期毛利)/NULLIF(ABS(上年同... |
| 120 | `OperProfitGrowRate` | 营业利润同比增长率(%) | number(19,4) | ✓ | 91.75% | 营业利润同比增长(%)(OperProfitGrowRate)=（本期营业利润-上年同期营业利润）/ABS(上年同期营业... |
| 121 | `TotalProfitGrowRate` | 利润总额同比增长率(%) | number(19,4) | ✓ | 91.99% | 利润总额同比增长率(%)(TotalProfitGrowRate)=(本期利润总额-上年同期利润总额)/NULLIF(A... |
| 122 | `NetProfitYOY` | 净利润同比增长率(%) | number(19,4) | ✓ | 92.08% | 净利润同比增长率(%)(NetProfitYOY)=(本期净利润-上年同期净利润)/NULLIF(ABS(上年同期净利润... |
| 123 | `NPParentCompanyYOY` | 归属母公司股东的净利润同比增长(%) | number(19,4) | ✓ | 91.7% | 归属母公司股东的净利润同比增长(%)(NPParentCompanyYOY)=（本期归属母公司股东的净利润-上年同期归属... |
| 124 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长率(%) | number(19,4) | ✓ | 46.39% | 归属母公司股东的净利润(扣除)同比增长(%)(NPParentCompanyCutYOY)=（本期扣除非经常性损益后的归... |
| 125 | `SaleSerRenderCashYOY` | 销售商品、提供劳务收到的现金同比增长率(%) | number(19,4) | ✓ | 85.45% | 销售商品、提供劳务收到的现金同比增长率(%)(SaleSerRenderCashYOY)=(本期销售商品、提供劳务收到的... |
| 126 | `GoodsSerCashPaidYOY` | 购买商品、接受劳务支付的现金同比增长率(%) | number(19,4) | ✓ | 85.1% | 购买商品、接受劳务支付的现金同比增长率(%)(GoodsSerCashPaidYOY)=(本期购买商品、接受劳务支付的现... |
| 127 | `StaffBehalfPaidYOY` | 支付给职工以及为职工支付的现金同比增长率(%) | number(19,4) | ✓ | 89.64% | 支付给职工以及为职工支付的现金同比增长率(%)(StaffBehalfPaidYOY)=(本期支付给职工以及为职工支付的... |
| 128 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 90.17% | 经营活动产生的现金流量净额同比增长(%)(NetOperateCashFlowYOY)=（本期经营活动产生的现金流量净额... |
| 129 | `SuOpCashInflowYOY` | 经营活动现金流入小计同比增长率(%) | number(19,4) | ✓ | 90.04% | 经营活动现金流入小计同比增长率(%)(SuOpCashInflowYOY)=（本期经营活动现金流入小计-上年同期经营活动... |
| 130 | `InvestCashGrowRate` | 投资活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 89.87% | 投资活动产生的现金流量净额增长率(%)(InvestCashGrowRate)=（本期投资活动产生的现金流量净额-上年同... |
| 131 | `FinancingCashGrowRate` | 筹资活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 89.15% | 筹资活动产生的现金流量净额增长率(%)(FinancingCashGrowRate)=（本期筹资活动产生的现金流量净额-... |
| 132 | `CashEqIncreaseYOY` | 现金净流量同比增长率(%) | number(19,4) | ✓ | 90.09% | 现金净流量同比增长(%)(CashEqIncreaseYOY)=（本期现金及现金等价物净增加额-上年同期现金及现金等价物... |
| 133 | `NAORYOY` | 净资产收益率(摊薄)同比增长率(%) | number(19,4) | ✓ | 86.01% | 净资产收益率(摊薄)同比增长(%)(NAORYOY)=（本期净资产收益率(摊薄)-上年同期净资产收益率(摊薄)）/ABS... |
| 134 | `GrossIncomeRatioYOY` | 毛利率同比增长率(%) | number(19,4) | ✓ | 86.0% | 毛利率同比增长率(%)(GrossIncomeRatioYOY)=(本期毛利率-上年同期毛利率)/ABS(上年同期毛利率... |
| 135 | `NetProfitCashCoverYOY` | 净利润现金含量同比增长率(%) | number(19,4) | ✓ | 74.99% | 净利润现金含量同比增长率(%)(NetProfitCashCoverYOY)=(本期净利润现金含量-上年同期净利润现金含... |
| 136 | `InventoryTRate` | 存货周转率(次) | number(19,4) | ✓ | 87.97% | 存货周转率（InventoryTRate）＝本期营业成本*2/（上年同期存货+期末存货），金融类企业不计算。 |
| 137 | `ARTRate` | 应收账款周转率(次) | number(19,4) | ✓ | 86.88% | 应收账款周转率（ARTRate）＝营业收入*2/（上年同期应收账款+期末应收账款），金融类企业不计算。 |
| 138 | `BillARTRate` | 应收票据及应收账款周转率(次) | number(19,4) | ✓ | 88.43% | 应收票据及应收账款周转率(次)(BillARTRate)=营业收入*2/(上年同期应收票据及应收账款+期初应收票据及应收... |
| 139 | `ContraAssetTRate` | 合同资产周转率(次) | number(19,4) | ✓ | 10.77% | 合同资产周转率(次)(ContraAssetTRate)=本期营业收入*2/（期末合同资产+上年同期合同资产），金融类企... |
| 140 | `AdvPayTRate` | 预付账款周转率(次) | number(19,4) | ✓ | 88.39% | 预付账款周转率(次)(AdvPayTRate)=本期营业成本*2/（期末预付款项+上年同期预付款项），金融类企业不计算。 |
| 141 | `CurrentTRate` | 流动资产周转率(次) | number(19,4) | ✓ | 91.04% | 流动资产周转率(次)(CurrentTRate)=本期营业总收入*2/（期末流动资产合计+上年同期流动资产合计），金融类... |
| 142 | `FixedAssetTRate` | 固定资产周转率(次) | number(19,4) | ✓ | 95.65% | 固定资产周转率（FixedAssetTRate）＝营业总收入*2/(上年同期固定资产+期末固定资产)。 |
| 143 | `TotalFixedATRate` | 固定资产合计周转率(次) | number(19,4) | ✓ | 90.76% | 固定资产合计周转率(次)(TotalFixedATRate)=2*营业总收入/(期末固定资产合计+上年同期固定资产合计)... |
| 144 | `IntangibleATRate` | 无形资产周转率(次) | number(19,4) | ✓ | 86.14% | 无形资产周转率(次)(IntangibleATRate)=营业总收入*2/(上年同期无形资产+期末无形资产），金融类企业... |
| 145 | `NonCurrentATRate` | 非流动资产周转率(次) | number(19,4) | ✓ | 90.89% | 非流动资产周转率(次)(NonCurrentATRate)=本期营业总收入*2/（上年同期非流动资产合计+期末非流动资产... |
| 146 | `TotalAssetTRate` | 总资产周转率(次) | number(19,4) | ✓ | 97.22% | 总资产周转率（TotalAssetTRate）＝营业总收入*2/（上年同期资产总计+期末资产总计）。 |
| 147 | `AccountsPayablesTRate` | 应付账款周转率(次) | number(19,4) | ✓ | 86.68% | 应付账款周转率（AccountsPayablesTRate）＝营业成本*2/（上年同期应付账款+期末应付账款），金融类企... |
| 148 | `NotAccPayableTRate` | 应付票据及应付账款周转率(次) | number(19,4) | ✓ | 89.14% | 应付票据及应付账款周转率(次)(NotAccPayableTRate)=本期营业成本*2/（期末应付票据及应付账款+上年... |
| 149 | `ConLiabTRate` | 合同负债周转率(次) | number(19,4) | ✓ | 29.35% | 合同负债周转率(次)(ConLiabTRate)=本期营业收入*2/（期末合同负债+上年同期合同负债），金融类企业不计算... |
| 150 | `AdvanceReceTRate` | 预收账款周转率(次) | number(19,4) | ✓ | 69.97% | 预收账款周转率(次)(AdvanceReceTRate)=本期营业收入*2/（期末预收款项+上年同期预收款项），金融类企... |
| 151 | `CurLiaTRate` | 流动负债周转率(次) | number(19,4) | ✓ | 90.99% | 流动负债周转率(次)(CurLiaTRate)=本期营业总收入*2/（期末流动负债合计+上年同期流动负债合计），金融类企... |
| 152 | `NonCurLiaTRate` | 非流动负债周转率(次) | number(19,4) | ✓ | 86.83% | 非流动负债周转率(次)(NonCurLiaTRate)=本期营业总收入*2/（期末非流动负债合计+上年同期非流动负债合计... |
| 153 | `EquityTRate` | 归母股东权益周转率(次) | number(19,4) | ✓ | 95.36% | 归母股东权益周转率(次)（EquityTRate）＝本期营业总收入*2/(上年同期归属母公司所有者权益(或股东权益)合计... |
| 154 | `WorkingCaitalTRate` | 营运资本周转率(次) | number(19,4) | ✓ | 70.55% | 营运资本周转率(次)(WorkingCaitalTRate)=本期营业总收入*2/（上年同期营运资本+期末营运资本），其... |
| 155 | `NetOperCFToToAssets` | 总资产现金回收率_摊薄(%) | number(19,4) | ✓ | 95.83% | 总资产现金回收率_摊薄(%)(NetOperCFToToAssets)=经营活动产生的现金流量净额/总资产*100%。 |
| 156 | `OperatingReveCashCover` | 营业收入现金含量(%) | number(19,4) | ✓ | 92.58% | 营业收入现金含量(%)(OperatingReveCashCover)=销售商品提供劳务收到的现金/营业收入*100%。 |
| 157 | `NetProfitCashCover` | 净利润现金含量(%) | number(19,4) | ✓ | 86.54% | 净利润现金含量(%)（NetProfitCashCover）＝经营活动产生的现金流量净额/净利润*100%。 |
| 158 | `CapitalExpenditureToDM` | 资本支出/折旧和摊销 | number(19,4) | ✓ | 91.76% | 资本支出/折旧和摊销（CapitalExpenditureToDM）=购建固定资产、无形资产和其他长期资产支付的现金／当... |
| 159 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(19,4) | ✓ | 97.49% | 经营活动产生的现金流量净额/营业收入(%)(CashRateOfSales)=经营活动产生的现金流量净额/营业收入*10... |
| 160 | `NetOperCFToToOperReve` | 经营现金净流量/营业总收入(%) | number(19,4) | ✓ | 97.56% | 经营现金净流量/营业总收入(%)(NetOperCFToToOperReve)=经营活动产生的现金流量净额/营业总收入*... |
| 161 | `NOCFToOperatingNI` | 经营活动产生的现金流量净额/经营活动净收益(%) | number(19,4) | ✓ | 70.6% | 经营活动产生的现金流量净额/经营活动净收益(NOCFToOperatingNI)＝经营活动产生的现金流量净额/经营活动净... |
| 162 | `NOCFToOperatingProf` | 经营活动产生的现金流量净额/营业利润(%) | number(19,4) | ✓ | 83.23% | 经营活动产生的现金流量净额/营业利润(%)(NOCFToOperatingProf)=经营活动产生的现金流量净额/营业利... |
| 163 | `NOCFToEBITDA` | 经营活动产生的现金流量净额/息税折旧摊销前利润(反推) | number(19,4) | ✓ | 83.45% | 经营活动产生的现金流量净额/息税折旧摊销前利润(反推)(NOCFToEBITDA)=经营活动产生的现金流量净额/息税折旧... |
| 164 | `NetOperCFRatio` | 经营活动产生的现金流量净额占比 | number(19,4) | ✓ | 55.26% | 经营活动产生的现金流量净额占比(NetOperCFRatio)=经营活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 165 | `NetInvestCFRatio` | 投资活动产生的现金流量净额占比 | number(19,4) | ✓ | 55.11% | 投资活动产生的现金流量净额占比(NetInvestCFRatio)=投资活动产生的现金流量净额/(经营活动产生的现金流量... |
| 166 | `NetFinaCFRatio` | 筹资活动产生的现金流量净额占比 | number(19,4) | ✓ | 54.9% | 筹资活动产生的现金流量净额占比(NetFinaCFRatio)=筹资活动产生的现金流量净额/(经营活动产生的现金流量净额... |
| 167 | `FreeCashFlowToNPPC` | 自由现金流与归属母公司净利润比率 | number(19,4) | ✓ | 77.2% | 自由现金流与归属母公司净利润比率(FreeCashFlowToNPPC)=企业自由现金流量/归属母公司股东的净利润，其中... |
| 168 | `Dividend` | 累计派现合计(元) | number(19,4) | ✓ | 31.35% | 累计派现合计(元)(Dividend)：根据公司公布的分红实施方案，将当年年初至当前截止日期实施的多次分红求和计算。 |
| 169 | `DividendCover` | 股利保障倍数(倍) | number(19,4) | ✓ | 31.35% | 股利保障倍数（DividendCover）＝归属于母公司所有者的净利润/累计派现合计。 |
| 170 | `CashDividendCover` | 现金股利保障倍数(倍) | number(19,4) | ✓ | 29.88% | 现金股利保障倍数（CashDividendCover）＝经营活动产生的现金流量净额/本期实际支付的普通股股利。 |
| 171 | `DividendPS` | 每股股利(元) | number(19,4) | ✓ | 31.35% | 每股股利(元)(DividendPS)=累计派现合计/期末总股本。 |
| 172 | `AccRecToOR` | 应收账款/营业收入(%) | number(19,4) | ✓ | 86.89% | 应收账款/营业收入(%)(AccRecToOR)=应收账款/营业收入*100%，金融类企业不计算。 |
| 173 | `MainProfitProportion` | 主营业务比率(%) | number(19,4) | ✓ | 88.89% | 主营业务比率(%)(MainProfitProportion)=营业利润/利润总额*100%。 |
| 174 | `PreFinExpOPToTP` | 扣除财务费用前营业利润/利润总额(%) | number(19,4) | ✓ | 93.78% | 扣除财务费用前营业利润/利润总额(%)(PreFinExpOPToTP)=扣除融资费用前营业利润/利润总额*100%，金... |
| 175 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(19,4) | ✓ | 88.57% | 经营活动净收益／利润总额（OperatingNIToTP）＝经营活动净收益／利润总额*100%，“其中，"经营活动净收益... |
| 176 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(19,4) | ✓ | 78.14% | 价值变动净收益／利润总额（ValueChangeNIToTP）＝价值变动净收益／利润总额*100% 其中，"价值变动净收... |
| 177 | `InvestRAssociatesToTP` | 对联营合营公司投资收益/利润总额(%) | number(19,4) | ✓ | 43.24% | 对联营合营公司投资收益/利润总额(%)(InvestRAssociatesToTP)=对联营合营公司投资收益/利润总额*... |
| 178 | `InvestRToTP` | 投资收益/利润总额(%) | number(19,4) | ✓ | 79.26% | 投资收益/利润总额(%)(InvestRToTP)=投资净收益/利润总额*100%。 |
| 179 | `NonOProToTP` | 非营业利润/利润总额(%) | number(19,4) | ✓ | 99.25% | 非营业利润/利润总额(%)(NonOProToTP)=（利润总额-营业利润）/利润总额*100%。 |
| 180 | `NonOpeIncToNP` | 营业外收入/净利润(%) | number(19,4) | ✓ | 86.33% | 营业外收入/净利润(%)(NonOpeIncToNP)=营业外收入/净利润*100%。 |
| 181 | `NetNonOperaIncomeToTP` | 营业外收支净额/利润总额(%) | number(19,4) | ✓ | 87.74% | 营业外收支净额/利润总额(%)(NetNonOperaIncomeToTP)=(营业外收入-营业外支出)/利润总额*10... |
| 182 | `TaxesToTP` | 所得税/利润总额(%) | number(19,4) | ✓ | 83.61% | 所得税/利润总额(%)(TaxesToTP)=所得税/利润总额*100%。 |
| 183 | `NonRecurrGLProportion` | 非经常性损益比率(%) | number(19,4) | ✓ | 45.07% | 非经常性损益比率(%)（NonRecurrGLProportion）=非经常性损益/净利润*100%。 |
| 184 | `NPCutToTP` | 扣除非经常损益后的归母净利润/净利润(%) | number(19,4) | ✓ | 52.4% | 扣除非经常损益后的归母净利润/净利润(%)(NPCutToTP)=扣除非经常损益后的归母净利润/净利润*100%。 |
| 185 | `NPCutToNPPC` | 扣除非经常损益后的归母净利润/归属母公司股东的净利润(%) | number(19,4) | ✓ | 52.4% | 扣除非经常损益后的归母净利润/归属母公司股东的净利润(%)(NPCutToNPPC)=扣非后归属于母公司所有者的净利润/... |
| 186 | `NPToTP_DuPont` | 净利润/利润总额(%) | number(19,4) | ✓ | 89.15% | 净利润/利润总额(%)(NPToTP_DuPont)=净利润/利润总额*100%。 |
| 187 | `TPToEBIT_DuPont` | 利润总额/息税前利润(反推)(%) | number(19,4) | ✓ | 85.77% | 利润总额/息税前利润(%)(TPToEBIT_DuPont)=利润总额/息税前利润*100%，“其中，"息税前利润"计算... |
| 188 | `NPPCToNP_DuPont` | 归属母公司股东的净利润/净利润(%) | number(19,4) | ✓ | 99.32% | 归属母公司股东的净利润/净利润(%)(NPPCToNP_DuPont)=归属母公司股东的净利润/净利润*100%。 |
| 189 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 190 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 191 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)：1-合并调整；2-合并未调整

### GrossProfit (毛利(元))

毛利(元)（GrossProfit）＝营业收入－营业成本，金融类公司不计算。

### PeriodExpense (期间费用(元))

期间费用(元)(PeriodExpense)=销售费用+管理费用+研发费用+财务费用。

### TotalCostExpense (成本费用总额(元))

成本费用总额(元)(TotalCostExpense)=营业成本+销售费用+管理费用+研发费用+财务费用，金融类企业不计算。

### NonRecurringProfitLoss (非经常性损益(元))

非经常性损益(元)（NonRecurringProfitLoss）：取定期报告公布值。
若未披露，则：非经常性损益=母公司净利润-扣非净利润。

### NetProfitCut (扣除非经常性损益后的归母净利润(元))

扣除非经常性损益后的归母净利润(元)（NetProfitCut）：取公布值。
若未披露，则：扣除非经常性损益后的净利润=归属于母公司股东的净利润-非经常性损益。

### NetIncomeFromOperating (经营活动净收益(元))

经营活动净收益(元)（NetIncomeFromOperating）：对于非金融类企业，经营活动净收益＝营业总收入－营业总成本（含减值损失）；对于保险及其他金融类企业，经营活动净收益＝营业收入－营业支出（含减值损失）－（投资净收益＋公允价值变动净收益＋汇兑收益+其他收益+资产处置收益）；对于银行及券商类企业，经营活动净收益＝手续费及佣金净收入+利息净收入+其他收入-营业支出（含减值损失）。

### NetIncFromValueChange (价值变动净收益(元))

价值变动净收益(元)(NetIncFromValueChange)=投资净收益+公允价值变动净收益+汇兑收益。

### NetInterestExpense (净利息费用(元))

净利息费用(元)(NetInterestExpense)=利息支出（不含资本化利息）-利息收入，金融类企业不计算。

## SQL示例

```sql
-- 查询 公司财务TTM衍生指标 数据
SELECT *
FROM fin_ttmderivative
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
