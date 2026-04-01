# MF_BenchmarkGRTrans

**中文名**: 公募基金基准收益率(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BenchmarkGRTrans` |
| MySQL表名 | `mf_benchmarkgrtrans` |
| 中文名 | 公募基金基准收益率(转型) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金的基准收益率，包括周、一个月、三个月、半年、一年、二年、三年、五年、十年、成立以来的回报。
2.历史数据：1998年3月起-至今。
3.信息来源：根据指数行情数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `DailyBenchGR` | 本日基金基准增长率(%) | number(18,10) | ✓ | 99.99% |  |
| 5 | `BenchGRForThisWeek` | 本周以来基金基准增长率(%) | number(18,10) | ✓ | 98.74% |  |
| 6 | `WeeklyBenchGR` | 一周基金基准增长率(%) | number(18,10) | ✓ | 99.66% |  |
| 7 | `BenchGRForThisMonth` | 本月以来基金基准增长率(%) | number(18,10) | ✓ | 100.0% |  |
| 8 | `MonthlyBenchGR` | 一个月基金基准增长率(%) | number(18,10) | ✓ | 98.31% |  |
| 9 | `BenchGRFor4Week` | 滚动周(4周)净值增长率(%) | number(18,10) | ✓ | 89.66% |  |
| 10 | `BenchGRFor3Month` | 三个月基金基准增长率(%) | number(18,10) | ✓ | 94.92% |  |
| 11 | `BenchGRForThisQuarter` | 本季度以来基金基准增长率(%) | number(18,10) | ✓ | 100.0% |  |
| 12 | `BenchGRFor6Month` | 六个月基金基准增长率(%) | number(18,10) | ✓ | 89.94% |  |
| 13 | `BenchGRForThisYear` | 今年以来基金基准增长率(%) | number(18,10) | ✓ | 99.82% |  |
| 14 | `BenchGRFor1Year` | 一年基金基准增长率(%) | number(18,10) | ✓ | 80.47% |  |
| 15 | `BenchGRFor2Year` | 两年基金基准增长率(%) | number(18,10) | ✓ | 63.54% |  |
| 16 | `BenchGRFor3Year` | 三年基金基准增长率(%) | number(18,10) | ✓ | 49.31% |  |
| 17 | `BenchGRFor5Year` | 五年基金基准增长率(%) | number(18,10) | ✓ | 29.08% |  |
| 18 | `BenchGRFor7Year` | 七年基金基准增长率(%) | number(18,10) | ✓ | 17.0% |  |
| 19 | `BenchGRFor10Year` | 十年基金基准增长率(%) | number(18,10) | ✓ | 6.8% |  |
| 20 | `BenchGRForSince` | 成立以来基准增长率(%) | number(18,10) | ✓ | 99.99% |  |
| 21 | `AnnualizedBRForSince` | 成立以来基准年化增长率(%) | number(18,10) | ✓ | 78.02% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 公募基金基准收益率(转型) 数据
SELECT *
FROM mf_benchmarkgrtrans
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
