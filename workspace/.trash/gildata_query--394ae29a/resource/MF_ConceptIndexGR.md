# MF_ConceptIndexGR

**中文名**: 概念标签指数收益率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ConceptIndexGR` |
| MySQL表名 | `mf_conceptindexgr` |
| 中文名 | 概念标签指数收益率 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：计算A股聚源概念板块（二级、三级）的收益表现。应用场景为，获取 <公募基金主题标签变动 MF_ThemeTagChange> 中，基金标签所属的股票概念板块，近期的收益表现。包括日、周、月、季、半年、一年、二年、三年等周期表现。
2.数据范围：2016年8月-至今。
3.信息来源：根据行情数据<公募基金概念标签指数行情 MF_ConceptIndexQuote>计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ConceptCode` | 概念代码 | number(10) | ✗ | 100.0% | 概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptC... |
| 3 | `ConceptName` | 概念名称 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `ConceptLevel` | 概念级别 | number(10) | ✗ | 100.0% |  |
| 5 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 6 | `DailyGR` | 日收益率(%) | number(18,6) | ✓ | 99.93% |  |
| 7 | `RRInSelectedWeek` | 本周以来回报率(%) | number(18,6) | ✓ | 99.89% |  |
| 8 | `RRInSingleWeek` | 一周回报率(%) | number(18,6) | ✓ | 99.73% |  |
| 9 | `RRInSelectedMonth` | 本月以来回报率(%) | number(18,6) | ✓ | 99.41% |  |
| 10 | `RRInSingleMonth` | 一个月回报率(%) | number(18,6) | ✓ | 98.7% |  |
| 11 | `RRInThreeMonth` | 三个月回报率(%) | number(18,6) | ✓ | 96.19% |  |
| 12 | `RRInSixMonth` | 六个月回报率(%) | number(18,6) | ✓ | 92.33% |  |
| 13 | `RRInNineMonth` | 九个月回报率(%) | number(18,6) | ✓ | 88.57% |  |
| 14 | `RRSinceThisYear` | 今年以来回报率(%) | number(18,6) | ✓ | 92.35% |  |
| 15 | `RRInSingleYear` | 一年回报率(%) | number(18,6) | ✓ | 84.79% |  |
| 16 | `RRSinceStart` | 设立以来回报率(%) | number(18,6) | ✓ | 99.92% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ConceptCode (概念代码)

概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。

## SQL示例

```sql
-- 查询 概念标签指数收益率 数据
SELECT *
FROM mf_conceptindexgr
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
