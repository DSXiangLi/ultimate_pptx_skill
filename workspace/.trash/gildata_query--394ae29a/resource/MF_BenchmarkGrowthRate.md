# MF_BenchmarkGrowthRate

**中文名**: 公募基金基准收益率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BenchmarkGrowthRate` |
| MySQL表名 | `mf_benchmarkgrowthrate` |
| 中文名 | 公募基金基准收益率 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金对应的基准的日收益率表现情况。
2.历史数据：2002年5月起-至今。
3.信息来源：聚源计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `DailyBenchGR` | 本日基金基准增长率(%) | float | ✓ | 100.0% |  |
| 5 | `BenchGRForThisWeek` | 本周以来基金基准增长率(%) | float | ✓ | 100.0% |  |
| 6 | `WeeklyBenchGR` | 一周基金基准增长率(%) | float | ✓ | 99.66% |  |
| 7 | `BenchGRForThisMonth` | 本月以来基金基准增长率(%) | float | ✓ | 100.0% |  |
| 8 | `MonthlyBenchGR` | 一个月基金基准增长率(%) | float | ✓ | 98.27% |  |
| 9 | `BenchGRFor4Week` | 滚动周(4周)净值增长率(%) | float | ✓ | 90.43% |  |
| 10 | `BenchGRFor3Month` | 三个月基金基准增长率(%) | float | ✓ | 94.78% |  |
| 11 | `BenchGRForThisQuarter` | 本季度以来基金基准增长率(%) | float | ✓ | 100.0% |  |
| 12 | `BenchGRFor6Month` | 六个月基金基准增长率(%) | float | ✓ | 89.66% |  |
| 13 | `BenchGRForThisYear` | 今年以来基金基准增长率(%) | float | ✓ | 100.0% |  |
| 14 | `BenchGRFor1Year` | 一年基金基准增长率(%) | float | ✓ | 79.94% |  |
| 15 | `BenchGRFor2Year` | 两年基金基准增长率(%) | float | ✓ | 62.6% |  |
| 16 | `BenchGRFor3Year` | 三年基金基准增长率(%) | float | ✓ | 48.04% |  |
| 17 | `BenchGRFor5Year` | 五年基金基准增长率(%) | float | ✓ | 27.5% |  |
| 18 | `BenchGRFor7Year` | 七年基金基准增长率(%) | float | ✓ | 15.63% |  |
| 19 | `BenchGRFor10Year` | 十年基金基准增长率(%) | float | ✓ | 6.26% |  |
| 20 | `BenchGRForSince` | 成立以来基准增长率(%) | float | ✓ | 100.0% |  |
| 21 | `AnnualizedBRForSince` | 成立以来基准年化增长率(%) | number(18,10) | ✓ | 79.87% |  |
| 22 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 23 | `UpdataTime` | 更新时间 | date | ✗ | 100.0% |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金基准收益率 数据
SELECT *
FROM mf_benchmarkgrowthrate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
