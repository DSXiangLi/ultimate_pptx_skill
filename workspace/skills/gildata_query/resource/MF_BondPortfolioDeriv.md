# MF_BondPortfolioDeriv

**中文名**: 基金重仓债券组合久期凸性

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BondPortfolioDeriv` |
| MySQL表名 | `mf_bondportfolioderiv` |
| 中文名 | 基金重仓债券组合久期凸性 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 季更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录公募基金重仓债券的组合久期凸性。
其中，计算规则如下：
（1）取公募基金季报中披露的重仓债券；
（2）计算该报告期各持仓债券的市值权重=持仓债券市值/（持仓债券市值合计值）；
（3）取《债券基础衍生指标》中各持仓债券的麦氏久期、修正久期、凸性，日期为小于等于报告期的最近交易日期；
（4）加权计算基金组合久期。
2.数据范围：2000年12月-至今。
3.信息来源：根据基金公司、证监会、交易所等披露的数据通过逻辑算法生成。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `IndexCode` | 指标内码 | number(10) | ✗ | 100.0% | 指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标... |
| 4 | `IndexName` | 指标名称 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB=2149 AND DM I... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `DataValue` | 指标值 | number(18,9) | ✓ | 69.34% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCode (指标内码)

指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB=2149 AND DM IN (3 ,6 ,12 ,24,36 ,60 ,120 ,998 ,999)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

## SQL示例

```sql
-- 查询 基金重仓债券组合久期凸性 数据
SELECT *
FROM mf_bondportfolioderiv
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
