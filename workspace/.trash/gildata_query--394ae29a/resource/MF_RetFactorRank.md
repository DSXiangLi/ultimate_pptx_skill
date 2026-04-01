# MF_RetFactorRank

**中文名**: 基金收益类指标同类排名

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_RetFactorRank` |
| MySQL表名 | `mf_retfactorrank` |
| 中文名 | 基金收益类指标同类排名 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

记录选定周期内公募基金收益率高于沪深300与基准的月份数以及同类排名

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `TypeCode` | 基金分类口径代码 | number(10) | ✓ | 100.0% | 基金分类口径代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252  and... |
| 6 | `TypeName` | 基金分类口径描述 | varchar2(100) | ✗ | 100.0% | 基金分类口径描述(TypeName)：‘聚源二级分类’ |
| 7 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75... |
| 8 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `MonthWinHS300Rank` | 月度收益跑赢沪深300排名 | varchar2(100) | ✓ | 99.98% | 月度收益跑赢沪深300排名(MonthWinHS300Rank)：收益跑赢沪深300指数排名 |
| 10 | `MonthWinBenchRank` | 跑赢基准的月份数量排名 | varchar2(100) | ✓ | 98.41% | 跑赢基准的月份数量排名(MonthWinBenchRank)：跑赢基准的月份数量排序 |
| 11 | `MonthWinAvgCount` | 月度收益率高于同类均值的月份数 | number(10) | ✓ | 94.82% | 月度收益率高于同类均值的月份数(MonthWinAvgCount)：月度收益率高于同类基金收益率均值的月份数 |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(12,24,36,60,120)，得到指标周期的具体描述：12-一年，24-两年，36-三年，60-五年，120-十年。

### TypeCode (基金分类口径代码)

基金分类口径代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252  and DM = 75，得到基金分类口径代码的具体描述：75-聚源基金分类。

### TypeName (基金分类口径描述)

基金分类口径描述(TypeName)：‘聚源二级分类’

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75,的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

### MonthWinHS300Rank (月度收益跑赢沪深300排名)

月度收益跑赢沪深300排名(MonthWinHS300Rank)：收益跑赢沪深300指数排名

### MonthWinBenchRank (跑赢基准的月份数量排名)

跑赢基准的月份数量排名(MonthWinBenchRank)：跑赢基准的月份数量排序

### MonthWinAvgCount (月度收益率高于同类均值的月份数)

月度收益率高于同类均值的月份数(MonthWinAvgCount)：月度收益率高于同类基金收益率均值的月份数

## SQL示例

```sql
-- 查询 基金收益类指标同类排名 数据
SELECT *
FROM mf_retfactorrank
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
