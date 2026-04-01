# LC_MainSHListNew

**中文名**: 股东名单(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_MainSHListNew` |
| MySQL表名 | `lc_mainshlistnew` |
| 中文名 | 股东名单(新) |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 60 |
| 版本 | 1.07 |

## 表描述

1.收录公司主要股东构成及持股数量比例、持股性质等明细资料，包括发行前和上市后的历次变动记录。
2.数据范围：1992-06-30至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 97.87% |  |
| 6 | `InfoTypeCode` | 信息类别编码 | number(3) | ✗ | 100.0% | 信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AN... |
| 7 | `SHNo` | 股东排名 | number(10) | ✗ | 100.0% | 股东排名（SHNo）：当“信息类别代码（InfoTypeCode）”=1时，“股东排名（SHNo）”表示股东排名；当“信... |
| 8 | `SHSerial` | 股东序号 | number(10) | ✗ | 100.0% |  |
| 9 | `GDID` | 股东ID | number(10) | ✓ | 52.59% | 股东ID（GDID）：当股东属性（SHAttribute）=2时，与企业码表（EP_CompanyMain）中的企业编号... |
| 10 | `SHList` | 股东名称 | varchar2(200) | ✓ | 100.0% | 股东名称（SHList）：此字段为股东名称公告原始披露值；如期望获取股东标准名称，可使用股东ID与相关表单关联，具体关联... |
| 11 | `SHAttribute` | 股东属性 | number(10) | ✓ | 100.0% | 股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属... |
| 12 | `SHKindCode` | 股东性质编码 | number(10) | ✓ | 100.0% | 股东性质编码(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026 AND ... |
| 13 | `SHKind` | 股东性质 | varchar2(50) | ✓ | 100.0% |  |
| 14 | `SHTypeCode` | 股东类别编码 | number(10) | ✓ | 65.34% | 股东类别编码(SHTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得到股东... |
| 15 | `SHType` | 股东类别 | varchar2(50) | ✓ | 65.34% |  |
| 16 | `HoldSum` | 持股数(股) | number(16,0) | ✓ | 100.0% | 持股数（股）（HoldSum）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)=总股本当“信息类别代... |
| 17 | `RestrainedTShare` | 其中:有限售股数(股) | number(16,0) | ✓ | 38.78% |  |
| 18 | `UnstintedTShare` | 其中:无限售股数(股) | number(16,0) | ✓ | 87.63% |  |
| 19 | `RefinanceLoanShare` | 包含转融通借出股份的限售股数(股) | number(16,0) | ✓ | 0.0% |  |
| 20 | `ShareCharacterStatement` | 股本性质描述 | varchar2(50) | ✓ | 98.21% |  |
| 21 | `HoldChangeType` | 持股变动类型 | number(10) | ✓ | 100.0% | 持股变动类型(HoldChangeType)的具体描述：1-不变；2-增加；3-减少；4-新进 |
| 22 | `HoldSumChange` | 持股数量增减(股) | number(16,0) | ✓ | 71.08% |  |
| 23 | `HoldSumChangeRate` | 持股比例增减幅度(%) | number(16,6) | ✓ | 71.08% |  |
| 24 | `PCTOfTotalShares` | 占总股本比例(%) | number(10,6) | ✓ | 100.0% | 占总股本比例（%）（PCTOfTotalShares）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股... |
| 25 | `PCTOfFloatShares` | 占流通A股比例(%) | number(10,6) | ✓ | 85.03% | 占流通A股比例（%）（PCTOfFloatShares） = 无限售流通A股/已上市无限售人民币普通股 * 100 |
| 26 | `PCTOfNRShares` | 占无限售股份比例(%) | number(10,6) | ✓ | 86.87% | 占无限售股份比例（%）（PCTOfNRShares） = 无限售条件股数/已上市无限售条件股份 * 100  |
| 27 | `HoldAShareSum` | 持有A股数量(股) | number(16,0) | ✓ | 90.3% |  |
| 28 | `RestrainedAShare` | 其中:有限售A股数(股) | number(16,0) | ✓ | 38.12% |  |
| 29 | `UnstintedAShare` | 其中:无限售A股数(股) | number(16,0) | ✓ | 85.59% |  |
| 30 | `HoldBShareSum` | 持有B股数量(股) | number(16,0) | ✓ | 1.47% |  |
| 31 | `HoldHShareSum` | 持有H股数量(股) | number(16,0) | ✓ | 0.45% |  |
| 32 | `HoldOthterShareSum` | 持有其他股数量(股) | number(16,0) | ✓ | 6.12% |  |
| 33 | `HoldShareASum` | 持有A类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 34 | `RestrainedShareA` | 其中:有限售A类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 35 | `UnstintedShareA` | 其中:无限售A类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 36 | `HoldShareBSum` | 持有B类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 37 | `RestrainedShareB` | 其中:有限售B类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 38 | `UnstintedShareB` | 其中:无限售B类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 39 | `HoldShareCSum` | 持有C类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 40 | `HoldShareDSum` | 持有D类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 41 | `HoldOtherComShareSum` | 持有其他类普通股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 42 | `PrefShareWithVotRight` | 有投票权的优先股数量(股) | number(16,0) | ✓ | 0.0% |  |
| 43 | `VotingRightsVol` | 表决权总数(股) | number(16,0) | ✓ | 0.0% |  |
| 44 | `VotingRightsRatio` | 表决权比例 | number(10,6) | ✓ | 0.0% |  |
| 45 | `SpecialVotingRightsVol` | 特别表决权数量(股) | number(16,0) | ✓ | 0.0% |  |
| 46 | `PledgeInvolvedSum` | 股权质押涉及股数(股) | number(16,0) | ✓ | 7.48% |  |
| 47 | `FreezeInvolvedSum` | 股权冻结涉及股数(股) | number(16,0) | ✓ | 0.76% |  |
| 48 | `PFStatement` | 股权质押冻结情况说明 | varchar2(200) | ✓ | 0.27% |  |
| 49 | `ConnectionRelation` | 股东关联关系 | varchar2(50) | ✓ | 10.52% |  |
| 50 | `ConnectionStatement` | 与其他股东关联关系说明 | varchar2(2000) | ✓ | 10.34% |  |
| 51 | `ActInConcertStatement` | 与其他股东同属一致行动人说明 | varchar2(2000) | ✓ | 5.46% |  |
| 52 | `Notes` | 备注 | varchar2(255) | ✓ | 0.05% |  |
| 53 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 54 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 55 | `JSID` | JSID | number(19) | ✗ |  |  |
| 56 | `SecuCoBelongedCode` | 归属机构编码 | number(10) | ✓ | 51.11% | 归属机构编码（SecuCoBelongedCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号... |
| 57 | `SecuCoBelongedName` | 归属机构名称 | varchar2(200) | ✓ | 45.28% |  |
| 58 | `SecuInnerCode` | 所属基金/股票内部编码 | number(10) | ✓ | 11.1% | 所属基金/股票内部编码（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 59 | `SecuCode` | 所属基金/股票代码 | varchar2(10) | ✓ | 11.1% |  |
| 60 | `SecuAbbr` | 所属基金/股票简称 | varchar2(20) | ✓ | 11.1% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoTypeCode (信息类别编码)

信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM IN (1,2,4,5,6,7)，得到信息类别编码的具体描述：1-前十大股东，2-前十流通股东，4-十大有限售条件股东，5-发行前股东，6-前十大表决权数量股东，7-5%以上股东持股变动。

### SHNo (股东排名)

股东排名（SHNo）：当“信息类别代码（InfoTypeCode）”=1时，“股东排名（SHNo）”表示股东排名；当“信息类别代码（InfoTypeCode）”=2时，“股东排名（SHNo）”表示流通股东排名。

### GDID (股东ID)

股东ID（GDID）：当股东属性（SHAttribute）=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与证券码表总表（SecuMainAll）中的证券内部编码（InnerCode）关联。

### SHList (股东名称)

股东名称（SHList）：此字段为股东名称公告原始披露值；如期望获取股东标准名称，可使用股东ID与相关表单关联，具体关联方式详见注4

### SHAttribute (股东属性)

股东属性(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到股东属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SHKindCode (股东性质编码)

股东性质编码(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026 AND DM NOT IN (13,16,40,50,60,61,67)，得到股东性质编码的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，14-职工工会，15-财务公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，64-保险投资组合，66-保险资管产品，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### SHTypeCode (股东类别编码)

股东类别编码(SHTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得到股东类别编码的具体描述：10-国有股东，20-外资股东，90-其他股东。

### HoldSum (持股数(股))

持股数（股）（HoldSum）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)=总股本当“信息类别代码（InfoTypeCode）”=2时，持股数(股)=无限售股数(股)

### HoldChangeType (持股变动类型)

持股变动类型(HoldChangeType)的具体描述：1-不变；2-增加；3-减少；4-新进

## SQL示例

```sql
-- 查询 股东名单(新) 数据
SELECT *
FROM lc_mainshlistnew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
