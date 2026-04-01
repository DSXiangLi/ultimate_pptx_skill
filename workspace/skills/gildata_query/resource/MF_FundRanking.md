# MF_FundRanking

**中文名**: 公募基金衍生指标最新排名

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundRanking` |
| MySQL表名 | `mf_fundranking` |
| 中文名 | 公募基金衍生指标最新排名 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 月更新 |
| 字段数量 | 20 |
| 版本 | 1.03 |

## 表描述

1.内容说明：记录公募基金重要衍生指标在同类基金中的排名，具体包括绝对收益能力，总风险调整后收益能力、超额收益能力、稳定性、抗风险能力、选股能力、择时能力、基准跟踪能力、超基准收益能力，应用于雷达测评等场景。基金分类口径为证监会基金分类。
2.数据范围：每个月最后交易日更新最新数据
3.信息来源：根据公募基金衍生数据库相应指标值排名而得，具体指标参见注释。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `FundType` | 基金类型代码 | number(10) | ✗ | 100.0% | 基金类型代码(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1737 and DM... |
| 5 | `IndexCycle` | 排名周期 | number(10) | ✓ | 100.0% | 排名周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 6 | `AbsoluteReturnCapacity` | 绝对收益能力 | varchar2(100) | ✓ | 99.27% | 绝对收益能力（AbsoluteReturnCapacity）：“公募基金净值历史表现(MF_NetValuePerfor... |
| 7 | `ExcessEarningCapacity` | 超额收益能力 | varchar2(100) | ✓ | 63.46% | 超额收益能力（ExcessEarningCapacity）:“公募基金衍生指标_基金詹森指数(MF_FundJenson... |
| 8 | `RiskAdjReturnAbility` | 总风险调整后收益能力 | varchar2(100) | ✓ | 99.86% | 总风险调整后收益能力（RiskAdjReturnAbility）:“公募基金衍生指标_基金夏普比率(MF_FundSha... |
| 9 | `PerformanceStability` | 收益稳定性 | varchar2(100) | ✓ | 100.0% | 稳定性（PerformanceStability）:“公募基金衍生指标_基金收益标准差(MF_FundReturnSD)... |
| 10 | `AntiRiskCapability` | 抗风险能力 | varchar2(100) | ✓ | 99.95% | 抗风险能力（AntiRiskCapability）:“公募基金衍生指标_基金最大回撤(MF_FundMaxDrawd)”... |
| 11 | `StockSelectionAbility` | 选股能力 | varchar2(100) | ✓ | 35.07% | 选股能力（StockSelectionAbility）：“公募基金衍生指标_TMFF选股择时能力分析(MF_TMFFPe... |
| 12 | `TimingAbility` | 择时能力 | varchar2(100) | ✓ | 35.07% | 择时能力（TimingAbility）：“公募基金衍生指标_TMFF选股择时能力分析(MF_TMFFPerfAtrb)”... |
| 13 | `BenchmarkTrackAbility` | 基准跟踪能力 | varchar2(100) | ✓ | 98.71% | 基准跟踪能力（ BenchmarkTrackAbility）：“公募基金衍生指标_基金相对基准收益标准差(MF_Fund... |
| 14 | `ActiveReturnAbility` | 风险调整后超基准收益能力 | varchar2(100) | ✓ | 98.59% | 超基准收益能力（ActiveReturnAbility）：“公募基金衍生指标_基金信息比率(MF_FundInfoRat... |
| 15 | `AssetAlloAbility` | 大类资产配置能力 | varchar2(100) | ✓ | 0.0% |  |
| 16 | `SecuSelAbility` | 择券能力 | varchar2(100) | ✓ | 0.0% |  |
| 17 | `CompEvaluation` | 综合测评 | number(8,4) | ✓ | 99.95% | 综合测评( CompEvaluation): 对证监会基金分类口径下的股票型、债券型、混合型、QDII基金进行综合评价。... |
| 18 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundType (基金类型代码)

基金类型代码(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1737 and DM IN (1105,1103,1101,1110)，得到基金类型代码的具体描述：1101-股票型，1103-混合型，1105-债券型，1110-QDII。

### IndexCycle (排名周期)

排名周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM IN (3,6,12,36,60,120)，得到排名周期的具体描述：3-三个月，6-六个月，12-一年，36-三年，60-五年，120-十年。

### AbsoluteReturnCapacity (绝对收益能力)

绝对收益能力（AbsoluteReturnCapacity）：“公募基金净值历史表现(MF_NetValuePerformanceHis)”在基金类别内排名。

### ExcessEarningCapacity (超额收益能力)

超额收益能力（ExcessEarningCapacity）:“公募基金衍生指标_基金詹森指数(MF_FundJensonIndex)”在基金类别内排名。

### RiskAdjReturnAbility (总风险调整后收益能力)

总风险调整后收益能力（RiskAdjReturnAbility）:“公募基金衍生指标_基金夏普比率(MF_FundSharpeRatio)”在基金类别内排名。

### PerformanceStability (收益稳定性)

稳定性（PerformanceStability）:“公募基金衍生指标_基金收益标准差(MF_FundReturnSD)”在基金类别内排名。

### AntiRiskCapability (抗风险能力)

抗风险能力（AntiRiskCapability）:“公募基金衍生指标_基金最大回撤(MF_FundMaxDrawd)”在基金类别内排名。

### StockSelectionAbility (选股能力)

选股能力（StockSelectionAbility）：“公募基金衍生指标_TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的“选股能力(StockSelectionAbility)”在基金类别内排名。

### TimingAbility (择时能力)

择时能力（TimingAbility）：“公募基金衍生指标_TMFF选股择时能力分析(MF_TMFFPerfAtrb)”的“择时能力(TimingAbility)”在基金类别内排名。

## SQL示例

```sql
-- 查询 公募基金衍生指标最新排名 数据
SELECT *
FROM mf_fundranking
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
