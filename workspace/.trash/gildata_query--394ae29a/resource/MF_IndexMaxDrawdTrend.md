# MF_IndexMaxDrawdTrend

**中文名**: 重要指数最大回撤走势

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IndexMaxDrawdTrend` |
| MySQL表名 | `mf_indexmaxdrawdtrend` |
| 中文名 | 重要指数最大回撤走势 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.本表记录基金跟踪的重要指数的动态回撤趋势表现，包括一个月、三个月、半年、一年、三年、五年、今年以来的重要指数的最大回撤走势。
2.历史数据：1998年3月起-至今。
3.信息来源：根据指数行情数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `ClosePrice` | 收盘价(元/点) | number(19,10) | ✓ | 100.0% |  |
| 5 | `InSingleMonth` | 截止日1月前 | number(19,10) | ✓ | 1.86% |  |
| 6 | `InThreeMonth` | 截止日3月前 | number(19,10) | ✓ | 4.97% |  |
| 7 | `InSixMonth` | 截止日6月前 | number(19,10) | ✓ | 10.31% |  |
| 8 | `InSingleYear` | 截止日1年前 | number(19,10) | ✓ | 20.03% |  |
| 9 | `InThreeYear` | 截止日3年前 | number(19,10) | ✓ | 60.12% |  |
| 10 | `InFiveYear` | 截止日5年前 | number(19,10) | ✓ | 100.0% |  |
| 11 | `SinceThisYear` | 今年以来 | number(19,10) | ✓ | 18.9% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 重要指数最大回撤走势 数据
SELECT *
FROM mf_indexmaxdrawdtrend
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
