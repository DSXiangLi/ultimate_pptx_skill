# CS_HKStockPerformance

**中文名**: 港股行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_HKStockPerformance` |
| MySQL表名 | `cs_hkstockperformance` |
| 中文名 | 港股行情表现 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 169 |
| 版本 | 1 |

## 表描述

1.内容说明：
收录股票从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、上市以来的表现情况，本表包含停牌数据。
2.数据范围：2005年至今。
3.数据来源：根据港交所披露数据聚源衍生计算。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `CurrencyUnitCode` | 货币代码 | number(10) | ✓ | 100.0% | 货币代码(CurrencyUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AN... |
| 5 | `PrevClosePrice` | 昨收盘 | number(19,4) | ✓ | 100.0% |  |
| 6 | `OpenPrice` | 今开盘 | number(19,4) | ✓ | 100.0% |  |
| 7 | `HighPrice` | 最高价 | number(19,4) | ✓ | 99.99% |  |
| 8 | `LowPrice` | 最低价 | number(19,4) | ✓ | 99.99% |  |
| 9 | `ClosePrice` | 收盘价 | number(19,4) | ✓ | 100.0% |  |
| 10 | `TurnoverVolume` | 成交量 | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `ChangeOF` | 涨跌 | number(19,4) | ✓ | 100.0% |  |
| 13 | `ChangePCT` | 涨跌幅(%) | number(19,4) | ✓ | 99.99% |  |
| 14 | `RangePCT` | 振幅(%) | number(19,4) | ✓ | 99.99% |  |
| 15 | `TurnoverRate` | 换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 16 | `AvgPrice` | 均价 | number(19,4) | ✓ | 100.0% |  |
| 17 | `TotalMV` | 总市值(元) | number(19,4) | ✓ | 100.0% |  |
| 18 | `NegotiableMV` | 流通市值(不含限售股)(元) | number(19,4) | ✓ | 100.0% |  |
| 19 | `TurnoverValueRW` | 近一周成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `TurnoverVolumeRW` | 近一周成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 21 | `ChangeOFRW` | 近一周涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 22 | `ChangePCTRW` | 近一周涨跌幅(%) | number(19,4) | ✓ | 98.9% |  |
| 23 | `RangePCTRW` | 近一周振幅(%) | number(19,4) | ✓ | 98.9% |  |
| 24 | `TurnoverRateRW` | 近一周换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 25 | `AvgPriceRW` | 近一周成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 26 | `HighPriceRW` | 近一周最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 27 | `LowPriceRW` | 近一周最低价(元) | number(19,4) | ✓ | 99.99% |  |
| 28 | `HighestClosePriceRW` | 近一周收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 29 | `LowestClosePriceRW` | 近一周收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 30 | `TurnoverValuePerDayRW` | 近一周日均成交金额(元) | number(19,4) | ✓ | 92.68% |  |
| 31 | `TurnoverRatePerDayRW` | 近一周日均换手率(%) | number(19,4) | ✓ | 92.68% |  |
| 32 | `TurnVolumePerDayRW` | 近一周日均成交量(股) | number(19,4) | ✓ | 92.68% |  |
| 33 | `ChangePCTPerDayRW` | 近一周日均涨跌幅(%) | number(19,4) | ✓ | 92.67% |  |
| 34 | `RangePCTPerDayRW` | 近一周日均振幅(%) | number(19,4) | ✓ | 92.67% |  |
| 35 | `TotalMVPerDayRW` | 近一周日均总市值(元) | number(19,4) | ✓ | 92.68% |  |
| 36 | `NegotiableMVPerDayRW` | 近一周日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 92.68% |  |
| 37 | `TurnoverValueTW` | 本周以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 38 | `TurnoverVolumeTW` | 本周以来成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 39 | `ChangeOFTW` | 本周以来涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 40 | `ChangePCTTW` | 本周以来涨跌幅(%) | number(19,4) | ✓ | 98.91% |  |
| 41 | `RangePCTTW` | 本周以来振幅(%) | number(19,4) | ✓ | 98.91% |  |
| 42 | `TurnoverRateTW` | 本周以来换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 43 | `AvgPriceTW` | 本周以来成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 44 | `HighPriceTW` | 本周以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 45 | `LowPriceTW` | 本周以来最低价(元) | number(19,4) | ✓ | 99.99% |  |
| 46 | `HighestClosePriceTW` | 本周以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 47 | `LowestClosePriceTW` | 本周以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 48 | `TurnoverValuePerDayTW` | 本周以来日均成交金额(元) | number(19,4) | ✓ | 89.05% |  |
| 49 | `TurnoverRatePerDayTW` | 本周以来日均换手率(%) | number(19,4) | ✓ | 89.05% |  |
| 50 | `TurnVolumePerDayTW` | 本周以来日均成交量(股) | number(19,4) | ✓ | 89.05% |  |
| 51 | `ChangePCTPerDayTW` | 本周以来日均涨跌幅(%) | number(19,4) | ✓ | 89.04% |  |
| 52 | `RangePCTPerDayTW` | 本周以来日均振幅(%) | number(19,4) | ✓ | 89.04% |  |
| 53 | `TotalMVPerDayTW` | 本周以来日均总市值(元) | number(19,4) | ✓ | 89.05% |  |
| 54 | `NegotiableMVPerDayTW` | 本周以来日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 89.05% |  |
| 55 | `TurnoverValueRM` | 近一月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 56 | `TurnoverVolumeRM` | 近一月成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 57 | `ChangeOFRM` | 近一月涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 58 | `ChangePCTRM` | 近一月涨跌幅(%) | number(19,4) | ✓ | 98.9% |  |
| 59 | `RangePCTRM` | 近一月振幅(%) | number(19,4) | ✓ | 98.9% |  |
| 60 | `TurnoverRateRM` | 近一月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 61 | `AvgPriceRM` | 近一月成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 62 | `HighPriceRM` | 近一月最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 63 | `LowPriceRM` | 近一月最低价(元) | number(19,4) | ✓ | 99.97% |  |
| 64 | `HighestClosePriceRM` | 近一月收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 65 | `LowestClosePriceRM` | 近一月收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 66 | `TurnoverValuePerDayRM` | 近一月日均成交金额(元) | number(19,4) | ✓ | 95.73% |  |
| 67 | `TurnoverRatePerDayRM` | 近一月日均换手率(%) | number(19,4) | ✓ | 95.73% |  |
| 68 | `TurnVolumePerDayRM` | 近一月日均成交量(股) | number(19,4) | ✓ | 95.73% |  |
| 69 | `ChangePCTPerDayRM` | 近一月日均涨跌幅(%) | number(19,4) | ✓ | 95.73% |  |
| 70 | `RangePCTPerDayRM` | 近一月日均振幅(%) | number(19,4) | ✓ | 95.73% |  |
| 71 | `TotalMVPerDayRM` | 近一月日均总市值(元) | number(19,4) | ✓ | 95.73% |  |
| 72 | `NegotiableMVPerDayRM` | 近一月日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 95.73% |  |
| 73 | `TurnoverValueTM` | 本月以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 74 | `TurnoverVolumeTM` | 本月以来成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 75 | `ChangeOFTM` | 本月以来涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 76 | `ChangePCTTM` | 本月以来涨跌幅(%) | number(19,4) | ✓ | 98.9% |  |
| 77 | `RangePCTTM` | 本月以来振幅(%) | number(19,4) | ✓ | 98.9% |  |
| 78 | `TurnoverRateTM` | 本月以来换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 79 | `AvgPriceTM` | 本月以来成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 80 | `HighPriceTM` | 本月以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 81 | `LowPriceTM` | 本月以来最低价(元) | number(19,4) | ✓ | 99.98% |  |
| 82 | `HighestClosePriceTM` | 本月以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 83 | `LowestClosePriceTM` | 本月以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 84 | `TurnoverValuePerDayTM` | 本月以来日均成交金额(元) | number(19,4) | ✓ | 93.56% |  |
| 85 | `TurnoverRatePerDayTM` | 本月以来日均换手率(%) | number(19,4) | ✓ | 93.56% |  |
| 86 | `TurnVolumePerDayTM` | 本月以来日均成交量(股) | number(19,4) | ✓ | 93.56% |  |
| 87 | `ChangePCTPerDayTM` | 本月以来日均涨跌幅(%) | number(19,4) | ✓ | 93.55% |  |
| 88 | `RangePCTPerDayTM` | 本月以来日均振幅(%) | number(19,4) | ✓ | 93.55% |  |
| 89 | `TotalMVPerDayTM` | 本月以来日均总市值(元) | number(19,4) | ✓ | 93.56% |  |
| 90 | `NegotiableMVPerDayTM` | 本月以来日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 93.56% |  |
| 91 | `TurnoverValueRMThree` | 近三个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 92 | `TurnoverVolumeRMThree` | 近三个月成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 93 | `ChangeOFRMThree` | 近三个月涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 94 | `ChangePCTRMThree` | 近三个月涨跌幅(%) | number(19,4) | ✓ | 98.92% |  |
| 95 | `RangePCTRMThree` | 近三个月振幅(%) | number(19,4) | ✓ | 98.92% |  |
| 96 | `TurnoverRateRMThree` | 近三个月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 97 | `AvgPriceRMThree` | 近三个月成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 98 | `HighPriceRMThree` | 近三个月以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 99 | `LowPriceRMThree` | 近三个月以来最低价(元) | number(19,4) | ✓ | 99.95% |  |
| 100 | `HighestClosePRMThree` | 近三个月以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 101 | `LowestClosePRMThree` | 近三个月以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 102 | `TurnValuePDayRMThree` | 近三个月日均成交金额(元) | number(19,4) | ✓ | 96.56% |  |
| 103 | `TurnRatePDayRMThree` | 近三个月日均换手率(%) | number(19,4) | ✓ | 96.56% |  |
| 104 | `TurnVolumePDayRMThree` | 近三个月日均成交量(股) | number(19,4) | ✓ | 96.56% |  |
| 105 | `ChangePCTPDayRMThree` | 近三个月日均涨跌幅(%) | number(19,4) | ✓ | 96.55% |  |
| 106 | `RangePCTPDayRMThree` | 近三个月日均振幅(%) | number(19,4) | ✓ | 96.55% |  |
| 107 | `TotalMVPerDayRMThree` | 近三个月日均总市值(元) | number(19,4) | ✓ | 96.56% |  |
| 108 | `NegotiableMVPRMThree` | 近三个月日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 96.56% |  |
| 109 | `TurnoverValueRMSix` | 近六个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 110 | `TurnoverVolumeRMSix` | 近六个月成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 111 | `ChangeOFRMSix` | 近六个月涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 112 | `ChangePCTRMSix` | 近六个月涨跌幅(%) | number(19,4) | ✓ | 98.94% |  |
| 113 | `RangePCTRMSix` | 近六个月振幅(%) | number(19,4) | ✓ | 98.94% |  |
| 114 | `TurnoverRateRMSix` | 近六个月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 115 | `AvgPriceRMSix` | 近六个月成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 116 | `HighPriceRMSix` | 近六个月以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 117 | `LowPriceRMSix` | 近六个月以来最低价(元) | number(19,4) | ✓ | 99.92% |  |
| 118 | `HighestClosePRMSix` | 近六个月以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 119 | `LowestClosePRMSix` | 近六个月以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 120 | `TurnValuePDayRMSix` | 近六个月日均成交金额(元) | number(19,4) | ✓ | 97.09% |  |
| 121 | `TurnRatePDayRMSix` | 近六个月日均换手率(%) | number(19,4) | ✓ | 97.09% |  |
| 122 | `TurnVolumePDayRMSix` | 近六个月日均成交量(股) | number(19,4) | ✓ | 97.09% |  |
| 123 | `ChangePCTPDayRMSix` | 近六个月日均涨跌幅(%) | number(19,4) | ✓ | 97.09% |  |
| 124 | `RangePCTPDayRMSix` | 近六个月日均振幅(%) | number(19,4) | ✓ | 97.09% |  |
| 125 | `TotalMVPerDayRMSix` | 近六个月日均总市值(元) | number(19,4) | ✓ | 97.09% |  |
| 126 | `NegotiableMVPRMSix` | 近六个月日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 97.09% |  |
| 127 | `TurnoverValueRY` | 近一年成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 128 | `TurnoverVolumeRY` | 近一年成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 129 | `ChangeOFRY` | 近一年涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 130 | `ChangePCTRY` | 近一年涨跌幅(%) | number(19,4) | ✓ | 99.0% |  |
| 131 | `RangePCTRY` | 近一年振幅(%) | number(19,4) | ✓ | 99.0% |  |
| 132 | `TurnoverRateRY` | 近一年换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 133 | `AvgPriceRY` | 近一年成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 134 | `HighPriceRY` | 近一年最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 135 | `LowPriceRY` | 近一年最低价(元) | number(19,4) | ✓ | 99.88% |  |
| 136 | `HighestClosePRY` | 近一年收盘价最高(元) | number(19,4) | ✓ | 100.0% |  |
| 137 | `LowestClosePRY` | 近一年收盘价最低(元) | number(19,4) | ✓ | 100.0% |  |
| 138 | `TurnoverValuePDayRY` | 近一年日均成交金额(元) | number(19,4) | ✓ | 97.86% |  |
| 139 | `TurnoverRatePDayRY` | 近一年日均换手率(%) | number(19,4) | ✓ | 97.86% |  |
| 140 | `TurnVolumePDayRY` | 近一年日均成交量(股) | number(19,4) | ✓ | 97.86% |  |
| 141 | `ChangePCTPDayRY` | 近一年日均涨跌幅(%) | number(19,4) | ✓ | 97.85% |  |
| 142 | `RangePCTPDayRY` | 近一年日均振幅(%) | number(19,4) | ✓ | 97.85% |  |
| 143 | `TotalMVPerDayRY` | 近一年日均总市值(元) | number(19,4) | ✓ | 97.86% |  |
| 144 | `NegotiableMVPRY` | 近一年日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 97.86% |  |
| 145 | `TurnoverValueYTD` | 今年以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 146 | `TurnoverVolumeYTD` | 今年以来成交量(股) | number(19,4) | ✓ | 100.0% |  |
| 147 | `ChangeOFYTD` | 今年以来涨跌(元) | number(19,4) | ✓ | 100.0% |  |
| 148 | `ChangePCTYTD` | 今年以来涨跌幅(%) | number(19,4) | ✓ | 98.93% |  |
| 149 | `RangePCTYTD` | 今年以来振幅(%) | number(19,4) | ✓ | 98.93% |  |
| 150 | `TurnoverRateYTD` | 今年以来换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 151 | `AvgPriceYTD` | 今年以来成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 152 | `HighPriceYTD` | 今年以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 153 | `LowPriceYTD` | 今年以来最低价(元) | number(19,4) | ✓ | 99.92% |  |
| 154 | `HighestClosePriceYTD` | 今年以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 155 | `LowestClosePriceYTD` | 今年以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 156 | `TurnoverValuePerDayYTD` | 今年以来日均成交金额(元) | number(19,4) | ✓ | 96.94% |  |
| 157 | `TurnoverRatePerDayYTD` | 今年以来日均换手率(%) | number(19,4) | ✓ | 96.94% |  |
| 158 | `TurnVolumePDayYTD` | 今年以来日均成交量(股) | number(19,4) | ✓ | 96.94% |  |
| 159 | `ChangePCTPerDayYTD` | 今年以来日均涨跌幅(%) | number(19,4) | ✓ | 96.93% |  |
| 160 | `RangePCTPerDayYTD` | 今年以来日均振幅(%) | number(19,4) | ✓ | 96.93% |  |
| 161 | `TotalMVPerDayYTD` | 今年以来日均总市值(元) | number(19,4) | ✓ | 96.94% |  |
| 162 | `NegotiableMVPYTD` | 今年以来日均流通市值(不含限售股)(元) | number(19,4) | ✓ | 96.94% |  |
| 163 | `HighAdjustedPrice` | 上市以来复权最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 164 | `HighAdjustedPriceDate` | 上市以来复权最高价日期 | date | ✓ | 100.0% |  |
| 165 | `LowAdjustedPrice` | 上市以来复权最低价(元) | number(19,4) | ✓ | 99.95% |  |
| 166 | `LowAdjustedPriceDate` | 上市以来复权最低价日期 | date | ✓ | 100.0% |  |
| 167 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 168 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 169 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CurrencyUnitCode (货币代码)

货币代码(CurrencyUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM IN (1000,1100,1420)，得到货币代码的具体描述：1000-美元，1100-港元，1420-人民币元。

## SQL示例

```sql
-- 查询 港股行情表现 数据
SELECT *
FROM cs_hkstockperformance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
