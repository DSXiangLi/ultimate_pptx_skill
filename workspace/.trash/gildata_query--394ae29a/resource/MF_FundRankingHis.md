# MF_FundRankingHis

**中文名**: 公募基金衍生指标同类均值与排名

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundRankingHis` |
| MySQL表名 | `mf_fundrankinghis` |
| 中文名 | 公募基金衍生指标同类均值与排名 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 周更新 |
| 字段数量 | 42 |
| 版本 | 1.01 |

## 表描述

1.内容说明：本表记录公募基金重要衍生指标在不同基金类别的历史排名与同类均值，指标包括收益评价指标（夏普比率、索提诺比率、卡玛比率、信息比率、平均月度回报、超基准年化收益、詹森阿尔法），风险评价指标（波动率、最大回撤、最大回撤修复天数、基准跟踪误差），业绩归因指标（选股能力、择时能力、大类资产配置能力、择券能力），以及基金综合评价。
2.数据范围：2006年2月-至今
3.信息来源：根据公募基金衍生数据库相应指标值排名而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TypeCode` | 基金分类口径代码 | number(10) | ✗ | 100.0% | 基金分类口径代码(TypeCode)：与系统常量表中的DM字段关联，令LB=1252，DM in(10,75),得到指标... |
| 5 | `TypeName` | 基金分类口径描述 | varchar2(100) | ✗ | 100.0% | 基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会分类“、”聚源二级分类“（聚源二级分类目前仅提供... |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTy... |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 9 | `CompEvaluation` | 综合测评 | number(8,4) | ✓ | 78.33% | 综合测评( CompEvaluation): 对证监会基金分类口径下的股票型、债券型、混合型、QDII基金进行综合评价。... |
| 10 | `SharpeRank` | 夏普比率排名(从大到小) | varchar2(100) | ✓ | 99.18% | 夏普比率排名(从大到小)（SharpeRank):取自公募基金衍生指标_基金夏普比率<MF_FundSharpeRati... |
| 11 | `SharpeTypeAvg` | 夏普比率同类均值 | number(18,9) | ✓ | 99.18% |  |
| 12 | `SortinoRank` | 索提诺比率排名(从大到小) | varchar2(100) | ✓ | 97.33% | 索提诺比率排名(从大到小)（SortinoRank):取自公募基金衍生指标_索提诺比率<MF_FundSortinoRa... |
| 13 | `SortinoTypeAvg` | 索提诺比率同类均值 | number(18,9) | ✓ | 97.33% |  |
| 14 | `CalmarRank` | 卡玛比率排名(从大到小) | varchar2(100) | ✓ | 97.45% | 卡玛比率排名(从大到小)（CalmarRank):取自公募基金衍生指标_卡玛比率<MF_CalmarRatio>。 |
| 15 | `CalmarTypeAvg` | 卡玛比率同类均值 | number(18,9) | ✓ | 97.45% |  |
| 16 | `InfoRatioRank` | 信息比率排名(从大到小) | varchar2(100) | ✓ | 95.83% | 信息比率排名(从大到小)（InfoRatioRank):取自公募基金衍生指标_基金信息比率<MF_FundInfoRat... |
| 17 | `InfoRatioTypeAvg` | 信息比率同类均值 | number(18,9) | ✓ | 95.83% |  |
| 18 | `MonRetRank` | 平均月度回报排名(从大到小) | varchar2(100) | ✓ | 98.87% | 平均月度回报排名(从大到小)（MonRetRank):取自公募基金衍生指标_基金绝对收益<MF_FundAbsolute... |
| 19 | `MonRetTypeAvg` | 平均月度回报均值(%) | number(18,9) | ✓ | 98.87% |  |
| 20 | `AbnRetRank` | 超基准年化收益排名(从大到小) | varchar2(100) | ✓ | 97.46% | 超基准年化收益排名(从大到小)（AbnRetRank):取自公募基金衍生指标_超基准年化收益<MF_AbnormalRe... |
| 21 | `AbnRetTypeAvg` | 超基准年化收益均值 | number(18,9) | ✓ | 97.46% |  |
| 22 | `JensonRank` | 詹森阿尔法排名(从大到小) | varchar2(100) | ✓ | 65.23% | 詹森阿尔法排名(从大到小)（JensenRank):取自公募基金衍生指标_基金詹森指数<MF_FundJensonInd... |
| 23 | `JensonTypeAvg` | 詹森阿尔法同类均值 | number(18,9) | ✓ | 65.23% |  |
| 24 | `VolRank` | 波动率排名(从小到大) | varchar2(100) | ✓ | 98.81% | 波动率排名(从小到大)（VolRank):取自公募基金衍生指标_基金收益标准差<MF_FundReturnSD>。 |
| 25 | `VolTypeAvg` | 波动率同类均值 | number(18,9) | ✓ | 98.81% |  |
| 26 | `MaxDDRank` | 最大回撤排名(从小到大) | varchar2(100) | ✓ | 99.36% | 最大回撤排名(从小到大)（MaxDDRank):取自公募基金衍生指标_基金最大回撤<MF_FundMaxDrawd>。 |
| 27 | `MaxDDTypeAvg` | 最大回撤同类均值 | number(18,9) | ✓ | 99.36% |  |
| 28 | `RestoreDRank` | 最大回撤修复天数排名(从小到大) | varchar2(100) | ✓ | 54.62% | 最大回撤修复天数排名(从小到大)（RestoreDRank):取自公募基金衍生指标_基金最大回撤修复天数<MF_Fund... |
| 29 | `RestoreDTypeAvg` | 最大回撤修复天数同类均值 | number(18,9) | ✓ | 96.53% |  |
| 30 | `TrackErrorRank` | 基准跟踪误差排名(从小到大) | varchar2(100) | ✓ | 96.76% | 基准跟踪误差排名(从小到大)（TrackErrorRank):取自公募基金衍生指标_基金相对基准收益标准差<MF_Fun... |
| 31 | `TrackErrorTypeAvg` | 基准跟踪误差均值 | number(18,9) | ✓ | 96.76% |  |
| 32 | `StockSelRank` | 选股能力排名(从大到小) | varchar2(100) | ✓ | 30.64% | 选股能力排名(从大到小)（StockSelRank):取自公募基金衍生指标_TMFF选股择时能力分析<MF_TMFFPe... |
| 33 | `StockSelectAbilityAvg` | 选股能力同类均值 | number(18,9) | ✓ | 30.64% |  |
| 34 | `TimingRank` | 择时能力排名(从大到小) | varchar2(100) | ✓ | 30.64% | 择时能力排名(从大到小)（TimingRank):取自公募基金衍生指标_TMFF选股择时能力分析<MF_TMFFPerf... |
| 35 | `TimingAbilityAvg` | 择时能力同类均值 | number(18,9) | ✓ | 30.64% |  |
| 36 | `AssetAlloRank` | 大类资产配置能力排名(从大到小) | varchar2(100) | ✓ | 1.02% | 大类资产配置能力排名(从大到小)(AssetAlloRank) :取自公募基金衍生指标_Brinson业绩归因 <MF_... |
| 37 | `AssetAlloAvg` | 大类资产配置能力同类均值 | number(18,9) | ✓ | 1.02% |  |
| 38 | `SecuSelRank` | 择券能力排名(从大到小) | varchar2(100) | ✓ | 1.02% | 择券能力排名(从大到小)(SecuSelRank) :取自公募基金衍生指标_Brinson业绩归因 <MF_Brinso... |
| 39 | `SecuSelAvg` | 择券能力同类均值 | number(18,9) | ✓ | 1.02% |  |
| 40 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 41 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 42 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TypeCode (基金分类口径代码)

