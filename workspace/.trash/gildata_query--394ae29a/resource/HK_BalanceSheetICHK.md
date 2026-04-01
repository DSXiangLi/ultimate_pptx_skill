# HK_BalanceSheetICHK

**中文名**: 港股资产负债表_保险(香港会计准则)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_BalanceSheetICHK` |
| MySQL表名 | `hk_balancesheetichk` |
| 中文名 | 港股资产负债表_保险(香港会计准则) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 滚动更新 |
| 字段数量 | 113 |
| 版本 | 1.06 |

## 表描述

1.介绍按香港会计准则、国际会计准则等披露的港股保险公司资产负债表中各项标准化会计指标。该表为港股资产负债表的横表。
2.数据范围：2000年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `InfoSourceCode` | 信息来源代码 | number(10) | ✓ | 100.0% | 信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AN... |
| 6 | `ReportType` | 报表类型 | varchar2(100) | ✓ | 100.0% | 报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年... |
| 7 | `FiscalYear` | 财政年度 | date | ✓ | 100.0% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 8 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与系统常量表中的DM字段关联，令LB = 1314 and DM not in (90)... |
| 9 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 10 | `Mark` | 合并调整标志 | number(10) | ✗ | 100.0% | 合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN ... |
| 11 | `CompanyNature` | 报表格式类型 | number(10) | ✓ | 100.0% | 报表格式类型(CompanyNature)与系统常量表中的DM字段关联，令LB = 1356 AND DM NOT IN... |
| 12 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 13 | `Gmark` | 聚源转换标识 | number(10) | ✓ | 100.0% | 聚源转换标识(Gmark):1-是，2-否。标识本组数据是否进行会计准则转换。 |
| 14 | `IfComplete` | 完整标志 | number(10) | ✓ | 100.0% | 完整标志(IfComplete)：1-完整；2-简表。 |
| 15 | `CurrencyUnit` | 货币单位 | number(10) | ✗ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 16 | `DepositCardIA` | 存款证(元) | number(19,4) | ✓ | 2.5% |  |
| 17 | `FixedDeposit` | 定期存款(元) | number(19,4) | ✓ | 60.68% |  |
| 18 | `ReserveDeposits` | 法定存款(元) | number(19,4) | ✓ | 6.96% |  |
| 19 | `Cash` | 现金及等价物(元) | number(19,4) | ✓ | 98.88% |  |
| 20 | `IsContractualAssets` | 保险合同资产(元) | number(19,4) | ✓ | 8.18% |  |
| 21 | `ReinsAssets` | 再保险合同资产(元) | number(19,4) | ✓ | 36.5% |  |
| 22 | `RefCapDeposit` | 存出资本保证金(元) | number(19,4) | ✓ | 46.33% |  |
| 23 | `PrepaidLeasePays` | 预付租赁付款(元) | number(19,4) | ✓ | 8.82% |  |
| 24 | `InvestIncRece` | 应收投资收益(元) | number(19,4) | ✓ | 14.88% |  |
| 25 | `InsuranceReceivables` | 应收保费(元) | number(19,4) | ✓ | 46.07% |  |
| 26 | `ReinsuranceReceivables` | 应收分保账款(元) | number(19,4) | ✓ | 22.37% |  |
| 27 | `InsAndOthRece` | 保险及其他应收款项(元) | number(19,4) | ✓ | 12.86% |  |
| 28 | `InvestInLoansAndRece` | 归入贷款及应收款的投资(元) | number(19,4) | ✓ | 12.7% |  |
| 29 | `SecuInvestment` | 证券投资(元) | number(19,4) | ✓ | 11.05% |  |
| 30 | `FinAetAtFValTPL` | 按公平值入损益金融资产(元) | number(19,4) | ✓ | 57.07% |  |
| 31 | `HoldForSaleAssets` | 可供出售金融资产(元) | number(19,4) | ✓ | 39.11% |  |
| 32 | `BoughtSellbackSecu` | 买入返售证券(元) | number(19,4) | ✓ | 47.77% |  |
| 33 | `EquUTFundInvPort` | 股本证券及单位信托基金投资组合(元) | number(19,4) | ✓ | 1.17% |  |
| 34 | `InvInAsJointVen` | 于联营企业和合营企业的投资(元) | number(19,4) | ✓ | 40.33% |  |
| 35 | `HoldToMatInv` | 持有至到期投资(元) | number(19,4) | ✓ | 38.31% |  |
| 36 | `SubCompanyEquity` | 联营公司权益(元) | number(19,4) | ✓ | 14.29% |  |
| 37 | `InvestProperty` | 投资物业(元) | number(19,4) | ✓ | 71.52% |  |
| 38 | `WorkshopAndEquipment` | 物业厂房及设备(元) | number(19,4) | ✓ | 51.59% |  |
| 39 | `DeferredTaxAssets` | 递延税项资产(元) | number(19,4) | ✓ | 66.26% |  |
| 40 | `Borrowings` | 贷款(元) | number(19,4) | ✓ | 21.09% |  |
| 41 | `InsurerImpawnLoan` | 保户质押贷款(元) | number(19,4) | ✓ | 22.95% |  |
| 42 | `DebtsSecurities` | 债务证券(元) | number(19,4) | ✓ | 3.56% |  |
| 43 | `RecoverTax` | 可收回税项(元) | number(19,4) | ✓ | 10.26% |  |
| 44 | `OtherFinAssets` | 其他金融资产(元) | number(19,4) | ✓ | 1.59% |  |
| 45 | `OtherReceivable` | 其他应收款(元) | number(19,4) | ✓ | 13.92% |  |
| 46 | `DebtInvestment` | 债权投资(元) | number(19,4) | ✓ | 13.92% |  |
| 47 | `OthDebtInvestment` | 其他债权投资(元) | number(19,4) | ✓ | 13.44% |  |
| 48 | `OthEquityInstrument` | 其他权益工具投资(元) | number(19,4) | ✓ | 12.86% |  |
| 49 | `FinAssetsAtFValTOCI` | 按公平值计入其他全面收益的金融资产(元) | number(19,4) | ✓ | 1.01% |  |
| 50 | `UsufructAssets` | 使用权资产(元) | number(19,4) | ✓ | 25.66% |  |
| 51 | `GoodwillIntangibleAssets` | 商誉及无形资产(元) | number(19,4) | ✓ | 73.09% | 商誉及无形资产(元)(GoodwillIntangibleAssets)：优先取财报披露值，如财报未披露，则商誉及无形资... |
| 52 | `IntangibleAssets` | 其中:无形资产(元) | number(19,4) | ✓ | 62.69% |  |
| 53 | `Goodwill` | 其中:商誉(元) | number(19,4) | ✓ | 21.66% |  |
| 54 | `DeriFinAssets` | 衍生性金融资产(元) | number(19,4) | ✓ | 26.22% |  |
| 55 | `AExcepItems` | 资产特殊项目(元) | number(19,4) | ✓ | 99.52% |  |
| 56 | `AAdjItems` | 资产调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 57 | `TotalAssets` | 总资产(元) | number(19,4) | ✓ | 100.0% | 总资产(元)(TotalAssets)：优先取财报披露值，如财报未披露，则总资产=存款证(元)+定期存款(元)+法定存款... |
| 58 | `DepositOfInsured` | 保户储金(元) | number(19,4) | ✓ | 22.42% |  |
| 59 | `InsContract` | 保险合同负债(元) | number(19,4) | ✓ | 58.24% |  |
| 60 | `InvestContract` | 投资合同(元) | number(19,4) | ✓ | 39.16% |  |
| 61 | `ReinPremPayable` | 再保险合同负债(元) | number(19,4) | ✓ | 32.25% |  |
| 62 | `InsurAccPayable` | 保险应付账款(元) | number(19,4) | ✓ | 49.26% |  |
| 63 | `SubordDebtIL` | 应付次级债(元) | number(19,4) | ✓ | 8.08% |  |
| 64 | `DiviForInsured` | 应付保户红利(元) | number(19,4) | ✓ | 32.47% |  |
| 65 | `BFinInstAmsPayable` | 应付银行及其他金融机构款项(元) | number(19,4) | ✓ | 9.67% |  |
| 66 | `CurIncTaxLiab` | 当期所得税负债(元) | number(19,4) | ✓ | 80.98% |  |
| 67 | `TaxesPayable` | 应付税项(元) | number(19,4) | ✓ | 0.0% | 应付税项(元)(TaxesPayable)：与当期所得税负债(元)（CurIncTaxLiab）含义相同，不单独展示数值... |
| 68 | `AccountsPayable` | 应付帐款(元) | number(19,4) | ✓ | 5.84% |  |
| 69 | `AdvanceInsurance` | 预收保费(元) | number(19,4) | ✓ | 37.09% |  |
| 70 | `NotDecidedReserves` | 未决赔款准备(元) | number(19,4) | ✓ | 29.12% |  |
| 71 | `SoldRepoSecuProceeds` | 卖出回购证券(元) | number(19,4) | ✓ | 62.17% |  |
| 72 | `FinliabAtFV` | 以公平值计入损益金融负债(元) | number(19,4) | ✓ | 17.32% |  |
| 73 | `DerivativeLiability` | 衍生金融负债(元) | number(19,4) | ✓ | 27.58% |  |
| 74 | `DeferredTaxLiability` | 递延税项负债(元) | number(19,4) | ✓ | 67.43% |  |
| 75 | `OtherFinLiability` | 其他金融负债(元) | number(19,4) | ✓ | 0.0% |  |
| 76 | `LeaseLiabilities` | 租赁负债(元) | number(19,4) | ✓ | 12.17% |  |
| 77 | `LExcepItems` | 负债特殊项目(元) | number(19,4) | ✓ | 99.57% |  |
| 78 | `LAdjuItems` | 负债调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 79 | `TotalLiability` | 总负债(元) | number(19,4) | ✓ | 99.63% | 总负债(元)(TotalLiability)：优先取财报披露值，如财报未披露，则总负债=+保户储金(元)+保险合同负债(... |
| 80 | `AssetLessTLiability` | 总资产减总负债(元) | number(19,4) | ✓ | 99.63% | 总资产减总负债(元)(AssetLessTLiability)：优先取财报披露值，如财报未披露，则总资产减总负债=总资产... |
| 81 | `ShareCapital` | 股本(元) | number(19,4) | ✓ | 95.06% |  |
| 82 | `OtherEquityinstruments` | 其他权益工具(元) | number(19,4) | ✓ | 5.26% |  |
| 83 | `EPreferStock` | 其中:优先股(其他权益工具)(元) | number(19,4) | ✓ | 0.0% |  |
| 84 | `EPerpetualDebt` | 其中:永续债(其他权益工具)(元) | number(19,4) | ✓ | 2.07% |  |
| 85 | `CapitalReserveFund` | 资本公积(元) | number(19,4) | ✓ | 26.09% |  |
| 86 | `StockPremium` | 股本溢价(元) | number(19,4) | ✓ | 2.18% |  |
| 87 | `SurplusReserveFund` | 盈余公积(元) | number(19,4) | ✓ | 26.09% |  |
| 88 | `Reserve` | 储备(元) | number(19,4) | ✓ | 54.41% |  |
| 89 | `ReserveFund` | 法定储备(元) | number(19,4) | ✓ | 0.0% |  |
| 90 | `RevaluationReserve` | 重估储备(元) | number(19,4) | ✓ | 0.0% |  |
| 91 | `ExchangeReserve` | 汇兑储备(元) | number(19,4) | ✓ | 3.08% |  |
| 92 | `OtherReserve` | 其他储备(元) | number(19,4) | ✓ | 2.5% |  |
| 93 | `RetainedProfit` | 未分配利润(元) | number(19,4) | ✓ | 43.46% |  |
| 94 | `HoldProfit` | 保留溢利(元) | number(19,4) | ✓ | 26.62% |  |
| 95 | `TreasuryStock` | 减:库存股(元) | number(19,4) | ✓ | 2.55% |  |
| 96 | `OtherCompositeIncome` | 其他综合收益(元) | number(19,4) | ✓ | 22.37% |  |
| 97 | `SimulantAllotDividend` | 拟派股息(元) | number(19,4) | ✓ | 6.75% |  |
| 98 | `SEExcepItems` | 股东权益特殊项目(元) | number(19,4) | ✓ | 37.78% |  |
| 99 | `SEAdjItems` | 股东权益调整项目(元) | number(19,4) | ✓ | 0.05% |  |
| 100 | `ShareholderEquity` | 股东权益(元) | number(19,4) | ✓ | 99.63% | 股东权益(元)(ShareholderEquity)：优先取财报披露值，如财报未披露，则股东权益=股本(元)+其他权益工... |
| 101 | `SECParentCompanyOwners` | 其中:归属于母公司普通股股东权益(元) | number(19,4) | ✓ | 0.53% |  |
| 102 | `MinorityInterests` | 非控股权益(元) | number(19,4) | ✓ | 66.31% |  |
| 103 | `AddEquityInstruments` | 额外股本工具(元) | number(19,4) | ✓ | 7.86% |  |
| 104 | `TSEExceptionalItems` | 所有者权益(或股东权益)特殊项目(元) | number(19,4) | ✓ | 0.0% |  |
| 105 | `OtherItemsEffectingSE` | 所有者权益(或股东权益)调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 106 | `TotalInterests` | 总权益(元) | number(19,4) | ✓ | 99.63% | 总权益(元)(TotalInterests)：优先取财报披露值，如财报未披露，则总权益=股东权益(元)(Sharehol... |
| 107 | `LEExceptionalItems` | 负债和权益特殊项目(元) | number(19,4) | ✓ | 0.0% |  |
| 108 | `LEAdjustmentItems` | 负债和权益调整项目(元) | number(19,4) | ✓ | 0.0% |  |
| 109 | `TotalIntATotalLiab` | 总权益及总负债(元) | number(19,4) | ✓ | 100.0% | 总权益及总负债(元)(TotalIntATotalLiab)：优先取财报披露值，如财报未披露，则总权益及总负债=总负债(... |
| 110 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 111 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 112 | `JSID` | JSID | number(19) | ✗ |  |  |
| 113 | `BeginDate` | 开始日期 | date | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### InfoSourceCode (信息来源代码)

信息来源代码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND IVALUE IN (1,3)，得到信息来源代码的具体描述：2-第一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，9-定期报告，10-申请版本，11-聆讯后资料集，12-招股章程，13-临时公告，27-配发结果，28-修改已刊发的财务报表及报告，29-修正重大错误而做出的前期调整，30-修订已刊发初步业绩的资料，32-内幕消息-年度报告，33-内幕消息-第一季报，34-内幕消息-第二季报，35-内幕消息-第三季报，36-内幕消息-第四季报，37-内幕消息-中期报告，38-内幕消息-申请版本，39-内幕消息-招股章程，40-内幕消息-聆讯后资料集，41-内幕消息-其他，99-其他。

### ReportType (报表类型)

报表类型（ReportType）: 展示截止日期对应具体报告期，如：第一季报、中期报告、第三季报、第四季报(企业发生财年变更，如年度报告累计报告期是18或15个月，对应披露的12个月中期数据)、第五季报(企业发生财年变更，如年度报告累计报告期是18个月，对应披露的15个月中期数据)、年度报告、其他（企业披露的非标准报告期数据，如1、2、4、5等月，或者非完整累计月度报告数据）等。

### FiscalYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”。

### PeriodMark (日期标志)

日期标志(PeriodMark)与系统常量表中的DM字段关联，令LB = 1314 and DM not in (90)，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，99-其他。
注：1、资产表期末对应报告期的会计期间长度；2、资产表披露的可比时点都是期初（上年年末），也通过日期标志区分是第几季报对应期初；如第一季报对应期初（上年年末）的日期标志是3-3个月；第二季报对应期初（上年年末）的日期标志是6-半年度，依次类推。

### Mark (合并调整标志)

合并调整标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN (1,2,3,4)，得到合并调整标志的具体描述：1-合并调整，2-合并未调整，3-母公司调整，4-母公司未调整。

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
-- 查询 港股资产负债表_保险(香港会计准则) 数据
SELECT *
FROM hk_balancesheetichk
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
