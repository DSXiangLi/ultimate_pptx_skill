# Bond_IssueNew

**中文名**: 债券发行上市与增发

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IssueNew` |
| MySQL表名 | `bond_issuenew` |
| 中文名 | 债券发行上市与增发 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 74 |
| 版本 | 1.01 |

## 表描述

1.收录债券（可转换债券除外）首次发行、增发的基本信息、发行规模、认购单位和数量等信息。
2.数据范围：1981-01-01 至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 主内部编码 | number(10) | ✗ | 100.0% | 债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `CrossExchange` | 是否跨市场 | number(10) | ✓ | 100.0% | 是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 4 | `BondNature` | 债券性质 | number(10) | ✓ | 100.0% | 债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券性质... |
| 5 | `Issuer` | 发行人 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `IssuerNature` | 发行人性质 | number(10) | ✓ | 100.0% | 发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND... |
| 7 | `IssueType` | 发行类型 | number(10) | ✓ | 100.0% | 发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1172 AND DM ... |
| 8 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 9 | `AdvanceDate` | 预案公告日期 | date | ✓ | 3.91% |  |
| 10 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 3.69% |  |
| 11 | `AdvanceValidStartDate` | 预案有效期起始日 | date | ✓ | 2.13% |  |
| 12 | `AdvanceValidEndDate` | 预案有效期截止日 | date | ✓ | 1.48% |  |
| 13 | `PublicAnnouncementDate` | 发行公告发布日期 | date | ✗ | 100.0% |  |
| 14 | `BidStartDate` | 招标日/薄记建档日起始日 | date | ✓ | 36.32% |  |
| 15 | `BidEndDate` | 招标日/薄记建档日截止日 | date | ✓ | 36.35% |  |
| 16 | `IssueDateStart` | 发行日期起始日 | date | ✓ | 78.57% |  |
| 17 | `IssueDateEnd` | 发行日期截止日 | date | ✓ | 78.57% |  |
| 18 | `IssueStartDateOnline` | 网上发行日期起始日 | date | ✓ | 0.14% |  |
| 19 | `IssueEndDateOnline` | 网上发行日期截止日 | date | ✓ | 0.14% |  |
| 20 | `IssueStartDateOffline` | 网下发行日期起始日 | date | ✓ | 12.45% |  |
| 21 | `IssueEndDateOffline` | 网下发行日期截止日 | date | ✓ | 12.45% |  |
| 22 | `DistributeStartDate` | 分销起始日 | date | ✓ | 10.59% |  |
| 23 | `DistributeEndDate` | 分销截止日 | date | ✓ | 10.59% |  |
| 24 | `TransferStartDate` | 划款起始日 | date | ✓ | 83.67% |  |
| 25 | `TransferEndDate` | 划款截止日 | date | ✓ | 83.67% |  |
| 26 | `ConStartDateOnline` | 网上缴款日起始日 | date | ✓ | 0.13% |  |
| 27 | `ConEndDateOnline` | 网上缴款日截止日 | date | ✓ | 0.13% |  |
| 28 | `ConStartDateOffline` | 网下缴款日起始日 | date | ✓ | 12.23% |  |
| 29 | `ConEndDateOffline` | 网下缴款日截止日 | date | ✓ | 12.23% |  |
| 30 | `TradesInCirclePubDate` | 交易流通公告发布日期 | date | ✓ | 77.49% |  |
| 31 | `RegDate` | 债权债务登记日 | date | ✓ | 76.8% |  |
| 32 | `ListAnnouncePubDate` | 上市公告书发布日期 | date | ✓ | 3.85% |  |
| 33 | `ListedDateInBank` | (银行间)上市日期 | date | ✓ | 78.13% |  |
| 34 | `ListedDateInExchange` | (交易所)上市日期 | date | ✓ | 17.85% |  |
| 35 | `BidTarget` | 招标标的 | number(10) | ✓ | 36.57% | 招标标的(BidTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 1171 and DM ... |
| 36 | `BidType` | 招标方式 | number(10) | ✓ |  |  |
| 37 | `IssueMethod` | 发行/分销方式 | number(10) | ✓ |  |  |
| 38 | `UnderwritingMethod` | 承销方式 | number(10) | ✓ | 30.16% | 承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 101... |
| 39 | `ParValue` | 债券面值(元) | number(19,4) | ✓ | 99.72% |  |
| 40 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 99.92% |  |
| 41 | `IssueCommissionRate` | 发行手续费 | number(19,4) | ✓ | 5.38% |  |
| 42 | `CommissionRate` | 兑付手续费 | number(19,4) | ✓ | 0.23% |  |
| 43 | `IssueObjectInBank` | (银行间)发行对象(文字) | varchar2(200) | ✓ | 27.49% |  |
| 44 | `IssueObjectInExchange` | (交易所)发行对象(文字) | varchar2(200) | ✓ | 16.07% |  |
| 45 | `ApplyCodeOnline` | 网上认购代码 | varchar2(10) | ✓ | 0.14% |  |
| 46 | `ApplyAbbrOnline` | 网上认购简称 | varchar2(50) | ✓ | 0.11% |  |
| 47 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM i... |
| 48 | `PlanIssueSize` | 计划发行总额(百万元) | number(19,8) | ✓ | 99.99% |  |
| 49 | `PlanIssueAddSize` | 其中:计划追加发行(百万元) | number(19,8) | ✓ | 2.63% |  |
| 50 | `PlanIssueSizeInBank` | 其中:银行间计划发行(百万元) | number(19,8) | ✓ | 0.06% |  |
| 51 | `PlanIssueSizeInExchange` | 其中:交易所计划发行(亿元) | number(19,8) | ✓ | 0.06% |  |
| 52 | `PlanIssueSizeOnline` | 交易所其中:网上计划发行(百万元) | number(19,8) | ✓ | 0.13% |  |
| 53 | `planIssueSizeOffline` | 交易所其中:网下计划发行(百万元) | number(19,8) | ✓ | 3.27% |  |
| 54 | `ActualIssueSize` | 实际发行总额(百万元) | number(19,8) | ✓ | 95.44% |  |
| 55 | `ActualAddIssueSize` | 其中:实际追加发行(百万元) | number(19,8) | ✓ | 2.59% |  |
| 56 | `ApplyUnit` | 认购单位(元) | number(19,4) | ✓ | 4.85% |  |
| 57 | `ApplyMax` | 认购数量上限(元) | number(19,4) | ✓ | 1.63% |  |
| 58 | `ApplyMin` | 认购数量下限(元) | number(19,4) | ✓ | 4.1% |  |
| 59 | `ApplyUnitOnline` | 网上认购单位(元) | number(19,4) | ✓ | 0.13% |  |
| 60 | `ApplyMaxOnline` | 网上认购数量上限(元) | number(19,4) | ✓ | 0.01% |  |
| 61 | `ApplyMinOnline` | 网上认购数量下限(元) | number(19,4) | ✓ | 0.11% |  |
| 62 | `ApplyUnitOffline` | 网下认购单位(元) | number(19,4) | ✓ | 8.94% |  |
| 63 | `ApplyMaxOffline` | 网下认购数量上限(元) | number(19,4) | ✓ | 6.7% |  |
| 64 | `ApplyMinOffline` | 网下认购数量下限(元) | number(19,4) | ✓ | 9.28% |  |
| 65 | `CompanyCode` | 企业编号 | number(10) | ✓ |  |  |
| 66 | `InnerCode` | 债券内码 | number(10) | ✓ |  |  |
| 67 | `ProjectChangingDes` | 方案变动说明 | varchar2(250) | ✓ | 2.28% |  |
| 68 | `ProjectChangingType` | 方案变动类型 | number(10) | ✓ | 7.63% | 方案变动类型(ProjectChangingType)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 69 | `RepalcementCode` | 被置换债券代码 | number(10) | ✓ | 0.0% | 与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到被置换债券的交易代码、债券... |
| 70 | `RepalcementPrice` | 被置换债券价格 | number(19,4) | ✓ | 0.0% |  |
| 71 | `IssueCodeAdd` | 增发代码 | number(10) | ✓ | 0.02% | 与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到增发债券的交易代码、债券简称等。 |
| 72 | `Remark` | 备注说明 | varchar2(2000) | ✓ | 0.08% |  |
| 73 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 74 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (主内部编码)

债券统一代码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### CrossExchange (是否跨市场)

是否跨市场(CrossExchange)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否跨市场的具体描述：1-是，2-否。

### BondNature (债券性质)

债券性质(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1243，得到债券性质的具体描述：1-企业债券，2-金融债券，3-金融次级债，4-国债现货，5-央行票据，6-短期融资券，7-MBS(房贷支持)，8-ABS(其他支持)，9-混合资本债券，10-可转换债券，11-国库现金管理，12-资产证券化，13-公司债券，14-中期票据，15-转债分离公司债，16-地方政府债券，17-中小企业集合票据，18-集合债券，19-超短期融资券，20-非公开定向债务融资工具，21-次级定期债务，22-中小企业区域集优票据，23-政府支持债券，24-中小企业私募债券，25-资产支持票据，26-小微企业扶持债券，27-二级资本债券，28-中小企业可交换私募债，29-可交换公司债券，30-同业存单，31-区域集优中期票据，32-项目收益票据，33-项目收益债券，34-证券公司短期公司债券，35-保险公司资本补充债券，36-非公开发行公司债，37-信用风险缓释凭证，38-信用联结票据，39-其他一级资本工具，40-标准化票据，41-自贸区债，42-TLAC非资本债券，99-其他。

### IssuerNature (发行人性质)

发行人性质(IssuerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1414 AND DM NOT IN (21)，得到发行人性质的具体描述：10-中央银行，11-政策性银行，13-商业银行，20-财政部，22-地方财政，29-其他部委，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，70-国际机构，75-自然人，80-外国主权政府，81-外国地方政府，91-建设基金，99-一般企业，100-地方融资平台。

### IssueType (发行类型)

发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1172 AND DM NOT IN (1001)，得到发行类型的具体描述：1-一次发行，2-二次发行，3-三次发行，4-四次发行，5-五次发行，6-六次发行，7-七次发行，8-八次发行，9-九次发行，10-十次发行，11-十一次发行，12-十二次发行，13-十三次发行，14-十四次发行，15-十五次发行，16-十六次发行，17-十七次发行，18-十八次发行，19-十九次发行，20-二十次发行，21-二十一次发行，22-二十二次发行，23-二十三发行，24-二十四次发行，25-二十五次发行，26-二十六次发行，27-二十七次发行，28-二十八次发行，29-二十九次发行，30-三十次发行，31-三十一次发行，32-三十二次发行，33-三十三次发行，34-三十四次发行，35-三十五次发行，36-三十六次发行，37-三十七次发行，38-三十八次发行，39-三十九次发行，40-四十次发行，41-四十一次发行，42-四十二次发行，43-四十三次发行，44-四十四次发行，45-四十五次发行，46-四十六次发行，47-四十七次发行，48-四十八次发行，49-四十九次发行，50-五十次发行，901-一次发行(超额)。

### BidTarget (招标标的)

招标标的(BidTarget)与(CT_SystemConst)表中的DM字段关联，令LB = 1171 and DM in (3,4,5,6)，得到招标标的的具体描述：3-价格招标，4-利率招标，5-利差招标，6-数量招标。

### UnderwritingMethod (承销方式)

承销方式(UnderwritingMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1420,9990)，得到货币单位的具体描述：1000-美元，1420-人民币元，9990-特别提款权。

### ProjectChangingType (方案变动类型)

方案变动类型(ProjectChangingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 and DM IN (3,4,5,11,12,13,14,15,17,18,19)，得到方案变动类型的具体描述：3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，17-重新发行，18-未发行，19-宣布发行不成功。

### RepalcementCode (被置换债券代码)

与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到被置换债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 债券发行上市与增发 数据
SELECT *
FROM bond_issuenew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
