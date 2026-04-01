# CS_StockPatterns

**中文名**: 股票技术形态表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockPatterns` |
| MySQL表名 | `cs_stockpatterns` |
| 中文名 | 股票技术形态表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 78 |
| 版本 | 1.01 |

## 表描述

内容说明：收录股票从最近一个交易日往前追溯一段时期的行情表现和技术形态表现，包括近1周、近1月、近3月、近半年、近1年、上市以来的表现情况，以及连涨跌天数、连续放量缩量天数、向上向下有效突破均线、N天M板、均线多空头排列看涨看跌等技术形态指标。 本表覆盖的证券品种有A股、B股、中国存托凭证(CDR), 覆盖的上市标志有主板、三板、创业板、科创板。
数据范围：股票上市或挂牌起-至今
信息来源：基于沪深京交易所及股转系统行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `GilCode` | 聚源代码 | varchar2(12) | ✗ | 100.0% |  |
| 5 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% |  |
| 6 | `IfHighestHPriceRW` | 是否创近一周的新高 | number(10) | ✓ | 100.0% | 指定日期最高价是否大于指定日期最近N天最高价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 7 | `IfHighestHPriceRM` | 是否创近一月的新高 | number(10) | ✓ | 100.0% |  |
| 8 | `IfHighestHPriceRMThree` | 是否创近一季度的新高 | number(10) | ✓ | 100.0% |  |
| 9 | `IfHighestHPriceRMSix` | 是否创近半年的新高 | number(10) | ✓ | 100.0% |  |
| 10 | `IfHighestHPriceRY` | 是否创近一年的新高 | number(10) | ✓ | 100.0% |  |
| 11 | `IfHighestHPriceSL` | 是否创上市以来的新高 | number(10) | ✓ | 100.0% |  |
| 12 | `IfHighestCPriceRW` | 是否创近一周的新高收盘价 | number(10) | ✓ | 100.0% | 指定日期收盘价是否大于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 13 | `IfHighestCPriceRM` | 是否创近一月的新高收盘价 | number(10) | ✓ | 100.0% |  |
| 14 | `IfHighestCPriceRMThree` | 是否创近一季度的新高收盘价 | number(10) | ✓ | 100.0% |  |
| 15 | `IfHighestCPriceRMSix` | 是否创近半年的新高收盘价 | number(10) | ✓ | 100.0% |  |
| 16 | `IfHighestCPriceRY` | 是否创近一年的新高收盘价 | number(10) | ✓ | 100.0% |  |
| 17 | `IfHighestCPriceSL` | 是否创上市以来的新高收盘价 | number(10) | ✓ | 100.0% |  |
| 18 | `IfHighestTVolumeRW` | 是否创近一周的新高成交量 | number(10) | ✓ | 100.0% | 指定日期成交量是否大于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 19 | `IfHighestTVolumeRM` | 是否创近一月的新高成交量 | number(10) | ✓ | 100.0% |  |
| 20 | `IfHighestTVRMThree` | 是否创近一季度的新高成交量 | number(10) | ✓ | 100.0% |  |
| 21 | `IfHighestTVolumeRMSix` | 是否创近半年的新高成交量 | number(10) | ✓ | 100.0% |  |
| 22 | `IfHighestTVolumeRY` | 是否创近一年的新高成交量 | number(10) | ✓ | 100.0% |  |
| 23 | `IfHighestTVolumeSL` | 是否创上市以来的新高成交量 | number(10) | ✓ | 100.0% |  |
| 24 | `IfHighestTValueRW` | 是否创近一周的新高成交金额 | number(10) | ✓ | 100.0% | 指定日期成交金额是否大于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年... |
| 25 | `IfHighestTValueRM` | 是否创近一月的新高成交金额 | number(10) | ✓ | 100.0% |  |
| 26 | `IfHighestTValueRMThree` | 是否创近一季度的新高成交金额 | number(10) | ✓ | 100.0% |  |
| 27 | `IfHighestTValueRMSix` | 是否创近半年的新高成交金额 | number(10) | ✓ | 100.0% |  |
| 28 | `IfHighestTValueRY` | 是否创近一年的新高成交金额 | number(10) | ✓ | 100.0% |  |
| 29 | `IfHighestTValueSL` | 是否创上市以来的新高成交金额 | number(10) | ✓ | 100.0% |  |
| 30 | `HighestHPTimesSL` | 最新交易日创历史新高次数 | number(10) | ✓ | 100.0% | 指定日期最近N天内大于指定日期之前的历史交易日最高价的次数。 N: 最新交易日、近1周、近1月、近3月、近半年、近1年 |
| 31 | `HighestHPTimesRW` | 最近一周创历史新高次数 | number(10) | ✓ | 100.0% |  |
| 32 | `HighestHPTimesRM` | 最近一月创历史新高次数 | number(10) | ✓ | 100.0% |  |
| 33 | `HighestHPTimesRMThree` | 最近一季度创历史新高次数 | number(10) | ✓ | 100.0% |  |
| 34 | `HighestHPTimesRMSix` | 最近半年创历史新高次数 | number(10) | ✓ | 100.0% |  |
| 35 | `HighestHPTimesRY` | 最近一年创历史新高次数 | number(10) | ✓ | 100.0% |  |
| 36 | `IfLowestLPriceRW` | 是否创近一周的新低 | number(10) | ✓ | 100.0% | 指定日期最低价是否小于指定日期最近N天最低价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 37 | `IfLowestLPriceRM` | 是否创近一个月的新低 | number(10) | ✓ | 100.0% |  |
| 38 | `IfLowestLPRMThree` | 是否创近一季度的新低 | number(10) | ✓ | 100.0% |  |
| 39 | `IfLowestLPriceRMSix` | 是否创近半年的新低 | number(10) | ✓ | 100.0% |  |
| 40 | `IfLowestLPriceRY` | 是否创近一年的新低 | number(10) | ✓ | 100.0% |  |
| 41 | `IfLowestLPriceSL` | 是否创上市以来的新低 | number(10) | ✓ | 100.0% |  |
| 42 | `IfLowestClosePriceRW` | 是否创近一周的新低收盘价 | number(10) | ✓ | 100.0% | 指定日期收盘价是否小于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 43 | `IfLowestClosePriceRM` | 是否创近一月的新低收盘价 | number(10) | ✓ | 100.0% |  |
| 44 | `IfLowestCPriceRMThree` | 是否创近一季度的新低收盘价 | number(10) | ✓ | 100.0% |  |
| 45 | `IfLowestCPriceRMSix` | 是否创近半年的新低收盘价 | number(10) | ✓ | 100.0% |  |
| 46 | `IfLowestClosePriceRY` | 是否创近一年的新低收盘价 | number(10) | ✓ | 100.0% |  |
| 47 | `IfLowestClosePriceSL` | 是否创上市以来的新低收盘价 | number(10) | ✓ | 100.0% |  |
| 48 | `IfLowestTVolumeRW` | 是否创近一周的新低成交量 | number(10) | ✓ | 100.0% | 指定日期成交量是否小于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、... |
| 49 | `IfLowestTVolumeRM` | 是否创近一月的新低成交量 | number(10) | ✓ | 100.0% |  |
| 50 | `IfLowestTVolumeRMThree` | 是否创近一季度的新低成交量 | number(10) | ✓ | 100.0% |  |
| 51 | `IfLowestVolumeRMSix` | 是否创近半年的新低成交量 | number(10) | ✓ | 100.0% |  |
| 52 | `IfLowestTVolumeRY` | 是否创近一年的新低成交量 | number(10) | ✓ | 100.0% |  |
| 53 | `IfLowestTVolumeSL` | 是否创上市以来的新低成交量 | number(10) | ✓ | 100.0% |  |
| 54 | `IfLowestTValueRW` | 是否创近一周的新低成交金额 | number(10) | ✓ | 100.0% | 指定日期成交金额是否小于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年... |
| 55 | `IfLowestTValueRM` | 是否创近一月的新低成交金额 | number(10) | ✓ | 100.0% |  |
| 56 | `IfLowestTValueRMThree` | 是否创近一季度的新低成交金额 | number(10) | ✓ | 100.0% |  |
| 57 | `IfLowestTValueRMSix` | 是否创近半年的新低成交金额 | number(10) | ✓ | 100.0% |  |
| 58 | `IfLowestTValueRY` | 是否创近一年的新低成交金额 | number(10) | ✓ | 100.0% |  |
| 59 | `IfLowestTValueSL` | 是否创上市以来的新低成交金额 | number(10) | ✓ | 100.0% |  |
| 60 | `LowestLowPriceTimesSL` | 最新交易日创历史新低次数 | number(10) | ✓ | 100.0% | 指定日期最近N天内小于指定日期之前的历史交易日最低价的次数， N: 最新交易日、近1周、近1月、近3月、近半年、近1年。... |
| 61 | `LowestLowPriceTimesRW` | 最近一周创历史新低次数 | number(10) | ✓ | 100.0% |  |
| 62 | `LowestLowPriceTimesRM` | 最近一个月创历史新低次数 | number(10) | ✓ | 100.0% |  |
| 63 | `LowestLPTimesRMThree` | 最近一季度创历史新低次数 | number(10) | ✓ | 100.0% |  |
| 64 | `LowestLPTimesRMSix` | 最近半年创历史新低次数 | number(10) | ✓ | 100.0% |  |
| 65 | `LowestLPTimesRY` | 最近一年创历史新低次数 | number(10) | ✓ | 100.0% |  |
| 66 | `RisingUpDays` | 连涨天数 | number(10) | ✓ | 100.0% | 统计个股在指定交易日期往前推连续上涨的天数。 |
| 67 | `FallingDownDays` | 连跌天数 | number(10) | ✓ | 100.0% | 统计个股在指定交易日期往前推连续下跌的天数。 |
| 68 | `VolumeRisingUpDays` | 连续放量天数 | number(10) | ✓ | 100.0% | 统计个股在指定交易日期往前推成交量连续上升的天数。 |
| 69 | `VolumeFallingDownDays` | 连续缩量天数 | number(10) | ✓ | 100.0% | 统计个股在指定交易日期往前推成交量连续下降的天数。 |
| 70 | `BreakingMAverageFive` | 向上向下有效突破5日均线 | number(10) | ✓ | 100.0% | 向上有效突破： 最近N天的收盘价>n日均线，且距今N+1天的收盘价<=n日均线。 向下有效突破： 最近N天的收盘价<n日... |
| 71 | `BreakingMAverageTen` | 向上向下有效突破10日均线 | number(10) | ✓ | 100.0% |  |
| 72 | `BreakingMAverageTwenty` | 向上向下有效突破20日均线 | number(10) | ✓ | 100.0% |  |
| 73 | `BreakingMAverageSixty` | 向上向下有效突破60日均线 | number(10) | ✓ | 100.0% |  |
| 74 | `RaisingLimitInNDays` | N天M板 | varchar2(20) | ✓ | 0.74% | N天： 指定交易日往前取到连续三个非涨停的交易日的最后一个交易日的后一个交易日且该交易日涨停作为起始日期，指定交易日作为... |
| 75 | `MAverageArrangements` | 均线多空头排列看涨看跌 | number(10) | ✓ | 100.0% | 看涨：5日均线>10日均线>20日均线>60日均线，看涨返回1。  看跌：5日均线<10日均线<20日均线<60日均线，... |
| 76 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 77 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 78 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### IfHighestHPriceRW (是否创近一周的新高)

指定日期最高价是否大于指定日期最近N天最高价，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfHighestCPriceRW (是否创近一周的新高收盘价)

指定日期收盘价是否大于指定日期最近N天收盘价，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfHighestTVolumeRW (是否创近一周的新高成交量)

指定日期成交量是否大于指定日期最近N天成交量，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfHighestTValueRW (是否创近一周的新高成交金额)

指定日期成交金额是否大于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### HighestHPTimesSL (最新交易日创历史新高次数)

指定日期最近N天内大于指定日期之前的历史交易日最高价的次数。
N: 最新交易日、近1周、近1月、近3月、近半年、近1年

### IfLowestLPriceRW (是否创近一周的新低)

指定日期最低价是否小于指定日期最近N天最低价，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfLowestClosePriceRW (是否创近一周的新低收盘价)

指定日期收盘价是否小于指定日期最近N天收盘价，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfLowestTVolumeRW (是否创近一周的新低成交量)

指定日期成交量是否小于指定日期最近N天成交量，是返回1， 否返回2。
N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

### IfLowestTValueRW (是否创近一周的新低成交金额)

指定日期成交金额是否小于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。

## SQL示例

```sql
-- 查询 股票技术形态表 数据
SELECT *
FROM cs_stockpatterns
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
