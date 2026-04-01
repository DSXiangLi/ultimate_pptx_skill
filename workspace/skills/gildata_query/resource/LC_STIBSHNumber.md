# LC_STIBSHNumber

**中文名**: 科创板股东户数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSHNumber` |
| MySQL表名 | `lc_stibshnumber` |
| 中文名 | 科创板股东户数 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 57 |
| 版本 | 1.04 |

## 表描述

1.内容说明：本表记录科创板上市公司全体股东、A股股东、H股东的持股情况及其历史变动情况等。
2.指标计算公式：
1)户均持股比例＝((股本/户均持股数量)/股本)*100%（公式中分子分母描述同一股票类型）
2)相对上一期报告期户均持股比例变化＝本报告期户均持股比例－上一报告期户均持股比例
3)户均持股数季度增长率＝(本季度户均持股数量/上一季度户均持股数量－1)*100%
4)户均持股比例季度增长率=(本季度户均持股比例/上一季度户均持股比例-1)*100%
5)户均持股数半年增长率=(本报告期户均持股数量/前推两季度户均持股数量-1)*100%
6)户均持股比例半年增长率 = (本报告期户均持股比例/ 前推两个季度户均持股比例-1)*100%
2.数据范围：科创板上市至今
3.信息来源：招股说明书、上市公告书、定报、临时公告、上证e互动等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `SHNum` | 股东总户数(户) | number(10) | ✓ | 99.28% |  |
| 7 | `NumApproxiMark` | 户数约数标识 | number(10) | ✓ | 0.06% | 户数约数标识(NumApproxiMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 A... |
| 8 | `AverageHoldSum` | 户均持股数(股/户) | number(18,2) | ✓ | 99.21% | 户均持股数（AverageHoldSum）＝总股本/股东总户数。 |
| 9 | `HoldProportionPAccount` | 户均持股比例(%) | number(18,12) | ✓ | 99.28% |  |
| 10 | `ProportionChange` | 相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 93.58% |  |
| 11 | `AvgHoldSumGRQuarter` | 户均持股数季度增长率(%) | number(18,4) | ✓ | 66.19% |  |
| 12 | `ProportionGRQuarter` | 户均持股比例季度增长率(%) | number(18,12) | ✓ | 66.19% |  |
| 13 | `AvgHoldSumGRHalfAYear` | 户均持股数半年增长率(%) | number(18,4) | ✓ | 66.27% |  |
| 14 | `ProportionGRHalfAYear` | 户均持股比例半年增长率(%) | number(18,12) | ✓ | 66.3% |  |
| 15 | `ASHNum` | A股股东户数(户) | number(10) | ✓ | 99.25% |  |
| 16 | `AAverageHoldSum` | A股股东户均持股数(股/户) | number(18,2) | ✓ | 81.94% | A股股东户均持股数（AAverageHoldSum）＝A股股本/A股股东户数。 |
| 17 | `AHoldPropPAccount` | A股户均持股比例(%) | number(18,12) | ✓ | 99.25% |  |
| 18 | `AProportionChange` | A股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 93.56% |  |
| 19 | `AAvgHoldSumGRQuarter` | A股户均持股数季度增长率(%) | number(18,4) | ✓ | 63.92% |  |
| 20 | `AProportionGRQuarter` | A股户均持股比例季度增长率(%) | number(18,12) | ✓ | 65.68% |  |
| 21 | `AAvgHoldSumGRHalfAYear` | A股户均持股数半年增长率(%) | number(18,4) | ✓ | 59.39% |  |
| 22 | `AProportionGRHalfAYear` | A股户均持股比例半年增长率(%) | number(18,12) | ✓ | 66.01% |  |
| 23 | `StaffSHNum` | 职工股户数(户) | number(10) | ✓ | 0.0% |  |
| 24 | `AFAverageHoldSum` | 无限售A股股东户均持股数(股/户) | number(10) | ✓ | 81.6% | 无限售A股股东户均持股数（AFAverageHoldSum）＝无限售A股/A股股东户数。 |
| 25 | `AFHoldPropPAccount` | 无限售A股户均持股比例(%) | number(18,12) | ✓ | 99.25% |  |
| 26 | `AFProportionChange` | 无限售A股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 93.56% |  |
| 27 | `AFAvgHoldSumGRQuarter` | 无限售A股户均持股数季度增长率(%) | number(18,4) | ✓ | 63.59% |  |
| 28 | `AFProportionGRQuarter` | 无限售A股户均持股比例季度增长率(%) | number(18,12) | ✓ | 65.68% |  |
| 29 | `AFAvgHoldSumGRHalfYear` | 无限售A股户均持股数半年增长率(%) | number(18,4) | ✓ | 59.07% |  |
| 30 | `AFPropGRHalfAYear` | 无限售A股户均持股比例半年增长率(%) | number(18,12) | ✓ | 66.01% |  |
| 31 | `HSHNum` | H股股东户数(户) | number(10) | ✓ | 1.2% |  |
| 32 | `HAverageHoldSum` | H股股东户均持股数(股) | number(18,2) | ✓ | 1.2% | H股股东户均持股数（HAverageHoldSum）＝H股股本/H股股东户数。 |
| 33 | `HHoldPropPAccount` | H股户均持股比例(%) | number(18,12) | ✓ | 1.2% |  |
| 34 | `HProportionChange` | H股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 0.93% |  |
| 35 | `HAvgHoldSumGRQuarter` | H股户均持股数季度增长率(%) | number(18,4) | ✓ | 0.77% |  |
| 36 | `HProportionGRQuarter` | H股户均持股比例季度增长率(%) | number(18,12) | ✓ | 0.77% |  |
| 37 | `HAvgHoldSumGRHalfAYear` | H股户均持股数半年增长率(%) | number(18,4) | ✓ | 0.79% |  |
| 38 | `HProportionGRHalfAYear` | H股户均持股比例半年增长率(%) | number(18,12) | ✓ | 0.79% |  |
| 39 | `CDRSHNum` | CDR股东户数(户) | number(10) | ✓ | 0.16% |  |
| 40 | `CDRAverageHoldSum` | CDR股东户均持股数(份/户) | number(18,2) | ✓ | 0.15% | CDR股东户均持股数（份/户）（CDRAverageHoldSum）=CDR份数/CDR股东总户数 |
| 41 | `CDRHoldPropPAccount` | CDR户均持股比例(%) | number(19,8) | ✓ | 0.16% |  |
| 42 | `CDRProportionChange` | CDR相对上一期报告期户均持股比例变化(%) | number(19,8) | ✓ | 0.14% |  |
| 43 | `CDRAvgHoldSumGRQtr` | CDR户均持股数季度增长率(%) | number(18,4) | ✓ | 0.11% |  |
| 44 | `CDRPropGRQuarter` | CDR户均持股比例季度增长率(%) | number(19,8) | ✓ | 0.11% |  |
| 45 | `CDRAvgHoldSumGRHalfAY` | CDR户均持股数半年增长率(%) | number(18,4) | ✓ | 0.1% |  |
| 46 | `CDRPropGRHalfAYear` | CDR股户均持股比例半年增长率(%) | number(19,8) | ✓ | 0.1% |  |
| 47 | `CDRFAverageHoldSum` | 无限售CDR股东户均持股数(份/户) | number(10) | ✓ | 0.14% | 无限售CDR股东户均持股数（份/户）（CDRFAverageHoldSum)=无限售CDR份数/CDR股东总户数 |
| 48 | `CDRFHoldPropPAccount` | 无限售CDR户均持股比例(%) | number(19,8) | ✓ | 0.16% |  |
| 49 | `CDRFProportionChange` | 无限售CDR相对上一期报告期户均持股比例变化(%) | number(19,8) | ✓ | 0.14% |  |
| 50 | `CDRFAvgHoldSumGRQtr` | 无限售CDR户均持股数季度增长率(%) | number(18,4) | ✓ | 0.11% |  |
| 51 | `CDRFPropGRQuarter` | 无限售CDR户均持股比例季度增长率(%) | number(19,8) | ✓ | 0.11% |  |
| 52 | `CDRFAvgHoldSumGRHalfAY` | 无限售CDR户均持股数半年增长率(%) | number(18,4) | ✓ | 0.1% |  |
| 53 | `CDRFPropGRHalfAYear` | 无限售CDR户均持股比例半年增长率(%) | number(19,8) | ✓ | 0.1% |  |
| 54 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 55 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 56 | `JSID` | JSID | number(19) | ✗ |  |  |
| 57 | `AFHoldPropTA` | 无限售A股/股东总户数(股/户) | number(10) | ✓ | 35.69% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，取“上市板块(ListedSector)”=7-科创板，得到上市公司的交易代码、简称等。

### NumApproxiMark (户数约数标识)

户数约数标识(NumApproxiMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1)，得到户数约数标识的具体描述：1-是。

### AverageHoldSum (户均持股数(股/户))

户均持股数（AverageHoldSum）＝总股本/股东总户数。

### AAverageHoldSum (A股股东户均持股数(股/户))

A股股东户均持股数（AAverageHoldSum）＝A股股本/A股股东户数。

### AFAverageHoldSum (无限售A股股东户均持股数(股/户))

无限售A股股东户均持股数（AFAverageHoldSum）＝无限售A股/A股股东户数。

### HAverageHoldSum (H股股东户均持股数(股))

H股股东户均持股数（HAverageHoldSum）＝H股股本/H股股东户数。

### CDRAverageHoldSum (CDR股东户均持股数(份/户))

CDR股东户均持股数（份/户）（CDRAverageHoldSum）=CDR份数/CDR股东总户数

### CDRFAverageHoldSum (无限售CDR股东户均持股数(份/户))

无限售CDR股东户均持股数（份/户）（CDRFAverageHoldSum)=无限售CDR份数/CDR股东总户数

## SQL示例

```sql
-- 查询 科创板股东户数 数据
SELECT *
FROM lc_stibshnumber
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
