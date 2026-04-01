# Fut_IntendedDeliBond

**中文名**: 期货意向交割国债

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_IntendedDeliBond` |
| MySQL表名 | `fut_intendeddelibond` |
| 中文名 | 期货意向交割国债 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国内国债期货的意向交割国债信息。
2.数据范围：2013年至今
3.信息来源：中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 4 | `Exchange` | 交易所 | number(10) | ✓ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = ... |
| 5 | `DeclareDeliveryVol` | 申报交割量 | number(19,4) | ✓ | 100.0% |  |
| 6 | `DeliverableInnerCode` | 可交割券内部编码 | number(10) | ✗ | 100.0% | 可交割券内部编码(DeliverableInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编... |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM = 20，得到交易所的具体描述：20-中国金融期货交易所。

### DeliverableInnerCode (可交割券内部编码)

可交割券内部编码(DeliverableInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 期货意向交割国债 数据
SELECT *
FROM fut_intendeddelibond
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
