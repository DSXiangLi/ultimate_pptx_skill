# Bond_ABSTradingQuote

**中文名**: 券商专项资产大宗交易行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ABSTradingQuote` |
| MySQL表名 | `bond_abstradingquote` |
| 中文名 | 券商专项资产大宗交易行情 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 暂未更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.信息来源：上海交易所，深圳交易所。
2.收录券商专项资产收益计划（资产证券化产品）每天的大宗交易行情数据。
3.数据范围：2005-12-29 至今
4.信息来源：上交所、深交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 昨收盘(元) | number(19,4) | ✓ | 85.97% |  |
| 5 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 89.44% |  |
| 6 | `TurnoverVolume` | 成交量(份) | number(19,4) | ✓ | 99.67% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到资产证券化产品的交易代码、简称等。

## SQL示例

```sql
-- 查询 券商专项资产大宗交易行情 数据
SELECT *
FROM bond_abstradingquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
