# LC_CBRSValuation

**中文名**: 中债登限售股估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_CBRSValuation` |
| MySQL表名 | `lc_cbrsvaluation` |
| 中文名 | 中债登限售股估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：根据中国证券投资基金业协会2017年9月4日发布的《证券投资基金投资流通受限股票估值指引(试行)》规定，采用亚式期权AAP模型衡量限售股的流动性折扣，并进一步计算限售股的公允价值。
2.数据范围：2017.10.10至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `SecuCode` | 标的股票代码 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `SecuAbbr` | 标的股票简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `ValuationDate` | 估值日 | date | ✗ | 100.0% |  |
| 6 | `ListDate` | 预计上市流通日 | date | ✗ | 100.0% |  |
| 7 | `YrMat` | 剩余期限(年) | number(6,4) | ✓ | 100.0% |  |
| 8 | `LastTradingDay` | 标的最后交易日 | date | ✓ | 100.0% |  |
| 9 | `RSSecuCode` | 参照标的 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `ExpVolatility` | 预期波动率(%) | number(10,6) | ✓ | 100.0% |  |
| 11 | `ExpDividYield` | 预期股利收益率(%) | number(10,6) | ✓ | 100.0% |  |
| 12 | `MarketValue` | 标的股票公允价值(元) | number(8,4) | ✓ | 100.0% |  |
| 13 | `StockOptValue` | 期权价值(元) | number(8,4) | ✓ | 100.0% |  |
| 14 | `LiquidDiscount` | 流动性折扣(%) | number(10,6) | ✓ | 100.0% |  |
| 15 | `RSValuation` | 限售股估值(元) | number(8,4) | ✓ | 100.0% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 中债登限售股估值 数据
SELECT *
FROM lc_cbrsvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
