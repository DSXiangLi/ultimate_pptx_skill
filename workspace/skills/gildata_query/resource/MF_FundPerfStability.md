# MF_FundPerfStability

**中文名**: 基金相对同类业绩稳定性

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundPerfStability` |
| MySQL表名 | `mf_fundperfstability` |
| 中文名 | 基金相对同类业绩稳定性 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：记录选定周期内公募基金收益率高于同类基金收益率均值的月份数与周期内总月数之比
2.数据范围：2014年7月起-至今。
3.信息来源：取自<公募基金收益率排名   MF_FundReturnRank >，令周期为N（月），每个截止日期T，取周期内N个时间节点，即日历日T-{1个月}、T-{2个月}……T-{(N-1)个月}，非交易的时间节点则取往前推的最新交易日，计算以上时间节点基金收益率高于同类基金收益均值的月份数M，业绩稳定性= M/N

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TypeCode` | 基金分类代码 | number(10) | ✗ | 100.0% | 基金分类代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 and DM... |
| 5 | `TypeName` | 基金分类描述 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% | 基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2197 AN... |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `IndexCode` | 指标内码 | number(10) | ✗ | 100.0% | 与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联... |
| 9 | `IndexName` | 指标名称 | varchar2(100) | ✗ | 100.0% |  |
| 10 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 11 | `DataValue` | 指标值 | number(18,9) | ✗ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TypeCode (基金分类代码)

基金分类代码(TypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 and DM = 75，得到基金分类代码的具体描述：75-聚源基金分类。

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2197 AND IVALUE = 1，得到基金类别代码的具体描述：11-股票型，12-混合型，13-债券型，14-货币型，15-QDII，16-商品型，17-REITs，18-FOF，99-其他。

### IndexCode (指标内码)

与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,36)，得到指标周期的具体描述：6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 基金相对同类业绩稳定性 数据
SELECT *
FROM mf_fundperfstability
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
