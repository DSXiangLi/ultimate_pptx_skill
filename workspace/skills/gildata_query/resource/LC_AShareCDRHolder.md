# LC_AShareCDRHolder

**中文名**: CDR持有人

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AShareCDRHolder` |
| MySQL表名 | `lc_asharecdrholder` |
| 中文名 | CDR持有人 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 41 |
| 版本 | 1.02 |

## 表描述

1.内容说明：本表收录公司CDR前十大持有人名单。
2.数据范围：CDR上市至今
3.信息来源：上海证券交易所、深圳证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 0.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 0.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 0.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 0.0% |  |
| 6 | `HolderNumber` | 持有人户数 | number(10) | ✓ | 0.0% |  |
| 7 | `HolderNo` | 持有人序号 | number(10) | ✗ | 0.0% |  |
| 8 | `HolderName` | 持有人名称 | varchar2(200) | ✓ | 0.0% |  |
| 9 | `HolderAttribute` | 持有人所属性质 | number(10) | ✓ | 0.0% | 持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 178... |
| 10 | `HolderID` | 持有人ID | number(10) | ✓ | 0.0% | 当持有人所属性质（HolderAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（... |
| 11 | `HolderCategoryDesc` | 持有人类别描述 | varchar2(100) | ✓ | 0.0% |  |
| 12 | `HolderCategory` | 持有人类别 | number(10) | ✓ | 0.0% | 持有人类别(HolderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得... |
| 13 | `HolderNature` | 持有人性质 | number(10) | ✓ |  |  |
| 14 | `SecuInnerCode` | 所属基金/股票 | number(10) | ✓ | 0.0% | 所属基金/股票（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 15 | `HoldSum` | 持有总数(万股) | number(18,2) | ✓ | 0.0% |  |
| 16 | `RestrictedSum` | 持有有限售总数(万股) | number(18,2) | ✓ | 0.0% |  |
| 17 | `NonRestrictedSum` | 持有无限售总数(万股) | number(18,2) | ✓ | 0.0% |  |
| 18 | `HoldRatio` | 持有比例(%) | number(19,8) | ✓ | 0.0% |  |
| 19 | `PledgedSum` | 质押数量(万股) | number(18,2) | ✓ | 0.0% |  |
| 20 | `FrozenSum` | 冻结数量(万股) | number(18,2) | ✓ | 0.0% |  |
| 21 | `PFStatement` | 质押冻结说明 | varchar2(200) | ✓ | 0.0% |  |
| 22 | `HolderRelationship` | 持有人关联关系 | varchar2(50) | ✓ | 0.0% |  |
| 23 | `ConnectionStatement` | 关联关系说明 | varchar2(1000) | ✓ | 0.0% |  |
| 24 | `ActInConcertStatement` | 一致行动人说明 | varchar2(1000) | ✓ | 0.0% |  |
| 25 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |
| 28 | `InfoTypeCode` | 信息类别编码 | number(10) | ✓ | 0.0% |  |
| 29 | `VotingRightsVol` | 表决权总数(票) | number(18,2) | ✓ | 0.0% |  |
| 30 | `VotingRightsRatio` | 表决权比例(%) | number(19,8) | ✓ | 0.0% |  |
| 31 | `HoldShareASum` | 持有A类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 32 | `RestrainedShareA` | 其中:有限售A类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 33 | `UnstintedShareA` | 其中:无限售A类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 34 | `HoldShareBSum` | 持有B类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 35 | `RestrainedShareB` | 其中:有限售B类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 36 | `UnstintedShareB` | 其中:无限售B类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 37 | `HoldShareCSum` | 持有C类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 38 | `HoldShareDSum` | 持有D类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 39 | `HoldOtherComShareSum` | 持有其他类普通股数量(份) | number(18,2) | ✓ | 0.0% |  |
| 40 | `SpecialVotingRightsVol` | 特别表决权数量(票) | number(18,2) | ✓ | 0.0% |  |
| 41 | `ShareTypeStatement` | 股份类别描述 | varchar2(50) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### HolderAttribute (持有人所属性质)

持有人所属性质(HolderAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到持有人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### HolderID (持有人ID)

当持有人所属性质（HolderAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；持有人所属性质（HolderAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。

### HolderCategory (持有人类别)

持有人类别(HolderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1368，得到持有人类别的具体描述：10-国有股东，20-外资股东，90-其他股东。

### SecuInnerCode (所属基金/股票)

所属基金/股票（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到所属基金/股票的交易代码、交易简称等

## SQL示例

```sql
-- 查询 CDR持有人 数据
SELECT *
FROM lc_asharecdrholder
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
