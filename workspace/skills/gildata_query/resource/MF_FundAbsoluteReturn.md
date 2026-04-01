# MF_FundAbsoluteReturn

**中文名**: 基金绝对收益

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundAbsoluteReturn` |
| MySQL表名 | `mf_fundabsolutereturn` |
| 中文名 | 基金绝对收益 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析 |
| 更新频率 | 日更新 |
| 字段数量 | 52 |
| 版本 | 1.02 |

## 表描述

1.内容说明：记录基金最高单月回报、最低单月回报、连涨月数、连跌月数以及最大盈利等指标，用于评价基金绝对收益能力
2.数据范围：2014年12月1日起-至今。
3.信息来源：根据基金每个交易日公布的复权单位净值计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB=2149 AND DM I... |
| 5 | `MonthlyHighestGR` | 最高单月回报(%) | number(18,4) | ✓ | 98.82% |  |
| 6 | `MonthlyLowestGR` | 最低单月回报(%) | number(18,4) | ✓ | 98.82% |  |
| 7 | `RisingUpMonth` | 连涨月数 | number(10) | ✓ | 98.82% |  |
| 8 | `FallingDownMonth` | 连跌月数 | number(10) | ✓ | 98.82% |  |
| 9 | `MaxRisingUpMonth` | 最长连涨月数 | number(10) | ✓ | 98.82% |  |
| 10 | `MaxRisingUpRange` | 最长连涨涨幅(%) | number(18,4) | ✓ | 98.63% |  |
| 11 | `MaxFallingM` | 最长连跌月数 | number(10) | ✓ | 86.65% |  |
| 12 | `MaxFallingRangeM` | 最长连跌跌幅(%) | number(24,10) | ✓ | 84.21% |  |
| 13 | `RiseToFallRatio` | 涨/跌月数比 | varchar2(100) | ✓ | 98.82% |  |
| 14 | `MonthlyCompoundGR` | 月度复合回报(%) | number(18,4) | ✓ | 98.82% |  |
| 15 | `MonthlyAverageGR` | 平均月度回报(%) | number(18,4) | ✓ | 98.82% |  |
| 16 | `QHighestGR` | 最高单季回报(%) | number(24,10) | ✓ | 70.94% |  |
| 17 | `QLowestGR` | 最低单季回报(%) | number(24,10) | ✓ | 70.94% |  |
| 18 | `RisingUpAvgM` | 上涨月份平均收益(%) | number(24,10) | ✓ | 82.91% |  |
| 19 | `FallingAvgM` | 下跌月份平均损失(%) | number(24,10) | ✓ | 75.05% |  |
| 20 | `RisingUpDays` | 连涨天数(日) | number(10) | ✓ | 87.82% |  |
| 21 | `FallingDays` | 连跌天数(日) | number(10) | ✓ | 87.82% |  |
| 22 | `MaxRisingUpD` | 最长连涨天数 | number(10) | ✓ | 87.82% |  |
| 23 | `MaxRisingRangeD` | 最长连涨涨幅(日)(%) | number(24,10) | ✓ | 87.75% |  |
| 24 | `MaxFallingD` | 最长连跌天数 | number(10) | ✓ | 87.82% |  |
| 25 | `MaxFallingRangeD` | 最长连跌跌幅(日)(%) | number(24,10) | ✓ | 87.09% |  |
| 26 | `RiseToFallRatioD` | 涨/跌天数比 | varchar2(100) | ✓ | 87.82% |  |
| 27 | `DProfitPer` | 盈利百分比(日) | number(24,10) | ✓ | 87.82% |  |
| 28 | `WProfitPer` | 盈利百分比(周) | number(24,10) | ✓ | 87.54% |  |
| 29 | `MProfitPer` | 盈利百分比(月) | number(24,10) | ✓ | 86.65% |  |
| 30 | `YProfitPer` | 盈利百分比(年) | number(24,10) | ✓ | 33.14% |  |
| 31 | `MonthlyProfitProb` | 月度盈利概率 | number(10,5) | ✓ | 98.88% |  |
| 32 | `ThreeMProfitProb` | 历史盈利概率-持有3个月 | number(24,10) | ✓ | 84.28% |  |
| 33 | `SixMProfitProb` | 历史盈利概率-持有6个月 | number(24,10) | ✓ | 66.87% |  |
| 34 | `YearProfitProb` | 历史盈利概率-持有一年 | number(24,10) | ✓ | 46.07% |  |
| 35 | `TwoYProfitProb` | 历史盈利概率-持有两年 | number(24,10) | ✓ | 31.98% |  |
| 36 | `ThreeYProfitProb` | 历史盈利概率-持有三年 | number(24,10) | ✓ | 20.48% |  |
| 37 | `ThreeMProfitMax` | 最高连续3月回报(%) | number(24,10) | ✓ | 84.28% |  |
| 38 | `SixMProfitMax` | 最高连续6月回报(%) | number(24,10) | ✓ | 66.87% |  |
| 39 | `YearProfitMax` | 最高连续12月回报(%) | number(24,10) | ✓ | 46.07% |  |
| 40 | `TwoYProfitMax` | 最高连续24月回报(%) | number(24,10) | ✓ | 31.98% |  |
| 41 | `ThreeYProfitMax` | 最高连续36月回报(%) | number(24,10) | ✓ | 20.48% |  |
| 42 | `ThreeMProfitMin` | 最差连续3月回报(%) | number(24,10) | ✓ | 84.28% |  |
| 43 | `SixMProfitMin` | 最差连续6月回报(%) | number(24,10) | ✓ | 66.87% |  |
| 44 | `YearProfitMin` | 最差连续12月回报(%) | number(24,10) | ✓ | 46.07% |  |
| 45 | `TwoYProfitMin` | 最差连续24月回报(%) | number(24,10) | ✓ | 31.98% |  |
| 46 | `ThreeYProfitMin` | 最差连续36月回报(%) | number(24,10) | ✓ | 20.48% |  |
| 47 | `MaxRet` | 最大盈利(%) | number(24,10) | ✓ | 87.76% |  |
| 48 | `MaxRetDate` | 最大盈利区间 | varchar2(100) | ✓ | 87.76% |  |
| 49 | `AccumProfit` | 累计盈利(万元) | number(18,4) | ✓ | 15.34% |  |
| 50 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 51 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 52 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB=2149 AND DM IN (3 ,6 ,12 ,24,36 ,60 ,120 ,998 ,999)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

## SQL示例

```sql
-- 查询 基金绝对收益 数据
SELECT *
FROM mf_fundabsolutereturn
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
