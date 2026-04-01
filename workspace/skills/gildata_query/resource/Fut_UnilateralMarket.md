# Fut_UnilateralMarket

**中文名**: 期货交易所单边市状态

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_UnilateralMarket` |
| MySQL表名 | `fut_unilateralmarket` |
| 中文名 | 期货交易所单边市状态 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货行情 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录期货交易所的单边市状态的数据。
2.数据范围：2004年至今
3.信息来源：大连商品交易所、广州期货交易所、郑州商品交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 4 | `Exchange` | 交易所 | number(10) | ✓ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 5 | `UnilateralStatus` | 单边市状态 | number(10) | ✗ | 100.0% | 单边市状态(UnilateralStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2617... |
| 6 | `UnilateralStatusDays` | 连续单边市天数(个数) | number(10) | ✓ | 44.2% |  |
| 7 | `PriceCeiling` | 涨停板价 | number(19,4) | ✓ | 53.62% |  |
| 8 | `PriceFloor` | 跌停板价 | number(19,4) | ✓ | 53.62% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN(13,15,17)，得到交易所的具体描述：13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所。

### UnilateralStatus (单边市状态)

单边市状态(UnilateralStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2617，得到单边市状态的具体描述：1-涨停，2-跌停，3-非单边市。

## SQL示例

```sql
-- 查询 期货交易所单边市状态 数据
SELECT *
FROM fut_unilateralmarket
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
