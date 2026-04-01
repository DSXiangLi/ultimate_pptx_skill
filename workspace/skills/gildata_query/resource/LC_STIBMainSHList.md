# LC_STIBMainSHList

**中文名**: 科创板股东名单

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBMainSHList` |
| MySQL表名 | `lc_stibmainshlist` |
| 中文名 | 科创板股东名单 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 50 |
| 版本 | 1.05 |

## 表描述

1.内容说明：收录科创板A股发行人的主要股东构成及持股数量比例、持股性质等明细资料，包括发行前和上市后的历次变动记录。
2.数据范围：2019至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `InfoTypeCode` | 信息类别编码 | number(10) | ✗ | 100.0% | 信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AN... |
| 7 | `SHSN` | 股东序号 | number(10) | ✗ | 100.0% |  |
| 8 | `SHID` | 股东ID | number(10) | ✓ | 64.86% | 股东ID（SHID）：当股东属性（SHAttribute）=2时，与企业码表（EP_CompanyMain）中的企业编号... |
| 9 | `SHName` | 股东名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `SHAttribute` | 股东属性 | number(10) | ✓ | 100.0% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属... |
| 11 | `SHKindCode` | 股东性质编码 | number(10) | ✓ |  | 股东性质编码(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026  AND... |
| 12 | `SHKind` | 股东性质 | varchar2(50) | ✓ | 100.0% |  |
| 13 | `HoldSum` | 持股数(股) | number(16,0) | ✓ | 100.0% |  |
| 14 | `RestrainedTShare` | 其中:有限售股数(股) | number(16,0) | ✓ | 41.06% |  |
| 15 | `UnstintedTShare` | 其中:无限售股数(股) | number(16,0) | ✓ | 66.44% |  |
| 16 | `RefinanceLoanShare` | 包含转融通借出股份的限售股数(股) | number(16,0) | ✓ | 24.75% |  |
| 17 | `ShareCharacterStatement` | 股本性质描述 | varchar2(50) | ✓ | 98.62% |  |
| 18 | `HoldChangeType` | 持股变动类型 | number(10) | ✓ | 100.0% | 持股变动类型(HoldChangeType)的具体描述：1-不变；2-增加；3-减少；4-新进  |
| 19 | `HoldSumChange` | 持股数量增减(股) | number(16,0) | ✓ | 71.9% |  |
| 20 | `HoldSumChangeRate` | 持股比例增减幅度(%) | number(19,10) | ✓ | 71.88% |  |
| 21 | `PCTOfTotalShares` | 占总股本比例(%) | number(10,6) | ✓ | 99.96% |  |
| 22 | `PCTOfAFloatShares` | 占流通A股比例(%) | number(10,6) | ✓ | 63.79% | 占流通A股比例（%）（PCTOfFloatShares） = 无限售流通A股/已上市无限售人民币普通股 * 100 |
| 23 | `PCTOfNRShares` | 占无限售股份比例(%) | number(10,6) | ✓ | 63.09% | 占无限售股份比例（%）（PCTOfNRShares） = 无限售条件股数/已上市无限售条件股份 * 100 |
| 24 | `HoldAShareSum` | 持有A股数量(股) | number(16,0) | ✓ | 77.6% |  |
| 25 | `RestrainedAShare` | 其中:有限售A股数(股) | number(16,0) | ✓ | 41.4% |  |
| 26 | `UnstintedAShare` | 其中:无限售A股数(股) | number(16,0) | ✓ | 66.65% |  |
| 27 | `HoldHShareSum` | 持有H股数量(股) | number(16,0) | ✓ | 18.47% |  |
| 28 | `HoldOthterShareSum` | 持有其他股数量(股) | number(16,0) | ✓ | 38.97% |  |
| 29 | `HoldShareASum` | 持有A类普通股数量(股) | number(16,0) | ✓ | 18.37% |  |
| 30 | `RestrainedShareA` | 其中:有限售A类普通股数量(股) | number(16,0) | ✓ | 9.69% |  |
| 31 | `UnstintedShareA` | 其中:无限售A类普通股数量(股) | number(16,0) | ✓ | 16.87% |  |
| 32 | `HoldShareBSum` | 持有B类普通股数量(股) | number(16,0) | ✓ | 19.02% |  |
| 33 | `RestrainedShareB` | 其中:有限售B类普通股数量(股) | number(16,0) | ✓ | 9.95% |  |
| 34 | `UnstintedShareB` | 其中:无限售B类普通股数量(股) | number(16,0) | ✓ | 17.28% |  |
| 35 | `HoldShareCSum` | 持有C类普通股数量(股) | number(16,0) | ✓ | 18.18% |  |
| 36 | `HoldShareDSum` | 持有D类普通股数量(股) | number(16,0) | ✓ | 18.18% |  |
| 37 | `HoldOthterComShareSum` | 持有其他类普通股数量(股) | number(16,0) | ✓ | 18.42% |  |
| 38 | `PrefShareWithVotRight` | 有投票权的优先股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 39 | `VotingRightsVol` | 表决权总数(股) | number(16,0) | ✓ | 1.34% |  |
| 40 | `VotingRightsRatio` | 表决权比例 | number(10,6) | ✓ | 1.34% |  |
| 41 | `SpecialVotingRightsVol` | 特别表决权股份数量(股) | number(16,0) | ✓ | 1.16% |  |
| 42 | `PledgeInvolvedSum` | 股权质押涉及股数(股) | number(16,0) | ✓ | 18.5% |  |
| 43 | `FreezeInvolvedSum` | 股权冻结涉及股数(股) | number(16,0) | ✓ | 18.29% |  |
| 44 | `PFStatement` | 股权质押冻结情况说明 | varchar2(200) | ✓ | 0.0% |  |
| 45 | `ConnectionRelation` | 股东关联关系 | varchar2(50) | ✓ | 11.52% |  |
| 46 | `ConnectionStatement` | 与其他股东关联关系说明 | varchar2(2000) | ✓ | 11.52% |  |
| 47 | `ActInConcertStatement` | 与其他股东同属一致行动人说明 | varchar2(2000) | ✓ | 8.89% |  |
| 48 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 49 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 50 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到科创板A股发行人的交易代码、简称等。

### InfoTypeCode (信息类别编码)

信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM IN (1,2,4,5,6,7)，得到信息类别编码的具体描述：1-前十大股东，2-前十流通股东，4-十大有限售条件股东，5-发行前股东，6-前十大表决权数量股东，7-5%以上股东持股变动。

### SHID (股东ID)

股东ID（SHID）：当股东属性（SHAttribute）=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与证券码表总表
（SecuMainAll）中的证券内部编码（InnerCode）关联。

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHKindCode (股东性质编码)

股东性质编码(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026  AND DM NOT IN (13,16,40,50,60,61,67)，得到股东性质编码的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，14-职工工会，15-财务公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，64-保险投资组合，66-保险资管产品，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### HoldChangeType (持股变动类型)

持股变动类型(HoldChangeType)的具体描述：1-不变；2-增加；3-减少；4-新进


### PCTOfAFloatShares (占流通A股比例(%))

占流通A股比例（%）（PCTOfFloatShares） = 无限售流通A股/已上市无限售人民币普通股 * 100

### PCTOfNRShares (占无限售股份比例(%))

占无限售股份比例（%）（PCTOfNRShares） = 无限售条件股数/已上市无限售条件股份 * 100

## SQL示例

```sql
-- 查询 科创板股东名单 数据
SELECT *
FROM lc_stibmainshlist
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
