# LC_AfterDailyQuote

**中文名**: A股盘后日行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AfterDailyQuote` |
| MySQL表名 | `lc_afterdailyquote` |
| 中文名 | A股盘后日行情 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：收录创业板股票每个交易日盘后以固定价格交易的行情数据，包括收盘价、买入申报数量、卖出申报数量、盘后成交量、盘后成交金额等行情指标。
2.数据范围：创业板注册制改革实施日起-至今
3.信息来源：深交所每日行情文件

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 今日收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `AfterTradeVolume` | 盘后成交量(股) | number(16,0) | ✓ | 100.0% |  |
| 6 | `AfterTradeValue` | 盘后成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `AfterBuyVolume` | 盘后买入申报数量(股) | number(16,0) | ✓ | 0.0% |  |
| 8 | `AfterSellVolume` | 盘后卖出申报数量(股) | number(16,0) | ✓ | 0.0% |  |
| 9 | `AccuTradeVolume` | 当日累计成交数量(股) | number(19,0) | ✓ | 100.0% |  |
| 10 | `AccuTradeValue` | 当日累计成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 A股盘后日行情 数据
SELECT *
FROM lc_afterdailyquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
