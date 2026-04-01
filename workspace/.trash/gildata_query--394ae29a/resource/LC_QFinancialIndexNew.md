# LC_QFinancialIndexNew

**中文名**: 公司单季财务指标_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_QFinancialIndexNew` |
| MySQL表名 | `lc_qfinancialindexnew` |
| 中文名 | 公司单季财务指标_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务衍生指标 |
| 更新频率 | 季更新 |
| 字段数量 | 102 |
| 版本 | 1.04 |

## 表描述

1.本表收录自公布季报以来上市企业(含科创板)、发债企业的单季主要财务指标信息，计算基础数据为“单季利润表_新会计准则”和“单季现金流量表_新会计准则”，单位为人民币元。
2.由于会计期间可能发生同一控制下企业合并、企业自身错报漏报、企业列报项目变化等问题，将会导致二、四季度的单季数据的可靠性下降
3.数据范围：2000-09-30至今
4.信息来源：定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `BulletinType` | 公告类型 | number(10) | ✓ | 100.0% | 公告类型(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告... |
| 4 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN ... |
| 7 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 8 | `NPFromParentCompanyOwners` | 归属母公司股东的净利润(元) | number(19,4) | ✓ | 99.85% | 归属母公司股东的净利润(元)（NPFromParentCompanyOwners）：根据“归属于母公司所有者的净利润“计... |
| 9 | `NetProfitCut` | 扣除非经常性损益后的归母净利润(元) | number(19,4) | ✓ | 50.61% | 扣除非经常性损益后的归母净利润(元)(NetProfitCut)：优先取原文披露值，原文未披露，则根据“归属母公司股东的... |
| 10 | `NetIncFromValueChange` | 价值变动净收益(元) | number(19,4) | ✓ | 100.0% | 价值变动净收益（NetIncFromValueChange）=投资净收益+公允价值变动净收益+汇兑收益。 |
| 11 | `NetIncomeFromOperating` | 经营活动净收益(元) | number(18,4) | ✓ | 99.85% | 经营活动净收益(元)(NetIncomeFromOperating)：对于非金融类企业，经营活动净收益＝营业总收入－营业... |
| 12 | `EBIT` | 息税前利润(反推)(元) | number(18,4) | ✓ | 96.51% | 息税前利润(反推)(元)(EBIT)：利润总额＋利息费用 其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用... |
| 13 | `NetProfitRatio` | 销售净利率_不含少数股东损益(%) | number(18,4) | ✓ | 99.29% | 销售净利率_不含少数股东损益(%)(NetProfitRatio)=归属于母公司的净利润/营业总收入*100%； |
| 14 | `GrossIncomeRatio` | 销售毛利率(%) | number(18,4) | ✓ | 95.87% | 销售毛利率(%)(GrossIncomeRatio)=（营业总收入-营业成本）/营业总收入*100%；本指标仅对非金融企... |
| 15 | `OperatingCostRate` | 营业成本率(%) | number(18,4) | ✓ | 96.15% | 营业成本率(%)(OperatingCostRate)=营业成本/营业总收入*100%；本指标仅对非金融企业。 |
| 16 | `PeriodCostsRate` | 期间费用率(%) | number(18,4) | ✓ | 99.63% | 期间费用率(%)(PeriodCostsRate)=（销售费用+管理费用+财务费用）/营业总收入*100%；本指标仅对非... |
| 17 | `OperatingExpenseRate` | 销售费用率(%) | number(18,4) | ✓ | 91.4% | 销售费用率(%)(OperatingExpenseRate)=销售费用/营业总收入*100%；本指标仅对非金融企业。 |
| 18 | `AdminiExpenseRate` | 管理费用率(%) | number(18,4) | ✓ | 96.21% | 管理费用率(%)(AdminiExpenseRate)=管理费用/营业总收入*100%；本指标仅对非金融企业。 |
| 19 | `FinancialExpenseRate` | 财务费用率(%) | number(18,4) | ✓ | 96.47% | 财务费用率(%)(FinancialExpenseRate)=财务费用/营业总收入*100%；本指标仅对非金融企业。 |
| 20 | `OperatingProfitMargin` | 营业利润率(%) | number(18,4) | ✓ | 99.63% | 营业利润率(%)(OperatingProfitMargin)=营业利润/营业总收入*100%；本指标仅对非金融企业。 |
| 21 | `TotalProfitCostRatio` | 利润总额/营业总成本(含减值损失)(%) | number(18,4) | ✓ | 99.84% | 利润总额/营业总成本(含减值损失)(%)(TotalProfitCostRatio)=利润总额/营业总成本(含减值损失)... |
| 22 | `TaxRatio` | 销售税金率(%) | number(18,4) | ✓ | 97.37% | 销售税金率(%)(TaxRatio)=税金及附加/营业收入*100%，该指标金融类和非金融类公司都计算。 |
| 23 | `NonRecurrGLProportion` | 非经常性损益/归属于母公司净利润(%) | number(18,4) | ✓ | 29.09% | 非经常性损益比率(%)(NonRecurrGLProportion)=非经常性损益/归属于母公司净利润*100%； 该指... |
| 24 | `SalesCostRatio` | 销售成本率(%) | number(18,4) | ✓ | 99.0% | 销售成本率(%)(SalesCostRatio)：1、非金融类企业：营业成本/营业总收入*100%；2、金融类企业：营业... |
| 25 | `ROECut` | 净资产收益率_扣除,摊薄(%) | number(18,6) | ✓ | 49.71% | 净资产收益率_扣除,摊薄(%)(ROECut)=扣除非经常性损益后归属于母公司的净利润/期末归属于母公司的股东权益*10... |
| 26 | `ROA_EBIT` | 总资产报酬率(%) | number(18,4) | ✓ | 94.49% | 总资产报酬率(%)(ROA_EBIT)=息税前利润*2/（期初总资产+期末总资产）*100% ，其中，“息税前利润”计算... |
| 27 | `ROIC` | 投入资本回报率(%) | number(18,4) | ✓ | 94.02% | 投入资本回报率(%)(ROIC)=息税前利润*（1-有效税率）*2/（期初全部投入资本+期末全部投入资本））*100%，... |
| 28 | `AssetImpaLossToTOR` | 资产减值损失/营业总收入(%) | number(18,4) | ✓ | 69.28% | 资产减值损失/营业总收入(%)(AssetImpaLossToTOR)=资产减值损失/营业总收入*100。 |
| 29 | `TOperatingCostToTOR` | 营业总成本(含减值损失)/营业总收入(%) | number(18,4) | ✓ | 99.29% | 营业总成本(含减值损失)/营业总收入(%)(TOperatingCostToTOR)=营业总成本(含减值损失)/营业总收... |
| 30 | `NPToTOR` | 净利润/营业总收入(%) | number(18,4) | ✓ | 99.3% | 净利润/营业总收入(%)(NPToTOR)=净利润/营业总收入*100。 |
| 31 | `ToProfToOperRevenue` | 利润总额/营业收入(%) | number(18,4) | ✓ | 99.19% | 利润总额/营业收入(%)(ToProfToOperRevenue)=利润总额/营业收入*100%。  |
| 32 | `NetProfToOpReven` | 归属母公司股东的净利润/营业收入(%) | number(18,4) | ✓ | 99.19% | 归属母公司股东的净利润/营业收入(%)(NetProfToOpReven)=归属母公司股东的净利润/营业收入*100。 |
| 33 | `OperatingProfitRatio` | 营业利润/营业收入(%) | number(18,4) | ✓ | 99.19% | 营业利润/营业收入(%)(OperatingProfitRatio)=营业利润/营业收入*100。 |
| 34 | `EBITToTOR` | 息税前利润(反推)/营业总收入(%) | number(18,4) | ✓ | 95.87% | 息税前利润(反推)/营业总收入(%)(EBITToTOR)=息税前利润(反推)/营业总收入*100。 |
| 35 | `OperCycle` | 营业周期(天) | number(18,4) | ✓ | 100.0% | 营业周期(天)(OperCycle)=应收帐款周转天数+存货周转天数；本指标仅对非金融企业。 |
| 36 | `WorkingCaitalTRate` | 营运资本周转率(次) | number(12,4) | ✓ | 76.56% | 营运资本周转率(次)(WorkingCaitalTRate)=营业总收入*2/（（上一报告期期末流动资产-上一报告期期末... |
| 37 | `InventoryTRate` | 存货周转率(次) | number(18,4) | ✓ | 93.44% | 存货周转率(次)(InventoryTRate)=营业成本*2/（上一报告期期末存货+本报告期期末存货）；本指标仅针对非... |
| 38 | `InventoryTDays` | 存货周转天数(天/次) | number(18,4) | ✓ | 93.37% | 存货周转天数(天/次)(InventoryTDays)=90/存货周转率；本指标仅对非金融企业。 |
| 39 | `ARTRate` | 应收账款周转率(次) | number(18,4) | ✓ | 94.25% | 应收账款周转率(次)(ARTRate)=营业总收入*2/（上一报告期期末应收帐款+本报告期期末应收帐款）；仅对非金融企业... |
| 40 | `ARTDays` | 应收账款周转天数(天/次) | number(18,4) | ✓ | 94.17% | 应收账款周转天数(天/次)(ARTDays)=90/应收帐款周转率；本指标仅对非金融企业。 |
| 41 | `AccountsPayablesTRate` | 应付账款周转率(次) | number(18,4) | ✓ | 89.46% | 应付账款周转率(次)(AccountsPayablesTRate)=营业成本*2/（上一报告期期末应付账款+本报告期期末... |
| 42 | `AccountsPayablesTDays` | 应付账款周转天数(天/次) | number(18,4) | ✓ | 89.46% | 应付账款周转天数(天/次)(AccountsPayablesTDays)=90/（营业成本*2/（上一报告期期末应付账款... |
| 43 | `CurrentTRate` | 流动资产周转率(次) | number(18,4) | ✓ | 95.84% | 流动资产周转率(次)(CurrentTRate)=营业总收入*2/（上一报告期期末流动资产合计+本报告期期末流动资产合计... |
| 44 | `TotalAssetTRate` | 总资产周转率(次) | number(18,4) | ✓ | 98.9% | 总资产周转率(次)(TotalAssetTRate)=营业总收入*2/（上一报告期期末资产总计+本报告期期末资产总计）；... |
| 45 | `FixedAssetTRate` | 固定资产周转率(次) | number(18,4) | ✓ | 93.92% | 固定资产周转率(次)(FixedAssetTRate)=营业总收入*2/[上一报告期期末固定资产合计（固定资产+固定资产... |
| 46 | `NonCurrentATRate` | 非流动资产周转率(次) | number(12,4) | ✓ | 93.53% | 非流动资产周转率(次)(NonCurrentATRate)=营业总收入*2/[上一报告期期末非流动资产合计+本报告期期末... |
| 47 | `NetOperCycle` | 净营业周期(天/次) | number(18,4) | ✓ | 95.58% | 净营业周期(天/次)(NetOperCycle)=应收账款周转天数＋存货周转天数－应付账款周转天数；本指标仅针对非金融企... |
| 48 | `WorkingCapitalTurDays` | 营运资金周转天数(天/次) | number(18,4) | ✓ | 95.02% | 营运资金周转天数(天/次)(WorkingCapitalTurDays)=应收帐款周转天数+预付帐款周转天数+存货周转天... |
| 49 | `ROA` | 总资产收益率(ROA)(%) | number(18,4) | ✓ | 98.91% | 总资产收益率(ROA)(%)(ROA)=归属于母公司的净利润*2/（上一报告期期末资产总计+本报告期期末资产总计）*10... |
| 50 | `ROE` | 净资产收益率(ROE)(摊薄)(%) | number(18,4) | ✓ | 96.38% | 净资产收益率(ROE)(摊薄)(%)(ROE)=归属于母公司的净利润/本报告期期末归属于母公司股东权益*100%，限制归... |
| 51 | `CashRateOfSales` | 销售现金比率(%) | number(18,4) | ✓ | 94.73% | 销售现金比率(%)(CashRateOfSales)=经营活动产生的现金流量净额/营业总收入*100%。 |
| 52 | `NetProfitCashCover` | 归属母公司股东的净利润现金含量(%) | number(18,4) | ✓ | 94.92% | 归属母公司股东的净利润现金含量(%)(NetProfitCashCover)=经营活动产生的现金流量净额/归属母公司股东... |
| 53 | `OperatingReveCashCover` | 营业收入现金含量(%) | number(18,4) | ✓ | 92.7% | 营业收入现金含量（OperatingReveCashCover）=销售商品、提供劳务收到的现金/营业总收入*100%；仅... |
| 54 | `OperCashInToAsset` | 总资产现金回收率(%) | number(18,4) | ✓ | 92.99% | 总资产现金回收率(%)(OperCashInToAsset)=经营活动产生的现金流量净额/期末资产总额*100%； 该指... |
| 55 | `NetProfitCashCoverAll` | 净利润现金含量(含少数股东)(%) | number(18,4) | ✓ | 76.43% | 净利润现金含量(含少数股东)(%)(NetProfitCashCoverAll)=经营活动产生的现金流量净额/净利润*1... |
| 56 | `NOCFToOperatingProf` | 经营活动产生的现金流量净额/营业利润(%) | number(18,4) | ✓ | 74.95% | 经营活动产生的现金流量净额/营业利润(%)(NOCFToOperatingProf)=经营活动产生的现金流量净额/营业利... |
| 57 | `NOCFToOperatingNI` | 经营活动产生的现金流量净额/经营活动净收益(%) | number(18,4) | ✓ | 65.41% | 经营活动产生的现金流量净额/经营活动净收益(%)(NOCFToOperatingNI)=经营活动产生的现金流量净额/经营... |
| 58 | `CashPayStaffRatio` | 支付给职工的现金比率(%) | number(18,4) | ✓ | 91.68% | 支付给职工的现金比率(%)(CashPayStaffRatio)=支付给职工以及为职工支付的现金/销售商品、提供劳务收到... |
| 59 | `OperatingRevenueYOY` | 营业收入同比增长(%) | number(18,4) | ✓ | 90.42% | 营业收入同比增长(%)(OperatingRevenueYOY)=（本期营业总收入-上年同期营业总收入）/︱上年同期营业... |
| 60 | `NetProfitYOY` | 归属母公司股东的净利润同比增长(%) | number(18,4) | ✓ | 90.65% | 归属母公司股东的净利润同比增长(%)(NetProfitYOY)=（本期归属母公司股东的净利润-上年同期归属母公司股东的... |
| 61 | `NetProfitGrowRate` | 净利润同比增长(%) | number(18,4) | ✓ | 90.66% | 净利润同比增长(%)(NetProfitGrowRate)=（本期净利润-上年同期净利润）/︱上年同期净利润︱*100% |
| 62 | `OperProfitGrowRate` | 营业利润同比增长(%) | number(18,4) | ✓ | 90.66% | 营业利润同比增长(%)(OperProfitGrowRate)=（本期营业利润-上年同期营业利润）/︱上年同期营业利润︱... |
| 63 | `TotalProfeiGrowRate` | 利润总额同比增长(%) | number(18,4) | ✓ | 90.66% | 利润总额同比增长(%)(TotalProfeiGrowRate)=（本期利润总额-上年同期利润总额）/︱上年同期利润总额... |
| 64 | `TORGrowRate` | 营业总收入同比增长率(%) | number(18,4) | ✓ | 87.75% | 营业总收入同比增长率(%)(TORGrowRate)=（本期营业总收入-上年同期营业总收入）/︱上年同期营业总收入︱*1... |
| 65 | `ToOpCostGrowRate` | 营业总成本(含减值损失)同比增长(%) | number(18,4) | ✓ | 87.92% | 营业总成本(含减值损失)同比增长(%)(ToOpCostGrowRate)=（本期营业总成本(含减值损失)-上年同期营业... |
| 66 | `NPParentCompanyCutYOY` | 归属母公司股东的净利润(扣除)同比增长(%) | number(18,4) | ✓ | 44.52% | 归属母公司股东的净利润(扣除)同比增长(%)(NPParentCompanyCutYOY)=（本期归属母公司股东的净利润... |
| 67 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长(%) | number(18,4) | ✓ | 86.52% | 经营活动产生的现金流量净额同比增长(%)(NetOperateCashFlowYOY)=（本期经营活动产生的现金流量净额... |
| 68 | `CashEqIncreaseYOY` | 现金净流量同比增长(%) | number(18,4) | ✓ | 86.52% | 现金净流量同比增长(%)(CashEqIncreaseYOY)=（本期现金及现金等价物净增加额-上年同期现金及现金等价物... |
| 69 | `NAORYOY` | 净资产收益率(摊薄)同比增长(%) | number(18,4) | ✓ | 86.25% | 净资产收益率(摊薄)同比增长(%)(NAORYOY)=（本期净资产收益率(摊薄)-上年同期净资产收益率(摊薄)）/︱上年... |
| 70 | `NetAssetGrowRate` | 净资产同比增长(%) | number(18,4) | ✓ | 90.35% | 净资产同比增长(%)(NetAssetGrowRate)=（本期期末归属于母公司股东权益-上年同期期末归属于母公司股东权... |
| 71 | `TotalAssetGrowRate` | 总资产同比增长(%) | number(18,4) | ✓ | 90.76% | 总资产同比增长(%)(TotalAssetGrowRate)=（本期期末总资产-上年同期期末总资产/︱上年同期期末总资产... |
| 72 | `ToLiabGrowRate` | 总负债同比增长(%) | number(18,4) | ✓ | 90.53% | 总负债同比增长(%)(ToLiabGrowRate)=（本期期末总负债-上年同期期末总负债/︱上年同期期末总负债︱*10... |
| 73 | `CashEquivalGrowRate` | 货币资金同比增长率(%) | number(18,4) | ✓ | 53.11% | 货币资金同比增长率(%)(CashEquivalGrowRate)=（本期期末货币资金-上年同期期末货币资金/︱上年同期... |
| 74 | `FAExpansionRate` | 固定资产投资扩张率(%) | number(18,4) | ✓ | 87.1% | 固定资产投资扩张率(%)(FAExpansionRate)=（本期期末固定资产-上年同期期末固定资产）/ABS[上年同期... |
| 75 | `ARTRGrowRate` | 应收账款周转率增长率(%) | number(18,4) | ✓ | 84.44% | 应收账款周转率增长率(%)(ARTRGrowRate)=（本期应收帐款周转率-上年同期应收帐款周转率）/ABS上年同期应... |
| 76 | `FATRGrowRate` | 固定资产周转率增长率(%) | number(18,4) | ✓ | 83.22% | 固定资产周转率增长率(%)(FATRGrowRate)=（本期固定资产周转率-上年同期固定资产周转率)/ABS上年同期固... |
| 77 | `InventoryTRGrowRate` | 存货周转率增长率(%) | number(18,4) | ✓ | 84.24% | 存货周转率增长率(%)(InventoryTRGrowRate)=（本期存货周转率-上年同期存货周转率)/ABS上年同期... |
| 78 | `OperCashPSGrowRate` | 每股经营活动产生的现金流量同比增长率(%) | number(18,4) | ✓ | 82.83% | 每股经营活动产生的现金流量同比增长率(%)(OperCashPSGrowRate)=（本期每股经营活动现金流量-上年同期... |
| 79 | `OperatingRevenueMOM` | 营业收入环比增长(%) | number(18,4) | ✓ | 95.1% | 营业收入环比增长(%)(OperatingRevenueMOM)=（本季度营业总收入-上季度营业总收入）/︱上季度营业总... |
| 80 | `NetProfitMOM` | 归属母公司股东的净利润环比增长(%) | number(18,4) | ✓ | 95.28% | 归属母公司股东的净利润环比增长(%)(NetProfitMOM)=（本季度归属母公司股东的净利润-上季度归属母公司股东的... |
| 81 | `TOperatingRevenueMOM` | 营业总收入环比增长率(%) | number(18,4) | ✓ | 95.1% | 营业总收入环比增长率(%)(TOperatingRevenueMOM)=（本季度营业总收入-上季度营业总收入）/︱上季度... |
| 82 | `OperProfitMOM` | 营业利润环比增长率(%) | number(18,4) | ✓ | 95.29% | 营业利润环比增长率(%)(OperProfitMOM)=（本季度营业利润-上季度营业利润）/︱上季度营业利润︱*100% |
| 83 | `NetProfMOM` | 净利润环比增长率(%) | number(18,4) | ✓ | 95.29% | 净利润环比增长率(%)(NetProfMOM)=（本季度净利润-上季度净利润）/︱上季度净利润︱*100%。 |
| 84 | `OperCashInToDueDebt` | 现金到期债务比(%) | number(18,4) | ✓ | 85.9% | 现金到期债务比(%)(OperCashInToDueDebt)=经营活动产生的现金流量净额/（短期借款+一年内到期的非流... |
| 85 | `OperCashToCurrentDebt` | 经营活动产生的现金流量净额/流动负债(%) | number(18,4) | ✓ | 90.72% | 经营活动产生的现金流量净额/流动负债(%)(OperCashToCurrentDebt)=经营活动产生的现金流量净额/期... |
| 86 | `OperCashInToTotalDebt` | 现金债务总额比(%) | number(18,4) | ✓ | 92.94% | 现金债务总额比(%)(OperCashInToTotalDebt)=经营活动产生的现金流量净额/期末负债总额*100%；... |
| 87 | `EPS` | 每股收益(摊薄)(元) | number(19,5) | ✓ | 98.7% | 每股收益(摊薄)(元)(EPS)=本期归属于母公司的净利润/本报告期期末总股本。 |
| 88 | `EPSCut` | 每股收益(扣除)(元/股) | number(19,4) | ✓ | 50.6% | 每股收益(扣除)(元/股)(EPSCut)=扣除非经常损益后的归属母公司净利润/总股本； 该指标金融类和非金融类公司都计... |
| 89 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(19,4) | ✓ | 94.1% | 每股经营活动产生的现金流量净额(元/股)(OperCashFlowPS)=经营活动产生的现金流量净额/总股本； 该指标金... |
| 90 | `OperProfitPS` | 每股营业利润(元/股) | number(19,4) | ✓ | 98.7% | 每股营业利润(元/股)(OperProfitPS)=营业利润/总股本； 该指标金融类和非金融类公司都计算。 |
| 91 | `EBITPS` | 每股息税前利润(反推)(元/股) | number(18,4) | ✓ | 95.45% | 每股息税前利润(反推)(元/股)(EBITPS)=息税前利润(反推)EBIT/期末总股本。 |
| 92 | `MainIncomePS` | 每股营业收入(元/股) | number(18,4) | ✓ | 98.59% | 每股营业收入(元/股)(MainIncomePS)=营业收入/期末总股本。 |
| 93 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(18,4) | ✓ | 98.69% | 每股营业总收入(元/股)(TotalOperateRevenuePS)=营业总收入/期末总股本。 |
| 94 | `CashFlowPS` | 每股现金流量净额(元/股) | number(18,4) | ✓ | 94.1% | 每股现金流量净额(元/股)(CashFlowPS)=现金及现金等价物净增加额/期末总股本。 |
| 95 | `ValueChangeNIToTP` | 价值变动净收益/利润总额(%) | number(18,4) | ✓ | 69.26% | 价值变动净收益/利润总额(%)(ValueChangeNIToTP)=价值变动净收益／利润总额*100，其中，“价值变动... |
| 96 | `OperatingNIToTP` | 经营活动净收益/利润总额(%) | number(18,4) | ✓ | 81.5% | 经营活动净收益/利润总额(%)(OperatingNIToTP)=经营活动净收益／利润总额*100，其中“经营活动净收益... |
| 97 | `NetNonOperaIncomeToTP` | 营业外收支净额/利润总额(%) | number(18,4) | ✓ | 80.32% | 营业外收支净额/利润总额(%)(NetNonOperaIncomeToTP)=(营业外收入-营业外支出)/利润总额*10... |
| 98 | `OperProfitToTP` | 营业利润/利润总额(%) | number(18,4) | ✓ | 99.83% | 营业利润/利润总额(%)(OperProfitToTP)=营业利润/利润总额*100。 |
| 99 | `NPCutToTP` | 扣除非经常损益后的归母净利润/净利润(%) | number(18,4) | ✓ | 50.6% | 扣除非经常损益后的归母净利润/净利润(%)(NPCutToTP)=扣除非经常损益后的归母净利润/净利润*100。 |
| 100 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 101 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 102 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### BulletinType (公告类型)

公告类型(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类型的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,3)，得到合并调整标志的具体描述：1-是，2-否，3-前。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### NPFromParentCompanyOwners (归属母公司股东的净利润(元))

归属母公司股东的净利润(元)（NPFromParentCompanyOwners）：根据“归属于母公司所有者的净利润“计算，其中，单季度算法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。

### NetProfitCut (扣除非经常性损益后的归母净利润(元))

扣除非经常性损益后的归母净利润(元)(NetProfitCut)：优先取原文披露值，原文未披露，则根据“归属母公司股东的净利润-非经常性损益”计算。

### NetIncFromValueChange (价值变动净收益(元))

价值变动净收益（NetIncFromValueChange）=投资净收益+公允价值变动净收益+汇兑收益。

### NetIncomeFromOperating (经营活动净收益(元))

经营活动净收益(元)(NetIncomeFromOperating)：对于非金融类企业，经营活动净收益＝营业总收入－营业总成本（含减值损失）；对于金融类企业，经营活动净收益＝营业收入－营业支出－（投资净收益＋公允价值变动净收益＋汇兑收益+其他收益+资产处置收益）

### EBIT (息税前利润(反推)(元))

息税前利润(反推)(元)(EBIT)：利润总额＋利息费用 其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用=利息费用(财务费用)+利息收入(财务费用)；若利润表未披露明细，则用报表附注的数据计算：利息费用=利息支出-利息收入-资本化利息支出；若报表附注中未披露，则用报表的“财务费用”代替；金融类企业不计算。

### NetProfitRatio (销售净利率_不含少数股东损益(%))

销售净利率_不含少数股东损益(%)(NetProfitRatio)=归属于母公司的净利润/营业总收入*100%；

## SQL示例

```sql
-- 查询 公司单季财务指标_新会计准则 数据
SELECT *
FROM lc_qfinancialindexnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
