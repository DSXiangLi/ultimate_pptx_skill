# MF_FundVaR

**中文名**: 基金在险价值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundVaR` |
| MySQL表名 | `mf_fundvar` |
| 中文名 | 基金在险价值 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：记录公募基金95%、99%置信水平下的不同时间区间(单日/双周)的在险价值(VaR)。VaR用于评价基金的下行风险，例如95%日VaR为A%，表示基金每100个交易日就有5天单日损失超过A%，99%双周VaR为B%，表示基金每100个交易日就有1天的近两周损失超过B%。
【计算方法：根据基金每个交易日公布的复权单位净值计算而得。c=∫f(x)dx, c=1-p，VaR(p)=-{Avg(基金日收益率序列)*T-Z_c*std(日收益率序列)*sqrt(T)}，
当时间区间分别取1日、双周，T分别取1、10, 当置信区间分别为95%、99%,Z_c分别为1.65、2.33。基金收益率的样本首日需大于等于截止日期往前追溯相应周期的日历日期加一天。】
2.数据范围：1998年3月起-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。

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
| 8 | `DataValue` | 指标值 | number(18,9) | ✗ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IndexCode (指标内码)

指标内码（IndexCode）：与“公募基金衍生指标基本资料（MF_DerivativeIndexInfo）”中的“指标代码（IndexCode）”关联，得到指标的名称、周期、指标的类型、指标涉及的对象等信息。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM IN (12,36)，得到指标周期的具体描述：12-一年，36-三年。

### TimeInterval (时间区间)

时间区间(TimeInterval)与(CT_SystemConst)表中的DM字段关联，令LB = 1174 AND DM IN (1,14)，得到时间区间的具体描述：1-日，14-两周。

## SQL示例

```sql
-- 查询 基金在险价值 数据
SELECT *
FROM mf_fundvar
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
