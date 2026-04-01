# MF_FundPandLProb

**中文名**: 基金盈亏概率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundPandLProb` |
| MySQL表名 | `mf_fundpandlprob` |
| 中文名 | 基金盈亏概率 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析 |
| 更新频率 | 日更新 |
| 字段数量 | 26 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录公募基金重要衍生指标，基金不同持有期的基金盈利、亏损概率和平均收益率。
【计算方法：指标周期内，基金盈利概率=持有期间的收益率>0的占比；基金亏损概率= 持有期间的收益率<0的占比；平均收益率= 持有期间的收益率均值。
如IndexCycle=12（即一年区间内），MonthlyProfitProb（历史盈利概率-持有1个月）=近一年区间内的 近一月收益率>0的占比。 】
2.数据范围：2023.1.30-至今。
3.信息来源：根据基金公司披露的净值数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM... |
| 5 | `Endpoint` | 区间端点 | number(10) | ✗ | 100.0% | 区间端点(EndDate): 收益率区间的上下限的绝对值：0 |
| 6 | `MonthlyProfitProb` | 历史盈利概率-持有1个月 | number(24,10) | ✓ | 100.0% |  |
| 7 | `ThreeMProfitProb` | 历史盈利概率-持有3个月 | number(24,10) | ✓ | 97.14% |  |
| 8 | `SixMProfitProb` | 历史盈利概率-持有6个月 | number(24,10) | ✓ | 92.72% |  |
| 9 | `YearProfitProb` | 历史盈利概率-持有一年 | number(24,10) | ✓ | 85.6% |  |
| 10 | `TwoYProfitProb` | 历史盈利概率-持有两年 | number(24,10) | ✓ | 72.63% |  |
| 11 | `ThreeYProfitProb` | 历史盈利概率-持有三年 | number(24,10) | ✓ | 59.58% |  |
| 12 | `MonthlyLossProb` | 历史亏损概率-持有1个月 | number(24,10) | ✓ | 100.0% |  |
| 13 | `ThreeMLossProb` | 历史亏损概率-持有3个月 | number(24,10) | ✓ | 97.14% |  |
| 14 | `SixMLossProb` | 历史亏损概率-持有6个月 | number(24,10) | ✓ | 92.72% |  |
| 15 | `YearlossProb` | 历史亏损概率-持有一年 | number(24,10) | ✓ | 85.6% |  |
| 16 | `TwoYLossProb` | 历史亏损概率-持有两年 | number(24,10) | ✓ | 72.63% |  |
| 17 | `ThreeYLossProb` | 历史亏损概率-持有三年 | number(24,10) | ✓ | 59.58% |  |
| 18 | `MonthlyAverage` | 平均收益率-持有1个月(%) | number(24,10) | ✓ | 100.0% |  |
| 19 | `ThreeMAverage` | 平均收益率-持有3个月(%) | number(24,10) | ✓ | 96.96% |  |
| 20 | `SixMAverage` | 平均收益率-持有6个月(%) | number(24,10) | ✓ | 92.34% |  |
| 21 | `YearAverage` | 平均收益率-持有一年(%) | number(24,10) | ✓ | 84.93% |  |
| 22 | `TwoYAverage` | 平均收益率-持有两年(%) | number(24,10) | ✓ | 70.99% |  |
| 23 | `ThreeYAverage` | 平均收益率-持有三年(%) | number(24,10) | ✓ | 58.06% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM IN (3 ,6 ,12 ,36 ,60 ,120 ,998 ,999)，得到指标周期的具体描述：3-三个月，6-六个月，12-一年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

### Endpoint (区间端点)

区间端点(EndDate): 收益率区间的上下限的绝对值：0

## SQL示例

```sql
-- 查询 基金盈亏概率 数据
SELECT *
FROM mf_fundpandlprob
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
