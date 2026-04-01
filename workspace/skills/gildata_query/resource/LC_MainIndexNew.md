# LC_MainIndexNew

**中文名**: 公司主要财务分析指标_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_MainIndexNew` |
| MySQL表名 | `lc_mainindexnew` |
| 中文名 | 公司主要财务分析指标_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务衍生指标 |
| 更新频率 | 季更新 |
| 字段数量 | 273 |
| 版本 | 1.03 |

## 表描述

1.根据报告期公布的财务科目数据衍生而来的每股指标，以及反映公司盈利、偿债、成长、营运、分红、现金流、资本结构等能力的指标。
2.若某个报告期的数据有多次调整，则该表优先展示最新未调整数据；如对应截止日期无未调整数据，则展示调整数据。
3.“十、杜邦分析”另有两个指标－“净资产收益率ROE_平均,计算”和“总资产周转率”，分别在“二、盈利能力”和“五、营运能力”下。
4.本表中的同比数据计算公式为：（本期数据－去年同期数据）/︱去年同期数据︱*100%。
5.数据范围：1989-12-31至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% | 信息发布日期(InfoPublDate)：本表是基于三大表数据进行衍生计算，当多表关联计算时，因各表信息发布日期会存在不... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `BasicEPS` | 基本每股收益(元/股) | number(19,4) | ✓ | 55.78% | 基本每股收益（BasicEPS）：新会计准则下，取公司的实际披露数；旧会计准则下，取公司披露的每股收益（加权）。 |
| 6 | `DilutedEPS` | 稀释每股收益(元/股) | number(19,4) | ✓ | 47.76% | 稀释每股收益（DilutedEPS）：新会计准则下，取公司的实际披露数；旧会计准则下，稀释每股收益=归属于母公司的净利润... |
| 7 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(19,4) | ✓ | 95.11% | 每股收益_期末股本摊薄（EPS）： 每股收益_期末股本摊薄=归属于母公司的净利润/该报告期末总股本。 |
| 8 | `EPSCut` | 基本每股收益(扣除)(元/股) | number(19,4) | ✓ | 50.95% | 每股收益(扣除)(元/股)（EPSCut）：优先取原文披露值，原文若未披露，则通过计算赋值：每股收益(扣除)＝扣除后的净... |
| 9 | `EPSTTM` | 每股收益_TTM(元/股) | number(19,4) | ✓ | 95.26% | 每股收益_TTM（EPSTTM）=归属于母公司的净利润（TTM）/期末总股本 |
| 10 | `NetAssetPS` | 每股净资产(元/股) | number(19,4) | ✓ | 93.45% | 每股净资产（NetAssetPS）：直接取公司定期报告披露数据；若无披露，则，每股净资产=（归属于母公司的所有者权益-其... |
| 11 | `NetAssetPSAdjusted` | 调整后每股净资产(元/股) | number(19,4) | ✓ | 5.8% | 调整后每股净资产(元/股)（NetAssetPSAdjusted）：取原文披露值 |
| 12 | `TotalOperatingRevenuePS` | 每股营业总收入(元/股) | number(19,4) | ✓ | 95.21% | 每股营业总收入（TotalOperatingRevenuePS）＝营业总收入/该报告期期末总股本 |
| 13 | `MainIncomePS` | 每股营业收入(元/股) | number(19,4) | ✓ | 94.89% | 每股营业收入（MainIncomePS）＝营业收入/该报告期期末总股本 |
| 14 | `OperatingRevenuePSTTM` | 每股营业收入_TTM(元/股) | number(19,4) | ✓ | 95.15% | 每股营业收入_TTM（OperatingRevenuePSTTM）＝营业收入（TTM）/期末总股本 |
| 15 | `OperProfitPS` | 每股营业利润(元/股) | number(19,4) | ✓ | 94.84% | 每股营业利润（OperProfitPS）＝营业利润/期末总股本 |
| 16 | `EBITPS` | 每股息税前利润(元/股) | number(19,4) | ✓ | 90.22% | 每股息税前利润（EBITPS）＝息税前利润/期末总股本；“息税前利润”计算方法见EBIT[息税前利润(元)]；金融类企业... |
| 17 | `EBITDAPS` | 每股息税折旧前利润(元/股) | number(19,4) | ✓ | 90.22% | 每股息税折旧前利润(元/股)(EBITDAPS)＝息税折旧摊销前利润/期末总股本；“息税折旧摊销前利润”计算方法见EBI... |
| 18 | `CapitalSurplusFundPS` | 每股资本公积金(元/股) | number(19,4) | ✓ | 89.31% | 每股资本公积金（CapitalSurplusFundPS）＝资本公积/期末总股本 |
| 19 | `SurplusReserveFundPS` | 每股盈余公积(元/股) | number(19,4) | ✓ | 88.37% | 每股盈余公积金（SurplusReserveFundPS）＝盈余公积/期末总股本 |
| 20 | `AccumulationFundPS` | 每股公积金(元/股) | number(19,4) | ✓ | 95.76% | 每股公积金（AccumulationFundPS）＝（资本公积金+盈余公积金）/期末总股本 |
| 21 | `UndividedProfit` | 每股未分配利润(元/股) | number(19,4) | ✓ | 93.13% | 每股未分配利润（UndividedProfit）＝未分配利润/期末总股本 |
| 22 | `RetainedEarningsPS` | 每股留存收益(元/股) | number(19,4) | ✓ | 95.76% | 每股留存收益（RetainedEarningsPS）＝（盈余公积+未分配利润）/期末总股本 |
| 23 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 92.3% | 每股经营活动产生的现金流量净额（OperCashFlowPS）：经营活动产生的现金流量净额/期末总股本。 |
| 24 | `OperCashFlowPSTTM` | 每股经营活动产生的现金流量净额_TTM(元/股) | number(19,4) | ✓ | 93.6% | 每股经营活动产生的现金流量净额_TTM（OperCashFlowPSTTM）=经营活动产生的现金流量净额（TTM）/期末... |
| 25 | `CashFlowPS` | 每股现金流量净额(元/股) | number(19,4) | ✓ | 91.74% | 每股现金流量净额（CashFlowPS）=现金及现金等价物净增加额/期末总股本 |
| 26 | `CashFlowPSTTM` | 每股现金流量净额_TTM(元/股) | number(19,4) | ✓ | 93.45% | 每股现金流量净额_TTM（CashFlowPSTTM）=现金及现金等价物净增加额（TTM）/期末总股本 |
| 27 | `EnterpriseFCFPS` | 每股企业自由现金流量(元/股) | number(19,4) | ✓ | 90.22% | 每股企业自由现金流量（EnterpriseFCFPS）=企业自由现金流量/期末总股本。企业自由现金流量（FreeCash... |
| 28 | `ShareHolderFCFPS` | 每股股东自由现金流量(元/股) | number(19,4) | ✓ | 90.22% | 每股股东自由现金流量（ShareholderFCFPS）=[企业自由现金流量-偿还债务所支付的现金+取得借款收到的现金+... |
| 29 | `ROEAvg` | 净资产收益率_平均,计算值(%) | number(18,4) | ✓ | 92.88% | 净资产收益率_平均,计算值（ROEAvg）=（归属于母公司的净利润*2/（期初归属于母公司的股东权益+期末归属于母公司的... |
| 30 | `ROEWeighted` | 净资产收益率_加权,公布值(%) | number(18,4) | ✓ | 46.76% | 净资产收益率_加权,公布值（ROEWeighted）：为公司定期报告披露数据。 |
| 31 | `ROE` | 净资产收益率_摊薄,公布值(%) | number(18,4) | ✓ | 92.95% | 净资产收益率_摊薄,公布值（ROE）：直接取公司定期报告披露数据；若无披露值，则ROE（摊薄）=归属于母公司的净利润/该... |
| 32 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(18,6) | ✓ | 49.46% | 净资产收益率_扣除,摊薄(%)(ROECut)：展示计算值，计算公式=扣除非经常性损益后归属于母公司的净利润/该报告期期... |
| 33 | `ROECutWeighted` | 净资产收益率_扣除,加权(%) | number(18,6) | ✓ | 31.09% | 净资产收益率_扣除,加权（ROECutWeighted）：直接取公司定期报告披露数据。 |
| 34 | `ROETTM` | 净资产收益率_TTM(%) | number(18,4) | ✓ | 92.69% | 净资产收益率_TTM（ROETTM）＝（归属于母公司的净利润（TTM）/期末归属于母公司的股东权益*100% |
| 35 | `ROA_EBIT` | 总资产报酬率(%) | number(18,4) | ✓ | 89.5% | 总资产报酬率（ROA_EBIT）＝息税前利润*2/（期初总资产+期末总资产）*100% 其中，“息税前利润”计算方法见E... |
| 36 | `ROA_EBITTTM` | 总资产报酬率_TTM(%) | number(18,4) | ✓ | 89.04% | 总资产报酬率_TTM（ROA_EBITTTM）＝息税前利润（TTM）/总资产（MRQ）*100%其中，息税前利润（TTM... |
| 37 | `ROA` | 总资产净利率(%) | number(18,6) | ✓ | 95.39% | 总资产净利率（ROA）＝含少数股东损益的净利润*2/（期初总资产+期末总资产）*100% |
| 38 | `ROATTM` | 总资产净利率_TTM(%) | number(18,4) | ✓ | 95.35% | 总资产净利率_TTM（ROATTM）＝含少数股东损益的净利润（TTM）/总资产（MRQ）*100% |
| 39 | `ROACut` | 总资产净利率_不含少数股东损益(%) | number(12,4) | ✓ | 93.91% | 总资产净利率_不含少数股东损益(%)(ROACut)＝归属于母公司所有者的净利润*2/（期初总资产+期末总资产）*100... |
| 40 | `ROACutTTM` | 总资产净利率_不含少数股东损益_TTM(%) | number(12,4) | ✓ | 94.45% | 总资产净利率_不含少数股东损益_TTM(%)(ROACutTTM)＝归属于母公司的净利润（TTM）/总资产 *100% |
| 41 | `AnnualizedROE` | 年化净资产收益率(%) | number(12,4) | ✓ | 92.88% | 年化净资产收益率(%)(AnnualizedROE)：根据“净资产收益率*N”计算，一季报N=4，二季报N=2，三季报N... |
| 42 | `AnnualizedROAEBIT` | 年化总资产报酬率(%) | number(12,4) | ✓ | 89.5% | 年化总资产报酬率(%)(AnnualizedROAEBIT)：根据“总资产报酬率*N”计算，一季报N=4，二季报N=2，... |
| 43 | `AnnualizedROA` | 年化总资产净利率(%) | number(12,4) | ✓ | 95.39% | 年化总资产净利率(%)(AnnualizedROA)：根据“总资产净利率*N”计算，一季报N=4，二季报N=2，三季报N... |
| 44 | `ROIC` | 投入资本回报率(%) | number(18,6) | ✓ | 92.94% | 投入资本回报率ROIC=（（息税前利润*（1-有效税率）*2/（期初全部投入资本+期末全部投入资本））*100% 其中，... |
| 45 | `ROICTTM` | 投入资本回报率_TTM(%) | number(12,4) | ✓ | 89.16% | 投入资本回报率_TTM(%)(ROICTTM)=EBIT*(1-有效税率)TTM／全部投入资本*100%；金融类企业不计... |
| 46 | `NetProfitRatio` | 销售净利率(%) | number(18,6) | ✓ | 98.29% | 销售净利率（NetProfitRatio）＝含少数股东损益的净利润/营业收入*100% |
| 47 | `NetProfitRatioTTM` | 销售净利率_TTM(%) | number(18,4) | ✓ | 98.7% | 销售净利率_TTM（NetProfitRatioTTM）＝含少数股东损益的净利润（TTM）/营业收入（TTM）*100% |
| 48 | `GrossIncomeRatio` | 销售毛利率(%) | number(18,6) | ✓ | 90.54% | 销售毛利率（GrossIncomeRatio）＝（营业收入-营业成本）/营业收入*100%，金融类企业不计算。 |
| 49 | `GrossIncomeRatioTTM` | 销售毛利率_TTM(%) | number(18,4) | ✓ | 91.58% | 销售毛利率_TTM（GrossIncomeRatioTTM）＝[营业收入（TTM）-营业成本（TTM）]/营业收入（TT... |
| 50 | `SalesCostRatio` | 销售成本率(%) | number(18,4) | ✓ | 90.54% | 销售成本率（SalesCostRatio）＝营业成本/营业收入*100%，金融类企业不计算。 |
| 51 | `PeriodCostsRate` | 销售期间费用率(%) | number(18,4) | ✓ | 91.21% | 销售期间费用率（PeriodCostsRate）＝（销售费用+管理费用+财务费用+研发费用）/营业收入*100%，金融类... |
| 52 | `PeriodCostsRateTTM` | 销售期间费用率_TTM(%) | number(18,4) | ✓ | 80.63% | 销售期间费用率_TTM（PeriodCostsRateTTM）＝[销售费用（TTM）+管理费用（TTM）+财务费用（TT... |
| 53 | `NPToTOR` | 净利润/营业总收入(%) | number(18,4) | ✓ | 98.42% | 净利润/营业总收入(%)(NPToTOR)：非金融类公司计算公式=净利润/营业总收入*100；金融类公司计算公式=净利润... |
| 54 | `NPToTORTTM` | 净利润/营业总收入_TTM(%) | number(18,4) | ✓ | 98.81% | 净利润／营业总收入_TTM（NPToTORTTM）；非金融类公司计算公式=净利润（TTM）/营业总收入（TTM）*100... |
| 55 | `OperatingProfitToTOR` | 营业利润/营业总收入(%) | number(18,4) | ✓ | 97.43% | 营业利润/营业总收入(%)(OperatingProfitToTOR)：非金融类公司计算公式=营业利润/营业总收入*10... |
| 56 | `OperatingProfitToTORTTM` | 营业利润/营业总收入_TTM(%) | number(18,4) | ✓ | 98.25% | 营业利润／营业总收入_TTM（OperatingProfitToTORTTM）：非金融类公司计算公式=营业利润（TTM）... |
| 57 | `EBIT` | 息税前利润(元) | number(19,4) | ✓ | 93.48% | 息税前利润（EBIT）＝利润总额＋利息费用  其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用=其中:利息... |
| 58 | `EBITToTOR` | 息税前利润/营业总收入(%) | number(18,4) | ✓ | 92.36% | 息税前利润/营业总收入(%)(EBITToTOR):此指标金融类企业不计算。 |
| 59 | `EBITToTORTTM` | 息税前利润/营业总收入_TTM(%) | number(18,4) | ✓ | 92.49% | 息税前利润／营业总收入_TTM（EBITToTORTTM）＝息税前利润（TTM）／营业总收入（TTM）*100%，金融类... |
| 60 | `EBITDA` | 息税折旧摊销前利润(元) | number(19,4) | ✓ | 93.48% | 息税折旧摊销前利润（EBITDA）＝息税前利润EBIT+固定资产折旧+投资性房地产折旧+无形资产摊销+长期待摊费用摊销+... |
| 61 | `EBITAssetRatio` | 息税前利润/资产总额(%) | number(18,4) | ✓ | 89.5% | 息税前利润/资产总额(%)（EBITAssetRatio）=EBIT/资产总额*100%，金融企业不计算。 |
| 62 | `EBITToToAssetsTTM` | 息税前利润/总资产_TTM(%) | number(12,4) | ✓ | 89.26% | 息税前利润/总资产_TTM(%)(EBITToToAssetsTTM)=息税前利润(TTM)/资产总额*100%,金融类... |
| 63 | `EBITDAToTOR` | 息税折旧前利润/营业总收入(%) | number(12,4) | ✓ | 92.36% | 息税折旧前利润/营业总收入(%)(EBITDAToTOR)=息税折旧前利润/营业总收入*100%,"息税折旧前利润"计算... |
| 64 | `EBIAT` | 息前税后利润(元) | number(19,4) | ✓ | 93.48% | 息前税后利润(元)（EBIAT）=EBIT*(1-有效税率），金融企业不计算。 |
| 65 | `TOperatingCostToTOR` | 营业总成本/营业总收入(%) | number(18,4) | ✓ | 90.96% | 营业总成本/营业总收入(%)(TOperatingCostToTOR):此指标金融类企业不计算。 |
| 66 | `TOperatingCostToTORTTM` | 营业总成本/营业总收入_TTM(%) | number(18,4) | ✓ | 91.95% | 营业总成本／营业总收入_TTM（TOperatingCostToTORTTM）＝营业总成本（TTM）／营业总收入（TTM... |
| 67 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(18,4) | ✓ | 82.75% | 销售费用/营业总收入(%)(	OperatingExpenseRate):此指标金融类企业不计算。 |
| 68 | `OperatingExpenseRateTTM` | 销售费用/营业总收入_TTM(%) | number(18,4) | ✓ | 83.92% | 销售费用／营业总收入_TTM（OperatingExpenseRateTTM）＝销售费用（TTM）／营业总收入（TTM）... |
| 69 | `AdminiExpenseRate` | 管理费用/营业总收入(%) | number(18,4) | ✓ | 90.77% | 管理费用/营业总收入(%)(AdminiExpenseRate):此指标金融类企业不计算。 |
| 70 | `AdminiExpenseRateTTM` | 管理费用/营业总收入_TTM(%) | number(18,4) | ✓ | 91.66% | 管理费用／营业总收入_TTM（AdminiExpenseRateTTM）＝管理费用（TTM）／营业总收入（TTM）*10... |
| 71 | `FinancialExpenseRate` | 财务费用/营业总收入(%) | number(18,4) | ✓ | 90.92% | 财务费用/营业总收入(%)(	FinancialExpenseRate):此指标金融类企业不计算。 |
| 72 | `FinancialExpenseRateTTM` | 财务费用/营业总收入_TTM(%) | number(18,4) | ✓ | 91.89% | 财务费用／营业总收入_TTM（FinancialExpenseRateTTM）＝财务费用（TTM）／营业总收入（TTM）... |
| 73 | `TotalProfitCostRatio` | 成本费用利润率(%) | number(18,6) | ✓ | 91.55% | 成本费用利润率（TotalProfitCostRatio）＝利润总额/成本费用总额*100%其中，成本费用总额＝营业成本... |
| 74 | `AssetImpaLossToTOR` | 资产减值损失/营业总收入(%) | number(18,4) | ✓ | 63.79% | 资产减值损失/营业总收入(%)(AssetImpaLossToTOR)：非金融类公司计算公式=资产减值损失/营业总收入*... |
| 75 | `AssetImpaLossToTORTTM` | 资产减值损失/营业总收入_TTM(%) | number(18,4) | ✓ | 75.75% | 资产减值损失／营业总收入_TTM（AssetImpaLossToTORTTM）：非金融类公司计算公式=资产减值损失（TT... |
| 76 | `AssetILossToOProfit` | 资产减值损失/营业利润(%) | number(12,4) | ✓ | 50.81% | 资产减值损失/营业利润(%)(AssetILossToOProfit)=资产减值损失/营业利润*100%。 |
| 77 | `TaxRatio` | 销售税金率(%) | number(18,4) | ✓ | 95.29% | 销售税金率(%)（TaxRatio）:非金融类公司计算公式=税金及附加/营业总收入*100；金融类公司计算公式=税金及附... |
| 78 | `NetProfit` | 归属母公司净利润(元) | number(19,4) | ✓ | 98.14% | 归属母公司净利润(元)(NetProfit)：取利润表披露值。 |
| 79 | `NetProfToOpRevenTTM` | 归属母公司股东的净利润/营业收入_TTM(%) | number(12,4) | ✓ | 97.87% | 归属母公司股东的净利润/营业收入_TTM(%)(NetProfToOpRevenTTM)=归属母公司股东的净利润（TTM... |
| 80 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(元) | number(19,4) | ✓ | 50.81% | 扣除非经常性损益后的净利润（NetProfitCut）：取公布值。 |
| 81 | `OperatingProfitRatio` | 营业利润率(%) | number(18,6) | ✓ | 97.32% | 营业利润率（OperatingProfitRatio）＝营业利润/营业收入*100% |
| 82 | `OperatingProRatioTTM` | 营业利润率_TTM(%) | number(12,4) | ✓ | 98.15% | 营业利润率_TTM(%)(OperatingProRatioTTM)=营业利润（TTM）／营业收入（TTM）*100%。 |
| 83 | `MainProfitProportion` | 主营业务比率(%) | number(12,4) | ✓ | 94.19% | 主营业务比率(%)(MainProfitProportion)=营业利润/利润总额*100% |
| 84 | `EVWtoEBITDA` | EVW/EBITDA(含货币资金) | number(18,4) | ✓ | 92.95% | EVW/EBITDA(含货币资金)(EVWtoEBITDA)=企业价值（含货币资金）EVW／息税折旧摊销前利润,金融类企... |
| 85 | `EVNtoEBITDA` | EVN/EBITDA(剔除货币资金) | number(18,4) | ✓ | 92.95% | EVN/EBITDA(剔除货币资金)(EVNtoEBITDA)=企业价值（剔除货币资金）EVN／息税折旧摊销前利润,金融... |
| 86 | `EVW` | EVW(含货币资金) | number(18,4) | ✓ | 93.48% | EVW(含货币资金)（EVW）=总市值+带息债务，金融企业不计算 |
| 87 | `EVN` | EVN(剔除货币资金) | number(18,4) | ✓ | 93.48% | EVN(剔除货币资金)（EVN）=总市值-货币资金+带息债务，金融企业不计算 |
| 88 | `NonRecurrGLProportion` | 非经常性损益比率(%) | number(18,4) | ✓ | 50.8% | 非经常性损益比率(%)（NonRecurrGLProportion）=非经常性损益/净利润*100 |
| 89 | `CapitalReturn` | 资本收益率(%) | number(18,4) | ✓ | 93.24% | 资本收益率(%)（CapitalReturn）=EBIT/(长期负债+股东权益)*100=EBIT/（(期末长期负债+期... |
| 90 | `EquityGrowRate` | 资本保值增值率(%) | number(18,4) | ✓ | 91.67% | 资本保值增值率(%)（EquityGrowRate）=期末所有者权益/期初所有者权益*100 |
| 91 | `RetainedEarningAsset` | 留存收益/资产总额(%) | number(18,4) | ✓ | 93.51% | 留存收益/资产总额(%)（RetainedEarningAsset）=（盈余公积+未分配利润）/资产总额*100 |
| 92 | `CurrentRatio` | 流动比率 | number(18,6) | ✓ | 88.57% | 流动比率（CurrentRatio）＝流动资产合计／流动负债合计，金融类企业不计算。 |
| 93 | `QuickRatio` | 速动比率 | number(18,6) | ✓ | 88.6% | 速动比率（QuickRatio）＝（流动资产合计-存货）／流动负债合计，金融类企业不计算。 |
| 94 | `SuperQuickRatio` | 超速动比率 | number(18,6) | ✓ | 88.6% | 超速动比率（SuperQuickRatio）＝（货币资金+交易性金融资产+应收票据及应收账款+其他应收款（含利息和股利）... |
| 95 | `DebtEquityRatio` | 产权比率(%) | number(18,6) | ✓ | 94.48% | 产权比率（DebtEquityRatio）＝负债合计／所有者权益(或股东权益)合计*100% |
| 96 | `SEWithoutMIToTL` | 归属母公司股东的权益/负债合计(%) | number(18,4) | ✓ | 93.69% | 归属母公司股东的权益/负债合计(%)(SEWithoutMIToTL)=归属母公司股东的权益/负债合计*100%。 |
| 97 | `SEWMIToInterestBearDebt` | 归属母公司股东的权益/带息债务(%) | number(18,4) | ✓ | 82.02% | 归属母公司股东的权益/带息债务(%)(SEWMIToInterestBearDebt)＝归属母公司股东的权益／（负债合计... |
| 98 | `DebtTangibleEquityRatio` | 有形净值债务率(%) | number(18,6) | ✓ | 93.91% | 有形净值债务率（DebtTangibleEquityRatio）＝负债合计／有形净值*100%，其中，有形净值=归属于母... |
| 99 | `TangibleAToInteBearDebt` | 有形净值/带息债务(%) | number(18,4) | ✓ | 82.7% | 有形净值／带息债务（TangibleAToInteBearDebt）＝有形净值／带息债务*100%，其中，有形净值=归属... |
| 100 | `TangibleAToNetDebt` | 有形净值/净债务(%) | number(18,4) | ✓ | 57.05% | 有形净值／净债务（TangibleAToNetDebt）＝（有形净值／净债务）*100%，其中，有形净值=归属于母公司的... |
| 101 | `TangibleAToTL` | 有形资产/负债合计(%) | number(18,4) | ✓ | 89.23% | 有形资产/负债合计(%)(TangibleAToTL)=有形资产净值/负债合计*100%，其中，有形净值=归属于母公司的... |
| 102 | `EBITDAToTLiability` | 息税折旧摊销前利润/负债合计 | number(18,4) | ✓ | 89.23% | 息税折旧摊销前利润／负债合计（EBITDAToTLiability）：“息税折旧摊销前利润”算法见EBITDA[息税折旧... |
| 103 | `NOCFToTLiability` | 经营活动产生现金流量净额/负债合计 | number(18,4) | ✓ | 87.02% | 经营活动产生现金流量净额/负债合计(NOCFToTLiability)：此指标金融类企业不计算。 |
| 104 | `NOCFToInterestBearDebt` | 经营活动产生现金流量净额/带息债务 | number(18,4) | ✓ | 80.61% | 经营活动产生现金流量净额/带息债务（NOCFToInterestBearDebt）：“带息债务”算法见TangibleA... |
| 105 | `NOCFToCurrentLiability` | 经营活动产生现金流量净额/流动负债 | number(18,4) | ✓ | 86.51% | 经营活动产生现金流量净额/流动负债(NOCFToCurrentLiability)：此指标金融类企业不计算。 |
| 106 | `NOCFToNetDebt` | 经营活动产生现金流量净额/净债务 | number(18,4) | ✓ | 59.05% | 经营活动产生现金流量净额/净债务（NOCFToNetDebt）：“净债务”算法见TangibleAToNetDebt[有... |
| 107 | `NOCFToTotalNonCurLia` | 经营活动产生现金流量净额/非流动负债(%) | number(18,4) | ✓ | 81.87% | 经营活动产生现金流量净额/非流动负债(%)(NOCFToTotalNonCurLia)=经营活动产生现金流量净额/非流动... |
| 108 | `InterestCover` | 利息保障倍数(倍) | number(18,6) | ✓ | 70.36% | 利息保障倍数（InterestCover）＝息税前利润/利息费用。其中，“息税前利润”计算方法见EBIT[息税前利润(元... |
| 109 | `NOCFInterestCover` | 现金流量利息保障倍数(倍) | number(18,4) | ✓ | 68.56% | 现金流量利息保障倍数(倍)(NOCFInterestCover)=经营活动产生现金流量净额/利息费用，其中，分母中的利息... |
| 110 | `RepaymentCover` | 偿债倍数(倍) | number(18,4) | ✓ | 91.81% | 偿债倍数(倍)（RepaymentCover）=EBIT/[利息+本金偿还/(1-税率)],税率取有效税率,当所得税和利... |
| 111 | `NetAssetLiabilityRatio` | 净资产负债率(%) | number(18,4) | ✓ | 93.69% | 净资产负债率(%)(NetAssetLiabilityRatio)=负债合计/归属母公司所有者权益(或股东权益)合计*1... |
| 112 | `NetLiabilityRatio` | 净负债率(%) | number(18,4) | ✓ | 88.56% | 净负债率(%)(NetLiabilityRatio)=（带息债务-货币资金）/所有者权益*100%；“带息债务”算法见T... |
| 113 | `WorkingCapitalAsset` | 营运资金/资产总额 | number(18,4) | ✓ | 88.71% | 营运资金/资产总额（WorkingCapitalAsset）：金融企业不计算 |
| 114 | `LongDebtToWorkingCapital` | 非流动负债/营运资金(%) | number(18,6) | ✓ | 68.65% | 	 非流动负债/营运资金(%)（LongDebtToWorkingCapital）＝非流动负债合计/（流动资产-流动负债... |
| 115 | `LongDebtRatio` | 长期负债占比 | number(18,4) | ✓ | 95.31% | 长期负债占比（LongDebtRatio）＝（长期借款+应付债券+长期应付款+专项应付款）/负债合计 |
| 116 | `OperCashInToCurrentDebt` | 现金流动负债比 | number(18,6) | ✓ | 86.51% | 现金流动负债比（OperCashInToCurrentDebt）＝经营现金净流入/流动负债，金融类企业不计算。 |
| 117 | `CashRatio` | 现金比率(%) | number(18,4) | ✓ | 88.6% | 现金比率(%)(CashRatio)＝（货币资金+交易性金融资产+应收票据）/流动负债合计*100%，金融类企业不计算。 |
| 118 | `OperCashInToDueDebt` | 现金到期债务比 | number(18,4) | ✓ | 80.59% | 现金到期债务比(OperCashInToDueDebt)=经营活动产生的现金流量净额／（短期借款+一年内到期的非流动负债... |
| 119 | `CashToCurliability` | 货币资金/短期债务(%) | number(18,4) | ✓ | 82.22% | 货币资金/短期债务(%)(CashToCurliability)=货币资金/短期债务*100%，其中，短期债务=短期借款... |
| 120 | `NetNoFCFToCLiability` | 非筹资性现金净流量与流动负债的比率(%) | number(18,4) | ✓ | 88.6% | 非筹资性现金净流量与流动负债的比率(%)(NetNoFCFToCLiability)=（经营活动产生的现金流量净额+投资... |
| 121 | `NetNoFCFToTLiability` | 非筹资性现金净流量与负债总额的比率(%) | number(18,4) | ✓ | 95.31% | 非筹资性现金净流量与负债总额的比率(%)(NetNoFCFToTLiability)=（经营活动产生的现金流量净额+投资... |
| 122 | `EBITDAToIntBearDebt` | 息税折旧前利润/带息债务(%) | number(18,4) | ✓ | 82.7% | 息税折旧前利润/带息债务(%)(EBITDAToIntBearDebt)=息税折旧前利润/带息债务*100%，“息税折旧... |
| 123 | `EBITDAToInttFinExp` | 息税折旧前利润/利息费用(%) | number(18,4) | ✓ | 70.36% | 息税折旧前利润/利息费用(%)(EBITDAToInttFinExp)=息税折旧前利润/利息费用*100%，“息税折旧摊... |
| 124 | `EntireliabToEBITDA` | 全部债务/息税折旧前利润 | number(18,4) | ✓ | 92.95% | 全部债务/息税折旧前利润(EntireliabToEBITDA)=全部债务/息税折旧前利润，“息税前利润”计算方法见EB... |
| 125 | `BasicEPSYOY` | 基本每股收益同比增长(%) | number(18,4) | ✓ | 49.46% | 基本每股收益同比增长(%)(BasicEPSYOY)=（本期基本每股收益-上年同期基本每股收益）/ABS(上年同期基本每... |
| 126 | `BasicEPSGrowRate3Y` | 基本每股收益3年复合增长率(%) | number(18,4) | ✓ | 41.45% | 基本每股收益3年复合增长率(%)(BasicEPSGrowRate3Y)：当三年前同期基本每股收益为正数时，基本每股收益... |
| 127 | `DilutedEPSYOY` | 稀释每股收益同比增长(%) | number(18,4) | ✓ | 44.17% | 稀释每股收益同比增长(%)(DilutedEPSYOY)=（本期稀释每股收益-上年同期稀释每股收益）/ABS(上年同期稀... |
| 128 | `DilutedEPSGrowRate3Y` | 稀释每股收益3年复合增长率(%) | number(18,4) | ✓ | 36.08% | 稀释每股收益3年复合增长率(%)(DilutedEPSGrowRate3Y)：当三年前同期稀释每股收益为正数时，稀释每股... |
| 129 | `EPSYOY` | 每股收益同比增长(%) | number(18,4) | ✓ | 83.38% | 每股收益同比增长(%)(EPSYOY)=（本期每股收益-上年同期每股收益）/ABS(上年同期每股收益)*100%，如果上... |
| 130 | `EPSGrowRate3Y` | 每股收益3年复合增长率(%) | number(18,4) | ✓ | 65.97% | 每股收益3年复合增长率(%)(EPSGrowRate3Y)：当三年前同期每股收益为正数时，每股收益3年复合增长率=[（本... |
| 131 | `PBVGrowRate` | 每股净资产同比增长(%) | number(18,4) | ✓ | 81.64% | 每股净资产同比增长(%)(PBVGrowRate)=（本期每股净资产-上年同期每股净资产）/ABS(上年同期每股净资产)... |
| 132 | `PBVGrowRate3Y` | 每股净资产3年复合增长率(%) | number(18,4) | ✓ | 64.52% | 每股净资产3年复合增长率(%)(PBVGrowRate3Y)：当三年前同期每股净资产为正数时，每股净资产3年复合增长率=... |
| 133 | `OperatingRevenueGrowRate` | 营业收入同比增长(%) | number(18,4) | ✓ | 86.58% | 营业收入同比增长(%)(OperatingRevenueGrowRate)=（本期营业收入-上年同期营业收入）/ABS(... |
| 134 | `ORComGrowRate3Y` | 营业收入3年复合增长率(%) | number(18,4) | ✓ | 68.33% | 营业收入3年复合增长率(%)(ORComGrowRate3Y)：当三年前同期营业收入为正数时，营业收入3年复合增长率=[... |
| 135 | `OperProfitGrowRate` | 营业利润同比增长(%) | number(18,4) | ✓ | 86.32% | 营业利润同比增长(%)(OperProfitGrowRate)=（本期营业利润-上年同期营业利润）/ABS(上年同期营业... |
| 136 | `OperProfitGrowRate3Y` | 营业利润3年复合增长率(%) | number(18,4) | ✓ | 68.11% | 营业利润3年复合增长率(%)(OperProfitGrowRate3Y)：当三年前同期营业利润为正数时，营业利润3年复合... |
| 137 | `TotalProfeiGrowRate` | 利润总额同比增长(%) | number(18,4) | ✓ | 87.16% | 利润总额同比增长(%)(TotalProfeiGrowRate)=（本期利润总额-上年同期利润总额）/ABS(上年同期利... |
| 138 | `TPGrowRate3Y` | 利润总额3年复合增长率(%) | number(18,4) | ✓ | 68.83% | 利润总额3年复合增长率(%)(TPGrowRate3Y)：当三年前同期利润总额为正数时，利润总额3年复合增长率=[（本期... |
| 139 | `NetProfitGrowRate` | 净利润同比增长(%) | number(18,4) | ✓ | 87.46% | 净利润同比增长(%)(NetProfitGrowRate)=（本期净利润-上年同期净利润）/ABS(上年同期净利润)*1... |
| 140 | `NetProfitGrowRate3Y` | 净利润3年复合增长率(%) | number(18,4) | ✓ | 69.04% | 净利润3年复合增长率(%)(NetProfitGrowRate3Y)：当三年前同期净利润为正数时，净利润3年复合增长率=... |
| 141 | `TORGrowRate` | 营业总收入同比增长率(%) | number(18,4) | ✓ | 86.71% | 营业总收入同比增长率(%)(TORGrowRate)=（本期营业总收入-上年同期营业总收入）/ABS(上年同期营业总收入... |
| 142 | `TORGrowRate3Y` | 营业总收入3年复合增长率(%) | number(18,4) | ✓ | 68.43% | 营业总收入3年复合增长率(%)(TORGrowRate3Y)：当三年前同期营业总收入为正数时，营业总收入3年复合增长率=... |
| 143 | `NPParentCompanyYOY` | 归属母公司股东的净利润同比增长(%) | number(18,4) | ✓ | 86.57% | 归属母公司股东的净利润同比增长(%)(NPParentCompanyYOY)=（本期归属母公司股东的净利润-上年同期归属... |
| 144 | `NPPCCGrowRate3Y` | 归属母公司股东的净利润3年复合增长率(%) | number(18,4) | ✓ | 68.38% | 归属母公司股东的净利润3年复合增长率(%)(NPPCCGrowRate3Y)：当三年前同期归属母公司股东的净利润为正数时... |
| 145 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长(%) | number(18,4) | ✓ | 44.8% | 归属母公司股东的净利润(扣除)同比增长(%)(NPParentCompanyCutYOY)=（本期扣除非经常性损益后的归... |
| 146 | `NPParentCompanyCut3Y` | 归属母公司股东的净利润(扣除)3年复合增长率(%) | number(18,4) | ✓ | 37.19% | 归属母公司股东的净利润(扣除)3年复合增长率(%)(NPParentCompanyCut3Y)：当三年前同期扣除非经常性... |
| 147 | `AvgNPYOYPastFiveYear` | 过去五年同期归属母公司净利润平均增幅(%) | number(18,4) | ✓ | 44.08% | 过去五年同期归属母公司净利润平均增幅（AvgNPYOYPastFiveYear）：该报告期过去五年的同期的归属母公司净利... |
| 148 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长(%) | number(18,4) | ✓ | 83.28% | 经营活动产生的现金流量净额同比增长(%)(NetOperateCashFlowYOY)=（本期经营活动产生的现金流量净额... |
| 149 | `NetOperateCashFlow3Y` | 经营活动产生的现金流量净额3年复合增长率(%) | number(18,4) | ✓ | 65.48% | 经营活动产生的现金流量净额3年复合增长率(%)(NetOperateCashFlow3Y)：当三年前同期经营活动产生的现... |
| 150 | `OperCashPSGrowRate` | 每股经营活动产生的现金流量净额同比增长(%) | number(18,4) | ✓ | 80.58% | 每股经营活动产生的现金流量净额同比增长(%)(OperCashPSGrowRate)=（本期每股经营活动产生的现金流量净... |
| 151 | `OperCashPSGrowRate3Y` | 每股经营活动产生的现金流量净额3年复合增长率(%) | number(18,4) | ✓ | 63.5% | 每股经营活动产生的现金流量净额3年复合增长率(%)(OperCashPSGrowRate3Y)：当三年前同期每股经营活动... |
| 152 | `NAORYOY` | 净资产收益率(摊薄)同比增长(%) | number(18,4) | ✓ | 81.82% | 净资产收益率(摊薄)同比增长(%)(NAORYOY)=（本期净资产收益率(摊薄)-上年同期净资产收益率(摊薄)）/ABS... |
| 153 | `NAORGrowRate3Y` | 净资产收益率(摊薄)3年复合增长率(%) | number(18,4) | ✓ | 63.65% | 净资产收益率(摊薄)3年复合增长率(%)(NAORGrowRate3Y)：当三年前同期净资产收益率(摊薄)为正数时，净资... |
| 154 | `NetAssetGrowRate` | 净资产同比增长(%) | number(18,4) | ✓ | 81.9% | 净资产同比增长(%)(NetAssetGrowRate)=（本期归属母公司所有者权益(或股东权益)合计-上年同期归属母公... |
| 155 | `NetAssetGrowRate3Y` | 净资产3年复合增长率(%) | number(18,4) | ✓ | 64.72% | 净资产3年复合增长率(%)(NetAssetGrowRate3Y)：当三年前同期归属母公司所有者权益(或股东权益)合计为... |
| 156 | `TotalAssetGrowRate` | 总资产同比增长(%) | number(18,4) | ✓ | 83.22% | 总资产同比增长(%)(TotalAssetGrowRate)=（本期总资产-上年同期总资产）/ABS(上年同期总资产)*... |
| 157 | `TotalAssetGrowRate3Y` | 总资产3年复合增长率(%) | number(18,4) | ✓ | 65.71% | 总资产3年复合增长率(%)(TotalAssetGrowRate3Y)：当三年前同期总资产为正数时，总资产3年复合增长率... |
| 158 | `ToOpCostGrowRate` | 营业总成本同比增长(%) | number(18,4) | ✓ | 85.84% | 营业总成本同比增长(%)(ToOpCostGrowRate)=（本期营业总成本-上年同期营业总成本）/ABS(上年同期营... |
| 159 | `ToLiabGrowRate` | 总负债同比增长(%) | number(18,4) | ✓ | 82.85% | 总负债同比增长(%)(ToLiabGrowRate)=（本期总负债-上年同期总负债）/ABS(上年同期总负债)*100%... |
| 160 | `CashEqIncreaseYOY` | 现金净流量同比增长(%) | number(18,4) | ✓ | 82.79% | 现金净流量同比增长(%)(CashEqIncreaseYOY)=（本期现金及现金等价物净增加额-上年同期现金及现金等价物... |
| 161 | `CashEquivalGrowRate` | 货币资金增长率(%) | number(18,4) | ✓ | 81.54% | 货币资金增长率(%)(CashEquivalGrowRate)=（本期货币资金-上年同期货币资金）/ABS(上年同期货币... |
| 162 | `FAExpansionRate` | 固定资产投资扩张率(%) | number(18,4) | ✓ | 58.59% | 固定资产投资扩张率(%)(FAExpansionRate)=（本期固定资产-上年同期固定资产）/ABS(上年同期固定资产... |
| 163 | `EPSGrowRateYTD` | 每股净资产相对年初增长率(%) | number(18,4) | ✓ | 89.87% | 每股净资产相对年初增长率(%)(EPSGrowRateYTD)=（本期每股净资产-上年度末每股净资产）/ABS(上年度末... |
| 164 | `SEWithoutMIGrowRateYTD` | 归属母公司股东的权益相对年初增长率(%) | number(18,4) | ✓ | 90.17% | 归属母公司股东的权益相对年初增长率(%)(SEWithoutMIGrowRateYTD)=（本期归属母公司股东的权益-上... |
| 165 | `TAGrowRateYTD` | 资产总计相对年初增长率(%) | number(18,4) | ✓ | 91.81% | 资产总计相对年初增长率(%)(TAGrowRateYTD)=（本期末总资产-上年度末总资产）/ABS(上年度末总资产)*... |
| 166 | `SustainableGrowRate` | 可持续增长率(%) | number(18,4) | ✓ | 80.31% | 可持续增长率（SustainableGrowRate）＝（本期净利润/期初归属母公司所有者权益(或股东权益)合计）*本期... |
| 167 | `CapitalStockGrowth` | 股本同比增长数(元) | number(19,4) | ✓ | 81.68% | 股本同比增长数(元)(CapitalStockGrowth)=本期实收资本(或股本)-上年同期实收资本(或股本) |
| 168 | `ARTRGrowRate` | 应收账款周转率增长率(%) | number(18,4) | ✓ | 73.49% | 应收账款周转率增长率(%)（ARTRGrowRate）：（本期应收账款周转率-上年同期应收账款周转率）/ABS(上年同期... |
| 169 | `FATRGrowRate` | 固定资产周转率增长率(%) | number(18,4) | ✓ | 57.96% | 固定资产周转率增长率(%)（FATRGrowRate）：（本期固定资产周转率-上年同期固定资产周转率）/ABS(上年同期... |
| 170 | `InventoryTRGrowRate` | 存货周转率增长率(%) | number(18,4) | ✓ | 73.68% | 存货周转率增长率(%)（InventoryTRGrowRate）：（本期存货周转率-上年同期存货周转率）/ABS(上年同... |
| 171 | `OperCycle` | 营业周期(天/次) | number(18,4) | ✓ | 93.48% | 营业周期（OperCycle）＝存货周转天数+应收账款周转天数，金融类企业不计算。 |
| 172 | `InventoryTRate` | 存货周转率(次) | number(18,4) | ✓ | 84.18% | 存货周转率（InventoryTRate）＝营业成本*2/（期初存货+期末存货），金融类企业不计算。 |
| 173 | `InventoryTDays` | 存货周转天数(天/次) | number(18,4) | ✓ | 84.19% | 存货周转天数（InventoryTDays）=N/存货周转率其中：一季报，N=90；中报，N=180；三季报，N=270... |
| 174 | `ARTRate` | 应收账款周转率(次) | number(18,4) | ✓ | 84.68% | 应收账款周转率（ARTRate）＝营业收入*2/（期初应收账款+期末应收账款），金融类企业不计算。 |
| 175 | `ARTDays` | 应收账款周转天数(天/次) | number(18,4) | ✓ | 83.2% | 应收账款周转天数（ARTDays）＝N/应收账款周转率其中：一季报，N=90；中报，N=180；三季报，N=270；年报... |
| 176 | `AccountsPayablesTRate` | 应付账款周转率(次) | number(18,4) | ✓ | 83.05% | 应付账款周转率（AccountsPayablesTRate）＝营业成本*2/（期初应付账款+期末应付账款），金融类企业不... |
| 177 | `AccountsPayablesTDays` | 应付账款周转天数(天/次) | number(18,4) | ✓ | 83.07% | 应付账款周转天数（AccountsPayablesTDays）=N/应付账款周转率其中：一季报，N=90；中报，N=18... |
| 178 | `WorkingCapitalTurDays` | 营运资金周转天数(天/次) | number(18,4) | ✓ | 85.52% | 营运资金周转天数(天/次)(WorkingCapitalTurDays)=存货周转天数+应收账款周转天数-应付账款周转天... |
| 179 | `CurrentAssetsTRate` | 流动资产周转率(次) | number(18,4) | ✓ | 87.75% | 流动资产周转率（CurrentAssetsTRate）＝营业总收入*2/（期初流动资产合计+期末流动资产合计），金融类企... |
| 180 | `FixedAssetTRate` | 固定资产周转率(次) | number(18,4) | ✓ | 67.05% | 固定资产周转率（FixedAssetTRate）＝营业总收入*2/（期初固定资产合计+期末固定资产合计），金融类企业不计... |
| 181 | `EquityTRate` | 股东权益周转率(次) | number(18,4) | ✓ | 92.1% | 股东权益周转率（EquityTRate）＝营业总收入*2/（期初净资产+期末净资产） |
| 182 | `TotalAssetTRate` | 总资产周转率(次) | number(18,4) | ✓ | 94.58% | 总资产周转率（TotalAssetTRate）＝营业总收入*2/（期初资产合计+期末资产合计） |
| 183 | `TotalAssetTRateTTM` | 总资产周转率_TTM(次) | number(12,4) | ✓ | 94.81% | 总资产周转率_TTM(次)(TotalAssetTRateTTM)=营业总收入(TTM)*2/（上年同期资产合计+期末资... |
| 184 | `NetOperCycle` | 净营业周期(天/次) | number(18,4) | ✓ | 85.61% | 净营业周期(天/次)(NetOperCycle)=存货周转天数+应收账款周转天数-应付账款周转天数,金融类企业不计算。 |
| 185 | `WorkingCaitalTRate` | 营运资本周转率(次) | number(12,4) | ✓ | 74.03% | 营运资本周转率(次)(WorkingCaitalTRate)=营业总收入*2/（期初营运资本+期末营运资本），其中，营运... |
| 186 | `NonCurrentATRate` | 非流动资产周转率(次) | number(12,4) | ✓ | 87.63% | 非流动资产周转率(次)(NonCurrentATRate)=营业总收入*2/（期初非流动资产合计+期末非流动资产合计），... |
| 187 | `SaleServiceCashToOR` | 销售商品提供劳务收到的现金/营业收入(%) | number(18,4) | ✓ | 88.47% | 销售商品提供劳务收到的现金/营业收入(%)(SaleServiceCashToOR):此指标金融类企业不计算。 |
| 188 | `SaleServiceCashToORTTM` | 销售商品提供劳务收到的现金/营业收入_TTM(%) | number(18,4) | ✓ | 90.12% | 销售商品提供劳务收到的现金/营业收入（TTM）=销售商品提供劳务收到的现金（TTM）/营业收入（TTM）*100%，金融... |
| 189 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(18,6) | ✓ | 94.27% | 经营活动产生的现金流量净额/营业收入(%)(CashRateOfSales)=经营活动产生的现金流量净额/营业收入*10... |
| 190 | `CashRateOfSalesTTM` | 经营活动产生的现金流量净额/营业收入_TTM(%) | number(18,4) | ✓ | 96.18% | 经营活动产生的现金流量净额/营业收入（TTM）=经营活动产生的现金流量净额（TTM）/营业收入（TTM）*100%。 |
| 191 | `NOCFToOperatingNI` | 经营活动产生的现金流量净额/经营活动净收益(%) | number(18,4) | ✓ | 68.35% | 经营活动产生的现金流量净额/经营活动净收益(%)(NOCFToOperatingNI)＝经营活动产生的现金流量净额/经营... |
| 192 | `NOCFToOperatingNITTM` | 经营活动产生的现金流量净额/经营活动净收益_TTM(%) | number(18,4) | ✓ | 69.48% | 经营活动产生的现金流量净额/经营活动净收益_TTM(%)(NOCFToOperatingNITTM)=经营活动产生的现金... |
| 193 | `CapitalExpenditureToDM` | 资本支出/折旧和摊销 | number(18,4) | ✓ | 47.55% | 资本支出/折旧和摊销（CapitalExpenditureToDM）=构建固定资产、无形资产和其他长期资产支付的现金/（... |
| 194 | `CashEquivalentIncrease` | 现金及现金等价物净增加额(元) | number(19,4) | ✓ | 94.09% | 现金及现金等价物净增加额(元)(CashEquivalentIncrease)：现金流量表披露值。 |
| 195 | `CashEqGroRate` | 现金及现金等价物增长率(%) | number(18,4) | ✓ | 73.76% | 现金及现金等价物增长率(%)(CashEqGroRate)=（本期期末现金及现金等价物余额-上年同期期末现金及现金等价物... |
| 196 | `NetOperateCashFlow` | 经营活动产生的现金流量净额(元) | number(19,4) | ✓ | 94.95% | 经营活动产生的现金流量净额(元)(NetOperateCashFlow)：现金流量表披露值。 |
| 197 | `GoodsSaleServiceRenderCash` | 销售商品提供劳务收到的现金(元) | number(19,4) | ✓ | 88.68% | 销售商品提供劳务收到的现金(元)(GoodsSaleServiceRenderCash):此指标金融类企业不计算。 |
| 198 | `CashPayStaffRatio` | 支付给职工的现金比率(%) | number(18,4) | ✓ | 88.09% | 支付给职工的现金比率(%)（CashPayStaffRatio）=用于职工的各项现金支出/销售商品出售劳务收回的现金，金... |
| 199 | `FreeCashFlow` | 自由现金流量(元) | number(19,4) | ✓ | 93.48% | 自由现金流量（FreeCashFlow）＝息前税后利润+折旧与摊销-营运资金增加-资本支出。其中，息前税后利润＝息税前利... |
| 200 | `NetProfitCashCover` | 净利润现金含量(%) | number(18,6) | ✓ | 81.52% | 净利润现金含量（NetProfitCashCover）＝经营活动产生的现金流量净额/净利润*100%。 |
| 201 | `OperatingRevenueCashCover` | 营业收入现金含量(%) | number(18,6) | ✓ | 88.47% | 营业收入现金含量（OperatingRevenueCashCover）＝销售商品、提供劳务收到的现金/营业收入*100%... |
| 202 | `OperCashInToAsset` | 总资产现金回收率(%) | number(18,6) | ✓ | 91.45% | 总资产现金回收率（OperCashInToAsset）＝经营活动产生的现金流量净额*2/（期初总资产+期末总资产）*10... |
| 203 | `FreeCashFlowToNPPC` | 自由现金流与归属母公司净利润比率 | number(18,4) | ✓ | 92.56% | 自由现金流与归属母公司净利润比率(FreeCashFlowToNPPC)=企业自由现金流量/归属母公司股东的净利润，其中... |
| 204 | `CashWorkingIndex` | 现金营运指数 | number(18,4) | ✓ | 46.27% | 现金营运指数(CashWorkingIndex)=经营活动产生的现金流量净额／（净利润+资产减值准备+当期计提折旧与摊销... |
| 205 | `NetOperCFToOperProfTTM` | 经营活动产生的现金流量净额/营业利润_TTM(%) | number(18,4) | ✓ | 82.19% | 经营活动产生的现金流量净额/营业利润_TTM(%)(NetOperCFToOperProfTTM)=经营活动产生的现金流... |
| 206 | `NetOperCFRatio` | 经营活动产生的现金流量净额占比 | number(18,4) | ✓ | 48.03% | 经营活动产生的现金流量净额占比(NetOperCFRatio)=经营活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 207 | `NetInvestCFRatio` | 投资活动产生的现金流量净额占比 | number(18,4) | ✓ | 47.39% | 投资活动产生的现金流量净额占比(NetInvestCFRatio)=投资活动产生的现金流量净额/（经营活动产生的现金流量... |
| 208 | `NetFinaCFRatio` | 筹资活动产生的现金流量净额占比 | number(18,4) | ✓ | 46.85% | 筹资活动产生的现金流量净额占比(NetFinaCFRatio)=筹资活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 209 | `FinancingCashGrowRate` | 筹资活动产生的现金流量净额增长率(%) | number(18,4) | ✓ | 80.08% | 筹资活动产生的现金流量净额增长率(%)(FinancingCashGrowRate)=（本期筹资活动产生的现金流量净额-... |
| 210 | `InvestCashGrowRate` | 投资活动产生的现金流量净额增长率(%) | number(18,4) | ✓ | 81.95% | 投资活动产生的现金流量净额增长率(%)(InvestCashGrowRate)=（本期投资活动产生的现金流量净额-上年同... |
| 211 | `NetOperCFToToOperReve` | 经营现金净流量/营业总收入(%) | number(18,4) | ✓ | 94.37% | 经营现金净流量/营业总收入(%)(NetOperCFToToOperReve)=经营活动产生的现金流量净额/营业总收入*... |
| 212 | `NetOperateCashProfit` | 经营活动现金净流量与净利润差(元) | number(19,4) | ✓ | 94.74% | 经营活动现金净流量与净利润差(元)(NetOperateCashProfit)=经营活动产生的现金流量净额-净利润。 |
| 213 | `NetOperCFToToAssets` | 全部资产现金回收率(%) | number(18,4) | ✓ | 91.45% | 全部资产现金回收率(%)(NetOperCFToToAssets)=经营活动产生的现金流量净额/总资产*100%。 |
| 214 | `CashToMeetInvestNeeds` | 现金满足投资比率(%) | number(18,4) | ✓ | 88.75% | 现金满足投资比率(%)（CashToMeetInvestNeeds）=经营活动产生的现金流量净额／（购建固定资产、无形资... |
| 215 | `ExternalFinanceRatio` | 外部融资比率(%) | number(18,4) | ✓ | 88.84% | 外部融资比率(%)（ExternalFinanceRatio）=(经营性应付项目增(减)净额+筹资现金流入量)/现金流入... |
| 216 | `OperCashStability` | 营业现金稳定性 | number(18,4) | ✓ | 48.15% | 营业现金稳定性（OperCashStability）=计提的折旧费用/经营活动产生的现金净流量  |
| 217 | `CashEquivalentPS` | 每股现金及现金等价物余额(元/股) | number(19,4) | ✓ | 83.35% | 每股现金及现金等价物余额（CashEquivalentPS）＝现金及现金等价物期末余额/期末总股本 |
| 218 | `DividendPS` | 每股股利(元/股) | number(19,4) | ✓ | 8.9% | 每股股利（DividendPS）：根据公司公布的分红方案确定。 |
| 219 | `ActualDividendPS` | 每股股利(元/股)(税后) | number(19,4) | ✓ | 8.83% | 每股股利(元/股)(税后)(ActualDividendPS)：公布值，根据公司公布的分红方案确定。 |
| 220 | `DividendCover` | 股利保障倍数(倍) | number(18,6) | ✓ | 8.9% | 股利保障倍数（CashDividendCover）＝归属于母公司的净利润/累计合计派现金额；若“累计派现金额”为0或NU... |
| 221 | `CashDividendCover` | 现金股利保障倍数(倍) | number(18,6) | ✓ | 8.72% | 现金股利保障倍数（CashDividendCover）＝经营活动产生的现金流量净额/累计合计派现金额；若“累计派现金额”... |
| 222 | `DividendPaidRatio` | 股利支付率(%) | number(18,6) | ✓ | 8.8% | 股利支付率（DividendPaidRatio）＝（累计合计派现金额/归属于母公司的净利润）*100% |
| 223 | `RetainedEarningRatio` | 留存盈余比率(%) | number(18,6) | ✓ | 84.18% | 留存盈余比率（RetainedEarningRatio）＝当归属于母公司的净利润>0时，（1-累计合计派现金额/归属于母... |
| 224 | `DividendTTM` | 股息TTM(元) | number(19,4) | ✓ | 29.59% | 股息TTM(元)(DividendTTM)：根据“累计派现合计”计算。 |
| 225 | `Dividend` | 累计派现合计(元) | number(19,4) | ✓ | 8.56% | 累计派现合计(元)(Dividend)：本年年初至本报告期，根据公司公布的分红实施方案，计算累计分红合计； |
| 226 | `DebtAssetsRatio` | 资产负债率(%) | number(18,6) | ✓ | 95.32% | 资产负债率（DebtAssetsRatio）＝负债合计/资产合计*100% |
| 227 | `CurrentAssetsToTA` | 流动资产/总资产(%) | number(18,4) | ✓ | 88.68% | 流动资产／总资产(%)(CurrentAssetsToTA):此指标金融类企业不计算。 |
| 228 | `NonCurrentAssetsToTA` | 非流动资产/总资产(%) | number(18,4) | ✓ | 88.39% | 非流动资产／总资产(%)(NonCurrentAssetsToTA):此指标金融类企业不计算。 |
| 229 | `FixAssetRatio` | 固定资产比率(%) | number(18,6) | ✓ | 71.37% | 固定资产比率(%)(FixAssetRatio)＝固定资产/资产总额*100% |
| 230 | `IntangibleAssetRatio` | 无形资产比率(%) | number(18,6) | ✓ | 87.36% | 无形资产比率(%)(IntangibleAssetRatio)＝无形资产/资产总额*100% |
| 231 | `LongDebtToAsset` | 长期借款/总资产 | number(18,6) | ✓ | 61.78% | 长期借款/总资产(LongDebtToAsset)=长期借款/总资产。 |
| 232 | `BondsPayableToAsset` | 应付债券/总资产 | number(18,6) | ✓ | 35.14% | 应付债券/总资产(BondsPayableToAsset)=应付债券/总资产。 |
| 233 | `NetTangibleAToTA` | 有形资产/总资产(%) | number(12,4) | ✓ | 89.5% | 有形资产/总资产(%)(NetTangibleAToTA)=有形资产净值/总资产*100%，有形资产净值=归属于母公司的... |
| 234 | `SEWithoutMIToTotalCapital` | 归属母公司股东的权益/全部投入资本(%) | number(18,4) | ✓ | 88.18% | 归属母公司股东的权益／全部投入资本（SEWithoutMIToTotalCapital）＝归属母公司股东的权益／全部投入... |
| 235 | `InteBearDebtToTotalCapital` | 带息债务/全部投入资本(%) | number(18,4) | ✓ | 89.04% | 带息债务／全部投入资本（InteBearDebtToTotalCapital）＝带息债务／（股东权益（含少数股东权益）+... |
| 236 | `InteBearDebtToTL` | 带息债务率(%) | number(18,4) | ✓ | 89.23% | 带息债务率(%)(InteBearDebtToTL)=带息债务/负债合计*100%，“带息债务”的计算方法见Tangib... |
| 237 | `CurrentLiabilityToTL` | 流动负债/负债合计(%) | number(18,4) | ✓ | 88.54% | 	 流动负债／负债合计(%)(CurrentLiabilityToTL):该指标金融类企业不计算。 |
| 238 | `NonCurrentLiabilityToTL` | 非流动负债/负债合计(%) | number(18,4) | ✓ | 85.19% | 非流动负债／负债合计(%)(NonCurrentLiabilityToTL):该指标金融类企业不计算。 |
| 239 | `TotalCLiaToSEWMI` | 流动负债权益比率(%) | number(18,4) | ✓ | 87.43% | 流动负债权益比率(%)(TotalCLiaToSEWMI)=流动负债合计/归属于母公司股东的权益合计*100%,金融类企... |
| 240 | `TotalNonCLiaToSEWMI` | 非流动负债权益比率(%) | number(18,4) | ✓ | 84.16% | 非流动负债权益比率(%)(TotalNonCLiaToSEWMI)=非流动负债合计/归属于母公司股东的权益合计*100%... |
| 241 | `DebtARatioCutADRecp` | 剔除预收账款后的资产负债率(%) | number(12,4) | ✓ | 95.32% | 剔除预收账款后的资产负债率(%)(DebtARatioCutADRecp)=(负债合计-预收款项-合同负债)／(资产总额... |
| 242 | `DebtARatioCutADReNo` | 剔除预收账款后的资产负债率_公告口径(%) | number(12,4) | ✓ | 95.32% | 剔除预收账款后的资产负债率_公告口径(%)(DebtARatioCutADReNo)=(负债合计-预收款项-合同负债)／... |
| 243 | `EquityToAsset` | 股东权益比率(%) | number(18,6) | ✓ | 95.55% | 股东权益比率(%)(EquityToAsset)＝股东权益合计/资产合计*100% |
| 244 | `EquityMultipler` | 权益乘数 | number(18,6) | ✓ | 94.71% | 权益乘数（EquityMultipler）＝资产合计/股东权益合计 |
| 245 | `WorkingCapital` | 营运资金(元) | number(19,4) | ✓ | 93.48% | 营运资金（WorkingCapital）＝流动资产合计-流动负债合计，金融类企业不计算。 |
| 246 | `LongDebtToEquity` | 长期负债/股东权益合计 | number(18,6) | ✓ | 84.48% | 长期负债/股东权益合计(LongDebtToEquity)=非流动负债合计/所有者权益(或股东权益)合计，该指标金融类企... |
| 247 | `LongAssetFitRate` | 长期资产适合率 | number(18,6) | ✓ | 67.71% | 长期资产适合率（LongAssetFitRate）＝（所有者权益+长期负债）/（固定资产净值+长期股权投资+可供出售金融... |
| 248 | `TotalNonCurLiaToSEWMI` | 长期资本负债率(%) | number(18,4) | ✓ | 84.45% | 长期资本负债率(%)(TotalNonCurLiaToSEWMI)=非流动负债合计／（非流动负债合计+归属母公司所有者权... |
| 249 | `TotalNonCurAToSEWMI` | 资本固定化比率(%) | number(18,4) | ✓ | 87.21% | 资本固定化比率(%)(TotalNonCurAToSEWMI)=非流动资产合计／归属母公司所有者权益(或股东权益)合计*... |
| 250 | `EquityFixedAssetRatio` | 股东权益与固定资产比率(%) | number(18,4) | ✓ | 71.32% | 股东权益与固定资产比率(%)(EquityFixedAssetRatio)=股东权益合计（含少数股东权益）/固定资产*1... |
| 251 | `FinancialLeverage` | 财务杠杆效率 | number(18,4) | ✓ | 87.62% | 财务杠杆效率（FinancialLeverage）=净资产收益率/资产报酬率，金融企业不计算。 |
| 252 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(18,4) | ✓ | 86.2% | 经营活动净收益／利润总额（OperatingNIToTP）＝经营活动净收益／利润总额*100%，“经营活动净收益”的计算... |
| 253 | `OperatingMIToTPTTM` | 经营活动净收益/利润总额_TTM(%) | number(18,4) | ✓ | 88.02% | 经营活动净收益／利润总额_TTM（OperatingNIToTPTTM）＝经营活动净收益(TTM)／利润总额(TTM)*... |
| 254 | `InvestRAssociatesToTP` | 对联营合营公司投资收益/利润总额(%) | number(18,4) | ✓ | 30.47% | 对联营合营公司投资收益/利润总额(%)(InvestRAssociatesToTP)=对联营合营公司投资收益/利润总额*... |
| 255 | `InvestRAssociatesToTPTTM` | 对联营合营公司投资收益/利润总额_TTM(%) | number(18,4) | ✓ | 41.71% | 对联营合营公司投资收益/利润总额_TTM(%)(InvestRAssociatesToTPTTM)=对联营合营公司投资收... |
| 256 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(18,4) | ✓ | 86.25% | 价值变动净收益／利润总额（ValueChangeNIToTP）＝价值变动净收益／利润总额*100%其中，价值变动净收益=... |
| 257 | `ValueChangeNIToTPTTM` | 价值变动净收益/利润总额_TTM(%) | number(18,4) | ✓ | 88.23% | 价值变动净收益／利润总额_TTM（ValueChangeNIToTPTTM）＝价值变动净收益(TTM)／利润总额(TTM... |
| 258 | `NetNonOperatingIncomeToTP` | 营业外收支净额/利润总额(%) | number(18,4) | ✓ | 86.25% | 营业外收支净额／利润总额（NetNonOperatingIncomeToTP）＝(营业外收入-营业外支出)/利润总额*1... |
| 259 | `NetNonOIToTPTTM` | 营业外收支净额/利润总额_TTM(%) | number(18,4) | ✓ | 88.23% | 营业外收支净额／利润总额_TTM（EquityMultipler）＝营业外收支净额(TTM)/利润总额(TTM)*100... |
| 260 | `TaxesToTP` | 所得税/利润总额(%) | number(18,4) | ✓ | 81.96% | 所得税/利润总额(%)(TaxesToTP)=所得税/利润总额*100%。 |
| 261 | `NPCutToTP` | 扣除非经常损益后的归母净利润/净利润(%) | number(18,4) | ✓ | 43.51% | 扣除非经常损益后的净利润／净利润（NPCutToTP）＝扣除非经常损益后的净利润／净利润*100%其中，“扣除非经常损益... |
| 262 | `ToProfToOperProfitTTM` | 营业利润/利润总额_TTM(%) | number(18,4) | ✓ | 94.63% | 营业利润/利润总额_TTM(%)(ToProfToOperProfitTTM)=营业利润(TTM)/利润总额(TTM)*... |
| 263 | `ToProfToOperRevenueTTM` | 利润总额/营业收入_TTM(%) | number(18,4) | ✓ | 98.43% | 利润总额/营业收入_TTM(%)(ToProfToOperRevenueTTM)=利润总额(TTM)/营业收入(TTM)... |
| 264 | `EquityMultipler_DuPont` | 权益乘数_杜邦分析 | number(18,4) | ✓ | 92.97% | 权益乘数_杜邦分析（EquityMultipler_DuPont）＝（期初资产总额+期末资产总额）/（期初归属于母公司股... |
| 265 | `NPPCToNP_DuPont` | 归属母公司股东的净利润/净利润(%)_杜邦分析 | number(18,4) | ✓ | 98.03% | 归属母公司股东的净利润/净利润(%)(NPPCToNP_DuPont)=归属母公司股东的净利润/净利润*100%。 |
| 266 | `NPToTOR_DuPont` | 净利润/营业总收入_杜邦分析(%) | number(18,4) | ✓ | 92.09% | 净利润/营业总收入(%)(NPToTOR_DuPont)=净利润/营业总收入*100，该指标金融类企业不计算。 |
| 267 | `NPToTP_DuPont` | 净利润/利润总额_杜邦分析(%) | number(18,4) | ✓ | 86.03% | 净利润/利润总额(%)(NPToTP_DuPont)=净利润/利润总额*100%。 |
| 268 | `TPToEBIT_DuPont` | 利润总额/息税前利润_杜邦分析(%) | number(18,4) | ✓ | 83.03% | 利润总额/息税前利润(%)(TPToEBIT_DuPont)=利润总额/息税前利润*100%，“息税前利润”计算方法见E... |
| 269 | `EBITToTOR_DuPont` | 息税前利润/营业总收入_杜邦分析(%) | number(18,4) | ✓ | 92.36% | 息税前利润/营业总收入(%)(EBITToTOR_DuPont):该指标金融类企业不计算。 |
| 270 | `DebtEquityRatio_DuPont` | 产权比率_杜邦分析(%) | number(18,4) | ✓ | 92.84% | 产权比率_杜邦分析(%)(DebtEquityRatio_DuPont)=（期初负债合计+期末负债合计）/（期初归属母公... |
| 271 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 272 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 273 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoPublDate (信息发布日期)

信息发布日期(InfoPublDate)：本表是基于三大表数据进行衍生计算，当多表关联计算时，因各表信息发布日期会存在不一致的情况，则取截止日期对应的本期维度最大信息发布日期赋值本字段。

### BasicEPS (基本每股收益(元/股))

基本每股收益（BasicEPS）：新会计准则下，取公司的实际披露数；旧会计准则下，取公司披露的每股收益（加权）。

### DilutedEPS (稀释每股收益(元/股))

稀释每股收益（DilutedEPS）：新会计准则下，取公司的实际披露数；旧会计准则下，稀释每股收益=归属于母公司的净利润（扣除已确认为费用的稀释性股权费用）/∑（发行在外普通股股数*发行在外月份数+稀释性潜在普通股*12）/12。

### EPS (每股收益_期末股本摊薄(元/股))

每股收益_期末股本摊薄（EPS）： 每股收益_期末股本摊薄=归属于母公司的净利润/该报告期末总股本。

### EPSCut (基本每股收益(扣除)(元/股))

每股收益(扣除)(元/股)（EPSCut）：优先取原文披露值，原文若未披露，则通过计算赋值：每股收益(扣除)＝扣除后的净利润/期末股本

### EPSTTM (每股收益_TTM(元/股))

每股收益_TTM（EPSTTM）=归属于母公司的净利润（TTM）/期末总股本

### NetAssetPS (每股净资产(元/股))

每股净资产（NetAssetPS）：直接取公司定期报告披露数据；若无披露，则，每股净资产=（归属于母公司的所有者权益-其他权益工具）/期末总股本。

### NetAssetPSAdjusted (调整后每股净资产(元/股))

调整后每股净资产(元/股)（NetAssetPSAdjusted）：取原文披露值

### TotalOperatingRevenuePS (每股营业总收入(元/股))

每股营业总收入（TotalOperatingRevenuePS）＝营业总收入/该报告期期末总股本

## SQL示例

```sql
-- 查询 公司主要财务分析指标_新会计准则 数据
SELECT *
FROM lc_mainindexnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
