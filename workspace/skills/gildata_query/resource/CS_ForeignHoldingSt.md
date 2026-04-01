# CS_ForeignHoldingSt

**中文名**: 外资持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_ForeignHoldingSt` |
| MySQL表名 | `cs_foreignholdingst` |
| 中文名 | 外资持股统计 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

内容说明：境外投资者持股统计，包含持股总数、持股比例，境外投资者指QFII/RQFII/深股通/全球存托凭证跨境转换机构/全球存托凭证存托人。
数据范围：2007年至今
信息来源：深交所、上交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `ForeignHoldings` | 外资持股总数(万股) | number(18,4) | ✓ | 100.0% |  |
| 5 | `ForeignHoldProp` | 外资持股比例(%) | number(18,4) | ✓ | 100.0% |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 外资持股统计 数据
SELECT *
FROM cs_foreignholdingst
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
