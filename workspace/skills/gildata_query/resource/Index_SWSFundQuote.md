# Index_SWSFundQuote

**中文名**: 申万基金指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_SWSFundQuote` |
| MySQL表名 | `index_swsfundquote` |
| 中文名 | 申万基金指数行情 |
| 路径 | 聚源新版数据库 > 产品代理 > 申万代理数据库 > 申万指数 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.收录申万公募基金分类指数行情数据。
2.历史数据：2004年12月31日至今
3.数据源：申万宏源证券研究所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(元/点) | number(19,4) | ✓ | 100.0% |  |
| 5 | `ChangeOF` | 涨跌 | number(19,4) | ✓ | 99.97% |  |
| 6 | `ChangePCT` | 涨跌幅(%) | number(19,6) | ✓ | 99.97% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

## SQL示例

```sql
-- 查询 申万基金指数行情 数据
SELECT *
FROM index_swsfundquote
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
