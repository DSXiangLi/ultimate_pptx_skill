# LC_ZHSCTradeStat

**中文名**: 深港通交易统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ZHSCTradeStat` |
| MySQL表名 | `lc_zhsctradestat` |
| 中文名 | 深港通交易统计 |
| 路径 | 聚源新版数据库 > 专题数据库 > 深港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 42 |
| 版本 | 1.04 |

## 表描述

1.收录深港通业务中，深股通和港深股通交易的日、周、月、年四个维度下成交量、成交额的统计信息。
2.数据范围：2016年12月起-至今
3.信息来源：聚源按照深交所、港交所披露整理
区间说明：
1) 周：自然周；月：自然月；年：自然年；2) 区间数据披露值在区间结束后港交所才会披露相应数值；计算值每日更新。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ReportPeriod` | 数据统计区间 | number(10) | ✗ | 100.0% | 数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 and... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 and DM ... |
| 5 | `IfAdjusted` | 是否为计算值 | number(10) | ✗ | 100.0% | 是否为计算值(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 and ... |
| 6 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM i... |
| 7 | `BTradeValue` | 买入成交额(元) | number(19,4) | ✓ | 92.44% |  |
| 8 | `BTradeAmount` | 买入成交数目 | number(18,2) | ✓ | 92.44% |  |
| 9 | `STradeValue` | 卖出成交额(元) | number(19,4) | ✓ | 92.44% |  |
| 10 | `STradeAmount` | 卖出成交数目 | number(18,2) | ✓ | 92.44% |  |
| 11 | `TradValSum` | 买入及卖出成交额(元) | number(18,2) | ✓ | 100.0% |  |
| 12 | `TradAmountSum` | 买入及卖出成交数目 | number(18,2) | ✓ | 99.89% |  |
| 13 | `TradValNetSum` | 买入成交净额(元) | number(18,2) | ✓ | 92.44% |  |
| 14 | `AccuTradValNetSum` | 累计买入成交净额(元) | number(18,2) | ✓ | 92.53% |  |
| 15 | `ETFTradValSum` | ETF买入及卖出成交额(元) | number(18,2) | ✓ | 38.6% |  |
| 16 | `BTradeValue_DA` | 日均买入成交额(元) | number(19,4) | ✓ | 23.08% | 日均买入成交额(元)(BTradeValue_DA)：∑区间买入成交额/∑区间交易日天数 |
| 17 | `BTradeAmount_DA` | 日均买入成交数目 | number(18,2) | ✓ | 23.08% | 日均买入成交数目(BTradeAmount_DA)：∑区间买入成交数目/∑区间交易日天数 |
| 18 | `STradeValue_DA` | 日均卖出成交额(元) | number(19,4) | ✓ | 23.08% | 日均卖出成交额(元)(STradeValue_DA)：∑区间卖出成交额/∑区间交易日天数 |
| 19 | `STradeAmount_DA` | 日均卖出成交数目 | number(18,2) | ✓ | 23.08% | 日均卖出成交数目(STradeAmount_DA)：∑区间卖出成交数目/∑区间交易日天数 |
| 20 | `TradValSum_DA` | 日均买入及卖出成交额(元) | number(18,2) | ✓ | 25.06% | 日均买入及卖出成交额(元)(TradValSum_DA)：∑区间买入及卖出成交额/∑区间交易日天数 |
| 21 | `TradAmountSum_DA` | 日均买入及卖出成交数目 | number(18,2) | ✓ | 25.06% | 日均买入及卖出成交数目(TradAmountSum_DA)：∑区间买入及卖出成交数目/∑区间交易日天数 |
| 22 | `TradValNetSum_DA` | 日均买入成交净额(元) | number(18,2) | ✓ | 23.08% | 日均买入成交净额(元)(TradValNetSum_DA)：∑区间买入成交净额/∑区间交易日天数 |
| 23 | `ETFTradValSum_DA` | 日均ETF买入及卖出成交额(元) | number(18,2) | ✓ | 9.46% | 日均ETF买入及卖出成交额(元)(ETFTradValSum_DA)：∑区间ETF买入及卖出成交额/∑区间交易日天数 |
| 24 | `BTradeValueChange` | 买入成交额增减 | number(13,4) | ✓ | 22.34% | 买入成交额增减(%)(BTradeValueChange)：相同区间买入成交额环比-1 |
| 25 | `BTradeValueChange_DA` | 日均买入成交额增减 | number(13,4) | ✓ | 22.34% | 日均买入成交额增减(%)(BTradeValueChange_DA)：相同区间日均买入成交额环比-1 |
| 26 | `BTradeAmountChange` | 买入成交数目增减 | number(13,4) | ✓ | 22.34% | 买入成交数目增减(%)(BTradeAmountChange)：相同区间买入成交数目环比-1 |
| 27 | `BTradeAmountChange_DA` | 日均买入成交数目增减 | number(13,4) | ✓ | 22.34% | 日均买入成交数目增减(%)(BTradeAmountChange_DA)：相同区间日均买入成交数目环比-1 |
| 28 | `STradeValueChange` | 卖出成交额增减 | number(13,4) | ✓ | 22.34% | 卖出成交额增减(%)(STradeValueChange)：相同区间卖出成交额环比-1 |
| 29 | `STradeValueChange_DA` | 日均卖出成交额增减 | number(13,4) | ✓ | 22.34% | 日均卖出成交额增减(%)(STradeValueChange_DA)：相同区间日均卖出成交额环比-1 |
| 30 | `STradeAmountChange` | 卖出成交数目增减 | number(13,4) | ✓ | 22.34% | 卖出成交数目增减(%)：相同区间日均卖出成交数目环比-1 |
| 31 | `STradeAmountChange_DA` | 日均卖出成交数目增减 | number(13,4) | ✓ | 22.34% | 	 日均卖出成交数目增减(%)(STradeAmountChange_DA)：相同区间日均卖出成交数目环比-1 |
| 32 | `TradValSumChange` | 买入及卖出成交额增减 | number(13,4) | ✓ | 24.21% | 买入及卖出成交额增减(%)(TradValSumChange)：相同区间买入及卖出成交额环比-1 |
| 33 | `TradValSumChange_DA` | 日均买入及卖出成交额增减 | number(13,4) | ✓ | 24.21% | 日均买入及卖出成交额增减(%)(TradValSumChange_DA)：相同区间日均买入及卖出成交额环比-1 |
| 34 | `TradAmountSumChange` | 买入及卖出成交数目增减 | number(13,4) | ✓ | 24.21% | 买入及卖出成交数目增减(%)(TradAmountSumChange)：相同区间买入及卖出成交数目环比-1 |
| 35 | `TradAmountSumChange_DA` | 日均买入及卖出成交数目增减 | number(13,4) | ✓ | 24.21% | 日均买入及卖出成交数目增减(%)(TradAmountSumChange_DA)：相同区间日均买入及卖出成交数目环比-1 |
| 36 | `TradValNetSumChange` | 买入成交净额增减 | number(13,4) | ✓ | 22.52% | 买入成交净额增减(%)(TradValNetSumChange)：相同区间买入成交净额环比-1 |
| 37 | `TradValNetSumChange_DA` | 日均买入成交净额增减 | number(13,4) | ✓ | 22.52% | 日均买入成交净额增减(%)(TradValNetSumChange_DA)：相同区间日均买入成交净额环比-1 |
| 38 | `ETFTradValSumChange` | ETF买入及卖出成交额增减 | number(13,4) | ✓ | 9.17% | ETF买入及卖出成交额增减(%)(ETFTradValSumChange)：相同区间ETF买入及卖出成交额环比-1 |
| 39 | `ETFTradValSumChange_DA` | 日均ETF买入及卖出成交额增减 | number(13,4) | ✓ | 9.17% | 日均ETF买入及卖出成交额增减(%)(ETFTradValSumChange_DA)：相同区间日均ETF买入及卖出成交额... |
| 40 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 41 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 42 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ReportPeriod (数据统计区间)

数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 and DM IN (27,28,29,32)，得到数据统计区间的具体描述：27-年，28-月，29-日，32-周。

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB=1844 and DM in (3,4) ，得到交易方向的具体描述。
3-深股通，4-港股通（深）

### IfAdjusted (是否为计算值)

是否为计算值(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 and DM in (1,2)，得到是否为计算值的具体描述：1-是，2-否。

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1100,1420)，得到货币单位的具体描述：1100-港元，1420-人民币元。

### BTradeValue_DA (日均买入成交额(元))

日均买入成交额(元)(BTradeValue_DA)：∑区间买入成交额/∑区间交易日天数

### BTradeAmount_DA (日均买入成交数目)

日均买入成交数目(BTradeAmount_DA)：∑区间买入成交数目/∑区间交易日天数

### STradeValue_DA (日均卖出成交额(元))

日均卖出成交额(元)(STradeValue_DA)：∑区间卖出成交额/∑区间交易日天数

### STradeAmount_DA (日均卖出成交数目)

日均卖出成交数目(STradeAmount_DA)：∑区间卖出成交数目/∑区间交易日天数

### TradValSum_DA (日均买入及卖出成交额(元))

日均买入及卖出成交额(元)(TradValSum_DA)：∑区间买入及卖出成交额/∑区间交易日天数

### TradAmountSum_DA (日均买入及卖出成交数目)

日均买入及卖出成交数目(TradAmountSum_DA)：∑区间买入及卖出成交数目/∑区间交易日天数

## SQL示例

```sql
-- 查询 深港通交易统计 数据
SELECT *
FROM lc_zhsctradestat
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
