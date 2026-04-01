# Bond_ConBDExchangeQuote

**中文名**: 可转换债券行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDExchangeQuote` |
| MySQL表名 | `bond_conbdexchangequote` |
| 中文名 | 可转换债券行情 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 44 |
| 版本 | 1.03 |

## 表描述

1.本表记录沪深交易所披露的可转债（含可交债）和三板市场披露的退债行情，其中：上交所提供的是上交所竞价平台的行情，深交所双边交易提供的深交所竞价平台行情，单边交易提供的深交所固定收益平台行情。
2.本表包含所有可转换债券(含分离交易可转债、可交换公司债)的行情、成交情况、基础股票收盘价等，并提供根据当天行情计算的转股溢价率、转换平价等。
3.交易方式：可转债常规债券都为全价。分离交易可转债：上交所竞价平台2008-10-13之前的分离交易可转债，深交所竞价及固收平台2009-3-30之前的分离交易可转债为全价交易，其它都为净价交易。可交债：深交所竞价及固收平台2022-5-16之前的可交债为全价交易，其它都为净价交易。
4.数据范围：1993-02-10 至今
5.信息来源：上海交易所、深圳交易所、全国中小企业股份转让系统

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `BondNature` | 债券类型 | number(10) | ✓ | 100.0% | 债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到债券类型... |
| 5 | `Maturity` | 债券期限 | number(9,6) | ✓ | 100.0% |  |
| 6 | `PrevClosePrice` | 昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `OpenPrice` | 开盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `HighPrice` | 最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `LowPrice` | 最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `ChangePCT` | 涨跌幅(%) | number(18,6) | ✓ | 100.0% |  |
| 12 | `TurnoverRate` | 换手率(%) | number(11,6) | ✓ | 100.0% |  |
| 13 | `TurnoverVolume` | 成交量(张) | number(19,4) | ✓ | 100.0% | 可转债的成交量的单位为“手”，“1手”等于“10张”。 |
| 14 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 15 | `TurnoverDeals` | 成交笔数(笔) | number(10) | ✓ | 56.68% |  |
| 16 | `NewConvetPrice` | 最新转股价(元) | number(19,4) | ✓ | 96.33% |  |
| 17 | `StockPrice` | 最新股票价格(元) | number(19,4) | ✓ | 99.74% |  |
| 18 | `CBConvertValue` | 转债转换价值 | float | ✓ | 96.22% | 转债转换价值＝转债对应的基础股票股价×（100／转债最新转股价格） |
| 19 | `ConvertPremiumRate` | 转股溢价率(%) | float | ✓ | 96.22% | 转股溢价率=（转债价格—转换价值）/转换价值*100 |
| 20 | `ConvertParPrice` | 转换平价 | float | ✓ | 96.33% | 转换平价＝转债价格／（100／转债最新转股价格） |
| 21 | `YrMat` | 剩余期限 | number(9,6) | ✓ | 100.0% |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |
| 24 | `YTM_OP` | 开盘价到期收益率(%) | float | ✓ | 33.06% |  |
| 25 | `Duration_OP` | 开盘价麦氏久期 | float | ✓ | 31.14% |  |
| 26 | `ModifiedDuration_OP` | 开盘价修正久期 | float | ✓ | 31.12% |  |
| 27 | `Convexity_OP` | 开盘价凸度 | float | ✓ | 32.71% |  |
| 28 | `YTM_HI` | 最高价到期收益率(%) | float | ✓ | 33.06% |  |
| 29 | `Duration_HI` | 最高价麦氏久期 | float | ✓ | 31.13% |  |
| 30 | `ModifiedDuration_HI` | 最高价修正久期 | float | ✓ | 31.11% |  |
| 31 | `Convexity_HI` | 最高价凸度 | float | ✓ | 32.71% |  |
| 32 | `YTM_LO` | 最低价到期收益率(%) | float | ✓ | 33.06% |  |
| 33 | `Duration_LO` | 最低价麦氏久期 | float | ✓ | 31.14% |  |
| 34 | `ModifiedDuration_LO` | 最低价修正久期 | float | ✓ | 31.12% |  |
| 35 | `Convexity_LO` | 最低价凸度 | float | ✓ | 32.72% |  |
| 36 | `YTM_CL` | 收盘价到期收益率(%) | float | ✓ | 33.31% |  |
| 37 | `Duration_CL` | 收盘价麦氏久期 | float | ✓ | 31.18% |  |
| 38 | `ModifiedDuration_CL` | 收盘价修正久期 | float | ✓ | 31.16% |  |
| 39 | `Convexity_CL` | 收盘价凸度 | float | ✓ | 32.97% |  |
| 40 | `YTM_AVG` | 均价到期收益率(%) | float | ✓ | 10.42% |  |
| 41 | `Duration_AVG` | 均价麦氏久期 | float | ✓ | 8.43% |  |
| 42 | `ModifiedDuration_AVG` | 均价修正久期 | float | ✓ | 8.43% |  |
| 43 | `Convexity_AVG` | 均价凸度 | float | ✓ | 10.21% |  |
| 44 | `AccruedInterest` | 应计利息(元) | number(19,4) | ✓ | 99.95% |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### BondNature (债券类型)

债券类型(BondNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到债券类型的具体描述：1-常规债券，2-分离交易可转债，3-本息分离交易债券，4-可交换公司债券。

### TurnoverVolume (成交量(张))

可转债的成交量的单位为“手”，“1手”等于“10张”。

### CBConvertValue (转债转换价值)

转债转换价值＝转债对应的基础股票股价×（100／转债最新转股价格）

### ConvertPremiumRate (转股溢价率(%))

转股溢价率=（转债价格—转换价值）/转换价值*100

### ConvertParPrice (转换平价)

转换平价＝转债价格／（100／转债最新转股价格）

## SQL示例

```sql
-- 查询 可转换债券行情 数据
SELECT *
FROM bond_conbdexchangequote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
