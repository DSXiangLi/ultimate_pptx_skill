# LC_SHSCTradeStat

**中文名**: 沪港通交易统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSCTradeStat` |
| MySQL表名 | `lc_shsctradestat` |
| 中文名 | 沪港通交易统计 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 42 |
| 版本 | 1.03 |

## 表描述

1.收录沪港通业务中，沪股通和港沪股通交易的日、周、月、年四个维度下成交量、成交额的统计信息。
2.历史数据：2014年11月起-至今
3.数据来源：聚源按照上交所、港交所披露整理
区间说明：
1) 周：自然周；月：自然月；年：自然年；2) 区间数据披露值在区间结束后港交所才会披露相应数值；计算值每日更新。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ReportPeriod` | 数据统计区间 | number(10) | ✗ | 100.0% | 数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 AND... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 AND DM ... |
| 5 | `IfAdjusted` | 是否为计算值 | number(10) | ✗ | 100.0% | 调整标志（IfAdjusted）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1... |
| 6 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM I... |
| 7 | `BTradeValue` | 买入成交额(元) | number(18,2) | ✓ | 93.84% |  |
| 8 | `BTradeAmount` | 买入成交数目 | number(18,2) | ✓ | 93.84% |  |
| 9 | `STradeValue` | 卖出成交额(元) | number(18,2) | ✓ | 93.84% |  |
| 10 | `STradeAmount` | 卖出成交数目 | number(18,2) | ✓ | 93.84% |  |
| 11 | `TradValSum` | 买入及卖出成交额(元) | number(18,2) | ✓ | 99.99% |  |
| 12 | `TradAmountSum` | 买入及卖出成交数目 | number(18,2) | ✓ | 99.9% |  |
| 13 | `TradValNetSum` | 买入成交净额(元) | number(18,2) | ✓ | 93.84% |  |
| 14 | `AccuTradValNetSum` | 累计买入成交净额(元) | number(18,2) | ✓ | 93.91% |  |
| 15 | `ETFTradValSum` | ETF买入及卖出成交额(元) | number(18,2) | ✓ | 31.48% |  |
| 16 | `BTradeValue_DA` | 日均买入成交额(元) | number(18,2) | ✓ | 23.44% | 日均买入成交额(元)(BTradeValue_DA)：∑区间买入成交额/∑区间交易日天数 |
| 17 | `BTradeAmount_DA` | 日均买入成交数目 | number(18,2) | ✓ | 23.44% | 日均买入成交数目(BTradeAmount_DA)：∑区间买入成交数目/∑区间交易日天数 |
| 18 | `STradeValue_DA` | 日均卖出成交额(元) | number(18,2) | ✓ | 23.44% | 日均卖出成交额(元)(STradeValue_DA)：∑区间卖出成交额/∑区间交易日天数 |
| 19 | `STradeAmount_DA` | 日均卖出成交数目 | number(18,2) | ✓ | 23.44% | 日均卖出成交数目(STradeAmount_DA)：∑区间卖出成交数目/∑区间交易日天数 |
| 20 | `TradValSum_DA` | 日均买入及卖出成交额(元) | number(18,2) | ✓ | 25.04% | ∑区间买入及卖出成交额/∑区间交易日天数 |
| 21 | `TradAmountSum_DA` | 日均买入及卖出成交数目 | number(18,2) | ✓ | 25.04% | ∑区间买入及卖出成交数目/∑区间交易日天数 |
| 22 | `TradValNetSum_DA` | 日均买入成交净额(元) | number(18,2) | ✓ | 23.44% | ∑区间买入成交净额/∑区间交易日天数 |
| 23 | `ETFTradValSum_DA` | 日均ETF买入及卖出成交额(元) | number(18,2) | ✓ | 7.72% | ∑区间ETF买入及卖出成交额/∑区间交易日天数 |
| 24 | `TradValSumChange` | 买入及卖出成交额增减 | number(13,4) | ✓ | 24.17% | 相同区间买入及卖出成交额环比-1 |
| 25 | `TradValSumChange_DA` | 日均买入及卖出成交额增减 | number(13,4) | ✓ | 24.17% | 相同区间日均买入及卖出成交额环比-1 |
| 26 | `TradAmountSumChange` | 买入及卖出成交数目增减 | number(13,4) | ✓ | 24.17% | 相同区间买入及卖出成交数目环比-1 |
| 27 | `TradAmountSumChange_DA` | 日均买入及卖出成交数目增减 | number(13,4) | ✓ | 24.17% | 相同区间日均买入及卖出成交数目环比-1 |
| 28 | `TradValNetSumChange` | 买入成交净额增减 | number(13,4) | ✓ | 22.88% | 相同区间买入成交净额环比-1 |
| 29 | `TradValNetSumChange_DA` | 日均买入成交净额增减 | number(13,4) | ✓ | 22.88% | 相同区间日均买入成交净额环比-1 |
| 30 | `BTradeValueChange` | 买入成交额增减 | number(13,4) | ✓ | 22.68% | 买入成交额增减(%)(BTradeValueChange)：相同区间买入成交额环比-1 |
| 31 | `BTradeValueChange_DA` | 日均买入成交额增减 | number(13,4) | ✓ | 22.68% | 日均买入成交额增减(%)(BTradeValueChange_DA)：相同区间日均买入成交额环比-1 |
| 32 | `BTradeAmountChange` | 买入成交数目增减 | number(13,4) | ✓ | 22.68% | 买入成交数目增减(%)(BTradeAmountChange)：相同区间买入成交数目环比-1 |
| 33 | `BTradeAmountChange_DA` | 日均买入成交数目增减 | number(13,4) | ✓ | 22.68% | 日均买入成交数目增减(%)(BTradeAmountChange_DA)：相同区间日均买入成交数目环比-1 |
| 34 | `STradeValueChange` | 卖出成交额增减 | number(13,4) | ✓ | 22.68% | 卖出成交额增减(%)(STradeValueChange)：相同区间卖出成交额环比-1 |
| 35 | `STradeValueChange_DA` | 日均卖出成交额增减 | number(13,4) | ✓ | 22.68% | 日均卖出成交额增减(%)(STradeValueChange_DA)：相同区间日均卖出成交额环比-1 |
| 36 | `STradeAmountChange` | 卖出成交数目增减 | number(13,4) | ✓ | 22.68% | 卖出成交数目增减(%)(STradeAmountChange)：相同区间卖出成交数目环比-1 |
| 37 | `STradeAmountChange_DA` | 日均卖出成交数目增减 | number(13,4) | ✓ | 22.68% | 日均卖出成交数目增减(%)(STradeAmountChange_DA)：相同区间日均卖出成交数目环比-1 |
| 38 | `ETFTradValSumChange` | ETF买入及卖出成交额增减 | number(13,4) | ✓ | 7.48% | 相同区间ETF买入及卖出成交额环比-1 |
| 39 | `ETFTradValSumChange_DA` | 日均ETF买入及卖出成交额增减 | number(13,4) | ✓ | 7.48% | 相同区间日均ETF买入及卖出成交额环比-1 |
| 40 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 41 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 42 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ReportPeriod (数据统计区间)

