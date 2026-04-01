# MF_FundAlphaN

**中文名**: 基金阿尔法系数(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundAlphaN` |
| MySQL表名 | `mf_fundalphan` |
| 中文名 | 基金阿尔法系数(全) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析(全) |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：记录不同计算周期、计算步长、标的指数下的阿尔法指标值。
【计算公式：根据根据α=Y-βX：Y为基金收益率，X为标的指数收益率计算而得。
（1）StepLength=1（日）：年化阿尔法=阿尔法*250^0.5；
StepLength=7（周）：年化阿尔法=阿尔法*52^0.5；
StepLength=30（月）：年化阿尔法=阿尔法*12^0.5；
StepLength=365（年）：年化阿尔法=阿尔法。
（2）阿尔法（%）= 阿尔法*100%】
【本表使用：本表新增StepLength（步长），TargetIndexCode（标的指数）字段可用于计算步长和指数的筛选。本表为非年化非百分比数值，可自行计算。
如计算近一月的年化阿尔法（%），可参照上述公式取	InSingleMonth*250^0.5*100%。
注：常用步长——StepLength = 1； 常用指数——TargetIndexCode=3145。】
2.数据范围：2022.7.29-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。
注：本表计算的指标值均为非年化数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StepLength` | 步长 | number(10) | ✗ | 100.0% | 步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN ... |
| 5 | `TargetIndexCode` | 标的指数 | number(10) | ✗ | 100.0% | 标的指数(TargetIndexCode)：1-上证综指；3145-沪深300 |
| 6 | `InSingleMonth` | 截止日1月前 | number(19,10) | ✓ | 58.72% |  |
| 7 | `InTwoMonth` | 截止日2月前 | number(19,10) | ✓ | 58.31% |  |
| 8 | `InThreeMonth` | 截止日3月前 | number(19,10) | ✓ | 60.82% |  |
| 9 | `InSixMonth` | 截止日6月前 | number(19,10) | ✓ | 78.48% |  |
| 10 | `InSingleYear` | 截止日1年前 | number(19,10) | ✓ | 71.89% |  |
| 11 | `InTwoYear` | 截止日2年前 | number(19,10) | ✓ | 57.85% |  |
| 12 | `InThreeYear` | 截止日3年前 | number(19,10) | ✓ | 45.52% |  |
| 13 | `InFiveYear` | 截止日5年前 | number(19,10) | ✓ | 34.43% |  |
| 14 | `InSevenYear` | 截止日7年前 | number(19,10) | ✓ | 20.91% |  |
| 15 | `InTenYear` | 截止日10年前 | number(19,10) | ✓ | 8.77% |  |
| 16 | `SinceThisYear` | 今年以来 | number(19,10) | ✓ | 77.62% |  |
| 17 | `SinceStart` | 成立以来 | number(19,10) | ✓ | 95.57% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StepLength (步长)

步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN (1,7,30,365)，得到步长的具体描述：1-日，7-周，30-月，365-年。

### TargetIndexCode (标的指数)

标的指数(TargetIndexCode)：1-上证综指；3145-沪深300

## SQL示例

```sql
-- 查询 基金阿尔法系数(全) 数据
SELECT *
FROM mf_fundalphan
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
