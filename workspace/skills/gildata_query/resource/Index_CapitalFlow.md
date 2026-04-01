# Index_CapitalFlow

**中文名**: 指数资金流动表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_CapitalFlow` |
| MySQL表名 | `index_capitalflow` |
| 中文名 | 指数资金流动表 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 39 |
| 版本 | 1 |

## 表描述

内容说明：收录境内股票指数的每日资金流向、融资融券、港资流向数据，计算指数维度的资金流向。其中资金流向数据仅包括二级市场股票交易所(不包含北京交易所)产生的资金流向数据，不含大宗交易产生的资金流向，个股数据可参考“股票交易资金流向（QT_TradingCapitalFlow）”表和“科创板交易资金分类流向（LC_STIBCapFlowType）”表；融资融券个股数据可参考“融资融券交易明细（MT_TradingDetail）”表；港资流向个股数据可参考“沪(深)港通持股统计（LC_SHSZHSCHoldings）”表；大宗交易资金流向数据可参考“股东股权变动（ LC_ShareTransfer）”表。
数据范围：2010年4月至今
信息来源：聚源按照上交所、深交所原始披露整理；恒生电子；聚源按照港交所披露衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内码 | number(10) | ✗ | 100.0% | 指数内码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `FinanceValue` | 融资余额(元) | number(19,4) | ✓ | 96.18% |  |
| 5 | `FinanceBuyValue` | 融资买入额(元) | number(19,4) | ✓ | 96.18% |  |
| 6 | `FinanceRefundValue` | 融资偿还额(元) | number(19,4) | ✓ | 96.18% |  |
| 7 | `SecurityVolume` | 融券余量(股) | number(18,2) | ✓ | 96.18% |  |
| 8 | `SecuritySellVolume` | 融券卖出量(股) | number(18,2) | ✓ | 96.18% |  |
| 9 | `SecurityRefundVolume` | 融券偿还量(股) | number(18,2) | ✓ | 96.18% |  |
| 10 | `SecurityValue` | 融券余额(元) | number(19,4) | ✓ | 96.18% |  |
| 11 | `TradingValue` | 融资融券余额(元) | number(19,4) | ✓ | 96.18% |  |
| 12 | `BuyValue` | 总流入金额(元) | number(19,4) | ✓ | 95.92% |  |
| 13 | `SellValue` | 总流出金额(元) | number(19,4) | ✓ | 95.92% |  |
| 14 | `BuyVolume` | 总流入量(股) | number(19,0) | ✓ | 95.92% |  |
| 15 | `SellVolume` | 总流出量(股) | number(19,0) | ✓ | 95.92% |  |
| 16 | `NetBuyValue` | 净流入金额(元) | number(19,4) | ✓ | 95.92% |  |
| 17 | `NetBuyVolume` | 净流入量(股) | number(19,0) | ✓ | 95.92% |  |
| 18 | `BuyValue_XL` | 流入金额(超大单) | number(19,4) | ✓ | 95.33% | 小单/中单/大单/超大单：按照个股单笔成交金额区间划分，[0，5w)-小单，[5w，30w)-中单，[30w，100w)... |
| 19 | `SellValue_XL` | 流出金额(超大单) | number(19,4) | ✓ | 95.33% |  |
| 20 | `BuyVolume_XL` | 流入量(超大单) | number(19,0) | ✓ | 95.33% |  |
| 21 | `SellVolume_XL` | 流出量(超大单) | number(19,0) | ✓ | 95.33% |  |
| 22 | `BuyValue_L` | 流入金额(大单) | number(19,4) | ✓ | 95.86% |  |
| 23 | `SellValue_L` | 流出金额(大单) | number(19,4) | ✓ | 95.86% |  |
| 24 | `BuyVolume_L` | 流入量(大单) | number(19,0) | ✓ | 95.86% |  |
| 25 | `SellVolume_L` | 流出量(大单) | number(19,0) | ✓ | 95.86% |  |
| 26 | `BuyValue_M` | 流入金额(中单) | number(19,4) | ✓ | 95.91% |  |
| 27 | `SellValue_M` | 流出金额(中单) | number(19,4) | ✓ | 95.91% |  |
| 28 | `BuyVolume_M` | 流入量(中单) | number(19,0) | ✓ | 95.91% |  |
| 29 | `SellVolume_M` | 流出量(中单) | number(19,0) | ✓ | 95.91% |  |
| 30 | `BuyValue_S` | 流入金额(小单) | number(19,4) | ✓ | 95.92% |  |
| 31 | `SellValue_S` | 流出金额(小单) | number(19,4) | ✓ | 95.92% |  |
| 32 | `BuyVolume_S` | 流入量(小单) | number(19,0) | ✓ | 95.92% |  |
| 33 | `SellVolume_S` | 流出量(小单) | number(19,0) | ✓ | 95.92% |  |
| 34 | `HK_Holdratio` | 沪深港通持股比例(%) | number(18,6) | ✓ | 56.58% | 沪深港通持股比例(%)（HK_Holdratio）=100 * Σ(沪深港通持股占已发行股份百分比*AB股流通市值)/Σ... |
| 35 | `HK_StockChangeRD` | 沪深港通持股日变动股数(股) | number(19,2) | ✓ | 53.01% | 沪深港通持股日变动股数(股)（HK_StockChangeRD）= Σ(沪深港通持股量-前一交易日沪深港通持股量) |
| 36 | `HK_MVChangeRD` | 沪深港通持股日变动市值(元) | number(19,2) | ✓ | 52.98% | 沪深港通持股日变动市值(元)（HK_MVChangeRD）= Σ沪深港通持股日变动股数*成份成交均价=Σ((沪深港通持股... |
| 37 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 38 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 39 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内码)

指数内码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### BuyValue_XL (流入金额(超大单))

小单/中单/大单/超大单：按照个股单笔成交金额区间划分，[0，5w)-小单，[5w，30w)-中单，[30w，100w)-大单，[100w，+∞)-超大单

### HK_Holdratio (沪深港通持股比例(%))

沪深港通持股比例(%)（HK_Holdratio）=100 * Σ(沪深港通持股占已发行股份百分比*AB股流通市值)/ΣAB股流通市值

### HK_StockChangeRD (沪深港通持股日变动股数(股))

沪深港通持股日变动股数(股)（HK_StockChangeRD）= Σ(沪深港通持股量-前一交易日沪深港通持股量)

### HK_MVChangeRD (沪深港通持股日变动市值(元))

沪深港通持股日变动市值(元)（HK_MVChangeRD）= Σ沪深港通持股日变动股数*成份成交均价=Σ((沪深港通持股量-前一交易日沪深港通持股量)*(成份成交金额/成交量))

## SQL示例

```sql
-- 查询 指数资金流动表 数据
SELECT *
FROM index_capitalflow
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
