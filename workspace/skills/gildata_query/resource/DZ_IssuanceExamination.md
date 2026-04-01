# DZ_IssuanceExamination

**中文名**: 发行审核表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_IssuanceExamination` |
| MySQL表名 | `dz_issuanceexamination` |
| 中文名 | 发行审核表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 64 |
| 版本 | 1.06 |

## 表描述

1.内容说明：收录股票发行审核委员会、科创板上市委历年来对各拟发行人的审核情况，包括审核会议召开日期、参会委员、是否通过等信息。
2.数据范围：2003-12-26至今
3.信息来源：中国证监会、临时公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 91.63% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 99.99% |  |
| 5 | `Issuer` | 发行人 | varchar2(200) | ✗ | 100.0% |  |
| 6 | `RegAddr` | 注册地址 | varchar2(200) | ✓ | 40.68% |  |
| 7 | `Province` | 所在省市 | varchar2(20) | ✓ | 40.66% |  |
| 8 | `ProvinceCode` | 省市代码 | number(10) | ✓ | 40.66% | 省市代码(ProvinceCode)：可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；也... |
| 9 | `BusinessMajor` | 主营产品及业务 | varchar2(1000) | ✓ | 39.33% |  |
| 10 | `IndustryStd` | 行业分类标准 | number(10) | ✓ | 39.26% | 行业分类标准（IndustryStd），当为1时，代表CSRC行业分类；当为22时，代表证监会行业分类2012版。 |
| 11 | `CSRCIndustryNum` | 行业类别 | number(10) | ✓ | 37.1% | 证监会行业类别(CSRCIndustryNum)：与“行业类别表（CT_IndustryType）”中的“行业内部编码（... |
| 12 | `CSRCIndustryCode` | 行业代码 | varchar2(10) | ✓ | 36.88% |  |
| 13 | `Committee` | 委员会 | varchar2(50) | ✓ | 97.84% |  |
| 14 | `CommitteeCode` | 委员会代码 | number(10) | ✓ | 97.84% | 委员会代码(CommitteeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1553，得到... |
| 15 | `MeetingNumber` | 会议列次 | number(10) | ✗ | 100.0% |  |
| 16 | `ExaminationMeetingDate` | 审核会议召开日 | date | ✓ | 98.33% |  |
| 17 | `PresentCommitteeman` | 参会委员 | varchar2(500) | ✓ | 67.15% |  |
| 18 | `PresentCommitteCode` | 参会委员代码 | number(10) | ✓ |  |  |
| 19 | `ResultPublDate` | 审核结果公告日 | date | ✓ | 99.9% |  |
| 20 | `IfPassed` | 审核是否通过 | number(10) | ✓ | 99.9% | 审核是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 21 | `RegiResultPublDate` | 注册结果公告日 | date | ✓ | 16.64% |  |
| 22 | `RegisterIfPassed` | 注册是否通过 | number(10) | ✓ | 16.64% | 注册是否通过(RegisterIfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 169... |
| 23 | `PrecontractedDisclosureD` | 发行申报稿预披露日 | date | ✓ | 40.62% |  |
| 24 | `MeetingDraftADD` | 上会稿预披露日 | date | ✓ | 14.74% |  |
| 25 | `RegisterDraftADD` | 注册稿预披露日 | date | ✓ | 12.61% |  |
| 26 | `InnerCode` | 股票代码 | number(10) | ✗ | 100.0% | 股票代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 27 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 28 | `RaisingMethod` | 募资方式 | varchar2(50) | ✓ | 100.0% |  |
| 29 | `RaisingMethodCode` | 募资方式代码 | number(10) | ✓ | 100.0% | 募资方式代码(RaisingMethodCode)与(CT_SystemConst)表中的DM字段关联，令LB = 10... |
| 30 | `SecuCategory` | 证券类别 | varchar2(20) | ✓ | 100.0% |  |
| 31 | `SecuCategoryCode` | 证券类别代码 | number(10) | ✓ | 100.0% | 证券类别代码(SecuCategoryCode)与(CT_SystemConst)表中的DM字段关联，令LB = 117... |
| 32 | `IssueShares` | 发行股数(万股/万份) | number(18,4) | ✓ | 44.17% |  |
| 33 | `NewSharesVol` | 其中:新股发行数量(万股/万份) | number(18,4) | ✓ | 21.17% |  |
| 34 | `ListStandard` | 上市标准 | number(10) | ✓ | 14.75% | 上市标准(ListStandard)与(CT_SystemConst)表中的DM字段关联，令LB = 2206，得到上市... |
| 35 | `ParValue` | 每股面值 | number(25,10) | ✓ | 39.49% |  |
| 36 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 39.49% | 每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 37 | `PlannedProceeds` | 拟募集资金金额(万元) | number(19,4) | ✓ | 38.92% |  |
| 38 | `TotalSharesBefore` | 发行前总股本(万股/万份) | number(18,4) | ✓ | 40.47% |  |
| 39 | `TotalSharesAfter` | 发行后总股本(万股/万份) | number(18,4) | ✓ | 40.31% |  |
| 40 | `PreparedListExchange` | 拟上市地 | varchar2(20) | ✓ | 40.21% |  |
| 41 | `ListExchangeCode` | 拟上市地代码 | number(10) | ✓ | 40.21% | 拟上市地代码(ListExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 201... |
| 42 | `Sponsor` | 保荐机构 | varchar2(600) | ✓ | 40.66% |  |
| 43 | `SponsorCode` | 保荐机构代码 | number(10) | ✓ |  |  |
| 44 | `EventDesc` | 事件描述 | varchar2(200) | ✓ | 99.21% |  |
| 45 | `CommitteeFeedback` | 委员会意见 | clob | ✓ | 57.04% |  |
| 46 | `IfImplemented` | 是否实施 | number(10) | ✓ | 100.0% | 是否实施(IfImplemented)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND ... |
| 47 | `Remark` | 备注说明 | clob | ✓ | 23.75% |  |
| 48 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 49 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 50 | `JSID` | JSID | number(19) | ✗ |  |  |
| 51 | `IssuePrice` | 发行价格(元/股) | number(19,4) | ✓ | 0.75% |  |
| 52 | `OriginalSharesVol` | 其中:股东公开发售股份数量(万股/万份) | number(18,4) | ✓ | 0.02% |  |
| 53 | `StrategicSharesVol` | 战略配售数量(万股/万份) | number(18,4) | ✓ | 0.0% |  |
| 54 | `CoreStaffsStraSHVol` | 其中:高管、员工参与战略配售数量(万股/万份) | number(18,4) | ✓ | 0.0% |  |
| 55 | `CoreStaffsStraSHVal` | 其中:高管、员工参与战略配售股份金额(万元) | number(19,4) | ✓ | 0.0% |  |
| 56 | `CoreStaffsStraSHRat` | 其中:高管、员工参与战略配售占比(%) | number(9,4) | ✓ | 0.05% |  |
| 57 | `SponsorStraSharesVol` | 其中:保荐机构及相关子公司参与战略配售数量(万股/万份) | number(18,4) | ✓ | 0.0% |  |
| 58 | `SponsorStraSharesHVal` | 其中:保荐机构及相关子公司参与战略配售股份金额(万元) | number(19,4) | ✓ | 0.0% |  |
| 59 | `SponsorStraSharesRat` | 其中:保荐机构及相关子公司参与战略配售占比(%) | number(9,4) | ✓ | 0.01% |  |
| 60 | `OtherStraSHVol` | 其中:其他参与战略配售计划数量(万股/万份) | number(18,4) | ✓ | 0.0% |  |
| 61 | `OtherStraSHVal` | 其中:其他参与战略配售计划金额(万元) | number(19,4) | ✓ | 0.01% |  |
| 62 | `OtherStraSHRat` | 其中:其他计划参与战略配售占比(%) | number(9,4) | ✓ | 0.0% |  |
| 63 | `FinancialAdviser` | 财务顾问 | varchar2(200) | ✓ | 1.31% |  |
| 64 | `FinancialAdviserCode` | 财务顾问代码 | number(10) | ✓ |  |  |

## 字段说明

### ProvinceCode (省市代码)

省市代码(ProvinceCode)：可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；也可关联国家城市代码表的“地区行政编码（AreaCode）”关联，得到地区代码的具体描述

### IndustryStd (行业分类标准)

行业分类标准（IndustryStd），当为1时，代表CSRC行业分类；当为22时，代表证监会行业分类2012版。

### CSRCIndustryNum (行业类别)

证监会行业类别(CSRCIndustryNum)：与“行业类别表（CT_IndustryType）”中的“行业内部编码（IndustryNum）”关联，且限定本表的行业分类标准(IndustryStd)=关联表的行业分类标准(Standard)，可得到行业代码及行业名称。

### CommitteeCode (委员会代码)

委员会代码(CommitteeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1553，得到委员会代码的具体描述：1001-证监会发审委，1002-证监会并购重组委，1003-证监会创业板发审委，2001-科创板上市委，2002-科创板并购重组委，2003-上海证券交易所上市审核委，2004-上海证券交易所并购重组委，3001-创业板上市委，3002-创业板并购重组委，3003-深圳证券交易所上市审核委，3004-深圳证券交易所并购重组委，4001-全国股转系统挂牌委，5001-北交所上市委，5002-北交所并购重组委。

### IfPassed (审核是否通过)

审核是否通过(IfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2,10,11,12)，得到审核是否通过的具体描述：1-是，2-否，10-暂缓，11-有条件通过，12-取消。

### RegisterIfPassed (注册是否通过)

注册是否通过(RegisterIfPassed)与(CT_SystemConst)表中的DM字段关联，令LB = 1691 AND DM IN (17,18,24)，得到注册是否通过的具体描述：17-注册生效，18-不予注册，24-终止注册。

### InnerCode (股票代码)

股票代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### RaisingMethodCode (募资方式代码)

募资方式代码(RaisingMethodCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1021，得到募资方式代码的具体描述：1-新股发行，2-历史遗留，3-增发新股，4-配股，5-发行可转换债券，6-发行企业债券，7-募资改投，8-非募集资金，9-发行权证，10-吸收合并，11-发行分离可转债，12-发行金融债，13-老股转让，14-老股转让+新股发行，15-CDR首发，16-CDR增发，17-CDR配股，19-转科创板上市，20-转中小板上市，21-转主板上市，22-转创业板上市，23-并购重组，31-预先披露，32-优先股发行，33-地方政府债发行，34-后续发行，99-其他。

### SecuCategoryCode (证券类别代码)

证券类别代码(SecuCategoryCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 ，得到证券类别代码的具体描述：1-A股，2-B股，3-H股，4-大盘，5-国债回购，6-国债现货，7-金融债券，8-开放式基金，9-可转换债券，10-其他，11-企业债券，12-企业债券回购，13-投资基金，14-央行票据，15-深市代理沪市股票，16-沪市代理深市股票，17-资产支持证券，18-资产证券化产品，19-买断式回购，20-衍生权证，21-股本权证，22-股指期货，23-商业银行定期存款，24-其他股票，25-牛熊证，26-收益增长线，27-新质押式回购，28-地方政府债，29-可交换公司债，30-拆借，31-信用风险缓释工具，32-浮息债计息基准利率，33-定期存款凭证，34-个股期权，35-大额存款凭证，36-债券借贷，37-存款类机构质押式回购，38-存款类机构信用拆借，39-现货，40-货币对，41-中国存托凭证，42-协议回购，43-三方回购，44-利率互换品种，45-标准利率互换合约，46-报价回购，47-标准化票据，51-港股，52-合订证券，53-红筹股，55-优先股，60-基金，61-信托基金，62-ETF基金，63-参与证书，64-杠杆及反向产品，65-债务证券，66-基金票据，68-界内证，69-美国证券(交易试验计划)，71-普通预托证券，72-优先预托证券，73-股票，74-普通股，75-美国存托凭证（ADR），76-国债期货，77-商品期货，78-临时证券(Temporary)，79-深市代理港交所股票，80-沪市代理港交所股票，81-SPAC股份，82-SPAC权证，101-全球存托凭证(GDR)，201-其他存托凭证(DR)，202-无投票权的存托凭证(NVDR)，203-具有权益特征的证券(Preferred Equity)，204-权利(Right)，205-结构性产品(Structured Products)，206-单位证券(Unit)，207-权证(Warrant)，208-外国证券(Alien/Foreign)，209-美元债，210-特定授权指数，211-自贸区债。

## SQL示例

```sql
-- 查询 发行审核表 数据
SELECT *
FROM dz_issuanceexamination
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
