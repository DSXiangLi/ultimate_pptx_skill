# Bond_BasicInfo

**中文名**: 债券要素表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BasicInfo` |
| MySQL表名 | `bond_basicinfo` |
| 中文名 | 债券要素表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 63 |
| 版本 | 1.04 |

## 表描述

1.本表展现所有债券（除可转债、券商专项资产支持证券以外）的基本要素。
2.涵盖在交易所、银行间、柜台等所有市场上交易的国债、金融债、企业债、短期融资券、资产支持证券、央行票据等各类债券，本表是以债券整体的角度展示了债券的基本资料，对于跨市场交易的债券，本表展示了其中一个市场的代码。。
3.包括记帐式、凭证式等各种形态的债券，不管其是否上市交易。
4.在该表“债券要素”栏目下，剔除带“*”的字段，余下的字段与中央国债登记结算中心披露的“债券交易流通要素公告”中的字段一一对应。
5.该表中的资产支持证券为人民银行监管的债券，包括ABS和MBS两种。
6.数据范围：1981-1-1 至今
7.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 债券统一代码 | number(10) | ✗ | 100.0% | 债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `BondFullName` | 债券全称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `CustodyCode` | 银行间托管代码 | varchar2(10) | ✓ | 89.86% | 银行间托管代码（CustodyCode）：债券在银行间市场托管代码。 |
| 6 | `BondForm` | 债券形态 | number(10) | ✓ | 99.99% | 债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具... |
| 7 | `BondNature` | 债券类型 | number(10) | ✓ | 100.0% | 债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型... |
| 8 | `OptionType` | 选择权类型 | varchar2(200) | ✓ | 14.61% |  |
| 9 | `IfSTRIPS` | 是否可分离债 | number(10) | ✓ | 100.0% | 是否可分离债(IfSTRIPS)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM... |
| 10 | `Issuer` | 发行人 | varchar2(1000) | ✓ | 100.0% |  |
| 11 | `IssuerNature` | 发行人性质 | number(10) | ✓ | 100.0% | 发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND... |
| 12 | `Guarantor` | 担保人 | varchar2(1000) | ✓ | 3.51% |  |
| 13 | `MultiGuarantor` | 再担保人 | varchar2(500) | ✓ | 0.01% |  |
| 14 | `Sponsor` | 保荐人 | varchar2(500) | ✓ | 0.14% |  |
| 15 | `LeadUnderwriter` | 主承销商 | varchar2(1000) | ✓ | 33.81% |  |
| 16 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✓ | 100.0% |  |
| 17 | `CreditRating` | 债项信用级别 | varchar2(50) | ✓ | 17.91% |  |
| 18 | `CRAs` | 债项信用机构 | varchar2(1000) | ✓ | 17.91% |  |
| 19 | `ActualIssueSize` | 实际发行总额(亿元) | number(19,4) | ✓ | 99.99% | （实际）发行总额（ActualIssueSize）：本字段下收录债券首次发行规模，若有增发或债券合并等情况，请通过“债券... |
| 20 | `Maturity` | 债券期限(年) | number(9,4) | ✓ | 99.98% |  |
| 21 | `OPMaturity` | 含权券特殊期限 | varchar2(100) | ✓ | 8.1% |  |
| 22 | `ParValue` | *初始债券面值(元) | number(19,4) | ✓ | 100.0% |  |
| 23 | `IssuePrice` | 初始发行价格(元) | number(19,4) | ✓ | 99.92% |  |
| 24 | `CurrencyUnit` | *货币单位 | number(10) | ✓ | 100.0% | *货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and... |
| 25 | `IssueRefYTM` | *发行参考收益率(%) | number(10,6) | ✓ | 60.49% |  |
| 26 | `CompoundMethod` | 计息方式 | number(10) | ✓ | 98.72% | 计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 27 | `IntPaymentMethod` | *付息方式 | number(10) | ✓ | 37.66% | *付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168... |
| 28 | `PayInterestEffency` | 付息频率(次/年) | number(10) | ✓ | 37.66% | 付息频率(次/年)（PayInterestEffency）：到期一次性还本付息的债券，其付息频率为0；每年付息的债券，其... |
| 29 | `PMRemark` | *支付机制说明 | varchar2(255) | ✓ | 98.62% |  |
| 30 | `InterestItem` | *利息条款描述 | clob | ✓ | 63.92% |  |
| 31 | `InterestFormula` | *利息计算公式 | number(10) | ✓ | 76.5% | *利息计算公式(InterestFormula)与(CT_SystemConst)表中的DM字段关联，令LB = 147... |
| 32 | `InterestFormulaHS` | *利息计算公式(沪深) | number(10) | ✓ | 0.04% | *利息计算公式(沪深)(InterestFormulaHS)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 33 | `RedemptionMethod` | 兑付方式 | number(10) | ✓ | 99.0% | 兑付方式(RedemptionMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1546，... |
| 34 | `CouponRate` | 初始票面年利率(%) | number(9,6) | ✓ | 97.02% |  |
| 35 | `RateIfFloat` | *利率是否浮动 | number(10) | ✓ | 37.73% | 利率是否浮动（RateIfFloat），该字段固定以下常量：1-是；2-否。本字段目前主要针对“计息方式”为“3-浮动利... |
| 36 | `IssueDate` | 发行日 | date | ✓ | 98.24% | 发行日（IssueDate）：本字段先取值债券公告中公布的发行日，再取值招标日、最后取值分销日，如果需要公告中的发行日，... |
| 37 | `BidDate` | 招标日 | date | ✓ | 34.48% |  |
| 38 | `TransferDate` | *划款日 | date | ✓ | 97.29% |  |
| 39 | `ValueDate` | 起息日(债券期限起始日) | date | ✓ | 98.3% |  |
| 40 | `EndDate` | 到期日(债券期限截止日) | date | ✓ | 98.29% |  |
| 41 | `RegDate` | 债权债务登记日 | date | ✓ | 77.05% |  |
| 42 | `ListedDate` | 上市日(交易流通起始日) | date | ✓ | 91.53% |  |
| 43 | `DelistDate` | 摘牌日(交易流通终止日) | date | ✓ | 83.5% |  |
| 44 | `EarlyMaturityDate` | 实际到期日 | date | ✓ | 3.87% |  |
| 45 | `RedemptionDate` | 首次兑付日 | date | ✓ | 91.49% |  |
| 46 | `Remark` | 备注 | varchar2(500) | ✓ | 2.52% |  |
| 47 | `FRNRefRateSelecrRemark` | 浮动利率计息基准 | number(10) | ✓ | 2.31% | 浮动利率计息基准(FRNRefRateSelecrRemark)与(CT_SystemConst)表中的DM字段关联，令... |
| 48 | `FRNRefRatePer` | 初始基准利率(%) | number(9,6) | ✓ | 0.49% |  |
| 49 | `FRNMargin` | 初始基准利差(%) | number(9,6) | ✓ | 2.07% |  |
| 50 | `MinAnnualRate` | 债券保底利率(%) | number(9,6) | ✓ | 0.0% |  |
| 51 | `PrimalPricingDate` | 首个定价日 | date | ✓ | 0.42% |  |
| 52 | `RateAdjustMode` | *利率调整模式 | number(10) | ✓ | 0.51% | *利率调整模式(RateAdjustMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1469... |
| 53 | `LegalEndDate` | *法定到期日 | date | ✓ | 2.55% |  |
| 54 | `CreatOrg` | *发起机构 | varchar2(200) | ✓ | 2.52% |  |
| 55 | `ABSLevel` | *分层级别 | number(10) | ✓ | 2.82% | *分层级别(ABSLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 1417 and DM ... |
| 56 | `ABSLevely` | *分层级别细分 | number(10) | ✓ | 1.17% | *分层级别细分(ABSLevely)与(CT_SystemConst)表中的DM字段关联，令LB = 1998，得到*分... |
| 57 | `BasicAssetType` | *基础资产类型 | number(10) | ✓ | 2.71% | *基础资产类型(BasicAssetType)与(CT_SystemConst)表中的DM字段关联，令LB = 2003... |
| 58 | `ABSLevelRatio` | *规模分层占比(%) | number(19,8) | ✓ | 2.84% |  |
| 59 | `InterestCap` | *利率上限说明 | varchar2(200) | ✓ | 0.26% |  |
| 60 | `InitialInvestorNum` | 初始投资人数量 | number(10) | ✓ | 0.34% |  |
| 61 | `PrivateInvestorNum` | 定向投资人数量 | number(10) | ✓ | 0.34% |  |
| 62 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 63 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (债券统一代码)

债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### CustodyCode (银行间托管代码)

银行间托管代码（CustodyCode）：债券在银行间市场托管代码。

### BondForm (债券形态)

债券形态(BondForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1242，得到债券形态的具体描述：1-实名制记帐式，2-无记名实物券，3-凭证式国债，4-其他形式，5-电子式储蓄国债。

### BondNature (债券类型)

债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券类型的具体描述：1-企业债券，2-金融债券，3-金融次级债，4-国债现货，5-央行票据，6-短期融资券，7-MBS(房贷支持)，8-ABS(其他支持)，9-混合资本债券，10-可转换债券，11-国库现金管理，12-资产证券化，13-公司债券，14-中期票据，15-转债分离公司债，16-地方政府债券，17-中小企业集合票据，18-集合债券，19-超短期融资券，20-非公开定向债务融资工具，21-次级定期债务，22-中小企业区域集优票据，23-政府支持债券，24-中小企业私募债券，25-资产支持票据，26-小微企业扶持债券，27-二级资本债券，28-中小企业可交换私募债，29-可交换公司债券，30-同业存单，31-区域集优中期票据，32-项目收益票据，33-项目收益债券，34-证券公司短期公司债券，35-保险公司资本补充债券，36-非公开发行公司债，37-信用风险缓释凭证，38-信用联结票据，39-其他一级资本工具，40-标准化票据，41-自贸区债，42-TLAC非资本债券，99-其他。

### IfSTRIPS (是否可分离债)

是否可分离债(IfSTRIPS)与(CT_SystemConst)表中的DM字段关联，令LB = 1413 AND DM IN (1,3)，得到是否可分离债的具体描述：1-常规债券，3-本息分离交易债券。

### IssuerNature (发行人性质)

发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM NOT IN (21)，得到发行人性质的具体描述：10-中央银行，11-政策性银行，13-商业银行，20-财政部，22-地方财政，29-其他部委，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，70-国际机构，75-自然人，80-外国主权政府，81-外国地方政府，91-建设基金，99-一般企业，100-地方融资平台。

### ActualIssueSize (实际发行总额(亿元))

（实际）发行总额（ActualIssueSize）：本字段下收录债券首次发行规模，若有增发或债券合并等情况，请通过“债券规模（Bond_Size）”表获取相关信息。

### CurrencyUnit (*货币单位)

*货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1420,9990)，得到*货币单位的具体描述：1000-美元，1420-人民币元，9990-特别提款权。

### CompoundMethod (计息方式)

计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AND DM in (1,3,4,5,6)，得到计息方式的具体描述：1-单利(固定利率)，3-浮动利率，4-累进利率，5-贴现，6-无序利率。

## SQL示例

```sql
-- 查询 债券要素表 数据
SELECT *
FROM bond_basicinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
