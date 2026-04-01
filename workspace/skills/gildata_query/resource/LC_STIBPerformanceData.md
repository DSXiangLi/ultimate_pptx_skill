# LC_STIBPerformanceData

**中文名**: 科创板日行情表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBPerformanceData` |
| MySQL表名 | `lc_stibperformancedata` |
| 中文名 | 科创板日行情表现 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 37 |
| 版本 | 1 |

## 表描述

1.内容说明：收录科创板股票行情表现相关的一些特色指标数据，如连涨天数、是否破发、是否破净、是否创历史新高或新低等指标，其中判断是否为历史新高或新低的价格均为后复权价格。
2.数据范围：证券上市之日起-至今
3.信息来源：基于上交所行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `ChangePCT` | 涨跌幅(%) | number(18,4) | ✓ | 100.0% |  |
| 6 | `BackwardPrice` | 后复权收盘价(元) | number(19,4) | ✓ | 100.0% | 后复权收盘价(元)(BackwardPrice)=每日收盘价*比例复权因子 |
| 7 | `RisingUpDays` | 连涨天数 | number(10) | ✓ | 100.0% |  |
| 8 | `FallingDownDays` | 连跌天数 | number(10) | ✓ | 100.0% |  |
| 9 | `MaxRisingUpDays` | 历史连涨最多天数 | number(10) | ✓ | 100.0% |  |
| 10 | `MaxFallingDownDays` | 历史连跌最多天数 | number(10) | ✓ | 100.0% |  |
| 11 | `FallOnDebut` | 是否破发 | number(10) | ✓ | 100.0% | 是否破发(FallOnDebut)：0-否，1-是，该常量对应值适用于其他是否判断的字段。 |
| 12 | `FallOnNAPS` | 是否破净 | number(10) | ✓ | 100.0% |  |
| 13 | `StockBoard` | 今日是否涨停一字板 | number(10) | ✓ | 100.0% |  |
| 14 | `LimitBoard` | 今日是否跌停一字板 | number(10) | ✓ | 100.0% |  |
| 15 | `SurgedLimit` | 今日是否涨停股 | number(10) | ✓ | 99.52% |  |
| 16 | `DeclineLimit` | 今日是否跌停股 | number(10) | ✓ | 99.52% |  |
| 17 | `HighestPrice` | 今日是否创历史新高 | number(10) | ✓ | 99.9% |  |
| 18 | `LowestPrice` | 今日是否创历史新低 | number(10) | ✓ | 99.9% |  |
| 19 | `HighestPriceRW` | 是否近一周新高 | number(10) | ✓ | 99.08% |  |
| 20 | `LowestPriceRW` | 是否近一周新低 | number(10) | ✓ | 99.08% |  |
| 21 | `HighestPriceTW` | 是否本周以来新高 | number(10) | ✓ | 78.85% | 是否本周以来新高(HighestAdjustedPriceTW)：1-是，0-否，当为NULL时，代表该交易日为该区间第... |
| 22 | `LowestPriceTW` | 是否本周以来新低 | number(10) | ✓ | 78.85% |  |
| 23 | `HighestPriceRM` | 是否近一月新高 | number(10) | ✓ | 99.9% |  |
| 24 | `LowestPriceRM` | 是否近一月新低 | number(10) | ✓ | 99.9% |  |
| 25 | `HighestPriceTM` | 是否本月以来新高 | number(10) | ✓ | 94.94% |  |
| 26 | `LowestPriceTM` | 是否本月以来新低 | number(10) | ✓ | 94.94% |  |
| 27 | `HighestPriceRMThree` | 是否近三个月新高 | number(10) | ✓ | 99.9% |  |
| 28 | `LowestPriceRMThree` | 是否近三个月新低 | number(10) | ✓ | 99.9% |  |
| 29 | `HighestPriceRMSix` | 是否近半年新高 | number(10) | ✓ | 99.9% |  |
| 30 | `LowestPriceRMSix` | 是否近半年新低 | number(10) | ✓ | 99.9% |  |
| 31 | `HighestPriceRY` | 是否近一年新高 | number(10) | ✓ | 99.9% |  |
| 32 | `LowestPriceRY` | 是否近一年新低 | number(10) | ✓ | 99.9% |  |
| 33 | `HighestPriceYTD` | 是否今年以来新高 | number(10) | ✓ | 99.53% |  |
| 34 | `LowestPriceYTD` | 是否今年以来新低 | number(10) | ✓ | 99.53% |  |
| 35 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 36 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 37 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### BackwardPrice (后复权收盘价(元))

后复权收盘价(元)(BackwardPrice)=每日收盘价*比例复权因子

### FallOnDebut (是否破发)

是否破发(FallOnDebut)：0-否，1-是，该常量对应值适用于其他是否判断的字段。

### HighestPriceTW (是否本周以来新高)

是否本周以来新高(HighestAdjustedPriceTW)：1-是，0-否，当为NULL时，代表该交易日为该区间第一交易日，无法判断新高或新低，该规则适用于其它是否判断中出现的NULL。

## SQL示例

```sql
-- 查询 科创板日行情表现 数据
SELECT *
FROM lc_stibperformancedata
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
