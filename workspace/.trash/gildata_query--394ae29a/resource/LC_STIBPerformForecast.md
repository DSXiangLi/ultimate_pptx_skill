# LC_STIBPerformForecast

**中文名**: 科创板业绩预告

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBPerformForecast` |
| MySQL表名 | `lc_stibperformforecast` |
| 中文名 | 科创板业绩预告 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 财务指标 |
| 更新频率 | 不定期更新 |
| 字段数量 | 20 |
| 版本 | 1.05 |

## 表描述

1.内容说明：收录科创板公司对未来报告期本公司业绩的预计情况，包括业绩预计类型、预计内容、具体预计值等。
2.数据范围：科创板上市至今
3.信息来源：科创板公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 业绩预计报告期 | date | ✗ | 100.0% |  |
| 5 | `ForcastType` | 业绩预计类型 | number(10) | ✓ | 100.0% | 业绩预计类型(ForcastType)：1-预亏，2-不确定，3-预盈，4-预增，5-预平，6-经营计划，7-减亏，8-... |
| 6 | `ResultStatement` | 业绩预计结果说明 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `ForcastReason` | 业绩变动原因类型 | number(10) | ✓ |  |  |
| 8 | `ForcastContent` | 业绩预计内容描述 | clob | ✓ | 5.06% |  |
| 9 | `ForecastObject` | 预计对象 | number(10) | ✗ | 100.0% | 预计对象(ForecastObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1505，得到... |
| 10 | `EValueFloor` | 预计对象值起始(元) | number(23,8) | ✓ | 96.5% |  |
| 11 | `EValueCeiling` | 预计对象值截止(元) | number(23,8) | ✓ | 96.47% |  |
| 12 | `LastSum` | 上年同期金额(元) | number(23,8) | ✓ | 77.91% |  |
| 13 | `EGrowthRateFloor` | 预计幅度起始(披露)(%) | number(23,8) | ✓ | 83.46% |  |
| 14 | `EGrowRateFloorC` | 预计幅度起始(计算)(%) | number(23,8) | ✓ | 77.3% | 预计幅度起始（计算）（%）（EGrowRateFloorC）：依据披露预计值做计算，计算公式=预计幅度起始（计算）（%）... |
| 15 | `EGrowthRateCeiling` | 预计幅度截止(披露)(%) | number(23,8) | ✓ | 83.3% |  |
| 16 | `EGrowthRateCeilC` | 预计幅度截止(计算)(%) | number(23,8) | ✓ | 77.29% | 预计幅度截止（计算）（%）（EGrowthRateCeilC）：依据披露预计值做计算，计算公式：预计幅度截止（计算）（%... |
| 17 | `AID` | 公告ID | number(19) | ✓ | 0.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ForcastType (业绩预计类型)

业绩预计类型(ForcastType)：1-预亏，2-不确定，3-预盈，4-预增，5-预平，6-经营计划，7-减亏，8-预降，9-减增，18-减降。可与系统常量表的DM字段关联，令LB=1158 AND DM IN(1,2,3,4,5,6,7,8,9,18)，其中“2-预警”对应“2-不确定”。

### ForecastObject (预计对象)

预计对象(ForecastObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1505，得到预计对象的具体描述：10-累计利润，13-季度利润，20-累计收入，23-季度收入，30-累计每股收益，33-季度每股收益，40-累计扣除非经常性损益后归属母公司净利润，43-季度扣除非经常性损益后归属母公司净利润，50-累计非经常性损益，53-季度非经常性损益，60-归母股东权益，70-累计扣除后营业收入，73-季度扣除后营业收入。

### EGrowRateFloorC (预计幅度起始(计算)(%))

预计幅度起始（计算）（%）（EGrowRateFloorC）：依据披露预计值做计算，计算公式=预计幅度起始（计算）（%）=（预计起始值-上年同期值）/|上年同期值|*100

### EGrowthRateCeilC (预计幅度截止(计算)(%))

预计幅度截止（计算）（%）（EGrowthRateCeilC）：依据披露预计值做计算，计算公式：预计幅度截止（计算）（%）=（预计截止值-上年同期值）/|上年同期值|*100

## SQL示例

```sql
-- 查询 科创板业绩预告 数据
SELECT *
FROM lc_stibperformforecast
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
