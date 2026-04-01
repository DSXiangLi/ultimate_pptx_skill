# LC_STIBPerformance

**中文名**: 科创板行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBPerformance` |
| MySQL表名 | `lc_stibperformance` |
| 中文名 | 科创板行情表现 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 124 |
| 版本 | 1.02 |

## 表描述

1.内容说明：展示科创板股票从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、上市以来的表现情况，以及波动率等风险指标。
2.数据范围：证券上市之日起-至今
3.信息来源：上交所每日行情收盘文件基础上进行衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `Ifsuspend` | 是否停牌 | number(10) | ✓ | 100.0% | 是否停牌(Ifsuspend)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM i... |
| 5 | `PrevClosePrice` | 昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `OpenPrice` | 今开盘(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `HighPrice` | 最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `LowPrice` | 最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `TurnoverVolume` | 成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `ChangePCT` | 涨跌幅(%) | number(19,4) | ✓ | 100.0% |  |
| 13 | `RangePCT` | 振幅(%) | number(19,4) | ✓ | 100.0% |  |
| 14 | `TurnoverRate` | 换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 15 | `TurnoverRateFreeFloat` | 换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 16 | `AvgPrice` | 成交均价(元) | number(19,4) | ✓ | 99.9% |  |
| 17 | `TurnoverValueRW` | 周成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 18 | `TurnoverVolumeRW` | 周成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 19 | `ChangePCTRW` | 周涨跌幅(%) | number(19,4) | ✓ | 99.54% |  |
| 20 | `RangePCTRW` | 周振幅(%) | number(19,4) | ✓ | 99.54% |  |
| 21 | `TurnoverRateRW` | 周换手率(%) | number(19,4) | ✓ | 99.95% |  |
| 22 | `TurnoverRateFFTRW` | 周换手率_自由流通股本(%) | number(19,4) | ✓ | 99.95% |  |
| 23 | `AvgPriceRW` | 周成交均价(元) | number(19,4) | ✓ | 99.95% |  |
| 24 | `HighPriceRW` | 周最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 25 | `LowPriceRW` | 周最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 26 | `HighestClosePriceRW` | 周收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 27 | `LowestClosePriceRW` | 周收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `TurnoverValuePerDayRW` | 周日均成交金额(元) | number(19,4) | ✓ | 99.95% |  |
| 29 | `TurnoverRatePerDayRW` | 周日均换手率(%) | number(19,4) | ✓ | 99.95% |  |
| 30 | `TurnoverRatePDFFTRW` | 周日均换手率_自由流通股本(%) | number(19,4) | ✓ | 99.95% |  |
| 31 | `TurnoverValueTW` | 本周以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 32 | `TurnoverVolumeTW` | 本周以来成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 33 | `ChangePCTTW` | 本周以来涨跌幅(%) | number(19,4) | ✓ | 99.72% |  |
| 34 | `RangePCTTW` | 本周以来振幅(%) | number(19,4) | ✓ | 99.72% |  |
| 35 | `TurnoverRateTW` | 本周以来换手率(%) | number(19,4) | ✓ | 99.92% |  |
| 36 | `TurnoverRateFFTTW` | 本周以来换手率_自由流通股本(%) | number(19,4) | ✓ | 99.92% |  |
| 37 | `AvgPriceTW` | 本周以来成交均价(元) | number(19,4) | ✓ | 99.92% |  |
| 38 | `HighPriceTW` | 本周以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 39 | `LowPriceTW` | 本周以来最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 40 | `HighestClosePriceTW` | 本周以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 41 | `LowestClosePriceTW` | 本周以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 42 | `TurnoverValuePerDayTW` | 本周以来日均成交金额(元) | number(19,4) | ✓ | 99.92% |  |
| 43 | `TurnoverRatePerDayTW` | 本周以来日均换手率(%) | number(19,4) | ✓ | 99.92% |  |
| 44 | `TurnoverRatePDFFTTW` | 本周以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 99.92% |  |
| 45 | `TurnoverValueRM` | 月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 46 | `TurnoverVolumeRM` | 月成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 47 | `ChangePCTRM` | 月涨跌幅(%) | number(19,4) | ✓ | 98.01% |  |
| 48 | `RangePCTRM` | 月振幅(%) | number(19,4) | ✓ | 98.01% |  |
| 49 | `TurnoverRateRM` | 月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 50 | `TurnoverRateFFTRM` | 月换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 51 | `AvgPriceRM` | 月成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 52 | `HighPriceRM` | 月最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 53 | `LowPriceRM` | 月最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 54 | `HighestClosePriceRM` | 月收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 55 | `LowestClosePriceRM` | 月收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 56 | `TurnoverValuePerDayRM` | 月日均成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 57 | `TurnoverRatePerDayRM` | 月日均换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 58 | `TurnoverRatePDFFTRM` | 月日均换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 59 | `TurnoverValueTM` | 本月以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 60 | `TurnoverVolumeTM` | 本月以来成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 61 | `ChangePCTTM` | 本月以来涨跌幅(%) | number(19,4) | ✓ | 99.02% |  |
| 62 | `RangePCTTM` | 本月以来振幅(%) | number(19,4) | ✓ | 99.02% |  |
| 63 | `TurnoverRateTM` | 本月以来换手率(%) | number(19,4) | ✓ | 99.96% |  |
| 64 | `TurnoverRateFFTTM` | 本月以来换手率_自由流通股本(%) | number(19,4) | ✓ | 99.96% |  |
| 65 | `AvgPriceTM` | 本月以来成交均价(元) | number(19,4) | ✓ | 99.96% |  |
| 66 | `HighPriceTM` | 本月以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 67 | `LowPriceTM` | 本月以来最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 68 | `HighestClosePriceTM` | 本月以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 69 | `LowestClosePriceTM` | 本月以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 70 | `TurnoverValuePerDayTM` | 本月以来日均成交金额(元) | number(19,4) | ✓ | 99.96% |  |
| 71 | `TurnoverRatePerDayTM` | 本月以来日均换手率(%) | number(19,4) | ✓ | 99.96% |  |
| 72 | `TurnoverRatePDFFTTM` | 本月以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 99.96% |  |
| 73 | `TurnoverValueRMThree` | 三个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 74 | `TurnoverVolumeRMThree` | 三个月成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 75 | `ChangePCTRMThree` | 三个月涨跌幅(%) | number(19,4) | ✓ | 94.2% |  |
| 76 | `RangePCTRMThree` | 三个月振幅(%) | number(19,4) | ✓ | 94.2% |  |
| 77 | `TurnoverRateRMThree` | 三个月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 78 | `TurnoverRateFFTRMThree` | 三个月换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 79 | `TurnoverValueRMSix` | 六个月成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 80 | `TurnoverVolumeRMSix` | 六个月成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 81 | `ChangePCTRMSix` | 六个月涨跌幅(%) | number(19,4) | ✓ | 88.38% |  |
| 82 | `RangePCTRMSix` | 六个月振幅(%) | number(19,4) | ✓ | 88.38% |  |
| 83 | `TurnoverRateRMSix` | 六个月换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 84 | `TurnoverRateFFTRMSix` | 六个月换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 85 | `TurnoverValueRY` | 近一年成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 86 | `TurnoverVolumeRY` | 近一年成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 87 | `ChangePCTRY` | 近一年涨跌幅(%) | number(19,4) | ✓ | 76.87% |  |
| 88 | `RangePCTRY` | 近一年振幅(%) | number(19,4) | ✓ | 76.87% |  |
| 89 | `TurnoverRateRY` | 近一年换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 90 | `TurnoverRateFFTRY` | 近一年换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 91 | `AvgPriceRY` | 近一年成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 92 | `HighPriceRY` | 近一年最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 93 | `LowPriceRY` | 近一年最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 94 | `HighestClosePriceRY` | 近一年收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 95 | `LowestClosePriceRY` | 近一年收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 96 | `TurnoverValuePDayRY` | 近一年日均成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 97 | `TurnoverRatePDayRY` | 近一年日均换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 98 | `TurnoverRatePDFFTRY` | 近一年日均换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 99 | `TurnoverValueYTD` | 今年以来成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 100 | `TurnoverVolumeYTD` | 今年以来成交量(股/份) | number(19,4) | ✓ | 100.0% |  |
| 101 | `ChangePCTYTD` | 今年以来涨跌幅(%) | number(19,4) | ✓ | 89.11% |  |
| 102 | `RangePCTYTD` | 今年以来振幅(%) | number(19,4) | ✓ | 89.11% |  |
| 103 | `TurnoverRateYTD` | 今年以来换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 104 | `TurnoverRateFFTYTD` | 今年以来换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 105 | `AvgPriceYTD` | 今年以来成交均价(元) | number(19,4) | ✓ | 100.0% |  |
| 106 | `HighPriceYTD` | 今年以来最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 107 | `LowPriceYTD` | 今年以来最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 108 | `HighestClosePriceYTD` | 今年以来收盘最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 109 | `LowestClosePriceYTD` | 今年以来收盘最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 110 | `TurnoverValuePerDayYTD` | 今年以来日均成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 111 | `TurnoverRatePerDayYTD` | 今年以来日均换手率(%) | number(19,4) | ✓ | 100.0% |  |
| 112 | `TurnoverRatePDFFTYTD` | 今年以来日均换手率_自由流通股本(%) | number(19,4) | ✓ | 100.0% |  |
| 113 | `HighAdjustedPrice` | 上市以来后复权最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 114 | `HighAdjustedPriceDate` | 上市以来后复权最高价时间 | date | ✓ | 100.0% |  |
| 115 | `LowAdjustedPrice` | 上市以来后复权最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 116 | `LowAdjustedPriceDate` | 上市以来后复权最低价时间 | date | ✓ | 100.0% |  |
| 117 | `WVolatility` | 波动率(周)(%) | number(19,4) | ✓ | 98.98% | 波动率(周)(%)（WVolatility）:计算中采用日步长数据，时间跨度为1周。 |
| 118 | `MVolatility` | 波动率(月)(%) | number(19,4) | ✓ | 99.81% | 波动率(月)(%)：计算中采用日步长数据，时间跨度为1个月。 |
| 119 | `YVolatility` | 波动率(年)(%) | number(19,4) | ✓ | 99.81% | 波动率(年)(%)：计算中采用日步长数据，时间跨度为一年。 |
| 120 | `TotalMV` | 总市值(元) | number(19,4) | ✓ | 100.0% |  |
| 121 | `NegotiableMV` | 流通市值(不含限售股)(元) | number(19,4) | ✓ | 100.0% |  |
| 122 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 123 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 124 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### Ifsuspend (是否停牌)

是否停牌(Ifsuspend)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否停牌的具体描述：1-是，2-否。

### WVolatility (波动率(周)(%))

波动率(周)(%)（WVolatility）:计算中采用日步长数据，时间跨度为1周。

### MVolatility (波动率(月)(%))

波动率(月)(%)：计算中采用日步长数据，时间跨度为1个月。

### YVolatility (波动率(年)(%))

波动率(年)(%)：计算中采用日步长数据，时间跨度为一年。

## SQL示例

```sql
-- 查询 科创板行情表现 数据
SELECT *
FROM lc_stibperformance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
