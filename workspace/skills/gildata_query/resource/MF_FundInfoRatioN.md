# MF_FundInfoRatioN

**中文名**: 基金信息比率(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundInfoRatioN` |
| MySQL表名 | `mf_fundinforation` |
| 中文名 | 基金信息比率(全) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析(全) |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：表示基金相对自身业绩比较基准产生的每个单位的跟踪误差，所获得的超额收益，用于评价基金相对自身基准的风险调整后收益能力.
2.数据范围：StepLength=1部分2018年1月起-至今。其余2022.11.11-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。
注：本表计算的指标值均为非年化数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StepLength` | 步长 | number(10) | ✗ | 100.0% | 步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令 LB=1174 AND DM IN... |
| 5 | `TargetIndexCode` | 标的指数 | number(10) | ✗ | 100.0% | 标的指数(TargetIndexCode)：1-上证综指，3145-沪深300，4978-中证500，46-上证50，1... |
| 6 | `InSingleMonth` | 截止日1月前 | number(19,10) | ✓ | 61.26% |  |
| 7 | `InTwoMonth` | 截止日2月前 | number(19,10) | ✓ | 63.23% |  |
| 8 | `InThreeMonth` | 截止日3月前 | number(19,10) | ✓ | 82.11% |  |
| 9 | `InSixMonth` | 截止日6月前 | number(19,10) | ✓ | 78.84% |  |
| 10 | `InSingleYear` | 截止日1年前 | number(19,10) | ✓ | 72.46% |  |
| 11 | `InTwoYear` | 截止日2年前 | number(19,10) | ✓ | 58.74% |  |
| 12 | `InThreeYear` | 截止日3年前 | number(19,10) | ✓ | 58.01% |  |
| 13 | `InFiveYear` | 截止日5年前 | number(19,10) | ✓ | 33.97% |  |
| 14 | `InSevenYear` | 截止日7年前 | number(19,10) | ✓ | 20.82% |  |
| 15 | `InTenYear` | 截止日10年前 | number(19,10) | ✓ | 8.6% |  |
| 16 | `SinceThisYear` | 今年以来 | number(19,10) | ✓ | 81.62% |  |
| 17 | `SinceStart` | 成立以来 | number(19,10) | ✓ | 99.52% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StepLength (步长)

步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令 LB=1174 AND DM IN (1,7,30,365)，得到步长的具体描述：1-日，7-周，30-月，365-年。

### TargetIndexCode (标的指数)

标的指数(TargetIndexCode)：1-上证综指，3145-沪深300，4978-中证500，46-上证50，11089-创业板指，0-业绩基准

## SQL示例

```sql
-- 查询 基金信息比率(全) 数据
SELECT *
FROM mf_fundinforation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
