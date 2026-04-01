# Index_GilPerformance

**中文名**: 聚源指数行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_GilPerformance` |
| MySQL表名 | `index_gilperformance` |
| 中文名 | 聚源指数行情表现 |
| 路径 | 聚源新版数据库 > 指数数据库 > 自编指数数据 > 衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 123 |
| 版本 | 1 |

## 表描述

1.内容说明：收录聚源自编指数从最近一个交易日往前追溯一段时期的行情表现信息，包括近1周、1周以来、近1月、1月以来、近3月、近半年、近1年、今年以来、成立以来的表现情况。
2.数据范围：指数基日-至今；覆盖全量自编指数
3.信息来源：指数行情基础上进行衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode):与"证券主表(SecuMain)"表中的"证券内部编码(InnerCode)"字段关... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `RangePCT` | 振幅(%) | number(19,4) | ✓ | 9.78% |  |
| 5 | `TurnoverRate` | 换手率(%) | number(19,4) | ✓ | 8.54% | 换手率(%)(TurnoverRate): 100*Σ成交量/Σ流通股本 |
| 6 | `TurnoverRateFreeFloat` | 换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% | 换手率_自由流通股本(%)(TurnoverRateFreeFloat): 100*Σ成交量/Σ自由流通股本 |
| 7 | `HighPriceTW` | 本周最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 8 | `LowPriceTW` | 本周最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 9 | `HighestClosePriceTW` | 本周最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `LowestClosePriceTW` | 本周最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValueTW` | 本周成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 12 | `TurnoverVolumeTW` | 本周成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 13 | `TurnoverValuePerDayTW` | 本周日均成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 14 | `ChangePCTTW` | 本周涨跌幅(%) | number(19,4) | ✓ | 99.92% |  |
| 15 | `RangePCTTW` | 本周振幅(%) | number(19,4) | ✓ | 9.78% |  |
| 16 | `TurnoverRateTW` | 本周换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 17 | `TurnoverRateFFTW` | 本周换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 18 | `TurnoverRatePerDayTW` | 本周日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 19 | `TurnoverRatePDFFTW` | 本周日均换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 20 | `HighPriceRW` | 周最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 21 | `LowPriceRW` | 周最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 22 | `HighestClosePriceRW` | 周最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 23 | `LowestClosePriceRW` | 周最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 24 | `TurnoverValueRW` | 周成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 25 | `TurnoverVolumeRW` | 周成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 26 | `TurnoverValuePerDayRW` | 周日均成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 27 | `ChangePCTRW` | 周涨跌幅(%) | number(19,4) | ✓ | 99.87% |  |
| 28 | `RangePCTRW` | 周振幅(%) | number(19,4) | ✓ | 9.78% |  |
| 29 | `TurnoverRateRW` | 周换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 30 | `TurnoverRateFFRW` | 周换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 31 | `TurnoverRatePerDayRW` | 周日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 32 | `TurnoverRatePDFFRW` | 周日均换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 33 | `HighPriceTM` | 本月最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 34 | `LowPriceTM` | 本月最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 35 | `HighestClosePriceTM` | 本月最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 36 | `LowestClosePriceTM` | 本月最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 37 | `TurnoverValueTM` | 本月成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 38 | `TurnoverVolumeTM` | 本月成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 39 | `TurnoverValuePerDayTM` | 本月日均成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 40 | `ChangePCTTM` | 本月涨跌幅(%) | number(19,4) | ✓ | 99.81% |  |
| 41 | `RangePCTTM` | 本月振幅(%) | number(19,4) | ✓ | 9.78% |  |
| 42 | `TurnoverRateTM` | 本月换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 43 | `TurnoverRateFFTM` | 本月换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 44 | `TurnoverRatePerDayTM` | 本月日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 45 | `TurnoverRatePDFFTM` | 本月日均换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 46 | `HighPriceRM` | 月最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 47 | `LowPriceRM` | 月最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 48 | `HighestClosePriceRM` | 月最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 49 | `LowestClosePriceRM` | 月最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 50 | `TurnoverValueRM` | 月成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 51 | `TurnoverVolumeRM` | 月成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 52 | `TurnoverValuePerDayRM` | 月日均成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 53 | `ChangePCTRM` | 月涨跌幅(%) | number(19,4) | ✓ | 99.47% |  |
| 54 | `RangePCTRM` | 月振幅(%) | number(19,4) | ✓ | 9.74% |  |
| 55 | `TurnoverRateRM` | 月换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 56 | `TurnoverRateFFRM` | 月换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 57 | `TurnoverRatePerDayRM` | 月日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 58 | `TurnoverRatePDFFRM` | 月日均换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 59 | `TurnoverValueRMThree` | 近三个月成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 60 | `TurnoverVolumeRMThree` | 近三个月成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 61 | `ChangePCTRMThree` | 近三个月涨跌幅(%) | number(19,4) | ✓ | 98.35% |  |
| 62 | `RangePCTRMThree` | 近三个月振幅(%) | number(19,4) | ✓ | 9.66% |  |
| 63 | `TurnoverRateRMThree` | 近三个月换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 64 | `TurnoverRateFFRMThree` | 近三个月换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 65 | `TurnoverValueRMSix` | 近六个月成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 66 | `TurnoverVolumeRMSix` | 近六个月成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 67 | `ChangePCTRMSix` | 近六个月涨跌幅(%) | number(19,4) | ✓ | 96.65% |  |
| 68 | `RangePCTRMSix` | 近六个月振幅(%) | number(19,4) | ✓ | 9.52% |  |
| 69 | `TurnoverRateRMSix` | 近六个月换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 70 | `TurnoverRateFFRMSix` | 近六个月换手率_自由流通股本(%) | number(19,4) | ✓ | 8.54% |  |
| 71 | `HighPriceYTD` | 今年以来最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 72 | `LowPriceYTD` | 今年以来最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 73 | `HighestClosePriceYTD` | 今年以来最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 74 | `LowestClosePriceYTD` | 今年以来最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 75 | `TurnoverValueYTD` | 今年以来成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 76 | `TurnoverVolumeYTD` | 今年以来成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 77 | `TurnoverValuePerDayYTD` | 今年以来日均成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 78 | `ChangePCTYTD` | 今年以来涨跌幅(%) | number(19,4) | ✓ | 97.47% |  |
| 79 | `RangePCTYTD` | 今年以来振幅(%) | number(19,4) | ✓ | 9.74% |  |
| 80 | `TurnoverRateYTD` | 今年以来换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 81 | `TurnoverRateFFYTD` | 今年以来换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 82 | `TurnoverRatePerDayYTD` | 今年以来日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 83 | `TurnoverRatePDFFYTD` | 今年以来日均换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 84 | `HighPriceRY` | 近一年最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 85 | `LowPriceRY` | 近一年最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 86 | `HighestClosePriceRY` | 近一年最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 87 | `LowestClosePriceRY` | 近一年最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 88 | `TurnoverValueRY` | 近一年成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 89 | `TurnoverVolumeRY` | 近一年成交量(股) | number(19,2) | ✓ | 9.78% |  |
| 90 | `TurnoverValuePDayRY` | 近一年日均成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 91 | `ChangePCTRY` | 近一年涨跌幅(%) | number(19,4) | ✓ | 93.24% |  |
| 92 | `RangePCTRY` | 近一年振幅(%) | number(19,4) | ✓ | 9.24% |  |
| 93 | `TurnoverRateRY` | 近一年换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 94 | `TurnoverRateFFRY` | 近一年换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 95 | `TurnoverRatePDayRY` | 近一年日均换手率(%) | number(19,4) | ✓ | 8.54% |  |
| 96 | `TurnoverRatePDFFRY` | 近一年日均换手率_自由流通股本1(%) | number(19,4) | ✓ | 8.54% |  |
| 97 | `HighPriceRTY` | 近三年最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 98 | `LowPriceRTY` | 近三年最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 99 | `HighestClosePriceRTY` | 近三年最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 100 | `LowestClosePriceRTY` | 近三年最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 101 | `TurnoverValuePDayRTY` | 近三年日均成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 102 | `ChangePCTRTY` | 近三年涨跌幅(%) | number(19,4) | ✓ | 79.97% |  |
| 103 | `HighPriceRFY` | 近五年最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 104 | `LowPriceRFY` | 近五年最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 105 | `HighestClosePriceRFY` | 近五年最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 106 | `LowestClosePriceRFY` | 近五年最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 107 | `TurnoverValuePDayRFY` | 近五年日均成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 108 | `ChangePCTRFY` | 近五年涨跌幅(%) | number(19,4) | ✓ | 67.2% |  |
| 109 | `HighPriceRTENY` | 近十年最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 110 | `LowPriceRTENY` | 近十年最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 111 | `HighestClosePriceRTENY` | 近十年最高收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 112 | `LowestClosePriceRTENY` | 近十年最低收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 113 | `TurnoverValuePDayRTENY` | 近十年日均成交金额1(元) | number(19,2) | ✓ | 9.78% |  |
| 114 | `ChangePCTRTENY` | 近十年涨跌幅(%) | number(19,4) | ✓ | 40.4% |  |
| 115 | `HighestPrice` | 上市以来最高价(元) | number(19,4) | ✓ | 9.78% |  |
| 116 | `HighestPriceDate` | 上市以来最高价时间 | date | ✓ | 9.78% |  |
| 117 | `LowestPrice` | 上市以来最低价(元) | number(19,4) | ✓ | 9.78% |  |
| 118 | `LowestPriceDate` | 上市以来最低价时间 | date | ✓ | 9.78% |  |
| 119 | `TurnoverValuePDay` | 上市以来日均成交金额(元) | number(19,2) | ✓ | 9.78% |  |
| 120 | `ChangePCT` | 上市以来涨跌幅(%) | number(19,4) | ✓ | 98.69% |  |
| 121 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 122 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 123 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode):与"证券主表(SecuMain)"表中的"证券内部编码(InnerCode)"字段关联，得到指数内部编码的具体描述：

### TurnoverRate (换手率(%))

换手率(%)(TurnoverRate): 100*Σ成交量/Σ流通股本

### TurnoverRateFreeFloat (换手率_自由流通股本(%))

换手率_自由流通股本(%)(TurnoverRateFreeFloat): 100*Σ成交量/Σ自由流通股本

## SQL示例

```sql
-- 查询 聚源指数行情表现 数据
SELECT *
FROM index_gilperformance
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
