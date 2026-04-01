# MF_FundArchives

**中文名**: 公募基金概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundArchives` |
| MySQL表名 | `mf_fundarchives` |
| 中文名 | 公募基金概况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 73 |
| 版本 | 1.08 |

## 表描述

1.本表记录了基金基本情况，包括基金规模、成立日期、投资类型、管理人、托管人、存续期、历史简介等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 4 | `ApplyingCodeFront` | 前端申购代码 | varchar2(10) | ✓ | 99.78% | 前端申购代码（ApplyingCodeFront）：取值为场外前端申购代码>场内申赎代码（场内基金）。 |
| 5 | `ApplyingCodeBack` | 后端申购代码 | varchar2(10) | ✓ | 0.76% |  |
| 6 | `SecurityCode` | 基金代码 | varchar2(10) | ✓ | 100.0% |  |
| 7 | `SecuCode` | 证券代码 | varchar2(10) | ✓ | 100.0% |  |
| 8 | `MainCode` | 基金主代码 | varchar2(10) | ✓ | 100.0% | 基金主代码（MainCode）：该字段记录基金季报中公布的基金主代码信息，当基金为非分级基金或分级基金主代码时，该字段与... |
| 9 | `ExApplyingMarket` | 场内申购赎回场所 | number(10) | ✓ | 8.7% | 场内申购赎回场所(ExApplyingMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 2... |
| 10 | `ExApplyingCode` | 场内申购赎回代码 | varchar2(10) | ✓ | 8.7% |  |
| 11 | `ExApplyingAbbr` | 场内申购赎回简称 | varchar2(100) | ✓ | 8.7% |  |
| 12 | `Type` | 基金运作方式 | number(10) | ✓ | 100.0% | 基金运作方式(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 1210 AND DM IN(... |
| 13 | `FundNature` | 基金性质 | number(10) | ✓ | 100.0% | 基金性质(FundNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1485，得到基金性质... |
| 14 | `InvestmentType` | 是否指数型 | number(10) | ✓ | 100.0% | 是否指数型(InvestmentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1094 A... |
| 15 | `InvestStyle` | 基金投资风格 | number(10) | ✓ | 100.0% | 基金投资风格(InvestStyle)与(CT_SystemConst)表中的DM字段关联，令LB = 1093，得到基... |
| 16 | `FundType` | 基金类别 | varchar2(100) | ✓ | 100.0% |  |
| 17 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1249 AN... |
| 18 | `InvestOrientation` | 基金投资方向 | varchar2(1000) | ✓ | 100.0% |  |
| 19 | `InvestTarget` | 基金投资目标 | varchar2(1000) | ✓ | 100.0% |  |
| 20 | `InvestField` | 基金投资范围 | varchar2(2000) | ✓ | 100.0% |  |
| 21 | `PerformanceBenchMark` | 业绩比较基准 | varchar2(500) | ✓ | 100.0% |  |
| 22 | `RiskReturncharacter` | 风险收益特征 | varchar2(500) | ✓ | 99.85% |  |
| 23 | `ProfitDistributionRule` | 收益分配原则 | varchar2(1000) | ✓ | 100.0% |  |
| 24 | `ExProfitDistri` | 场内收益分配方式 | number(10) | ✓ | 10.42% | 场内收益分配方式(ExProfitDistri)与(CT_SystemConst)表中的DM字段关联，令LB = 198... |
| 25 | `OTCProfitDistri` | 场外收益分配方式 | number(10) | ✓ | 93.77% | 场外收益分配方式(OTCProfitDistri)与(CT_SystemConst)表中的DM字段关联，令LB = 19... |
| 26 | `BriefIntro` | 基金简介 | clob | ✓ | 2.98% |  |
| 27 | `FloatType` | 发售方式 | number(10) | ✓ | 100.0% | 发售方式(FloatType)与(CT_SystemConst)表中的DM字段关联，令LB = 1652，得到发售方式的... |
| 28 | `FoundedSize` | 基金设立规模(份) | number(18,2) | ✓ | 97.03% |  |
| 29 | `EstablishmentDate` | 设立日期 | date | ✓ | 98.24% |  |
| 30 | `EstablishmentDateII` | 转型前设立日期 | date | ✓ | 3.52% |  |
| 31 | `ListedDate` | 上市日期 | date | ✓ | 8.33% |  |
| 32 | `Duration` | 存续年限(年) | number(18,2) | ✓ | 0.99% |  |
| 33 | `StartDate` | 存续期起始日 | date | ✓ | 98.24% |  |
| 34 | `ExpireDate` | 存续期截止日 | date | ✓ | 17.4% | 存续期截止日（ExpireDate）：优先取契约型封闭式基金的存续期截止日，其次取基金的清算日>合同失效日。 |
| 35 | `LastOperationDate` | 最后运作日 | date | ✓ | 17.13% | 最后运作日（LastOperationDate）：指基金的最后运作日，一般是净值的最后披露日，是清算日的前一个工作日。 |
| 36 | `StClearingDate` | 清算起始日 | date | ✓ | 11.3% |  |
| 37 | `EnClearingDate` | 清算截止日 | date | ✓ | 11.02% |  |
| 38 | `GuaranteedPeriod` | 保本型基金保本期(月) | number(18,2) | ✓ | 0.68% |  |
| 39 | `CarryOverDate` | 货币基金结转日 | number(10) | ✓ | 3.84% | 货币基金结转日(CarryOverDate)与(CT_SystemConst)表中的DM字段关联，令LB = 1250，... |
| 40 | `CarryOverDateRemark` | 货币基金结转日说明 | varchar2(100) | ✓ | 3.84% |  |
| 41 | `CarryOverType` | 货币基金收益分配方式(份额结转方式) | number(10) | ✓ | 3.84% | 货币基金收益分配方式(份额结转方式)(CarryOverType)与(CT_SystemConst)表中的DM字段关联，... |
| 42 | `AgrBenchmkRateOfShareA` | A份额约定年基准收益率表达式 | varchar2(200) | ✓ | 0.31% | A份额约定年基准收益率表达式（AgrBenchmkRateOfShareA）：本表该字段已停止维护，此信息在分级基金主表... |
| 43 | `AgrBenchmkRateOfShareANotes` | A份额约定年基准收益率表达式备注 | varchar2(1000) | ✓ | 0.31% | A份额约定年基准收益率表达式备注（AgrBenchmkRateOfShareANotes）：本表该字段已停止维护，此信息... |
| 44 | `ShareProperties` | 份额属性 | number(10) | ✓ | 1.43% | 份额属性(ShareProperties)与(CT_SystemConst)表中的DM字段关联，令LB = 1651，得... |
| 45 | `RegularShareConversionNotes` | 定期份额折算说明 | varchar2(1000) | ✓ | 0.3% | 定期份额折算说明（RegularShareConversionNotes）：本表该字段已停止维护，此信息在分级基金主表（... |
| 46 | `NonRegularShareConversionNotes` | 不定期份额折算说明 | varchar2(1000) | ✓ | 0.14% | 不定期份额折算说明（NonRegularShareConversionNotes）：本表该字段已停止维护，此信息在分级基... |
| 47 | `Manager` | 基金经理 | varchar2(50) | ✓ | 82.05% |  |
| 48 | `InvestAdvisorCode` | 基金管理人 | number(10) | ✓ | 100.0% | 基金管理人代码（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutlin... |
| 49 | `TrusteeCode` | 基金托管人 | number(10) | ✓ | 100.0% | 基金托管人代码（TrusteeCode）：与“基金托管人概况表（MF_TrusteeOutline）”中的“基金托管人名... |
| 50 | `Warrantor` | 保本担保机构 | varchar2(250) | ✓ | 0.69% |  |
| 51 | `RegInstCode` | 注册登记机构 | number(10) | ✓ | 100.0% | 注册登记机构（RegInstCode）：与“机构基本资料（LC_InstiArchive）”中“企业编号（Company... |
| 52 | `LowestSumSubscribing` | 最低认购申购金额描述 | varchar2(500) | ✓ | 98.24% |  |
| 53 | `LowestSumSubLL` | 最低认购金额下限(元) | number(19,4) | ✓ | 78.58% | 最低认购金额下限（元）（LowestSumSubLL）：取值为不同认购平台最低认购金额的最小值。 |
| 54 | `LowestSumPurLL` | 最低申购金额下限(元) | number(19,4) | ✓ | 92.68% | 最低申购金额下限（元）（LowestSumPurLL）：取值为不同申购平台最低申购金额的最小值。 |
| 55 | `LowestSumRedemption` | 最低赎回份额(份) | number(16,6) | ✓ | 91.87% |  |
| 56 | `LSFRDescription` | 最低赎回份额描述 | varchar2(200) | ✓ | 95.71% |  |
| 57 | `LowestSumForHolding` | 最低持有份额(份) | number(16,6) | ✓ | 87.8% |  |
| 58 | `LSFHDescription` | 最低持有份额描述 | varchar2(200) | ✓ | 91.47% |  |
| 59 | `LargeRedemptionRatio` | 巨额赎回认定比例 | number(19,6) | ✓ | 93.15% |  |
| 60 | `PRconfirmationdate` | 申赎确认日 | number(10) | ✓ | 98.11% | 申赎确认日(PRconfirmationdate)：该字段的数值含义指的是T+n，1代表T+1,2代表T+2，以此类推。... |
| 61 | `DeliveryDays` | 赎回款到账天数 | number(10) | ✓ | 99.01% | 赎回款到账天数(DeliveryDays)：指一般基金的赎回款到账日。针对ETF基金，维护现金差额交收日。 |
| 62 | `CustodyMarket` | 转托管市场 | number(10) | ✓ | 2.35% | 转托管市场(CustodyMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND... |
| 63 | `IfInitiatingFund` | 是否发起式基金 | number(10) | ✓ | 100.0% | 是否发起式基金(IfInitiatingFund)：1-否，2-是。 |
| 64 | `IfPensionTarget` | 是否养老目标基金 | number(10) | ✓ | 99.99% | 是否养老目标基金(IfPensionTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 99... |
| 65 | `IfFOF` | 是否FOF | number(10) | ✓ | 100.0% | 是否FOF(IfFOF)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN(1... |
| 66 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 67 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 68 | `JSID` | JSID | number(19) | ✗ |  |  |
| 69 | `ClassificationFundType` | 分级基金类别 | number(10) | ✓ | 0.0% |  |
| 70 | `RiskReturnCode` | 风险收益特征代码 | number(10) | ✓ | 1.43% | 风险收益特征代码(RiskReturnCode)与(CT_SystemConst)表中的DM字段关联，令LB = 165... |
| 71 | `OperationPeriod` | 运作期 | number(9,2) | ✓ | 0.0% |  |
| 72 | `OperationPDUnitCode` | 运作期单位代码 | number(10) | ✓ | 0.0% |  |
| 73 | `OperationPDUnitName` | 运作期单位名称 | varchar2(20) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### ApplyingCodeFront (前端申购代码)

前端申购代码（ApplyingCodeFront）：取值为场外前端申购代码>场内申赎代码（场内基金）。

### MainCode (基金主代码)

基金主代码（MainCode）：该字段记录基金季报中公布的基金主代码信息，当基金为非分级基金或分级基金主代码时，该字段与基金代码（SecurityCode）一致。

### ExApplyingMarket (场内申购赎回场所)

场内申购赎回场所(ExApplyingMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (90,83)，得到场内申购赎回场所的具体描述：83-上海证券交易所，90-深圳证券交易所。

### Type (基金运作方式)

基金运作方式(Type)与(CT_SystemConst)表中的DM字段关联，令LB = 1210 AND DM IN(1,2,3,4,6,7,8)，得到基金运作方式的具体描述：1-契约型封闭式，2-开放式，3-LOF，4-ETF，6-创新型封闭式，7-开放式(带固定封闭期)，8-ETF联接基金。

### FundNature (基金性质)

基金性质(FundNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1485，得到基金性质的具体描述：1-常规基金，2-QDII基金，3-互认基金。

### InvestmentType (是否指数型)

是否指数型(InvestmentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1094 AND DM IN (7,8,16)，得到是否指数型的具体描述：7-指数型，8-优化指数型，16-非指数型。

### InvestStyle (基金投资风格)

基金投资风格(InvestStyle)与(CT_SystemConst)表中的DM字段关联，令LB = 1093，得到基金投资风格的具体描述：1-普通股票型，2-指数型，3-配置型，4-货币市场，5-积极债券型，6-债券型，7-普通债券型，8-短债型，9-保本型，10-积极配置型，11-保守混合型，12-偏股型，13-偏债型，14-中短债型，15-特殊策略型，16-标准混合型，17-QDII，20-封闭式基金，21-大规模封闭式基金，22-小规模封闭式基金，23-普通股票型(封闭)，24-标准混合型基金(封闭)，25-积极债券型(封闭)，26-普通债券型基金(封闭)，27-积极配置型(封闭)，29-其它(封闭)，30-亚太区不包括日本股票，31-大中华区股票，32-新兴市场股票，33-环球股票，34-行业股票，35-美国股票，36-环球股债混合，37-环球债券，38-商品(QDII)，39-可转债型，40-纯债型，41-纯债型(封闭)，42-混合型，43-混合型(封闭)，44-可转债型(封闭)，45-债券型(封闭)，46-股票型(QDII)，47-混合型(QDII)，48-债券型(QDII)，49-保守混合型(封闭)，50-商品基金(QDII)，51-货币型，52-短债型(封闭)，53-市场中性策略，54-市场中性策略(封闭)，55-商品，56-另类，57-另类(封闭)，58-其它(QDII)，59-灵活配置型，60-灵活配置型(封闭)，61-亚洲股债混合，62-大中华区股债混合，63-全球新兴市场股债混合，64-行业股票-医药，65-行业股票-科技、传媒及通讯，66-沪港深股票型，67-沪港深混合型，68-沪港深混合型(封闭)，69-债券型QDII(封闭)，70-FOF，71-其他债券，72-亚洲不包括日本股票-货币对冲，73-中国股票，74-亚太区股票，75-环球债券(封闭)，76-亚洲债券，77-股票型基金，78-可转债基金，79-保本基金，80-商品基金，81-其它，82-其它基金(QDII)，83-债券型基金，84-香港股票型基金，85-行业股票-消费，86-行业股票-金融地产，87-行业混合-消费，88-行业混合-医药，89-行业混合-科技、传媒及通讯，90-沪港深积极配置型，91-沪港深保守混合型，92-沪港深灵活配置型，93-目标日期，94-商品-贵金属，95-商品-其它，96-沪港深积极配置型(封闭)，97-沪港深保守混合型(封闭)，98-沪港深灵活配置型(封闭)，99-其他型，100-环球债券 - 美元对冲，101-行业混合 - 科技、传媒及通讯（封闭式），102-美元积极型股债混合，103-科技股票，104-新兴市场债券，105-大中华股票，106-亚洲高收益债券，107-其他行业股票，108-大中华高收益债券，109-亚洲不包括日本股票，110-其他股债混合，111-美元灵活配置型，112-信用债(封闭)，113-信用债，114-行业股票-其它，115-行业混合-医药(封闭)，116-利率债，117-利率债(封闭)，118-香港股票型基金(封闭式)，119-大盘成长股票，120-大盘平衡股票，121-大盘价值股票，122-中盘成长股票，123-中盘平衡股票，124-积极配置-大盘成长，125-积极配置-大盘平衡，126-积极配置-中小盘，127-沪港深积极配置，128-港股积极配置，129-基础设施REITs（废弃），130-积极配置-大盘平衡(封闭式)，131-大盘平衡股票(封闭式)，132-大盘成长股票(封闭式)，133-积极配置-大盘成长(封闭式)，134-积极配置-中小盘(封闭式)，135-QDII环球股票，136-QDII环球债券，137-QDII行业股票，138-QDII美国股票，139-QDII大中华区股票，140-QDII全球新兴市场股债混合，141-QDII亚洲股债混合，142-QDII新兴市场股票，143-环球新兴市场债券，144-美元激进配置型，145-QDII环球股债混合，146-QDII大中华区股债混合，147-QDII亚太区不包括日本股票，148-QDII环球债券(封闭式)，149-QDII其它，150-QDII商品，151-沪港深股票(封闭)，152-基础设施REITs(封闭)，155-行业混合-消费(封闭式)。

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1249 AND DM NOT IN (1110,1111,1112)，得到基金类别代码的具体描述：1101-股票型，1103-混合型，1105-债券型，1107-保本型，1109-货币型，1199-其他型，1200-基础设施证券投资基金。

## SQL示例

```sql
-- 查询 公募基金概况 数据
SELECT *
FROM mf_fundarchives
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
