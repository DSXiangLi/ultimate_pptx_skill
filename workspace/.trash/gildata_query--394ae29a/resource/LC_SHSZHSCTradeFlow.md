# LC_SHSZHSCTradeFlow

**中文名**: 沪(深)港通交易流向

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSZHSCTradeFlow` |
| MySQL表名 | `lc_shszhsctradeflow` |
| 中文名 | 沪(深)港通交易流向 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1 |

## 表描述

1.内容说明：收录沪深港通标的南北流向持股及资金变动信息，包括最近1日、近3日、近5日、近10日、近1月、近3月、近1年等区间统计信息。
2.数据范围：2017年3月起-至今
3.信息来源：聚源按照港交所披露衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 当TradingType=1或3时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `TradingType` | 交易类型 | number(10) | ✓ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and D... |
| 5 | `SHSZHSCode` | 沪(深)港通证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 6 | `SecuAbbr` | 证券简称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `SecuCode` | 股票代码 | varchar2(10) | ✓ | 100.0% |  |
| 8 | `StockChangeRD` | 日变动股数(股) | number(19,2) | ✓ | 99.58% |  |
| 9 | `MVChangeRD` | 日变动市值(元) | number(19,2) | ✓ | 99.58% |  |
| 10 | `StockChangeRDThree` | 三日变动股数(股) | number(19,2) | ✓ | 99.58% |  |
| 11 | `MVChangeRDThree` | 三日变动市值(元) | number(19,2) | ✓ | 99.58% |  |
| 12 | `StockChangeRDFive` | 五日变动股数(股) | number(19,2) | ✓ | 99.58% |  |
| 13 | `MVChangeRDFive` | 五日变动市值(元) | number(19,2) | ✓ | 99.58% |  |
| 14 | `StockChangeRDTen` | 十日变动股数(股) | number(19,2) | ✓ | 99.58% |  |
| 15 | `MVChangeRDTen` | 十日变动市值(元) | number(19,2) | ✓ | 99.58% |  |
| 16 | `StockChangeRM` | 月变动股数(股) | number(19,2) | ✓ | 99.58% |  |
| 17 | `MVChangeRM` | 月变动市值(元) | number(19,2) | ✓ | 99.58% |  |
| 18 | `StockChangeRQ` | 季变动股数(股) | number(19,2) | ✓ | 99.91% |  |
| 19 | `MVChangeRQ` | 季变动市值(元) | number(19,2) | ✓ | 99.86% |  |
| 20 | `StockChangeRY` | 年变动股数(股) | number(19,2) | ✓ | 99.91% |  |
| 21 | `MVChangeRY` | 年变动市值(元) | number(19,2) | ✓ | 99.86% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

当TradingType=1或3时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到A股的证券代码、证券简称及市场等信息；当TradingType=5时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的证券代码、证券简称及市场等信息。

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and DM in (1,3,5)，得到交易类型的具体描述：1-沪股通，3-深股通，5-港股通（沪深）。

## SQL示例

```sql
-- 查询 沪(深)港通交易流向 数据
SELECT *
FROM lc_shszhsctradeflow
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
