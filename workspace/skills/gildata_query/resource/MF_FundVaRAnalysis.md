# MF_FundVaRAnalysis

**中文名**: 基金在险价值同类分析

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundVaRAnalysis` |
| MySQL表名 | `mf_fundvaranalysis` |
| 中文名 | 基金在险价值同类分析 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：记录公募基金95%、99%置信水平下的单日VaR和2周VaR的同类均值与排名。VaR用于评价基金的下行风险，例如95%日VaR为A%，表示基金每100个交易日就有5天单日损失超过A%，99%双周VaR为B%，表示基金每100个交易日就有1天的近两周损失超过B%。
2.数据范围：1998年3月起-至今。
3.信息来源：取自<公募基金衍生指标_基金在险价值   MF_FundVaR >，将截止日期相同基金类别、置信区间、指标周期和时间区间的VaR指标按升序排名、计算同类基金平均值。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `IndexCode` | 指标内码 | number(10) | ✗ | 100.0% | 指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标... |
| 4 | `IndexName` | 指标名称 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `TimeInterval` | 时间区间 | number(10) | ✗ | 100.0% | 时间区间(TimeInterval)与(CT_SystemConst)表中的DM字段关联，令LB = 1174 AND ... |
| 8 | `TypeCode` | 基金分类代码 | number(10) | ✓ | 100.0% | 基金分类代码（TypeCode）：与系统常量表中的DM字段关联，令LB=1252，得到指标周期的具体描述：10-证监会基... |
| 9 | `TypeName` | 基金分类描述 | varchar2(100) | ✗ | 100.0% |  |
| 10 | `FundTypeCode` | 基金类别代码 | number(10) | ✓ | 100.0% | 基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1737，得到... |
| 11 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 100.0% |  |
| 12 | `VaR` | 在险价值 | number(18,9) | ✗ | 100.0% |  |
| 13 | `AvgVaR` | VaR同类均值 | number(18,9) | ✗ | 100.0% |  |
| 14 | `AvgVaRTypeRank` | VaR同类排名 | varchar2(100) | ✗ | 100.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCode (指标内码)

指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(12,36)，得到指标周期的具体描述：12-一年，36-三年。

### TimeInterval (时间区间)

时间区间(TimeInterval)与(CT_SystemConst)表中的DM字段关联，令LB = 1174 AND DM IN (1,14)，得到时间区间的具体描述：1-日，14-两周。

### TypeCode (基金分类代码)

基金分类代码（TypeCode）：与系统常量表中的DM字段关联，令LB=1252，得到指标周期的具体描述：10-证监会基金分类等。

### FundTypeCode (基金类别代码)

基金类别代码(FundTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1737，得到基金类别代码的具体描述：1101-股票型，1103-混合型，1105-债券型，1106-短期理财债券型，1109-货币型，1110-QDII，1111-基金中基金（FOF），1112-基础设施基金，1113-商品基金。

## SQL示例

```sql
-- 查询 基金在险价值同类分析 数据
SELECT *
FROM mf_fundvaranalysis
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
