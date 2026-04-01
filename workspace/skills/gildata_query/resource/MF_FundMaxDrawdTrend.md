# MF_FundMaxDrawdTrend

**中文名**: 基金最大回撤走势

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundMaxDrawdTrend` |
| MySQL表名 | `mf_fundmaxdrawdtrend` |
| 中文名 | 基金最大回撤走势 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.本表记录基金的动态回撤趋势表现，包括一个月、三个月、半年、一年、三年、五年、今年以来、成立以来的最大回撤走势。本表对于基金发生转型，仍将转型前后当作一只基金考虑。
2.历史数据：1998年3月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值(元) | number(19,10) | ✓ | 100.0% |  |
| 5 | `UnitNVRestored` | 复权单位净值 | number(19,10) | ✓ | 100.0% |  |
| 6 | `InSingleMonth` | 截止日1月前 | number(19,10) | ✓ | 1.95% |  |
| 7 | `InThreeMonth` | 截止日3月前 | number(19,10) | ✓ | 5.08% |  |
| 8 | `InSixMonth` | 截止日6月前 | number(19,10) | ✓ | 10.16% |  |
| 9 | `InSingleYear` | 截止日1年前 | number(19,10) | ✓ | 18.4% |  |
| 10 | `InThreeYear` | 截止日3年前 | number(19,10) | ✓ | 39.55% |  |
| 11 | `InFiveYear` | 截止日5年前 | number(19,10) | ✓ | 38.58% |  |
| 12 | `SinceThisYear` | 今年以来 | number(19,10) | ✓ | 16.58% |  |
| 13 | `SinceStart` | 成立以来 | number(19,10) | ✓ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 基金最大回撤走势 数据
SELECT *
FROM mf_fundmaxdrawdtrend
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
