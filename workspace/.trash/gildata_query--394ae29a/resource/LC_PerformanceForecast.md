# LC_PerformanceForecast

**中文名**: 业绩预告

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PerformanceForecast` |
| MySQL表名 | `lc_performanceforecast` |
| 中文名 | 业绩预告 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 不定时更新 |
| 字段数量 | 29 |
| 版本 | 1.05 |

## 表描述

1.收录上市公司对未来报告期本公司业绩的预计情况，包括业绩预计类型、预计内容、具体预计值等。
2.数据范围：1998-12-31至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 业绩预计报告期 | date | ✗ | 100.0% |  |
| 5 | `ForcastType` | 业绩预计类型 | number(10) | ✓ | 100.0% | 业绩预计类型(ForcastType)：1-预亏，2-不确定，3-预盈，4-预增，5-预平，6-经营计划，7-减亏，8-... |
| 6 | `ResultStatement` | 业绩预计结果说明 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `ForcastContent` | 业绩预计内容描述 | clob | ✓ | 0.7% |  |
| 8 | `ForecastObject` | 预计对象 | number(10) | ✓ | 100.0% | 预计对象(ForecastObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1505，得到... |
| 9 | `EValueFloor` | 预计对象值起始(元) | number(19,4) | ✓ | 2.41% | 预计对象值起始(元)(EValueFloor)：为预计对象ForecastObject)  IN (50,53,60)时... |
| 10 | `EValueCeiling` | 预计对象值截止(元) | number(19,4) | ✓ | 2.42% | 预计对象值截止(元)(EValueCeiling)：为预计对象ForecastObject)  IN (50,53,60... |
| 11 | `EGrowthRateFloor` | 预计幅度起始(披露)(%) | number(23,8) | ✓ | 54.57% | 预计幅度起始(披露)(%)：为公告原始披露数据。 |
| 12 | `EGrowRateFloorC` | 预计幅度起始(计算)(%) | number(23,8) | ✓ | 77.05% | 预计幅度起始（计算）（%）（EGrowRateFloorC）：依据披露预计值做计算，计算公式：预计幅度起始（计算）（%）... |
| 13 | `EGrowthRateCeiling` | 预计幅度截止(披露)(%) | number(23,8) | ✓ | 53.1% | 预计幅度截止(披露)(%)：为公告原始披露数据。 |
| 14 | `EGrowthRateCeilC` | 预计幅度截止(计算)(%) | number(23,8) | ✓ | 76.82% | 预计幅度截止（计算）（%）（EGrowthRateCeilC）：依据披露预计值做计算，计算公式：预计幅度截止（计算）（%... |
| 15 | `EEarningFloor` | 预计收入起始(元) | number(19,4) | ✓ | 8.46% | 预计收入起始(元)(EEarningFloor)：展示收入类指标指标，即预计对象ForecastObject) IN (... |
| 16 | `EEarningCeiling` | 预计收入截止(元) | number(19,4) | ✓ | 8.26% | 预计收入截止(元)(EEarningCeiling)：展示收入类指标指标，即预计对象ForecastObject) IN... |
| 17 | `LastEarning` | 上年同期收入(元) | number(19,4) | ✓ | 6.21% | 上年同期收入(元)(LastEarning)：展示收入类指标指标，即预计对象ForecastObject) IN (20... |
| 18 | `EProfitFloor` | 预计净利润起始(元) | number(19,4) | ✓ | 58.3% | 预计净利润起始(元)(EProfitFloor)：展示利润类指标指标，即预计对象ForecastObject) IN (... |
| 19 | `EProfitCeiling` | 预计净利润截止(元) | number(19,4) | ✓ | 58.21% | 预计净利润截止(元)(EProfitCeiling)：展示利润类指标指标，即预计对象ForecastObject) IN... |
| 20 | `LastProfit` | 上年同期净利润(元) | number(19,4) | ✓ | 65.68% | 上年同期净利润(元)(LastProfit)：展示利润类指标指标，即预计对象ForecastObject) IN (10... |
| 21 | `EEPSFloor` | 预计每股收益起始(元) | number(23,8) | ✓ | 13.64% | 预计每股收益起始(元)(EEPSFloor)：展示每股收益类指标指标，即预计对象ForecastObject) IN (... |
| 22 | `EEPSCeiling` | 预计每股收益截止(元) | number(23,8) | ✓ | 13.63% | 预计每股收益截止(元)(EEPSCeiling)：展示每股收益类指标指标，即预计对象ForecastObject) IN... |
| 23 | `LastEPS` | 上年同期基本每股收益(元) | number(23,8) | ✓ | 13.58% | 上年同期基本每股收益(元)(LastEPS)：展示每股收益类指标指标，即预计对象ForecastObject) IN (... |
| 24 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 25 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |
| 27 | `AnnouncementTag` | 公告标签 | number(10) | ✓ | 42.83% | 本字段为废弃字段，公告标签（AnnouncementTag）：1-15:30前公告，2-15:30后公告。 |
| 28 | `ForcastReason` | 业绩预计原因 | number(10) | ✓ |  |  |
| 29 | `NPYOYConsistentForecast` | 一致预期净利润增幅(%) | number(18,4) | ✓ | 32.64% | 本字段为废弃字段，一致预期净利润增幅（NPYOYConsistentForecast））＝(预测净利润平均值(t年)/最... |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ForcastType (业绩预计类型)

业绩预计类型(ForcastType)：1-预亏，2-不确定，3-预盈，4-预增，5-预平，6-经营计划，7-减亏，8-预降，9-减增，18-减降。可与系统常量表的DM字段关联，令LB=1158 AND DM IN(1,2,3,4,5,6,7,8,9,18)，其中“2-预警”对应“2-不确定”。

### ForecastObject (预计对象)

预计对象(ForecastObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1505，得到预计对象的具体描述：10-累计利润，13-季度利润，20-累计收入，23-季度收入，30-累计每股收益，33-季度每股收益，40-累计扣除非经常性损益后归属母公司净利润，43-季度扣除非经常性损益后归属母公司净利润，50-累计非经常性损益，53-季度非经常性损益，60-归母股东权益，70-累计扣除后营业收入，73-季度扣除后营业收入。

### EValueFloor (预计对象值起始(元))

预计对象值起始(元)(EValueFloor)：为预计对象ForecastObject)  IN (50,53,60)时，预计指标的公告原始披露起始值。

### EValueCeiling (预计对象值截止(元))

预计对象值截止(元)(EValueCeiling)：为预计对象ForecastObject)  IN (50,53,60)时，预计指标的公告原始披露截止值。

### EGrowthRateFloor (预计幅度起始(披露)(%))

预计幅度起始(披露)(%)：为公告原始披露数据。

### EGrowRateFloorC (预计幅度起始(计算)(%))

预计幅度起始（计算）（%）（EGrowRateFloorC）：依据披露预计值做计算，计算公式：预计幅度起始（计算）（%）=（预计起始-上年同期值）/|上年同期值|*100

### EGrowthRateCeiling (预计幅度截止(披露)(%))

预计幅度截止(披露)(%)：为公告原始披露数据。

### EGrowthRateCeilC (预计幅度截止(计算)(%))

预计幅度截止（计算）（%）（EGrowthRateCeilC）：依据披露预计值做计算，计算公式：预计幅度截止（计算）（%）=（预计截止-上年同期值）/|上年同期值|*100。

### EEarningFloor (预计收入起始(元))

预计收入起始(元)(EEarningFloor)：展示收入类指标指标，即预计对象ForecastObject) IN (20,23,70,73)的预计起始值。

## SQL示例

```sql
-- 查询 业绩预告 数据
SELECT *
FROM lc_performanceforecast
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
