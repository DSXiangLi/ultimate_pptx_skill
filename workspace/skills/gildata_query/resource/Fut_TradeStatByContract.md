# Fut_TradeStatByContract

**中文名**: 期货交易统计_按交易合约

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_TradeStatByContract` |
| MySQL表名 | `fut_tradestatbycontract` |
| 中文名 | 期货交易统计_按交易合约 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货交易统计 |
| 更新频率 | 周更新和月更新 |
| 字段数量 | 21 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表收录国内各大交易所按交易合约统计的信息。包括期货成交量、成交额、持仓量等数据，数据统计期间为月和周的数据。
2.数据范围：2002年至今
3.信息来源：上海期货交易所、大连商品交易所、郑州商品交易和中国金融期货交易所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `ExchangeCode` | 交易所代码 | number(10) | ✗ | 100.0% | 交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND... |
| 4 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部... |
| 5 | `ContractCode` | 合约代码 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `ReportPeriod` | 数据统计期间 | number(10) | ✗ | 100.0% | 数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AN... |
| 7 | `OpenPrice` | 区间开盘价 | number(19,4) | ✓ | 92.09% |  |
| 8 | `HighPrice` | 区间最高价 | number(19,4) | ✓ | 92.09% |  |
| 9 | `LowPrice` | 区间最低价 | number(19,4) | ✓ | 92.08% |  |
| 10 | `ClosePrice` | 区间收盘价 | number(19,4) | ✓ | 100.0% |  |
| 11 | `ChangeOfClosePrice` | 区间收盘价涨跌 | number(19,4) | ✓ | 36.75% |  |
| 12 | `SettlePrice` | 期末结算价 | number(19,4) | ✓ | 99.93% |  |
| 13 | `OpenInterest` | 期末持仓量(手) | number(18,4) | ✓ | 100.0% |  |
| 14 | `ChangeOfOpenInterest` | 期末较期初持仓量变化(手) | number(18,4) | ✓ | 99.99% |  |
| 15 | `TurnoverVolume` | 区间成交量(手) | number(18,4) | ✓ | 100.0% |  |
| 16 | `TurnoverValue` | 区间成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `RemarkDesc` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `ChangeOfCTPS` | 区间收盘较前结算涨跌 | number(19,4) | ✓ | 55.22% |  |
| 21 | `ChangeOfSettPrice` | 区间结算价涨跌 | number(19,4) | ✓ | 22.06% |  |

## 字段说明

### ExchangeCode (交易所代码)

交易所代码(ExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,11,13,15,17,20)，得到交易所代码的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所，20-中国金融期货交易所。

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“期货合约主表（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联，得到该期货合约的基础信息。

### ReportPeriod (数据统计期间)

数据统计期间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM IN (1,6)，得到数据统计期间的具体描述：1-月份，6-周。

## SQL示例

```sql
-- 查询 期货交易统计_按交易合约 数据
SELECT *
FROM fut_tradestatbycontract
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
