# MF_FundDetermCoeffi

**中文名**: 公募基金衍生指标_基金可决系数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundDetermCoeffi` |
| MySQL表名 | `mf_funddetermcoeffi` |
| 中文名 | 公募基金衍生指标_基金可决系数 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：可决系数用于在拟合以基金收益率为因变量、沪深300指数收益率为自变量的回归方程后，进一步评价回归方程的解释作用，即沪深300指数对基金净值变动的作用，可决系数越大，表示大盘对基金收益的解释作用越大
2.数据范围：2005年月1月起-至今。
3.信息来源：根据基金和沪深300指数的日收益计算而得，等于基金与沪深300指数的相关系数的二次幂

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `IndexCode` | 指标内码 | number(10) | ✗ | 100.0% | 指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标... |
| 4 | `IndexName` | 指标名称 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `DataValue` | 指标值 | number(18,9) | ✗ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCode (指标内码)

指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM IN (3 ,6 ,12 ,24,36 ,60 ,120 ,998 ,999)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

## SQL示例

```sql
-- 查询 公募基金衍生指标_基金可决系数 数据
SELECT *
FROM mf_funddetermcoeffi
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
