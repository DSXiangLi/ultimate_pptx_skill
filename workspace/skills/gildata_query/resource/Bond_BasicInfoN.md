# Bond_BasicInfoN

**中文名**: 债券要素新表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BasicInfoN` |
| MySQL表名 | `bond_basicinfon` |
| 中文名 | 债券要素新表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 95 |
| 版本 | 1.22 |

## 表描述

1.本表展现所有债券（除可转债）的基本要素信息；
2.涵盖在交易所、银行间、柜台等所有市场上交易的国债、金融债、企业债、短期融资券、资产支持证券、信用风险缓释工具等各类品种；
3.包括记帐式、凭证式等各种形态的债券，不管其是否上市交易；
4.该表中的资产支持证券包含人民银行监管的债券：包括ABS和MBS两种；交易所的企业资产支持证券；
5.该表记录债券在不同市场的基本信息。
6.数据范围：1981-1-1 至今
7.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `MainCode` | 债券统一代码 | number(10) | ✓ | 100.0% | 债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 4 | `BondFullName` | 债券全称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `IfListedIssuer` | 发行人是否上市公司 | number(10) | ✓ | 100.0% | 发行人是否上市公司(IfListedIssuer)与(CT_SystemConst)表中的DM字段关联，令LB = 99... |
| 6 | `IFMultiIssuer` | 是否多个发行人 | number(10) | ✓ | 100.0% | 是否多个发行人(IFMultiIssuer)与(CT_SystemConst)表中的DM字段关联，令LB = 999 a... |
| 7 | `BondForm` | 债券形态 | number(10) | ✓ | 99.99% | 债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具... |
| 8 | `OptionType` | 选择权类型 | varchar2(200) | ✓ | 13.05% |  |
| 9 | `BondNature` | 债券性质 | number(10) | ✓ | 100.0% | 债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券性质... |
| 10 | `CrossExchange` | 是否跨市场 | number(10) | ✓ | 100.0% | 是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and... |
| 11 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✓ | 100.0% |  |
| 12 | `CreditRating` | 债项信用级别 | varchar2(50) | ✓ | 29.14% | 债项信用级别：具体含义为该债券对应的首次评级 取数规则：取该债券所有的评级（包含长期和短期）中的首次评级，若存在有多条，... |
| 13 | `InitialIssueSize` | 计划发行总额(元) | number(19,4) | ✓ | 99.99% |  |
| 14 | `LatestIssueSize` | 实际发行总额(元) | number(19,4) | ✓ | 99.95% |  |
| 15 | `Maturity` | 债券期限(年) | number(9,6) | ✓ | 99.95% |  |
| 16 | `MaturityDays` | 债券期限(天) | number(10) | ✓ | 98.49% |  |
| 17 | `OPMaturity` | 含权券特殊期限 | varchar2(100) | ✓ | 7.59% |  |
| 18 | `ParValue` | 初始债券面值(元) | number(19,4) | ✓ | 100.0% |  |
| 19 | `IssuePrice` | 初始发行价格(元) | number(19,4) | ✓ | 99.93% |  |
| 20 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 and ... |
| 21 | `IssueRefYTM` | 发行参考收益率(%) | number(10,6) | ✓ | 50.41% |  |
| 22 | `CompoundMethod` | 计息方式 | number(10) | ✓ | 97.13% | 计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 23 | `IntPaymentMethod` | 付息方式 | number(10) | ✓ | 47.26% | 付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，... |
| 24 | `PayInterestEffency` | 付息频率(次/年) | number(10) | ✓ | 47.26% | 付息频率(次/年)（PayInterestEffency）：到期一次性还本付息的债券，其付息频率为0；每年付息的债券，其... |
| 25 | `APIntPaymentMethod` | 摊还期付息方式 | number(10) | ✓ | 2.97% | 摊还期付息方式(APIntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 26 | `PMRemark` | 支付机制说明 | varchar2(255) | ✓ | 98.21% |  |
| 27 | `InterestItem` | 利息条款描述 | clob | ✓ | 52.99% |  |
| 28 | `InterestFormula` | 利息计算公式 | number(10) | ✓ | 66.57% | 利息计算公式(InterestFormula)与(CT_SystemConst)表中的DM字段关联，令LB = 1470... |
| 29 | `InterestFormulaGen` | 利息计算公式(赋值) | number(10) | ✓ | 99.35% | 利息计算公式(赋值)(InterestFormulaGen)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 30 | `RedemptionMethod` | 兑付方式 | number(10) | ✓ | 97.51% | 兑付方式(RedemptionMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1546，... |
| 31 | `CouponRate` | 初始票面年利率(%) | number(9,6) | ✓ | 95.62% |  |
| 32 | `InterestRatePeriod` | 利率变动区间 | varchar2(2000) | ✓ | 44.58% |  |
| 33 | `IfCRM` | 是否含有信用风险缓释工具 | number(10) | ✓ | 100.0% | 是否含有信用风险缓释工具(IfCRM)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and ... |
| 34 | `IfGuaranteedSettle` | 是否担保交收(交易所) | number(10) | ✓ | 20.19% | 是否担保交收(交易所)(IfGuaranteedSettle)与(CT_SystemConst)表中的DM字段关联，令L... |
| 35 | `RIssueCode` | 被增发代码 | number(10) | ✓ | 0.02% | 被增发代码（RIssueCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 36 | `LatestParValue` | 最新面值 | number(10,6) | ✓ | 100.0% |  |
| 37 | `TaxRate` | 所得税率 | number(10,6) | ✓ | 86.26% |  |
| 38 | `IfTaxFree` | 是否免税 | number(10) | ✓ | 100.0% | 是否免税(IfTaxFree)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM I... |
| 39 | `IfVAT` | 是否征收增值税 | number(10) | ✓ | 99.95% | 是否征收增值税（ IfVAT）：1-是，2-否 |
| 40 | `PricingMethod` | 最新计价方式 | number(10) | ✓ | 100.0% | 最新计价方式(PricingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1517，得... |
| 41 | `LatestCouponRate` | 最新票面利率 | number(10,6) | ✓ | 44.58% |  |
| 42 | `ListedMarket` | 上市交易平台 | varchar2(100) | ✓ | 20.59% |  |
| 43 | `TradeType` | 交易方式 | number(10) | ✓ | 20.19% | 交易方式(TradeType)：1-匹配成交;协商成交;点击成交;询价成交;竞买成交，2-协商成交;点击成交;询价成交;... |
| 44 | `IssueDate` | 发行日 | date | ✓ | 97.9% | 发行日（IssueDate）：该日期取发行相关日期中的最小值：包含招标日(簿记建档日)、分销日、发行日（含网上、网下）。 |
| 45 | `ValueDate` | 起息日(债券期限起始日) | date | ✓ | 98.53% |  |
| 46 | `EndDate` | 到期日(债券期限截止日) | date | ✓ | 98.55% |  |
| 47 | `InitialPaymentDate` | 首次理论付息日 | date | ✓ | 44.58% |  |
| 48 | `RegDate` | 债权债务登记日 | date | ✓ | 69.24% |  |
| 49 | `ListedDate` | 上市日(交易流通起始日) | date | ✓ | 91.31% |  |
| 50 | `DelistDate` | 摘牌日(交易流通终止日) | date | ✓ | 77.99% |  |
| 51 | `EarlyMaturityDate` | 实际到期日 | date | ✓ | 5.4% | 针对提前到期的债券，使用提前到期日，即为债券实际到期日 |
| 52 | `ActualPaymentDate` | 实际兑付日 | date | ✓ | 98.55% |  |
| 53 | `LastTradingDateE` | 最后交易日(预估) | date | ✓ | 98.51% |  |
| 54 | `LastTradingDateA` | 最后交易日(实际) | date | ✓ | 2.58% |  |
| 55 | `DelistDateE` | 摘牌日(预估) | date | ✓ | 98.51% |  |
| 56 | `DelistDateA` | 摘牌日(实际) | date | ✓ | 77.99% |  |
| 57 | `BondOtherState` | 状态 | number(10) | ✓ | 6.22% | 状态(BondOtherState)：10-发行失败，20-初始发行变增发 |
| 58 | `Remark` | 备注 | varchar2(500) | ✓ | 3.88% |  |
| 59 | `FRNRefRateSelecrRemark` | 浮动利率计息基准 | number(10) | ✓ | 1.98% | 浮动利率计息基准(FRNRefRateSelecrRemark)与(CT_SystemConst)表中的DM字段关联，令... |
| 60 | `FRNRefRatePer` | 初始基准利率(%) | number(9,6) | ✓ | 0.44% |  |
| 61 | `FRNMargin` | 初始基准利差(%) | number(9,6) | ✓ | 1.79% |  |
| 62 | `MinAnnualRate` | 债券保底利率(%) | number(9,6) | ✓ | 0.0% |  |
| 63 | `PrimalPricingDate` | 首个定价日 | date | ✓ | 0.36% |  |
| 64 | `RateAdjustMode` | 利率调整模式 | number(10) | ✓ | 0.45% | 利率调整模式(RateAdjustMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1469，... |
| 65 | `LegalEndDate` | 法定到期日 | date | ✓ | 6.14% |  |
| 66 | `CreatOrg` | 发起机构/原始权益人 | varchar2(200) | ✓ | 8.17% |  |
| 67 | `ProjectName` | 项目名称 | varchar2(200) | ✓ | 8.1% |  |
| 68 | `StartDate` | 初始起算日 | date | ✓ | 2.5% |  |
| 69 | `AssetIfTable` | 资产是否出表 | number(10) | ✓ | 0.64% |  |
| 70 | `ProjectAbbr` | 项目简称 | varchar2(200) | ✓ | 8.01% |  |
| 71 | `IfRevolving` | 是否循环购买 | number(10) | ✓ | 6.35% | 是否循环购买(IfRevolving)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and ... |
| 72 | `RevolveEDate` | 循环期届满日 | date | ✓ | 2.03% |  |
| 73 | `ABSLevel` | 分层级别 | number(10) | ✓ | 8.15% | 分层级别(ABSLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1417 and DM i... |
| 74 | `ABSLevely` | 分层级别细分 | number(10) | ✓ | 3.92% | 分层级别细分(ABSLevely)与(CT_SystemConst)表中的DM字段关联，令LB = 1998，得到分层级... |
| 75 | `BasicAssetType` | 基础资产类型 | number(10) | ✓ | 7.99% | 基础资产类型(BasicAssetType)与(CT_SystemConst)表中的DM字段关联，令LB=2003 AN... |
| 76 | `ABSLevelRatio` | 规模分层占比(%) | number(19,8) | ✓ | 8.15% |  |
| 77 | `InterestCap` | 利率上限说明 | varchar2(200) | ✓ | 0.44% |  |
| 78 | `InterestCeiling` | 债券封顶利率(%) | number(10,6) | ✓ | 0.48% |  |
| 79 | `IfMultiL` | 是否多层级 | number(10) | ✓ | 8.17% | 是否多层级(IfMultiL)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM i... |
| 80 | `TranchesSum` | 细分层总数量 | number(10) | ✓ | 8.17% |  |
| 81 | `InitialInvestorNum` | 初始投资人数量 | number(10) | ✓ | 0.28% |  |
| 82 | `PrivateInvestorNum` | 定向投资人数量 | number(10) | ✓ | 0.28% |  |
| 83 | `TargetInnerCode` | 标的债务 | number(10) | ✓ | 0.22% | 标的债务(TargetInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCo... |
| 84 | `TargetTotalSize` | 标的债务流通总量(亿) | number(19,12) | ✓ | 0.14% |  |
| 85 | `PaymentMethod` | 付费方式 | number(10) | ✓ | 0.22% | 付费方式(PaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1678，得到付... |
| 86 | `SettlemtMethod` | 结算方式 | varchar2(100) | ✓ | 0.26% |  |
| 87 | `Creditevent` | 信用事件 | varchar2(200) | ✓ | 0.26% |  |
| 88 | `CalCode` | 计算机构 | number(10) | ✓ | 0.17% | 计算机构(CalCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2200，得到计算机构的具体... |
| 89 | `CreditProRatio` | 信用保护比例(%) | number(10,2) | ✓ | 0.16% |  |
| 90 | `PaymentCycle` | 付费周期长度(月) | varchar2(20) | ✓ | 0.06% |  |
| 91 | `CreditProTrigRange` | 信用保护触发范围 | number(10) | ✓ | 0.26% | 信用保护触发范围(CreditProTrigRange)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 92 | `TaxPayer` | 所得税税款承担方 | number(10) | ✓ | 1.2% | 所得税税款承担方(TaxPayer)与(CT_SystemConst)表中的DM字段关联，令LB = 2524，得到所得... |
| 93 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 94 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 95 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### MainCode (债券统一代码)

债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。 

### IfListedIssuer (发行人是否上市公司)

发行人是否上市公司(IfListedIssuer)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到发行人是否上市公司的具体描述：1-是，2-否。

### IFMultiIssuer (是否多个发行人)

是否多个发行人(IFMultiIssuer)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否多个发行人的具体描述：1-是，2-否。

### BondForm (债券形态)

债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具体描述：1-实名制记帐式，2-无记名实物券，3-凭证式国债，4-其他形式，5-电子式储蓄国债。

### BondNature (债券性质)

债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券性质的具体描述：1-企业债券，2-金融债券，3-金融次级债，4-国债现货，5-央行票据，6-短期融资券，7-MBS(房贷支持)，8-ABS(其他支持)，9-混合资本债券，10-可转换债券，11-国库现金管理，12-资产证券化，13-公司债券，14-中期票据，15-转债分离公司债，16-地方政府债券，17-中小企业集合票据，18-集合债券，19-超短期融资券，20-非公开定向债务融资工具，21-次级定期债务，22-中小企业区域集优票据，23-政府支持债券，24-中小企业私募债券，25-资产支持票据，26-小微企业扶持债券，27-二级资本债券，28-中小企业可交换私募债，29-可交换公司债券，30-同业存单，31-区域集优中期票据，32-项目收益票据，33-项目收益债券，34-证券公司短期公司债券，35-保险公司资本补充债券，36-非公开发行公司债，37-信用风险缓释凭证，38-信用联结票据，39-其他一级资本工具，40-标准化票据，41-自贸区债，42-TLAC非资本债券，99-其他。

### CrossExchange (是否跨市场)

是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否跨市场的具体描述：1-是，2-否。

### CreditRating (债项信用级别)

债项信用级别：具体含义为该债券对应的首次评级
取数规则：取该债券所有的评级（包含长期和短期）中的首次评级，若存在有多条，则使用逗号(,)隔开；
具体债券如有其他使用需求可直接使用Bond_BDCreditGrading进行直接取数

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 and DM in (1000,1420,3000,9990)，得到货币单位的具体描述：1000-美元，1420-人民币元，3000-欧元，9990-特别提款权。

### CompoundMethod (计息方式)

计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AND DM in (1,3,5,6)，得到计息方式的具体描述：1-单利(固定利率)，3-浮动利率，5-贴现，6-无序利率。

## SQL示例

```sql
-- 查询 债券要素新表 数据
SELECT *
FROM bond_basicinfon
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
