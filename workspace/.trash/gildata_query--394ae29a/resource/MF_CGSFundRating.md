# MF_CGSFundRating

**中文名**: 公募基金评级_银河证券

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CGSFundRating` |
| MySQL表名 | `mf_cgsfundrating` |
| 中文名 | 公募基金评级_银河证券 |
| 路径 | 聚源新版数据库 > 产品代理 > 基金评级代理数据库 |
| 更新频率 | 周更新 |
| 字段数量 | 46 |
| 版本 | 1.04 |

## 表描述

1.本表记录银河证券按周提供的基金评级信息，包括各区间段的收益率数据及星级评价数据。
2.历史数据：1998年3月起-至今。
3.数据来源：聚源按照源原始披露整理。
4.授权提示：此表需要额外拿到银河证券的授权才能使用。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PubOrgCode` | 评级机构代码 | number(10) | ✓ | 100.0% |  |
| 3 | `PubOrgName` | 评级机构名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `ReportPeriod` | 报告周期 | number(10) | ✗ | 100.0% | 报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告... |
| 7 | `RunningTime` | 成立以来运作时间(年) | number(9,4) | ✓ | 86.36% |  |
| 8 | `ReturAccuUnitNV` | 还原后份额累计净值(元) | number(19,6) | ✓ | 5.62% |  |
| 9 | `CGSFundType` | 银河证券基金分类 | number(10) | ✓ | 100.0% | 银河证券基金分类（CGSFundType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联， ... |
| 10 | `NVGrowthRateR1W` | 一周净值增长率(%) | number(9,4) | ✓ | 23.38% |  |
| 11 | `NVGrowthRateR1M` | 一个月(4周)净值增长率(%) | number(9,4) | ✓ | 22.88% |  |
| 12 | `NVGrowthRateR3M` | 三个月(13周)净值增长率(%) | number(9,4) | ✓ | 21.76% |  |
| 13 | `NVGrowthRateR6M` | 六个月(26周)净值增长率(%) | number(9,4) | ✓ | 20.2% |  |
| 14 | `NVGrowthRateYTD` | 今年以来净值增长率(%) | number(9,4) | ✓ | 23.36% |  |
| 15 | `NVGrowthRateR1Y` | 一年(52周)净值增长率(%) | number(9,4) | ✓ | 81.96% |  |
| 16 | `RankR1Y` | 一年(52周)同类型排名 | varchar2(200) | ✓ | 59.09% |  |
| 17 | `NVGrowthRateR2Y` | 两年(104周)净值增长率(%) | number(9,4) | ✓ | 53.47% |  |
| 18 | `RankR2Y` | 两年(104周)同类型排名 | varchar2(200) | ✓ | 36.91% |  |
| 19 | `NVGrowthRateR3Y` | 近三年净值增长率(%) | number(9,4) | ✓ | 48.59% |  |
| 20 | `RankR3Y` | 近三年同类型排名 | varchar2(200) | ✓ | 35.31% |  |
| 21 | `StarRankR3Y` | 近三年星级评价 | number(10) | ✓ | 81.55% | 近三年星级评价(StarRankR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 22 | `NVGrowthRateR4Y` | 近四年净值增长率(%) | number(9,4) | ✓ | 30.51% |  |
| 23 | `RankR4Y` | 近四年同类型排名 | varchar2(200) | ✓ | 21.21% |  |
| 24 | `StarRankR4Y` | 近四年星级评价 | number(10) | ✓ | 81.22% | 近四年星级评价(StarRankR4Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 25 | `NVGrowthRateR5Y` | 近五年净值增长率(%) | number(9,4) | ✓ | 27.51% |  |
| 26 | `RankR5Y` | 近五年同类型排名 | varchar2(200) | ✓ | 19.84% |  |
| 27 | `StarRankR5Y` | 近五年星级评价 | number(10) | ✓ | 81.01% | 近五年星级评价(StarRankR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 28 | `NVGrowthRateR6Y` | 近六年净值增长率(%) | number(9,4) | ✓ | 17.18% |  |
| 29 | `RankR6Y` | 近六年同类型排名 | varchar2(200) | ✓ | 11.95% |  |
| 30 | `StarRankR6Y` | 近六年星级评价 | number(10) | ✓ | 10.23% | 近六年星级评价(StarRankR6Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 31 | `NVGrowthRateR7Y` | 近七年净值增长率(%) | number(9,4) | ✓ | 15.61% |  |
| 32 | `RankR7Y` | 近七年同类型排名 | varchar2(200) | ✓ | 11.24% |  |
| 33 | `StarRankR7Y` | 近七年星级评价 | number(10) | ✓ | 7.67% | 近七年星级评价(StarRankR7Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 34 | `NVGrowthRateR8Y` | 近八年(416周)净值增长率(%) | number(9,4) | ✓ | 7.75% |  |
| 35 | `RankR8Y` | 近八年(416周)同类型排名 | varchar2(200) | ✓ | 6.65% |  |
| 36 | `StarRankR8Y` | 近八年星级评价 | number(10) | ✓ | 63.43% | 近八年星级评价(StarRankR8Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 37 | `NVGrowthRateR9Y` | 近九年(468周)净值增长率(%) | number(9,4) | ✓ | 5.7% |  |
| 38 | `RankR9Y` | 近九年(468周)同类型排名 | varchar2(200) | ✓ | 4.84% |  |
| 39 | `StarRankR9Y` | 近九年星级评价 | number(10) | ✓ | 63.43% | 近九年星级评价(StarRankR9Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到... |
| 40 | `NVGrowthRateR10Y` | 近十年(520周)净值增长率(%) | number(9,4) | ✓ | 5.39% |  |
| 41 | `RankR10Y` | 近十年(520周)同类型排名 | varchar2(200) | ✓ | 4.55% |  |
| 42 | `StarRankR10Y` | 近十年星级评价 | number(10) | ✓ | 63.42% | 近十年星级评价(StarRankR10Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得... |
| 43 | `AccuNVGrowthRate` | 成立以来累计净值增长率(%) | number(9,4) | ✓ | 86.68% |  |
| 44 | `AverNVGrowthRate` | 成立以来年化平均净值增长率(%) | number(9,4) | ✓ | 74.51% |  |
| 45 | `UpdateTime` | 修改日期 | date | ✗ |  |  |
| 46 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportPeriod (报告周期)

报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告周期的具体描述：1-日，7-周，14-两周，30-月，90-季，180-半年，365-年。

### CGSFundType (银河证券基金分类)

银河证券基金分类（CGSFundType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，
    截止日期（EndDate）为2017-06-16以前的，令“LB=1641”，得到银河证券基金分类的具体描述；
    截止日期（EndDate）为2017-06-16（含）以后的，令“LB=2017”，得到银河证券基金分类的具体描述。

### StarRankR3Y (近三年星级评价)

近三年星级评价(StarRankR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近三年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR4Y (近四年星级评价)

近四年星级评价(StarRankR4Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近四年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR5Y (近五年星级评价)

近五年星级评价(StarRankR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近五年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR6Y (近六年星级评价)

近六年星级评价(StarRankR6Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近六年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR7Y (近七年星级评价)

近七年星级评价(StarRankR7Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近七年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR8Y (近八年星级评价)

近八年星级评价(StarRankR8Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近八年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StarRankR9Y (近九年星级评价)

近九年星级评价(StarRankR9Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到近九年星级评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

## SQL示例

```sql
-- 查询 公募基金评级_银河证券 数据
SELECT *
FROM mf_cgsfundrating
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
