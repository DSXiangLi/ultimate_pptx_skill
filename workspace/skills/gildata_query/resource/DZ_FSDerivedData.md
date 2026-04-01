# DZ_FSDerivedData

**中文名**: 公司衍生报表数据_新会计准则(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_FSDerivedData` |
| MySQL表名 | `dz_fsderiveddata` |
| 中文名 | 公司衍生报表数据_新会计准则(新) |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务衍生指标 |
| 更新频率 | 季更新 |
| 字段数量 | 54 |
| 版本 | 1.01 |

## 表描述

1.内容说明：
1.1 由公司披露的主要会计科目（合并报表）衍生出来的数据，单位均为人民币元，起始年度为2008年。
1.2 若三大财务报表中任意报表在某报告期的数据经历调整/修订，则该表相关字段展示每个历史调整数据；未经历调整/修订的报表相关字段则沿用未调整数据。
1.3 TTM指标为滚动计算的指标，即最近四个季度的单季数据之和。
(1)最新报告期（EndDate	）是年报，则TTM=年报数据；
(2)最新报告期（EndDate	）非年报，则TTM=本期数据+(上年年报数据-上年同期合并数据)；如果本期、上年年报、上年同期(合并数)存在空值，则返回上年期末;
2.数据范围：2008-03-31至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 98.7% |  |
| 5 | `BulletinType` | 公告类别 | varchar2(30) | ✗ | 100.0% | 公告类别(BulletinType)：10-发行上市书，20-定期报告，70-临时公告； |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整（IfAdjusted），该字段固定以下常量：1-调整；2-未调整；6-一季末调整（年度资产负债表）；7-半年报... |
| 8 | `AccountingStandards` | 会计准则 | number(10) | ✗ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 9 | `InterestFreeCLiabilities` | 无息流动负债 | number(19,4) | ✓ | 92.98% | 无息流动负债（InterestFreeCLiabilities）=应付帐款及应付票据+预收款项+合同负债+应付职工薪酬+... |
| 10 | `InterestFreeNonCL` | 无息非流动负债 | number(19,4) | ✓ | 92.98% | 无息非流动负债（InterestFreeNonCL）=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。 |
| 11 | `InterestBearDebt` | 带息债务 | number(19,4) | ✓ | 97.93% | 带息债务（InterestBearDebt）:非金融类企业计算公式=负债合计－无息流动负债－无息非流动负债；“无息流动负... |
| 12 | `NetDebt` | 净债务 | number(19,4) | ✓ | 92.98% | 净债务（NetDebt）=带息债务－货币资金；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类... |
| 13 | `TotalPaidinCapital` | 全部投入资本 | number(19,4) | ✓ | 92.98% | 全部投入资本（TotalPaidinCapital）=股东权益合计+带息债务；“带息债务”计算方法见InterestBe... |
| 14 | `WorkingCaital` | 营运资本 | number(19,4) | ✓ | 92.98% | 营运资本（WorkingCaital）=流动资产合计-流动负债合计；金融类企业不计算。 |
| 15 | `NetWorkingCaital` | 净营运资本 | number(19,4) | ✓ | 92.44% | 净营运资本（NetWorkingCaital）=流动资产－货币资金－无息流动负债；“无息流动负债”计算方法见Intere... |
| 16 | `NetTangibleAssets` | 有形资产净值 | number(19,4) | ✓ | 100.0% | 有形资产净值（NetTangibleAssets）=归属于母公司的股东权益-(无形资产+开发支出+商誉+长期待摊费用+递... |
| 17 | `RetainedEarnings` | 留存收益 | number(19,4) | ✓ | 96.66% | 留存收益（RetainedEarnings）＝盈余公积＋未分配利润 |
| 18 | `NonRecurringProfitLoss` | 非经常性损益 | number(19,4) | ✓ | 54.88% | 非经常性损益（NonRecurringProfitLoss）：取定期报告公布值 |
| 19 | `NPDeductNonRecurringPL` | 扣除非经常性损益后的归母净利润 | number(19,4) | ✓ | 54.89% | 扣除非经常性损益后的净利润（NPDeductNonRecurringPL）：若披露，则取公布值；若不披露，则由“归属于母... |
| 20 | `GrossProfit` | 毛利 | number(19,4) | ✓ | 94.25% | 毛利（GrossProfit）＝营业收入－营业成本，金融类公司不计算。 |
| 21 | `NetIncomeFromOperating` | 经营活动净收益 | number(19,4) | ✓ | 98.19% | 经营活动净收益（NetIncomeFromOperating）：对于非金融类企业，经营活动净收益＝营业总收入－营业总成本... |
| 22 | `NetIncomeFromValueChange` | 价值变动净收益 | number(19,4) | ✓ | 100.0% | 价值变动净收益（NetIncomeFromValueChange）＝投资净收益＋公允价值变动净收益＋汇兑收益 |
| 23 | `EBIT` | 息税前利润 | number(19,4) | ✓ | 94.48% | 息税前利润（EBIT）＝利润总额＋利息费用  其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用=其中:利息... |
| 24 | `EBITDA` | 息税折旧摊销前利润 | number(19,4) | ✓ | 94.48% | 息税折旧摊销前利润（EBITDA）＝息税前利润EBIT＋固定资产折旧＋投资性房地产折旧摊销+无形资产摊销＋长期待摊费用摊... |
| 25 | `TotalOperatingRevenueTTM` | 营业总收入(TTM) | number(19,4) | ✓ | 94.11% | 营业总收入(TTM)(TotalOperatingRevenueTTM)：根据报表科目“营业总收入”计算： (1)当报告... |
| 26 | `TotalOperatingCostTTM` | 营业总成本(TTM) | number(19,4) | ✓ | 93.89% | 营业总成本(TTM)(TotalOperatingCostTTM)：根据报告期“营业总成本(含减值损失)”计算，： (1... |
| 27 | `OperatingRevenueTTM` | 营业收入(TTM) | number(19,4) | ✓ | 99.57% | 营业收入(TTM)(OperatingRevenueTTM)：根据报表科目“营业收入”计算： (1)当报告期是年报，则T... |
| 28 | `OperatingCostTTM` | 营业成本-非金融类(TTM) | number(19,4) | ✓ | 93.35% | 营业成本-非金融类(TTM)(OperatingCostTTM)：根据报表科目“营业成本”计算： (1)当报告期是年报，... |
| 29 | `OperatingPayoutTTM` | 营业支出-金融类(TTM) | number(19,4) | ✓ | 4.79% | 营业支出-金融类(TTM)(OperatingPayoutTTM)：根据报表科目“营业支出”计算： (1)当报告期是年报... |
| 30 | `GrossProfitTTM` | 毛利(TTM) | number(19,4) | ✓ | 93.89% | 毛利(TTM)(GrossProfitTTM):根据报告期“毛利”计算： (1)当报告期是年报，则TTM=年报； (2)... |
| 31 | `OperatingExpenseTTM` | 销售费用(TTM) | number(19,4) | ✓ | 86.95% | 销售费用(TTM)(OperatingExpenseTTM)：根据报表科目“销售费用”计算： (1)当报告期是年报，则T... |
| 32 | `AdministrationExpenseTTM` | 管理费用(TTM) | number(19,4) | ✓ | 98.5% | 管理费用(TTM)(AdministrationExpenseTTM)：根据报表科目“管理费用合计”计算： (1)当报告... |
| 33 | `RAndDTTM` | 研发费用(TTM) | number(19,4) | ✓ | 33.62% | 研发费用(TTM)(RAndDTTM)：根据报表科目“研发费用”计算： (1)当报告期是年报，则TTM=年报； (2)当... |
| 34 | `FinancialExpenseTTM` | 财务费用(TTM) | number(19,4) | ✓ | 93.93% | 财务费用(TTM)(FinancialExpenseTTM)：根据报表科目“财务费用”计算： (1)当报告期是年报，则T... |
| 35 | `AssetImpairmentLossTTM` | 资产减值损失(TTM) | number(19,4) | ✓ | 79.73% | 资产减值损失(TTM)(AssetImpairmentLossTTM)：根据报告期“资产减值损失净额”计算： (1)当报... |
| 36 | `NIFromOperatingTTM` | 经营活动净收益(TTM) | number(19,4) | ✓ | 98.76% | 经营活动净收益(TTM)(NIFromOperatingTTM)：根据报告期“经营活动净收益”计算： (1)当报告期是年... |
| 37 | `NIFromValueChangeTTM` | 价值变动净收益(TTM) | number(19,4) | ✓ | 94.53% | 价值变动净收益(TTM)(NIFromValueChangeTTM)：根据报告期“价值变动净收益”计算： (1)当报告期... |
| 38 | `OperatingProfitTTM` | 营业利润(TTM) | number(19,4) | ✓ | 98.86% | 营业利润(TTM)(OperatingProfitTTM)：根据报表科目“营业利润”计算： (1)当报告期是年报，则TT... |
| 39 | `NonoperatingNetIncomeTTM` | 营业外收支净额(TTM) | number(19,4) | ✓ | 99.18% | 营业外收支净额(TTM)(NonoperatingNetIncomeTTM)：根据报告期“营业收入收支净额”计算，： (... |
| 40 | `EBITTTM` | 息税前利润(TTM) | number(19,4) | ✓ | 94.29% | 息税前利润(TTM)(EBITTTM)：根据报告期“息税前利润”计算： (1)当报告期是年报，则TTM=年报； (2)当... |
| 41 | `TotalProfitTTM` | 利润总额(TTM) | number(19,4) | ✓ | 99.12% | 利润总额(TTM)(TotalProfitTTM)：根据报表科目“利润总额”计算： (1)当报告期是年报，则TTM=年报... |
| 42 | `NetProfitTTM` | 净利润(TTM) | number(19,4) | ✓ | 99.26% | 净利润(TTM)(NetProfitTTM)：根据报表科目“净利润”计算： (1)当报告期是年报，则TTM=年报； (2... |
| 43 | `NPParentCompanyOwnersTTM` | 归属母公司股东的净利润(TTM) | number(19,4) | ✓ | 98.81% | 归属母公司股东的净利润(TTM)(NPParentCompanyOwnersTTM)：根据报表科目“归属母公司股东的净利... |
| 44 | `FCFF` | 企业自由现金流量FCFF | number(19,4) | ✓ | 100.0% | 企业自由现金流量（FCFF）＝息前税后利润+折旧与摊销-营运资本增加-资本支出 =息税前利润*(1-有效税率)+当体计提... |
| 45 | `FCFE` | 股权自由现金流量FCFE | number(19,4) | ✓ | 100.0% | 股权自由现金流量（FCFE）=企业自由现金流量FCFF-偿还债务所支付的现金+取得借款收到的现金+发行债券所收到的现金 ... |
| 46 | `CurrentAccruedDA` | 当期计提折旧与摊销 | number(19,4) | ✓ | 100.0% | 当期计提折旧与摊销（CurrentAccruedDA）=固定资产折旧＋投资性房地产折旧摊销+无形资产摊销＋长期待摊费用摊... |
| 47 | `SaleServiceRenderCashTTM` | 销售商品提供劳务收到的现金(TTM) | number(19,4) | ✓ | 92.99% | 销售商品提供劳务收到的现金(TTM)(SaleServiceRenderCashTTM)：根据报表科目“销售商品提供劳务... |
| 48 | `NetOperateCashFlowTTM` | 经营活动现金净流量(TTM) | number(19,4) | ✓ | 97.69% | 经营活动现金净流量(TTM)(NetOperateCashFlowTTM)：根据报表科目“经营活动产生的现金净流量”计算... |
| 49 | `NetInvestCashFlowTTM` | 投资活动现金净流量(TTM) | number(19,4) | ✓ | 97.28% | 投资活动现金净流量(TTM)(NetInvestCashFlowTTM)：根据报表科目“投资活动现金净流量”计算： (1... |
| 50 | `NetFinanceCashFlowTTM` | 筹资活动现金净流量(TTM) | number(19,4) | ✓ | 96.44% | 筹资活动现金净流量(TTM)(NetFinanceCashFlowTTM)：根据报表科目“筹资活动现金净流量”计算： (... |
| 51 | `NetCashFlowTTM` | 现金净流量(TTM) | number(19,4) | ✓ | 97.57% | 现金净流量(TTM)(NetCashFlowTTM)：根据报表科目“现金及现金等价物净增加额”计算： (1)当报告期是年... |
| 52 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 53 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 54 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### BulletinType (公告类别)

公告类别(BulletinType)：10-发行上市书，20-定期报告，70-临时公告；

### IfAdjusted (是否调整)

是否调整（IfAdjusted），该字段固定以下常量：1-调整；2-未调整；6-一季末调整（年度资产负债表）；7-半年报调整（年度资产负债表）；8-三季末调整（年度资产负债表）

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455 and DM<>9，得到会计准则的具体描述：1-新会计准则(2007)。

### InterestFreeCLiabilities (无息流动负债)

无息流动负债（InterestFreeCLiabilities）=应付帐款及应付票据+预收款项+合同负债+应付职工薪酬+应交税费+其他应付款(含利息和股利)+预提费用+递延收益.流动负债+其他流动负债+衍生金融负债。其中：其他应付款(含利息和股利)包括：应付股利、应付利息、其他应付款；金融类企业不计算。

### InterestFreeNonCL (无息非流动负债)

无息非流动负债（InterestFreeNonCL）=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。

### InterestBearDebt (带息债务)

带息债务（InterestBearDebt）:非金融类企业计算公式=负债合计－无息流动负债－无息非流动负债；“无息流动负债”计算方法见InterestFreeCLiability[无息流动负债]，“无息非流动负债”见InterestFreeNonCL[无息非流动负债]；
金融类企业计算公式=负债合计-卖出回购金融资产款-代理买卖证券款-代理承销证券款-应付职工薪酬-长期应付职工薪酬-应付款项-应交税费-应付利息-合同负债-划分为持有待售的负债-代理业务负债递延所得税负债-其他负债-衍生金融负债。

### NetDebt (净债务)

净债务（NetDebt）=带息债务－货币资金；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类企业不计算。

### TotalPaidinCapital (全部投入资本)

全部投入资本（TotalPaidinCapital）=股东权益合计+带息债务；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类企业不计算。

### WorkingCaital (营运资本)

营运资本（WorkingCaital）=流动资产合计-流动负债合计；金融类企业不计算。

## SQL示例

```sql
-- 查询 公司衍生报表数据_新会计准则(新) 数据
SELECT *
FROM dz_fsderiveddata
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
