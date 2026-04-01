# FM_FundCMPFSize

**中文名**: 基金业协会公募基金规模

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FM_FundCMPFSize` |
| MySQL表名 | `fm_fundcmpfsize` |
| 中文名 | 基金业协会公募基金规模 |
| 路径 | 聚源新版数据库 > 市场统计数据库 > 证券市场统计 |
| 更新频率 | 月更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.本表记录基金管理公司管理公募基金的基金数量、基金份额和基金净值等统计情况。
2.数据范围：2013.1-至今
3.信息来源：中国证券投资基金业协会

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `StatPeriod` | 统计区间 | number(10) | ✗ | 100.0% | 统计区间（StatPeriod）：该字段固定常量以下常量：200-当月及累计；210-当季及累计。 |
| 6 | `ClosedEndFundN` | 1.封闭式基金(只) | number(10) | ✓ | 98.32% |  |
| 7 | `OpenEndedFundN` | 2.开放式基金(只) | number(10) | ✓ | 98.32% |  |
| 8 | `EquityFundN` | 其中:股票基金(只) | number(10) | ✓ | 98.32% |  |
| 9 | `HybridFundN` | 其中:混合基金(只) | number(10) | ✓ | 98.32% |  |
| 10 | `MonetaryFundN` | 其中:货币基金(只) | number(10) | ✓ | 98.32% |  |
| 11 | `BondFundN` | 其中:债券基金(只) | number(10) | ✓ | 98.32% |  |
| 12 | `QDIIFundN` | 其中:QDII基金(只) | number(10) | ✓ | 98.32% |  |
| 13 | `TotalFundN` | 合计-基金数量(只) | number(10) | ✓ | 98.32% |  |
| 14 | `ClosedEndFundS` | 1.封闭式基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 15 | `OpenEndedFundS` | 2.开放式基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 16 | `EquityFundS` | 其中:股票基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 17 | `HybridFundS` | 其中:混合基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 18 | `MonetaryFundS` | 其中:货币基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 19 | `BondFundS` | 其中:债券基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 20 | `QDIIFundS` | 其中:QDII基金(亿份) | number(10,2) | ✓ | 98.32% |  |
| 21 | `TotalFundS` | 合计-基金份额(亿份) | number(10,2) | ✓ | 98.32% |  |
| 22 | `ClosedEndFundNV` | 1.封闭式基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 23 | `OpenEndedFundNV` | 2.开放式基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 24 | `EquityFundNV` | 其中:股票基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 25 | `HybridFundNV` | 其中:混合基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 26 | `MonetaryFundNV` | 其中:货币基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 27 | `BondFundNV` | 其中:债券基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 28 | `QDIIFundNV` | 其中:QDII基金(亿元) | number(10,2) | ✓ | 98.32% |  |
| 29 | `TotalFundNV` | 合计-基金净值(亿元) | number(10,2) | ✓ | 98.32% |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StatPeriod (统计区间)

统计区间（StatPeriod）：该字段固定常量以下常量：200-当月及累计；210-当季及累计。

## SQL示例

```sql
-- 查询 基金业协会公募基金规模 数据
SELECT *
FROM fm_fundcmpfsize
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
