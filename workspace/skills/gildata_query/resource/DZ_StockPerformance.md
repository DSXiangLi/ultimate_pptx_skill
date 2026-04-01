# DZ_StockPerformance

**中文名**: 股票行情表现(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_StockPerformance` |
| MySQL表名 | `dz_stockperformance` |
| 中文名 | 股票行情表现(新) |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 136 |
| 版本 | 1 |

## 表描述

说明:
1.内容说明：
收录股票从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、上市以来的表现情况，以及β、α、波动率、夏普比率等风险指标，本表包含停牌数据。
计算方法：
1)区间成交金额＝∑区间每个交易日成交金额
2)区间成交量＝∑区间每个交易日成交量
3)区间涨跌幅＝(区间内最新复权收盘价/区间首日复权昨收盘－1)*100
4)区间振幅＝(区间最高复权价－区间最低复权家价)/区间首日复权昨收盘*100
5)区间换手率＝区间每一天换手率的合计值
6) 区间成交均价＝区间成交金额之和/区间成交量之和（考虑了区间有除权的情况）
7) 区间日均成交金额＝区间成交金额之和/区间实际交易天数
8) 区间日均换手率＝区间每日换手率之和/区间实际交易天数
2.数据范围：股票上市起-至今
3.信息来源：基于沪深京交易所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `Ifsuspend` | 是否停牌 | number(10) | ✓ | 100.0% | 非科创板：1：当日停牌；0：当日非停牌；科创板：1：当日停牌；2：当日非停牌 |
| 5 | `PrevClosePrice` | 昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `OpenPrice` | 今开盘(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `HighPrice` | 最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `LowPrice` | 最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `TurnoverVolume` | 成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `ChangePCT` | 涨跌幅(%) | number(18,4) | ✓ | 100.0% |  |
| 13 | `RangePCT` | 振幅(%) | number(18,4) | ✓ | 100.0% |  |
| 14 | `TurnoverRate` | 换手率(%) | number(18,4) | ✓ | 100.0% |  |
| 15 | `TurnoverRateFreeFloat` | 换手率_自由流通股本(%) | number(18,4) | ✓ | 100.0% |  |
| 16 | `AvgPrice` | 均价(元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `TurnoverValueRW` | 周成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 18 | `TurnoverVolumeRW` | 周成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 19 | `ChangePCTRW` | 周涨跌幅(%) | number(18,4) | ✓ | 99.85% |  |
| 20 | `RangePCTRW` | 周振幅(%) | number(18,4) | ✓ | 99.85% |  |
| 21 | `TurnoverRateRW` | 周换手率(%) | number(18,4) | ✓ | 97.68% |  |
| 22 | `TurnoverRateFFTRW` | 周换手率_自由流通股本(%) | number(18,4) | ✓ | 79.28% |  |
| 23 | `AvgPriceRW` | 周成交均价(元) | number(19,4) | ✓ | 97.69% |  |
| 24 | `HighPriceRW` | 周最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 25 | `LowPriceRW` | 周最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 26 | `HighestClosePriceRW` | 周收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 27 | `LowestClosePriceRW` | 周收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `TurnoverValuePerDayRW` | 周日均成交金额(元) | number(19,4) | ✓ | 97.69% |  |
| 29 | `TurnoverRatePerDayRW` | 周日均换手率(%) | number(18,4) | ✓ | 97.68% |  |
| 30 | `TurnoverRatePDFFTRW` | 周日均换手率_自由流通股本(%) | number(18,4) | ✓ | 79.28% |  |
| 31 | `TurnoverValueTW` | 本周以来成交金额(元) | number(19,4) | ✓ | 99.99% |  |
| 32 | `TurnoverVolumeTW` | 本周以来成交量(股/份) | number(18,4) | ✓ | 99.99% |  |
| 33 | `ChangePCTTW` | 本周以来涨跌幅(%) | number(18,4) | ✓ | 99.91% |  |
| 34 | `RangePCTTW` | 本周以来振幅(%) | number(18,4) | ✓ | 99.91% |  |
| 35 | `TurnoverRateTW` | 本周以来换手率(%) | number(18,4) | ✓ | 97.35% |  |
| 36 | `TurnoverRateFFTTW` | 本周以来换手率_自由流通股本(%) | number(18,4) | ✓ | 79.08% |  |
| 37 | `AvgPriceTW` | 本周以来成交均价(元) | number(19,4) | ✓ | 97.36% |  |
| 38 | `HighPriceTW` | 本周以来最高价(元) | number(19,4) | ✓ | 99.99% |  |
| 39 | `LowPriceTW` | 本周以来最低价(元) | number(19,4) | ✓ | 99.99% |  |
| 40 | `HighestClosePriceTW` | 本周以来收盘最高价(元) | number(19,4) | ✓ | 99.99% |  |
| 41 | `LowestClosePriceTW` | 本周以来收盘最低价(元) | number(19,4) | ✓ | 99.99% |  |
| 42 | `TurnoverValuePerDayTW` | 本周以来日均成交金额(元) | number(19,4) | ✓ | 97.36% |  |
| 43 | `TurnoverRatePerDayTW` | 本周以来日均换手率(%) | number(18,4) | ✓ | 97.35% |  |
| 44 | `TurnoverRatePDFFTTW` | 本周以来日均换手率_自由流通股本(%) | number(18,4) | ✓ | 79.08% |  |
| 45 | `TurnoverValueRM` | 月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 46 | `TurnoverVolumeRM` | 月成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 47 | `ChangePCTRM` | 月涨跌幅(%) | number(18,4) | ✓ | 99.34% |  |
| 48 | `RangePCTRM` | 月振幅(%) | number(18,4) | ✓ | 99.34% |  |
| 49 | `TurnoverRateRM` | 月换手率(%) | number(18,4) | ✓ | 98.48% |  |
| 50 | `TurnoverRateFFTRM` | 月换手率_自由流通股本(%) | number(18,4) | ✓ | 79.85% |  |
| 51 | `AvgPriceRM` | 月成交均价(元) | number(19,4) | ✓ | 98.49% |  |
| 52 | `HighPriceRM` | 月最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 53 | `LowPriceRM` | 月最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 54 | `HighestClosePriceRM` | 月收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 55 | `LowestClosePriceRM` | 月收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 56 | `TurnoverValuePerDayRM` | 月日均成交金额(元) | number(19,4) | ✓ | 98.49% |  |
| 57 | `TurnoverRatePerDayRM` | 月日均换手率(%) | number(18,4) | ✓ | 98.48% |  |
| 58 | `TurnoverRatePDFFTRM` | 月日均换手率_自由流通股本(%) | number(18,4) | ✓ | 79.85% |  |
| 59 | `TurnoverValueTM` | 本月以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 60 | `TurnoverVolumeTM` | 本月以来成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 61 | `ChangePCTTM` | 本月以来涨跌幅(%) | number(18,4) | ✓ | 99.67% |  |
| 62 | `RangePCTTM` | 本月以来振幅(%) | number(18,4) | ✓ | 99.67% |  |
| 63 | `TurnoverRateTM` | 本月以来换手率(%) | number(18,4) | ✓ | 97.98% |  |
| 64 | `TurnoverRateFFTTM` | 本月以来换手率_自由流通股本(%) | number(18,4) | ✓ | 79.5% |  |
| 65 | `AvgPriceTM` | 本月以来成交均价(元) | number(19,4) | ✓ | 97.99% |  |
| 66 | `HighPriceTM` | 本月以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 67 | `LowPriceTM` | 本月以来最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 68 | `HighestClosePriceTM` | 本月以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 69 | `LowestClosePriceTM` | 本月以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 70 | `TurnoverValuePerDayTM` | 本月以来日均成交金额(元) | number(19,4) | ✓ | 97.99% |  |
| 71 | `TurnoverRatePerDayTM` | 本月以来日均换手率(%) | number(18,4) | ✓ | 97.98% |  |
| 72 | `TurnoverRatePDFFTTM` | 本月以来日均换手率_自由流通股本(%) | number(18,4) | ✓ | 79.5% |  |
| 73 | `TurnoverValueRMThree` | 三个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 74 | `TurnoverVolumeRMThree` | 三个月成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 75 | `ChangePCTRMThree` | 三个月涨跌幅(%) | number(18,4) | ✓ | 98.05% |  |
| 76 | `RangePCTRMThree` | 三个月振幅(%) | number(18,4) | ✓ | 98.05% |  |
| 77 | `TurnoverRateRMThree` | 三个月换手率(%) | number(18,4) | ✓ | 99.32% |  |
| 78 | `TurnoverRateFFTRMThree` | 三个月换手率_自由流通股本(%) | number(18,4) | ✓ | 80.59% |  |
| 79 | `TurnoverValueRMSix` | 六个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 80 | `TurnoverVolumeRMSix` | 六个月成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 81 | `ChangePCTRMSix` | 六个月涨跌幅(%) | number(18,4) | ✓ | 96.11% |  |
| 82 | `RangePCTRMSix` | 六个月振幅(%) | number(18,4) | ✓ | 96.11% |  |
| 83 | `TurnoverRateRMSix` | 六个月换手率(%) | number(18,4) | ✓ | 99.78% |  |
| 84 | `TurnoverRateFFTRMSix` | 六个月换手率_自由流通股本(%) | number(18,4) | ✓ | 80.99% |  |
| 85 | `TurnoverValueRY` | 十二个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 86 | `TurnoverVolumeRY` | 十二个月成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 87 | `ChangePCTRY` | 十二个月涨跌幅(%) | number(18,4) | ✓ | 92.26% |  |
| 88 | `RangePCTRY` | 十二个月振幅(%) | number(18,4) | ✓ | 92.26% |  |
| 89 | `TurnoverRateRY` | 十二个月换手率(%) | number(18,4) | ✓ | 99.92% |  |
| 90 | `TurnoverRateFFTRY` | 十二个月换手率_自由流通股本(%) | number(18,4) | ✓ | 81.09% |  |
| 91 | `AvgPriceRY` | 十二个月成交均价(元) | number(19,4) | ✓ | 99.93% |  |
| 92 | `HighPriceRY` | 十二个月最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 93 | `LowPriceRY` | 十二个月最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 94 | `HighestClosePriceRY` | 十二个月收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 95 | `LowestClosePriceRY` | 十二个月收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 96 | `TurnoverValuePDayRY` | 十二个月日均成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 97 | `TurnoverRatePDayRY` | 十二个月日均换手率(%) | number(18,4) | ✓ | 99.92% |  |
| 98 | `TurnoverRatePDFFTRY` | 十二个月日均换手率_自由流通股本(%) | number(18,4) | ✓ | 81.09% |  |
| 99 | `TurnoverValueYTD` | 今年以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 100 | `TurnoverVolumeYTD` | 今年以来成交量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 101 | `ChangePCTYTD` | 今年以来涨跌幅(%) | number(18,4) | ✓ | 96.15% |  |
| 102 | `RangePCTYTD` | 今年以来振幅(%) | number(18,4) | ✓ | 96.15% |  |
| 103 | `TurnoverRateYTD` | 今年以来换手率(%) | number(18,4) | ✓ | 99.54% |  |
| 104 | `TurnoverRateFFTYTD` | 今年以来换手率_自由流通股本(%) | number(18,4) | ✓ | 80.78% |  |
| 105 | `AvgPriceYTD` | 今年以来成交均价(元) | number(19,4) | ✓ | 99.55% |  |
| 106 | `HighPriceYTD` | 今年以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 107 | `LowPriceYTD` | 今年以来最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 108 | `HighestClosePriceYTD` | 今年以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 109 | `LowestClosePriceYTD` | 今年以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 110 | `TurnoverValuePerDayYTD` | 今年以来日均成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 111 | `TurnoverRatePerDayYTD` | 今年以来日均换手率(%) | number(18,4) | ✓ | 99.54% |  |
| 112 | `TurnoverRatePDFFTYTD` | 今年以来日均换手率_自由流通股本(%) | number(18,4) | ✓ | 80.78% |  |
| 113 | `HighAdjustedPrice` | 上市以来后复权最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 114 | `HighAdjustedPriceDate` | 上市以来后复权最高价时间 | date | ✓ | 100.0% |  |
| 115 | `LowAdjustedPrice` | 上市以来后复权最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 116 | `LowAdjustedPriceDate` | 上市以来后复权最低价时间 | date | ✓ | 100.0% |  |
| 117 | `BetaLargeCapIndex` | Beta值(相对沪深300,一年) | number(18,6) | ✓ | 81.63% |  |
| 118 | `BetaCompositeIndex` | Beta值(相对综合指数,一年) | number(18,6) | ✓ | 80.78% | 在上海交易所上市，则取沪综指；在深圳交易所上市，则取深综指。 |
| 119 | `BetaSYWGIndustryIndex` | Beta值(相对申万行业,一年) | number(18,6) | ✓ | 78.85% | 取该股票所属的申万行业指数 |
| 120 | `BetaMidCapIndex` | Beta值(相对中证500,一年) | number(18,6) | ✓ | 75.85% |  |
| 121 | `BetaWeekly` | Beta值(两年,周步长) | number(18,6) | ✓ | 84.22% | Beta值（两年,周步长）（BetaWeekly）：Beta=[n∑RXiRi-(∑RXi)*(∑Ri)]／[n∑（RX... |
| 122 | `AdjustBetaWeekly` | 调整Beta值(两年,周步长) | number(18,6) | ✓ | 84.22% | 调整Beta值（两年,周步长）（AdjustBetaWeekly）：BETA值（两年,周步长）*0.67+0.33 |
| 123 | `AlphaLargeCapIndex` | 阿尔法(相对沪深300,一年) | number(18,6) | ✓ | 81.63% |  |
| 124 | `AlphaCompositeIndex` | 阿尔法(相对综合指数,一年) | number(18,6) | ✓ | 80.78% | 在上海交易所上市，则取沪综指；在深圳交易所上市，则取深综指。 |
| 125 | `AlphaSYWGIndustryIndex` | 阿尔法(相对申万行业,一年) | number(18,6) | ✓ | 78.85% | 取该股票所属的申万行业指数。 |
| 126 | `AlphMidCapIndex` | 阿尔法(相对中证500,一年) | number(18,6) | ✓ | 75.85% |  |
| 127 | `YearVolatilityByDay` | 波动率(日步长) | number(18,6) | ✓ | 99.94% | 波动率(日步长)(YearVolatilityByDay):计算中为日步长数据，时间跨度为1年 |
| 128 | `YearVolatilityByWeek` | 波动率(周步长) | number(18,6) | ✓ | 99.88% |  |
| 129 | `YearSharpeRatio` | 夏普比率(年化) | number(18,6) | ✓ | 88.26% |  |
| 130 | `MarketIndexRORArithAvg` | 市场收益率(算术平均) | number(18,6) | ✓ | 84.77% | 市场收益率（算术平均）（MarketIndexRORArithAvg）：Rm=（Rm1+Rm2）/2Rm1为上证综指年收... |
| 131 | `MarketIndexRORGeomMean` | 市场收益率(几何平均) | number(18,6) | ✓ | 84.77% | 市场收益率（几何平均）（MarketIndexRORGeomMean）：Rm=（Rm1+Rm2）/2Rm1为上证综指年收... |
| 132 | `TotalMV` | 总市值(元) | number(19,4) | ✓ | 99.99% |  |
| 133 | `NegotiableMV` | 流通市值(不含限售股)(元) | number(19,4) | ✓ | 99.99% |  |
| 134 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 135 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 136 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### Ifsuspend (是否停牌)

非科创板：1：当日停牌；0：当日非停牌；科创板：1：当日停牌；2：当日非停牌

### BetaCompositeIndex (Beta值(相对综合指数,一年))

在上海交易所上市，则取沪综指；在深圳交易所上市，则取深综指。

### BetaSYWGIndustryIndex (Beta值(相对申万行业,一年))

取该股票所属的申万行业指数

### BetaWeekly (Beta值(两年,周步长))

Beta值（两年,周步长）（BetaWeekly）：Beta=[n∑RXiRi-(∑RXi)*(∑Ri)]／[n∑（RXi^2）-(∑RXi)^2]Ri为步长区间股票增长率Rxi为步长区间基准增长率

### AdjustBetaWeekly (调整Beta值(两年,周步长))

调整Beta值（两年,周步长）（AdjustBetaWeekly）：BETA值（两年,周步长）*0.67+0.33

### AlphaCompositeIndex (阿尔法(相对综合指数,一年))

在上海交易所上市，则取沪综指；在深圳交易所上市，则取深综指。

### AlphaSYWGIndustryIndex (阿尔法(相对申万行业,一年))

取该股票所属的申万行业指数。

### YearVolatilityByDay (波动率(日步长))

波动率(日步长)(YearVolatilityByDay):计算中为日步长数据，时间跨度为1年

### MarketIndexRORArithAvg (市场收益率(算术平均))

市场收益率（算术平均）（MarketIndexRORArithAvg）：Rm=（Rm1+Rm2）/2Rm1为上证综指年收益率（算术平均）Rm2为深证综指年收益率（算术平均）指数年平均收益率Rxi=(∑（Ri）/10)*100%

## SQL示例

```sql
-- 查询 股票行情表现(新) 数据
SELECT *
FROM dz_stockperformance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
