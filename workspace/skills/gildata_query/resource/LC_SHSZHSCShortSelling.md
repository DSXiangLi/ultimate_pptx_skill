# LC_SHSZHSCShortSelling

**中文名**: 沪(深)港通股票卖空数据

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSZHSCShortSelling` |
| MySQL表名 | `lc_shszhscshortselling` |
| 中文名 | 沪(深)港通股票卖空数据 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录内部编码、聚源代码、证券市场、交易日期、交易方向、交易状态、证券代码、证券简称、最多可卖空股数、可供卖空的股数余额、卖空成交股数(股)、卖空成交金额(元)、当天卖空比例(%)、累计10天卖空比例，用于展示沪股通及深股通股票卖空数据。
2.数据范围：沪(深)港通于2015-3-2开始实行可担保卖空操作
3.信息来源：香港交易所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `TradingType` | 交易方向 | number(10) | ✗ | 100.0% | 交易方向(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 AND DM ... |
| 5 | `TransactionStatus` | 交易状态 | number(10) | ✓ | 100.0% | 交易状态(TransactionStatus)与(CT_SystemConst)表中的DM字段关联，令LB=1176 A... |
| 6 | `SecuCode` | 证券代码 | varchar2(50) | ✗ | 100.0% |  |
| 7 | `SecuAbbr` | 证券简称 | varchar2(50) | ✓ | 100.0% |  |
| 8 | `MaxAvailShortSell` | 最多可卖空股数 | number(19,4) | ✓ | 93.95% | 2024年8月19日，交易所政策变更，当余额低于30万股时公布可卖空余额，否则展示“可用”，因此当本字段为空值时表示“可... |
| 9 | `RemainAvailShortSell` | 可供卖空的股数余额 | number(19,4) | ✓ | 93.95% | 2024年8月19日，交易所政策变更，当余额低于30万股时公布可卖空余额，否则展示“可用”，因此当本字段为空值时表示“可... |
| 10 | `SharesShortSell` | 卖空成交股数 | number(19,4) | ✓ | 100.0% |  |
| 11 | `ValueShortSell` | 卖空成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `ShortSellPct` | 当天卖空比例(%) | number(10,6) | ✓ | 100.0% |  |
| 13 | `ShortSellPctIn10` | 累计10天卖空比例(%) | number(10,6) | ✓ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### TradingType (交易方向)

交易方向(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 AND DM IN (1,3)，得到交易方向的具体描述：1-沪股通，3-深股通。

### TransactionStatus (交易状态)

交易状态(TransactionStatus)与(CT_SystemConst)表中的DM字段关联，令LB=1176 AND DM=10，得到交易状态的具体描述：10-交易。

### MaxAvailShortSell (最多可卖空股数)

2024年8月19日，交易所政策变更，当余额低于30万股时公布可卖空余额，否则展示“可用”，因此当本字段为空值时表示“可用”，当低于30万股时展示具体股数

### RemainAvailShortSell (可供卖空的股数余额)

2024年8月19日，交易所政策变更，当余额低于30万股时公布可卖空余额，否则展示“可用”，因此当本字段为空值时表示“可用”，当低于30万股时展示具体股数

## SQL示例

```sql
-- 查询 沪(深)港通股票卖空数据 数据
SELECT *
FROM lc_shszhscshortselling
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
