# DZ_Performance

**中文名**: 股票行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_Performance` |
| MySQL表名 | `dz_performance` |
| 中文名 | 股票行情表现 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 130 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录股票从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、上市以来的表现情况，以及β、α、波动率、夏普比率等风险指标。
计算方法：1)区间成交金额＝∑区间每个交易日成交金额 2)区间成交量＝∑区间每个交易日成交量 3)区间涨跌幅＝(区间内最新复权收盘价/区间首日复权昨收盘－1)*100 4)区间振幅＝(区间最高复权价－区间最低复权家价)/区间首日复权昨收盘*100 5)区间换手率＝区间内成交量之和/区间内最新未限售流通股*100 6) 区间成交均价＝区间成交金额之和/区间成交量之和 7) 区间日均成交金额＝区间成交金额之和/区间交易日天数 8) 区间日均换手率＝区间每日换手率之和/区间交易日天数
2.数据范围：股票上市起-至今
3.信息来源：基于沪深京交易所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 昨收盘 | number(19,4) | ✓ | 99.96% |  |
| 5 | `OpenPrice` | 今开盘 | number(19,4) | ✓ | 100.0% |  |
| 6 | `HighPrice` | 最高价 | number(19,4) | ✓ | 100.0% |  |
| 7 | `LowPrice` | 最低价 | number(19,4) | ✓ | 100.0% |  |
| 8 | `ClosePrice` | 收盘价 | number(19,4) | ✓ | 99.96% |  |
| 9 | `TurnoverVolume` | 成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 10 | `TurnoverValue` | 成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `ChangePCT` | 涨跌幅(%) | number(19,4) | ✓ | 99.96% |  |
| 12 | `RangePCT` | 振幅(%) | number(19,4) | ✓ | 99.96% |  |
| 13 | `TurnoverRate` | 换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 14 | `TurnoverRateFreeFloat` | 换手率_自由流通股本(%) | number(19,4) | ✓ | 80.84% |  |
| 15 | `AvgPrice` | 均价 | number(19,4) | ✓ | 96.42% |  |
| 16 | `TurnoverValueRW` | 周成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `TurnoverVolumeRW` | 周成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 18 | `ChangePCTRW` | 周涨跌幅(%) | number(19,4) | ✓ | 99.79% |  |
| 19 | `RangePCTRW` | 周振幅(%) | number(19,4) | ✓ | 99.79% |  |
| 20 | `TurnoverRateRW` | 周换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 21 | `TurnoverRateFFTRW` | 周换手率_自由流通股本(%) | number(19,4) | ✓ | 78.94% |  |
| 22 | `AvgPriceRW` | 周成交均价(元) | number(19,4) | ✓ | 97.34% |  |
| 23 | `HighPriceRW` | 周最高价(元) | number(19,4) | ✓ | 99.95% |  |
| 24 | `LowPriceRW` | 周最低价(元) | number(19,4) | ✓ | 97.35% |  |
| 25 | `HighestClosePriceRW` | 周收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 26 | `LowestClosePriceRW` | 周收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 27 | `TurnoverValuePerDayRW` | 周日均成交金额(万元) | number(19,4) | ✓ | 97.34% |  |
| 28 | `TurnoverRatePerDayRW` | 周日均换手率(%) | number(19,4) | ✓ | 97.31% |  |
| 29 | `TurnoverRatePDFFTRW` | 周日均换手率_自由流通股本(%) | number(19,4) | ✓ | 78.94% |  |
| 30 | `TurnoverValueTW` | 本周以来成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 31 | `TurnoverVolumeTW` | 本周以来成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 32 | `ChangePCTTW` | 本周以来涨跌幅(%) | number(19,4) | ✓ | 99.87% |  |
| 33 | `RangePCTTW` | 本周以来振幅(%) | number(19,4) | ✓ | 99.87% |  |
| 34 | `TurnoverRateTW` | 本周以来换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 35 | `TurnoverRateFFTTW` | 本周以来换手率_自由流通股本(%) | number(19,4) | ✓ | 78.68% |  |
| 36 | `AvgPriceTW` | 本周以来成交均价(元) | number(19,4) | ✓ | 96.9% |  |
| 37 | `HighPriceTW` | 本周以来最高价(元) | number(19,4) | ✓ | 99.94% |  |
| 38 | `LowPriceTW` | 本周以来最低价(元) | number(19,4) | ✓ | 96.92% |  |
| 39 | `HighestClosePriceTW` | 本周以来收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 40 | `LowestClosePriceTW` | 本周以来收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 41 | `TurnoverValuePerDayTW` | 本周以来日均成交金额(万元) | number(19,4) | ✓ | 96.9% |  |
| 42 | `TurnoverRatePerDayTW` | 本周以来日均换手率(%) | number(19,4) | ✓ | 96.88% |  |
| 43 | `TurnoverRatePDFFTTW` | 本周以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 78.68% |  |
| 44 | `TurnoverValueRM` | 月成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 45 | `TurnoverVolumeRM` | 月成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 46 | `ChangePCTRM` | 月涨跌幅(%) | number(19,4) | ✓ | 99.3% |  |
| 47 | `RangePCTRM` | 月振幅(%) | number(19,4) | ✓ | 99.3% |  |
| 48 | `TurnoverRateRM` | 月换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 49 | `TurnoverRateFFTRM` | 月换手率_自由流通股本(%) | number(19,4) | ✓ | 79.46% |  |
| 50 | `AvgPriceRM` | 月成交均价(元) | number(19,4) | ✓ | 98.08% |  |
| 51 | `HighPriceRM` | 月最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 52 | `LowPriceRM` | 月最低价(元) | number(19,4) | ✓ | 98.09% |  |
| 53 | `HighestClosePriceRM` | 月收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 54 | `LowestClosePriceRM` | 月收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 55 | `TurnoverValuePerDayRM` | 月日均成交金额(万元) | number(19,4) | ✓ | 98.08% |  |
| 56 | `TurnoverRatePerDayRM` | 月日均换手率(%) | number(19,4) | ✓ | 98.04% |  |
| 57 | `TurnoverRatePDFFTRM` | 月日均换手率_自由流通股本(%) | number(19,4) | ✓ | 79.46% |  |
| 58 | `TurnoverValueTM` | 本月以来成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 59 | `TurnoverVolumeTM` | 本月以来成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 60 | `ChangePCTTM` | 本月以来涨跌幅(%) | number(19,4) | ✓ | 99.64% |  |
| 61 | `RangePCTTM` | 本月以来振幅(%) | number(19,4) | ✓ | 99.64% |  |
| 62 | `TurnoverRateTM` | 本月以来换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 63 | `TurnoverRateFFTTM` | 本月以来换手率_自由流通股本(%) | number(19,4) | ✓ | 79.1% |  |
| 64 | `AvgPriceTM` | 本月以来成交均价(元) | number(19,4) | ✓ | 97.55% |  |
| 65 | `HighPriceTM` | 本月以来最高价(元) | number(19,4) | ✓ | 99.95% |  |
| 66 | `LowPriceTM` | 本月以来最低价(元) | number(19,4) | ✓ | 97.57% |  |
| 67 | `HighestClosePriceTM` | 本月以来收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 68 | `LowestClosePriceTM` | 本月以来收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 69 | `TurnoverValuePerDayTM` | 本月以来日均成交金额(万元) | number(19,4) | ✓ | 97.55% |  |
| 70 | `TurnoverRatePerDayTM` | 本月以来日均换手率(%) | number(19,4) | ✓ | 97.52% |  |
| 71 | `TurnoverRatePDFFTTM` | 本月以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 79.1% |  |
| 72 | `TurnoverValueR3M` | 三个月成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 73 | `TurnoverVolumeR3M` | 三个月成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 74 | `ChangePCTR3M` | 三个月涨跌幅(%) | number(19,4) | ✓ | 98.01% |  |
| 75 | `RangePCTR3M` | 三个月振幅(%) | number(19,4) | ✓ | 98.01% |  |
| 76 | `TurnoverRateR3M` | 三个月换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 77 | `TurnoverRateFFTRMThree` | 三个月换手率_自由流通股本(%) | number(19,4) | ✓ | 80.17% |  |
| 78 | `TurnoverValueR6M` | 六个月成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 79 | `TurnoverVolumeR6M` | 六个月成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 80 | `ChangePCTR6M` | 六个月涨跌幅(%) | number(19,4) | ✓ | 96.09% |  |
| 81 | `RangePCTR6M` | 六个月振幅(%) | number(19,4) | ✓ | 96.09% |  |
| 82 | `TurnoverRateR6M` | 六个月换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 83 | `TurnoverRateFFTRMSix` | 六个月换手率_自由流通股本(%) | number(19,4) | ✓ | 80.57% |  |
| 84 | `TurnoverValueR12M` | 十二个月成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 85 | `TurnoverVolumeR12M` | 十二个月成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 86 | `ChangePCTR12M` | 十二个月涨跌幅(%) | number(19,4) | ✓ | 92.26% |  |
| 87 | `RangePCTR12M` | 十二个月振幅(%) | number(19,4) | ✓ | 92.26% |  |
| 88 | `TurnoverRateR12M` | 十二个月换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 89 | `TurnoverRateFFTRY` | 十二个月换手率_自由流通股本(%) | number(19,4) | ✓ | 80.71% |  |
| 90 | `AvgPriceR12M` | 十二个月成交均价(元) | number(19,4) | ✓ | 99.69% |  |
| 91 | `HighPriceR12M` | 十二个月最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 92 | `LowPriceR12M` | 十二个月最低价(元) | number(19,4) | ✓ | 99.69% |  |
| 93 | `HighestClosePriceR12M` | 十二个月收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 94 | `LowestClosePriceR12M` | 十二个月收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 95 | `TurnoverValuePerDayR12M` | 十二个月日均成交金额(万元) | number(19,4) | ✓ | 99.69% |  |
| 96 | `TurnoverRatePerDayR12M` | 十二个月日均换手率(%) | number(19,4) | ✓ | 99.62% |  |
| 97 | `TurnoverRatePDFFTRY` | 十二个月日均换手率_自由流通股本(%) | number(19,4) | ✓ | 80.71% |  |
| 98 | `TurnoverValueYTD` | 今年以来成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 99 | `TurnoverVolumeYTD` | 今年以来成交量(万股/万份) | number(19,4) | ✓ | 100.0% |  |
| 100 | `ChangePCTYTD` | 今年以来涨跌幅(%) | number(19,4) | ✓ | 96.13% |  |
| 101 | `RangePCTYTD` | 今年以来振幅(%) | number(19,4) | ✓ | 96.13% |  |
| 102 | `TurnoverRateYTD` | 今年以来换手率(%) | number(19,4) | ✓ | 99.86% |  |
| 103 | `TurnoverRateFFTYTD` | 今年以来换手率_自由流通股本(%) | number(19,4) | ✓ | 80.4% |  |
| 104 | `AvgPriceYTD` | 今年以来成交均价(元) | number(19,4) | ✓ | 99.26% |  |
| 105 | `HighPriceYTD` | 今年以来最高价(元) | number(19,4) | ✓ | 99.98% |  |
| 106 | `LowPriceYTD` | 今年以来最低价(元) | number(19,4) | ✓ | 99.27% |  |
| 107 | `HighestClosePriceYTD` | 今年以来收盘最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 108 | `LowestClosePriceYTD` | 今年以来收盘最低价(元) | number(19,4) | ✓ | 99.96% |  |
| 109 | `TurnoverValuePerDayYTD` | 今年以来日均成交金额(万元) | number(19,4) | ✓ | 99.26% |  |
| 110 | `TurnoverRatePerDayYTD` | 今年以来日均换手率(%) | number(19,4) | ✓ | 99.2% |  |
| 111 | `TurnoverRatePDFFTYTD` | 今年以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 80.4% |  |
| 112 | `HighestAdjustedPrice` | 上市以来后复权最高价(元) | number(19,4) | ✓ | 99.96% |  |
| 113 | `HighestAdjustedPriceDate` | 上市以来后复权最高价时间 | date | ✓ | 99.96% |  |
| 114 | `BetaHS300Index` | Beta值(相对沪深300,一年) | number(19,4) | ✓ | 77.75% |  |
| 115 | `BetaCompositeIndex` | Beta值(相对综合指数,一年) | number(19,4) | ✓ | 74.89% | 参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。 |
| 116 | `BetaSYWGIndustryIndex` | Beta值(相对申万行业,一年) | number(19,4) | ✓ | 74.97% | 参考指数的取法：该股票所属的申万行业指数。 |
| 117 | `BetaWeekly2Y` | Beta值(两年,周步长) | number(19,4) | ✓ | 82.42% | Beta值（两年,周步长）（BetaWeekly2Y）：Beta=[n∑RXiRi-(∑RXi)*(∑Ri)]／[n∑（... |
| 118 | `AdjustBetaWeekly2Y` | 调整Beta值(两年,周步长) | number(19,4) | ✓ | 82.42% | 调整Beta值（两年,周步长）（AdjustBetaWeekly2Y）：BETA值（两年,周步长）*0.67+0.33 |
| 119 | `AlphaHS300Index` | Alpha(相对沪深300,一年) | number(19,4) | ✓ | 77.75% |  |
| 120 | `AlphaCompositeIndex` | Alpha(相对综合指数,一年) | number(19,4) | ✓ | 74.89% | 参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。 |
| 121 | `AlphaSYWGIndustryIndex` | Alpha(相对申万行业,一年) | number(19,4) | ✓ | 74.97% | 参考指数的取法：该股票所属的申万行业指数。 |
| 122 | `Y1Volatility` | 波动率(一年) | number(19,4) | ✓ | 88.55% | 波动率σ(一年)（Y1Volatility）:计算中为日步长数据。 |
| 123 | `Y1SharpeRatio` | 夏普比率(一年) | number(19,4) | ✓ | 81.34% |  |
| 124 | `MarketIndexROR_ArithAvg` | 市场收益率(算术平均) | number(19,4) | ✓ | 82.97% | 市场收益率（算术平均）（MarketIndexROR_ArithAvg）：Rm=（Rm1+Rm2）/2Rm1为上证指数年... |
| 125 | `MarketIndexROR_GeomMean` | 市场收益率(几何平均) | number(19,4) | ✓ | 82.97% | 市场收益率（几何平均）（MarketIndexROR_GeomMean）：Rm=（Rm1+Rm2）/2Rm1为上证指数年... |
| 126 | `TotalMV` | 总市值(万元) | number(19,4) | ✓ | 99.96% |  |
| 127 | `NegotiableMV` | 流通市值(万元) | number(19,4) | ✓ | 99.96% |  |
| 128 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 129 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 130 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### BetaCompositeIndex (Beta值(相对综合指数,一年))

参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。

### BetaSYWGIndustryIndex (Beta值(相对申万行业,一年))

参考指数的取法：该股票所属的申万行业指数。

### BetaWeekly2Y (Beta值(两年,周步长))

Beta值（两年,周步长）（BetaWeekly2Y）：Beta=[n∑RXiRi-(∑RXi)*(∑Ri)]／[n∑（RXi^2）-(∑RXi)^2]Ri为步长区间股票增长率Rxi为步长区间基准增长率

### AdjustBetaWeekly2Y (调整Beta值(两年,周步长))

调整Beta值（两年,周步长）（AdjustBetaWeekly2Y）：BETA值（两年,周步长）*0.67+0.33

### AlphaCompositeIndex (Alpha(相对综合指数,一年))

参考指数的取法：如在上海交易所上市，则是沪综指；在深圳交易所上市，则是深成指。

### AlphaSYWGIndustryIndex (Alpha(相对申万行业,一年))

参考指数的取法：该股票所属的申万行业指数。

### Y1Volatility (波动率(一年))

波动率σ(一年)（Y1Volatility）:计算中为日步长数据。

### MarketIndexROR_ArithAvg (市场收益率(算术平均))

市场收益率（算术平均）（MarketIndexROR_ArithAvg）：Rm=（Rm1+Rm2）/2Rm1为上证指数年收益率（算术平均）Rm2为深成指年收益率（算术平均）指数年平均收益率Rxi=(∑（Ri）/10)*100%

### MarketIndexROR_GeomMean (市场收益率(几何平均))

市场收益率（几何平均）（MarketIndexROR_GeomMean）：Rm=（Rm1+Rm2）/2Rm1为上证指数年收益率（几何平均）Rm2为深成指年收益率（几何平均）

## SQL示例

```sql
-- 查询 股票行情表现 数据
SELECT *
FROM dz_performance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
