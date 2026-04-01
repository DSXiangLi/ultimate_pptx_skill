# Bond_SSEFirmQuoteFI

**中文名**: 沪固收确定报价行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SSEFirmQuoteFI` |
| MySQL表名 | `bond_ssefirmquotefi` |
| 中文名 | 沪固收确定报价行情 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

内容说明：本表提供上交所固收平台的确定报价行情数据，包括买入报价方、买入价、买入数量、买入到期收益率、卖出报价方、卖出价、卖出到期收益率、卖出数量等。
数据范围：2024-04-24至今
信息来源：上海证券交易所固定收益平台

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `BidOrderNumber` | 买入订单编号 | number(10) | ✗ | 100.0% | 买入订单编号(BidOrderNumber)：其中买入订单编号为0表示无买入订单。 |
| 5 | `BidTradeTime` | 买入报价时间 | varchar2(12) | ✓ | 87.97% |  |
| 6 | `BidQuotingParty` | 买入报价方 | varchar2(30) | ✓ | 87.97% |  |
| 7 | `BidCompanyCode` | 买入方公司代码 | number(10) | ✓ | 87.96% |  |
| 8 | `BidCleanPrice` | 买入价净价(元) | number(19,4) | ✓ | 87.97% |  |
| 9 | `BidNumber` | 买入数量(手) | number(19,4) | ✓ | 87.97% |  |
| 10 | `BidFullPrice` | 买入价全价(元) | number(19,4) | ✓ | 87.97% |  |
| 11 | `BidYTM` | 买入到期收益率(%) | number(19,4) | ✓ | 87.97% |  |
| 12 | `AskOrderNumber` | 卖出订单编号 | number(10) | ✗ | 100.0% | 卖出订单编号(AskOrderNumber)：其中卖出订单编号为0表示无卖出订单。 |
| 13 | `AskTradeTime` | 卖出报价时间 | varchar2(12) | ✓ | 69.81% |  |
| 14 | `AskQuotingParty` | 卖出报价方 | varchar2(30) | ✓ | 69.81% |  |
| 15 | `AskCompanyCode` | 卖出方公司代码 | number(10) | ✓ | 69.8% |  |
| 16 | `AskCleanPrice` | 卖出价净价(元) | number(19,4) | ✓ | 69.81% |  |
| 17 | `AskNumber` | 卖出数量 | number(19,4) | ✓ | 69.81% |  |
| 18 | `AskFullPrice` | 卖出价全价(元) | number(19,4) | ✓ | 69.81% |  |
| 19 | `AskYTM` | 卖出到期收益率(%) | number(19,4) | ✓ | 69.81% |  |
| 20 | `AccruedInterest` | 应计利息 | number(19,4) | ✓ | 100.0% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### BidOrderNumber (买入订单编号)

买入订单编号(BidOrderNumber)：其中买入订单编号为0表示无买入订单。

### AskOrderNumber (卖出订单编号)

卖出订单编号(AskOrderNumber)：其中卖出订单编号为0表示无卖出订单。

## SQL示例

```sql
-- 查询 沪固收确定报价行情 数据
SELECT *
FROM bond_ssefirmquotefi
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
