# LC_STIBDerivedData

**中文名**: 科创板衍生报表数据

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBDerivedData` |
| MySQL表名 | `lc_stibderiveddata` |
| 中文名 | 科创板衍生报表数据 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 财务衍生 |
| 更新频率 | 季更新 |
| 字段数量 | 52 |
| 版本 | 1 |

## 表描述

1.内容说明：由上市公司的主要会计科目（合并报表）衍生出来的数据，若三大财务报表中任意报表在某报告期的数据经历调整/修订，则该表相关字段展示每个历史调整数据；未经历调整/修订的报表相关字段则沿用未调整数据。
2.TTM指标为滚动计算的指标，即最近四个季度的单季数据之和。
(1)最新报告期（EndDate）是年报，则TTM=年报数据；
(2)最新报告期（EndDate）非年报，则TTM=本期数据+(上年年报数据-上年同期合并数据)；如果本期、上年年报、上年同期(合并数)存在空值，则返回上年期末;
3.数据范围：科创板上市至今
4.信息来源：招股说明书、定报、审计报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 ... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `IfMerged` | 是否合并 | number(10) | ✗ | 100.0% | 是否合并（IfMerged）固定常量：1-合并 |
| 7 | `IfAdjusted` | 是否调整 | number(10) | ✗ | 100.0% | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM... |
| 8 | `InterestFreeCLiability` | 无息流动负债 | number(19,4) | ✓ | 96.74% | 无息流动负债(InterestFreeCLiability)=应付帐款及应付票据+预收款项+合同负债+应付职工薪酬+应交... |
| 9 | `InterestFreeNonCL` | 无息非流动负债 | number(19,4) | ✓ | 96.74% | 无息非流动负债(InterestFreeNonCL)=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。 |
| 10 | `InterestBearDebt` | 带息债务 | number(19,4) | ✓ | 96.74% | 带息债务(InterestBearDebt)=负债合计－无息流动负债－无息非流动负债；“无息流动负债”计算方法见Inte... |
| 11 | `NetDebt` | 净债务 | number(19,4) | ✓ | 96.74% | 净债务(NetDebt)=带息债务－货币资金；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类... |
| 12 | `TotalPaidinCapital` | 全部投入资本 | number(19,4) | ✓ | 96.74% | 全部投入资本(TotalPaidinCapital)=股东权益合计+带息债务；“带息债务”计算方法见InterestBe... |
| 13 | `WorkingCaital` | 营运资本 | number(19,4) | ✓ | 96.74% | 营运资本(WorkingCaital)=流动资产合计-流动负债合计；金融类企业不计算。 |
| 14 | `NetWorkingCaital` | 净营运资本 | number(19,4) | ✓ | 94.24% | 净营运资本(NetWorkingCaital)=流动资产－货币资金－无息流动负债；“无息流动负债”计算方法见Intere... |
| 15 | `NetTangibleAssets` | 有形资产净值 | number(19,4) | ✓ | 100.0% | 有形资产净值(NetTangibleAssets)=归属于母公司的股东权益-(无形资产+开发支出+商誉+长期待摊费用+递... |
| 16 | `RetainedEarnings` | 留存收益 | number(19,4) | ✓ | 93.95% | 留存收益(RetainedEarnings)=盈余公积+未分配利润 |
| 17 | `NonRecurringProfitLoss` | 非经常性损益 | number(19,4) | ✓ | 95.78% | 非经常性损益（NonRecurringProfitLoss）：取定期报告公布值。 |
| 18 | `NPDeductNonRecurringPL` | 扣除非经常性损益后的归母净利润 | number(19,4) | ✓ | 95.79% | 扣除非经常性损益后的净利润（NPDeductNonRecurringPL）：若披露，则取公布值；若不披露，则由“归属于母... |
| 19 | `GrossProfit` | 毛利 | number(19,4) | ✓ | 99.8% | 毛利(GrossProfit)＝营业收入－营业成本，金融类企业不计算。 |
| 20 | `NetIncomeFromOperating` | 经营活动净收益 | number(19,4) | ✓ | 96.44% | 经营活动净收益（NetIncomeFromOperating）：对于非金融类企业，经营活动净收益＝营业总收入－营业总成本... |
| 21 | `NetIncFromValueChange` | 价值变动净收益 | number(19,4) | ✓ | 100.0% | 价值变动净收益（NetIncFromValueChange）＝投资净收益＋公允价值变动净收益＋汇兑收益 |
| 22 | `EBIT` | 息税前利润 | number(19,4) | ✓ | 99.98% | 息税前利润（EBIT）＝利润总额＋利息费用  其中，利息费用优先取利润表财务费用科目其中项明细计算，利息费用=其中:利息... |
| 23 | `EBITDA` | 息税折旧摊销前利润 | number(19,4) | ✓ | 99.98% | 息税折旧摊销前利润（EBITDA）＝息税前利润EBIT＋固定资产折旧＋投资性房地产折旧摊销+无形资产摊销＋长期待摊费用摊... |
| 24 | `TotalOperateRevenueTTM` | 营业总收入(TTM) | number(19,4) | ✓ | 99.96% | 营业总收入(TTM)(TotalOperateRevenueTTM)：根据报表科目“营业总收入”计算： (1)当报告期是... |
| 25 | `TotalOperatingCostTTM` | 营业总成本(TTM) | number(19,4) | ✓ | 99.64% | 营业总成本(TTM)(TotalOperatingCostTTM)：根据报告期“营业总成本(含减值损失)”计算，： (1... |
| 26 | `OperatingRevenueTTM` | 营业收入(TTM) | number(19,4) | ✓ | 99.95% | 营业收入(TTM)(OperatingRevenueTTM)：根据报表科目“营业收入”计算： (1)当报告期是年报，则T... |
| 27 | `OperatingCostTTM` | 营业成本/支出(TTM) | number(19,4) | ✓ | 99.01% | 直接注释：营业成本/支出(TTM)(OperatingCostTTM)：根据报表科目“营业成本”计算： (1)当报告期是... |
| 28 | `GrossProfitTTM` | 毛利(TTM) | number(19,4) | ✓ | 99.61% | 毛利(TTM)(GrossProfitTTM):根据报告期“毛利”计算： (1)当报告期是年报，则TTM=年报； (2)... |
| 29 | `OperatingExpenseTTM` | 销售费用(TTM) | number(19,4) | ✓ | 98.42% | 销售费用(TTM)(OperatingExpenseTTM)：根据报表科目“销售费用”计算： (1)当报告期是年报，则T... |
| 30 | `AdministExpenseTTM` | 管理费用(TTM) | number(19,4) | ✓ | 99.66% | 管理费用(TTM)(AdministExpenseTTM)：根据报表科目“管理费用合计”计算： (1)当报告期是年报，则... |
| 31 | `RAndDTTM` | 研发费用(TTM) | number(19,4) | ✓ | 98.86% | 研发费用(TTM)(RAndDTTM)：根据报表科目“研发费用”计算： (1)当报告期是年报，则TTM=年报； (2)当... |
| 32 | `FinancialExpenseTTM` | 财务费用(TTM) | number(19,4) | ✓ | 99.65% | 财务费用(TTM)(FinancialExpenseTTM)：根据报表科目“财务费用”计算： (1)当报告期是年报，则T... |
| 33 | `AssetImpairmentLossTTM` | 资产减值损失(TTM) | number(19,4) | ✓ | 91.75% | 资产减值损失(TTM)(AssetImpairmentLossTTM)：根据报告期“资产减值损失净额”计算： (1)当报... |
| 34 | `NIFromOperatingTTM` | 经营活动净收益(TTM) | number(19,4) | ✓ | 99.65% | 经营活动净收益(TTM)(NIFromOperatingTTM)：根据报告期“经营活动净收益”计算： (1)当报告期是年... |
| 35 | `NIFromValueChangeTTM` | 价值变动净收益(TTM) | number(19,4) | ✓ | 96.11% | 价值变动净收益(TTM)(NIFromValueChangeTTM)：根据报告期“价值变动净收益”计算： (1)当报告期... |
| 36 | `OperatingProfitTTM` | 营业利润(TTM) | number(19,4) | ✓ | 99.95% | 营业利润(TTM)(OperatingProfitTTM)：根据报表科目“营业利润”计算： (1)当报告期是年报，则TT... |
| 37 | `NonOperateNetIncomeTTM` | 营业外收支净额(TTM) | number(19,4) | ✓ | 99.74% | 营业外收支净额(TTM)(NonOperateNetIncomeTTM)：根据报告期“营业收入收支净额”计算，： (1)... |
| 38 | `EBITTTM` | 息税前利润(TTM) | number(19,4) | ✓ | 99.98% | 息税前利润(TTM)(EBITTTM)：根据报告期“息税前利润”计算： (1)当报告期是年报，则TTM=年报； (2)当... |
| 39 | `TotalProfitTTM` | 利润总额(TTM) | number(19,4) | ✓ | 99.95% | 利润总额(TTM)(TotalProfitTTM)：根据报表科目“利润总额”计算： (1)当报告期是年报，则TTM=年报... |
| 40 | `NetProfitTTM` | 净利润(TTM) | number(19,4) | ✓ | 99.95% | 净利润(TTM)(NetProfitTTM)：根据报表科目“净利润”计算： (1)当报告期是年报，则TTM=年报； (2... |
| 41 | `NPParentCompanyOwnTTM` | 归属母公司股东的净利润(TTM) | number(19,4) | ✓ | 99.96% | 归属母公司股东的净利润(TTM)(NPParentCompanyOwnTTM)：根据报表科目“归属母公司股东的净利润”计... |
| 42 | `FCFF` | 企业自由现金流量FCFF | number(19,4) | ✓ | 100.0% | 企业自由现金流量（FCFF）＝息前税后利润+折旧与摊销-营运资本增加-资本支出 =息税前利润*(1-有效税率)+当体计提... |
| 43 | `FCFE` | 股权自由现金流量FCFE | number(19,4) | ✓ | 100.0% | 股权自由现金流量（FCFE）=企业自由现金流量FCFF-偿还债务所支付的现金+取得借款收到的现金+发行债券所收到的现金 ... |
| 44 | `CurrentAccruedDA` | 当期计提折旧与摊销 | number(19,4) | ✓ | 100.0% | 当期计提折旧与摊销（CurrentAccruedDA）=固定资产折旧＋投资性房地产折旧摊销+无形资产摊销＋长期待摊费用摊... |
| 45 | `SaleServiceRendCashTTM` | 销售商品提供劳务收到的现金(TTM) | number(19,4) | ✓ | 98.97% | 销售商品提供劳务收到的现金(TTM)(SaleServiceRendCashTTM)：根据报表科目“销售商品提供劳务收到... |
| 46 | `NetOperateCashFlowTTM` | 经营活动现金净流量(TTM) | number(19,4) | ✓ | 99.96% | 经营活动现金净流量(TTM)(NetOperateCashFlowTTM)：根据报表科目“经营活动产生的现金净流量”计算... |
| 47 | `NetInvestCashFlowTTM` | 投资活动现金净流量(TTM) | number(19,4) | ✓ | 99.87% | 投资活动现金净流量(TTM)(NetInvestCashFlowTTM)：根据报表科目“投资活动现金净流量”计算： (1... |
| 48 | `NetFinanceCashFlowTTM` | 筹资活动现金净流量(TTM) | number(19,4) | ✓ | 98.49% | 筹资活动现金净流量(TTM)(NetFinanceCashFlowTTM)：根据报表科目“筹资活动现金净流量”计算： (... |
| 49 | `NetCashFlowTTM` | 现金净流量(TTM) | number(19,4) | ✓ | 99.83% | 现金净流量(TTM)(NetCashFlowTTM)：根据报表科目“现金及现金等价物净增加额”计算： (1)当报告期是年... |
| 50 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 51 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 52 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到公司的交易代码、简称等。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND IVALUE<>2 AND CVALUE NOT IN ('关联方','比较式财务报表')，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，120101-临时公告:审计报告(更正后)，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)，120106-临时公告:公开转让说明书(更正后)，120107-临时公告:业绩快报，120108-临时公告:业绩快报(更正后)，120201-临时公告:跟踪评级报告，120202-临时公告:同业存单发行计划，120205-临时公告:其他，120206-临时公告:前期差错更正，120207-临时公告:第一季度报告，120208-临时公告:第二季度报告，120209-临时公告:第三季度报告，120210-临时公告:第四季度报告，120211-临时公告：年度报告，120212-临时公告：半年度报告，120213-临时公告:受托管理人事务报告，120214-临时公告:资产评估报告，120215-临时公告:资产管理报告，120216-临时公告：经营数据公告，120217-临时公告：经营数据公告(更正后），120218-临时公告：主要经营业绩，130101-发行上市书:募集说明书，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130105-发行上市书:审阅报告，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130108-发行上市书:发行公告，130109-发行上市书:审计报告，130111-发行上市书:其他，130112-发行上市书:招股说明书(上会稿)，130113-发行上市书:招股说明书(注册稿)，140101-发行披露文件:第一季报，140102-发行披露文件:半年度报告，140103-发行披露文件:第三季报，140104-发行披露文件:审计报告，140105-发行披露文件:募集说明书，140106-发行披露文件:跟踪评级报告，140107-发行披露文件:年度报告，140108-发行披露文件:关联方，140109-发行披露文件:预案公告，140110-发行披露文件:转让服务公告书，140111-发行披露文件:备案登记表，140112-发行披露文件:初始信息披露，150101-发债定期报告:第一季报，150102-发债定期报告:半年度报告，150103-发债定期报告:第三季报，150104-发债定期报告:年度报告，150105-发债:其他报告。

### IfMerged (是否合并)

是否合并（IfMerged）固定常量：1-合并

### IfAdjusted (是否调整)

是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,6,7,8)，得到是否调整的具体描述：1-是，2-否，6-一季末调整，7-二季末调整，8-三季末调整。

### InterestFreeCLiability (无息流动负债)

无息流动负债(InterestFreeCLiability)=应付帐款及应付票据+预收款项+合同负债+应付职工薪酬+应交税费+其他应付款(含利息和股利)+预提费用+递延收益.流动负债+其他流动负债+衍生金融负债。其中：其他应付款(含利息和股利)包括：应付股利、应付利息、其他应付款；金融类企业不计算。

### InterestFreeNonCL (无息非流动负债)

无息非流动负债(InterestFreeNonCL)=非流动负债合计-长期借款-应付债券-租赁负债；金融类企业不计算。

### InterestBearDebt (带息债务)

带息债务(InterestBearDebt)=负债合计－无息流动负债－无息非流动负债；“无息流动负债”计算方法见InterestFreeCLiability[无息流动负债]，“无息非流动负债”见InterestFreeNonCL[无息非流动负债]；金融类企业不计算。

### NetDebt (净债务)

净债务(NetDebt)=带息债务－货币资金；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类企业不计算。

### TotalPaidinCapital (全部投入资本)

全部投入资本(TotalPaidinCapital)=股东权益合计+带息债务；“带息债务”计算方法见InterestBearDebt[带息债务]；金融类企业不计算。

### WorkingCaital (营运资本)

营运资本(WorkingCaital)=流动资产合计-流动负债合计；金融类企业不计算。

## SQL示例

```sql
-- 查询 科创板衍生报表数据 数据
SELECT *
FROM lc_stibderiveddata
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
