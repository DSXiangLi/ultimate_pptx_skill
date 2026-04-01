# MF_CLPerfAtrb

**中文名**: 基金CL选股择时能力分析

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CLPerfAtrb` |
| MySQL表名 | `mf_clperfatrb` |
| 中文名 | 基金CL选股择时能力分析 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：Chang&Lewellen在Treynor&Mazuy(TM)和Hensiksson&Merton(HM)模型的基础上继续研究，通过构建多头和空头时的基金组合得到选股能力与择时能力的结论。同理，选股能力或择时能力系数越大，表示基金选股能力或择时能力越强。
2.数据范围：2006年2月起-至今。
3.信息来源：根据证监会分类，选取股票型基金和混合型基金，同时剔除ETF型、ETF联接基金、指数型和指数增强型。算法基于CL模型:
R(p,t)-R(f,t)=α+β1 (R(m,t)-R(f,t) )*D1+β2 (R(m,t)-R(f,t) )*D2+ε(p,t) 其中：α为选股能力系数，β1-β2表示择时能力系数，β1和β2分别为多头和空头时的基金组合，当R(m,t)-R(f,t)>0，虚拟变量D1=1，D2=0，否则，D1=0，D2=1。基金收益率取自每周最后一个交易日的复权单位净值，无风险收益率取自一年期国债收益率/52，市场因子取自沪深300指数和上证国债指数(按照80%、20%取加权平均）

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 5 | `StockSelectionAbility` | 选股能力 | number(18,9) | ✗ | 100.0% |  |
| 6 | `StockSelectionPValue` | 选股能力P值 | number(18,9) | ✗ | 100.0% |  |
| 7 | `TimingAbility` | 择时能力 | number(18,9) | ✗ | 100.0% |  |
| 8 | `LongCoeffi` | 多头系数 | number(18,9) | ✗ | 100.0% |  |
| 9 | `LongPValue` | 多头P值 | number(18,9) | ✗ | 100.0% |  |
| 10 | `ShortCoeffi` | 空头系数 | number(18,9) | ✗ | 100.0% |  |
| 11 | `ShortPValue` | 空头P值 | number(18,9) | ✗ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,24,36,60,120)，得到指标周期的具体描述：6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年。

## SQL示例

```sql
-- 查询 基金CL选股择时能力分析 数据
SELECT *
FROM mf_clperfatrb
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
