# Bond_BasicQuote

**中文名**: 债券基础行情表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_BasicQuote` |
| MySQL表名 | `bond_basicquote` |
| 中文名 | 债券基础行情表 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 本币市场成交收盘行情 > 债券市场成交收盘行情  |
| 更新频率 | 日更新 |
| 字段数量 | 27 |
| 版本 | 1 |

## 表描述

1.内容说明：
1.1收录所有现券每个交易日行情信息，交易市场包括银行间市场、沪深交易所竞价系统、上交所固定收益平台、深交所综合收益平台、北京证券交易所、三板市场。
1.2.提供当天行情的交易方式、净价、全价、均价、涨跌幅、应计利息、当日是否有交易等数据。
1.3.所有市场行情均考虑减少面值还本对价格的影响。
2.数据范围：1990-12-19至今
3.信息来源：银行间、上交所、深交所、北交所、三板市场等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)：83-上海证券交易所,89-银行间债券市场,90-深圳证券交易所, 12-上交所固定收... |
| 4 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 5 | `TradeType` | 交易方式 | number(10) | ✗ | 100.0% | 交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1517，得到交易方式的... |
| 6 | `IfTrading` | 当日是否交易 | number(10) | ✗ | 100.0% | 当日是否交易(IfTrading)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM... |
| 7 | `AccruInterest` | 应计利息 | number(18,8) | ✓ | 97.53% |  |
| 8 | `PrevCloseNetPrice` | 净价昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `OpenNetPrice` | 净价开盘价(元) | number(19,4) | ✓ | 99.98% |  |
| 10 | `HighNetPrice` | 净价最高价(元) | number(19,4) | ✓ | 99.98% |  |
| 11 | `LowNetPrice` | 净价最低价(元) | number(19,4) | ✓ | 99.98% |  |
| 12 | `CloseNetPrice` | 净价收盘价(元) | number(19,4) | ✓ | 99.98% |  |
| 13 | `WeightedNetPrice` | 净价加权价(元) | number(19,4) | ✓ | 74.18% |  |
| 14 | `ChangePCTCln` | 净价涨跌幅(%) | number(19,4) | ✓ | 5.18% |  |
| 15 | `PrevCloseDirtyPrice` | 全价昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 16 | `OpenDirtyPrice` | 全价开盘价(元) | number(19,4) | ✓ | 99.98% |  |
| 17 | `HighDirtyPrice` | 全价最高价(元) | number(19,4) | ✓ | 99.98% |  |
| 18 | `LowDirtyPrice` | 全价最低价(元) | number(19,4) | ✓ | 99.98% |  |
| 19 | `CloseDirtyPrice` | 全价收盘价(元) | number(19,4) | ✓ | 99.98% |  |
| 20 | `WeightedDirtyPrice` | 全价加权价(元) | number(19,4) | ✓ | 74.18% |  |
| 21 | `ChangePCTDt` | 全价涨跌幅(%) | number(19,4) | ✓ | 5.18% |  |
| 22 | `TurnoverVolume` | 成交量(张) | number(19,0) | ✓ | 100.0% |  |
| 23 | `TurnoverDeals` | 成交笔数(笔) | number(19,0) | ✓ | 98.79% | 对历史券，由于行情传输文件中经常出现不提供成交笔数的情况，本表对【成交笔数 TurnoverDeals】字段进行了赋0填... |
| 24 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 25 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)：83-上海证券交易所,89-银行间债券市场,90-深圳证券交易所, 12-上交所固定收益平台,18-深交所综合收益平台,21-上交所大宗交易，22-上交所综合业务平台定转交易，30-北京证券交易所，81-三板市场

### TradeType (交易方式)

交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1517，得到交易方式的具体描述：10-净价交易，20-全价交易。

### IfTrading (当日是否交易)

当日是否交易(IfTrading)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到当日是否交易的具体描述：1-是，2-否。

### TurnoverDeals (成交笔数(笔))

对历史券，由于行情传输文件中经常出现不提供成交笔数的情况，本表对【成交笔数 TurnoverDeals】字段进行了赋0填充。
2021-2-24开始，本字段逻辑修改为显示传输文件原始值，若原始文件为null，则本表【成交笔数 TurnoverDeals】字段也为null

## SQL示例

```sql
-- 查询 债券基础行情表 数据
SELECT *
FROM bond_basicquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
