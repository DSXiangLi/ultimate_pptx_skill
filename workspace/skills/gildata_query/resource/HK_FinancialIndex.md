# HK_FinancialIndex

**中文名**: 港股财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FinancialIndex` |
| MySQL表名 | `hk_financialindex` |
| 中文名 | 港股财务指标 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 51 |
| 版本 | 1.03 |

## 表描述

1.介绍港股财务指标的基本属性、每股数据、资产负债、损益和现金流量等相关信息。主要包含市场关注度较高的三大报表常用财务指标，是财务数据的简表。                                          2.数据范围：1998年至今。
3.数据来源:港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `InfoPublDate` | 最新信息发布日期 | date | ✓ | 99.96% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.97% |  |
| 5 | `ReportTypeCode` | 报表类型代码 | number(10) | ✓ | 93.55% | 报表类型代码(ReportTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AN... |
| 6 | `AbstrPublDate` | 摘要发布日期 | date | ✓ | 14.69% |  |
| 7 | `PerformancePublDate` | 业绩公告发布日期 | date | ✓ | 82.76% |  |
| 8 | `PeriodicReportPublDate` | 定期报告发布日期 | date | ✓ | 78.77% |  |
| 9 | `ChangePublDate` | 更正日期 | date | ✓ | 0.45% |  |
| 10 | `IfAdjusted` | 调整标志 | number(10) | ✓ | 100.0% | 调整标志（IfAdjusted）：与“系统常量表”中的“代码（DM）”关联，令LB=“1188”和“DM<4”，得到“调... |
| 11 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 12 | `PeriodMark` | 日期标志 | number(10) | ✓ | 100.0% | 日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标志... |
| 13 | `FinancialYear` | 财政年度 | date | ✓ | 99.97% | 财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331... |
| 14 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency):1100-港币 |
| 15 | `OpinionType` | 核数师意见类型 | number(10) | ✓ | 97.88% | 核数师意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB=1051 AND ... |
| 16 | `EPSBasic` | 每股基本盈利(元) | number(18,8) | ✓ | 93.4% | 每股基本盈利（EPSBasic）：取公告值，如果财务报表中未列报该项目，该项目以空值展示 |
| 17 | `EPS` | 每股摊薄盈利(元) | number(18,8) | ✓ | 66.58% | 每股摊薄盈利（EPS）：取公告值，如果财务报表中未列报该项目，该项目以空值展示 |
| 18 | `TotalAssets` | 总资产(元) | number(19,4) | ✓ | 74.07% |  |
| 19 | `NoncurrentAssets` | 非流动资产(元) | number(19,4) | ✓ | 70.97% |  |
| 20 | `CurrentAssets` | 流动资产(元) | number(19,4) | ✓ | 71.18% |  |
| 21 | `CurrentLiability` | 流动负债(元) | number(19,4) | ✓ | 71.18% |  |
| 22 | `NonurrentLiability` | 非流动负债(元) | number(19,4) | ✓ | 64.25% |  |
| 23 | `TotalLiability` | 总负债(元) | number(19,4) | ✓ | 73.98% |  |
| 24 | `MinorityInterests` | 少数股东权益(元) | number(19,4) | ✓ | 47.77% |  |
| 25 | `TotalShareholderEquity` | 股东权益/资产净值(元) | number(19,4) | ✓ | 73.91% |  |
| 26 | `ShareCapital` | 股本(元) | number(19,4) | ✓ | 70.14% |  |
| 27 | `Reserves` | 储备(元) | number(19,4) | ✓ | 56.38% |  |
| 28 | `OperatingIncome` | 营业额/银行经营收入(元) | number(19,4) | ✓ | 98.34% |  |
| 29 | `OperatingProfit` | 经营溢利(元) | number(19,4) | ✓ | 98.14% |  |
| 30 | `FinancialExpense` | 融资成本/财务费用(元) | number(19,4) | ✓ | 78.95% |  |
| 31 | `AffiliatedComapnyprofit` | 应占联营公司溢利(元) | number(19,4) | ✓ | 36.92% |  |
| 32 | `CooperateBusinessProfit` | 应占共同控制实体之溢利(合营公司)(元) | number(19,4) | ✓ | 5.73% |  |
| 33 | `EarningBeforeTax` | 除税前溢利(元) | number(19,4) | ✓ | 92.75% |  |
| 34 | `TaxExpense` | 税项(元) | number(19,4) | ✓ | 81.5% |  |
| 35 | `EarningAfterTax` | 除税后溢利(元) | number(19,4) | ✓ | 92.85% |  |
| 36 | `MinorityProfit` | 少数股东损益(元) | number(19,4) | ✓ | 57.9% |  |
| 37 | `ProfitToShareholders` | 股东应占溢利净额(扣税及少数权益后溢利)(元) | number(19,4) | ✓ | 99.18% |  |
| 38 | `GrowthRate` | 相对上期增减 | number(18,8) | ✓ | 0.12% | 相对上期增减(GrowthRate):本字段自2008年之后不再维护。 |
| 39 | `Dividend` | 股息(元) | number(19,4) | ✓ | 7.91% |  |
| 40 | `SpecialItemProfit` | 非经常性项目收益(元) | number(19,4) | ✓ | 3.74% |  |
| 41 | `ProfitExSpecialItem` | 扣除非经常性项目后溢利(元) | number(19,4) | ✓ | 99.54% |  |
| 42 | `NetOperateCashFlow` | 经营业务现金流量净额(元) | number(19,4) | ✓ | 74.78% |  |
| 43 | `NetInvestCashFlow` | 投资活动现金流量净额(元) | number(19,4) | ✓ | 74.0% |  |
| 44 | `NetFinanceCashFlow` | 融资活动现金流量净额(元) | number(19,4) | ✓ | 72.25% |  |
| 45 | `NetCashFlow` | 现金流量净额(元) | number(19,4) | ✓ | 74.75% |  |
| 46 | `CashEquivalentBeginPer` | 期初现金及现金等价物(元) | number(19,4) | ✓ | 74.5% |  |
| 47 | `EffectOfFERChanges` | 外币汇率转换影响(元) | number(19,4) | ✓ | 52.43% |  |
| 48 | `CashEquivalentEndPer` | 期末现金及现金等价物(元) | number(19,4) | ✓ | 74.74% |  |
| 49 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 50 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 51 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### ReportTypeCode (报表类型代码)

报表类型代码(ReportTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB=1926 AND DM IN (2,4,5,6,7,8,99)，得到报表类型代码的具体描述：2-第一季报，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-第五季报，99-其他。

### IfAdjusted (调整标志)

调整标志（IfAdjusted）：与“系统常量表”中的“代码（DM）”关联，令LB=“1188”和“DM<4”，得到“调整标志”描述。1-是，2-否，3-前。其中：IfAdjusted）=1-是 均为2011年以前历史数据，现已不再维护。其中：IfAdjusted）=3-前 均是更正前数据，现统一展示最新数据，不再展示更正前数据。

### PeriodMark (日期标志)

日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标志的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，90-季度，99-其他。

### FinancialYear (财政年度)

财政年度（FiscalYear）: 展示报告期对应财政年度的年结日，如某企业2023年一季报（截止日期：20230331）对应财政年度为“20231231”；如某企业2022年中期报告（截止日期：20221130）对应财政年度为“20230531”；

### Currency (货币单位)

货币单位(Currency):1100-港币

### OpinionType (核数师意见类型)

核数师意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB=1051 AND DM NOT IN(70)，得到核数师意见类型的具体描述：1-无保留，2-无保留带解释性说明，3-保留意见，4-拒绝/无法表示意见，5-否定意见，6-未经审计，7-保留带解释性说明，9-修改意见，10-经审计（不确定具体意见类型），11-无保留带持续经营重大不确定性。

### EPSBasic (每股基本盈利(元))

每股基本盈利（EPSBasic）：取公告值，如果财务报表中未列报该项目，该项目以空值展示

### EPS (每股摊薄盈利(元))

每股摊薄盈利（EPS）：取公告值，如果财务报表中未列报该项目，该项目以空值展示

### GrowthRate (相对上期增减)

相对上期增减(GrowthRate):本字段自2008年之后不再维护。

## SQL示例

```sql
-- 查询 港股财务指标 数据
SELECT *
FROM hk_financialindex
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
