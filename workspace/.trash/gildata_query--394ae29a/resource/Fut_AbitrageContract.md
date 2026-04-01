# Fut_AbitrageContract

**中文名**: 国内期货套利合约

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_AbitrageContract` |
| MySQL表名 | `fut_abitragecontract` |
| 中文名 | 国内期货套利合约 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国内期货的套利合约信息，包括两部分内容，一部分为大商所披露的可直接交易的套利组合信息，另一部分为聚源人工整理的可套利的组合信息。通过是否交易所披露合约进行区分。
2.数据范围：2020年至今
3.信息来源：国内期货交易所及聚源人工整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `Exchange` | 交易所 | number(10) | ✓ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 4 | `ArbitrageStrategy` | 套利策略类型 | number(10) | ✓ | 100.0% | 套利策略类型(ArbitrageStrategy)与(CT_SystemConst)表中的DM字段关联，令LB = 23... |
| 5 | `ArbitrageVariety` | 套利品种名称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `LongInnerCode` | 多头合约内部编码 | number(10) | ✗ | 100.0% |  |
| 7 | `ShortInnerCode` | 空头合约内部编码 | number(10) | ✗ | 100.0% |  |
| 8 | `ArbitrageContractCode` | 套利合约代码 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `ArbitrageContractName` | 套利合约名称 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `PortLmtOrdMax` | 组合最大下单手数 | number(18,2) | ✓ | 4.14% |  |
| 11 | `PortLmtOrdMin` | 组合最小下单手数 | number(18,2) | ✓ | 0.7% |  |
| 12 | `PLittlestChangeUnit` | 组合最小变动价位(元) | number(18,2) | ✓ | 4.14% |  |
| 13 | `SpeculativeHedge` | 组合投机套保属性 | number(10) | ✓ | 4.14% | 组合投机套保属性(SpeculativeHedge)与(CT_SystemConst)表中的DM字段关联，令LB = 2... |
| 14 | `PortfolioMargin` | 组合交易保证金额(元) | number(19,4) | ✓ | 4.13% |  |
| 15 | `IfExchangeDisclosure` | 是否交易所披露合约 | number(10) | ✓ | 100.0% | 是否交易所披露合约(IfExchangeDisclosure)与(CT_SystemConst)表中的DM字段关联，令L... |
| 16 | `Remark` | 备注 | clob | ✓ | 0.0% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN(10,11,13,15,20)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，20-中国金融期货交易所。

### ArbitrageStrategy (套利策略类型)

套利策略类型(ArbitrageStrategy)与(CT_SystemConst)表中的DM字段关联，令LB = 2336，得到套利策略类型的具体描述：1-期货对锁套利，2-期货跨期套利，3-期货跨品种套利，4-期货期现套利，5-不同交割方式套利。

### SpeculativeHedge (组合投机套保属性)

组合投机套保属性(SpeculativeHedge)与(CT_SystemConst)表中的DM字段关联，令LB = 2337，得到组合投机套保属性的具体描述：1-投机-投机，2-套保-套保，3-套保-投机，4-投机-套保。

### IfExchangeDisclosure (是否交易所披露合约)

是否交易所披露合约(IfExchangeDisclosure)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN(1,2)，得到是否交易所披露合约的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 国内期货套利合约 数据
SELECT *
FROM fut_abitragecontract
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
