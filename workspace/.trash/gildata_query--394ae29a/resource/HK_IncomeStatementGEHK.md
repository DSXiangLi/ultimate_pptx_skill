# HK_IncomeStatementGEHK

**中文名**: 港股利润分配表_一般企业(香港会计准则)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IncomeStatementGEHK` |
| MySQL表名 | `hk_incomestatementgehk` |
| 中文名 | 港股利润分配表_一般企业(香港会计准则) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 88 |
| 版本 | 1.07 |

## 表描述

1.介绍按香港会计准则、国际会计准则等披露的港股一般企业利润分配表中各项标准化会计指标。该表为港股利润分配表的横表。
2.表内“减项”类字段统一以负数形式展示；
3.数据范围：1999年至今。
4.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IV... |
| 5 | `InfoSourceDes` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ReportType` | 报表类型 | varchar2(100) | ✓ | 100.0% | 报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年... |
| 7 | `FiscalYear` | 财政年度 | date | ✓ | 100.0% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 8 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM... |
| 9 | `BeginDate` | 开始日期 | date | ✓ | 100.0% |  |
| 10 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 11 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN... |
| 12 | `CompanyNature` | 报表格式类型 | number(10) | ✓ | 100.0% | 报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN... |
| 13 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 14 | `Gmark` | 聚源转换标识 | number(10) | ✓ | 100.0% | 聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。 |
| 15 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)：1-完整；2-简表。 |
| 16 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068  AND... |
| 17 | `Turnover` | 营业额(元) | number(19,4) | ✓ | 97.78% |  |
| 18 | `SpeItemsOR` | 营业收入特殊项目(元) | number(19,4) | ✓ | 1.94% |  |
| 19 | `AdjItemsOR` | 营业收入调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 20 | `OperatingIncome` | 营业收入(元) | number(19,4) | ✓ | 98.34% | 营业收入(元)(OperatingIncome)：优先取财报披露值，如财报未披露，则营业收入=营业额(元)(Turnov... |
| 21 | `SalesCost` | 销售成本(元)(减项) | number(19,4) | ✓ | 79.21% |  |
| 22 | `OtherCost` | 其他成本(元)(减项) | number(19,4) | ✓ | 1.3% |  |
| 23 | `OperExpenses` | 营运支出(元)(减项) | number(19,4) | ✓ | 87.52% | 营运支出(元)(减项)(OperExpenses)：优先取财报披露值，如财报未披露，则营运支出=销售成本(元)(减项)(... |
| 24 | `SpeItemsGrossProfit` | 毛利特殊项目(元) | number(19,4) | ✓ | 0.31% |  |
| 25 | `AdjItemsGrossProfit` | 毛利调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 26 | `GrossProfit` | 毛利(元) | number(19,4) | ✓ | 87.98% | 毛利(元)(GrossProfit)：优先取财报披露值，如财报未披露，则 报表格式类型(CompanyNature)=1... |
| 27 | `OperatingTaxSurcharges` | 税金及附加(元)(减项) | number(19,4) | ✓ | 9.4% |  |
| 28 | `OpeExpenseAE` | 销售费用(元)(减项) | number(19,4) | ✓ | 69.99% |  |
| 29 | `AdmExpensesAE` | 管理费用(元)(减项) | number(19,4) | ✓ | 85.76% |  |
| 30 | `RAndDExpensesAE` | 研发支出(元)(减项) | number(19,4) | ✓ | 14.32% |  |
| 31 | `ProfitDispOfAssets` | 出售资产溢利(元)(减项) | number(19,4) | ✓ | 8.38% |  |
| 32 | `EmpTurnover` | 员工支销(元)(减项) | number(19,4) | ✓ | 10.69% |  |
| 33 | `DepDividerSale` | 折旧与摊销(元)(减项) | number(19,4) | ✓ | 11.42% |  |
| 34 | `OpeInterestExpense` | 营运利息支出(元)(减项) | number(19,4) | ✓ | 7.5% |  |
| 35 | `RevaluationSurplus` | 重估盈余(元) | number(19,4) | ✓ | 19.44% |  |
| 36 | `CInFVofInvPropert` | ###其中:投资物业公平值变动(元) | number(19,4) | ✓ | 8.71% |  |
| 37 | `CInFVofDerFinInst` | ######衍生金融工具公平值变动(元) | number(19,4) | ✓ | 1.59% |  |
| 38 | `CInFVofFinAssets` | ######财务资产公平值变动(元) | number(19,4) | ✓ | 4.01% |  |
| 39 | `CInFVofOtherAssets` | ######其他资产公平值变动(元) | number(19,4) | ✓ | 8.11% |  |
| 40 | `DevalAndAccBadDebt` | 减值及拨备(元)(减项) | number(19,4) | ✓ | 27.82% | 减值及拨备(元)(减项)(DevalAndAccBadDebt)：优先取财报披露值，如财报未披露，则减值及拨备=无形资产... |
| 41 | `DevalofIntangAssets` | ###其中:无形资产减值(元)(减项) | number(19,4) | ✓ | 0.93% |  |
| 42 | `DevalofProPlEquip` | #######物业、机器及设备减值(元)(减项) | number(19,4) | ✓ | 2.05% |  |
| 43 | `DevalofAvaForSaleInv` | #######可供出售投资减值(元)(减项) | number(19,4) | ✓ | 0.6% |  |
| 44 | `DevalofGoodwill` | #######商誉减值(元)(减项) | number(19,4) | ✓ | 1.42% |  |
| 45 | `DevalofOthers` | #######其他减值及拨备(减项)(元) | number(19,4) | ✓ | 25.61% |  |
| 46 | `SpeItemsOperateProfit` | 经营溢利特殊项目(元) | number(19,4) | ✓ | 96.17% |  |
| 47 | `AdjItemsOperateProfit` | 经营溢利调整项目(元) | number(19,4) | ✓ | 0.23% |  |
| 48 | `OperatingProfit` | 经营溢利(元) | number(19,4) | ✓ | 99.51% | 经营溢利(元)(OperatingProfit)：优先取财报披露值，如财报未披露，则经营溢利=毛利(元)(GrossPr... |
| 49 | `FinancialExpense` | 融资费用(元)(减项) | number(19,4) | ✓ | 83.51% | 融资费用(元)(减项)(FinancialExpense)：优先取财报披露值，如财报未披露，则融资费用=融资成本(元)(... |
| 50 | `FundingCost` | ##其中:融资成本(元)(减项) | number(19,4) | ✓ | 81.48% |  |
| 51 | `FinancingIncome` | ##其中:融资收入(元) | number(19,4) | ✓ | 15.32% |  |
| 52 | `AffiliatedComFrofit` | 应占联营公司溢利(元) | number(19,4) | ✓ | 30.84% |  |
| 53 | `JointVenturesProfit` | 应占合营公司溢利(元) | number(19,4) | ✓ | 10.81% |  |
| 54 | `CooperateBusProfit` | 应占共同控制实体溢利(元) | number(19,4) | ✓ | 4.74% |  |
| 55 | `SpeItemsProfits` | 溢利特殊项目(元) | number(19,4) | ✓ | 16.47% |  |
| 56 | `AdjItemsProfits` | 溢利调整项目(元) | number(19,4) | ✓ | 8.62% |  |
| 57 | `EarningBeforeTax` | 除税前溢利(元) | number(19,4) | ✓ | 99.48% | 除税前溢利(元)(EarningBeforeTax)：优先取财报披露值，如财报未披露，则除税前溢利=经营溢利(元)(Op... |
| 58 | `IncomeTaxCost` | 所得税费用(元)(减项) | number(19,4) | ✓ | 86.65% | 所得税费用(减项)(IncomeTaxCost)：优先取财报披露值，如财报未披露，则以税项(元)(减项)(Tax)+递延... |
| 59 | `Tax` | ##其中:税项(元)(减项) | number(19,4) | ✓ | 86.64% |  |
| 60 | `DeferredTax` | ##其中:递延税项(元)(减项) | number(19,4) | ✓ | 0.26% |  |
| 61 | `AftaxProfitFCBusi` | 持续经营业务税后利润(元) | number(19,4) | ✓ | 99.46% | 持续经营业务税后利润（AftaxProfitFCBusi）：若原始报表没有披露持续经营业务税后利润数据，则持续经营业务税... |
| 62 | `AftaxProfitFNCBusi` | 非持续经营业务税后溢利(元) | number(19,4) | ✓ | 5.23% |  |
| 63 | `SpeItemsAftaxProfit` | 除税后溢利特殊项目(元) | number(19,4) | ✓ | 0.45% |  |
| 64 | `AdjItemsAftaxProfit` | 除税后溢利调整项目(元) | number(19,4) | ✓ | 0.14% |  |
| 65 | `EarningAfterTax` | 除税后溢利(元) | number(19,4) | ✓ | 99.54% | 除税后溢利(元)(EarningAfterTax)：优先取财报披露值，如财报未披露，则除税前溢利(元)(EarningB... |
| 66 | `AttriToMSholdFCBprof` | ##少数股东应占来自持续业务溢利(元) | number(19,4) | ✓ | 1.69% |  |
| 67 | `AttriToMSholdFNCBprof` | ##少数股东应占来自非持续业务溢利(元) | number(19,4) | ✓ | 0.99% |  |
| 68 | `MinorityProfit` | 少数股东损益(元) | number(19,4) | ✓ | 59.52% | 少数股东损益（MinorityProfit）：优先取财报披露值，如财报未披露，则少数股东损益=少数股东应占来自持续业务溢... |
| 69 | `AttriToSholdFCBprof` | ##股东应占来自持续业务溢利(元) | number(19,4) | ✓ | 3.07% |  |
| 70 | `AttriToSholdFNCBprof` | ##股东应占来自非持续业务溢利(元) | number(19,4) | ✓ | 2.23% |  |
| 71 | `SpeItemsProfTSholders` | 股东应占溢利其他项目(元) | number(19,4) | ✓ | 0.84% |  |
| 72 | `AdjItemsProfTSholders` | 股东应占溢利调整项目(元) | number(19,4) | ✓ | 0.08% |  |
| 73 | `ProfitToShareholders` | 股东应占溢利(元) | number(19,4) | ✓ | 99.64% | 股东应占溢利（ProfitToShareholders）：优先取财报披露值，如财报未披露，则股东应占溢利=股东应占来自持... |
| 74 | `ProfitToComShold` | ##其中:普通股股东应占溢利(元) | number(19,4) | ✓ | 99.44% |  |
| 75 | `NPOtherEqinstruments` | ##其中:归属于母公司其他权益工具持有者的净利润(元) | number(19,4) | ✓ | 0.22% |  |
| 76 | `EPSBasic` | 每股基本盈利(元) | number(19,4) | ✓ | 91.59% | 每股基本盈利(元)(EPSBasic):财报披露值。 |
| 77 | `EPSBasicFCBusi` | ##其中:来自持续业务每股基本盈利(元) | number(19,4) | ✓ | 6.48% |  |
| 78 | `EPSBasicFNCBusi` | #####来自非持续业务每股基本盈利(元) | number(19,4) | ✓ | 1.71% |  |
| 79 | `EPS` | 每股摊薄盈利(元) | number(19,4) | ✓ | 67.34% | 每股摊薄盈利(元)(EPS):财报披露值。 |
| 80 | `EPSFCBusi` | ##其中:来自持续业务每股摊薄盈利(元) | number(19,4) | ✓ | 5.13% |  |
| 81 | `EPSFNCBusi` | #####来自非持续业务每股摊薄盈利(元) | number(19,4) | ✓ | 1.43% |  |
| 82 | `Dividend` | 股息(元) | number(19,4) | ✓ | 8.12% | 股息(元)(Dividend):财报披露值。 |
| 83 | `DividendPerShare` | 每股股息(元) | number(19,4) | ✓ | 0.73% | 每股股息(元)(DividendPerShare):财报披露值。 |
| 84 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 85 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 86 | `JSID` | JSID | number(19) | ✗ |  |  |
| 87 | `EmpTurnoverOP` | 员工支销-营业支出(元) | number(19,4) | ✓ | 0.0% |  |
| 88 | `DepDividerSaleOP` | 折旧与摊销-营业支出(元) | number(19,4) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSource (信息来源代码)

信息来源代码(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IVALUE IN (1,3)，得到信息来源代码的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，27-配发结果，28-修改已刊发的财务报表及报告，29-修正重大错误而做出的前期调整，30-修订已刊发初步业绩的资料，32-内幕消息-年度报告，33-内幕消息-第一季报，34-内幕消息-第二季报，35-内幕消息-第三季报，36-内幕消息-第四季报，37-内幕消息-中期报告，38-内幕消息-申请版本，39-内幕消息-招股章程，40-内幕消息-聆讯后资料集，41-内幕消息-其他，99-其他。

### ReportType (报表类型)

报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年变更，如年度报告累计报告期是18或15个月，对应披露的12个月中期数据)、第五季报(企业发生财年变更，如年度报告累计报告期是18个月，对应披露的15个月中期数据)、年度报告、其他（企业披露的非标准报告期数据，如1、2、4、5等月，或者非完整累计月度报告数据）等。

### FiscalYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”。

### PeriodMark (日期标志)

日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM not in (90)，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，99-其他。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整。

### CompanyNature (报表格式类型)

报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN (4,5)，得到报表格式类型的具体描述：1-普通，2-金融，3-保险，6-证券，7-信托。本表报表格式类型(CompanyNature)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，其中证券和信托因披露形式与一般类企业类似，但是又存在一定区别，所以单独分类展示。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则的具体描述：7-国际会计准则，110-香港会计准则，120-澳门会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则(2007)，521-中国会计准则(1993)。

### Gmark (聚源转换标识)

聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。

### IfComplete (完整标志)

完整标志(IfComplete)：1-完整；2-简表。

## SQL示例

```sql
-- 查询 港股利润分配表_一般企业(香港会计准则) 数据
SELECT *
FROM hk_incomestatementgehk
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
