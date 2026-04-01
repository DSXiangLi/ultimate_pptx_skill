# DZ_PerformanceData

**中文名**: 股票日行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_PerformanceData` |
| MySQL表名 | `dz_performancedata` |
| 中文名 | 股票日行情表现 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 38 |
| 版本 | 1 |

## 表描述

1.内容说明：收录股票行情表现相关的一些特色指标数据，如连涨天数、是否破发、是否破净、是否创历史新高或新低等指标，其中判断是否为历史新高或新低的价格均为后复权价格。
2.数据范围：证券上市之日起-至今
3.信息来源：基于沪深京交易所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `ChangePCT` | 涨跌幅(%) | number(18,4) | ✓ | 100.0% |  |
| 6 | `BackwardPrice` | 后复权收盘价(元) | number(19,4) | ✓ | 100.0% | 后复权收盘价(元)(BackwardPrice)=每日收盘价*精确复权因子+精确复权常数。 |
| 7 | `RisingUpDays` | 连涨天数 | number(10) | ✓ | 100.0% |  |
| 8 | `FallingDownDays` | 连跌天数 | number(10) | ✓ | 100.0% |  |
| 9 | `MaxRisingUpDays` | 历史连涨最多天数 | number(10) | ✓ | 100.0% |  |
| 10 | `MaxFallingDownDays` | 历史连跌最多天数 | number(10) | ✓ | 100.0% |  |
| 11 | `FallOnDebut` | 是否破发 | number(10) | ✓ | 99.93% | 是否破发(FallOnDebut)：0-否，1-是，该常量对应值适用于其他是否判断的字段。 |
| 12 | `FallOnNAPS` | 是否破净 | number(10) | ✓ | 99.67% | 是否破净(FallOnNAPS)：0-否，1-是，该常量对应值适用于其他是否判断的字段。 |
| 13 | `AHPremiumRate` | AH溢价率是否大于50% | number(10) | ✓ | 2.82% | AH溢价率是否大于50%(AHPremiumRate)：0-否，1-是，当为NULL时，代表该股票非AH上市股。 |
| 14 | `StockBoard` | 今日是否涨停一字板 | number(10) | ✓ | 100.0% |  |
| 15 | `LimitBoard` | 今日是否跌停一字板 | number(10) | ✓ | 100.0% |  |
| 16 | `SurgedLimit` | 今日是否涨停股 | number(10) | ✓ | 98.03% | 今日是否涨停股(SurgedLimit)：0-否，1-是，当为NULL时，代表该股票不设涨跌幅限制。 |
| 17 | `DeclineLimit` | 今日是否跌停股 | number(10) | ✓ | 97.98% | 今日是否跌停股(DeclineLimit)：0-否，1-是，当为NULL时，代表该股票不设涨跌幅限制。 |
| 18 | `HighestPrice` | 今日是否创历史新高 | number(10) | ✓ | 99.97% |  |
| 19 | `LowestPrice` | 今日是否创历史新低 | number(10) | ✓ | 99.97% |  |
| 20 | `HighestPriceRW` | 是否近一周新高 | number(10) | ✓ | 99.1% |  |
| 21 | `LowestPriceRW` | 是否近一周新低 | number(10) | ✓ | 99.1% |  |
| 22 | `HighestPriceTW` | 是否本周以来新高 | number(10) | ✓ | 79.02% | 	 是否本周以来新高(HighestAdjustedPriceTW)：1-是，0-否，当为NULL时，代表该交易日为该区... |
| 23 | `LowestPriceTW` | 是否本周以来新低 | number(10) | ✓ | 79.02% |  |
| 24 | `HighestPriceRM` | 是否近一月新高 | number(10) | ✓ | 99.97% |  |
| 25 | `LowestPriceRM` | 是否近一月新低 | number(10) | ✓ | 99.97% |  |
| 26 | `HighestPriceTM` | 是否本月以来新高 | number(10) | ✓ | 95.02% |  |
| 27 | `LowestPriceTM` | 是否本月以来新低 | number(10) | ✓ | 95.02% |  |
| 28 | `HighestPriceRMThree` | 是否近三个月新高 | number(10) | ✓ | 99.97% |  |
| 29 | `LowestPriceRMThree` | 是否近三个月新低 | number(10) | ✓ | 99.97% |  |
| 30 | `HighestPriceRMSix` | 是否近半年新高 | number(10) | ✓ | 99.97% |  |
| 31 | `LowestPriceRMSix` | 是否近半年新低 | number(10) | ✓ | 99.97% |  |
| 32 | `HighestPriceRY` | 是否近一年新高 | number(10) | ✓ | 99.97% |  |
| 33 | `LowestPriceRY` | 是否近一年新低 | number(10) | ✓ | 99.97% |  |
| 34 | `HighestPriceYTD` | 是否今年以来新高 | number(10) | ✓ | 99.57% |  |
| 35 | `LowestPriceYTD` | 是否今年以来新低 | number(10) | ✓ | 99.57% |  |
| 36 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 37 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 38 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### BackwardPrice (后复权收盘价(元))

后复权收盘价(元)(BackwardPrice)=每日收盘价*精确复权因子+精确复权常数。

### FallOnDebut (是否破发)

是否破发(FallOnDebut)：0-否，1-是，该常量对应值适用于其他是否判断的字段。

### FallOnNAPS (是否破净)

是否破净(FallOnNAPS)：0-否，1-是，该常量对应值适用于其他是否判断的字段。

### AHPremiumRate (AH溢价率是否大于50%)

AH溢价率是否大于50%(AHPremiumRate)：0-否，1-是，当为NULL时，代表该股票非AH上市股。

### SurgedLimit (今日是否涨停股)

今日是否涨停股(SurgedLimit)：0-否，1-是，当为NULL时，代表该股票不设涨跌幅限制。

### DeclineLimit (今日是否跌停股)

今日是否跌停股(DeclineLimit)：0-否，1-是，当为NULL时，代表该股票不设涨跌幅限制。

### HighestPriceTW (是否本周以来新高)

	
是否本周以来新高(HighestAdjustedPriceTW)：1-是，0-否，当为NULL时，代表该交易日为该区间第一交易日，无法判断新高或新低，该规则适用于其它是否判断中出现的NULL。

## SQL示例

```sql
-- 查询 股票日行情表现 数据
SELECT *
FROM dz_performancedata
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
