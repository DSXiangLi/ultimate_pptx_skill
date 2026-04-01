# Bond_ConBDBasicInfo

**中文名**: 可转债基本信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDBasicInfo` |
| MySQL表名 | `bond_conbdbasicinfo` |
| 中文名 | 可转债基本信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 80 |
| 版本 | 1.09 |

## 表描述

1.包含可转换债券的评级人、担保人、主承销商、债券要素、上市情况、以及发行公告中的转股和赎回信息等。
2.数据范围：1991-08-11 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `StockInnerCode` | 对应基础股票内部代码 | number(10) | ✓ | 99.81% | 对应基础股票内部代码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 4 | `SecuCode` | 对应基础股票证券代码 | varchar2(10) | ✓ | 99.81% |  |
| 5 | `SecuAbbr` | 对应基础股票证券简称 | varchar2(100) | ✓ | 99.81% |  |
| 6 | `BondForm` | 债券形式 | number(10) | ✓ | 100.0% | 债券形式(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM I... |
| 7 | `CBEmbeddedOption` | 附属权证 | number(10) | ✓ | 1.32% | 附属权证(CBEmbeddedOption)：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)... |
| 8 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 9 | `LatestStatus` | 最新状态 | number(10) | ✓ | 100.0% | 最新状态（LatestStatus）：1-发行中，2-存续中，3-已到期，4-发行失败 |
| 10 | `CompanyCode` | 发行人公司代码 | number(10) | ✓ | 100.0% | 发行人公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 11 | `Issuer` | 发行人 | varchar2(200) | ✓ | 100.0% |  |
| 12 | `IndustryCode` | 所属行业代码(证监会) | number(10) | ✓ | 100.0% | 所属行业代码(证监会)(IndustryCode)：与“行业类别表（CT_IndustryType）”的“ 行业内部编码... |
| 13 | `IssuerFirstArea` | 所属省级区域 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `IssuerFirstAreaCode` | 所属省级区域代码 | number(10) | ✓ | 100.0% |  |
| 15 | `IssuerSecondArea` | 所属市级区域 | varchar2(100) | ✓ | 99.94% |  |
| 16 | `IssuerSecondAreaCode` | 所属市级区域代码 | number(10) | ✓ | 99.94% |  |
| 17 | `Guarantor` | 担保人 | varchar2(1000) | ✓ | 40.19% |  |
| 18 | `GuaranteeMethod` | 担保方式 | varchar2(200) | ✓ | 41.58% |  |
| 19 | `MultiGuarantor` | 再担保人 | varchar2(500) | ✓ | 0.0% |  |
| 20 | `CounGuarantor` | 反担保人 | varchar2(500) | ✓ | 0.38% |  |
| 21 | `CRAs` | 评级人 | varchar2(1000) | ✓ | 74.2% |  |
| 22 | `CRACode` | 初始评级机构代码 | number(10) | ✓ | 74.2% | 初始评级机构代码（CRACode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 23 | `CreditRating` | 初始债券信用级别 | varchar2(50) | ✓ | 74.2% |  |
| 24 | `CreditRatingCode` | 初始债项评级代码 | number(10) | ✓ | 74.2% | 初始债项评级代码(CreditRatingCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 25 | `Sponsor` | 保荐人 | varchar2(500) | ✓ | 65.24% |  |
| 26 | `LeadUnderwriter` | 主承销商 | varchar2(1000) | ✓ | 98.49% |  |
| 27 | `FirstDateOfDeliPeriod` | 退市整理期首日 | date | ✓ | 0.13% |  |
| 28 | `EndDateOfDeliPeriod` | 退市整理期截止日 | date | ✓ | 0.13% |  |
| 29 | `MaturityMode` | 到期退出方式 | number(10) | ✓ | 66.56% | 到期退出方式（MaturityMode）：1-转股，2-赎回，3-到期，4-回售 |
| 30 | `Maturity` | 债券期限(年) | number(5,2) | ✓ | 100.0% |  |
| 31 | `StartDate` | 起息日(债券期限起始日) | date | ✓ | 99.43% |  |
| 32 | `EndDate` | 到期日(债券期限截止日) | date | ✓ | 99.43% |  |
| 33 | `EarlyMaturityDate` | 实际到期日 | date | ✓ | 51.8% |  |
| 34 | `ParValue` | 初始债券面值(元) | number(19,4) | ✓ | 100.0% |  |
| 35 | `IssueVolume` | 发行张数(张) | number(16,0) | ✓ | 99.94% |  |
| 36 | `ActualIssueSize` | 实际发行规模(百万元) | number(19,4) | ✓ | 99.94% |  |
| 37 | `PrefAltSizeRatio` | 原股东配售转债占比(%) | number(19,4) | ✓ | 65.05% |  |
| 38 | `CompoundMethod` | 计息方式 | number(10) | ✓ | 100.0% | 计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 39 | `IntPaymentMethod` | 付息方式 | number(10) | ✓ | 100.0% | 付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，... |
| 40 | `CouponFreq` | 付息频率(次/年) | number(10) | ✓ | 100.0% |  |
| 41 | `RedemptionMethod` | 兑付方式 | number(10) | ✓ | 100.0% | 兑付方式(RedemptionMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1546，... |
| 42 | `IncrsCouponMargin` | 累进利率计息年递增额(%) | number(9,6) | ✓ | 4.98% |  |
| 43 | `RedeemOfInterest` | 到期利息补偿(元/张) | number(19,4) | ✓ | 85.43% |  |
| 44 | `CompRate` | 补偿利率(%) | number(10,4) | ✓ | 84.73% |  |
| 45 | `IntPaymentDescription` | 支付机制说明 | varchar2(255) | ✓ | 100.0% |  |
| 46 | `InterestItem` | 利息条款描述 | clob | ✓ | 19.81% |  |
| 47 | `InterestFormula` | 利息计算公式 | number(10) | ✓ | 0.0% | 利息计算公式(InterestFormula)：该字段维护公告披露利息计算规则，若未披露为NULL。实际使用可根据通用规... |
| 48 | `CouponRate` | 初始票面年利率(%) | number(9,6) | ✓ | 99.81% |  |
| 49 | `LatestCouponRate` | 最新票面利率(%) | number(18,6) | ✓ | 99.18% |  |
| 50 | `RateIfFloat` | 利率是否浮动 | number(10) | ✓ | 100.0% | 利率是否浮动(RateIfFloat)，该字段固定以下常量：1-是，2-否。本字段目前主要针对“计息方式”为“3-浮动利... |
| 51 | `InitialConvPrice` | (发行披露)初始转股价 | number(19,4) | ✓ | 97.92% |  |
| 52 | `BondOtherState` | 状态 | number(10) | ✓ | 0.63% | 状态(BondOtherState)：10-发行失败 |
| 53 | `OPMaturity` | 含权券特殊期限 | varchar2(100) | ✓ | 2.4% |  |
| 54 | `IfGuaranteedSettle` | 是否担保交收(交易所) | number(10) | ✓ | 83.53% | 是否担保交收(交易所)(IfGuaranteedSettle)与(CT_SystemConst)表中的DM字段关联，令L... |
| 55 | `FRNRefRateText` | 浮动利率计息基准 | number(10) | ✓ | 0.5% | 浮动利率计息基准(FRNRefRateText)与(CT_SystemConst)表中的DM字段关联，令LB = 101... |
| 56 | `FRNMargin` | 初始基准利差(%) | number(9,6) | ✓ | 0.0% |  |
| 57 | `MinAnnualRate` | 债券保底利率(%) | number(9,6) | ✓ | 0.0% |  |
| 58 | `RateAdjustMode` | 利率调整模式 | number(10) | ✓ | 0.5% | 利率调整模式(RateAdjustMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1469，... |
| 59 | `ListedDate` | 上市起始日 | date | ✓ | 97.29% |  |
| 60 | `TradeEndDate` | 摘牌日 | date | ✓ | 66.18% |  |
| 61 | `LastTradingDate` | 最后交易日 | date | ✓ | 55.9% |  |
| 62 | `DelistDate` | 停止交易日 | date | ✓ | 55.9% |  |
| 63 | `ListedMarket` | 上市交易平台 | varchar2(50) | ✓ | 98.23% |  |
| 64 | `TradeType` | 交易方式 | number(10) | ✓ | 83.53% | 交易方式(TradeType)：1-匹配成交;协商成交;点击成交;询价成交;竞买成交  2-协商成交;点击成交;询价成交... |
| 65 | `PricingMethod` | 最新计价方式 | number(10) | ✓ | 98.23% | 最新计价方式(PricingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1517 A... |
| 66 | `ConvStkAbbrName` | 转股简称 | varchar2(50) | ✓ | 23.28% | 转股简称(ConvStkAbbrName)：上海证券交易所自5月24日（含）起，可转债回售、可转债转股、可交换债换股业务... |
| 67 | `LatestConvPrice` | 最新转股价 | number(19,4) | ✓ | 97.92% |  |
| 68 | `ConvCode` | 转股申报代码 | varchar2(10) | ✓ | 24.79% | 转股申报代码(ConvCode)：上海证券交易所自5月24日（含）起，可转债回售、可转债转股、可交换债换股业务从辅助证券... |
| 69 | `ConvTermStartDate` | 转换期起始日 | date | ✓ | 97.85% |  |
| 70 | `ConvTermEndDate` | 转换期截止日 | date | ✓ | 97.85% |  |
| 71 | `LastConvDate` | 最后转股日 | date | ✓ | 97.85% |  |
| 72 | `StopConvDate` | 停止转股日(提前到期) | date | ✓ | 54.83% |  |
| 73 | `CallProtection` | 赎回保护期(年) | number(9,6) | ✓ | 0.0% |  |
| 74 | `CallPriceEnd` | 赎回价(到期赎回) | number(9,4) | ✓ | 82.78% |  |
| 75 | `PrimalGuarRatio` | 初始担保比例 | number(19,4) | ✓ | 17.67% |  |
| 76 | `IfIssuedUnspec` | 是否向不特定对象发行 | number(10) | ✓ | 100.0% | 是否向不特定对象发行（IfIssuedUnspec）：1-是  2-否 |
| 77 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 78 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 79 | `JSID` | JSID | number(19) | ✗ |  |  |
| 80 | `ListedEndDate` | 上市截止日 | date | ✓ | 57.1% |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### StockInnerCode (对应基础股票内部代码)

对应基础股票内部代码(StockInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。

### BondForm (债券形式)

债券形式(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM IN (1,2,4)，得到债券形式的具体描述：1-常规债券，2-分离交易可转债，4-可交换公司债券。

### CBEmbeddedOption (附属权证)

附属权证(CBEmbeddedOption)：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到附属权证的交易代码、交易简称等。

### LatestStatus (最新状态)

最新状态（LatestStatus）：1-发行中，2-存续中，3-已到期，4-发行失败

### CompanyCode (发行人公司代码)

发行人公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### IndustryCode (所属行业代码(证监会))

所属行业代码(证监会)(IndustryCode)：与“行业类别表（CT_IndustryType）”的“ 行业内部编码(IndustryNum)”关联，得到行业的详细名称与信息

### CRACode (初始评级机构代码)

初始评级机构代码（CRACode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到评级机构的具体名称、基本信息等。

### CreditRatingCode (初始债项评级代码)

初始债项评级代码(CreditRatingCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1372，得到初始债项评级代码的具体描述：740-D，760-C，770-CC，799-CCC，830-B-，840-B，850-B+，860-BB-，870-BB，880-BB+，891-BBB-，895-BBB，899-BBB+，930-A-，940-A，950-A+，960-AA-，970-AA，980-AA+，990-AAA-，999-AAA，1000-AAA+。

### MaturityMode (到期退出方式)

到期退出方式（MaturityMode）：1-转股，2-赎回，3-到期，4-回售

## SQL示例

```sql
-- 查询 可转债基本信息 数据
SELECT *
FROM bond_conbdbasicinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
