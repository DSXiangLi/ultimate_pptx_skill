# Bond_CBLiquidityLQI

**中文名**: 中债流动性指标(LQI)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBLiquidityLQI` |
| MySQL表名 | `bond_cbliquiditylqi` |
| 中文名 | 中债流动性指标(LQI) |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1.02 |

## 表描述

1.内容说明：本表记录中债估值中心根据中债LQI模型发布的中债流动性指标
2.数据范围：2023年1月3日至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `BondType` | 债券类别 | number(10) | ✓ | 100.0% | 债券类别(BondType)与(Bond_SystemConst)表中的DM字段关联，令LB = 40 and DM i... |
| 5 | `LiquidityScore` | 流动性指标 | number(18,8) | ✓ | 100.0% |  |
| 6 | `LiquidityPercentile` | 流动性指标分位数(%) | number(18,8) | ✓ | 100.0% |  |
| 7 | `LiquidityRank` | 流动性指标排名 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `LiquidityRankChange` | 流动性指标排名较上月末变化 | number(10) | ✓ | 97.78% |  |
| 9 | `TradePercentile` | 成交因子分位数(%) | number(18,8) | ✓ | 100.0% |  |
| 10 | `TradeRank` | 成交因子排名 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `TradeRankChange` | 成交因子排名较上月末变化 | number(10) | ✓ | 97.78% |  |
| 12 | `QuotePercentile` | 报价因子分位数(%) | number(18,8) | ✓ | 100.0% |  |
| 13 | `QuoteRank` | 报价因子排名 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `QuoteRankChange` | 报价因子排名较上月末变化 | number(10) | ✓ | 97.78% |  |
| 15 | `FeaturePercentile` | 债券特征因子分位数(%) | number(18,8) | ✓ | 100.0% |  |
| 16 | `FeatureRank` | 债券特征因子排名 | varchar2(100) | ✓ | 100.0% |  |
| 17 | `FeatureRankChange` | 债券特征因子排名较上月末变化 | number(10) | ✓ | 97.78% |  |
| 18 | `LiquidityGrade` | 流动性指标评价等级 | varchar2(10) | ✓ | 30.21% |  |
| 19 | `TurnoverRatePerDay` | 日均换手率(%) | number(18,8) | ✓ | 30.21% |  |
| 20 | `TransactionNumPerDay` | 日均成交笔数 | number(10) | ✓ | 30.21% |  |
| 21 | `TradeDays` | 成交天数 | number(10) | ✓ | 30.21% |  |
| 22 | `QuotesCountPerDay` | 日均报价笔数 | number(10) | ✓ | 30.21% |  |
| 23 | `QuotesSpread` | 报价价差(BP) | number(18,8) | ✓ | 11.75% |  |
| 24 | `ListedYears` | 已上市时间(年) | number(18,8) | ✓ | 30.21% |  |
| 25 | `TotalSize` | 债券余额(亿) | number(18,8) | ✓ | 30.21% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

### BondType (债券类别)

债券类别(BondType)与(Bond_SystemConst)表中的DM字段关联，令LB = 40 and DM in (4001,4002)，得到债券类别的具体描述：4001-利率债，4002-信用债。

## SQL示例

```sql
-- 查询 中债流动性指标(LQI) 数据
SELECT *
FROM bond_cbliquiditylqi
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
