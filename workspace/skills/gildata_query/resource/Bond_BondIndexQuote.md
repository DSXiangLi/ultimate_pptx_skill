# Bond_BondIndexQuote

**中文名**: 债券指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BondIndexQuote` |
| MySQL表名 | `bond_bondindexquote` |
| 中文名 | 债券指数行情 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.收录了上证债券指数、中证债券指数、深证债券/国证债券指数等指数的行情数据。
2.历史数据：1996年7月至今
3.数据源：上海交易所、深圳交易所、中证指数有限公司、深圳证券信息有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 指数内部代码 | number(10) | ✗ | 100.0% | 指数内部代码（InnerCode）：与“债券指数概况（Bond_IndexBasicInfo）”中的“指数内部代码（In... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 昨收盘(点) | number(19,4) | ✓ | 99.84% |  |
| 5 | `OpenPrice` | 今开盘(点) | number(19,4) | ✓ | 2.46% |  |
| 6 | `HighPrice` | 最高价(点) | number(19,4) | ✓ | 2.46% |  |
| 7 | `LowPrice` | 最低价(点) | number(19,4) | ✓ | 2.46% |  |
| 8 | `ClosePrice` | 收盘价(点) | number(19,4) | ✓ | 99.88% |  |
| 9 | `TurnoverVolume` | 成交量(元) | number(19,2) | ✓ | 76.36% |  |
| 10 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 41.26% |  |
| 11 | `TurnoverDeals` | 成交笔数 | number(10) | ✓ | 0.43% |  |
| 12 | `ChangePCT` | 涨跌幅(%) | number(19,8) | ✓ | 99.84% |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (指数内部代码)

指数内部代码（InnerCode）：与“债券指数概况（Bond_IndexBasicInfo）”中的“指数内部代码（IndexCode）”关联，得到指数的代码、简称等。

## SQL示例

```sql
-- 查询 债券指数行情 数据
SELECT *
FROM bond_bondindexquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