数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 AND DM IN (27,28,29,32)，得到数据统计区间的具体描述：27-年，28-月，29-日，32-周。

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 AND DM IN (1,2)，得到交易类型的具体描述：1-沪股通，2-港股通（沪）。

### IfAdjusted (是否为计算值)

调整标志（IfAdjusted）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1188”，得到具体的调整标志。1-是2-否

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1100,1420)，得到货币单位的具体描述：1100-港元，1420-人民币元。

### BTradeValue_DA (日均买入成交额(元))

日均买入成交额(元)(BTradeValue_DA)：∑区间买入成交额/∑区间交易日天数

### BTradeAmount_DA (日均买入成交数目)

日均买入成交数目(BTradeAmount_DA)：∑区间买入成交数目/∑区间交易日天数

### STradeValue_DA (日均卖出成交额(元))

日均卖出成交额(元)(STradeValue_DA)：∑区间卖出成交额/∑区间交易日天数

### STradeAmount_DA (日均卖出成交数目)

日均卖出成交数目(STradeAmount_DA)：∑区间卖出成交数目/∑区间交易日天数

### TradValSum_DA (日均买入及卖出成交额(元))

∑区间买入及卖出成交额/∑区间交易日天数

### TradAmountSum_DA (日均买入及卖出成交数目)

∑区间买入及卖出成交数目/∑区间交易日天数

## SQL示例

```sql
-- 查询 沪港通交易统计 数据
SELECT *
FROM lc_shsctradestat
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
