# MF_FundReturnSDN

**中文名**: 基金收益标准差(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundReturnSDN` |
| MySQL表名 | `mf_fundreturnsdn` |
| 中文名 | 基金收益标准差(全) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系(全) |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：记录不同计算周期、计算步长下的标准差值（波动率）。
【计算公式：sqrt{∑[(Ri-∑Ri/N)^2]/(N-1)},其中：N表示交易日数，Ri表示基金复权净值日涨跌幅，基金收益率的样本首日需大于等于截止日期往前追溯相应周期的日历日期加一天。
（1）StepLength=1-日：年化波动率=波动率*250^0.5；StepLength=7-周：年化波动率=波动率*52^0.5；StepLength=30-月：年化波动率=波动率12^0.5；StepLength=365-年：年化波动率=波动率。（2）波动率（%）= 波动率*100%】
【本表使用：本表新增StepLength（步长）字段可用于计算步长的筛选。本表为非年化非百分比数值，可自行计算。
如计算近一月的年化标准差（%），可参照上述公式取 InSingleMonth*250^0.5*100%。
注：常用步长——StepLength = 1】
2.数据范围：2023.2.2-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。
注：本表计算的指标值均为非年化数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StepLength` | 步长 | number(10) | ✗ | 100.0% | 步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN ... |
| 5 | `InSingleMonth` | 截止日1月前 | number(18,9) | ✓ | 54.56% |  |
| 6 | `InTwoMonth` | 截止日2月前 | number(18,9) | ✓ | 57.41% |  |
| 7 | `InThreeMonth` | 截止日3月前 | number(18,9) | ✓ | 77.32% |  |
| 8 | `InSixMonth` | 截止日6月前 | number(18,9) | ✓ | 77.95% |  |
| 9 | `InSingleYear` | 截止日1年前 | number(18,9) | ✓ | 71.71% |  |
| 10 | `InTwoYear` | 截止日2年前 | number(18,9) | ✓ | 58.64% |  |
| 11 | `InThreeYear` | 截止日3年前 | number(18,9) | ✓ | 58.68% |  |
| 12 | `InFiveYear` | 截止日5年前 | number(18,9) | ✓ | 35.8% |  |
| 13 | `InSevenYear` | 截止日7年前 | number(18,9) | ✓ | 22.32% |  |
| 14 | `InTenYear` | 截止日10年前 | number(18,9) | ✓ | 9.29% |  |
| 15 | `SinceThisYear` | 今年以来 | number(18,9) | ✓ | 78.12% |  |
| 16 | `SinceStart` | 成立以来 | number(18,9) | ✓ | 99.22% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StepLength (步长)

步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN (1,7,30,365)，得到步长的具体描述：1-日，7-周，30-月，365-年。

## SQL示例

```sql
-- 查询 基金收益标准差(全) 数据
SELECT *
FROM mf_fundreturnsdn
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
