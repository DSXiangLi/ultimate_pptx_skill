# MF_ScaleChange

**中文名**: 公募基金规模份额变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ScaleChange` |
| MySQL表名 | `mf_scalechange` |
| 中文名 | 公募基金规模份额变动 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析 |
| 更新频率 | 季更新 |
| 字段数量 | 31 |
| 版本 | 1.01 |

## 表描述

1.内容说明：记录公募基金规模与份额的相关统计指标的变动,包括不同周期的规模、合并规模、份额、合并份额、资产总值的变动、变动率、季度平均变动率，以及变动情况的同类均值与排名。具体规模与份额的计算规则参见（公募基金衍生指标_规模份额相关统计 MF_ScaleAnalysis）
2.数据范围：最新规模变动日。
3.信息来源：取自（公募基金衍生指标_规模份额相关统计 MF_ScaleAnalysis)

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TypeCode` | 基金分类口径代码 | number(10) | ✓ | 100.0% |  |
| 5 | `TypeName` | 基金分类口径描述 | varchar2(100) | ✗ | 100.0% | 基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类“ |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✓ | 99.94% | 基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTy... |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 99.94% |  |
| 8 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 9 | `NVIIChange` | 规模变动 | number(18,4) | ✓ | 99.91% |  |
| 10 | `NVIIROC` | 规模变动率 | number(18,4) | ✓ | 99.35% |  |
| 11 | `CombNVIIChange` | 合并规模变动 | number(18,4) | ✓ | 99.93% |  |
| 12 | `CombNVIIROC` | 合并规模变动率 | number(18,4) | ✓ | 99.93% |  |
| 13 | `SharesChange` | 份额变动 | number(18,4) | ✓ | 99.8% |  |
| 14 | `SharesROC` | 份额变动率 | number(18,4) | ✓ | 99.21% |  |
| 15 | `CombSharesChanges` | 合并份额变动 | number(18,4) | ✓ | 99.99% |  |
| 16 | `CombSharesROC` | 合并份额变动率 | number(18,4) | ✓ | 99.99% |  |
| 17 | `TotalAssetChange` | 资产总值变动 | number(18,4) | ✓ | 62.65% |  |
| 18 | `TotalAssetROC` | 资产总值变动率 | number(18,4) | ✓ | 62.65% |  |
| 19 | `QNVIIROC` | 规模季平均变动率 | number(18,4) | ✓ | 99.3% |  |
| 20 | `QCombNVIIROC` | 合并规模季平均变动率 | number(18,4) | ✓ | 99.8% |  |
| 21 | `NVIIROCTypeAvg` | 规模变动率同类均值 | number(18,4) | ✓ | 99.29% |  |
| 22 | `NVIIROCTypeRank` | 规模变动率同类排名 | varchar2(100) | ✓ | 99.29% |  |
| 23 | `CombNVIIROCTypeAvg` | 合并规模变动率同类均值 | number(18,4) | ✓ | 65.11% |  |
| 24 | `CombNVIIROCTypeRank` | 合并规模变动率同类排名 | varchar2(100) | ✓ | 65.11% |  |
| 25 | `QNVIIROCTypeAvg` | 规模季平均变动率同类均值 | number(18,4) | ✓ | 99.24% |  |
| 26 | `QNVIIROCRank` | 规模季平均变动率同类排名 | varchar2(100) | ✓ | 99.24% |  |
| 27 | `QCombNVIIROCTypeAvg` | 合并规模季平均变动率同类均值 | number(18,4) | ✓ | 64.98% |  |
| 28 | `QCombNVIIROCRank` | 合并规模季平均变动率排名 | varchar2(100) | ✓ | 64.98% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TypeName (基金分类口径描述)

基金分类口径描述(TypeName):表示基金分类标准。目前包括"证监会基金分类“

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述，1101-股票型，1103-混合型，1105-债券型，1110-QDII，1106-短期理财债券型，1109-货币型。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(3,6,12,36)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 公募基金规模份额变动 数据
SELECT *
FROM mf_scalechange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
