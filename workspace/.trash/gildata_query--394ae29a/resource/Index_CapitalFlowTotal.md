# Index_CapitalFlowTotal

**中文名**: 指数交易资金流向

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_CapitalFlowTotal` |
| MySQL表名 | `index_capitalflowtotal` |
| 中文名 | 指数交易资金流向 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 103 |
| 版本 | 1 |

## 表描述

1. 内容说明：本表收录成份为沪深京交易所股票的指数在每个交易日基于不同成交金额区间及成交时间区间主动及含主动被动交易的累计流入流出金额、量等信息衍生计算的统计类指标。北交所因不统计平盘资金流，全单流入量或全单流出量会小于总成交量，且北交所资金流无主被动之分，因此主动字样字段计算不包含北交所个股数据。个股数据可参考境内股票交易资金流向指标(CS_StockCapFlowIndex)。
2. 数据范围：2016-11-29至今
2023-10-09 及以后提供完整全盘、开盘、尾盘主买主卖及含主动被动数据
2022-11-15~2023-09-28 仅提供全盘主买主卖及含主动被动资金流向数据
2016-11-29~2022-11-14 仅提供全盘含主动被动资金流向数据
3. 信息来源：基于交易所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `TimeRange` | 成交时间区间 | number(10) | ✗ | 100.0% | 成交时间区间(TimeRange)，该字段固定以下常量：1-全盘，2-开盘，3-尾盘 |
| 5 | `SmallBuyValue` | 小单流入额(元) | number(19,4) | ✓ | 100.0% | 小单：单笔成交量区间为[0，2w)或成交金额区间为[0，4w) |
| 6 | `SmallSellValue` | 小单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `SmallBuyVolume` | 小单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 8 | `SmallSellVolume` | 小单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 9 | `SmallBuyNum` | 小单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 10 | `SmallSellNum` | 小单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 11 | `SmallNetBuyValue` | 小单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `SmallNetBuyVolume` | 小单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 13 | `SmallActBuyValue` | 小单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 14 | `SmallActSellValue` | 小单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 15 | `SmallActBuyVolume` | 小单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 16 | `SmallActSellVolume` | 小单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 17 | `SmallActBuyNum` | 小单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 18 | `SmallActSellNum` | 小单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 19 | `SmallNetActBuyValue` | 小单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `SmallNetActBuyVolume` | 小单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 21 | `MediumBuyValue` | 中单流入额(元) | number(19,4) | ✓ | 100.0% | 中单：单笔成交量区间为[2w，10w)或成交金额区间为[4w，20w) |
| 22 | `MediumSellValue` | 中单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 23 | `MediumBuyVolume` | 中单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 24 | `MediumSellVolume` | 中单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 25 | `MediumBuyNum` | 中单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 26 | `MediumSellNum` | 中单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 27 | `MediumNetBuyValue` | 中单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `MediumNetBuyVolume` | 中单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 29 | `MediumActBuyValue` | 中单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 30 | `MediumActSellValue` | 中单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 31 | `MediumActBuyVolume` | 中单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 32 | `MediumActSellVolume` | 中单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 33 | `MediumActBuyNum` | 中单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 34 | `MediumActSellNum` | 中单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 35 | `MediumNetActBuyValue` | 中单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 36 | `MediumNetActBuyVolume` | 中单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 37 | `LargeBuyValue` | 大单流入额(元) | number(19,4) | ✓ | 100.0% | 大单：单笔成交量区间为[10w，50w)或成交金额区间为[20w，100w) |
| 38 | `LargeSellValue` | 大单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 39 | `LargeBuyVolume` | 大单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 40 | `LargeSellVolume` | 大单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 41 | `LargeBuyNum` | 大单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 42 | `LargeSellNum` | 大单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 43 | `LargeNetBuyValue` | 大单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 44 | `LargeNetBuyVolume` | 大单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 45 | `LargeActBuyValue` | 大单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 46 | `LargeActSellValue` | 大单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 47 | `LargeActBuyVolume` | 大单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 48 | `LargeActSellVolume` | 大单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 49 | `LargeActBuyNum` | 大单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 50 | `LargeActSellNum` | 大单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 51 | `LargeNetActBuyValue` | 大单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 52 | `LargeNetActBuyVolume` | 大单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 53 | `HugeBuyValue` | 超大单流入额(元) | number(19,4) | ✓ | 100.0% | 超大单：单笔成交量区间为[50w，+∞)或成交金额区间为[100w，+∞) |
| 54 | `HugeSellValue` | 超大单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 55 | `HugeBuyVolume` | 超大单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 56 | `HugeSellVolume` | 超大单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 57 | `HugeBuyNum` | 超大单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 58 | `HugeSellNum` | 超大单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 59 | `HugeNetBuyValue` | 超大单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 60 | `HugeNetBuyVolume` | 超大单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 61 | `HugeActBuyValue` | 超大单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 62 | `HugeActSellValue` | 超大单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 63 | `HugeActBuyVolume` | 超大单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 64 | `HugeActSellVolume` | 超大单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 65 | `HugeActBuyNum` | 超大单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 66 | `HugeActSellNum` | 超大单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 67 | `HugeNetActBuyValue` | 超大单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 68 | `HugeNetActBuyVolume` | 超大单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 69 | `MainBuyValue` | 主力流入额(元) | number(19,4) | ✓ | 100.0% | 主力=大单+超大单 |
| 70 | `MainSellValue` | 主力流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 71 | `MainBuyVolume` | 主力流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 72 | `MainSellVolume` | 主力流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 73 | `MainBuyNum` | 主力流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 74 | `MainSellNum` | 主力流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 75 | `MainNetBuyValue` | 主力净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 76 | `MainNetBuyVolume` | 主力净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 77 | `MainActBuyValue` | 主力主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 78 | `MainActSellValue` | 主力主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 79 | `MainActBuyVolume` | 主力主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 80 | `MainActSellVolume` | 主力主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 81 | `MainActBuyNum` | 主力主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 82 | `MainActSellNum` | 主力主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 83 | `MainNetActBuyValue` | 主力净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 84 | `MainNetActBuyVolume` | 主力净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 85 | `TotalBuyValue` | 全单流入额(元) | number(19,4) | ✓ | 100.0% | 全单=小单+中单+大单+超大单 |
| 86 | `TotalSellValue` | 全单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 87 | `TotalBuyVolume` | 全单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 88 | `TotalSellVolume` | 全单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 89 | `TotalBuyNum` | 全单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 90 | `TotalSellNum` | 全单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 91 | `TotalNetBuyValue` | 全单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 92 | `TotalNetBuyVolume` | 全单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 93 | `TotalActBuyValue` | 全单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 94 | `TotalActSellValue` | 全单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 95 | `TotalActBuyVolume` | 全单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 96 | `TotalActSellVolume` | 全单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 97 | `TotalActBuyNum` | 全单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 98 | `TotalActSellNum` | 全单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 99 | `TotalNetActBuyValue` | 全单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 100 | `TotalNetActBuyVolume` | 全单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 101 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 102 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 103 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### TimeRange (成交时间区间)

成交时间区间(TimeRange)，该字段固定以下常量：1-全盘，2-开盘，3-尾盘

### SmallBuyValue (小单流入额(元))

小单：单笔成交量区间为[0，2w)或成交金额区间为[0，4w)

### MediumBuyValue (中单流入额(元))

中单：单笔成交量区间为[2w，10w)或成交金额区间为[4w，20w)

### LargeBuyValue (大单流入额(元))

大单：单笔成交量区间为[10w，50w)或成交金额区间为[20w，100w)

### HugeBuyValue (超大单流入额(元))

超大单：单笔成交量区间为[50w，+∞)或成交金额区间为[100w，+∞)

### MainBuyValue (主力流入额(元))

主力=大单+超大单

### TotalBuyValue (全单流入额(元))

全单=小单+中单+大单+超大单

## SQL示例

```sql
-- 查询 指数交易资金流向 数据
SELECT *
FROM index_capitalflowtotal
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
