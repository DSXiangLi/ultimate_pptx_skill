# MF_JAJXFundRating

**中文名**: 公募基金评级_济安金信

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_JAJXFundRating` |
| MySQL表名 | `mf_jajxfundrating` |
| 中文名 | 公募基金评级_济安金信 |
| 路径 | 聚源新版数据库 > 产品代理 > 基金评级代理数据库 |
| 更新频率 | 季更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.本表记录济安金信按季度提供的基金评级信息，包括抗风险能力、业绩稳定性、择时能力、选股能力等全面的评价指标。
2.历史数据：2009年12月起-至今。
3.数据来源：聚源按照源原始披露整理。
4.授权提示：此表需要额外拿到济安金信的授权才能使用。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PubOrgCode` | 评级机构代码 | number(10) | ✗ | 100.0% |  |
| 3 | `PubOrgName` | 评级机构名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `InnerCode` | 基金内部编码 | number(10) | ✓ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `ReportPeriod` | 报告周期 | number(10) | ✗ | 100.0% | 报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告... |
| 7 | `FundTypeCode` | 济安金信基金分类代码 | number(10) | ✓ | 100.0% | 济安金信基金分类代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 164... |
| 8 | `FundTypeName` | 济安金信基金分类名称 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `ComprehensiveEvaluation` | 综合评价 | number(10) | ✓ | 100.0% | 综合评价(ComprehensiveEvaluation)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 10 | `ProfitAbility` | 盈利能力 | number(10) | ✓ | 89.69% | 盈利能力(ProfitAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到盈... |
| 11 | `PerformanceStability` | 业绩稳定性 | number(10) | ✓ | 69.07% | 业绩稳定性(PerformanceStability)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 12 | `AntiRiskCapability` | 抗风险能力 | number(10) | ✓ | 56.63% | 抗风险能力(AntiRiskCapability)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 13 | `TimingAbility` | 择时能力 | number(10) | ✓ | 39.88% | 择时能力(TimingAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到择... |
| 14 | `StockSelectionAbility` | 选股能力 | number(10) | ✓ | 45.58% | 选股能力(StockSelectionAbility)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 15 | `ReferenceRrackingAbility` | 基准跟踪能力 | number(10) | ✓ | 12.05% | 基准跟踪能力(ReferenceRrackingAbility)与(CT_SystemConst)表中的DM字段关联，令... |
| 16 | `ExcessEarningCapacity` | 超额收益能力 | number(10) | ✓ | 12.05% | 超额收益能力(ExcessEarningCapacity)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 17 | `OverallCost` | 整体费用 | number(10) | ✓ | 60.54% | 整体费用(OverallCost)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到整体费... |
| 18 | `UpdateTime` | 修改日期 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportPeriod (报告周期)

报告周期(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1174，得到报告周期的具体描述：1-日，7-周，14-两周，30-月，90-季，180-半年，365-年。

### FundTypeCode (济安金信基金分类代码)

济安金信基金分类代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1644，得到济安金信基金分类代码的具体描述：10000000-货币型基金，10010000-普通货币型，11000000-纯债型基金，11010000-短期纯债型，11020000-普通纯债型，11030000-中短期纯债型，12000000-一级债基金，12010000-普通一级债，13000000-二级债基金，13010000-普通二级债，14000000-股票型基金，14010000-普通股票型，15000000-混合型基金，15010000-偏债混合型，15020000-偏股混合型，15030000-普通混合型，15040000-绝对目标收益，16000000-封闭型基金，16010000-偏股封闭型，16020000-偏债封闭型，17000000-指数型基金，17010000-标准指数型，17020000-增强指数型，17030000-普通指数型，17040000-其他指数型，18000000-QDII，18010000-被动权益，18020000-主动权益，18030000-固定收益，18040000-其他QDII，99000000-其他。

### ComprehensiveEvaluation (综合评价)

综合评价(ComprehensiveEvaluation)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到综合评价的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### ProfitAbility (盈利能力)

盈利能力(ProfitAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到盈利能力的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### PerformanceStability (业绩稳定性)

业绩稳定性(PerformanceStability)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到业绩稳定性的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### AntiRiskCapability (抗风险能力)

抗风险能力(AntiRiskCapability)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到抗风险能力的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### TimingAbility (择时能力)

择时能力(TimingAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到择时能力的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### StockSelectionAbility (选股能力)

选股能力(StockSelectionAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到选股能力的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

### ReferenceRrackingAbility (基准跟踪能力)

基准跟踪能力(ReferenceRrackingAbility)与(CT_SystemConst)表中的DM字段关联，令LB = 1364，得到基准跟踪能力的具体描述：1-★，2-★★，3-★★★，4-★★★★，5-★★★★★，6-★★★★★★，99-—。

## SQL示例

```sql
-- 查询 公募基金评级_济安金信 数据
SELECT *
FROM mf_jajxfundrating
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
