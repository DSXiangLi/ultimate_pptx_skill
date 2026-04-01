# Fut_CGBDeriv

**中文名**: 国债期货衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_CGBDeriv` |
| MySQL表名 | `fut_cgbderiv` |
| 中文名 | 国债期货衍生指标 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货行情 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国债期货衍生指标，包括发票价格、基差、交割利息、IRR、CTD券等。
2.数据范围：2013年至今
3.信息来源：聚源数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 期货合约内码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 4 | `ContractCode` | 期货合约代码 | varchar2(10) | ✓ | 100.0% |  |
| 5 | `SettlePrice` | 结算价 | number(19,8) | ✓ | 100.0% |  |
| 6 | `DeliverableInnerCode` | 可交割券内部编码 | number(10) | ✗ | 100.0% | 可交割券内部编码(DeliverableInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编... |
| 7 | `PriceType` | 价格类型 | number(10) | ✗ | 100.0% | 价格类型(PriceType)：1-中债估值，2-中证估值，3-银行间市场行情 |
| 8 | `DeliveredInterest` | 交割利息 | number(19,7) | ✓ | 100.0% |  |
| 9 | `InvoicePrice` | 发票价格 | number(19,7) | ✓ | 100.0% |  |
| 10 | `Spread` | 期现价差 | number(19,7) | ✓ | 100.0% |  |
| 11 | `Basis` | 基差 | number(19,4) | ✓ | 100.0% |  |
| 12 | `IRR` | 隐含回购率(%) | number(19,4) | ✓ | 100.0% |  |
| 13 | `TheoreticalCTDNum` | 理论CTD券序号 | number(10) | ✓ | 100.0% |  |
| 14 | `ActiveCTDNum` | 活跃CTD券序号 | number(10) | ✓ | 65.47% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (期货合约内码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### DeliverableInnerCode (可交割券内部编码)

可交割券内部编码(DeliverableInnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### PriceType (价格类型)

价格类型(PriceType)：1-中债估值，2-中证估值，3-银行间市场行情

## SQL示例

```sql
-- 查询 国债期货衍生指标 数据
SELECT *
FROM fut_cgbderiv
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
