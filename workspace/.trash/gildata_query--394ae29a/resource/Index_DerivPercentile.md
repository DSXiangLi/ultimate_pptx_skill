# Index_DerivPercentile

**中文名**: 指数衍生指标分位数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_DerivPercentile` |
| MySQL表名 | `index_derivpercentile` |
| 中文名 | 指数衍生指标分位数 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1.04 |

## 表描述

1.内容说明：本表记录A股、港股主要指数衍生指标的百分位，包括滚动市盈率、市净率等指标每天所处的历史分位情况；以及30%分位和70%等分位对应的分位值。当滚动市盈率、市净率为负时，不会计算相应的分位数。
2.数据范围：指数上市日期至今
3.信息来源：聚源计算得到

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode = In... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `IndicatorType` | 指标类型 | number(10) | ✗ | 100.0% | 指标类型(IndicatorType)：1-PE_TTM，2-PB_LF |
| 5 | `StatisPeriod` | 统计周期 | number(10) | ✓ | 100.0% | 统计周期(StatisPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND ... |
| 6 | `IndiPercentile` | 指标分位数(%) | number(19,4) | ✓ | 100.0% |  |
| 7 | `Indi10PercentileV` | 指标10%分位值 | number(19,4) | ✓ | 100.0% |  |
| 8 | `Indi20PercentileV` | 指标20%分位值 | number(19,4) | ✓ | 100.0% |  |
| 9 | `Indi25PercentileV` | 指标25%分位值 | number(19,4) | ✓ | 100.0% |  |
| 10 | `Indi30PercentileV` | 指标30%分位值 | number(19,4) | ✓ | 100.0% |  |
| 11 | `Indi40PercentileV` | 指标40%分位值 | number(19,4) | ✓ | 100.0% |  |
| 12 | `Indi50PercentileV` | 指标50%分位值 | number(19,4) | ✓ | 100.0% |  |
| 13 | `Indi60PercentileV` | 指标60%分位值 | number(19,4) | ✓ | 100.0% |  |
| 14 | `Indi70PercentileV` | 指标70%分位值 | number(19,4) | ✓ | 100.0% |  |
| 15 | `Indi75PercentileV` | 指标75%分位值 | number(19,4) | ✓ | 100.0% |  |
| 16 | `Indi80PercentileV` | 指标80%分位值 | number(19,4) | ✓ | 100.0% |  |
| 17 | `Indi90PercentileV` | 指标90%分位值 | number(19,4) | ✓ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode = InnerCode，得到指数内部编码的具体描述：

### IndicatorType (指标类型)

指标类型(IndicatorType)：1-PE_TTM，2-PB_LF

### StatisPeriod (统计周期)

统计周期(StatisPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM in (3,6,12,24,36,60,120,998,999)，得到统计周期的具体描述：3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

## SQL示例

```sql
-- 查询 指数衍生指标分位数 数据
SELECT *
FROM index_derivpercentile
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