基金分类口径代码(TypeCode)：与系统常量表中的DM字段关联，令LB=1252，DM in(10,75),得到指标周期的具体描述：10-证监会基金分类；75-聚源基金分类

### TypeName (基金分类口径描述)

基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会分类“、”聚源二级分类“（聚源二级分类目前仅提供1102-指数股票型,1304-指数债券型）。

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述。当基金分类口径描述(TypeName)=聚源二级分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=2197，IVALUE=2，得到聚源基金二级分类的具体描述(聚源二级分类目前仅提供1102-指数股票型,1304-指数债券型）。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(3,6,12,36,60,120)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，36-三年，60-五年，120-十年。

### CompEvaluation (综合测评)

综合测评( CompEvaluation): 对证监会基金分类口径下的股票型、债券型、混合型、QDII基金进行综合评价。数值越小表示排名越前。比如0.2，表示基金的综合能力位于同类的前20%。

### SharpeRank (夏普比率排名(从大到小))

夏普比率排名(从大到小)（SharpeRank):取自公募基金衍生指标_基金夏普比率<MF_FundSharpeRatio>。

### SortinoRank (索提诺比率排名(从大到小))

索提诺比率排名(从大到小)（SortinoRank):取自公募基金衍生指标_索提诺比率<MF_FundSortinoRatio>。

### CalmarRank (卡玛比率排名(从大到小))

卡玛比率排名(从大到小)（CalmarRank):取自公募基金衍生指标_卡玛比率<MF_CalmarRatio>。

### InfoRatioRank (信息比率排名(从大到小))

信息比率排名(从大到小)（InfoRatioRank):取自公募基金衍生指标_基金信息比率<MF_FundInfoRatio>。

## SQL示例

```sql
-- 查询 公募基金衍生指标同类均值与排名 数据
SELECT *
FROM mf_fundrankinghis
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
