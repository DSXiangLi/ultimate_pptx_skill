# Fut_TradingHours

**中文名**: 国内期货交易时间表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Fut_TradingHours` |
| MySQL表名 | `fut_tradinghours` |
| 中文名 | 国内期货交易时间表 |
| 路径 | 聚源新版数据库 > 期货数据库 > 期货基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录国内以日度和合约为维度的连续交易和非连续交易品种的各个交易时段的交易时间。
2.数据范围：1995年至今
3.信息来源：上海期货交易所、上海国际能源交易中心、郑州商品交易所、大连商品交易所和中国金融期货交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CalendarDate` | 日历日期 | date | ✗ | 100.0% |  |
| 3 | `IfTradingDay` | 是否交易日 | number(10) | ✓ | 100.0% | 是否交易日(IfTradingDay)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND ... |
| 4 | `TradeBusinessDate` | 交易所属业务日期 | date | ✓ | 100.0% |  |
| 5 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码(ContractInnerCode)与(Fut_ContractMain)表中的ContractInner... |
| 6 | `VarietyInnerCode` | 品种内部编码 | number(10) | ✓ | 100.0% | 品种内部编码(VarietyInnerCode) 与Fut_FuturesContract表的ContractInner... |
| 7 | `Exchange` | 交易所 | number(10) | ✓ | 100.0% | 交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN... |
| 8 | `Week` | 星期 | number(10) | ✓ | 100.0% |  |
| 9 | `CallAuctionBeginTime` | 集合竞价开始时间 | varchar2(20) | ✓ | 100.0% |  |
| 10 | `CallAuctionEndTime` | 集合竞价结束时间 | varchar2(20) | ✓ | 100.0% |  |
| 11 | `IfOvernightTrading` | 是否跨夜交易 | number(10) | ✓ | 53.28% | 是否跨夜交易(IfOvernightTrading)与(CT_SystemConst)表中的DM字段关联，令LB = 9... |
| 12 | `NightTradingMark` | 夜盘标识 | number(10) | ✓ | 53.28% | 夜盘标识(NightTradingMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 A... |
| 13 | `ContinuousTradeBDate` | 夜盘交易开始日期 | date | ✓ | 51.99% |  |
| 14 | `ContinuousTradeBTime` | 夜盘交易开始时间 | varchar2(20) | ✓ | 51.99% |  |
| 15 | `ContinuousTradeETime` | 夜盘交易结束时间 | varchar2(20) | ✓ | 51.99% |  |
| 16 | `ContinuousTradeEDate` | 夜盘交易结束日期 | date | ✓ | 51.99% |  |
| 17 | `DayTradeFirstSessionBT` | 日盘交易第一节开始时间 | varchar2(20) | ✓ | 100.0% |  |
| 18 | `DayTradeFirstSessionET` | 日盘交易第一节结束时间 | varchar2(20) | ✓ | 100.0% |  |
| 19 | `DayTradeSeconSessionBT` | 日盘交易第二节开始时间 | varchar2(20) | ✓ | 99.99% |  |
| 20 | `DayTradeSeconSessionET` | 日盘交易第二节结束时间 | varchar2(20) | ✓ | 99.99% |  |
| 21 | `DayTradeThirdSessionBT` | 日盘交易第三节开始时间 | varchar2(20) | ✓ | 97.07% |  |
| 22 | `DayTradeThirdSessionET` | 日盘交易第三节结束时间 | varchar2(20) | ✓ | 97.07% |  |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfTradingDay (是否交易日)

是否交易日(IfTradingDay)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否交易日的具体描述：1-是，2-否。

### ContractInnerCode (合约内部编码)

合约内部编码(ContractInnerCode)与(Fut_ContractMain)表中的ContractInnerCode字段关联，得到合约内部编码的具体描述：

### VarietyInnerCode (品种内部编码)

品种内部编码(VarietyInnerCode) 与Fut_FuturesContract表的ContractInnerCode字段关联，得到该期货品种的基础信息：

### Exchange (交易所)

交易所(Exchange)与(CT_SystemConst)表中的DM字段关联，令LB = 1324 AND DM IN (10,11,13,15,17,20)，得到交易所的具体描述：10-上海期货交易所，11-上海国际能源交易中心，13-大连商品交易所，15-郑州商品交易所，17-广州期货交易所，20-中国金融期货交易所。

### IfOvernightTrading (是否跨夜交易)

是否跨夜交易(IfOvernightTrading)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否跨夜交易的具体描述：1-是，2-否。

### NightTradingMark (夜盘标识)

夜盘标识(NightTradingMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到夜盘标识的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 国内期货交易时间表 数据
SELECT *
FROM fut_tradinghours
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
