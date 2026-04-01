# LC_SHPromise

**中文名**: 股东承诺

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHPromise` |
| MySQL表名 | `lc_shpromise` |
| 中文名 | 股东承诺 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 113 |
| 版本 | 1.02 |

## 表描述

1.收录股权分置改革中非流通股东承诺事项，包括对价支付、持股变动、限售解禁期限、上市价格、增持计划等类别指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.83% |  |
| 6 | `PromiseSubject` | 承诺主体 | number(10) | ✓ | 100.0% | 承诺主体(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351，得到... |
| 7 | `EventType` | 事项类型 | number(10) | ✓ | 100.0% | 事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352，得到事项类型的... |
| 8 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效（IfEffected），该字段固定以下常量：0-否；1-是；2-否 |
| 9 | `SHSN` | 股东序号 | number(10) | ✓ | 98.5% |  |
| 10 | `SHName` | 股东名单 | varchar2(200) | ✓ | 98.51% |  |
| 11 | `CompanyNumber` | 企业编号 | number(10) | ✓ | 0.59% | 企业编号(CompanyNumber)和机构基本资料表（LC_InstiArchive）中企业编号（CompanyCod... |
| 12 | `PromiseType` | 承诺类别 | number(10) | ✓ |  | 承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306，得到承诺类... |
| 13 | `ShareConsideration` | 1)直接支付对价股份总额 | number(18,2) | ✓ | 9.58% |  |
| 14 | `CashConsideration` | 直接支付对价现金总额 | number(19,4) | ✓ | 0.23% |  |
| 15 | `WarrantConsideration` | 直接支付对价认股证总额 | number(18,2) | ✓ | 0.05% |  |
| 16 | `ShareCompressed` | 2)缩股总额 | number(18,2) | ✓ | 0.1% |  |
| 17 | `ShareConsiderationTranPaid` | 3)转付对价股份总额 | number(18,2) | ✓ | 0.63% |  |
| 18 | `CashConsiderationTranPaid` | 转付对价现金总额 | number(19,4) | ✓ | 0.18% |  |
| 19 | `WarrantConsiderationTranPaid` | 转付对价认股证总额 | number(18,2) | ✓ | 0.0% |  |
| 20 | `OtherConsideration` | 其他对价说明 | varchar2(500) | ✓ | 1.62% |  |
| 21 | `HoldingBeforeConsideration` | 1)对价支付前持股数 | number(18,2) | ✓ | 15.58% |  |
| 22 | `ATradableShare` | 其中:流通A股 | number(18,2) | ✓ | 0.01% |  |
| 23 | `ShareKind` | 股本性质 | number(10) | ✓ | 14.12% | 股本性质(ShareKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1024，得到股本性质的... |
| 24 | `HoldingRatioBConsideration` | 对价支付前持股比例 | number(18,8) | ✓ | 15.53% |  |
| 25 | `PledgedShare` | 质押股份数量 | number(18,2) | ✓ | 0.44% |  |
| 26 | `FrozenShare` | 冻结股份数量 | number(18,2) | ✓ | 0.17% |  |
| 27 | `HoldingAfterConsideration` | 2)对价支付后持股数 | number(18,2) | ✓ | 15.49% |  |
| 28 | `ATShareUnrestricted` | 其中:无限售流通A股 | number(18,2) | ✓ | 0.01% |  |
| 29 | `HoldingRatioAConsideration` | 对价支付后持股比例 | number(18,8) | ✓ | 15.48% |  |
| 30 | `ListingDate` | 3)上市流通日期 | date | ✓ | 11.05% |  |
| 31 | `PromisingRestrictedTerm` | 1)获流通权后承诺限售期限 | number(18,8) | ✓ | 33.03% |  |
| 32 | `PromisingRestrictedStatement` | 限售期限说明 | varchar2(1000) | ✓ | 0.0% |  |
| 33 | `PromisingHoldingRatio` | 2)获流通权后承诺持股比例下限 | number(18,8) | ✓ | 0.05% |  |
| 34 | `TermOfHoldingRatio` | 获流通权后最低持股比例承诺期限 | number(18,8) | ✓ | 0.04% |  |
| 35 | `EndDateOfHoldingRatio` | 获流通权后最低持股比例截止日 | date | ✓ | 0.0% |  |
| 36 | `LowestHoldingStatement` | 最低持股说明 | varchar2(1000) | ✓ | 0.0% |  |
| 37 | `FirstSaleRatio` | 1)首期出售股份比例上限-占总股本(限售期满后) | number(18,8) | ✓ | 1.93% |  |
| 38 | `FirstSaleHoldingRatio` | 首期出售股份比例上限-占所持有股本(限售期满后) | number(18,8) | ✓ | 0.0% |  |
| 39 | `FirstSaleTerm` | 首期出售承诺期限(限售期满后) | number(18,8) | ✓ | 1.93% |  |
| 40 | `SecondSaleRatio` | 2)二期出售股份比例上限-占总股本(限售期满后起) | number(18,8) | ✓ | 1.59% |  |
| 41 | `SecondSaleHoldingRatio` | 二期出售股份比例上限-占所持有股本(限售期满后) | number(18,8) | ✓ | 0.0% |  |
| 42 | `SecondSaleTerm` | 二期出售承诺期限(限售期满后起) | number(18,8) | ✓ | 1.59% |  |
| 43 | `StepSaleStatement` | 分步出售说明 | varchar2(1000) | ✓ | 0.0% |  |
| 44 | `RestrictedListingPrice` | 承诺限制上市触发价格 | number(19,4) | ✓ | 0.51% |  |
| 45 | `ListingPriceCondition` | 上市价格条件描述 | varchar2(200) | ✓ | 0.52% |  |
| 46 | `ListingPrice` | 上市价格条件 | number(10) | ✓ | 0.51% | 上市价格条件(ListingPrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1297，得到... |
| 47 | `ListingPriceTerm` | 上市价格期限描述 | varchar2(200) | ✓ | 0.52% |  |
| 48 | `TermOfRLPrice` | 上市触发价格有效期限(限售期满后) | number(18,8) | ✓ | 0.44% |  |
| 49 | `DeadlineOfRLPrice` | 上市触发价格有效期限截止 | date | ✓ | 0.02% |  |
| 50 | `PromiseStatement` | 上市承诺说明 | varchar2(1000) | ✓ | 31.87% |  |
| 51 | `AddingHoldingTime` | 增持时间描述 | varchar2(200) | ✓ | 7.78% |  |
| 52 | `AddingHoldingStartDateType` | 增持起始日期类别 | number(10) | ✓ | 0.11% | 增持起始日期类别(AddingHoldingStartDateType)与(CT_SystemConst)表中的DM字段... |
| 53 | `AddingHoldingTerm` | 增持实施期限 | number(18,8) | ✓ | 7.58% |  |
| 54 | `AddingHoldingPriceStatement` | 增持价格描述 | varchar2(200) | ✓ | 4.66% |  |
| 55 | `AddingHoldingTriggerPrice` | 增持股票触发价格 | number(19,4) | ✓ | 0.13% |  |
| 56 | `AddingHoldingPrice` | 增持价格条件 | number(10) | ✓ | 0.07% | 增持价格条件(AddingHoldingPrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 57 | `AddingHoldingSize` | 增持规模描述 | varchar2(200) | ✓ | 7.82% |  |
| 58 | `AddingHoldingShareCeiling` | 增持股份数量上限 | number(18,2) | ✓ | 1.18% |  |
| 59 | `AddingHoldingShareMin` | 增持股份数量下限 | number(18,2) | ✓ | 1.44% |  |
| 60 | `AddingHoldingRatioCeiling` | 增持比例上限-占总股本 | number(18,8) | ✓ | 1.83% |  |
| 61 | `AddingHoldingRatioMin` | 增持比例下限-占总股本 | number(18,8) | ✓ | 0.67% |  |
| 62 | `AddingHoldingFundCeiling` | 增持投入资金上限 | number(19,4) | ✓ | 3.1% |  |
| 63 | `AddingHoldingFundMin` | 增持投入资金下限 | number(19,4) | ✓ | 4.05% |  |
| 64 | `AddingHoldingRestrictedTerm` | 增持股份限售期限 | number(18,8) | ✓ | 4.33% |  |
| 65 | `AddingHoldingStatement` | 增持计划说明 | varchar2(1000) | ✓ | 8.26% |  |
| 66 | `SaleRightTime` | 出售权实施时间描述 | varchar2(200) | ✓ | 0.0% |  |
| 67 | `SaleRightStartDateType` | 出售权起始日期类别 | number(10) | ✓ | 0.0% | 出售权起始日期类别(SaleRightStartDateType)与(CT_SystemConst)表中的DM字段关联，... |
| 68 | `SaleRightExerciseTerm` | 出售权实施期限 | number(18,8) | ✓ | 0.0% |  |
| 69 | `SaleExerciseTerms` | 出售权实施条件描述 | varchar2(200) | ✓ | 0.0% |  |
| 70 | `SaleRightTriggeringPrice` | 出售权触发价格 | number(19,4) | ✓ | 0.0% |  |
| 71 | `SaleRightPrice` | 出售权价格条件 | number(10) | ✓ | 0.0% | 出售权价格条件(SaleRightPrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1297... |
| 72 | `SaleRightSize` | 出售权实施规模描述 | varchar2(200) | ✓ | 0.0% |  |
| 73 | `SaleRightShareRatio` | 出售权股份比例-占流通股 | number(18,8) | ✓ | 0.0% |  |
| 74 | `SaleExercisePrice` | 出售权实施价格 | number(19,4) | ✓ | 0.0% |  |
| 75 | `SaleRightStatement` | 出售权说明 | varchar2(1000) | ✓ | 0.0% |  |
| 76 | `AddingGrantingTime` | 追送时间描述 | varchar2(200) | ✓ | 0.34% |  |
| 77 | `AddingGrantingStartDateType` | 追送起始日期类别 | number(10) | ✓ | 0.23% | 追送起始日期类别(AddingGrantingStartDateType)与(CT_SystemConst)表中的DM字... |
| 78 | `AddingGrantingTerm` | 追送实施期限 | number(18,8) | ✓ | 0.05% |  |
| 79 | `AddingGrantingTrigger` | 追送触发条件说明 | varchar2(1000) | ✓ | 0.34% |  |
| 80 | `AddingGrantingSize` | 追送规模描述 | varchar2(200) | ✓ | 0.34% |  |
| 81 | `AddingGrantingRate` | 追送比例(10送X)-流通股获付 | number(18,8) | ✓ | 0.26% |  |
| 82 | `AddingGrantingShares` | 追送股数(万股/万份) | number(18,2) | ✓ | 0.19% |  |
| 83 | `AddingGrantingRatio` | 追送占股东持股比例 | number(18,8) | ✓ | 0.02% |  |
| 84 | `AddingGrantingTimes` | 追送次数(次) | number(10) | ✓ | 0.3% |  |
| 85 | `AddingGrantingStatement` | 追送说明 | varchar2(1000) | ✓ | 0.34% |  |
| 86 | `MarginPayingTime` | 差额支付时间描述 | varchar2(200) | ✓ | 0.0% |  |
| 87 | `MarginPayingStartDateType` | 差额支付起始日期类别 | number(10) | ✓ | 0.0% | 差额支付起始日期类别(MarginPayingStartDateType)与(CT_SystemConst)表中的DM字... |
| 88 | `MarginPayingTerm` | 差额支付实施期限 | number(18,6) | ✓ | 0.0% |  |
| 89 | `MarginPayingCondition` | 差额支付条件描述 | varchar2(200) | ✓ | 0.0% |  |
| 90 | `MarginPayingTrigger` | 差额支付触发价格 | number(19,4) | ✓ | 0.0% |  |
| 91 | `MarginPayingPrice` | 差额支付价格条件 | number(10) | ✓ | 0.0% | 差额支付价格条件(MarginPayingPrice)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 92 | `MarginPayingAmount` | 差额支付金额描述 | varchar2(200) | ✓ | 0.0% |  |
| 93 | `MarginPayingShares` | 差额支付涉及股数(万股/万份) | number(18,2) | ✓ | 0.0% |  |
| 94 | `MarginPayingRatio` | 差额支付涉及比例-占无受限流通股(%) | number(18,6) | ✓ | 0.0% |  |
| 95 | `MarginPayingStatement` | 差额支付说明 | varchar2(1000) | ✓ | 0.0% |  |
| 96 | `StimulantTime` | 股权激励实施时间描述 | varchar2(200) | ✓ | 0.06% |  |
| 97 | `StimulantCondition` | 股权激励实施条件描述 | varchar2(200) | ✓ | 0.03% |  |
| 98 | `StimulantShareBConsideration` | 支付对价前股权激励股数 | number(18,2) | ✓ | 0.01% |  |
| 99 | `StimulantShareAConsideration` | 支付对价后股权激励股数 | number(18,2) | ✓ | 0.06% |  |
| 100 | `SubscribingPrice` | 认购价格 | number(19,4) | ✓ | 0.01% |  |
| 101 | `SubscribingPriceCondition` | 认购价格条件 | number(10) | ✓ | 0.01% | 认购价格条件(SubscribingPriceCondition)与(CT_SystemConst)表中的DM字段关联，... |
| 102 | `ExercisePrice` | 行权价格 | number(19,4) | ✓ | 0.0% |  |
| 103 | `ShareStimulusStatement` | 股权激励说明 | varchar2(500) | ✓ | 0.29% |  |
| 104 | `SharesInvolved` | 涉及股数(股/份) | number(19,2) | ✓ | 3.4% |  |
| 105 | `RestrictedState` | 限售状态(承诺时) | number(10) | ✓ | 3.5% | 限售状态(承诺时)(RestrictedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 106 | `ProlongedLockupPeriod` | 延长锁定期限(月) | number(18,8) | ✓ | 3.42% |  |
| 107 | `DeadlineLockupDate` | 锁定期限截止 | date | ✓ | 0.17% |  |
| 108 | `DividendPromise` | 分红承诺说明 | varchar2(1000) | ✓ | 0.39% |  |
| 109 | `DefaultPromise` | 违约承诺说明 | varchar2(1000) | ✓ | 3.03% |  |
| 110 | `OtherPromise` | 其他承诺说明 | clob | ✓ | 32.35% |  |
| 111 | `InsertTime` | 发布时间 | date | ✓ |  | 发布时间(InsertTime)：指该条记录首次在本表发布的时间。 |
| 112 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 113 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### PromiseSubject (承诺主体)

承诺主体(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351，得到承诺主体的具体描述：100-非流通股东，110-间接控股股东，150-流通股东，300-上市公司，500-公司管理层。

### EventType (事项类型)

事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352，得到事项类型的具体描述：10-股改时承诺，15-股改后追加承诺，25-发行后追加承诺，31-承诺总体说明，35-承诺变更说明，51-对价支付及持股变动，61-招股时承诺，71-新股上市股东承诺，72-上市后股东追加承诺。

### IfEffected (是否有效)

是否有效（IfEffected），该字段固定以下常量：0-否；1-是；2-否

### CompanyNumber (企业编号)

企业编号(CompanyNumber)和机构基本资料表（LC_InstiArchive）中企业编号（CompanyCode）关联

### PromiseType (承诺类别)

承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306，得到承诺类别的具体描述：11-直接支付对价，13-转付对价，15-直接缩股，19-其他对价，20-不支付转付对价，21-由其他股东垫付对价，31-代其他股东垫付对价，101-上市限售期限，102-询价转让限售期限，104-最低持股比例，107-分步出售比例，110-上市价格限制，121-延长锁定期，124-不减持，127-主动减持计划，128-被动减持计划，201-增持计划，301-流通股东出售权，401-股份追送，403-股价差额现金支付，501-股权激励，991-违约责任承诺，992-分红承诺，993-资产注入承诺，999-其他承诺。

### ShareKind (股本性质)

股本性质(ShareKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1024，得到股本性质的具体描述：1-流通A股，2-H股，3-B股，4-国家股，5-法人股，6-境外法人股，7-职工股，8-转配股，9-个人持股，10-S股，11-限售流通A股，12-境内优先股，13-境外优先股，15-N股，16-D股，17-三板流通股，43-国有法人股，51-A类普通股，52-B类普通股，53-C类普通股，54-D类普通股，80-有投票权的优先股，99-其他，100-个人股，101-GDR代表基础股票，102-CDR代表基础股票。

### ListingPrice (上市价格条件)

上市价格条件(ListingPrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1297，得到上市价格条件的具体描述：100-收盘价，101-点位价，201-连续5日收盘价，202-连续2日收盘价，203-连续3日收盘价，210-连续10日收盘价，220-连续20日中累计10日收盘价，230-复牌后20个交易日收盘价的算术平均值。

### AddingHoldingStartDateType (增持起始日期类别)

增持起始日期类别(AddingHoldingStartDateType)与(CT_SystemConst)表中的DM字段关联，令LB = 1307，得到增持起始日期类别的具体描述：10-股东大会通过后，20-改革方案实施后，21-方案实施后或实施日起12个月后，41-当年年报披露后，42-当年或次年年报披露后。

### AddingHoldingPrice (增持价格条件)

增持价格条件(AddingHoldingPrice)与(CT_SystemConst)表中的DM字段关联，令LB = 1297，得到增持价格条件的具体描述：100-收盘价，101-点位价，201-连续5日收盘价，202-连续2日收盘价，203-连续3日收盘价，210-连续10日收盘价，220-连续20日中累计10日收盘价，230-复牌后20个交易日收盘价的算术平均值。

## SQL示例

```sql
-- 查询 股东承诺 数据
SELECT *
FROM lc_shpromise
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
