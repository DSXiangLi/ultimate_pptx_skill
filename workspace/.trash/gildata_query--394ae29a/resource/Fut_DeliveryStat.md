# Fut_DeliveryStat

**中文名**: 期货交割统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_DeliveryStat` |
| MySQL表名 | `fut_deliverystat` |
| 中文名 | 期货交割统计 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录期货合约的交割数据。
2.数据范围：2005年至今
3.信息来源：上海期货交易所、大连商品交易所、郑州商品交易所、广州期货交易所和中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 4 | `Exchange` | 交易所 | number(10) | ✓ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 5 | `DeliveryVol` | 交割量 | number(19,4) | ✓ | 100.0% |  |
| 6 | `DeliveryAmount` | 交割金额 | number(19,4) | ✓ | 30.42% |  |
| 7 | `DeliveryType` | 交割类型 | number(10) | ✗ | 100.0% | 交割类型(DeliveryType)与(CT_SystemConst)表中的DM字段关联，令LB = 2623 AND ... |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,11,13,15,17,20)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所，20-中国金融期货交易所。

### DeliveryType (交割类型)

交割类型(DeliveryType)与(CT_SystemConst)表中的DM字段关联，令LB = 2623 AND DM in (1,2)，得到交割类型的具体描述：1-实际交割，2-期转现。

## SQL示例

```sql
-- 查询 期货交割统计 数据
SELECT *
FROM fut_deliverystat
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
