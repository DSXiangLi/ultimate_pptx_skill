# MF_SHSECFundRating

**中文名**: 公募基金评级_上海证券

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_SHSECFundRating` |
| MySQL表名 | `mf_shsecfundrating` |
| 中文名 | 公募基金评级_上海证券 |
| 路径 | 聚源新版数据库 > 产品代理 > 基金评级代理数据库 |
| 更新频率 | 月更新 |
| 字段数量 | 33 |
| 版本 | 1.01 |

## 表描述

1.本表上海证券按月、季度提供的基金评级信息，包括选股能力、择时能力、夏普比率等评价指标。
2.历史数据：2010年5月起-至今。
3.数据来源：聚源按照源原始披露整理。
4.授权提示：此表需要额外拿到上海证券的授权才能使用。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PubOrgCode` | 评级机构代码 | number(10) | ✗ | 100.0% |  |
| 3 | `PubOrgName` | 评级机构名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `InnerCode` | 基金内部编码 | number(10) | ✓ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `ReportPeriod` | 报告周期 | number(10) | ✗ | 100.0% | 报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告... |
| 8 | `FundTypeCode` | 上海证券基金分类代码 | number(10) | ✓ | 100.0% | 上海证券基金分类代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 173... |
| 9 | `FundTypeName` | 上海证券基金分类名称 | varchar2(100) | ✓ | 100.0% |  |
| 10 | `UnitNV` | 单位净值(元) | number(9,6) | ✓ | 73.13% |  |
| 11 | `RRInSingleMonth` | 近一月净值增长率(%) | number(18,6) | ✓ | 11.55% |  |
| 12 | `RRInSingleMonthToBM` | 近一月相对基准增长率(%) | number(18,6) | ✓ | 10.16% |  |
| 13 | `RRInThisMonth` | 本月以来净值增长率(%) | number(18,6) | ✓ | 51.46% |  |
| 14 | `RRInThisMonthToBM` | 本月以来相对基准增长率(%) | number(18,6) | ✓ | 48.56% |  |
| 15 | `RRInSingleQuarter` | 近一季度净值增长率(%) | number(18,6) | ✓ | 16.98% |  |
| 16 | `RRInSingleQuarterToBM` | 近一季度相对基准增长率(%) | number(18,6) | ✓ | 14.93% |  |
| 17 | `RRInThisQuarter` | 本季度以来净值增长率(%) | number(18,6) | ✓ | 76.78% |  |
| 18 | `RRInThisQuarterToBM` | 本季度以来相对基准增长率(%) | number(18,6) | ✓ | 72.27% |  |
| 19 | `RRInSingleYear` | 近一年净值增长率(%) | number(18,6) | ✓ | 15.9% |  |
| 20 | `RRInSingleYearToBM` | 近一年相对基准增长率(%) | number(18,6) | ✓ | 14.03% |  |
| 21 | `RRSinceThisYear` | 本年以来净值增长率(%) | number(18,6) | ✓ | 76.19% |  |
| 22 | `RRSinceThisYearToBM` | 本年以来相对基准增长率(%) | number(18,6) | ✓ | 72.04% |  |
| 23 | `DiscountRate` | 折价率(%) | number(18,6) | ✓ | 0.12% | 折价率（DiscountRate）：该字段只对封闭式基金有效 |
| 24 | `CompEvaluationR3Y` | 综合评级(3年) | number(10) | ✓ | 39.59% | 综合评级(3年)(CompEvaluationR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 25 | `StockSelectionAbilityR3Y` | 选证能力评级(3年) | number(10) | ✓ | 59.26% | 选证能力评级(3年)(StockSelectionAbilityR3Y)与(CT_SystemConst)表中的DM字段... |
| 26 | `TimingAbilityR3Y` | 择时能力评级(3年) | number(10) | ✓ | 59.23% | 择时能力评级(3年)(TimingAbilityR3Y)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 27 | `SharpRatioR3Y` | 夏普比率评级(3年) | number(10) | ✓ | 59.26% | 夏普比率评级(3年)(SharpRatioR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 28 | `CompEvaluationR5Y` | 综合评级(5年) | number(10) | ✓ | 38.53% | 综合评级(5年)(CompEvaluationR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 29 | `StockSelectionAbilityR5Y` | 选证能力评级(5年) | number(10) | ✓ | 51.09% | 选证能力评级(5年)(StockSelectionAbilityR5Y)与(CT_SystemConst)表中的DM字段... |
| 30 | `TimingAbilityR5Y` | 择时能力评级(5年) | number(10) | ✓ | 51.05% | 择时能力评级(5年)(TimingAbilityR5Y)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 31 | `SharpRatioR5Y` | 夏普比率评级(5年) | number(10) | ✓ | 51.09% | 夏普比率评级(5年)(SharpRatioR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 32 | `UpdateTime` | 修改日期 | date | ✗ |  |  |
| 33 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportPeriod (报告周期)

报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告周期的具体描述：1-日，7-周，14-两周，30-月，90-季，180-半年，365-年。

### FundTypeCode (上海证券基金分类代码)

上海证券基金分类代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1730，得到上海证券基金分类代码的具体描述：10000000-股票型，10010000-主动投资股票基金，10010001-普通股票基金，10010002-港股通股票基金，10020000-指数投资股票基金，10020001-标准指数股票基金，10020002-增强指数股票基金，11000000-混合型，11010000-主动投资混合基金，11010001-偏股混合基金，11010002-灵活配置混合基金，11010003-偏债混合基金，11010004-港股通混合基金，12000000-债券型，12010000-主动投资债券基金，12010001-长期纯债基金，12010002-中短期纯债基金，12010003-短期纯债基金，12010004-普通债券基金，12010005-可转债基金，12020000-指数投资债券基金，12020001-标准指数债券基金，12020002-增强指数债券基金，13000000-指数型，14000000-保本型，15000000-货币型，15010000-货币市场基金，15010001-货币市场基金，16000000-QDII，16010000-QDII股票基金，16010001-QDII主动投资股票基金，16010002-QDII指数投资股票基金，16020000-QDII混合基金，16020001-QDII混合基金，16030000-QDII债券基金，16030001-QDII主动投资债券基金，16030002-QDII指数投资债券基金，16040000-其他QDII基金，16040001-其他QDII基金，17000000-FOF，17010000-普通FOF，17010001-股票FOF，17010002-偏股混合FOF，17010003-灵活配置混合FOF，17010004-偏债混合FOF，17010005-债券FOF，17020000-养老目标日期FOF，17020001-养老目标日期FOF2025，17020002-养老目标日期FOF2030，17020003-养老目标日期FOF2035，17020004-养老目标日期FOF2040，17020005-养老目标日期FOF2045，17020006-养老目标日期FOF2050，17020007-养老目标日期FOF2055，17020008-养老目标日期FOF2060，17030000-养老目标风险FOF，17030001-积极养老目标风险FOF，17030002-平衡养老目标风险FOF，17030003-稳健养老目标风险FOF，20000000-封闭式，20010000-封闭式股票基金，20010001-封闭式股票基金，20020000-封闭式混合基金，20020001-封闭式混合基金，20030000-封闭式债券基金，20030001-封闭式债券基金，30000000-其他创新，30010000-商品基金，30010001-商品基金，30020000-REITs，30020001-REITs，30030000-同业存单基金，30030001-同业存单基金，30040000-其他基金，30040001-其他基金。

### DiscountRate (折价率(%))

折价率（DiscountRate）：该字段只对封闭式基金有效

### CompEvaluationR3Y (综合评级(3年))

综合评级(3年)(CompEvaluationR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到综合评级(3年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StockSelectionAbilityR3Y (选证能力评级(3年))

选证能力评级(3年)(StockSelectionAbilityR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到选证能力评级(3年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### TimingAbilityR3Y (择时能力评级(3年))

择时能力评级(3年)(TimingAbilityR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到择时能力评级(3年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### SharpRatioR3Y (夏普比率评级(3年))

夏普比率评级(3年)(SharpRatioR3Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到夏普比率评级(3年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### CompEvaluationR5Y (综合评级(5年))

综合评级(5年)(CompEvaluationR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到综合评级(5年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StockSelectionAbilityR5Y (选证能力评级(5年))

选证能力评级(5年)(StockSelectionAbilityR5Y)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到选证能力评级(5年)的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

## SQL示例

```sql
-- 查询 公募基金评级_上海证券 数据
SELECT *
FROM mf_shsecfundrating
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
