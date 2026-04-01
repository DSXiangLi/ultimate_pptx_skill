# CS_StockCapFlowIndex

**中文名**: 境内股票交易资金流向指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockCapFlowIndex` |
| MySQL表名 | `cs_stockcapflowindex` |
| 中文名 | 境内股票交易资金流向指标 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 199 |
| 版本 | 1 |

## 表描述

内容说明：
1、收录深沪京交易所正常交易的股票在每个交易日基于不同成交金额区间及成交时间区间主动及含主动被动交易的累计流入流出金额、量等信息衍生计算的统计类指标
2、数据提供范围说明
2023-10-09 及以后提供完整全盘、开盘、尾盘主买主卖及含主动被动数据
2022-11-15~2023-09-28 仅提供全盘主买主卖及含主动被动资金流向数据
2016-11-29~2022-11-14 仅提供全盘含主动被动资金流向数据
3、北交所数据特别说明：北交所因不统计平盘资金流，全单流入量或全单流出量会小于总成交量，且北交所资金流无主被动之分，因此主动字样字段不提供
数据范围：2016-11-29至今
信息来源：基于交易所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
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
| 13 | `SmallBValueRatio` | 小单买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 14 | `SmallSValueRatio` | 小单卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 15 | `SmallBVolumeRatio` | 小单买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 16 | `SmallSVolumeRatio` | 小单卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 17 | `SmallNBValueRatio` | 小单净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 18 | `SmallNBVFloatMVRatio` | 小单净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 19 | `SmallNBVolumeRatio` | 小单净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 20 | `SmallNBVFloatSRatio` | 小单净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 21 | `SmallActBuyValue` | 小单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 22 | `SmallActSellValue` | 小单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 23 | `SmallActBuyVolume` | 小单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 24 | `SmallActSellVolume` | 小单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 25 | `SmallActBuyNum` | 小单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 26 | `SmallActSellNum` | 小单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 27 | `SmallNetActBuyValue` | 小单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `SmallNetActBuyVolume` | 小单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 29 | `SmallABValueRatio` | 小单主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 30 | `SmallASValueRatio` | 小单主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 31 | `SmallABVolumeRatio` | 小单主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 32 | `SmallASVolumeRatio` | 小单主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 33 | `SmallNABValueRatio` | 小单净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 34 | `SmallNABVFloatMVRatio` | 小单净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 35 | `SmallNABVolumeRatio` | 小单净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 36 | `SmallNABVFloatSRatio` | 小单净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 37 | `MediumBuyValue` | 中单流入额(元) | number(19,4) | ✓ | 100.0% | 中单：单笔成交量区间为[2w，10w)或成交金额区间为[4w，20w) |
| 38 | `MediumSellValue` | 中单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 39 | `MediumBuyVolume` | 中单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 40 | `MediumSellVolume` | 中单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 41 | `MediumBuyNum` | 中单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 42 | `MediumSellNum` | 中单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 43 | `MediumNetBuyValue` | 中单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 44 | `MediumNetBuyVolume` | 中单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 45 | `MediumBValueRatio` | 中单买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 46 | `MediumSValueRatio` | 中单卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 47 | `MediumBVolumeRatio` | 中单买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 48 | `MediumSVolumeRatio` | 中单卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 49 | `MediumNBValueRatio` | 中单净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 50 | `MediumNBVFloatMVRatio` | 中单净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 51 | `MediumNBVolumeRatio` | 中单净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 52 | `MediumNBVFloatSRatio` | 中单净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 53 | `MediumActBuyValue` | 中单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 54 | `MediumActSellValue` | 中单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 55 | `MediumActBuyVolume` | 中单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 56 | `MediumActSellVolume` | 中单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 57 | `MediumActBuyNum` | 中单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 58 | `MediumActSellNum` | 中单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 59 | `MediumNetActBuyValue` | 中单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 60 | `MediumNetActBuyVolume` | 中单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 61 | `MediumABValueRatio` | 中单主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 62 | `MediumASValueRatio` | 中单主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 63 | `MediumABVolumeRatio` | 中单主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 64 | `MediumASVolumeRatio` | 中单主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 65 | `MediumNABValueRatio` | 中单净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 66 | `MediumNABVFloatMVRatio` | 中单净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 67 | `MediumNABVolumeRatio` | 中单净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 68 | `MediumNABVFloatSRatio` | 中单净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 69 | `LargeBuyValue` | 大单流入额(元) | number(19,4) | ✓ | 100.0% | 大单：单笔成交量区间为[10w，50w)或成交金额区间为[20w，100w) |
| 70 | `LargeSellValue` | 大单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 71 | `LargeBuyVolume` | 大单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 72 | `LargeSellVolume` | 大单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 73 | `LargeBuyNum` | 大单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 74 | `LargeSellNum` | 大单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 75 | `LargeNetBuyValue` | 大单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 76 | `LargeNetBuyVolume` | 大单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 77 | `LargeBValueRatio` | 大单买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 78 | `LargeSValueRatio` | 大单卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 79 | `LargeBVolumeRatio` | 大单买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 80 | `LargeSVolumeRatio` | 大单卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 81 | `LargeNBValueRatio` | 大单净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 82 | `LargeNBVFloatMVRatio` | 大单净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 83 | `LargeNBVolumeRatio` | 大单净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 84 | `LargeNBVFloatSRatio` | 大单净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 85 | `LargeActBuyValue` | 大单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 86 | `LargeActSellValue` | 大单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 87 | `LargeActBuyVolume` | 大单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 88 | `LargeActSellVolume` | 大单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 89 | `LargeActBuyNum` | 大单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 90 | `LargeActSellNum` | 大单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 91 | `LargeNetActBuyValue` | 大单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 92 | `LargeNetActBuyVolume` | 大单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 93 | `LargeABValueRatio` | 大单主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 94 | `LargeASValueRatio` | 大单主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 95 | `LargeABVolumeRatio` | 大单主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 96 | `LargeASVolumeRatio` | 大单主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 97 | `LargeNABValueRatio` | 大单净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 98 | `LargeNABVFloatMVRatio` | 大单净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 99 | `LargeNABVolumeRatio` | 大单净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 100 | `LargeNABVFloatSRatio` | 大单净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 101 | `HugeBuyValue` | 超大单流入额(元) | number(19,4) | ✓ | 100.0% | 超大单：单笔成交量区间为[50w，+∞)或成交金额区间为[100w，+∞) |
| 102 | `HugeSellValue` | 超大单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 103 | `HugeBuyVolume` | 超大单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 104 | `HugeSellVolume` | 超大单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 105 | `HugeBuyNum` | 超大单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 106 | `HugeSellNum` | 超大单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 107 | `HugeNetBuyValue` | 超大单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 108 | `HugeNetBuyVolume` | 超大单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 109 | `HugeBValueRatio` | 超大单买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 110 | `HugeSValueRatio` | 超大单卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 111 | `HugeBVolumeRatio` | 超大单买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 112 | `HugeSVolumeRatio` | 超大单卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 113 | `HugeNBValueRatio` | 超大单净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 114 | `HugeNBVFloatMVRatio` | 超大单净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 115 | `HugeNBVolumeRatio` | 超大单净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 116 | `HugeNBVFloatSRatio` | 超大单净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 117 | `HugeActBuyValue` | 超大单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 118 | `HugeActSellValue` | 超大单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 119 | `HugeActBuyVolume` | 超大单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 120 | `HugeActSellVolume` | 超大单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 121 | `HugeActBuyNum` | 超大单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 122 | `HugeActSellNum` | 超大单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 123 | `HugeNetActBuyValue` | 超大单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 124 | `HugeNetActBuyVolume` | 超大单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 125 | `HugeABValueRatio` | 超大单主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 126 | `HugeASValueRatio` | 超大单主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 127 | `HugeABVolumeRatio` | 超大单主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 128 | `HugeASVolumeRatio` | 超大单主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 129 | `HugeNABValueRatio` | 超大单净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 130 | `HugeNABVFloatMVRatio` | 超大单净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 131 | `HugeNABVolumeRatio` | 超大单净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 132 | `HugeNABVFloatSRatio` | 超大单净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 133 | `MainBuyValue` | 主力流入额(元) | number(19,4) | ✓ | 100.0% | 主力=大单+超大单 |
| 134 | `MainSellValue` | 主力流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 135 | `MainBuyVolume` | 主力流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 136 | `MainSellVolume` | 主力流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 137 | `MainBuyNum` | 主力流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 138 | `MainSellNum` | 主力流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 139 | `MainNetBuyValue` | 主力净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 140 | `MainNetBuyVolume` | 主力净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 141 | `MainBValueRatio` | 主力买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 142 | `MainSValueRatio` | 主力卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 143 | `MainBVolumeRatio` | 主力买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 144 | `MainSVolumeRatio` | 主力卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 145 | `MainNBValueRatio` | 主力净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 146 | `MainNBVFloatMVRatio` | 主力净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 147 | `MainNBVolumeRatio` | 主力净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 148 | `MainNBVFloatSRatio` | 主力净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 149 | `MainActBuyValue` | 主力主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 150 | `MainActSellValue` | 主力主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 151 | `MainActBuyVolume` | 主力主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 152 | `MainActSellVolume` | 主力主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 153 | `MainActBuyNum` | 主力主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 154 | `MainActSellNum` | 主力主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 155 | `MainNetActBuyValue` | 主力净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 156 | `MainNetActBuyVolume` | 主力净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 157 | `MainABValueRatio` | 主力主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 158 | `MainASValueRatio` | 主力主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 159 | `MainABVolumeRatio` | 主力主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 160 | `MainASVolumeRatio` | 主力主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 161 | `MainNABValueRatio` | 主力净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 162 | `MainNABVFloatMVRatio` | 主力净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 163 | `MainNABVolumeRatio` | 主力净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 164 | `MainNABVFloatSRatio` | 主力净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 165 | `TotalBuyValue` | 全单流入额(元) | number(19,4) | ✓ | 100.0% | 全单=小单+中单+大单+超大单 |
| 166 | `TotalSellValue` | 全单流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 167 | `TotalBuyVolume` | 全单流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 168 | `TotalSellVolume` | 全单流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 169 | `TotalBuyNum` | 全单流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 170 | `TotalSellNum` | 全单流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 171 | `TotalNetBuyValue` | 全单净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 172 | `TotalNetBuyVolume` | 全单净流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 173 | `TotalBValueRatio` | 全单买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 174 | `TotalSValueRatio` | 全单卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 175 | `TotalBVolumeRatio` | 全单买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 176 | `TotalSVolumeRatio` | 全单卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 177 | `TotalNBValueRatio` | 全单净买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 178 | `TotalNBVFloatMVRatio` | 全单净买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 179 | `TotalNBVolumeRatio` | 全单净买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 180 | `TotalNBVFloatSRatio` | 全单净买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 181 | `TotalActBuyValue` | 全单主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 182 | `TotalActSellValue` | 全单主动流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 183 | `TotalActBuyVolume` | 全单主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 184 | `TotalActSellVolume` | 全单主动流出量(股) | number(19,4) | ✓ | 100.0% |  |
| 185 | `TotalActBuyNum` | 全单主动流入笔数 | number(19,4) | ✓ | 100.0% |  |
| 186 | `TotalActSellNum` | 全单主动流出笔数 | number(19,4) | ✓ | 100.0% |  |
| 187 | `TotalNetActBuyValue` | 全单净主动流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 188 | `TotalNetActBuyVolume` | 全单净主动流入量(股) | number(19,4) | ✓ | 100.0% |  |
| 189 | `TotalABValueRatio` | 全单主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 190 | `TotalASValueRatio` | 全单主动卖出率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 191 | `TotalABVolumeRatio` | 全单主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 192 | `TotalASVolumeRatio` | 全单主动卖出率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 193 | `TotalNABValueRatio` | 全单净主动买入率(额)(%) | number(19,4) | ✓ | 99.94% |  |
| 194 | `TotalNABVFloatMVRatio` | 全单净主动买入额流通市值比(%) | number(19,4) | ✓ | 100.0% |  |
| 195 | `TotalNABVolumeRatio` | 全单净主动买入率(量)(%) | number(19,4) | ✓ | 99.94% |  |
| 196 | `TotalNABVFloatSRatio` | 全单净主动买入量流通股本比(%) | number(19,4) | ✓ | 100.0% |  |
| 197 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 198 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 199 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

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
-- 查询 境内股票交易资金流向指标 数据
SELECT *
FROM cs_stockcapflowindex
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
