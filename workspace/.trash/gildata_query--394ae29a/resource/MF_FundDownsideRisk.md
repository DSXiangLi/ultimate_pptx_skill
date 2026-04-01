# MF_FundDownsideRisk

**中文名**: 基金下行风险

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundDownsideRisk` |
| MySQL表名 | `mf_funddownsiderisk` |
| 中文名 | 基金下行风险 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 周更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：类似下行标准差，也是标准差的变形，计算时忽略“好”的收益，代表“不良”收益的波动率，用于评价基金的下行风险，“不良”的基准为一年期国债收益率
2.数据范围：2006年月2月起-至今。
3.信息来源：根据基金每周最后交易日的复权单位净值计算而得，
公式为：下行风险={∑[Min（0，Ri-Rf/52)^2]/N}^0.5，下行风险(年化)=sqrt(52)* {∑[Min（0，Ri-Rf/52)^2]/N}^0.5，其中:Ri表示基金复权单位净值周增长率，Rf表示样本首日的一年期国债收益率，N表示样本区间所含样本周数，基金收益率的样本首日需大于等于截止日期往前追溯相应周期的日历日期加一天，周期一年（含）以上为年化下行风险

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

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM IN (3 ,6 ,12 ,24,36 ,60 ,120 )，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，24-两年，36-三年，60-五年，120-十年。

## SQL示例

```sql
-- 查询 基金下行风险 数据
SELECT *
FROM mf_funddownsiderisk
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
