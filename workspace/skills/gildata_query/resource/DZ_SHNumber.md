# DZ_SHNumber

**中文名**: 股东户数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_SHNumber` |
| MySQL表名 | `dz_shnumber` |
| 中文名 | 股东户数 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股东股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 65 |
| 版本 | 1.04 |

## 表描述

1.内容说明：反映公司全体股东、A股股东、B股东、H股东、CDR股东的持股情况及其历史变动情况等。
2.指标计算公式：
1)户均持股比例＝((股本/股东总户数)/股本)*100%（公式中分子分母描述同一股票类型）
2)相对上一期报告期户均持股比例变化＝本报告期户均持股比例－上一报告期户均持股比例
3)户均持股数季度增长率＝(本季度户均持股数量/上一季度户均持股数量－1)*100%
4)户均持股比例季度增长率=(本季度户均持股比例/上一季度户均持股比例-1)*100%
5)户均持股数半年增长率=(本报告期户均持股数量/前推两季度户均持股数量-1)*100%
6)户均持股比例半年增长率 = (本报告期户均持股比例/ 前推两个季度户均持股比例-1)*100%
2.数据范围：1991-1-1至今
3.信息来源：招股说明书、上市公告书、定报、临时公告、深交所互动易、上证e互动等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布时间 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `NumApproxiMark` | 户数约数标识 | number(10) | ✓ | 1.35% | 户数约数标识(NumApproxiMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 A... |
| 7 | `SHNum` | 股东总户数(户) | number(10) | ✓ | 99.57% |  |
| 8 | `AverageHoldSum` | 户均持股数(股/户) | number(18,2) | ✓ | 99.53% | 户均持股数（AverageHoldSum）＝总股本/股东总户数 |
| 9 | `HoldProportionPAccount` | 户均持股比例(%) | number(18,12) | ✓ | 99.57% |  |
| 10 | `ProportionChange` | 相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 97.93% |  |
| 11 | `AvgHoldSumGRQuarter` | 户均持股数季度增长率(%) | number(18,4) | ✓ | 71.74% |  |
| 12 | `ProportionGRQuarter` | 户均持股比例季度增长率(%) | number(18,12) | ✓ | 71.74% |  |
| 13 | `AvgHoldSumGRHalfAYear` | 户均持股数半年增长率(%) | number(18,4) | ✓ | 71.52% |  |
| 14 | `ProportionGRHalfAYear` | 户均持股比例半年增长率(%) | number(18,12) | ✓ | 71.52% |  |
| 15 | `ASHNum` | A股股东户数(户) | number(10) | ✓ | 97.36% |  |
| 16 | `AAverageHoldSum` | A股股东户均持股数(股/户) | number(18,2) | ✓ | 92.25% | A股股东户均持股数（AAverageHoldSum）＝A股股本/A股股东户数 |
| 17 | `AHoldProportionPAccount` | A股户均持股比例(%) | number(18,12) | ✓ | 97.36% |  |
| 18 | `AProportionChange` | A股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 95.5% |  |
| 19 | `AAvgHoldSumGRQuarter` | A股户均持股数季度增长率(%) | number(18,4) | ✓ | 68.99% |  |
| 20 | `AProportionGRQuarter` | A股户均持股比例季度增长率(%) | number(18,12) | ✓ | 69.6% |  |
| 21 | `AAvgHoldSumGRHalfAYear` | A股户均持股数半年增长率(%) | number(18,4) | ✓ | 67.12% |  |
| 22 | `AProportionGRHalfAYear` | A股户均持股比例半年增长率(%) | number(18,12) | ✓ | 69.47% |  |
| 23 | `StaffSHNum` | 职工股户数(户) | number(10) | ✓ | 0.23% |  |
| 24 | `AFAverageHoldSum` | 无限售A股股东户均持股数(股/户) | number(10) | ✓ | 92.16% | 无限售A股股东户均持股数（AFAverageHoldSum）＝无限售A股/A股股东户数 |
| 25 | `AFHoldProportionPAccount` | 无限售A股户均持股比例(%) | number(18,12) | ✓ | 97.36% |  |
| 26 | `AFProportionChange` | 无限售A股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 95.5% |  |
| 27 | `AFAvgHoldSumGRQuarter` | 无限售A股户均持股数季度增长率(%) | number(18,4) | ✓ | 68.9% |  |
| 28 | `AFProportionGRQuarter` | 无限售A股户均持股比例季度增长率(%) | number(18,12) | ✓ | 69.6% |  |
| 29 | `AFAvgHoldSumGRHalfAYear` | 无限售A股户均持股数半年增长率(%) | number(18,4) | ✓ | 67.03% |  |
| 30 | `AFProportionGRHalfAYear` | 无限售A股户均持股比例半年增长率(%) | number(18,12) | ✓ | 69.47% |  |
| 31 | `BSHNum` | B股股东户数(户) | number(10) | ✓ | 1.29% |  |
| 32 | `BAverageHoldSum` | B股股东户均持股数(股/户) | number(18,2) | ✓ | 1.29% | B股股东户均持股数（BAverageHoldSum）＝B股股本/B股股东户数 |
| 33 | `BHoldProportionPAccount` | B股户均持股比例(%) | number(18,12) | ✓ | 1.29% |  |
| 34 | `BProportionChange` | B股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 1.09% |  |
| 35 | `BAvgHoldSumGRQuarter` | B股户均持股数季度增长率(%) | number(18,4) | ✓ | 0.89% |  |
| 36 | `BProportionGRQuarter` | B股户均持股比例季度增长率(%) | number(18,12) | ✓ | 0.89% |  |
| 37 | `BAvgHoldSumGRHalfAYear` | B股户均持股数半年增长率(%) | number(18,4) | ✓ | 0.97% |  |
| 38 | `BProportionGRHalfAYear` | B股户均持股比例半年增长率(%) | number(18,12) | ✓ | 0.97% |  |
| 39 | `HSHNum` | H股股东户数(户) | number(10) | ✓ | 1.11% |  |
| 40 | `HAverageHoldSum` | H股股东户均持股数(股/户) | number(18,2) | ✓ | 1.11% | H股股东户均持股数（HAverageHoldSum）＝H股股本/H股股东户数 |
| 41 | `HHoldProportionPAccount` | H股户均持股比例(%) | number(18,12) | ✓ | 1.11% |  |
| 42 | `HProportionChange` | H股相对上一期报告期户均持股比例变化(%) | number(18,12) | ✓ | 0.94% |  |
| 43 | `HAvgHoldSumGRQuarter` | H股户均持股数季度增长率(%) | number(18,4) | ✓ | 0.79% |  |
| 44 | `HProportionGRQuarter` | H股户均持股比例季度增长率(%) | number(18,12) | ✓ | 0.79% |  |
| 45 | `HAvgHoldSumGRHalfAYear` | H股户均持股数半年增长率(%) | number(18,4) | ✓ | 0.84% |  |
| 46 | `HProportionGRHalfAYear` | H股户均持股比例半年增长率(%) | number(18,12) | ✓ | 0.84% |  |
| 47 | `CDRSHNum` | CDR股东户数(户) | number(10) | ✓ | 0.01% |  |
| 48 | `CDRAverageHoldSum` | CDR股东户均持股数(份/户) | number(18,2) | ✓ | 0.01% | CDR股东户均持股数（份/户）（CDRAverageHoldSum）=CDR份数/CDR股东总户数 |
| 49 | `CDRHoldPropPAccount` | CDR户均持股比例(%) | number(19,8) | ✓ | 0.01% |  |
| 50 | `CDRProportionChange` | CDR相对上一期报告期户均持股比例变化(%) | number(19,8) | ✓ | 0.01% |  |
| 51 | `CDRAvgHoldSumGRQtr` | CDR户均持股数季度增长率(%) | number(18,4) | ✓ | 0.0% |  |
| 52 | `CDRPropGRQuarter` | CDR户均持股比例季度增长率(%) | number(19,8) | ✓ | 0.0% |  |
| 53 | `CDRAvgHoldSumGRHalfAY` | CDR户均持股数半年增长率(%) | number(18,4) | ✓ | 0.0% |  |
| 54 | `CDRPropGRHalfAYear` | CDR股户均持股比例半年增长率(%) | number(19,8) | ✓ | 0.0% |  |
| 55 | `CDRFAverageHoldSum` | 无限售CDR股东户均持股数(份/户) | number(10) | ✓ | 0.0% |  |
| 56 | `CDRFHoldPropPAccount` | 无限售CDR户均持股比例(%) | number(19,8) | ✓ | 0.01% | 无限售CDR股东户均持股数（份/户）（CDRFAverageHoldSum)=无限售CDR份数/CDR股东总户数 |
| 57 | `CDRFProportionChange` | 无限售CDR相对上一期报告期户均持股比例变化(%) | number(19,8) | ✓ | 0.01% |  |
| 58 | `CDRFAvgHoldSumGRQtr` | 无限售CDR户均持股数季度增长率(%) | number(18,4) | ✓ | 0.0% |  |
| 59 | `CDRFPropGRQuarter` | 无限售CDR户均持股比例季度增长率(%) | number(19,8) | ✓ | 0.0% |  |
| 60 | `CDRFAvgHoldSumGRHalfAY` | 无限售CDR户均持股数半年增长率(%) | number(18,4) | ✓ | 0.0% |  |
| 61 | `CDRFPropGRHalfAYear` | 无限售CDR户均持股比例半年增长率(%) | number(19,8) | ✓ | 0.0% |  |
| 62 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 63 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 64 | `JSID` | JSID | number(19) | ✗ |  |  |
| 65 | `AFHoldPropTA` | 无限售A股/股东总户数(股/户) | number(10) | ✓ | 69.63% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### NumApproxiMark (户数约数标识)

户数约数标识(NumApproxiMark)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1)，得到户数约数标识的具体描述：1-是。

### AverageHoldSum (户均持股数(股/户))

户均持股数（AverageHoldSum）＝总股本/股东总户数

### AAverageHoldSum (A股股东户均持股数(股/户))

A股股东户均持股数（AAverageHoldSum）＝A股股本/A股股东户数

### AFAverageHoldSum (无限售A股股东户均持股数(股/户))

无限售A股股东户均持股数（AFAverageHoldSum）＝无限售A股/A股股东户数

### BAverageHoldSum (B股股东户均持股数(股/户))

B股股东户均持股数（BAverageHoldSum）＝B股股本/B股股东户数

### HAverageHoldSum (H股股东户均持股数(股/户))

H股股东户均持股数（HAverageHoldSum）＝H股股本/H股股东户数

### CDRAverageHoldSum (CDR股东户均持股数(份/户))

CDR股东户均持股数（份/户）（CDRAverageHoldSum）=CDR份数/CDR股东总户数

### CDRFHoldPropPAccount (无限售CDR户均持股比例(%))

无限售CDR股东户均持股数（份/户）（CDRFAverageHoldSum)=无限售CDR份数/CDR股东总户数

## SQL示例

```sql
-- 查询 股东户数 数据
SELECT *
FROM dz_shnumber
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
