# CS_StockQuoteInfo

**中文名**: 境内股票盘口信息表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockQuoteInfo` |
| MySQL表名 | `cs_stockquoteinfo` |
| 中文名 | 境内股票盘口信息表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

内容说明：收录上交所及深交所集合竞价时间段(9:15至9:25，14:57至15:00)的集合竞价信息以及15:00收盘时刻的盘口买1~买5、卖1~卖5的量价信息
数据范围：2023年2月至今
信息来源：沪深交易所行情数据，聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `AuctionType` | 集合竞价类型 | number(10) | ✗ | 100.0% | 集合竞价类型(AuctionType)，该字段固定以下常量：1-开盘集合竞价，2-收盘集合竞价 |
| 5 | `AuctionPrice` | 集合竞价成交价 | number(19,4) | ✓ | 57.24% |  |
| 6 | `AuctionVolume` | 集合竞价成交量 | number(19,4) | ✓ | 57.24% |  |
| 7 | `AuctionValue` | 集合竞价成交金额 | number(19,4) | ✓ | 24.57% |  |
| 8 | `AuctionDeals` | 集合竞价成交笔数 | number(19,4) | ✓ | 46.2% |  |
| 9 | `BidFirstPrice` | 买入价一 | number(19,4) | ✓ | 59.46% |  |
| 10 | `BidSecondPrice` | 买入价二 | number(19,4) | ✓ | 59.45% |  |
| 11 | `BidThirdPrice` | 买入价三 | number(19,4) | ✓ | 59.45% |  |
| 12 | `BidFourthPrice` | 买入价四 | number(19,4) | ✓ | 59.45% |  |
| 13 | `BidFifthPrice` | 买入价五 | number(19,4) | ✓ | 59.45% |  |
| 14 | `BidFirstVolume` | 买入量一 | number(19,4) | ✓ | 24.57% |  |
| 15 | `BidSecondVolume` | 买入量二 | number(19,4) | ✓ | 24.57% |  |
| 16 | `BidThirdVolume` | 买入量三 | number(19,4) | ✓ | 24.57% |  |
| 17 | `BidFourthVolume` | 买入量四 | number(19,4) | ✓ | 24.57% |  |
| 18 | `BidFifthVolume` | 买入量五 | number(19,4) | ✓ | 24.57% |  |
| 19 | `AskFirstPrice` | 卖出价一 | number(19,4) | ✓ | 59.45% |  |
| 20 | `AskSecondPrice` | 卖出价二 | number(19,4) | ✓ | 59.45% |  |
| 21 | `AskThirdPrice` | 卖出价三 | number(19,4) | ✓ | 59.45% |  |
| 22 | `AskFourthPrice` | 卖出价四 | number(19,4) | ✓ | 59.45% |  |
| 23 | `AskFifthPrice` | 卖出价五 | number(19,4) | ✓ | 59.46% |  |
| 24 | `AskFirstVolume` | 卖出量一 | number(19,4) | ✓ | 24.57% |  |
| 25 | `AskSecondVolume` | 卖出量二 | number(19,4) | ✓ | 24.57% |  |
| 26 | `AskThirdVolume` | 卖出量三 | number(19,4) | ✓ | 24.57% |  |
| 27 | `AskFourthVolume` | 卖出量四 | number(19,4) | ✓ | 24.57% |  |
| 28 | `AskFifthVolume` | 卖出量五 | number(19,4) | ✓ | 24.57% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### AuctionType (集合竞价类型)

集合竞价类型(AuctionType)，该字段固定以下常量：1-开盘集合竞价，2-收盘集合竞价

## SQL示例

```sql
-- 查询 境内股票盘口信息表 数据
SELECT *
FROM cs_stockquoteinfo
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
