# LC_STIBMainIndex

**中文名**: 科创板主要财务分析指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBMainIndex` |
| MySQL表名 | `lc_stibmainindex` |
| 中文名 | 科创板主要财务分析指标 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 财务衍生 |
| 更新频率 | 季更新 |
| 字段数量 | 227 |
| 版本 | 1.01 |

## 表描述

1.内容说明：
1.1 由上市公司的主要会计科目（合并报表）衍生出来的数据，若三大财务报表中任意报表在某报告期的数据经历调整/修订，则该表相关字段展示每个历史调整数据；未经历调整/修订的报表相关字段则沿用未调整数据。
1.2 根据报告期公布的财务科目数据衍生而来的每股指标，以及反映公司盈利、偿债、成长、营运、分红、现金流、资本结构等能力的指标。
1.3 “十、杜邦分析”另有两个指标“净资产收益率ROE_平均,计算”和“总资产周转率”，分别在“二、盈利能力”和“五、营运能力”下。
1.4 本表中的同比数据计算公式为：（本期数据－去年同期数据）/︱去年同期数据︱*100。
1.5 本表比率类指标（字段后有%）展示数据有进行百分化处理（计算过程中*100）。
1.6 针对CDR证券，权益分派单位均为“股”，表内每股类等指标按照股数展示。
2.数据范围：科创板上市至今
3.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181，... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并（IfMerged）固定常量：1-合并，2-母公司 |
| 7 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 8 | `BasicEPS` | 基本每股收益(元/股) | number(19,4) | ✓ | 90.93% | 基本每股收益(元/股)(BasicEPS)：直取公司的实际披露数； |
| 9 | `DilutedEPS` | 稀释每股收益(元/股) | number(19,4) | ✓ | 87.74% | 稀释每股收益(元/股)(DilutedEPS)：直取公司的实际披露数； |
| 10 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(19,4) | ✓ | 98.96% | 每股收益_期末股本摊薄(元/股)(EPS)： 每股收益_期末股本摊薄=归属于母公司的净利润/该报告期末总股本。 |
| 11 | `EPSTTM` | 每股收益_TTM(元/股) | number(19,4) | ✓ | 99.04% | 每股收益_TTM(元/股)(EPSTTM)=归属于母公司的净利润（TTM）/期末总股本 |
| 12 | `NetAssetPS` | 每股净资产(元/股) | number(19,4) | ✓ | 95.74% | 每股净资产(元/股)(NetAssetPS)：直接取公司定期报告披露数据；若无披露，则，每股净资产=（归属于母公司的所有... |
| 13 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(19,4) | ✓ | 99.04% | 每股营业总收入(元/股)(TotalOperateRevenuePS)＝营业总收入/该报告期期末总股本 |
| 14 | `MainIncomePS` | 每股营业收入(元/股) | number(19,4) | ✓ | 98.91% | 每股营业收入(元/股)(MainIncomePS)＝营业收入/该报告期期末总股本 |
| 15 | `OperatingRevenuePSTTM` | 每股营业收入_TTM(元/股) | number(19,4) | ✓ | 98.97% | 每股营业收入_TTM(元/股)(OperatingRevenuePSTTM)＝营业收入（TTM）/期末总股本 |
| 16 | `OperProfitPS` | 每股营业利润(元/股) | number(19,4) | ✓ | 98.81% | 每股营业利润(元/股)(OperProfitPS)＝营业利润/期末总股本 |
| 17 | `EBITPS` | 每股息税前利润(元/股) | number(19,4) | ✓ | 99.09% | 每股息税前利润(元/股)(EBITPS)＝息税前利润/期末总股本；“息税前利润”计算方法见EBIT[息税前利润(元)]；... |
| 18 | `EBITDAPS` | 每股息税折旧前利润(元/股) | number(19,4) | ✓ | 99.09% | 每股息税折旧前利润(元/股)(EBITDAPS)＝息税折旧摊销前利润/期末总股本；“息税折旧摊销前利润”计算方法见EBI... |
| 19 | `CapitalSurplusFundPS` | 每股资本公积金(元/股) | number(19,4) | ✓ | 92.54% | 每股资本公积金(元/股)(CapitalSurplusFundPS)＝资本公积/期末总股本 |
| 20 | `SurplusReserveFundPS` | 每股盈余公积(元/股) | number(19,4) | ✓ | 83.0% | 每股盈余公积(元/股)(SurplusReserveFundPS)＝盈余公积/期末总股本 |
| 21 | `AccumulationFundPS` | 每股公积金(元/股) | number(19,4) | ✓ | 99.09% | 每股公积金(元/股)(AccumulationFundPS)＝（资本公积金+盈余公积金）/期末总股本 |
| 22 | `UndividedProfit` | 每股未分配利润(元/股) | number(19,4) | ✓ | 93.43% | 每股未分配利润(元/股)(UndividedProfit)＝未分配利润/期末总股本 |
| 23 | `RetainedEarningsPS` | 每股留存收益(元/股) | number(19,4) | ✓ | 99.09% | 每股留存收益(元/股)(RetainedEarningsPS)＝（盈余公积+未分配利润）/期末总股本 |
| 24 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 98.87% | 每股经营活动产生的现金流量净额(元/股)(OperCashFlowPS)：经营活动产生的现金流量净额/期末总股本。 |
| 25 | `OperCashFlowPSTTM` | 每股经营活动产生的现金流量净额_TTM(元/股) | number(19,4) | ✓ | 99.03% | 每股经营活动产生的现金流量净额_TTM(元/股)(OperCashFlowPSTTM)=经营活动产生的现金流量净额（TT... |
| 26 | `CashFlowPS` | 每股现金流量净额(元/股) | number(19,4) | ✓ | 97.57% | 每股现金流量净额(元/股)(CashFlowPS)=现金及现金等价物净增加额/期末总股本 |
| 27 | `CashFlowPSTTM` | 每股现金流量净额_TTM(元/股) | number(19,4) | ✓ | 98.86% | 每股现金流量净额_TTM(元/股)(CashFlowPSTTM)=现金及现金等价物净增加额（TTM）/期末总股本 |
| 28 | `EnterpriseFCFPS` | 每股企业自由现金流量(元/股) | number(19,4) | ✓ | 99.09% | 每股企业自由现金流量(元/股)(EnterpriseFCFPS)=企业自由现金流量/期末总股本。企业自由现金流量（Fre... |
| 29 | `ShareHolderFCFPS` | 每股股东自由现金流量(元/股) | number(19,4) | ✓ | 99.09% | 每股股东自由现金流量(元/股)(ShareHolderFCFPS)=[企业自由现金流量-偿还债务所支付的现金+取得借款收... |
| 30 | `ROEAvg` | 净资产收益率_平均,计算值(%) | number(12,4) | ✓ | 95.12% | 净资产收益率_平均,计算值(%)(ROEAvg)=（归属于母公司的净利润*2/（期初归属于母公司的股东权益+期末归属于母... |
| 31 | `ROEWeighted` | 净资产收益率_加权,公布值(%) | number(12,4) | ✓ | 85.57% | 净资产收益率_加权,公布值(%)(ROEWeighted)：为公司定期报告披露数据。 |
| 32 | `ROE` | 净资产收益率_摊薄,公布值(%) | number(12,4) | ✓ | 95.13% | 净资产收益率_摊薄,公布值(%)(ROE)：直接取公司定期报告披露数据；若无披露值，则ROE（摊薄）=归属于母公司的净利... |
| 33 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(12,4) | ✓ | 86.75% | 净资产收益率_扣除,摊薄(%)(ROECut)：直接取公司定期报告披露数据；若无披露值，则ROE（摊薄）=扣除非经常性损... |
| 34 | `ROECutWeighted` | 净资产收益率_扣除,加权(%) | number(12,4) | ✓ | 66.64% | 净资产收益率_扣除,加权(%)(ROECutWeighted)：直接取公司定期报告披露数据。 |
| 35 | `ROETTM` | 净资产收益率_TTM(%) | number(12,4) | ✓ | 95.16% | 净资产收益率_TTM(%)(ROETTM)＝（归属于母公司的净利润（TTM）/期末归属于母公司的股东权益*100 |
| 36 | `AnnualizedROE` | 年化净资产收益率(%) | number(12,4) | ✓ | 94.95% | 年化净资产收益率(%)(AnnualizedROE)：根据“净资产收益率*N”计算，一季报N=4，二季报N=2，三季报N... |
| 37 | `ROA_EBIT` | 总资产报酬率(%) | number(12,4) | ✓ | 96.51% | 总资产报酬率(%)(ROA_EBIT)＝息税前利润*2/（期初总资产+期末总资产）*100 ，其中，“息税前利润”计算方... |
| 38 | `ROA_EBITTTM` | 总资产报酬率_TTM(%) | number(12,4) | ✓ | 96.45% | 总资产报酬率_TTM(%)(ROA_EBITTTM)＝息税前利润（TTM）/总资产（MRQ）*100； 其中，息税前利润... |
| 39 | `AnnualizedROAEBIT` | 年化总资产报酬率(%) | number(12,4) | ✓ | 96.34% | 年化总资产报酬率(%)(AnnualizedROAEBIT)：根据“总资产报酬率*N”计算，一季报N=4，二季报N=2，... |
| 40 | `ROA` | 总资产净利率(%) | number(12,4) | ✓ | 96.35% | 总资产净利率(%)(ROA)＝含少数股东损益的净利润*2/（期初总资产+期末总资产）*100 |
| 41 | `ROATTM` | 总资产净利率_TTM(%) | number(12,4) | ✓ | 96.44% | 总资产净利率_TTM(%)(ROATTM)＝含少数股东损益的净利润（TTM）/总资产（MRQ）*100 |
| 42 | `AnnualizedROA` | 年化总资产净利率(%) | number(12,4) | ✓ | 96.18% | 年化总资产净利率(%)(AnnualizedROA)：根据“总资产净利率*N”计算，一季报N=4，二季报N=2，三季报N... |
| 43 | `ROACutTTM` | 总资产净利率_不含少数股东损益_TTM(%) | number(12,4) | ✓ | 96.46% | 总资产净利率_不含少数股东损益_TTM(%)(ROACutTTM)＝归属于母公司的净利润（TTM）/总资产 *100 |
| 44 | `ROIC` | 投入资本回报率(%) | number(12,4) | ✓ | 99.66% | 投入资本回报率(%)(ROIC)=（息税前利润*（1-有效税率）*2/（期初全部投入资本+期末全部投入资本））*100。... |
| 45 | `ROICTTM` | 投入资本回报率_TTM(%) | number(12,4) | ✓ | 96.41% | 投入资本回报率_TTM(%)(ROICTTM)=EBIT*(1-有效税率)TTM／全部投入资本*100；金融类企业不计算 |
| 46 | `NetProfitRatio` | 销售净利率(%) | number(12,4) | ✓ | 99.11% | 销售净利率(%)(NetProfitRatio)＝含少数股东损益的净利润/营业收入*100 |
| 47 | `NetProfitRatioTTM` | 销售净利率_TTM(%) | number(12,4) | ✓ | 99.38% | 销售净利率_TTM(%)(NetProfitRatioTTM)＝含少数股东损益的净利润（TTM）/营业收入（TTM）*1... |
| 48 | `GrossIncomeRatio` | 销售毛利率(%) | number(12,4) | ✓ | 96.14% | 销售毛利率(%)(GrossIncomeRatio)＝（营业收入-营业成本）/营业收入*100%，金融类企业不计算。 |
| 49 | `GrossIncomeRatioTTM` | 销售毛利率_TTM(%) | number(12,4) | ✓ | 98.96% | 销售毛利率_TTM(%)(GrossIncomeRatioTTM)＝[营业收入（TTM）-营业成本（TTM）]/营业收入... |
| 50 | `SalesCostRatio` | 销售成本率(%) | number(12,4) | ✓ | 96.14% | 销售成本率(%)(SalesCostRatio)＝营业成本/营业收入*100，金融类企业不计算。 |
| 51 | `PeriodCostsRate` | 销售期间费用率(%) | number(12,4) | ✓ | 99.33% | 销售期间费用率(%)(PeriodCostsRate)＝（销售费用+管理费用+财务费用+研发费用）/营业收入*100，金... |
| 52 | `PeriodCostsRateTTM` | 销售期间费用率_TTM(%) | number(12,4) | ✓ | 91.25% | 销售期间费用率_TTM(%)(PeriodCostsRateTTM)＝[销售费用（TTM）+管理费用（TTM）+财务费用... |
| 53 | `NPToTOR` | 净利润/营业总收入(%) | number(12,4) | ✓ | 99.14% | 净利润/营业总收入(%)(NPToTOR)：非金融类公司计算公式=净利润/营业总收入*100；金融类公司计算公式=净利润... |
| 54 | `NPToTORTTM` | 净利润/营业总收入_TTM(%) | number(12,4) | ✓ | 99.37% | 净利润/营业总收入_TTM(%)(NPToTORTTM)：非金融类公司计算公式=净利润（TTM）/营业总收入（TTM）*... |
| 55 | `OperatingProfitToTOR` | 营业利润/营业总收入(%) | number(12,4) | ✓ | 99.08% | 营业利润/营业总收入(%)(OperatingProfitToTOR)：非金融类公司计算公式=营业利润/营业总收入*10... |
| 56 | `OperatProfitToTORTTM` | 营业利润/营业总收入_TTM(%) | number(12,4) | ✓ | 99.38% | 营业利润/营业总收入_TTM(%)(OperatProfitToTORTTM)：非金融类公司计算公式=营业利润（TTM）... |
| 57 | `EBITToTOR` | 息税前利润/营业总收入(%) | number(12,4) | ✓ | 99.35% | 息税前利润/营业总收入(%)(EBITToTOR)：此指标金融类企业不计算。 |
| 58 | `EBITToTORTTM` | 息税前利润/营业总收入_TTM(%) | number(12,4) | ✓ | 99.38% | 息税前利润/营业总收入_TTM(%)(EBITToTORTTM)＝息税前利润(TTM)/营业总收入(TTM)*100，金... |
| 59 | `TOperatingCostToTOR` | 营业总成本/营业总收入(%) | number(12,4) | ✓ | 95.71% | 营业总成本/营业总收入(%)(TOperatingCostToTOR):此指标金融类企业不计算。 |
| 60 | `TOperatingCostToTORTTM` | 营业总成本/营业总收入_TTM(%) | number(12,4) | ✓ | 99.03% | 营业总成本/营业总收入_TTM(%)(TOperatingCostToTORTTM)＝营业总成本（TTM）/营业总收入（... |
| 61 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(12,4) | ✓ | 95.16% | 销售费用/营业总收入(%)(OperatingExpenseRate):此指标金融类企业不计算。 |
| 62 | `OperatExpenseRateTTM` | 销售费用/营业总收入_TTM(%) | number(12,4) | ✓ | 98.19% | 销售费用/营业总收入_TTM(%)(OperatExpenseRateTTM)＝销售费用（TTM）/营业总收入（TTM）... |
| 63 | `AdminiExpenseRate` | 管理费用/营业总收入(%) | number(12,4) | ✓ | 95.84% | 管理费用/营业总收入(%)(AdminiExpenseRate):此指标金融类企业不计算。 |
| 64 | `AdminiExpenseRateTTM` | 管理费用/营业总收入_TTM(%) | number(12,4) | ✓ | 99.03% | 管理费用/营业总收入_TTM(%)(AdminiExpenseRateTTM)＝管理费用（TTM）／营业总收入（TTM）... |
| 65 | `FinancialExpenseRate` | 财务费用/营业总收入(%) | number(12,4) | ✓ | 95.77% | 财务费用/营业总收入(%)(FinancialExpenseRate):此指标金融类企业不计算。 |
| 66 | `FinanceExpenseRateTTM` | 财务费用/营业总收入_TTM(%) | number(12,4) | ✓ | 99.03% | 财务费用/营业总收入_TTM(%)(FinanceExpenseRateTTM)＝财务费用（TTM）／营业总收入（TTM... |
| 67 | `AssetImpaLossToTOR` | 资产减值损失/营业总收入(%) | number(12,4) | ✓ | 80.85% | 资产减值损失/营业总收入(%)(AssetImpaLossToTOR)：非金融类公司计算公式=资产减值损失/营业总收入*... |
| 68 | `AssetImpaLossToTORTTM` | 资产减值损失/营业总收入_TTM(%) | number(12,4) | ✓ | 87.23% | 资产减值损失/营业总收入_TTM(%)(AssetImpaLossToTORTTM)：非金融类公司计算公式=资产减值损失... |
| 69 | `AssetILossToOProfit` | 资产减值损失/营业利润(%) | number(12,4) | ✓ | 65.19% | 资产减值损失/营业利润(%)(AssetILossToOProfit)=资产减值损失/营业利润*100%。 |
| 70 | `NPParentCompanyOwners` | 归属母公司净利润(元) | number(19,4) | ✓ | 99.83% | 归属母公司净利润(元)(NPParentCompanyOwners)：取公布值。 |
| 71 | `NetProfToOpRevenTTM` | 归属母公司股东的净利润/营业收入_TTM(%) | number(12,4) | ✓ | 99.39% | 归属母公司股东的净利润/营业收入_TTM(%)(NetProfToOpRevenTTM)=归属母公司股东的净利润（TTM... |
| 72 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(元) | number(19,4) | ✓ | 88.55% | 扣除非经常性损益后的归母净利润(元)(NetProfitCut)：取公布值。 |
| 73 | `EBIT` | 息税前利润(元) | number(19,4) | ✓ | 100.0% | 息税前利润(元)(EBIT)＝利润总额＋利息费用  其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用=其中... |
| 74 | `EBITDA` | 息税折旧摊销前利润(元) | number(19,4) | ✓ | 100.0% | 息税折旧摊销前利润(元)(EBITDA)＝息税前利润EBIT+固定资产折旧+投资性房地产折旧+无形资产摊销+长期待摊费用... |
| 75 | `EBITToToAssetsTTM` | 息税前利润/总资产_TTM(%) | number(12,4) | ✓ | 96.45% | 息税前利润/总资产_TTM(%)(EBITToToAssetsTTM)=息税前利润(TTM)/资产总额*100%,金融类... |
| 76 | `EBITDAToTOR` | 息税折旧前利润/营业总收入(%) | number(12,4) | ✓ | 99.35% | 息税折旧前利润/营业总收入(%)(EBITDAToTOR)=息税折旧前利润/营业总收入*100%,金融类企业不计算。 |
| 77 | `OperatingProfitMargin` | 营业利润率(%) | number(12,4) | ✓ | 99.05% | 营业利润率(%)(OperatingProfitMargin)＝营业利润/营业收入*100% |
| 78 | `OperatingProRatioTTM` | 营业利润率_TTM(%) | number(12,4) | ✓ | 99.38% | 营业利润率_TTM(%)(OperatingProRatioTTM)=营业利润（TTM）／营业收入（TTM）*100%。 |
| 79 | `TotalProfitCostRatio` | 成本费用利润率(%) | number(12,4) | ✓ | 96.83% | 成本费用利润率(%)(TotalProfitCostRatio)＝利润总额/成本费用总额*100%其中，成本费用总额＝营... |
| 80 | `MainProfitProportion` | 主营业务比率(%) | number(12,4) | ✓ | 98.94% | 主营业务比率(%)(MainProfitProportion)=营业利润／利润总额*100%。 |
| 81 | `CurrentRatio` | 流动比率 | number(18,4) | ✓ | 93.76% | 流动比率(CurrentRatio)=流动资产合计/流动负债合计。 |
| 82 | `QuickRatio` | 速动比率 | number(18,4) | ✓ | 93.76% | 速动比率(QuickRatio)=（流动资产合计-存货）/流动负债合计 |
| 83 | `SuperQuickRatio` | 超速动比率 | number(18,4) | ✓ | 93.76% | 超速动比率（SuperQuickRatio）＝（货币资金+交易性金融资产+应收票据及应收账款+其他应收款（含利息和股利）... |
| 84 | `DebtEquityRatio` | 产权比率(%) | number(18,4) | ✓ | 95.53% | 产权比率(%)(DebtEquityRatio) ＝负债合计／所有者权益(或股东权益)合计*100% |
| 85 | `SEWithoutMIToTL` | 归属母公司股东的权益/负债合计(%) | number(18,4) | ✓ | 95.49% | 归属母公司股东的权益/负债合计(%)(SEWithoutMIToTL)=归属母公司股东的权益/负债合计*100%。 |
| 86 | `SEWToInterestBearDebt` | 归属母公司股东的权益/带息债务(%) | number(18,4) | ✓ | 83.05% | 归属母公司股东的权益/带息债务(%)(SEWToInterestBearDebt)＝归属母公司股东的权益／（负债合计-无... |
| 87 | `DebtTangibEquityRatio` | 有形净值债务率(%) | number(18,4) | ✓ | 95.5% | 有形净值债务率(%)(DebtTangibEquityRatio)＝负债合计／有形净值*100%其中，有形净值=归属于母... |
| 88 | `TangibleAToTL` | 有形资产/负债合计(%) | number(18,4) | ✓ | 96.09% | 有形资产/负债合计(%)(TangibleAToTL)=有形资产净值/负债合计*100%，其中，有形净值=归属于母公司的... |
| 89 | `TangibAToInteBearDebt` | 有形净值/带息债务(%) | number(18,4) | ✓ | 83.65% | 有形净值/带息债务(%)(TangibAToInteBearDebt)＝有形净值／带息债务*100%其中，有形净值=归属... |
| 90 | `TangibleAToNetDebt` | 有形净值/净债务(%) | number(18,4) | ✓ | 24.74% | 有形净值/净债务(%)(TangibleAToNetDebt)＝（有形净值／净债务）*100%其中，有形净值=归属于母公... |
| 91 | `EBITDAToTLiability` | 息税折旧摊销前利润/负债合计 | number(18,4) | ✓ | 96.09% | 息税折旧摊销前利润/负债合计(EBITDAToTLiability)=息税折旧摊销前利润/负债合计，“息税折旧摊销前利润... |
| 92 | `NOCFToTLiability` | 经营活动产生现金流量净额/负债合计 | number(18,4) | ✓ | 95.97% | 经营活动产生现金流量净额/负债合计(NOCFToTLiability)=经营活动产生现金流量净额/负债合计，此指标金融类... |
| 93 | `NOCFToInterestBearDebt` | 经营活动产生现金流量净额/带息债务 | number(18,4) | ✓ | 83.53% | 经营活动产生现金流量净额/带息债务(NOCFToInterestBearDebt)=经营活动产生现金流量净额/带息债务，... |
| 94 | `NOCFToCurrentLiability` | 经营活动产生现金流量净额/流动负债 | number(18,4) | ✓ | 93.71% | 经营活动产生现金流量净额/流动负债(NOCFToCurrentLiability)=经营活动产生现金流量净额/流动负债，... |
| 95 | `NOCFToNetDebt` | 经营活动产生现金流量净额/净债务 | number(18,4) | ✓ | 24.65% | 经营活动产生现金流量净额/净债务(NOCFToNetDebt)=经营活动产生现金流量净额/净债务。“净债务”算法见Tan... |
| 96 | `NOCFToTotalNonCurLia` | 经营活动产生现金流量净额/非流动负债(%) | number(18,4) | ✓ | 89.6% | 经营活动产生现金流量净额/非流动负债(%)(NOCFToTotalNonCurLia)=经营活动产生现金流量净额/非流动... |
| 97 | `InterestCover` | 利息保障倍数(倍) | number(18,4) | ✓ | 45.67% | 利息保障倍数(倍)(InterestCover)＝息税前利润/利息费用。其中，“息税前利润”计算方法见EBIT[息税前利... |
| 98 | `NOCFInterestCover` | 现金流量利息保障倍数(倍) | number(18,4) | ✓ | 45.67% | 现金流量利息保障倍数(倍)(NOCFInterestCover)=经营活动产生现金流量净额/利息费用，其中，利息费用=利... |
| 99 | `LongDebtToWorkCapital` | 长期负债与营运资金比率 | number(18,4) | ✓ | 86.05% | 长期负债与营运资金比率(LongDebtToWorkCapital)＝长期负债/（流动资产-流动负债），金融类企业不计算... |
| 100 | `OperCashToCurrentDebt` | 现金流动负债比 | number(18,4) | ✓ | 93.71% | 现金流动负债比(OperCashToCurrentDebt)＝经营现金净流入/流动负债，金融类企业不计算。 |
| 101 | `CashRatio` | 现金比率(%) | number(18,4) | ✓ | 93.76% | 现金比率(%)(CashRatio)=（货币资金+交易性金融资产+应收票据)/非流动负债总计*100%,金融类企业不计算... |
| 102 | `OperCashInToDueDebt` | 现金到期债务比 | number(18,4) | ✓ | 82.8% | 现金到期债务比(OperCashInToDueDebt)=经营活动产生的现金流量净额／（短期借款+一年内到期的非流动负债... |
| 103 | `NetAssetLiabilityRatio` | 净资产负债率(%) | number(18,4) | ✓ | 95.49% | 净资产负债率(%)(NetAssetLiabilityRatio)=负债合计/归属母公司所有者权益(或股东权益)合计*1... |
| 104 | `NetLiabilityRatio` | 净负债率(%) | number(18,4) | ✓ | 95.86% | 净负债率(%)(NetLiabilityRatio)=（带息债务-货币资金）/所有者权益*100%；“带息债务”算法见T... |
| 105 | `NetNoFCFToCLiability` | 非筹资性现金净流量与流动负债的比率(%) | number(18,4) | ✓ | 93.76% | 非筹资性现金净流量与流动负债的比率(%)(NetNoFCFToCLiability)=（经营活动产生的现金流量净额+投资... |
| 106 | `NetNoFCFToTLiability` | 非筹资性现金净流量与负债总额的比率(%) | number(18,4) | ✓ | 96.09% | 非筹资性现金净流量与负债总额的比率(%)(NetNoFCFToTLiability)=（经营活动产生的现金流量净额+投资... |
| 107 | `LongDebtRatio` | 长期负债占比 | number(18,4) | ✓ | 96.09% | 长期负债占比(LongDebtRatio)=（长期借款+应付债券+长期应付款+专项应付款)/负债总计。 |
| 108 | `EBITDAToIntBearDebt` | 息税折旧前利润/带息债务(%) | number(18,4) | ✓ | 83.65% | 息税折旧前利润/带息债务(%)(EBITDAToIntBearDebt)=息税折旧前利润/带息债务*100%，“息税折旧... |
| 109 | `EBITDAToInttFinExp` | 息税折旧前利润/利息费用(%) | number(18,4) | ✓ | 45.67% | 息税折旧前利润/利息费用(%)(EBITDAToInttFinExp)=息税折旧前利润/利息费用*100%，“息税折旧摊... |
| 110 | `EntireliabToEBITDA` | 全部债务/息税折旧前利润 | number(18,4) | ✓ | 99.72% | 全部债务/息税折旧前利润(EntireliabToEBITDA)=全部债务/息税折旧前利润，“息税前利润”计算方法见EB... |
| 111 | `CashToCurliability` | 货币资金/短期债务(%) | number(18,4) | ✓ | 82.93% | 货币资金/短期债务(%)(CashToCurliability)=货币资金/短期债务*100%，其中，货币资金=短期借款... |
| 112 | `BasicEPSYOY` | 基本每股收益同比增长(%) | number(18,4) | ✓ | 77.51% | 基本每股收益同比增长(%)(BasicEPSYOY)=（本期基本每股收益-上年同期基本每股收益）/ABS(上年同期基本每... |
| 113 | `DilutedEPSYOY` | 稀释每股收益同比增长(%) | number(18,4) | ✓ | 74.36% | 稀释每股收益同比增长(%)(DilutedEPSYOY)=（本期稀释每股收益-上年同期稀释每股收益）/ABS(上年同期稀... |
| 114 | `OperatingRevenueYOY` | 营业收入同比增长(%) | number(18,4) | ✓ | 87.91% | 营业收入同比增长(%)(OperatingRevenueYOY)=（本期营业收入-上年同期营业收入）/ABS(上年同期营... |
| 115 | `ORComGrowRateThreeY` | 营业收入3年复合增长率(%) | number(18,4) | ✓ | 58.07% | 营业收入3年复合增长率(%)(ORComGrowRateThreeY)：当三年前同期营业收入为正数时，营业收入3年复合增... |
| 116 | `OperProfitGrowRate` | 营业利润同比增长(%) | number(18,4) | ✓ | 88.31% | 营业利润同比增长(%)(OperProfitGrowRate)=（本期营业利润-上年同期营业利润）/ABS(上年同期营业... |
| 117 | `TotalProfeiGrowRate` | 利润总额同比增长(%) | number(18,4) | ✓ | 88.28% | 利润总额同比增长(%)(TotalProfeiGrowRate)=（本期利润总额-上年同期利润总额）/ABS(上年同期利... |
| 118 | `NetProfitYOY` | 净利润同比增长(%) | number(18,4) | ✓ | 88.36% | 净利润同比增长(%)(NetProfitYOY)=（本期净利润-上年同期净利润）/ABS(上年同期净利润)*100%，如... |
| 119 | `NPParentCompanyYOY` | 归属母公司股东的净利润同比增长(%) | number(18,4) | ✓ | 88.42% | 归属母公司股东的净利润同比增长(%)(NPParentCompanyYOY)=（本期归属母公司股东的净利润-上年同期归属... |
| 120 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长(%) | number(18,4) | ✓ | 76.45% | 归属母公司股东的净利润(扣除)同比增长(%)(NPParentCompanyCutYOY)=（本期扣除非经常性损益后的归... |
| 121 | `NPPCCGrowRateThreeY` | 归属母公司股东的净利润3年复合增长率(%) | number(18,4) | ✓ | 58.46% | 归属母公司股东的净利润3年复合增长率(%)(NPPCCGrowRateThreeY)：当三年前同期归属母公司股东的净利润... |
| 122 | `AvgNPYOYPastFiveYear` | 过去五年同期归属母公司净利润平均增幅 | number(18,4) | ✓ | 31.18% | 过去五年同期归属母公司净利润平均增幅(AvgNPYOYPastFiveYear)：该报告期过去五年的同期的归属母公司净利... |
| 123 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长(%) | number(18,4) | ✓ | 88.3% | 经营活动产生的现金流量净额同比增长(%)(NetOperateCashFlowYOY)=（本期经营活动产生的现金流量净额... |
| 124 | `OperCashPSGrowRate` | 每股经营活动产生的现金流量净额同比增长(%) | number(18,4) | ✓ | 86.79% | 每股经营活动产生的现金流量净额同比增长(%)(OperCashPSGrowRate)=（本期每股经营活动产生的现金流量净... |
| 125 | `NAORYOY` | 净资产收益率(摊薄)同比增长(%) | number(18,4) | ✓ | 81.66% | 净资产收益率(摊薄)同比增长(%)(NAORYOY)=（本期净资产收益率(摊薄)-上年同期净资产收益率(摊薄)）/ABS... |
| 126 | `NetAssetGrowRate` | 净资产同比增长(%) | number(18,4) | ✓ | 81.46% | 净资产同比增长(%)(NetAssetGrowRate)=（本期归属母公司所有者权益(或股东权益)合计-上年同期归属母公... |
| 127 | `TotalAssetGrowRate` | 总资产同比增长(%) | number(18,4) | ✓ | 82.08% | 总资产同比增长(%)(TotalAssetGrowRate)=（本期总资产-上年同期总资产）/ABS(上年同期总资产)*... |
| 128 | `EPSGrowRateYTD` | 每股净资产相对年初增长率(%) | number(18,4) | ✓ | 91.46% | 每股净资产相对年初增长率(%)(EPSGrowRateYTD)=（本期每股净资产-上年度末每股净资产）/ABS(上年上年... |
| 129 | `SEWithoutMIGrowRateYTD` | 归属母公司股东的权益相对年初增长率(%) | number(18,4) | ✓ | 91.49% | 归属母公司股东的权益相对年初增长率(%)(SEWithoutMIGrowRateYTD)=（本期归属母公司股东的权益-上... |
| 130 | `TAGrowRateYTD` | 资产总计相对年初增长率(%) | number(18,4) | ✓ | 92.25% | 资产总计相对年初增长率(%)(TAGrowRateYTD)=（本期末总资产-上年度末总资产）/ABS(上年上年度末总资产... |
| 131 | `SustainableGrowRate` | 可持续增长率(%) | number(18,4) | ✓ | 77.44% | 可持续增长率（SustainableGrowRate）＝（本期净利润/期初股东权益）*本期留存收益率*100%该指标只计... |
| 132 | `ToOpRevenueGrowRate` | 营业总收入同比增长(%) | number(18,4) | ✓ | 87.97% | 营业总收入同比增长率(%)(ToOpRevenueGrowRate)=（本期营业总收入-上年同期营业总收入）/ABS(上... |
| 133 | `ToOpCostGrowRate` | 营业总成本同比增长(%) | number(18,4) | ✓ | 85.19% | 营业总成本同比增长(%)(ToOpCostGrowRate)=（本期营业总成本-上年同期营业总成本）/ABS(上年同期营... |
| 134 | `ToLiabGrowRate` | 总负债同比增长(%) | number(18,4) | ✓ | 81.75% | 总负债同比增长(%)(ToLiabGrowRate)=（本期总负债-上年同期总负债）/ABS(上年同期总负债)*100%... |
| 135 | `CashEqIncreaseYOY` | 现金净流量同比增长(%) | number(18,4) | ✓ | 86.97% | 现金净流量同比增长(%)(CashEqIncreaseYOY)=（本期现金及现金等价物净增加额-上年同期现金及现金等价物... |
| 136 | `CashEquivalGrowRate` | 货币资金增长率(%) | number(18,4) | ✓ | 79.67% | 货币资金增长率(%)(CashEquivalGrowRate)=（本期货币资金-上年同期货币资金）/ABS(上年同期货币... |
| 137 | `FAExpansionRate` | 固定资产投资扩张率(%) | number(18,4) | ✓ | 79.67% | 固定资产投资扩张率(%)(FAExpansionRate)=（本期固定资产-上年同期固定资产）/ABS(上年同期固定资产... |
| 138 | `OperCycle` | 营业周期(天/次) | number(12,4) | ✓ | 100.0% | 营业周期(天/次)(OperCycle)＝存货周转天数+应收账款周转天数，金融类企业不计算。 |
| 139 | `NetOperCycle` | 净营业周期 | number(12,4) | ✓ | 100.0% | 净营业周期(天/次)(NetOperCycle)=存货周转天数+应收账款周转天数-应付账款周转天数,金融类企业不计算。 |
| 140 | `WorkingCapitalTurDays` | 营运资金周转天数 | number(12,4) | ✓ | 100.0% | 营运资金周转天数(天/次)(WorkingCapitalTurDays)=存货周转天数+应收账款周转天数-应付账款周转天... |
| 141 | `InventoryTRate` | 存货周转率(次) | number(12,4) | ✓ | 91.9% | 存货周转率(次)(InventoryTRate)＝营业成本*2/（期初存货+期末存货），金融类企业不计算。 |
| 142 | `InventoryTDays` | 存货周转天数(天/次) | number(12,4) | ✓ | 91.89% | 存货周转天数(天/次)(InventoryTDays)=N/存货周转率，其中：一季报，N=90；中报，N=180；三季报... |
| 143 | `ARTRate` | 应收账款周转率(次) | number(12,4) | ✓ | 91.69% | 应收账款周转率(次)(ARTRate)＝营业收入*2/（期初应收账款+期末应收账款），金融类企业不计算。 |
| 144 | `ARTDays` | 应收账款周转天数(天/次) | number(12,4) | ✓ | 91.29% | 应收账款周转天数(天/次)(ARTDays)＝N/应收账款周转率，其中：一季报，N=90；中报，N=180；三季报，N=... |
| 145 | `AccountsPayablesTRate` | 应付账款周转率(次) | number(12,4) | ✓ | 91.43% | 应付账款周转率(次)(AccountsPayablesTRate)＝营业成本*2/（期初应付账款+期末应付账款），金融类... |
| 146 | `AccountsPayablesTDays` | 应付账款周转天数(天/次) | number(12,4) | ✓ | 91.39% | 应付账款周转天数(天/次)(AccountsPayablesTDays)=N/应付账款周转率，其中：一季报，N=90；中... |
| 147 | `CurrentTRate` | 流动资产周转率(次) | number(12,4) | ✓ | 93.22% | 流动资产周转率(次)(CurrentTRate)＝营业总收入*2/（期初流动资产合计+期末流动资产合计），金融类企业不计... |
| 148 | `FixedAssetTRate` | 固定资产周转率(次) | number(12,4) | ✓ | 92.91% | 固定资产周转率(次)(FixedAssetTRate)＝营业总收入*2/（期初固定资产合计+期末固定资产合计），金融类企... |
| 149 | `EquityTRate` | 股东权益周转率(次) | number(12,4) | ✓ | 94.61% | 股东权益周转率(次)(EquityTRate)＝营业总收入*2/（期初净资产+期末净资产）。 |
| 150 | `TotalAssetTRate` | 总资产周转率(次) | number(12,4) | ✓ | 95.91% | 总资产周转率(次)(TotalAssetTRate)＝营业总收入*2/（期初资产合计+期末资产合计）。 |
| 151 | `TotalAssetTRateTTM` | 总资产周转率_TTM(次) | number(12,4) | ✓ | 95.97% | 总资产周转率_TTM(次)(TotalAssetTRateTTM)=营业总收入(TTM)*2/（上年同期资产合计+期末资... |
| 152 | `WorkingCaitalTRate` | 营运资本周转率(次) | number(12,4) | ✓ | 94.76% | 营运资本周转率(次)(WorkingCaitalTRate)=营业总收入*2/（期初营运资本+期末营运资本），其中，营运... |
| 153 | `NonCurrentATRate` | 非流动资产周转率(次) | number(12,4) | ✓ | 93.21% | 非流动资产周转率(次)(NonCurrentATRate)=营业总收入*2/（期初非流动资产合计+期末非流动资产合计），... |
| 154 | `SaleServiceCashToOR` | 销售商品提供劳务收到的现金/营业收入(%) | number(18,4) | ✓ | 95.47% | 销售商品提供劳务收到的现金/营业收入(%)(SaleServiceCashToOR):销售商品提供劳务收到的现金/营业收... |
| 155 | `SaleServiceCashToORTTM` | 销售商品提供劳务收到的现金/营业收入_TTM(%) | number(18,4) | ✓ | 98.84% | 销售商品提供劳务收到的现金/营业收入_TTM(%)(SaleServiceCashToORTTM)=销售商品提供劳务收到... |
| 156 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(18,4) | ✓ | 99.04% | 经营活动产生的现金流量净额/营业收入(%)(CashRateOfSales)=经营活动产生的现金流量净额/营业收入*10... |
| 157 | `CashRateOfSalesTTM` | 经营活动产生的现金流量净额/营业收入_TTM(%) | number(18,4) | ✓ | 99.38% | 经营活动产生的现金流量净额/营业收入_TTM(%)(CashRateOfSalesTTM)=经营活动产生的现金流量净额(... |
| 158 | `NOCFToOperatingNI` | 经营活动产生的现金流量净额/经营活动净收益(%) | number(18,4) | ✓ | 76.23% | 经营活动产生的现金流量净额/经营活动净收益(%)(NOCFToOperatingNI)＝经营活动产生的现金流量净额/经营... |
| 159 | `NOCFToOperatingNITTM` | 经营活动产生的现金流量净额/经营活动净收益_TTM(%) | number(18,4) | ✓ | 76.29% | 经营活动产生的现金流量净额/经营活动净收益_TTM(%)(NOCFToOperatingNITTM)=经营活动产生的现金... |
| 160 | `CapitalExpenditureToDM` | 资本支出/折旧和摊销 | number(18,4) | ✓ | 72.76% | 资本支出/折旧和摊销(CapitalExpenditureToDM)=构建固定资产、无形资产和其他长期资产支付的现金/（... |
| 161 | `CashEquivalentIncrease` | 现金及现金等价物净增加额(元) | number(19,4) | ✓ | 98.28% | 现金及现金等价物净增加额(元)(CashEquivalentIncrease)：现金流量表公布值。 |
| 162 | `NetOperateCashFlow` | 经营活动产生的现金流量净额(元) | number(19,4) | ✓ | 99.7% | 经营活动产生的现金流量净额(元)(NetOperateCashFlow)：现金流量表公布值。 |
| 163 | `GoodsSaleServRendCash` | 销售商品提供劳务收到的现金(元) | number(19,4) | ✓ | 95.56% | 销售商品提供劳务收到的现金(元)(GoodsSaleServRendCash):现金流量表公布值。 |
| 164 | `FreeCashFlow` | 自由现金流量(元) | number(19,4) | ✓ | 100.0% | 自由现金流量(元)(FreeCashFlow)＝息前税后利润+折旧与摊销-营运资金增加-资本支出。其中，息前税后利润＝息... |
| 165 | `NetProfitCashCover` | 净利润现金含量(%) | number(18,4) | ✓ | 80.77% | 净利润现金含量(%)(NetProfitCashCover)＝经营活动产生的现金流量净额/净利润*100%。 |
| 166 | `OperatingReveCashCover` | 营业收入现金含量(%) | number(18,4) | ✓ | 95.47% | 营业收入现金含量(%)(OperatingReveCashCover)＝销售商品、提供劳务收到的现金/营业收入*100%... |
| 167 | `OperCashInToAsset` | 总资产现金回收率(%) | number(18,4) | ✓ | 96.36% | 总资产现金回收率(%)(OperCashInToAsset)＝经营活动产生的现金流量净额*2/（期初总资产+期末总资产）... |
| 168 | `NetOperCFToOperProfTTM` | 经营活动产生的现金流量净额/营业利润_TTM(%) | number(18,4) | ✓ | 82.57% | 经营活动产生的现金流量净额/营业利润_TTM(%)(NetOperCFToOperProfTTM)=经营活动产生的现金流... |
| 169 | `NetOperCFRatio` | 经营活动产生的现金流量净额占比 | number(18,4) | ✓ | 99.7% | 经营活动产生的现金流量净额占比(NetOperCFRatio)=经营活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 170 | `NetInvestCFRatio` | 投资活动产生的现金流量净额占比 | number(18,4) | ✓ | 98.72% | 投资活动产生的现金流量净额占比(NetInvestCFRatio)=投资活动产生的现金流量净额/（经营活动产生的现金流量... |
| 171 | `NetFinaCFRatio` | 筹资活动产生的现金流量净额占比 | number(18,4) | ✓ | 95.92% | 筹资活动产生的现金流量净额占比(NetFinaCFRatio)=筹资活动产生的现金流量净额/（经营活动产生的现金流量净额... |
| 172 | `NetOperCFToToOperReve` | 经营现金净流量/营业总收入(%) | number(18,4) | ✓ | 99.07% | 经营现金净流量/营业总收入(%)(NetOperCFToToOperReve)=经营活动产生的现金流量净额/营业总收入*... |
| 173 | `CashWorkingIndex` | 现金营运指数 | number(18,4) | ✓ | 72.85% | 现金营运指数(CashWorkingIndex)=经营活动产生的现金流量净额／（净利润+资产减值准备+当期计提折旧与摊销... |
| 174 | `NetOperCFToToAssets` | 全部资产现金回收率(%) | number(18,4) | ✓ | 96.36% | 全部资产现金回收率(%)(NetOperCFToToAssets)=经营活动产生的现金流量净额/总资产*100%。 |
| 175 | `CashEquivalentPS` | 每股现金及现金等价物余额(元/股) | number(19,4) | ✓ | 95.85% | 每股现金及现金等价物余额(元/股)(CashEquivalentPS)＝现金及现金等价物期末余额/期末总股本。 |
| 176 | `DividendPS` | 每股股利(元/股)(税前) | number(19,4) | ✓ | 18.23% | 每股股利(元/股)(税前)(DividendPS)：根据公司公布的分红方案确定。 |
| 177 | `ActualDividendPS` | 每股股利(元/股)(税后) | number(19,4) | ✓ | 18.23% | 每股股利(元/股)(税后)(ActualDividendPS)：公布值，根据公司公布的分红方案确定。 |
| 178 | `DividendCover` | 股利保障倍数(倍) | number(12,4) | ✓ | 18.23% | 股利保障倍数(倍)(DividendCover)＝归属于母公司的净利润/累计合计派现金额；若“累计派现金额”为0或NUL... |
| 179 | `CashDividendCover` | 现金股利保障倍数(倍) | number(12,4) | ✓ | 18.21% | 现金股利保障倍数(倍)(CashDividendCover)＝经营活动产生的现金流量净额/累计合计派现金额；若“累计派现... |
| 180 | `DividendPaidRatio` | 股利支付率(%) | number(12,4) | ✓ | 81.0% | 股利支付率(%)(DividendPaidRatio)＝（累计合计派现金额/归属于母公司的净利润）*100%。 |
| 181 | `RetainedEarningRatio` | 留存盈余比率(%) | number(12,4) | ✓ | 81.0% | 留存盈余比率(%)(RetainedEarningRatio)＝100%-股利支付率，“股利支付率”计算方法见Divid... |
| 182 | `DividendTTM` | 股息TTM | number(19,4) | ✓ | 35.82% | 股息TTM(元)(DividendTTM)：根据“累计派现合计”计算。 |
| 183 | `DebtAssetsRatio` | 资产负债率(%) | number(12,4) | ✓ | 96.1% | 资产负债率(%)(DebtAssetsRatio)＝负债合计/资产合计*100%。 |
| 184 | `DebtARatioCutADRecp` | 剔除预收账款后的资产负债率(%) | number(12,4) | ✓ | 96.1% | 剔除预收账款后的资产负债率(%)(DebtARatioCutADRecp)=(负债合计-预收款项-合同负债)／(资产总额... |
| 185 | `DebtARatioCutADReNo` | 剔除预收账款后的资产负债率_公告口径(%) | number(12,4) | ✓ | 96.1% | 剔除预收账款后的资产负债率_公告口径(%)(DebtARatioCutADReNo)=(负债合计-预收款项-合同负债)／... |
| 186 | `CurrentAssetsToTA` | 流动资产/总资产(%) | number(12,4) | ✓ | 93.78% | 流动资产/总资产(%)(CurrentAssetsToTA)=流动资产/总资产*100%，此指标金融类企业不计算。 |
| 187 | `NonCurrentAssetsToTA` | 非流动资产/总资产(%) | number(12,4) | ✓ | 93.77% | 非流动资产／总资产(%)(NonCurrentAssetsToTA)=非流动资产/总资产*100%，此指标金融类企业不计... |
| 188 | `NetTangibleAToTA` | 有形资产/总资产(%) | number(12,4) | ✓ | 96.51% | 有形资产/总资产(%)(NetTangibleAToTA)=有形资产净值/总资产*100%，有形资产净值=归属于母公司的... |
| 189 | `FixAssetRatio` | 固定资产比率(%) | number(12,4) | ✓ | 93.47% | 固定资产比率(%)(FixAssetRatio)＝固定资产/资产总额*100% |
| 190 | `IntangibleAssetRatio` | 无形资产比率(%) | number(12,4) | ✓ | 91.57% | 无形资产比率(%)(IntangibleAssetRatio)＝无形资产/资产总额*100%。 |
| 191 | `LongDebtToAsset` | 长期借款/总资产(%) | number(12,4) | ✓ | 33.26% | 长期借款/总资产(%)(LongDebtToAsset)=长期借款/总资产*100。 |
| 192 | `BondsPayableToAsset` | 应付债券/总资产(%) | number(12,4) | ✓ | 3.97% | 应付债券/总资产(%)(BondsPayableToAsset)=应付债券/总资产*100%。 |
| 193 | `SEWMIToTotalCapital` | 归属母公司股东的权益/全部投入资本(%) | number(12,4) | ✓ | 95.4% | 归属母公司股东的权益/全部投入资本(%)(SEWMIToTotalCapital)＝归属母公司股东的权益/全部投入资本*... |
| 194 | `InBearDebtToTotCapital` | 带息债务/全部投入资本(%) | number(12,4) | ✓ | 96.16% | 带息债务/全部投入资本(%)(InBearDebtToTotCapital)＝带息债务/（归属于母公司的股东权益+带息债... |
| 195 | `CurrentLiabilityToTL` | 流动负债/负债合计(%) | number(12,4) | ✓ | 93.75% | 流动负债/负债合计(%)(CurrentLiabilityToTL):流动负债／负债合计*100%，该指标金融类企业不计... |
| 196 | `NonCurrLiabilityToTL` | 非流动负债/负债合计(%) | number(12,4) | ✓ | 89.85% | 非流动负债/负债合计(%)(NonCurrLiabilityToTL):非流动负债/负债合计*100%，该指标金融类企业... |
| 197 | `EquityToAsset` | 股东权益比率(%) | number(12,4) | ✓ | 96.43% | 股东权益比率(%)(EquityToAsset)＝股东权益合计/资产合计*100% |
| 198 | `EquityMultipler` | 权益乘数(%) | number(18,4) | ✓ | 95.86% | 权益乘数(%)(EquityMultipler)＝资产合计/股东权益合计*100%。 |
| 199 | `WorkingCapital` | 营运资金(元) | number(19,4) | ✓ | 100.0% | 营运资金(元)(WorkingCapital)＝流动资产-流动负债，金融类企业不计算。 |
| 200 | `LongDebtToEquity` | 长期负债/股东权益合计 | number(18,4) | ✓ | 89.38% | 长期负债/股东权益合计(LongDebtToEquity)=长期负债/股东权益合计；该指标金融类企业不计算。 |
| 201 | `LongAssetFitRate` | 长期资产适合率 | number(18,4) | ✓ | 93.47% | 长期资产适合率(LongAssetFitRate)＝（所有者权益+长期负债）/（固定资产净值+长期股权投资+可供出售金融... |
| 202 | `TotalCLiaToSEWMI` | 流动负债权益比率(%) | number(18,4) | ✓ | 93.13% | 流动负债权益比率(%)(TotalCLiaToSEWMI)=流动负债合计/归属于母公司股东的权益合计*100%,金融类企... |
| 203 | `TotalNonCLiaToSEWMI` | 非流动负债权益比率(%) | number(18,4) | ✓ | 89.31% | 非流动负债权益比率(%)(TotalNonCLiaToSEWMI)=非流动负债合计/归属于母公司股东的权益合计*100%... |
| 204 | `TotalNonCurLiaToSEWMI` | 长期资本负债率(%) | number(18,4) | ✓ | 89.55% | 长期资本负债率(%)(TotalNonCurLiaToSEWMI)=非流动负债合计／（非流动负债合计+归属母公司所有者权... |
| 205 | `TotalNonCurAToSEWMI` | 资本固定化比率(%) | number(18,4) | ✓ | 93.13% | 资本固定化比率(%)(TotalNonCurAToSEWMI)=非流动资产合计／归属母公司所有者权益(或股东权益)合计*... |
| 206 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(18,4) | ✓ | 80.25% | 经营活动净收益/利润总额(%)(OperatingNIToTP)＝经营活动净收益／利润总额*100%，“经营活动净收益”... |
| 207 | `OperatingMIToTPTTM` | 经营活动净收益/利润总额_TTM(%) | number(18,4) | ✓ | 83.03% | 经营活动净收益/利润总额_TTM(%)(OperatingMIToTPTTM)＝经营活动净收益(TTM)／利润总额(TT... |
| 208 | `InvestRAssociatesToTP` | 对联营合营公司投资收益/利润总额(%) | number(18,4) | ✓ | 25.31% | 对联营合营公司投资收益/利润总额(%)(InvestRAssociatesToTP)=对联营合营公司投资收益/利润总额*... |
| 209 | `InvRAssociatesToTPTTM` | 对联营合营公司投资收益/利润总额_TTM(%) | number(18,4) | ✓ | 28.25% | 对联营合营公司投资收益/利润总额_TTM(%)(InvRAssociatesToTPTTM)=对联营合营公司投资收益(T... |
| 210 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(18,4) | ✓ | 80.25% | 价值变动净收益/利润总额(%)(ValueChangeNIToTP)＝价值变动净收益／利润总额*100%；其中，价值变动... |
| 211 | `ValueChangeNIToTPTTM` | 价值变动净收益/利润总额_TTM(%) | number(18,4) | ✓ | 83.04% | 价值变动净收益/利润总额_TTM(%)(ValueChangeNIToTPTTM)＝价值变动净收益(TTM)／利润总额(... |
| 212 | `NetNonOperaIncomeToTP` | 营业外收支净额/利润总额(%) | number(18,4) | ✓ | 80.25% | 营业外收支净额/利润总额(%)(NetNonOperaIncomeToTP)＝(营业外收入-营业外支出)/利润总额*10... |
| 213 | `NetNonOIToTPTTM` | 营业外收支净额/利润总额_TTM(%) | number(18,4) | ✓ | 82.31% | 营业外收支净额/利润总额_TTM(%)(NetNonOIToTPTTM)＝营业外收支净额(TTM)/利润总额(TTM)*... |
| 214 | `TaxesToTP` | 所得税/利润总额(%) | number(18,4) | ✓ | 76.39% | 所得税/利润总额(%)(TaxesToTP)=所得税/利润总额*100%。 |
| 215 | `NPCutToTP` | 扣除非经常损益后的归母净利润/净利润(%) | number(18,4) | ✓ | 71.26% | 扣除非经常损益后的归母净利润/净利润(%)(NPCutToTP)＝扣除非经常损益后的净利润／净利润*100%，其中，“扣... |
| 216 | `ToProfToOperProfitTTM` | 营业利润/利润总额_TTM(%) | number(18,4) | ✓ | 99.23% | 营业利润/利润总额_TTM(%)(ToProfToOperProfitTTM)=营业利润(TTM)/利润总额(TTM)*... |
| 217 | `ToProfToOperRevenueTTM` | 利润总额/营业收入_TTM(%) | number(18,4) | ✓ | 99.38% | 利润总额/营业收入_TTM(%)(ToProfToOperRevenueTTM)=利润总额(TTM)/营业收入(TTM)... |
| 218 | `EquityMultipler_DuPont` | 权益乘数_杜邦分析(%) | number(18,4) | ✓ | 95.17% | 权益乘数_杜邦分析(%)(EquityMultipler_DuPont)＝（期初资产总额+期末资产总额）/（期初归属于母... |
| 219 | `DebtEquityRatio_DuPont` | 产权比率_杜邦分析(%) | number(18,4) | ✓ | 94.92% | 产权比率_杜邦分析(%)(DebtEquityRatio_DuPont)=（期初负债合计+期末负债合计）/（期初归属母公... |
| 220 | `NPPCToNP_DuPont` | 归属母公司股东的净利润/净利润(%)_杜邦分析(%) | number(18,4) | ✓ | 99.61% | 归属母公司股东的净利润/净利润(%)(NPPCToNP_DuPont)=归属母公司股东的净利润/净利润*100。 |
| 221 | `NPToTOR_DuPont` | 净利润/营业总收入_杜邦分析(%) | number(18,4) | ✓ | 99.14% | 净利润/营业总收入(%)(NPToTOR_DuPont):净利润/营业总收入*100；金融类企业不计算。 |
| 222 | `NPToTP_DuPont` | 净利润/利润总额(%)_杜邦分析(%) | number(18,4) | ✓ | 80.14% | 净利润/利润总额(%)(NPToTP_DuPont)=净利润/利润总额*100。 |
| 223 | `TPToEBIT_DuPont` | 利润总额/息税前利润(%)_杜邦分析(%) | number(18,4) | ✓ | 80.08% | 利润总额/息税前利润(%)(TPToEBIT_DuPont)=利润总额/息税前利润*100，“息税前利润”计算方法见EB... |
| 224 | `EBITToTOR_DuPont` | 息税前利润/营业总收入_杜邦分析(%) | number(18,4) | ✓ | 99.35% | 息税前利润/营业总收入(%)(EBITToTOR_DuPont):息税前利润/营业总收入*100，“息税前利润”计算方法... |
| 225 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 226 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 227 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到公司的交易代码、简称等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，110106-定期报告:第二季报，110107-定期报告:第四季报，110108-定期报告:第五季报，110109-定期报告:第二季报（更正后），110110-定期报告:第四季报（更正后），110111-定期报告:第五季报（更正后），110201-定期报告:年度报告(关联方)，110202-定期报告:半年度报告(关联方)，110203-定期报告:第一季报(关联方)，110204-定期报告:第三季报(关联方)，110205-定期报告:审计报告(关联方)，120101-临时公告:审计报告(更正后)，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)，120106-临时公告:公开转让说明书(更正后)，120107-临时公告:业绩快报，120108-临时公告:业绩快报(更正后)，120109-临时公告:第二季报(更正后)，120110-临时公告:第四季报(更正后)，120201-临时公告:跟踪评级报告，120202-临时公告:同业存单发行计划，120203-临时公告:比较式财务报表，120204-临时公告:关联方，120205-临时公告:其他，120206-临时公告:前期差错更正，120207-临时公告:第一季度报告，120208-临时公告:第二季度报告，120209-临时公告:第三季度报告，120210-临时公告:第四季度报告，120211-临时公告：年度报告，120212-临时公告：半年度报告，120213-临时公告:受托管理人事务报告，120214-临时公告:资产评估报告，120215-临时公告:资产管理报告，120216-临时公告：经营数据公告，120217-临时公告：经营数据公告(更正后），120218-临时公告：主要经营业绩，130101-发行上市书:募集说明书，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130105-发行上市书:审阅报告，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130108-发行上市书:发行公告，130109-发行上市书:审计报告，130110-发行上市书:关联方，130111-发行上市书:其他，130112-发行上市书:招股说明书(上会稿)，130113-发行上市书:招股说明书(注册稿)，140101-发行披露文件:第一季报，140102-发行披露文件:半年度报告，140103-发行披露文件:第三季报，140104-发行披露文件:审计报告，140105-发行披露文件:募集说明书，140106-发行披露文件:跟踪评级报告，140107-发行披露文件:年度报告，140108-发行披露文件:关联方，140109-发行披露文件:预案公告，140110-发行披露文件:转让服务公告书，140111-发行披露文件:备案登记表，140112-发行披露文件:初始信息披露，150101-发债定期报告:第一季报，150102-发债定期报告:半年度报告，150103-发债定期报告:第三季报，150104-发债定期报告:年度报告，150105-发债:其他报告。

### IfMerged (是否合并)

是否合并（IfMerged）固定常量：1-合并，2-母公司

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。

### BasicEPS (基本每股收益(元/股))

基本每股收益(元/股)(BasicEPS)：直取公司的实际披露数；

### DilutedEPS (稀释每股收益(元/股))

稀释每股收益(元/股)(DilutedEPS)：直取公司的实际披露数；

### EPS (每股收益_期末股本摊薄(元/股))

每股收益_期末股本摊薄(元/股)(EPS)： 每股收益_期末股本摊薄=归属于母公司的净利润/该报告期末总股本。

### EPSTTM (每股收益_TTM(元/股))

每股收益_TTM(元/股)(EPSTTM)=归属于母公司的净利润（TTM）/期末总股本

### NetAssetPS (每股净资产(元/股))

每股净资产(元/股)(NetAssetPS)：直接取公司定期报告披露数据；若无披露，则，每股净资产=（归属于母公司的所有者权益-其他权益工具）/期末总股本。

### TotalOperateRevenuePS (每股营业总收入(元/股))

每股营业总收入(元/股)(TotalOperateRevenuePS)＝营业总收入/该报告期期末总股本

## SQL示例

```sql
-- 查询 科创板主要财务分析指标 数据
SELECT *
FROM lc_stibmainindex
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
