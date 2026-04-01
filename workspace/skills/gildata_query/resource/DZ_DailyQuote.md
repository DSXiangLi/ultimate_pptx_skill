# DZ_DailyQuote

**中文名**: 日行情表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_DailyQuote` |
| MySQL表名 | `dz_dailyquote` |
| 中文名 | 日行情表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：收录股票、债券（不包含银行间交易的债券）、基金、指数每个交易日收盘行情数据，包括昨收盘、今开盘、最高价、最低价、收盘价、成交量、成交金额、成交笔数等行情指标。
2.数据范围：证券上市起-至今
3.信息来源：上交所/深交所/北交所每日行情收盘文件

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `OpenPrice` | 今开盘(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `HighPrice` | 最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `LowPrice` | 最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `TurnoverVolume` | 成交量(股/份) | number(20,0) | ✓ | 100.0% |  |
| 10 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverDeals` | 成交笔数(笔) | number(10) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 日行情表 数据
SELECT *
FROM dz_dailyquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
