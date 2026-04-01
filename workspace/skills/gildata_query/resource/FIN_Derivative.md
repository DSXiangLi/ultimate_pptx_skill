# FIN_Derivative

**中文名**: 公司财务衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FIN_Derivative` |
| MySQL表名 | `fin_derivative` |
| 中文名 | 公司财务衍生指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务衍生指标 |
| 更新频率 | 季更新 |
| 字段数量 | 343 |
| 版本 | 1.02 |

## 表描述

1.内容说明：根据上市企业(含科创板)、发债企业披露的财务数据，基于2018年新会计准则计算的财务指标，反映公司每股指标、资本结构情况以及盈利、偿债、成长、营运、分红、现金流等能力的指标。
2.本表汇总了原有的指标表累计报告期维度指标，且在指标数量和计算公式上进行了迭代更新。
3.本表针对历史数据进行了留痕：若某个报告期存在多次更正，则更正前及历次更正数据均保留。
4.数据范围：1989-12-31至今
5.信息来源：招股说明书、定报、审计报告等
6.数据维度：均展示人民币元

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)：1-合并调整；2-合并未调整 |
| 6 | `WorkingCapital` | 营运资本(元) | number(19,4) | ✓ | 92.56% | 营运资本(元)（WorkingCapital）＝流动资产合计-流动负债合计。 |
| 7 | `NetWorkingCaital` | 净营运资本(元) | number(19,4) | ✓ | 92.46% | 净营运资本(元)（NetWorkingCaital）=流动资产合计－货币资金－无息流动负债；“无息流动负债”计算方法见I... |
| 8 | `NetTangibleAssets` | 有形资产净值(元) | number(19,4) | ✓ | 97.14% | 有形资产净值(元)（NetTangibleAssets）＝归属于母公司的股东权益－(无形资产＋开发支出＋商誉＋长期待摊费... |
| 9 | `InterestFreeCLiability` | 无息流动负债(元) | number(19,4) | ✓ | 92.23% | 无息流动负债(元)(InterestFreeCLiability)=应付票据及应付账款(若为空，则取应付账款+应付票据)... |
| 10 | `InterestFreeNonCL` | 无息非流动负债(元) | number(19,4) | ✓ | 89.32% | 无息非流动负债（InterestFreeNonCL）=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。 |
| 11 | `InterestBearCLiability` | 带息流动负债(元) | number(19,4) | ✓ | 92.42% | 带息流动负债(元)(InterestBearCLiability)=流动负债合计-无息流动负债“其中，"无息流动负债"计... |
| 12 | `InterestBearNonCL` | 带息非流动负债(元) | number(19,4) | ✓ | 89.32% | 带息非流动负债(元)(InterestBearNonCL)=非流动负债合计-无息非流动负债 其中，"无息非流动负债"计算... |
| 13 | `InterestFreeDebt` | 无息负债(元) | number(19,4) | ✓ | 96.91% | 无息负债(元)（InterestFreeDebt）=应付票据及应付账款（应付账款)+应付票据)+预收款项+应付职工薪酬+... |
| 14 | `InterestBearDebt` | 带息债务(元) | number(19,4) | ✓ | 92.81% | 带息债务(元)（InterestBearDebt）=负债合计－无息流动负债－无息非流动负债；“无息流动负债”计算方法见I... |
| 15 | `NetDebt` | 净债务(元) | number(19,4) | ✓ | 92.81% | 净债务(元)（NetDebt）=带息债务－货币资金；“带息债务”计算方法见InterestBearDebt[带息债务]，... |
| 16 | `LongDebt` | 长期债务(元) | number(19,4) | ✓ | 79.74% | 长期债务(元)（LongDebt）=长期借款+应付债券+长期应付款合计（长期应付款+专项应付款）+应付融资租赁款+应付融... |
| 17 | `Curliability` | 短期债务(元) | number(19,4) | ✓ | 87.86% | 短期债务(元)(Curliability)=短期借款+应付票据+交易性金融负债+一年内到期的非流动负债。 |
| 18 | `Entireliability` | 全部债务(元) | number(19,4) | ✓ | 91.79% | 全部债务(元)(Entireliability)=长期债务(LongDebt)+短期债务(Curliability)；计... |
| 19 | `RetainedEarnings` | 留存收益(元) | number(19,4) | ✓ | 96.85% | 留存收益(元)（RetainedEarnings）＝盈余公积＋未分配利润。 |
| 20 | `TotalPaidinCapital` | 全部投入资本(元) | number(19,4) | ✓ | 92.73% | 全部投入资本(元)（TotalPaidinCapital）=所有者权益(或股东权益)总计+带息债务；“带息债务”计算方法... |
| 21 | `TotalShares` | 期末总股本(股)(财务口径) | number(19,4) | ✓ | 98.04% | 期末总股本(股)(TotalShares)：当每股面值货币单位为人民币时，取母公司实收资本/每股面值，若为空，则判断合并... |
| 22 | `PeriodExpense` | 期间费用(元) | number(19,4) | ✓ | 98.27% | 期间费用(元)(PeriodExpense)=销售费用+管理费用+研发费用+财务费用。 |
| 23 | `TotalCostExpense` | 成本费用总额(元) | number(19,4) | ✓ | 93.65% | 成本费用总额(元)(TotalCostExpense)=营业成本+销售费用+管理费用+研发费用+财务费用，金融类企业不计... |
| 24 | `GrossProfit` | 毛利(元) | number(19,4) | ✓ | 93.97% | 毛利(元)(GrossProfit)＝营业收入－营业成本，金融类公司不计算。 |
| 25 | `NetIncomeFromOperating` | 经营活动净收益(元) | number(19,4) | ✓ | 98.23% | 经营活动净收益(元)(NetIncomeFromOperating)：对于非金融类企业，经营活动净收益＝营业总收入－营业... |
| 26 | `NetIncFromValueChange` | 价值变动净收益(元) | number(19,4) | ✓ | 83.47% | 价值变动净收益(元)(NetIncFromValueChange)=投资净收益+公允价值变动净收益+汇兑收益。 |
| 27 | `NetInterestExpense` | 净利息费用(元) | number(19,4) | ✓ | 61.54% | 净利息费用(元)(NetInterestExpense)=利息支出（不含资本化利息）-利息收入，金融类企业不计算。 |
| 28 | `EBIT` | 息税前利润(反推)(元) | number(19,4) | ✓ | 94.19% | 息税前利润(反推)(元)(EBIT)＝利润总额＋利息费用, 其中，利息费用优先取NetInterestExpense[净... |
| 29 | `EBITDA` | 息税折旧摊销前利润(反推)(元) | number(19,4) | ✓ | 60.02% | 息税折旧摊销前利润(反推)(元)(EBITDA)＝息税前利润EBIT+当期计提折旧和摊销，其中，"息税前利润"计算方法详... |
| 30 | `EBIT_Positive` | 息税前利润(正向)(元) | number(19,4) | ✓ | 98.34% | 息税前利润(正向)(元)(EBIT_Positive)：非银行类公司：营业总收入-(营业总成本-财务费用)+(资产减值损... |
| 31 | `EBITDA_Positive` | 息税折旧摊销前利润(正向)(元) | number(19,4) | ✓ | 62.46% | 息税折旧摊销前利润(正向)(元)(EBITDA_Positive)=息税前利润(正向）+当期计提折旧和摊销，其中，"息税... |
| 32 | `EBIAT` | 息前税后利润(反推)(元) | number(19,4) | ✓ | 94.19% | 息前税后利润(反推)(元)(EBIAT)=EBIT*(1-有效税率），其中，当所得税，利润总额均大于0时，有效税率=所得... |
| 33 | `PreFinExpOP` | 扣除财务费用前营业利润(元) | number(19,4) | ✓ | 93.86% | 扣除财务费用前营业利润(元)(PreFinExpOP)=营业利润+财务费用，金融类企业不计算。 |
| 34 | `NonOperatingProfit` | 非营业利润(元) | number(19,4) | ✓ | 98.71% | 非营业利润(元)(NonOperatingProfit)=利润总额-营业利润。 |
| 35 | `NetNonoperating` | 营业外收支净额(元) | number(19,4) | ✓ | 96.82% | 营业外收支净额(元)(NetNonoperating)=营业外收入-营业外支出。 |
| 36 | `NonRecurringProfitLoss` | 非经常性损益(元) | number(19,4) | ✓ | 54.05% | 非经常性损益(元)(NonRecurringProfitLoss)：取定期报告公布值。若未披露，则：非经常性损益=母公司... |
| 37 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(元) | number(19,4) | ✓ | 54.05% | 扣除非经常性损益后的归母净利润(元)(NetProfitCut)：优先展示公布值；若未披露，则计算赋值=归属于母公司股东... |
| 38 | `CurrentAccruedDA` | 当期计提折旧与摊销(元) | number(19,4) | ✓ | 62.52% | 当期计提折旧与摊销(元)(CurrentAccruedDA)=固定资产折旧＋投资性房地产折旧/摊销+无形资产摊销＋长期待... |
| 39 | `EnterpriseFCF` | 企业自由现金流量(元) | number(19,4) | ✓ | 60.02% | 企业自由现金流量(元)(EnterpriseFCF)：息税前利润*(1-有效税率)+当期计提折旧和摊销-期末净营运资本+... |
| 40 | `ShareHolderFCF` | 股权自由现金流量(元) | number(19,4) | ✓ | 60.02% | 股权自由现金流量(元)(ShareHolderFCF)=企业自由现金流量-偿还债务支付的现金+取得借款收到的现金+发行债... |
| 41 | `BasicEPS` | 基本每股收益(披露)(元/股) | number(19,4) | ✓ | 57.42% | 基本每股收益(披露)(元/股)(BasicEPS)：取公布值。 |
| 42 | `DilutedEPS` | 稀释每股收益(披露)(元/股) | number(19,4) | ✓ | 51.31% | 稀释每股收益(披露)(元/股)(DilutedEPS)：取公布值。 |
| 43 | `BasicEPSCut` | 基本每股收益_扣除(元/股) | number(19,4) | ✓ | 32.97% | 基本每股收益_扣除(元/股)(BasicEPSCut)：取公布值。 |
| 44 | `DilutedEPSCut` | 稀释每股收益_扣除(元/股) | number(19,4) | ✓ | 25.2% | 稀释每股收益_扣除(元/股)(DilutedEPSCut)：取公布值。 |
| 45 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(19,4) | ✓ | 97.5% | 每股收益_期末股本摊薄(元/股)(EPS)=归属于母公司普通股股东的净利润（若为空，则取“归属于母公司所有者的净利润”）... |
| 46 | `EPSCut` | 每股收益(扣除)(元/股) | number(19,4) | ✓ | 53.99% | 每股收益(扣除)(元/股)(EPSCut)：每股收益=扣除非经常性损益后普通股股东的净利润(元)(若为空，则取“扣除非经... |
| 47 | `NetAssetPSAdjusted` | 调整后每股净资产(元/股) | number(19,4) | ✓ | 4.36% | 调整后每股净资产(元/股)(NetAssetPSAdjusted)：取公布值。 |
| 48 | `NAPS` | 每股净资产(元/股) | number(19,4) | ✓ | 96.91% | 每股净资产(元/股)(NAPS)=(归属母公司所有者权益(或股东权益)合计-其他权益工具)/期末总股本，其中，"期末总股... |
| 49 | `CapitalSurplusFundPS` | 每股资本公积金(元/股) | number(19,4) | ✓ | 93.68% | 每股资本公积金(元/股)(CapitalSurplusFundPS)=资本公积/期末总股本，其中，"期末总股本"计算方法... |
| 50 | `SurplusReserveFundPS` | 每股盈余公积(元/股) | number(19,4) | ✓ | 91.87% | 每股盈余公积(元/股)(SurplusReserveFundPS)＝盈余公积/期末总股本，其中，"期末总股本"计算方法详... |
| 51 | `AccumulationFundPS` | 每股公积金(元/股) | number(19,4) | ✓ | 96.2% | 每股公积金(元/股)(AccumulationFundPS)＝（资本公积金+盈余公积金）/期末总股本，其中，"期末总股本... |
| 52 | `UndividedProfit` | 每股未分配利润(元/股) | number(19,4) | ✓ | 96.61% | 每股未分配利润(元/股)(UndividedProfit)＝未分配利润/期末总股本，其中，"期末总股本"计算方法详见To... |
| 53 | `RetainedEarningsPS` | 每股留存收益(元/股) | number(19,4) | ✓ | 96.75% | 每股留存收益(元/股)(RetainedEarningsPS)＝（盈余公积+未分配利润）/期末总股本，其中，"期末总股本... |
| 54 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(19,4) | ✓ | 97.57% | 每股营业总收入(元/股)(TotalOperateRevenuePS)=营业总收入/期末总股本，其中，"期末总股本"计算... |
| 55 | `MainIncomePS` | 每股营业收入(元/股) | number(19,4) | ✓ | 97.34% | 每股营业收入(元/股)(MainIncomePS)＝营业收入/该报告期期末总股本，其中，"期末总股本"计算方法详见Tot... |
| 56 | `OperProfitPS` | 每股营业利润(元/股) | number(19,4) | ✓ | 97.4% | 每股营业利润(元/股)(OperProfitPS)＝营业利润/期末总股本，其中，"期末总股本"计算方法详见TotalSh... |
| 57 | `EBITPS` | 每股息税前利润(反推)(元/股) | number(19,4) | ✓ | 92.88% | 每股息税前利润(反推)(元/股)(EBITPS)＝息税前利润/期末总股本；“息税前利润”计算方法见EBIT[息税前利润(... |
| 58 | `EBITDAPS` | 每股息税折旧摊销前利润(反推)(元/股) | number(19,4) | ✓ | 59.81% | 每股息税折旧摊销前利润(反推)(元/股)(EBITDAPS)＝息税折旧摊销前利润(反推)/期末总股本；“息税折旧摊销前利... |
| 59 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 95.74% | 每股经营活动产生的现金流量净额(元/股)（OperCashFlowPS)：经营活动产生的现金流量净额/期末总股本，"期末... |
| 60 | `CashFlowPS` | 每股现金流量净额(元/股) | number(19,4) | ✓ | 95.41% | 每股现金流量净额(元/股)(CashFlowPS)=现金及现金等价物净增加额/期末总股本，"期末总股本"计算方法详见To... |
| 61 | `CashEquivalentPS` | 每股现金及现金等价物余额(元/股) | number(19,4) | ✓ | 88.55% | 每股现金及现金等价物余额(元/股)(CashEquivalentPS)＝现金及现金等价物期末余额/期末总股本，"期末总股... |
| 62 | `EnterpriseFCFPS` | 每股企业自由现金流量(元/股) | number(19,4) | ✓ | 59.81% | 每股企业自由现金流量(元/股)(EnterpriseFCFPS)=企业自由现金流量/期末总股本，其中，"企业自由现金流量... |
| 63 | `ShareHolderFCFPS` | 每股股权自由现金流量(元/股) | number(19,4) | ✓ | 59.81% | 每股股东自由现金流量(元/股)(ShareholderFCFPS)=股权自由现金流量/期末总股本，其中，"股权自由现金流... |
| 64 | `NAPSBasis` | 每股净资产(股本口径)(元/股) | number(19,4) | ✓ | 55.18% | 每股净资产(股本口径)(元/股)(NAPSBasis)=(归属母公司所有者权益(或股东权益)合计-其他权益工具)/总股本... |
| 65 | `EPSBasis` | 每股收益(股本口径)(元/股) | number(19,4) | ✓ | 55.96% | 每股收益(股本口径)(元/股)(EPSBasis)=归属于母公司普通股股东的净利润（若为空，则取“归属于母公司所有者的净... |
| 66 | `OperCashFlowPSBasis` | 每股经营活动产生的现金流量净额(股本口径)(元/股) | number(19,4) | ✓ | 54.98% | 每股经营活动产生的现金流量净额(股本口径)(元/股)(OperCashFlowPSBasis)=经营活动产生的现金流量净... |
| 67 | `CashFlowPSBasis` | 每股现金流量净额(股本口径)(元/股) | number(19,4) | ✓ | 54.84% | 每股现金流量净额(股本口径)(元/股)(CashFlowPSBasis)=现金及现金等价物净增加额/总股本，其中，"总股... |
| 68 | `MainIncomePSBasis` | 每股营业收入(股本口径)(元/股) | number(19,4) | ✓ | 55.8% | 每股营业收入(股本口径)(元/股)(MainIncomePSBasis)=营业收入/总股本，其中，"总股本"取股本表对应... |
| 69 | `WROE` | 净资产收益率_加权(%) | number(19,4) | ✓ | 49.57% | 净资产收益率_加权(%)(WROE)：直取披露值。 |
| 70 | `WROECut` | 净资产收益率_加权,扣除,公布值(%) | number(19,4) | ✓ | 33.73% | 净资产收益率_加权,扣除,公布值(%)(WROECut)：直取披露值。 |
| 71 | `ROEAvg` | 净资产收益率_平均(%) | number(19,4) | ✓ | 96.07% | 净资产收益率_平均(%)(ROEAvg)=归属于母公司所有者的净利润*2/（期初归属母公司所有者权益(或股东权益)合计+... |
| 72 | `ROECutAvg` | 净资产收益率_扣除,平均(%) | number(19,4) | ✓ | 53.05% | 净资产收益率_扣除,平均(%)(ROECutAvg)=扣除非经常性损益后的归母净利润*2/（期初归属母公司所有者权益(或... |
| 73 | `ROE` | 净资产收益率_摊薄(%) | number(19,4) | ✓ | 96.14% | 净资产收益率_摊薄(%)(ROE)=归属于母公司所有者的净利润/期末归属母公司所有者权益(或股东权益)合计*100%。 |
| 74 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(19,4) | ✓ | 54.27% | 净资产收益率_扣除,摊薄(%)(ROECut)=扣除非经常性损益后的归母净利润/该报告期期末归属母公司所有者权益(或股东... |
| 75 | `ROENewIssue` | 净资产收益率_增发条件(%) | number(19,4) | ✓ | 32.28% | 净资产收益率_增发条件(%)(ROENewIssue)：取净资产收益率(加权)、净资产收益率(扣除/加权)中较小的乘以1... |
| 76 | `AnnualizedROE` | 年化净资产收益率(%) | number(19,4) | ✓ | 96.07% | 年化净资产收益率(%)(AnnualizedROE)：根据“年化净资产收益率*N”计算，一季报N=4，二季报N=2，三季... |
| 77 | `ROA_EBIT` | 总资产报酬率(%) | number(19,4) | ✓ | 92.48% | 总资产报酬率(%)(ROA_EBIT)＝息税前利润*2/（期初资产总计+期末资产总计）*100% 其中，“息税前利润”计... |
| 78 | `AnnualizedROAEBIT` | 年化总资产报酬率(%) | number(19,4) | ✓ | 92.48% | 年化总资产报酬率(%)(AnnualizedROAEBIT)：根据“总资产报酬率(ROA_EBIT)*N”计算，一季报N... |
| 79 | `ROA` | 总资产净利率(%) | number(19,4) | ✓ | 97.71% | 总资产净利率(%)(ROA)＝净利润*2/(期末资产总计+期初资产总计)*100%。 |
| 80 | `ROACut` | 总资产净利率_不含少数股东损益(%) | number(19,4) | ✓ | 97.05% | 总资产净利率_不含少数股东损益(%)(ROACut)＝归属于母公司所有者的净利润*2/（期初总资产+期末总资产）*100... |
| 81 | `AnnualizedROA` | 年化总资产净利率(%) | number(19,4) | ✓ | 97.71% | 年化总资产净利率(%)(AnnualizedROA)：根据“总资产净利率(ROA)*N”计算，一季报N=4，二季报N=2... |
| 82 | `ROIC` | 投入资本回报率(%) | number(19,4) | ✓ | 92.24% | 投入资本回报率(%)(ROIC)=息税前利润*（1-有效税率）*2/（期初全部投入资本+期末全部投入资本）*100% 其... |
| 83 | `AnnualizedROIC` | 年化投入资本回报率(%) | number(19,4) | ✓ | 92.24% | 年化投入资本回报率(%)(AnnualizedROIC)： 根据“投入资本回报率(ROIC)*N”计算，一季报N=4，二... |
| 84 | `CapitalReturn` | 资本收益率(%) | number(19,4) | ✓ | 88.56% | 资本收益率(%)(CapitalReturn)=息税前利润（反推）*2/（期末非流动负债合计+期初非流动负债合计+期末所... |
| 85 | `ROCE` | 已动用资本回报率(%) | number(19,4) | ✓ | 91.96% | 已动用资本回报率(%)(ROCE)=息税前利润（反推）*2/（期初全部投入资本＋期末全部投入资本）*100%，其中,"息... |
| 86 | `GrossIncomeRatio` | 销售毛利率(%) | number(19,4) | ✓ | 93.75% | 销售毛利率(%)(GrossIncomeRatio)＝（营业收入-营业成本）/营业收入*100%，金融类企业不计算。 |
| 87 | `NetProfitRatio` | 销售净利率(%) | number(19,4) | ✓ | 98.77% | 销售净利率(%)(NetProfitRatio)＝净利润/营业收入*100%。 |
| 88 | `NetProfitRatioCut` | 扣非后销售净利率(%) | number(19,4) | ✓ | 53.94% | 扣非后销售净利率(%)(NetProfitRatioCut)＝扣除非经常性损益后的归母净利润/营业收入*100%。 |
| 89 | `NetProfitCutToTOR` | 扣除非经常性损益后的归母净利润/营业总收入(%) | number(19,4) | ✓ | 53.96% | 扣除非经常性损益后的归母净利润/营业总收入(%)(NetProfitCutToTOR)＝扣除非经常性损益后的归母净利润/... |
| 90 | `SalesCostRatio` | 销售成本率(%) | number(19,4) | ✓ | 92.8% | 销售成本率(%)(SalesCostRatio)＝营业成本/营业收入*100%，金融类企业不计算。 |
| 91 | `TOperatingCostToTOR` | 营业总成本(含减值损失)/营业总收入(%) | number(19,4) | ✓ | 98.02% | 营业总成本(含减值损失)/营业总收入(%)(TOperatingCostToTOR)=营业总成本(含减值损失）／营业总收... |
| 92 | `TotalProfitCostRatio` | 成本费用利润率(%) | number(19,4) | ✓ | 93.49% | 成本费用利润率(%)(TotalProfitCostRatio)＝利润总额/(营业成本+财务费用+销售费用+管理费用+研... |
| 93 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(19,4) | ✓ | 86.07% | 销售费用/营业总收入(%)( OperatingExpenseRate)=销售费用/营业总收入*100%，金融类企业不计... |
| 94 | `AdminiExpenseRate` | 管理费用/营业总收入(%) | number(19,4) | ✓ | 97.57% | 管理费用/营业总收入(%)(AdminiExpenseRate)=管理费用/营业总收入*100%，金融类企业不计算。 |
| 95 | `FinancialExpenseRate` | 财务费用/营业总收入(%) | number(19,4) | ✓ | 93.03% | 财务费用/营业总收入(%)( FinancialExpenseRate)=财务费用/营业总收入*100%，金融类企业不计... |
| 96 | `RAndDExpenseRate` | 研发费用/营业总收入(%) | number(19,4) | ✓ | 33.33% | 研发费用/营业总收入(%)(RAndDExpenseRate)=研发费用/营业总收入*100%。 |
| 97 | `PeriodCostsRate` | 销售期间费用率(%) | number(19,4) | ✓ | 97.8% | 销售期间费用率(%)(PeriodCostsRate)＝（销售费用+管理费用+财务费用+研发费用）/营业收入*100%。 |
| 98 | `AssetImpaLossToTOR` | 资产减值损失/营业总收入(%) | number(19,4) | ✓ | 71.09% | 资产减值损失/营业总收入(%)(AssetImpaLossToTOR)=资产减值损失/营业总收入*100%。 |
| 99 | `AssetILossToOProfit` | 资产减值损失/营业利润(%) | number(19,4) | ✓ | 60.39% | 资产减值损失/营业利润(%)(AssetILossToOProfit)=资产减值损失/营业利润*100%。 |
| 100 | `TaxRatio` | 销售税金率(%) | number(19,4) | ✓ | 97.12% | 销售税金率(%)(TaxRatio)=营业税金及附加/营业收入*100%。 |
| 101 | `OperatingProfitMargin` | 营业利润率(%) | number(19,4) | ✓ | 98.33% | 营业利润率(%)(OperatingProfitMargin)=营业利润/营业收入*100%。 |
| 102 | `OperatingProfitToTOR` | 营业利润/营业总收入(%) | number(19,4) | ✓ | 98.44% | 营业利润/营业总收入(%)(OperatingProfitToTOR)=营业利润/营业总收入*100%。 |
| 103 | `PreFinExpOPToOR` | 扣除财务费用前营业利润/营业收入(%) | number(19,4) | ✓ | 93.44% | 扣除财务费用前营业利润/营业收入(%)(PreFinExpOPToOR)=扣除融资费用前营业利润/营业收入*100%,金... |
| 104 | `ToProfToOperRevenue` | 利润总额/营业收入(%) | number(19,4) | ✓ | 98.62% | 利润总额/营业收入(%)(ToProfToOperRevenue)=利润总额/营业收入*100%。 |
| 105 | `NPToTOR` | 净利润/营业总收入(%) | number(19,4) | ✓ | 98.88% | 净利润/营业总收入(%)(NPToTOR)：=净利润/营业总收入*100%。 |
| 106 | `NPPCToTOR` | 归属于母公司股东的净利润/营业总收入(%) | number(19,4) | ✓ | 98.27% | 归属于母公司股东的净利润/营业总收入(%)(NPPCToTOR)=归属于母公司所有者的净利润/营业总收入*100%。 |
| 107 | `EBITToTOR` | 息税前利润(反推)/营业总收入(%) | number(19,4) | ✓ | 93.64% | 息税前利润(反推)/营业总收入(%)(EBITToTOR)=息税前利润(反推)/营业总收入*100%，其中，"息税前利润... |
| 108 | `EBITAssetRatio` | 息税前利润(反推)/资产总额(%) | number(19,4) | ✓ | 92.48% | 息税前利润(反推)/资产总额(%)(EBITAssetRatio)=息税前利润(反推/资产总额*100%，其中，"息税前... |
| 109 | `EBITDAToTOR` | 息税折旧摊销前利润(反推)/营业总收入(%) | number(19,4) | ✓ | 59.83% | 息税折旧摊销前利润(反推)/营业总收入(%)(EBITDAToTOR)=息税折旧摊销前利润(反推)/营业总收入*100%... |
| 110 | `CurrentRatio` | 流动比率 | number(19,4) | ✓ | 92.53% | 流动比率(CurrentRatio)＝流动资产合计／流动负债合计。 |
| 111 | `QuickRatio` | 速动比率 | number(19,4) | ✓ | 92.37% | 速动比率(QuickRatio)＝（流动资产合计-存货）／流动负债合计。 |
| 112 | `SuperQuickRatio` | 超速动比率 | number(19,4) | ✓ | 92.41% | 超速动比率(SuperQuickRatio)＝（货币资金+交易性金融资产+应收票据及应收账款（为空，则取应收票据+应收账... |
| 113 | `CashToTL` | 货币资金/全部债务 | number(19,4) | ✓ | 91.6% | 货币资金/全部债务(CashToTL)=货币资金/全部债务，其中，"全部债务"计算方法详见Entireliability... |
| 114 | `CashToCurliability` | 货币资金/短期债务 | number(19,4) | ✓ | 87.65% | 货币资金/短期债务(CashToCurliability)=货币资金/短期债务，其中，"短期债务"计算方法详见A.Cur... |
| 115 | `CashToInteBearCL` | 货币资金/带息流动负债 | number(19,4) | ✓ | 83.79% | 货币资金/带息流动负债(CashToInteBearCL)=货币资金/带息流动负债，金融类企业不计算。 |
| 116 | `CashToCLiability` | 货币资金/流动负债 | number(19,4) | ✓ | 92.24% | 货币资金/流动负债(CashToCLiability)=货币资金/流动负债合计。 |
| 117 | `CashRatio` | 现金比率(%) | number(19,4) | ✓ | 92.25% | 现金比率(%)(CashRatio)＝（货币资金+交易性金融资产+应收票据）/流动负债合计*100%。 |
| 118 | `OperCashInToDueDebt` | 现金到期债务比 | number(19,4) | ✓ | 85.77% | 现金到期债务比(OperCashInToDueDebt)=经营活动产生的现金流量净额／（短期借款+一年内到期的非流动负债... |
| 119 | `TangibAToInteBearDebt` | 有形净值/带息债务(%) | number(19,4) | ✓ | 85.71% | 有形净值/带息债务(%)(TangibAToInteBearDebt)=有形资产净值/带息债务*100%，"带息债务"计... |
| 120 | `TangibleAToNetDebt` | 有形净值/净债务(%) | number(19,4) | ✓ | 61.96% | 有形净值/净债务(TangibleAToNetDebt)＝（有形资产净值／净债务）*100%，其中，"有形资产净值"计算... |
| 121 | `TangibleAToTL` | 有形资产/负债合计(%) | number(19,4) | ✓ | 97.03% | 有形资产/负债合计(%)(TangibleAToTL)=有形资产净值/负债总计*100%，其中，"有形资产净值"计算方法... |
| 122 | `LongDebtToWorkCapital` | 非流动负债/营运资金(%) | number(19,4) | ✓ | 71.45% | 非流动负债/营运资金(%)(LongDebtToWorkCapital)=非流动负债合计/营运资本*100%，其中，"营... |
| 123 | `LongDebtRatio` | 长期债务占比(%) | number(19,4) | ✓ | 79.73% | 长期债务占比(%)(LongDebtRatio)＝长期债务/负债合计*100%，“长期债务”计算方法见LongDebt[... |
| 124 | `NetLiabilityRatio` | 净负债率(%) | number(19,4) | ✓ | 91.96% | 净负债率(%)(NetLiabilityRatio)=（净债务/所有者权益(或股东权益)总计*100%，其中，"净债务"... |
| 125 | `CurliaToTCL` | 短期债务/流动负债(%) | number(19,4) | ✓ | 86.58% | 短期债务/流动负债(%)(CurliaToTCL)=短期债务/流动负债合计*100%。 |
| 126 | `CurliaToEntireliab` | 短期债务/总债务(%) | number(19,4) | ✓ | 87.74% | 短期债务/总债务(%)(CurliaToEntireliab)=短期债务/全部债务*100%，其中，"短期债务"计算方法... |
| 127 | `IntBearDebtToTL` | 带息债务/总负债(%) | number(19,4) | ✓ | 92.8% | 带息债务/总负债(%)(IntBearDebtToTL)=带息债务/负债总计*100%，"带息债务"计算方法详见Inte... |
| 128 | `EntireliabToEBITDA` | 全部债务/息税折旧摊销前利润(反推) | number(19,4) | ✓ | 57.2% | 全部债务/息税折旧前利润(EntireliabToEBITDA)=全部债务/息税折旧前利润，其中,“全部债务”计算方法详... |
| 129 | `SEWithoutMIToTL` | 归属母公司股东的权益/负债合计(%) | number(19,4) | ✓ | 97.03% | 归属母公司股东的权益/负债合计(%)(SEWithoutMIToTL)=归属母公司股东的权益/负债合计*100%。 |
| 130 | `SEWToInterestBearDebt` | 归属母公司股东的权益/带息债务(%) | number(19,4) | ✓ | 85.71% | 归属母公司股东的权益/带息债务(%)(SEWToInterestBearDebt)=归属母公司所有者权益(或股东权益)合... |
| 131 | `InterestCover` | 利息保障倍数(倍) | number(19,4) | ✓ | 74.12% | 利息保障倍数(倍)(InterestCover)＝息税前利润/（利息支出（含资本化利息）-利息收入）。其中，“息税前利润... |
| 132 | `NOCFInterestCover` | 现金流量利息保障倍数(倍) | number(19,4) | ✓ | 73.02% | 现金流量利息保障倍数(倍)(NOCFInterestCover)=经营活动产生现金流量净额/（利息支出（含资本化利息）-... |
| 133 | `RepaymentCover` | 偿债倍数(倍) | number(19,4) | ✓ | 93.54% | 偿债倍数(倍)(RepaymentCover)=息税前利润/(利息+本金偿还/(1-有效税率))，金融企业不计算。 |
| 134 | `OperProfitToCL` | 营业利润/流动负债(%) | number(19,4) | ✓ | 92.06% | 营业利润/流动负债(%)(OperProfitToCL)=营业利润/流动负债合计*100%。 |
| 135 | `OperProfitToTL` | 营业利润/负债合计(%) | number(19,4) | ✓ | 96.9% | 营业利润/负债合计(%)(OperProfitToTL)=营业利润/负债总计*100%。 |
| 136 | `EBITToInteBearDebt` | 息税前利润(反推)/带息债务(%) | number(19,4) | ✓ | 85.66% | 息税前利润(反推)/带息债务(%)(EBITToInteBearDebt)=息税前利润/带息债务*100%，"带息债务"... |
| 137 | `EBITDAToIntBearDebt` | 息税折旧摊销前利润(反推)/带息债务(%) | number(19,4) | ✓ | 55.15% | 息税折旧摊销前利润(反推)/带息债务(%)(EBITDAToIntBearDebt)=息税折旧摊销前利润(反推)/带息债... |
| 138 | `EBITDAToInttFinExp` | 息税折旧摊销前利润(反推)/利息费用 | number(19,4) | ✓ | 47.55% | 息税折旧摊销前利润(反推)/利息费用(EBITDAToInttFinExp)=息税折旧摊销前利润(反推)/（利息支出（含... |
| 139 | `EBITDAToTLiability` | 息税折旧摊销前利润(反推)/负债合计(%) | number(19,4) | ✓ | 59.73% | 息税折旧摊销前利润(反推)/负债合计(%)(EBITDAToTLiability)=息税折旧摊销前利润(反推)/负债总计... |
| 140 | `OperCashToCurrentDebt` | 现金流动负债比 | number(19,4) | ✓ | 90.77% | 现金流动负债比(%)(OperCashToCurrentDebt)=经营活动产生的现金净流入/流动负债合计，金融类企业不... |
| 141 | `OperCashFlowToTL` | 经营活动产生的现金流量净额/负债合计 | number(19,4) | ✓ | 95.23% | 经营活动产生的现金流量净额/负债合计(OperCashFlowToTL)=经营活动产生的现金流量净额/负债总计。 |
| 142 | `NOCFToInterestBearDebt` | 经营活动产生的现金流量净额/带息债务 | number(19,4) | ✓ | 84.68% | 经营活动产生现金流量净额/带息债务(NOCFToInterestBearDebt)=经营活动产生的现金流量净额/带息债务... |
| 143 | `OperCashFlowToCL` | 经营活动产生的现金流量净额/流动负债 | number(19,4) | ✓ | 91.01% | 经营活动产生的现金流量净额/流动负债(OperCashFlowToCL)=经营活动产生的现金流量净额/流动负债合计。 |
| 144 | `NOCFToNetDebt` | 经营活动产生的现金流量净额/净债务 | number(19,4) | ✓ | 61.17% | 经营活动产生现金流量净额/净债务(NOCFToNetDebt)=经营活动产生的现金流量净额/净债务，其中，"净债务"计算... |
| 145 | `NOCFToTotalNonCurLia` | 经营活动产生的现金流量净额/非流动负债 | number(19,4) | ✓ | 86.81% | 经营活动产生现金流量净额/非流动负债(%)(NOCFToTotalNonCurLia)=经营活动产生现金流量净额/非流动... |
| 146 | `NetNoFCFToCLiability` | 非筹资性现金净流量与流动负债的比率 | number(19,4) | ✓ | 91.02% | 非筹资性现金净流量与流动负债的比率(NetNoFCFToCLiability)=（经营活动产生的现金流量净额+投资活动产... |
| 147 | `NetNoFCFToTLiability` | 非筹资性现金净流量与负债总额的比率 | number(19,4) | ✓ | 95.25% | 非筹资性现金净流量与负债总额的比率(NetNoFCFToTLiability)=（经营活动产生的现金流量净额+投资活动产... |
| 148 | `BasicEPSYOY` | 基本每股收益同比增长率(%) | number(19,4) | ✓ | 52.61% | 基本每股收益同比增长率(%)(BasicEPSYOY)=（本期基本每股收益-上年同期基本每股收益）/ABS(上年同期基本... |
| 149 | `BasicEPSGrowRate3Y` | 基本每股收益3年复合增长率(%) | number(19,4) | ✓ | 44.48% | 基本每股收益3年复合增长率(%)(BasicEPSGrowRate3Y)：当三年前同期基本每股收益为正数时，基本每股收益... |
| 150 | `DilutedEPSYOY` | 稀释每股收益同比增长率(%) | number(19,4) | ✓ | 48.28% | 稀释每股收益同比增长率(%)(DilutedEPSYOY)=（本期稀释每股收益-上年同期稀释每股收益）/ABS(上年同期... |
| 151 | `DilutedEPSGrowRate3Y` | 稀释每股收益3年复合增长率(%) | number(19,4) | ✓ | 39.93% | 稀释每股收益3年复合增长率(%)(DilutedEPSGrowRate3Y)：当三年前同期稀释每股收益为正数时，稀释每股... |
| 152 | `EPSYOY` | 每股收益同比增长率(%) | number(19,4) | ✓ | 90.66% | 每股收益同比增长率(%)(EPSYOY)=（本期每股收益-上年同期每股收益）/ABS(上年同期每股收益)*100%，如果... |
| 153 | `EPSGrowRate3Y` | 每股收益3年复合增长率(%) | number(19,4) | ✓ | 76.01% | 每股收益3年复合增长率(%)(EPSGrowRate3Y)：当三年前同期每股收益为正数时，每股收益3年复合增长率=[（本... |
| 154 | `EPSCutYOY` | 每股收益(扣除)同比增长率(%) | number(19,4) | ✓ | 49.25% | 每股收益(扣除)同比增长率(%)(EPSCutYOY)=(本期每股收益(扣除)-上年同期每股收益(扣除))/ABS(上年... |
| 155 | `NAPSGrowRate` | 每股净资产同比增长率(%) | number(19,4) | ✓ | 89.38% | 每股净资产同比增长率(%)(NAPSGrowRate)=(本期每股净资产-上年同期每股净资产)/ABS(上年同期每股净资... |
| 156 | `NAPSGrowRateYTD` | 每股净资产相对年初增长率(%) | number(19,4) | ✓ | 94.92% | 每股净资产相对年初增长率(%)(NAPSGrowRateYTD)=(本期每股净资产-期初每股净资产)/ABS(期初数每股... |
| 157 | `NAPSGrowRate3Y` | 每股净资产3年复合增长率(%) | number(19,4) | ✓ | 74.92% | 每股净资产3年复合增长率(%)(NAPSGrowRate3Y)：当三年前同期每股净资产为正数时，每股净资产3年复合增长率... |
| 158 | `OperCashPSGrowRate` | 每股经营活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 88.74% | 每股经营活动产生的现金流量净额同比增长率(%)(OperCashPSGrowRate)=（本期每股经营活动产生的现金流量... |
| 159 | `OperCashPSGrowRate3Y` | 每股经营活动产生的现金流量净额3年复合增长率(%) | number(19,4) | ✓ | 74.04% | 每股经营活动产生的现金流量净额3年复合增长率(%)(OperCashPSGrowRate3Y)：当三年前同期每股经营活动... |
| 160 | `CashEquivalGrowRate` | 货币资金同比增长率(%) | number(19,4) | ✓ | 89.32% | 货币资金增长率(%)(CashEquivalGrowRate)=（本期货币资金-上年同期货币资金）/ABS(上年同期货币... |
| 161 | `ARGrowRate` | 应收账款同比增长率(%) | number(19,4) | ✓ | 80.81% | 应收账款同比增长率(%)(ARGrowRate)=(本期应收账款-上年同期应收账款)/ABS(上年同期应收账款)*100... |
| 162 | `ReceivablesGrowRate` | 应收类款项同比增长率(%) | number(19,4) | ✓ | 87.26% | 应收类款项同比增长率(%)(ReceivablesGrowRate)=（本期应收类款项-上年同期应收类款项）/ABS(上... |
| 163 | `InventoryGrowRate` | 存货同比增长率(%) | number(19,4) | ✓ | 82.56% | 存货同比增长率(%)(InventoryGrowRate)=(本期存货-上年同期存货)/ABS(上年同期存货)*100%... |
| 164 | `CurAssetsGrowRate` | 流动资产合计同比增长率(%) | number(19,4) | ✓ | 85.42% | 流动资产合计同比增长率(%)(CurAssetsGrowRate)=(本期流动资产合计-上年同期流动资产合计)/NULL... |
| 165 | `DeferredExpGrowRate` | 长期待摊费用同比增长率(%) | number(19,4) | ✓ | 65.62% | 长期待摊费用同比增长率(%)(DeferredExpGrowRate)=(本期长期待摊费用-上年同期长期待摊费用)/NU... |
| 166 | `FAExpansionRate` | 固定资产投资扩张率(%) | number(19,4) | ✓ | 89.2% | 固定资产投资扩张率(%)(FAExpansionRate)=（本期固定资产（若无数据，取固定资产合计)-上年同期固定资产... |
| 167 | `NonCurAssetsGrowRate` | 非流动资产合计同比增长率(%) | number(19,4) | ✓ | 85.25% | 非流动资产合计同比增长率(%)(NonCurAssetsGrowRate)=(本期非流动资产合计-上年同期非流动资产合计... |
| 168 | `TotalAssetGrowRate` | 总资产同比增长率(%) | number(19,4) | ✓ | 90.41% | 总资产同比增长率(%)(TotalAssetGrowRate)=（本期总资产-上年同期总资产）/ABS(上年同期总资产)... |
| 169 | `TAGrowRateYTD` | 资产总计相对年初增长率(%) | number(19,4) | ✓ | 96.07% | 资产总计相对年初增长率(%)(TAGrowRateYTD)=（本期末资产总计-期初资产总计）/ABS(期初资产总计)*1... |
| 170 | `TotalAssetGrowRate3Y` | 总资产3年复合增长率(%) | number(19,4) | ✓ | 75.9% | 总资产3年复合增长率(%)(TotalAssetGrowRate3Y)：当三年前同期总资产为正数时，总资产3年复合增长率... |
| 171 | `CurrentLiaGrowRate` | 流动负债合计同比增长率(%) | number(19,4) | ✓ | 85.38% | 流动负债合计同比增长率(%)(CurrentLiaGrowRate)=(本期流动负债合计-上年同期流动负债合计)/ABS... |
| 172 | `NonCurrentLiaGrowRate` | 非流动负债合计同比增长率(%) | number(19,4) | ✓ | 80.23% | 非流动负债合计同比增长率(%)(NonCurrentLiaGrowRate)=(本期非流动负债合计-上年同期非流动负债合... |
| 173 | `InteBearDebtGrowRate` | 带息债务同比增长率(%) | number(19,4) | ✓ | 79.05% | 带息债务同比增长率(%)(InteBearDebtGrowRate)=(本期带息债务-上年同期带息债务)/ABS(上年同... |
| 174 | `InteBearDebtGrowRate3Y` | 带息债务3年复合增长率(%) | number(19,4) | ✓ | 65.62% | 带息债务3年复合增长率(%)(InteBearDebtGrowRate3Y):当三年前同期带息债务为正数时，带息债务3年... |
| 175 | `ToLiabGrowRate` | 总负债同比增长率(%) | number(19,4) | ✓ | 90.17% | 总负债同比增长率(%)(ToLiabGrowRate)=（本期总负债-上年同期总负债）/ABS(上年同期总负债)*100... |
| 176 | `ToLiabGrowRate3Y` | 总负债3年复合增长率(%) | number(19,4) | ✓ | 75.68% | 总负债3年复合增长率(%)(ToLiabGrowRate3Y):当三年前同期总负债为正数时，总负债3年复合增长率=[（本... |
| 177 | `NetAssetGrowRate` | 所有者权益(或股东权益)同比增长率(%) | number(19,4) | ✓ | 90.2% | 所有者权益(或股东权益)同比增长率(%)(NetAssetGrowRate)=（本期所有者权益(或股东权益)-上年同期所... |
| 178 | `NetAssetGrowRate3Y` | 所有者权益(或股东权益)3年复合增长率(%) | number(19,4) | ✓ | 75.71% | 所有者权益(或股东权益)3年复合增长率(%)(NetAssetGrowRate3Y)：当三年前同期所有者权益(或股东权益... |
| 179 | `SEWithoutMIGrowRate` | 归属母公司所有者权益(或股东权益)同比增长率(%) | number(19,4) | ✓ | 89.6% | 归属母公司所有者权益(或股东权益)同比增长率(%)(SEWithoutMIGrowRate)=(本期归属母公司所有者权益... |
| 180 | `SEWithoutMIGrowRate3Y` | 归属母公司股东的权益3年复合增长率(%) | number(19,4) | ✓ | 75.19% | 归属母公司股东的权益3年复合增长率(%)(SEWithoutMIGrowRate3Y):当三年前同期归属母公司股东的权益... |
| 181 | `SEWithoutMIGrowRateYTD` | 归属母公司股东的权益相对年初增长率(%) | number(19,4) | ✓ | 95.16% | 归属母公司股东的权益相对年初增长率(%)(SEWithoutMIGrowRateYTD)=（本期归属母公司股东的权益-期... |
| 182 | `EquityGrowRate` | 资本保值增值率(%) | number(19,4) | ✓ | 95.88% | 资本保值增值率(%)(EquityGrowRate)=期末所有者权益（或股东权益）总计/期初所有者权益或股东权益）总计*... |
| 183 | `MinoritySEGrowRate` | 少数股东权益同比增长率(%) | number(19,4) | ✓ | 65.82% | 少数股东权益同比增长率(%)(MinoritySEGrowRate)=(本期少数股东权益-上年同期少数股东权益)/ABS... |
| 184 | `CapitalStockGrowth` | 股本同比增长数(元) | number(19,4) | ✓ | 89.38% | 股本同比增长数(元)(CapitalStockGrowth)=本期实收资本(或股本)-上年同期实收资本(或股本)。 |
| 185 | `TORGrowRate` | 营业总收入同比增长率(%) | number(19,4) | ✓ | 92.91% | 营业总收入同比增长率(%)(TORGrowRate)=（本期营业总收入-上年同期营业总收入）/ABS(上年同期营业总收入... |
| 186 | `TORGrowRate3Y` | 营业总收入3年复合增长率(%) | number(19,4) | ✓ | 77.87% | 营业总收入3年复合增长率(%)(TORGrowRate3Y)：当三年前同期营业总收入为正数时，营业总收入3年复合增长率=... |
| 187 | `OperatingRevenueYOY` | 营业收入同比增长率(%) | number(19,4) | ✓ | 92.78% | 营业收入同比增长率(%)(OperatingRevenueYOY)=(本期营业收入-上年同期营业收入)/ABS(上年同期... |
| 188 | `ORComGrowRate3Y` | 营业收入3年复合增长率(%) | number(19,4) | ✓ | 77.75% | 营业收入3年复合增长率(%)(ORComGrowRate3Y)：当三年前同期营业收入为正数时，营业收入3年复合增长率=[... |
| 189 | `OperatingCostGrowRate` | 营业成本同比增长率(%) | number(19,4) | ✓ | 87.28% | 营业成本同比增长率(%)(OperatingCostGrowRate)=(本期营业成本-上年同期营业成本)/ABS(上年... |
| 190 | `ToOpCostGrowRate` | 营业总成本同比增长率(%) | number(19,4) | ✓ | 92.43% | 营业总成本同比增长(%)(ToOpCostGrowRate)=（本期营业总成本-上年同期营业总成本）/ABS(上年同期营... |
| 191 | `RAndDExpenseGrowRate` | 研发费用同比增长率(%) | number(19,4) | ✓ | 29.75% | 研发费用同比增长率(%)(RAndDExpenseGrowRate)=(本期研发费用-上年同期研发费用)/ABS(上年同... |
| 192 | `GrossProfitGrowRate` | 毛利同比增长率(%) | number(19,4) | ✓ | 88.1% | 毛利同比增长率(%)(GrossProfitGrowRate)=(本期毛利-上年同期毛利)/ABS(上年同期毛利)*10... |
| 193 | `GrossProfitGrowRate3Y` | 毛利3年复合增长率(%) | number(19,4) | ✓ | 73.94% | 毛利3年复合增长率(%)(GrossProfitGrowRate3Y)：当三年前同期毛利为正数时，毛利3年复合增长率=[... |
| 194 | `OperProfitGrowRate` | 营业利润同比增长率(%) | number(19,4) | ✓ | 92.78% | 营业利润同比增长率(%)(OperProfitGrowRate)=（本期营业利润-上年同期营业利润）/ABS(上年同期营... |
| 195 | `OperProfitGrowRate3Y` | 营业利润3年复合增长率(%) | number(19,4) | ✓ | 77.73% | 营业利润3年复合增长率(%)(OperProfitGrowRate3Y)：当三年前同期营业利润为正数时，营业利润3年复合... |
| 196 | `TotalProfitGrowRate` | 利润总额同比增长率(%) | number(19,4) | ✓ | 93.23% | 利润总额同比增长率(%)(TotalProfitGrowRate)=(本期利润总额-上年同期利润总额)/ABS(上年同期... |
| 197 | `TPGrowRate3Y` | 利润总额3年复合增长率(%) | number(19,4) | ✓ | 78.2% | 利润总额3年复合增长率(%)(TPGrowRate3Y)：当三年前同期利润总额为正数时，利润总额3年复合增长率=[（本期... |
| 198 | `NetProfitYOY` | 净利润同比增长率(%) | number(19,4) | ✓ | 93.38% | 净利润同比增长率(%)(NetProfitYOY)=(本期净利润-上年同期净利润)/ABS(上年同期净利润)*100%，... |
| 199 | `NetProfitGrowRate3Y` | 净利润3年复合增长率(%) | number(19,4) | ✓ | 78.31% | 净利润3年复合增长率(%)(NetProfitGrowRate3Y)：当三年前同期净利润为正数时，净利润3年复合增长率=... |
| 200 | `NPParentCompanyYOY` | 归属母公司股东的净利润同比增长(%) | number(19,4) | ✓ | 92.9% | 归属母公司股东的净利润同比增长(%)(NPParentCompanyYOY)=（本期归属母公司股东的净利润-上年同期归属... |
| 201 | `NPPCCGrowRate3Y` | 归属母公司股东的净利润3年复合增长率(%) | number(19,4) | ✓ | 77.89% | 归属母公司股东的净利润3年复合增长率(%)(NPPCCGrowRate3Y)：当三年前同期归属母公司股东的净利润为正数时... |
| 202 | `AvgNPYOYPastFiveYear` | 过去五年同期归属母公司净利润平均增幅(%) | number(19,4) | ✓ | 54.29% | 过去五年同期归属母公司净利润平均增幅（AvgNPYOYPastFiveYear）：该报告期过去五年的同期的归属母公司净利... |
| 203 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长率(%) | number(19,4) | ✓ | 49.43% | 归属母公司股东的净利润(扣除)同比增长(%)(NPParentCompanyCutYOY)：优先取原文披露值,若原文未披... |
| 204 | `NPParentCompanyCut3Y` | 归属母公司股东的净利润(扣除)3年复合增长率(%) | number(19,4) | ✓ | 41.48% | 归属母公司股东的净利润(扣除)3年复合增长率(%)(NPParentCompanyCut3Y)：当三年前同期扣除非经常性... |
| 205 | `SaleSerRenderCashYOY` | 销售商品、提供劳务收到的现金同比增长率(%) | number(19,4) | ✓ | 86.24% | 销售商品、提供劳务收到的现金同比增长率(%)(SaleSerRenderCashYOY)=(本期销售商品、提供劳务收到的... |
| 206 | `GoodsSerCashPaidYOY` | 购买商品、接受劳务支付的现金同比增长率(%) | number(19,4) | ✓ | 85.86% | 购买商品、接受劳务支付的现金同比增长率(%)(GoodsSerCashPaidYOY)=(本期购买商品、接受劳务支付的现... |
| 207 | `StaffBehalfPaidYOY` | 支付给职工以及为职工支付的现金同比增长率(%) | number(19,4) | ✓ | 89.73% | 支付给职工以及为职工支付的现金同比增长率(%)(StaffBehalfPaidYOY)=(本期支付给职工以及为职工支付的... |
| 208 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 90.7% | 经营活动产生的现金流量净额同比增长率(%)(NetOperateCashFlowYOY)=（本期经营活动产生的现金流量净... |
| 209 | `NetOperateCashFlow3Y` | 经营活动产生的现金流量净额3年复合增长率(%) | number(19,4) | ✓ | 75.72% | 经营活动产生的现金流量净额3年复合增长率(%)(NetOperateCashFlow3Y)：当三年前同期经营活动产生的现... |
| 210 | `InvestCashGrowRate` | 投资活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 89.78% | 投资活动产生的现金流量净额同比增长率(%)(InvestCashGrowRate)=（本期投资活动产生的现金流量净额-上... |
| 211 | `FinancingCashGrowRate` | 筹资活动产生的现金流量净额同比增长率(%) | number(19,4) | ✓ | 87.93% | 筹资活动产生的现金流量净额同比增长率(%)(FinancingCashGrowRate) =（本期筹资活动产生的现金流量... |
| 212 | `CashEqIncreaseYOY` | 现金净流量同比增长率(%) | number(19,4) | ✓ | 90.42% | 现金净流量同比增长率(%)(CashEqIncreaseYOY)=（本期现金及现金等价物净增加额-上年同期现金及现金等价... |
| 213 | `CashEquivtYOY` | 现金及现金等价物同比增长率(%) | number(19,4) | ✓ | 83.9% | 现金及现金等价物同比增长率(%)(CashEquivtYOY)=(本期现金及现金等价物-上年同期现金及现金等价物)/AB... |
| 214 | `NAORYOY` | 净资产收益率(摊薄)同比增长率(%) | number(19,4) | ✓ | 88.47% | 净资产收益率(摊薄)同比增长(%)(NAORYOY)=（本期净资产收益率(摊薄)-上年同期净资产收益率(摊薄)）/ABS... |
| 215 | `NAORGrowRate3Y` | 净资产收益率(摊薄)3年复合增长率(%) | number(19,4) | ✓ | 74.03% | 净资产收益率(摊薄)3年复合增长率(%)(NAORGrowRate3Y)：当三年前同期净资产收益率(摊薄)为正数时，净资... |
| 216 | `GrossIncomeRatioYOY` | 毛利率同比增长率(%) | number(19,4) | ✓ | 87.99% | 毛利率同比增长率(%)(GrossIncomeRatioYOY)=(本期毛利率-上年同期毛利率)/ABS(上年同期毛利率... |
| 217 | `NetProfitRatioYOY` | 销售净利率同比增长率(%) | number(19,4) | ✓ | 92.59% | 销售净利率同比增长率(%)(NetProfitRatioYOY)=(本期销售净利率-上年同期销售净利率)/ABS(上年同... |
| 218 | `PeriodCostsRateYOY` | 销售期间费用率同比增长率(%) | number(19,4) | ✓ | 91.85% | 销售期间费用率同比增长率(%)(PeriodCostsRateYOY)=(本期销售期间费用率-上年同期销售期间费用率)/... |
| 219 | `NetProfitCashCoverYOY` | 净利润现金含量同比增长率(%) | number(19,4) | ✓ | 74.54% | 净利润现金含量同比增长率(%)(NetProfitCashCoverYOY)=(本期净利润现金含量-上年同期净利润现金含... |
| 220 | `ARTRGrowRate` | 应收账款周转率增长率(%) | number(19,4) | ✓ | 80.23% | 应收账款周转率增长率(%)(ARTRGrowRate)：（本期应收账款周转率-上年同期应收账款周转率）/ABS(上年同期... |
| 221 | `BillARTRGrowRate` | 应收票据及应收账款周转率同比增长率(%) | number(19,4) | ✓ | 82.25% | 应收票据及应收账款周转率同比增长率(%)(BillARTRGrowRate)=(本期应收票据及应收账款周转率-上年同期应... |
| 222 | `InventoryTRGrowRate` | 存货周转率增长率(%) | number(19,4) | ✓ | 81.9% | 存货周转率增长率(%)(InventoryTRGrowRate)：（本期存货周转率-上年同期存货周转率）/ABS(上年同... |
| 223 | `FATRGrowRate` | 固定资产周转率增长率(%) | number(19,4) | ✓ | 88.57% | 固定资产周转率增长率(%)(FATRGrowRate)：（本期固定资产周转率-上年同期固定资产周转率）/ABS(上年同期... |
| 224 | `SustainableGrowRate` | 可持续增长率(%) | number(19,4) | ✓ | 95.54% | 可持续增长率(SustainableGrowRate)＝（本期净利润/期初归属母公司所有者权益(或股东权益)合计）*本期... |
| 225 | `OperCycle` | 营业周期(天/次) | number(19,4) | ✓ | 90.82% | 营业周期(天/次)(OperCycle)＝存货周转天数+应收票据及应收账款周转天数，金融类企业不计算。 |
| 226 | `NetOperCycle` | 净营业周期(天/次) | number(19,4) | ✓ | 91.07% | 净营业周期(天/次)(NetOperCycle)=存货周转天数+应收票据及应收账款周转天数-应付票据及应付账款周转天数，... |
| 227 | `InventoryTRate` | 存货周转率(次) | number(19,4) | ✓ | 88.8% | 存货周转率(次)(InventoryTRate)＝本期营业成本*2/（期初存货+期末存货），金融类企业不计算。 |
| 228 | `InventoryTDays` | 存货周转天数(天/次) | number(19,4) | ✓ | 88.8% | 存货周转天数(天/次)(InventoryTDays)=N/存货周转率，其中：一季报，N=90；中报，N=180；三季报... |
| 229 | `ARTRate` | 应收账款周转率(次) | number(19,4) | ✓ | 87.96% | 应收账款周转率(次)(ARTRate)＝营业收入*2/（期初应收账款+期末应收账款），金融类企业不计算。 |
| 230 | `ARTDays` | 应收账款周转天数(天/次) | number(19,4) | ✓ | 87.96% | 应收账款周转天数(天/次)(ARTDays)＝N/应收账款周转率，其中：一季报，N=90；中报，N=180；三季报，N=... |
| 231 | `BillARTRate` | 应收票据及应收账款周转率(次) | number(19,4) | ✓ | 89.57% | 应收票据及应收账款周转率(次)(BillARTRate)=营业收入*2/(期末应收票据及应收账款+期初应收票据及应收账款... |
| 232 | `BillARTDays` | 应收票据及应收账款周转天数(天/次) | number(19,4) | ✓ | 89.57% | 应收票据及应收账款周转天数(天/次)(BillARTDays)：N/应收票据及应收账款周转率 N:一季报N=90；中报N... |
| 233 | `ContraAssetTRate` | 合同资产周转率(次) | number(19,4) | ✓ | 11.44% | 合同资产周转率(次)(ContraAssetTRate)=本期营业收入*2/（期末合同资产+期初合同资产），金融类企业不... |
| 234 | `ContraAssetTDays` | 合同资产周转天数(天/次) | number(19,4) | ✓ | 11.44% | 合同资产周转天数(天/次)(ContraAssetTDays)：N/合同资产周转率N:一季报N=90；中报N=180；三... |
| 235 | `AdvPayTRate` | 预付账款周转率(次) | number(19,4) | ✓ | 89.39% | 预付账款周转率(次)(AdvPayTRate)=本期营业成本*2/（期末预付款项+期初预付款项），金融类企业不计算。 |
| 236 | `AdvPayTDays` | 预付账款周转天数(天/次) | number(19,4) | ✓ | 89.39% | 预付账款周转天数(天/次)(AdvPayTDays)：N/预收账款周转率 N:一季报N=90；中报N=180；三季报N=... |
| 237 | `CurrentTRate` | 流动资产周转率(次) | number(19,4) | ✓ | 91.75% | 流动资产周转率(次)(CurrentTRate)=本期营业总收入*2/（期末流动资产合计+期初流动资产合计），金融类企业... |
| 238 | `CurrentTDays` | 流动资产周转天数 | number(19,4) | ✓ | 91.75% | 流动资产周转天数(CurrentTDays)：N/流动资产周转率 N:一季报N=90；中报N=180；三季报N=270；... |
| 239 | `FixedAssetTRate` | 固定资产周转率(次) | number(19,4) | ✓ | 96.06% | 固定资产周转率(次)(FixedAssetTRate)＝营业总收入*2/(期初固定资产+期末固定资产)。 |
| 240 | `TotalFixedATRate` | 固定资产合计周转率(次) | number(19,4) | ✓ | 96.11% | 固定资产合计周转率(次)(TotalFixedATRate)=2*营业总收入/(期末固定资产合计+期初固定资产合计)，其... |
| 241 | `FixedAssetTDays` | 固定资产周转天数(天/次) | number(19,4) | ✓ | 96.06% | 固定资产周转天数(天/次)(FixedAssetTDays)：N/固定资产周转率 N:一季报N=90；中报N=180；三... |
| 242 | `TotalFixedATDays` | 固定资产合计周转天数(天/次) | number(19,4) | ✓ | 96.11% | 固定资产合计周转天数(天/次)(TotalFixedATDays)：N/固定资产合计周转率 N:一季报N=90；中报N=... |
| 243 | `IntangibleATRate` | 无形资产周转率(次) | number(19,4) | ✓ | 87.3% | 无形资产周转率(次)(IntangibleATRate)=营业总收入*2/(期初无形资产+期末无形资产），金融类企业不计... |
| 244 | `IntangibleATDays` | 无形资产周转天数(天/次) | number(19,4) | ✓ | 87.3% | 无形资产周转天数(天/次)(IntangibleATDays)：N/无形资产周转率  N:一季报N=90；中报N=180... |
| 245 | `NonCurrentATRate` | 非流动资产周转率(次) | number(19,4) | ✓ | 91.66% | 非流动资产周转率(次)(NonCurrentATRate)=本期营业总收入*2/（期初非流动资产合计+期末非流动资产合计... |
| 246 | `NonCurrentATDays` | 非流动资产周转天数 | number(19,4) | ✓ | 91.66% | 非流动资产周转天数(NonCurrentATDays)：N/非流动资产周转率 N:一季报N=90；中报N=180；三季报... |
| 247 | `TotalAssetTRate` | 总资产周转率(次) | number(19,4) | ✓ | 97.26% | 总资产周转率(次)(TotalAssetTRate)＝营业总收入*2/（期初资产总计+期末资产总计）。 |
| 248 | `TotalAssetTDays` | 总资产周转天数(天/次) | number(19,4) | ✓ | 97.26% | 总资产周转天数(天/次)(TotalAssetTDays)：N/总资产周转率 N:一季报N=90；中报N=180；三季报... |
| 249 | `AccountsPayablesTRate` | 应付账款周转率(次) | number(19,4) | ✓ | 87.3% | 应付账款周转率(次)(AccountsPayablesTRate)＝营业成本*2/（期初应付账款+期末应付账款），金融类... |
| 250 | `AccountsPayablesTDays` | 应付账款周转天数(天/次) | number(19,4) | ✓ | 87.3% | 应付账款周转天数(天/次)(AccountsPayablesTDays)=N/应付账款周转率其中：一季报，N=90；中报... |
| 251 | `NotAccPayableTRate` | 应付票据及应付账款周转率(次) | number(19,4) | ✓ | 90.11% | 应付票据及应付账款周转率(次)(NotAccPayableTRate)=本期营业成本*2/（期末应付票据及应付账款+期初... |
| 252 | `NotAccPayableTDays` | 应付票据及应付账款周转天数(天/次) | number(19,4) | ✓ | 90.11% | 应付票据及应付账款周转天数(天/次)(NotAccPayableTDays)：N/应付票据及应付账款周转率 N:一季报N... |
| 253 | `ConLiabTRate` | 合同负债周转率(次) | number(19,4) | ✓ | 31.06% | 合同负债周转率(次)(ConLiabTRate)=本期营业收入*2/（期末合同负债+期初合同负债），金融类企业不计算。 |
| 254 | `ConLiabTDays` | 合同负债周转天数(天/次) | number(19,4) | ✓ | 31.06% | 合同负债周转天数(天/次)(ConLiabTDays)：N/合同负债周转率 N:一季报N=90；中报N=180；三季报N... |
| 255 | `AdvanceReceTRate` | 预收账款周转率(次) | number(19,4) | ✓ | 70.22% | 预收账款周转率(次)(AdvanceReceTRate)=本期营业收入*2/（期末预收款项+期初预收款项），金融类企业不... |
| 256 | `AdvanceReceTDays` | 预收账款周转天数(天/次) | number(19,4) | ✓ | 70.22% | 预收账款周转天数(天/次)(AdvanceReceTDays)：N/预收账款周转率N:一季报N=90；中报N=180；三... |
| 257 | `CurLiaTRate` | 流动负债周转率(次) | number(19,4) | ✓ | 91.71% | 流动负债周转率(次)(CurLiaTRate)=本期营业总收入*2/（期末流动负债合计+期初流动负债合计），金融类企业不... |
| 258 | `NonCurLiaTRate` | 非流动负债周转率(次) | number(19,4) | ✓ | 87.68% | 非流动负债周转率(次)(NonCurLiaTRate)=本期营业总收入*2/（期末非流动负债合计+期初非流动负债合计），... |
| 259 | `EquityTRate` | 归母股东权益周转率(次) | number(19,4) | ✓ | 95.66% | 归母股东权益周转率(次)(EquityTRate)＝本期营业总收入*2/(期初归属母公司所有者权益(或股东权益)合计+期... |
| 260 | `EquityTDays` | 归母股东权益周转天数(天/次) | number(19,4) | ✓ | 95.66% | 归母股东权益周转天数(天/次)(EquityTDays)：N/股东权益周转率 N:一季报N=90；中报N=180；三季报... |
| 261 | `WorkingCaitalTRate` | 营运资本周转率(次) | number(19,4) | ✓ | 73.63% | 营运资本周转率(次)(WorkingCaitalTRate)=本期营业总收入*2/（期初营运资本+期末营运资本），其中，... |
| 262 | `WorkingCapitalTurDays` | 营运资金周转天数(天/次) | number(19,4) | ✓ | 91.33% | 营运资金周转天数(天/次)(WorkingCapitalTurDays)=存货周转天数+应收票据及应收帐款周转天数+合同... |
| 263 | `NetOperCFToAssetsAvg` | 总资产现金回收率_平均(%) | number(19,4) | ✓ | 95.33% | 总资产现金回收率_平均(%)(NetOperCFToAssetsAvg)=经营活动产生的现金流量净额*2/(期末资产总计... |
| 264 | `NetOperCFToToAssets` | 全部资产现金回收率(%) | number(19,4) | ✓ | 95.32% | 全部资产现金回收率(%)(NetOperCFToToAssets)=经营活动产生的现金流量净额/总资产*100%。 |
| 265 | `OperatingReveCashCover` | 营业收入现金含量(%) | number(19,4) | ✓ | 91.89% | 营业收入现金含量(%)(OperatingReveCashCover)=销售商品提供劳务收到的现金/营业收入*100%。 |
| 266 | `NetProfitCashCover` | 净利润现金含量(%) | number(19,4) | ✓ | 84.3% | 净利润现金含量(%)(NetProfitCashCover)＝经营活动产生的现金流量净额/净利润*100%。 |
| 267 | `NOCFToNPPC` | 经营活动产生的现金流量净额/归属于母公司股东的净利润(%) | number(19,4) | ✓ | 83.47% | 经营活动产生的现金流量净额/归属于母公司股东的净利润(%)(NOCFToNPPC)＝经营活动产生的现金流量净额/归属于母... |
| 268 | `CapitalExpenditureToDM` | 资本支出/折旧和摊销 | number(19,4) | ✓ | 61.76% | 资本支出/折旧和摊销(CapitalExpenditureToDM)=购建固定资产、无形资产和其他长期资产支付的现金／当... |
| 269 | `CashWorkingIndex` | 现金营运指数 | number(19,4) | ✓ | 62.51% | 现金营运指数(CashWorkingIndex)=经营活动产生的现金流量净额／（净利润+资产减值准备+当期计提折旧与摊销... |
| 270 | `OperCashStability` | 营业现金稳定性 | number(19,4) | ✓ | 44.11% | 营业现金稳定性(OperCashStability)=(固定资产折旧+投资性房地产折旧/摊销+使用权资产摊销/折旧）/经... |
| 271 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(19,4) | ✓ | 96.35% | 经营活动产生的现金流量净额/营业收入(%)(CashRateOfSales)=经营活动产生的现金流量净额/营业收入*10... |
| 272 | `NetOperCFToToOperReve` | 经营现金净流量/营业总收入(%) | number(19,4) | ✓ | 96.45% | 经营现金净流量/营业总收入(%)(NetOperCFToToOperReve)=经营活动产生的现金流量净额/营业总收入*... |
| 273 | `NOCFToOperatingNI` | 经营活动产生的现金流量净额/经营活动净收益(%) | number(19,4) | ✓ | 69.23% | 经营活动产生的现金流量净额/经营活动净收益＝经营活动产生的现金流量净额/经营活动净收益*100% 其中，"经营活动净收益... |
| 274 | `NOCFToOperatingProf` | 经营活动产生的现金流量净额/营业利润(%) | number(19,4) | ✓ | 81.0% | 经营活动产生的现金流量净额/营业利润(%)(NOCFToOperatingProf)=经营活动产生的现金流量净额/营业利... |
| 275 | `NOCFToEBITDA` | 经营活动产生的现金流量净额/息税折旧摊销前利润(反推) | number(19,4) | ✓ | 56.43% | 经营活动产生的现金流量净额/息税折旧摊销前利润(反推)(NOCFToEBITDA)=经营活动产生的现金流量净额/息税折旧... |
| 276 | `MarginOperCashtoProfit` | 经营活动产生的现金净流量与净利润差(元) | number(19,4) | ✓ | 96.73% | 经营活动产生的现金净流量与净利润差(元)(MarginOperCashtoProfit)=经营活动产生的现金流量净额-净... |
| 277 | `NetOperCFRatio` | 经营活动产生的现金流量净额占比 | number(19,4) | ✓ | 50.68% | 经营活动产生的现金流量净额占比(NetOperCFRatio)=经营活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 278 | `NetInvestCFRatio` | 投资活动产生的现金流量净额占比 | number(19,4) | ✓ | 50.32% | 投资活动产生的现金流量净额占比(NetInvestCFRatio)=投资活动产生的现金流量净额/(经营活动产生的现金流量... |
| 279 | `NetFinaCFRatio` | 筹资活动产生的现金流量净额占比 | number(19,4) | ✓ | 49.8% | 筹资活动产生的现金流量净额占比(NetFinaCFRatio)=筹资活动产生的现金流量净额/(经营活动产生的现金流量净额... |
| 280 | `FreeCashFlowToNPPC` | 自由现金流与归属母公司净利润比率 | number(19,4) | ✓ | 53.06% | 自由现金流与归属母公司净利润比率(FreeCashFlowToNPPC)=企业自由现金流量/归属母公司股东的净利润，其中... |
| 281 | `CashToMeetInvestNeeds` | 现金满足投资比率(%) | number(19,4) | ✓ | 91.85% | 现金满足投资比率(%)(CashToMeetInvestNeeds)=经营活动产生的现金流量净额／(购建固定资产、无形资... |
| 282 | `ExternalFinanceRatio` | 外部融资比率(%) | number(19,4) | ✓ | 92.65% | 外部融资比率(%)(ExternalFinanceRatio)=(经营性应付项目增(减)净额+筹资现金流入量)/现金流入... |
| 283 | `CashPayStaffRatio` | 支付给职工的现金比率(%) | number(19,4) | ✓ | 91.33% | 支付给职工的现金比率(%)(CashPayStaffRatio)=支付给职工以及为职工支付的现金/销售商品、提供劳务收到... |
| 284 | `DividendPaidRatio` | 股利支付率(%) | number(19,4) | ✓ | 16.0% | 股利支付率(%)(DividendPaidRatio)＝（累计派现合计/归属于母公司所有者的净利润）*100%。 |
| 285 | `RetainedEarningRatio` | 留存盈余比率(%) | number(19,4) | ✓ | 100.0% | 留存盈余比率(%)(RetainedEarningRatio)＝100%-股利支付率。 |
| 286 | `Dividend` | 累计派现合计(元) | number(19,4) | ✓ | 16.18% | 累计派现合计(元)(Dividend)：根据公司公布的分红实施方案，将当年年初至当前截止日期实施的多次分红求和计算。 |
| 287 | `DividendCover` | 股利保障倍数(倍) | number(19,4) | ✓ | 16.17% | 股利保障倍数(倍)(CashDividendCover)＝归属于母公司所有者的净利润/累计派现合计。 |
| 288 | `CashDividendCover` | 现金股利保障倍数(倍) | number(19,4) | ✓ | 26.2% | 现金股利保障倍数(倍)(CashDividendCover)＝经营活动产生的现金流量净额/本期实际支付的普通股股利；其中... |
| 289 | `DebtAssetsRatio` | 资产负债率(%) | number(19,4) | ✓ | 97.9% | 资产负债率(%)(DebtAssetsRatio)＝负债合计/资产合计*100%。 |
| 290 | `DebtARatioCutADRecp` | 剔除预收账款后的资产负债率(%) | number(19,4) | ✓ | 97.9% | 剔除预收账款后的资产负债率(%)(DebtARatioCutADRecp)=(负债合计-预收款项-合同负债)／(资产总额... |
| 291 | `DebtARatioCutADReNo` | 剔除预收账款后的资产负债率_公告口径(%) | number(19,4) | ✓ | 97.9% | 剔除预收账款后的资产负债率_公告口径(%)(DebtARatioCutADReNo)=(负债合计-预收款项-合同负债)／... |
| 292 | `DebtARatioCutGoodwill` | 剔除商誉后的资产负债率(%) | number(19,4) | ✓ | 92.81% | 剔除商誉后的资产负债率(%)(DebtARatioCutGoodwill)=负债总计／（资产总计-商誉)*100%，金融... |
| 293 | `InBearDebtAssetsRatio` | 有息资产负债率(%) | number(19,4) | ✓ | 92.81% | 有息资产负债率(%)(InBearDebtAssetsRatio)=带息债务/资产总计*100%，"带息债务"计算方法详... |
| 294 | `CashEquivalentsRatio` | 货币资金/流动资产(%) | number(19,4) | ✓ | 92.29% | 货币资金/流动资产(%)(CashEquivalentsRatio)=(货币资金/现金及存放中央银行款项)/流动资产合计... |
| 295 | `FixAssetRatio` | 固定资产比率(%) | number(19,4) | ✓ | 96.69% | 固定资产比率(%)(FixAssetRatio)＝固定资产（若无数据，取固定资产合计）/资产总额*100%。 |
| 296 | `IntangibleAssetRatio` | 无形资产比率(%) | number(19,4) | ✓ | 91.91% | 无形资产比率(%)(IntangibleAssetRatio)＝无形资产/资产总额*100%。 |
| 297 | `CurrentAssetsToTA` | 流动资产/总资产(%) | number(19,4) | ✓ | 92.6% | 流动资产/总资产(%)(CurrentAssetsToTA)=流动资产合计/资产总计*100%。 |
| 298 | `NonCurrentAssetsToTA` | 非流动资产/总资产(%) | number(19,4) | ✓ | 92.43% | 非流动资产/总资产(%)(NonCurrentAssetsToTA)=非流动资产合计/资产总计*100%。 |
| 299 | `NetTangibleAToTA` | 有形资产/总资产(%) | number(19,4) | ✓ | 97.14% | 有形资产/总资产(%)(NetTangibleAToTA)=有形资产净值/总资产*100%，其中，"有形资产净值"计算方... |
| 300 | `BondsPayableToAsset` | 应付债券/总资产(%) | number(19,4) | ✓ | 38.53% | 应付债券/总资产(%)(BondsPayableToAsset)=应付债券/总资产*100%。 |
| 301 | `LongDebtToAsset` | 长期借款/总资产(%) | number(19,4) | ✓ | 64.51% | 长期借款/总资产(%)(LongDebtToAsset)=长期借款/总资产。 |
| 302 | `WorkingCapitalAsset` | 营运资金/资产总额(%) | number(19,4) | ✓ | 92.55% | 营运资金/资产总额(%)(WorkingCapitalAsset)=营运资本/资产总计C1.ZCZE*100%，其中，"... |
| 303 | `RetainedEarningAsset` | 留存收益/资产总额(%) | number(19,4) | ✓ | 96.84% | 留存收益/资产总额(%)(RetainedEarningAsset)=（盈余公积+未分配利润）/资产总额*100%。 |
| 304 | `SEWMIToTotalCapital` | 归属母公司股东的权益/全部投入资本(%) | number(19,4) | ✓ | 92.01% | 归属母公司股东的权益/全部投入资本(%)(SEWMIToTotalCapital)=归属母公司所有者权益(或股东权益)合... |
| 305 | `InBearDebtToTotCapital` | 带息债务/全部投入资本(%) | number(19,4) | ✓ | 92.4% | 带息债务/全部投入资本(%)(InBearDebtToTotCapital)=带息债务/全部投入资本*100%，"带息债... |
| 306 | `CurrentLiabilityToTL` | 流动负债/负债合计(%) | number(19,4) | ✓ | 92.51% | 流动负债/负债合计(%)(CurrentLiabilityToTL)=流动负债合计/负债总计*100%。 |
| 307 | `TotalCLiaToSEWMI` | 流动负债权益比率(%) | number(19,4) | ✓ | 91.58% | 流动负债权益比率(%)(TotalCLiaToSEWMI)=流动负债合计/归属于母公司股东的权益合计*100%。 |
| 308 | `NonCurrLiabilityToTL` | 非流动负债/负债合计(%) | number(19,4) | ✓ | 89.44% | 非流动负债/负债合计(%)(NonCurrLiabilityToTL)=非流动负债合计/负债总计*100。 |
| 309 | `TotalNonCLiaToSEWMI` | 非流动负债权益比率(%) | number(19,4) | ✓ | 88.56% | 非流动负债权益比率(%)(TotalNonCLiaToSEWMI)=非流动负债合计/归属于母公司股东的权益合计*100%... |
| 310 | `GoodWillToEquity` | 商誉/所有者权益(或股东权益)(%) | number(19,4) | ✓ | 37.65% | 商誉/所有者权益(或股东权益)(%)(GoodWillToEquity)=商誉/所有者权益(或股东权益)总计*100%。 |
| 311 | `LongDebtToEquity` | 非流动负债/股东权益合计 | number(19,4) | ✓ | 88.76% | 非流动负债/股东权益合计(LongDebtToEquity)=非流动负债合计/所有者权益(或股东权益)合计。 |
| 312 | `EquityFixedAssetRatio` | 股东权益与固定资产比率(%) | number(19,4) | ✓ | 96.62% | 股东权益与固定资产比率(%)(EquityFixedAssetRatio)=所有者权益（或股东权益）/固定资产(若无数据... |
| 313 | `EquityMultipler` | 权益乘数 | number(19,4) | ✓ | 97.17% | 权益乘数(EquityMultipler)＝资产合计/股东权益合计。 |
| 314 | `DebtEquityRatio` | 产权比率(%) | number(19,4) | ✓ | 97.02% | 产权比率(%)(DebtEquityRatio)＝负债合计／所有者权益(或股东权益)合计*100%。 |
| 315 | `DebtSEWithoutMIRatio` | 产权比率_不含少数股东权益(%) | number(19,4) | ✓ | 96.21% | 产权比率_不含少数股东权益(%)(DebtSEWithoutMIRatio)=负债总计/归属母公司所有者权益(或股东权益... |
| 316 | `LongAssetFitRate` | 长期资产适合率 | number(19,4) | ✓ | 96.88% | 长期资产适合率(LongAssetFitRate)＝(所有者权益+应付融资租赁款+长期借款+应付债券+长期应付款合计(为... |
| 317 | `TotalNonCurLiaToSEWMI` | 长期资本负债率(%) | number(19,4) | ✓ | 88.95% | 长期资本负债率(%)(TotalNonCurLiaToSEWMI)=非流动负债合计/（非流动负债合计+归属母公司所有者权... |
| 318 | `TotalNonCurAToSEWMI` | 资本固定化比率(%) | number(19,4) | ✓ | 91.45% | 资本固定化比率(%)(TotalNonCurAToSEWMI)=非流动资产合计/归属母公司所有者权益(或股东权益)合计*... |
| 319 | `FinancialLeverage` | 财务杠杆效率 | number(19,4) | ✓ | 91.35% | 财务杠杆效率（FinancialLeverage）=净资产收益率/资产报酬率，金融企业不计算。 |
| 320 | `NetDebtToEquityValue` | 净债务/股权价值 | number(19,4) | ✓ | 47.09% | 净债务/股权价值(NetDebtToEquityValue)=净债务/股权价值，其中，股权价值（总市值）=最近一个交易日... |
| 321 | `InBearDebtToEquiValue` | 带息债务/股权价值 | number(19,4) | ✓ | 47.09% | 带息债务/股权价值(InBearDebtToEquiValue)=带息债务/股权价值，"带息债务"计算方法详见Inter... |
| 322 | `EquityValueToTL` | 股权价值/负债合计(%) | number(19,4) | ✓ | 50.1% | 股权价值/负债合计(%)(EquityValueToTL)=股权价值/负债总计*100%，股权价值（总市值）=最近一个交... |
| 323 | `AccRecToOR` | 应收账款/营业收入(%) | number(19,4) | ✓ | 87.97% | 应收账款/营业收入(%)(AccRecToOR)=应收账款/营业收入*100%，金融类企业不计算。 |
| 324 | `MainProfitProportion` | 主营业务比率(%) | number(19,4) | ✓ | 86.92% | 主营业务比率(%)(MainProfitProportion)=营业利润/利润总额*100%。 |
| 325 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(19,4) | ✓ | 86.47% | 经营活动净收益/利润总额（OperatingNIToTP）＝经营活动净收益／利润总额*100%，“其中，"经营活动净收益... |
| 326 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(19,4) | ✓ | 73.86% | 价值变动净收益/利润总额(%)(ValueChangeNIToTP)＝价值变动净收益／利润总额*100% 其中，"价值变... |
| 327 | `InvestRAssociatesToTP` | 对联营合营公司投资收益/利润总额(%) | number(19,4) | ✓ | 36.42% | 对联营合营公司投资收益/利润总额(%)(InvestRAssociatesToTP)=对联营合营公司投资收益/利润总额*... |
| 328 | `InvestRToTP` | 投资收益/利润总额(%) | number(19,4) | ✓ | 73.0% | 投资收益/利润总额(%)(InvestRToTP)=投资净收益/利润总额*100%。 |
| 329 | `PreFinExpOPToTP` | 扣除财务费用前营业利润/利润总额(%) | number(19,4) | ✓ | 82.29% | 扣除财务费用前营业利润/利润总额(%)(PreFinExpOPToTP)=扣除融资费用前营业利润/利润总额*100%，金... |
| 330 | `NonOProToTP` | 非营业利润/利润总额(%) | number(19,4) | ✓ | 87.48% | 非营业利润/利润总额(%)(NonOProToTP)=（利润总额-营业利润）/利润总额*100%。 |
| 331 | `NetNonOperaIncomeToTP` | 营业外收支净额/利润总额(%) | number(19,4) | ✓ | 85.35% | 营业外收支净额/利润总额(%)(NetNonOperaIncomeToTP)=(营业外收入-营业外支出)/利润总额*10... |
| 332 | `TaxesToTP` | 所得税/利润总额(%) | number(19,4) | ✓ | 81.12% | 所得税/利润总额(%)(TaxesToTP)=所得税/利润总额*100%。 |
| 333 | `NonRecurrGLProportion` | 非经常性损益比率(%) | number(19,4) | ✓ | 46.42% | 非经常性损益比率(%)(NonRecurrGLProportion)=非经常性损益/净利润*100%。 |
| 334 | `NPCutToNP` | 扣除非经常损益后的归母净利润/净利润(%) | number(19,4) | ✓ | 54.04% | 扣除非经常损益后的归母净利润/净利润(%)(NPCutToNP)=扣非后归属于母公司所有者的净利润／净利润*100% ，... |
| 335 | `NPCutToNPPC` | 扣除非经常损益后的归母净利润/归属母公司股东的净利润(%) | number(19,4) | ✓ | 54.04% | 扣除非经常损益后的净利润/归属母公司股东的净利润(%)(NPCutToNPPC)=扣非后归属于母公司所有者的净利润/归属... |
| 336 | `EquityMultipler_DuPont` | 权益乘数_杜邦分析 | number(19,4) | ✓ | 96.35% | 权益乘数_杜邦分析(EquityMultipler_DuPont)＝（期初资产总额+期末资产总额）/（期初归属于母公司股... |
| 337 | `DebtEquityRatio_DuPont` | 产权比率_杜邦分析(%) | number(19,4) | ✓ | 96.25% | 产权比率_杜邦分析(%)(DebtEquityRatio_DuPont)=（期初负债合计+期末负债合计）/（期初归属母公... |
| 338 | `NPToTP_DuPont` | 净利润/利润总额(%) | number(19,4) | ✓ | 87.37% | 净利润/利润总额(%)(NPToTP_DuPont)=净利润/利润总额*100%。 |
| 339 | `TPToEBIT_DuPont` | 利润总额/息税前利润(反推)(%) | number(19,4) | ✓ | 84.88% | 利润总额/息税前利润(反推)(%)(TPToEBIT_DuPont)=利润总额/息税前利润*100%，“其中，"息税前利... |
| 340 | `NPPCToNP_DuPont` | 归属母公司股东的净利润/净利润(%) | number(19,4) | ✓ | 98.79% | 归属母公司股东的净利润/净利润(%)(NPPCToNP_DuPont)=归属母公司股东的净利润/净利润*100%。 |
| 341 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 342 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 343 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)：1-合并调整；2-合并未调整

### WorkingCapital (营运资本(元))

营运资本(元)（WorkingCapital）＝流动资产合计-流动负债合计。

### NetWorkingCaital (净营运资本(元))

净营运资本(元)（NetWorkingCaital）=流动资产合计－货币资金－无息流动负债；“无息流动负债”计算方法见InterestFreeCLiability[无息流动负债]；金融类企业不计算。

### NetTangibleAssets (有形资产净值(元))

有形资产净值(元)（NetTangibleAssets）＝归属于母公司的股东权益－(无形资产＋开发支出＋商誉＋长期待摊费用＋递延所得税资产)。

### InterestFreeCLiability (无息流动负债(元))

无息流动负债(元)(InterestFreeCLiability)=应付票据及应付账款(若为空，则取应付账款+应付票据)+预收款项+应付职工薪酬+应交税费+其他应付款(含利息和股利)(若为空，则取其他应付款+应付股利+应付利息)+预提费用+递延收益+合同负债+其他流动负债+衍生金融负债，金融类企业不计算。

### InterestFreeNonCL (无息非流动负债(元))

无息非流动负债（InterestFreeNonCL）=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。

### InterestBearCLiability (带息流动负债(元))

带息流动负债(元)(InterestBearCLiability)=流动负债合计-无息流动负债“其中，"无息流动负债"计算方法详见InterestFreeCLiability[无息流动负债(元)]，金融类企业不计算。

### InterestBearNonCL (带息非流动负债(元))

带息非流动负债(元)(InterestBearNonCL)=非流动负债合计-无息非流动负债 其中，"无息非流动负债"计算方法详见InterestFreeNonCL[无息非流动负债(元)]，金融类企业不计算。

### InterestFreeDebt (无息负债(元))

无息负债(元)（InterestFreeDebt）=应付票据及应付账款（应付账款)+应付票据)+预收款项+应付职工薪酬+应交税费+其他应付款(含利息和股利)（其他应付款+应付股利+应付利息)+预提费用+递延收益+合同负债+其他流动负债+衍生金融负债+应付款项
+长期应付款合计（长期应付款+专项应付款)+长期应付职工薪酬+预计负债+递延所得税负债+长期递延收益+其他非流动负债+卖出回购金融资产款+代理业务负债+持有待售负债+预收保费+应付手续费及佣金+应付分保账款
+保户储金及投资款+长期保险合同准备金（未到期责任准备金+未决赔款准备金+寿险责任准备金+长期健康险责任准备金)+独立账户负债+应付赔付款+应付保单红利+保险合同准备金+代理承销证券款+代理买卖证券款
+其他负债。

## SQL示例

```sql
-- 查询 公司财务衍生指标 数据
SELECT *
FROM fin_derivative
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
