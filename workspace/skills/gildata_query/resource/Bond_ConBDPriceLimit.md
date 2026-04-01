# Bond_ConBDPriceLimit

**中文名**: 可转债涨跌停价

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDPriceLimit` |
| MySQL表名 | `bond_conbdpricelimit` |
| 中文名 | 可转债涨跌停价 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：记录可转债每日的涨停价和跌停价，盘前提供。
2.数据范围：2017-01-01 至今
3.信息来源：上交所/深交所每日盘前信息接口文件

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 前收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 5 | `PriceCeiling` | 涨停价(元) | number(19,4) | ✓ | 81.88% |  |
| 6 | `PriceFloor` | 跌停价(元) | number(19,4) | ✓ | 81.88% |  |
| 7 | `BuyNumUnit` | 买入数量单位 | number(12,0) | ✓ | 99.1% |  |
| 8 | `SellNumUnit` | 卖出数量单位 | number(12,0) | ✓ | 99.1% |  |
| 9 | `LmtOrdMin` | 单笔限价申报下限 | number(12,0) | ✓ | 97.92% |  |
| 10 | `LmtOrdMax` | 单笔限价申报上限 | number(12,0) | ✓ | 97.92% |  |
| 11 | `MktOrdMin` | 单笔市价申报下限 | number(12,0) | ✓ | 98.62% |  |
| 12 | `MktOrdMax` | 单笔市价申报上限 | number(12,0) | ✓ | 98.62% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 可转债涨跌停价 数据
SELECT *
FROM bond_conbdpricelimit
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
