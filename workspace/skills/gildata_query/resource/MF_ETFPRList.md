# MF_ETFPRList

**中文名**: 公募基金ETF申购赎回清单信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ETFPRList` |
| MySQL表名 | `mf_etfprlist` |
| 中文名 | 公募基金ETF申购赎回清单信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > ETF类别 |
| 更新频率 | 日更新 |
| 字段数量 | 32 |
| 版本 | 1.01 |

## 表描述

1.本表收录ETF基金每个交易日公布的ETF申购赎回清单，包括是否允许赎回、是否允许申购，及单个账户申购、赎回上限等信息。
2.历史数据：2008年4月起-至今。
3.数据来源：基金公司官网和交易所官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `PrimaryMarketCode` | 一级市场基金代码 | varchar2(20) | ✓ | 99.99% |  |
| 6 | `TargetIndexCode` | 标的指数代码 | varchar2(20) | ✓ | 94.91% |  |
| 7 | `TargetIndexInnerCode` | 标的指数内部编码 | number(10) | ✓ | 94.91% | 标的指数编码（TargetIndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（Inne... |
| 8 | `PreviousTradingDate` | 上一交易日期 | date | ✓ | 100.0% |  |
| 9 | `CashBalance` | 现金差额(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `NAVPerLeastPRUnit` | 最小申赎单位资产净值(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `NAVPerShare` | 基金份额净值(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `CashForecasted` | 预估现金部分(元) | number(19,4) | ✓ | 100.0% |  |
| 13 | `CashSubstituteProportion` | 现金替代比例上限 | number(19,8) | ✓ | 100.0% |  |
| 14 | `LeastRedemptionUnit` | 最小申赎单位(份) | number(10) | ✓ | 100.0% |  |
| 15 | `DividendForLRU` | 最小申赎单位分红金额(元) | number(19,4) | ✓ | 30.96% |  |
| 16 | `IfIOPVDescription` | 是否需要公布IOPV描述 | varchar2(100) | ✓ | 100.0% |  |
| 17 | `IfPuschasableDescrip` | 是否允许申购描述 | varchar2(100) | ✓ | 100.0% |  |
| 18 | `IfRedeemableDescrip` | 是否允许赎回描述 | varchar2(100) | ✓ | 100.0% |  |
| 19 | `IfIOPV` | 是否需要公布IOPV | number(10) | ✓ | 100.0% | 是否需要公布IOPV(IfIOPV)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND D... |
| 20 | `IfPuschasable` | 是否允许申购 | number(10) | ✓ | 100.0% | 是否允许申购(IfPuschasable)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AN... |
| 21 | `IfRedeemable` | 是否允许赎回 | number(10) | ✓ | 100.0% | 是否允许赎回(IfRedeemable)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 22 | `PurchaseUL` | 申购份额上限(份) | number(19,0) | ✓ | 20.91% | 申购份额上限（份）（PurchaseUL）：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可申购... |
| 23 | `RedemptionUL` | 赎回份额上限(份) | number(19,0) | ✓ | 86.85% | 赎回份额上限（份）(RedemptionUL)：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可... |
| 24 | `SglAccPurACUL` | 单个账户当日累计申购上限(份) | number(19,0) | ✓ | 0.66% | 单个账户当日累计申购上限（份）(SglAccPurACUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 25 | `SglAccReACUL` | 单个账户当日累计赎回上限(份) | number(19,0) | ✓ | 1.19% | 单个账户当日累计赎回上限（份）(SglAccReACUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 26 | `NetPurUL` | 净申购份额上限(份) | number(19,6) | ✓ | 1.65% | 净申购份额上限（份）(NetPurUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 27 | `NetReUL` | 净赎回份额上限(份) | number(19,6) | ✓ | 1.84% | 净赎回份额上限（份）(NetReUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 28 | `SglAccNetPurUL` | 单个账户当日净申购上限(份) | number(19,6) | ✓ | 0.83% | 单个账户当日净申购上限（份）(SglAccNetPurUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 29 | `SglAccNetReUL` | 单个账户当日净赎回上限(份) | number(19,6) | ✓ | 1.05% | 单个账户当日净赎回上限（份）(SglAccNetReUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 30 | `IOPV` | IOPV收盘价 | number(19,4) | ✓ | 77.35% |  |
| 31 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到ETF的交易代码、简称等。

### TargetIndexInnerCode (标的指数内部编码)

标的指数编码（TargetIndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到ETF所追踪的指数的交易代码、简称等。

### IfIOPV (是否需要公布IOPV)

是否需要公布IOPV(IfIOPV)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否需要公布IOPV的具体描述：1-是，2-否。

### IfPuschasable (是否允许申购)

是否允许申购(IfPuschasable)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否允许申购的具体描述：1-是，2-否。

### IfRedeemable (是否允许赎回)

是否允许赎回(IfRedeemable)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否允许赎回的具体描述：1-是，2-否。

### PurchaseUL (申购份额上限(份))

申购份额上限（份）（PurchaseUL）：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可申购的基金份额上限。

### RedemptionUL (赎回份额上限(份))

赎回份额上限（份）(RedemptionUL)：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可赎回的基金份额上限。

### SglAccPurACUL (单个账户当日累计申购上限(份))

单个账户当日累计申购上限（份）(SglAccPurACUL)：统计对象为深圳证券交易所上市交易的ETF。

### SglAccReACUL (单个账户当日累计赎回上限(份))

单个账户当日累计赎回上限（份）(SglAccReACUL)：统计对象为深圳证券交易所上市交易的ETF。

### NetPurUL (净申购份额上限(份))

净申购份额上限（份）(NetPurUL)：统计对象为深圳证券交易所上市交易的ETF。

## SQL示例

```sql
-- 查询 公募基金ETF申购赎回清单信息 数据
SELECT *
FROM mf_etfprlist
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
