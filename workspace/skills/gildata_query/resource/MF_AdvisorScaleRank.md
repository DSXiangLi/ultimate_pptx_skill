# MF_AdvisorScaleRank

**中文名**: 公募基金管理人规模及排名情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AdvisorScaleRank` |
| MySQL表名 | `mf_advisorscalerank` |
| 中文名 | 公募基金管理人规模及排名情况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 季更新 |
| 字段数量 | 66 |
| 版本 | 1.03 |

## 表描述

1.内容说明：本表记录基金管理公司管理公募基金的基金数量、基金份额和基金净值等统计情况。
2.数据范围：2013.1-至今
3.信息来源：基于基金公司定报披露基础数据计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InvestAdvisorCode` | 基金管理人编码 | number(10) | ✗ | 100.0% | 基金管理人编码(InvestAdvisorCode)：与机构基本资料(LC_InstiArchive)表的企业编号(Co... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TotalFundNV` | 总管理规模(亿元) | number(18,10) | ✓ | 99.92% |  |
| 5 | `FundNVRank` | 总管理规模排名 | number(10) | ✓ | 99.92% |  |
| 6 | `TotalFundN` | 旗下基金总数(只) | number(10) | ✓ | 100.0% |  |
| 7 | `FundNRank` | 旗下基金数量排名 | number(10) | ✓ | 100.0% |  |
| 8 | `TotalAdvisor` | 基金公司总数 | number(10) | ✓ | 100.0% |  |
| 9 | `EquityFundNV` | 股票型管理规模(亿元) | number(18,10) | ✓ | 73.42% |  |
| 10 | `EquityNVRank` | 股票型基金管理规模排名 | number(10) | ✓ | 73.42% |  |
| 11 | `EquityFundN` | 股票型基金数量(只) | number(10) | ✓ | 100.0% |  |
| 12 | `EquityNRank` | 股票型基金管理数量排名 | number(10) | ✓ | 73.44% |  |
| 13 | `AdvisorOfEquity` | 管理股票型基金公司数 | number(10) | ✓ | 100.0% |  |
| 14 | `HybridFundNV` | 混合型管理规模(亿元) | number(18,10) | ✓ | 90.07% |  |
| 15 | `HybridNVRank` | 混合型基金管理规模排名 | number(10) | ✓ | 90.07% |  |
| 16 | `HybridFundN` | 混合型基金数量(只) | number(10) | ✓ | 100.0% |  |
| 17 | `HybridNRank` | 混合型基金管理数量排名 | number(10) | ✓ | 90.13% |  |
| 18 | `AdvisorOfHybrid` | 管理混合型基金公司数 | number(10) | ✓ | 100.0% |  |
| 19 | `BondFundNV` | 债券型管理规模(亿元) | number(18,10) | ✓ | 81.07% |  |
| 20 | `BondNVRank` | 债券型基金管理规模排名 | number(10) | ✓ | 81.07% |  |
| 21 | `BondFundN` | 债券型基金数量(只) | number(10) | ✓ | 100.0% |  |
| 22 | `BondNRank` | 债券型基金管理数量排名 | number(10) | ✓ | 81.2% |  |
| 23 | `AdvisorOfBond` | 管理债券型基金公司数 | number(10) | ✓ | 100.0% |  |
| 24 | `MonetaryFundNV` | 货币型管理规模(亿元) | number(18,10) | ✓ | 73.06% |  |
| 25 | `MonetaryNVRank` | 货币型基金管理规模排名 | number(10) | ✓ | 73.05% |  |
| 26 | `MonetaryFundN` | 货币型基金数量(只) | number(10) | ✓ | 100.0% |  |
| 27 | `MonetaryNRank` | 货币型基金管理数量排名 | number(10) | ✓ | 73.19% |  |
| 28 | `AdvisorOfMonetary` | 管理货币型基金公司数 | number(10) | ✓ | 100.0% |  |
| 29 | `ShortBondFundNV` | 理财型管理规模(亿元) | number(18,10) | ✓ | 7.62% |  |
| 30 | `ShortBondNVRank` | 理财型基金管理规模排名 | number(10) | ✓ | 7.23% |  |
| 31 | `ShortBondFundN` | 理财型基金数量(只) | number(10) | ✓ | 100.0% |  |
| 32 | `ShortBondNRank` | 理财型基金管理数量排名 | number(10) | ✓ | 7.62% |  |
| 33 | `AdvisorOfShortBond` | 管理理财型基金公司数 | number(10) | ✓ | 100.0% |  |
| 34 | `QDIINV` | QDII管理规模(亿元) | number(18,10) | ✓ | 22.45% |  |
| 35 | `QDIINVRank` | QDII基金管理规模排名 | number(10) | ✓ | 22.45% |  |
| 36 | `QDIIN` | QDII基金数量(只) | number(10) | ✓ | 100.0% |  |
| 37 | `QDIINRank` | QDII基金管理数量排名 | number(10) | ✓ | 22.45% |  |
| 38 | `AdvisorOfQDII` | 管理QDII基金公司数 | number(10) | ✓ | 100.0% |  |
| 39 | `FOFNV` | FOF管理规模(亿元) | number(18,10) | ✓ | 19.4% |  |
| 40 | `FOFNVRank` | FOF基金管理规模排名 | number(10) | ✓ | 19.4% |  |
| 41 | `FOFN` | FOF基金数量(只) | number(10) | ✓ | 100.0% |  |
| 42 | `FOFNRank` | FOF基金管理数量排名 | number(10) | ✓ | 19.43% |  |
| 43 | `AdvisorOfFOF` | 管理FOF基金公司数 | number(10) | ✓ | 100.0% |  |
| 44 | `REITsNV` | REITs管理规模(亿元) | number(18,10) | ✓ | 3.18% |  |
| 45 | `REITsNVRank` | REITs基金管理规模排名 | number(10) | ✓ | 3.18% |  |
| 46 | `REITsN` | REITs基金数量(只) | number(10) | ✓ | 100.0% |  |
| 47 | `REITsNRank` | REITs基金管理数量排名 | number(10) | ✓ | 3.18% |  |
| 48 | `AdvisorOfREITs` | 管理REITs基金公司数 | number(10) | ✓ | 100.0% |  |
| 49 | `CommodityFundNV` | 商品管理规模(亿元) | number(18,10) | ✓ | 4.85% |  |
| 50 | `CommodityFundNVRank` | 商品基金管理规模排名 | number(10) | ✓ | 4.85% |  |
| 51 | `CommodityFundN` | 商品基金数量(只) | number(10) | ✓ | 100.0% |  |
| 52 | `CommodityFundNRank` | 商品基金管理数量排名 | number(10) | ✓ | 4.85% |  |
| 53 | `AdvisorOfCommodityFund` | 管理商品基金公司数 | number(10) | ✓ | 100.0% |  |
| 54 | `UnMSBFNV` | 非货基与理财债基管理规模(亿元) | number(18,10) | ✓ | 97.82% |  |
| 55 | `UnMSBFNVRank` | 非货基与理财债基管理规模排名 | number(10) | ✓ | 97.82% |  |
| 56 | `UnMSBFN` | 非货基与理财债基数量(只) | number(10) | ✓ | 100.0% |  |
| 57 | `UnMSBFNRank` | 非货基与理财债基管理数量排名 | number(10) | ✓ | 97.91% |  |
| 58 | `AdvisorOfUnMSBF` | 管理非货基与理财债基公司数 | number(10) | ✓ | 100.0% |  |
| 59 | `ActiveEFNV` | 主动权益类基金管理规模(亿元) | number(18,10) | ✓ | 63.79% |  |
| 60 | `ActiveEFNVRank` | 主动权益类基金管理规模排名 | number(10) | ✓ | 63.79% |  |
| 61 | `ActiveEFN` | 主动权益类基金数量(只) | number(10) | ✓ | 100.0% |  |
| 62 | `ActiveEFNRank` | 主动权益类基金管理数量排名 | number(10) | ✓ | 63.81% |  |
| 63 | `AdvisorOfActiveEF` | 管理主动权益类基金公司数 | number(10) | ✓ | 100.0% |  |
| 64 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 65 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 66 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InvestAdvisorCode (基金管理人编码)

基金管理人编码(InvestAdvisorCode)：与机构基本资料(LC_InstiArchive)表的企业编号(CompanyCode)字段关联，可查询基金管理人中文名称、英文名称、组织机构代码等基本信息。

## SQL示例

```sql
-- 查询 公募基金管理人规模及排名情况 数据
SELECT *
FROM mf_advisorscalerank
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
