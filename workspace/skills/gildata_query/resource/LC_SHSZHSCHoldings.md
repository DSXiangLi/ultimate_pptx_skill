# LC_SHSZHSCHoldings

**中文名**: 沪(深)港通持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSZHSCHoldings` |
| MySQL表名 | `lc_shszhscholdings` |
| 中文名 | 沪(深)港通持股统计 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.04 |

## 表描述

1.记录港交所中央結算系統参与者在每日日终的合计持股数量，持股占比。
2.历史数据：港交所2017年3月起-至今，深交所2016年12月起至今
3.数据来源：聚源按照港交所及深交所披露整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoSource` | 信息来源 | number(10) | ✗ | 100.0% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM ... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TradingType` | 交易类型 | number(10) | ✓ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and D... |
| 5 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：当TradingType=1或3时，与“证券主表（SecuMain）”中的“证券内部... |
| 6 | `SHSZHSCode` | 沪(深)港通证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 7 | `SecuAbbr` | 证券简称 | varchar2(100) | ✓ | 99.87% |  |
| 8 | `SharesHolding` | 持股数量(股) | number(18,2) | ✓ | 100.0% |  |
| 9 | `AdjustedSharesHolding` | 调整后的持股数量(股) | number(18,2) | ✓ | 0.01% | 当有公司权益分派事件时，调整持股数量，当TradingType=1或3时，调整后持股数量为持股数量/（1+送股比例+转增... |
| 10 | `Holdratio` | 持股占比(%) | number(18,4) | ✓ | 61.68% |  |
| 11 | `AdjustedHoldratio` | 调整后的持股占比(%) | number(18,4) | ✓ | 99.78% | 调整后的持股占比(%)（AdjustedHoldratio）：当TradingType=1或3时，会在公司权益分派事件时... |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |
| 15 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |

## 字段说明

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM in (72,90,83)，得到信息来源的具体描述：72-香港联交所，83-上海证券交易所，90-深圳证券交易所。

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and DM in (1,3,5)，得到交易类型的具体描述：1-沪股通，3-深股通，5-港股通（沪深）。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：当TradingType=1或3时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到A股的证券代码、证券简称及市场等信息；当TradingType=5时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的证券代码、证券简称及市场等信息。

### AdjustedSharesHolding (调整后的持股数量(股))

当有公司权益分派事件时，调整持股数量，当TradingType=1或3时，调整后持股数量为持股数量/（1+送股比例+转增股比例）；当TradingType=5，调整后持股数量为持股数量*拆分股比例或持股数量/合并股比例。

### AdjustedHoldratio (调整后的持股占比(%))

调整后的持股占比(%)（AdjustedHoldratio）：当TradingType=1或3时，会在公司权益分派事件时，对分子持股数量进行了调整，使用调整后的持股数量，分母为无限售流通A股；当TradingType=5时，该字段等于持股量占港股截止日期前一日已上市股数的百分比，其中在公司权益分派事件时使用调整后的持股数量作为分子，以港股截止日期当日已上市股数作为分母。

## SQL示例

```sql
-- 查询 沪(深)港通持股统计 数据
SELECT *
FROM lc_shszhscholdings
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
