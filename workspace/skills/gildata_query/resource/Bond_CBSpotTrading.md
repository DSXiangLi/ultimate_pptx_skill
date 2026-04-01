# Bond_CBSpotTrading

**中文名**: 央行现券买卖操作

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBSpotTrading` |
| MySQL表名 | `bond_cbspottrading` |
| 中文名 | 央行现券买卖操作 |
| 路径 | 聚源新版数据库 > 债券数据库 > 央行公开市场操作 |
| 更新频率 | 暂未更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.收录中国人民银行在公开市场业务操作中，每笔现券买卖的操作情况。
2.数据范围：2000-01-04 至今
3.信息来源：中债登、中国人民银行

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 4 | `SpotTradingType` | 现券交易类型 | number(10) | ✓ | 100.0% | 现券交易类型(SpotTradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1236... |
| 5 | `SpotTradingMethod` | 现券交易方式 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `TenderSize` | 招标数量(亿元) | number(19,4) | ✓ | 5.74% |  |
| 7 | `TenderPrice` | 招标价格(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SpotTradingType (现券交易类型)

现券交易类型(SpotTradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1236，得到现券交易类型的具体描述：1-现券买断，2-现券卖断。

## SQL示例

```sql
-- 查询 央行现券买卖操作 数据
SELECT *
FROM bond_cbspottrading
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
