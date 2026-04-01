# HK_IncomeStatementBHK

**中文名**: 港股利润分配表_银行(香港会计准则)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IncomeStatementBHK` |
| MySQL表名 | `hk_incomestatementbhk` |
| 中文名 | 港股利润分配表_银行(香港会计准则) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 72 |
| 版本 | 1.07 |

## 表描述

1.介绍按香港会计准则、国际会计准则等披露的港股银行利润分配表中各项标准化会计指标。该表为港股利润分配表的横表。
2.表内“减项”类字段统一以负数形式展示。
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
| 6 | `ReportType` | 报表类型 | varchar2(100) | ✓ | 100.0% |   报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生... |
| 7 | `FiscalYear` | 财政年度 | date | ✓ | 100.0% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 8 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM... |
| 9 | `BeginDate` | 开始日期 | date | ✓ | 100.0% |  |
| 10 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 11 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN... |
| 12 | `CompanyNature` | 报表格式类型 | number(10) | ✓ | 100.0% | 报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN... |
| 13 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 14 | `Gmark` | 聚源转换标识 | number(10) | ✓ | 100.0% | 聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。 |
| 15 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)：1-完整；2-简表。 |
| 16 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 17 | `NetInterestIncome` | 净利息收入(元) | number(19,4) | ✓ | 97.04% | 净利息收入(元)(NetInterestIncome)：优先取财报披露值，如财报未披露，则净利息收入=利息收入(元)(I... |
| 18 | `InterestIncome` | ###其中:利息收入(元) | number(19,4) | ✓ | 95.34% |  |
| 19 | `InterestExpense` | #######利息支出(元)(减项) | number(19,4) | ✓ | 92.05% |  |
| 20 | `NetServiceIncome` | 净服务费收入(元) | number(19,4) | ✓ | 79.43% | 净服务费收入(元)(NetServiceIncome)：优先取财报披露值，如财报未披露，则净服务费收入=服务费收入(元)... |
| 21 | `ServiceIncome` | ###其中:服务费收入(元) | number(19,4) | ✓ | 73.0% |  |
| 22 | `ServiceCharge` | #######服务费支出(元)(减项) | number(19,4) | ✓ | 70.54% |  |
| 23 | `DividendIncome` | 股息收入(元) | number(19,4) | ✓ | 15.99% |  |
| 24 | `NetTransIncome` | 外汇交易净收入(元) | number(19,4) | ✓ | 45.03% |  |
| 25 | `SecuAndInvestIncome` | 证券交易及投资净收入(元) | number(19,4) | ✓ | 51.1% |  |
| 26 | `NetRentIncome` | 租金净收入(元) | number(19,4) | ✓ | 1.32% |  |
| 27 | `NetRemittance` | 汇兑净额(元) | number(19,4) | ✓ | 5.47% |  |
| 28 | `NetIFInsAtFairValue` | 以公平值列账的金融工具净收益(元) | number(19,4) | ✓ | 16.68% |  |
| 29 | `NetOpenHedgeIncome` | 净敞口套期收益(元) | number(19,4) | ✓ | 1.32% |  |
| 30 | `ProfitDispOfAssets` | 出售资产之溢利(元) | number(19,4) | ✓ | 4.74% |  |
| 31 | `SpeItemsOperatRevenue` | 经营收入特殊项目(元) | number(19,4) | ✓ | 96.89% |  |
| 32 | `AdjItemsOperatRevenue` | 经营收入调整项目(元) | number(19,4) | ✓ | 0.29% |  |
| 33 | `OperatingRevenue` | 经营收入(元) | number(19,4) | ✓ | 99.15% | 经营收入(元)(OperatingRevenue)：优先取财报披露值，如财报未披露，则经营收入=净利息收入(元)(Net... |
| 34 | `OperatingPayoutBD` | 营业支出-扣除减值前(元)(减项) | number(19,4) | ✓ | 75.67% |  |
| 35 | `NetInsClaAPolHoldLiab` | 保险索偿净额及保单持有负债(元)(减项) | number(19,4) | ✓ | 7.09% |  |
| 36 | `SpeItemsBefDedImp` | 经营溢利(扣除减值前)特殊项目目(元) | number(19,4) | ✓ | 8.49% |  |
| 37 | `AdjItemsBefDedImp` | 经营溢利(扣除减值前)调整项目(元) | number(19,4) | ✓ | 0.09% |  |
| 38 | `OpeProfitBefDedImp` | 经营溢利(扣除减值前)(元) | number(19,4) | ✓ | 98.9% | 经营溢利(扣除减值前)(元)(OpeProfitBefDedImp)：优先取财报披露值，如财报未披露，则经营溢利(扣除减... |
| 39 | `DevalAndAccBadDebt` | 减值及拨备(元)(减项) | number(19,4) | ✓ | 83.4% | 减值及拨备(元)(减项)(DevalAndAccBadDebt)：优先取财报披露值，如财报未披露，则减值及拨备=呆坏帐准... |
| 40 | `LoansAdvancesImp` | ######贷款及垫款资产减值(元)(减项) | number(19,4) | ✓ | 22.18% |  |
| 41 | `HeldToMatInvImp` | ######持至到期投资减值(元)(减项) | number(19,4) | ✓ | 2.85% |  |
| 42 | `AvaForSaleFinAsImp` | ######可供出售金融资产减值(元)(减项) | number(19,4) | ✓ | 1.95% |  |
| 43 | `GoodwillImp` | ######商誉减值(元)(减项) | number(19,4) | ✓ | 1.02% |  |
| 44 | `OtherAssetsImp` | ######其他资产减值损失(元)(减项) | number(19,4) | ✓ | 70.31% |  |
| 45 | `SpeItemsOPAfImp` | 经营溢利(扣除减值后)特殊项目(元) | number(19,4) | ✓ | 2.29% |  |
| 46 | `AdjItemsOPAfImp` | 经营溢利(扣除减值后)调整项目(元) | number(19,4) | ✓ | 0.08% |  |
| 47 | `OpeProfitAfDedImp` | 经营溢利(扣除减值后)(元) | number(19,4) | ✓ | 98.61% | 经营溢利(扣除减值后)(元)(OpeProfitAfDedImp)：优先取财报披露值，如财报未披露，则经营溢利(扣除减值... |
| 48 | `OperatingPayoutAD` | 营业支出-扣除减值后(元)(减项) | number(19,4) | ✓ | 19.1% | 营业支出-扣除减值后（OperatingPayoutAD）如果原始财报没有披露营业支出-扣除减值后的数据，则营业支出-扣... |
| 49 | `EmpTurnover` | ###其中:雇员报酬及福利(元)(减项) | number(19,4) | ✓ | 5.17% |  |
| 50 | `DevAImpProPlEquip` | ######物业、机器及设备折旧与减值(元)(减项) | number(19,4) | ✓ | 3.95% |  |
| 51 | `AmorAImpIntangAssets` | ######无形资产摊销及减值(元)(减项) | number(19,4) | ✓ | 3.59% |  |
| 52 | `OperatingAndAdminExpense` | ######业务及管理费(元)(减项) | number(19,4) | ✓ | 9.26% |  |
| 53 | `OperatingTaxSurcharges` | ######税金及附加(元)(减项) | number(19,4) | ✓ | 8.47% |  |
| 54 | `SpeItemsOpePayout` | ######营业支出其他项目(元)(减项) | number(19,4) | ✓ | 17.87% |  |
| 55 | `AdjItemsOpePayout` | ######营业支出调整项目(元)(减项) | number(19,4) | ✓ | 0.0% |  |
| 56 | `SpeItemsOpeProfit` | 经营溢利其他项目(元) | number(19,4) | ✓ | 22.44% |  |
| 57 | `AdjItemsOpeProfit` | 经营溢利调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 58 | `OperatingProfit` | 经营溢利(元) | number(19,4) | ✓ | 98.64% | 经营溢利(元)(OperatingProfit)：优先取财报披露值，如财报未披露，则经营溢利=经营溢利(扣除减值后)(元... |
| 59 | `NPDispAvaFSaleSecu` | 处置金融工具净收益(元) | number(19,4) | ✓ | 4.34% |  |
| 60 | `NPDispInvestProp` | 处置投资性房地产净收益(元) | number(19,4) | ✓ | 2.31% |  |
| 61 | `NPDispAffilComp` | 处置长期股权投资净收益(元) | number(19,4) | ✓ | 4.45% |  |
| 62 | `NPDispFixedAssets` | 处置固定资产净收益(元) | number(19,4) | ✓ | 9.45% |  |
| 63 | `RevaluationSurplus` | 重估盈余(元) | number(19,4) | ✓ | 8.27% |  |
| 64 | `AffiliatedComFrofit` | 应占联营公司溢利(元) | number(19,4) | ✓ | 52.66% |  |
| 65 | `AttriToProfJVent` | 应占合营公司溢利(元) | number(19,4) | ✓ | 11.9% |  |
| 66 | `SpeItemsEBefTax` | 溢利特殊项目(元) | number(19,4) | ✓ | 30.61% |  |
| 67 | `AdjItemsEBefTax` | 溢利调整项目(元) | number(19,4) | ✓ | 7.4% |  |
| 68 | `EarningBeforeTax` | 除税前溢利(元) | number(19,4) | ✓ | 98.73% | 除税前溢利(元)(EarningBeforeTax)：优先取财报披露值，如财报未披露，则除税前溢利=经营溢利(元)(Op... |
| 69 | `IncomeTaxCost` | 所得税费用(元)(减项) | number(19,4) | ✓ | 97.2% | 所得税费用(减项)(IncomeTaxCost)：优先取财报披露值，如财报未披露，则所得税费用(减项)=税项(元)(减项... |
| 70 | `Tax` | ###其中:税项(元)(减项) | number(19,4) | ✓ | 97.2% |  |
| 71 | `DeferredTax` | ###其中:递延税项(元)(减项) | number(19,4) | ✓ | 0.62% |  |
| 72 | `AftaxProfitFCBusi` | 持续经营业务税后利润(元) | number(19,4) | ✓ | 98.54% | 持续经营业务税后利润（AftaxProfitFCBusi）如果原始财报没有披露持续经营业务税后利润的数据，则持续经营业务... |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSource (信息来源代码)

信息来源代码(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IVALUE IN (1,3)，得到信息来源代码的具体描述：

### ReportType (报表类型)

 
报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年变更，如年度报告累计报告期是18或15个月，对应披露的12个月中期数据)、第五季报(企业发生财年变更，如年度报告累计报告期是18个月，对应披露的15个月中期数据)、年度报告、其他（企业披露的非标准报告期数据，如1、2、4、5等月，或者非完整累计月度报告数据）等。

### FiscalYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”。

### PeriodMark (日期标志)

日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314 and DM not in (90)，得到日期标志的具体描述：

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511  AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：

### CompanyNature (报表格式类型)

报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN (4,5)，得到报表格式类型的具体描述：1-普通，2-金融，3-保险，6-证券，7-信托。本表报表格式类型(CompanyNature)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，其中证券和信托因披露形式与一般类企业类似，但是又存在一定区别，所以单独分类展示。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则的具体描述：

### Gmark (聚源转换标识)

聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。

### IfComplete (完整标志)

完整标志(IfComplete)：1-完整；2-简表。

## SQL示例

```sql
-- 查询 港股利润分配表_银行(香港会计准则) 数据
SELECT *
FROM hk_incomestatementbhk
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
