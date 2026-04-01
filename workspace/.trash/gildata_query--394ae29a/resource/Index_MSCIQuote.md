# Index_MSCIQuote

**中文名**: MSCI指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_MSCIQuote` |
| MySQL表名 | `index_msciquote` |
| 中文名 | MSCI指数行情 |
| 路径 | 聚源新版数据库 > 产品代理 > MSCI代理数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 34 |
| 版本 | 1 |

## 表描述

内容说明：MSCI指数行情收录收盘价、涨跌幅、市值、成份数量、再平衡日期、除数、股息点等数据。
数据范围：2003年1月至今
信息来源：MSCI

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `PrevClosePrice` | 昨收盘 | number(26,6) | ✓ | 99.99% |  |
| 5 | `ClosePrice` | 收盘价 | number(26,6) | ✓ | 100.0% |  |
| 6 | `ChangePCT` | 涨跌幅(%) | number(26,6) | ✓ | 98.59% |  |
| 7 | `DailyYield` | 股息收益率 | number(26,6) | ✓ | 12.72% |  |
| 8 | `HighestPrice` | 设立以来最高价 | number(26,6) | ✓ | 1.98% |  |
| 9 | `LowestPrice` | 设立以来最低价 | number(26,6) | ✓ | 1.98% |  |
| 10 | `InitialMV` | 初始市值(万元) | number(28,4) | ✓ | 53.08% |  |
| 11 | `AdjustedMV` | 调整市值(万元) | number(28,4) | ✓ | 53.08% |  |
| 12 | `CloseMV` | 收盘市值(万元) | number(28,4) | ✓ | 53.08% |  |
| 13 | `NDInitialMV` | 次日初始市值(万元) | number(28,4) | ✓ | 37.19% |  |
| 14 | `ComponentMVAvg` | 指数成份平均市值(万元) | number(28,4) | ✓ | 44.0% |  |
| 15 | `ComponentMVMed` | 指数成份市值中位数(万元) | number(28,4) | ✓ | 44.3% |  |
| 16 | `CloseMVII` | 收盘市值2(万元) | number(28,4) | ✓ | 2.71% |  |
| 17 | `MVCurrencyCode` | 收盘市值币种 | number(10) | ✓ | 42.76% |  |
| 18 | `Divisor` | 指数除数 | number(30,2) | ✓ | 54.93% |  |
| 19 | `NDDivisor` | 次日指数除数 | number(30,2) | ✓ | 38.73% |  |
| 20 | `IndexNC` | 指数成份股数量 | number(10) | ✓ | 99.99% |  |
| 21 | `IssuerSum` | 成份发行人数量 | number(10) | ✓ | 98.02% |  |
| 22 | `GroupSum` | 成份发行集团数量 | number(10) | ✓ | 90.07% |  |
| 23 | `LastRebalancingDate` | 最近成份调整日 | date | ✓ | 82.41% |  |
| 24 | `NextRebalancingDate` | 下一成份调整日 | date | ✓ | 16.37% |  |
| 25 | `DivPts` | 总股息点 | number(25,15) | ✓ | 43.03% |  |
| 26 | `NDDivPts` | 次日总股息点 | number(25,15) | ✓ | 32.65% |  |
| 27 | `NetDivPts` | 净股息点 | number(25,15) | ✓ | 42.99% |  |
| 28 | `NDNetDivPts` | 次日净股息点 | number(25,15) | ✓ | 32.32% |  |
| 29 | `FullIssuerMVCutoffUSD` | 昨日细分市场规模(万美元) | number(28,4) | ✓ | 3.17% |  |
| 30 | `GlobalMinSizeRefUSD` | 最小市值参照水平(万美元) | number(28,4) | ✓ | 7.6% |  |
| 31 | `SegTargetCompNum` | 目标市值对应公司数量 | number(10) | ✓ | 5.18% |  |
| 32 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 33 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 34 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

## SQL示例

```sql
-- 查询 MSCI指数行情 数据
SELECT *
FROM index_msciquote
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
