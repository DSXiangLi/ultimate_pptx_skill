# LC_STIBCDRHolder

**中文名**: 科创板CDR持有人

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCDRHolder` |
| MySQL表名 | `lc_stibcdrholder` |
| 中文名 | 科创板CDR持有人 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 41 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录科创板公司发行存托凭证前十大持有人名单。
2.数据范围：2019至今
3.信息来源：上市公告书、临时公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `InfoTypeCode` | 信息类别编码 | number(10) | ✓ | 100.0% |  |
| 7 | `HolderNumber` | 持有人户数(户) | number(10) | ✓ | 32.86% |  |
| 8 | `HolderSN` | 持有人序号 | number(10) | ✗ | 100.0% |  |
| 9 | `HolderName` | 持有人名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `HolderAttribute` | 持有人所属性质 | number(10) | ✓ | 100.0% | 持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 178... |
| 11 | `HolderID` | 持有人ID | number(10) | ✓ | 87.79% | 持有人ID（CYRID）：当持有人所属性质（HolderAttribute）=2时，与机构基本资料（LC_InstiAr... |
| 12 | `HolderCategory` | 持有人类别 | number(10) | ✓ | 63.85% | 持有人类别(HolderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得... |
| 13 | `HolderCategoryDesc` | 持有人类别描述 | varchar2(100) | ✓ | 34.43% |  |
| 14 | `SHKindCode` | 持有人性质 | number(10) | ✓ |  | 持有人性质(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到持有人... |
| 15 | `SecuInnerCode` | 所属基金/股票 | number(10) | ✓ | 6.1% | 所属基金/股票（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 16 | `HoldSum` | 持有总数(份) | number(18,2) | ✓ | 94.68% |  |
| 17 | `RestrictedSum` | 持有有限售总数(份) | number(18,2) | ✓ | 47.89% |  |
| 18 | `NonRestrictedSum` | 持有无限售总数(份) | number(18,2) | ✓ | 63.54% |  |
| 19 | `HoldRatio` | 持有比例(%) | number(19,8) | ✓ | 94.68% |  |
| 20 | `VotingRightsVol` | 表决权总数(票) | number(18,2) | ✓ | 14.08% |  |
| 21 | `VotingRightsRatio` | 表决权比例(%) | number(19,8) | ✓ | 14.08% |  |
| 22 | `HoldShareASum` | 持有A类普通股数量(份) | number(18,2) | ✓ | 67.29% |  |
| 23 | `RestrainedShareA` | 其中:有限售A类普通股数量(份) | number(18,2) | ✓ | 32.55% |  |
| 24 | `UnstintedShareA` | 其中:无限售A类普通股数量(份) | number(18,2) | ✓ | 56.03% |  |
| 25 | `HoldShareBSum` | 持有B类普通股数量(份) | number(18,2) | ✓ | 20.34% |  |
| 26 | `RestrainedShareB` | 其中:有限售B类普通股数量(份) | number(18,2) | ✓ | 19.87% |  |
| 27 | `UnstintedShareB` | 其中:无限售B类普通股数量(份) | number(18,2) | ✓ | 11.89% |  |
| 28 | `HoldShareCSum` | 持有C类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 29 | `HoldShareDSum` | 持有D类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 30 | `HoldOtherComShareSum` | 持有其他类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 31 | `SpecialVotingRightsVol` | 特别表决权数量(票) | number(18,2) | ✓ | 7.04% |  |
| 32 | `ShareTypeStatement` | 股份类别描述 | varchar2(50) | ✓ | 87.79% |  |
| 33 | `PledgedSum` | 质押数量(份) | number(18,2) | ✓ | 0.0% |  |
| 34 | `FrozenSum` | 冻结数量(份) | number(18,2) | ✓ | 0.0% |  |
| 35 | `PFStatement` | 质押冻结说明 | varchar2(200) | ✓ | 0.0% |  |
| 36 | `HolderRelationship` | 持有人关联关系 | varchar2(50) | ✓ | 7.04% |  |
| 37 | `ConnectionStatement` | 关联关系说明 | varchar2(1000) | ✓ | 7.36% |  |
| 38 | `ActInConcertStatement` | 一致行动人说明 | varchar2(1000) | ✓ | 7.36% |  |
| 39 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 40 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 41 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### HolderAttribute (持有人所属性质)

持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持有人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### HolderID (持有人ID)

持有人ID（CYRID）：当持有人所属性质（HolderAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；持有人所属性质（HolderAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

### HolderCategory (持有人类别)

持有人类别(HolderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得到持有人类别的具体描述：10-国有股东，20-外资股东，90-其他股东。

### SHKindCode (持有人性质)

持有人性质(SHKindCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1026，得到持有人性质的具体描述：1-封闭式投资基金，2-开放式投资基金，3-金融机构—信托公司，4-金融机构—保险公司，5-金融机构—期货公司，6-金融机构—银行，7-公益基金，8-投资、咨询公司，9-风险投资公司，10-金融机构—金融租赁公司，11-院校—高校，12-院校—研究院，13-院校—院校企业，14-职工工会，15-财务公司，16-上市公司，17-资产管理公司，18-自然人，19-国资局，20-基金管理公司，21-基金专户理财，22-金融机构—证券公司，30-社保基金、社保机构，35-企业年金，37-券商集合资产管理计划，38-信托公司单一证券信托，39-信托公司集合信托计划，40-金融机构—信用社，50-上市公司下属公司，60-中外合资企业，61-外资独资企业，64-保险投资组合，66-保险资管产品，67-股市国家队，68-基本养老保险基金，98-一般企业，99-其他金融产品。

### SecuInnerCode (所属基金/股票)

所属基金/股票（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到所属基金/股票的交易代码、交易简称等" 

## SQL示例

```sql
-- 查询 科创板CDR持有人 数据
SELECT *
FROM lc_stibcdrholder
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
