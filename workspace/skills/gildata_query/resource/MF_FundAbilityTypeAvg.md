# MF_FundAbilityTypeAvg

**中文名**: 公募基金衍生指标最新同类均值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundAbilityTypeAvg` |
| MySQL表名 | `mf_fundabilitytypeavg` |
| 中文名 | 公募基金衍生指标最新同类均值 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 月更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录公募基金重要衍生指标的指标值、同类型基金平均值，可与公募基金衍生指标最新排名(MF_FundRanking)配合使用，具体包括绝对收益能力，总风险调整后收益能力、超额收益能力、稳定性、抗风险能力、选股能力、择时能力、基准跟踪能力、超基准收益能力和综合排名。
2.数据范围：每个月最后交易日更新最新数据(更新数据为每月最后一个星期五对应数据）
3.信息来源：根据公募基金衍生数据库相应指标值计算同类基金指标均值，具体指标参见注释。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `FundType` | 基金类型代码 | number(10) | ✗ | 100.0% | 基金类型代码(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1737 and DM... |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 6 | `AbsoluteReturnCapacity` | 绝对收益能力(指标值) | number(18,9) | ✓ | 99.95% | 绝对收益能力（AbsoluteReturnCapacity）：“公募基金净值历史表现(MF_NVPerformanceT... |
| 7 | `AbsReturnCapacityAvg` | 绝对收益能力同类均值 | number(18,9) | ✓ | 99.95% |  |
| 8 | `ExcessEarningCapacity` | 超额收益能力(指标值) | number(18,9) | ✓ | 38.52% | 超额收益能力（ExcessEarningCapacity）：“基金詹森指数(MF_FundJensonIndex)”在基... |
| 9 | `ExcEarningCapacityAvg` | 超额收益能力同类均值 | number(18,9) | ✓ | 38.52% |  |
| 10 | `RiskAdjReturnAbility` | 总风险调整后收益能力(指标值) | number(18,9) | ✓ | 99.42% | 风险调整后收益能力（RiskAdjReturnAbility）：“基金夏普比率(MF_FundSharpeRatio)”... |
| 11 | `RiskAdjRetAbilityAvg` | 总风险调整后收益能力同类均值 | number(18,9) | ✓ | 99.42% |  |
| 12 | `PerformanceStability` | 收益稳定性(指标值) | number(18,9) | ✓ | 98.25% | 稳定性（PerformanceStability）：“基金收益标准差(MF_FundReturnSD)”在基金类别内排名... |
| 13 | `PerfStabilityAvg` | 收益稳定性同类均值 | number(18,9) | ✓ | 98.25% |  |
| 14 | `AntiRiskCapability` | 抗风险能力(指标值) | number(18,9) | ✓ | 99.76% | 抗风险能力（AntiRiskCapability）：“基金最大回撤(MF_FundMaxDrawd)”在基金类别内排名对... |
| 15 | `AntiRiskCapabilityAvg` | 抗风险能力同类均值 | number(18,9) | ✓ | 99.76% |  |
| 16 | `StockSelectionAbility` | 选股能力(指标值) | number(18,9) | ✓ | 22.62% | 选股能力（StockSelectionAbility）：“TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的... |
| 17 | `StockSelectAbilityAvg` | 选股能力同类均值 | number(18,9) | ✓ | 22.62% |  |
| 18 | `TimingAbility` | 择时能力(指标值) | number(18,9) | ✓ | 22.62% | 择时能力（TimingAbility）：“TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的“择时能力(Ti... |
| 19 | `TimingAbilityAvg` | 择时能力同类均值 | number(18,9) | ✓ | 22.62% |  |
| 20 | `BenchmarkTrackAbility` | 基准跟踪能力(指标值) | number(18,9) | ✓ | 84.23% | 基准跟踪能力（BenchmarkTrackingAbility）：“基金相对基准收益标准差(MF_FundExcessR... |
| 21 | `BenchTrackAbilityAvg` | 基准跟踪能力同类均值 | number(18,9) | ✓ | 84.23% |  |
| 22 | `ActiveReturnAbility` | 风险调整后超基准收益能力(指标值) | number(18,9) | ✓ | 59.73% | 超基准收益能力（ActiveReturnAbility）：“基金信息比率(MF_FundInfoRatio)”在基金类别... |
| 23 | `ActiveReturnAbilityAvg` | 风险调整后超基准收益能力同类均值 | number(18,9) | ✓ | 59.73% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundType (基金类型代码)

基金类型代码(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1737 and DM IN (1101,1103,1105,1110)，得到基金类型代码的具体描述：1101-股票型，1103-混合型，1105-债券型，1110-QDII。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(1,3,6,12,24, 36,60,120,998,999)，得到指标周期的具体描述：1-一个月，3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

### AbsoluteReturnCapacity (绝对收益能力(指标值))

绝对收益能力（AbsoluteReturnCapacity）：“公募基金净值历史表现(MF_NVPerformanceTransH)”在基金类别内排名对应的指标值。

### ExcessEarningCapacity (超额收益能力(指标值))

超额收益能力（ExcessEarningCapacity）：“基金詹森指数(MF_FundJensonIndex)”在基金类别内排名对应的指标值。

### RiskAdjReturnAbility (总风险调整后收益能力(指标值))

风险调整后收益能力（RiskAdjReturnAbility）：“基金夏普比率(MF_FundSharpeRatio)”在基金类别内排名对应的指标值。

### PerformanceStability (收益稳定性(指标值))

稳定性（PerformanceStability）：“基金收益标准差(MF_FundReturnSD)”在基金类别内排名对应的指标值。

### AntiRiskCapability (抗风险能力(指标值))

抗风险能力（AntiRiskCapability）：“基金最大回撤(MF_FundMaxDrawd)”在基金类别内排名对应的指标值。

### StockSelectionAbility (选股能力(指标值))

选股能力（StockSelectionAbility）：“TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的“选股能力(StockSelectionAbility)”在基金类别内排名对应的指标值。

### TimingAbility (择时能力(指标值))

择时能力（TimingAbility）：“TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的“择时能力(TimingAbility)”在基金类别内排名对应的指标值。

## SQL示例

```sql
-- 查询 公募基金衍生指标最新同类均值 数据
SELECT *
FROM mf_fundabilitytypeavg
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
