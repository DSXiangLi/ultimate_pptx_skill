# MF_FundCorrelCoeffiN

**中文名**: 基金相关系数(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundCorrelCoeffiN` |
| MySQL表名 | `mf_fundcorrelcoeffin` |
| 中文名 | 基金相关系数(全) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 风险评价体系(全) |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：记录不同计算周期、计算步长、标的指数下的相关系数指标值。
2.数据范围：2022.12.16-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StepLength` | 步长 | number(10) | ✗ | 100.0% | 步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN ... |
| 5 | `TargetIndexCode` | 标的指数 | number(10) | ✗ | 100.0% | 标的指数(TargetIndexCode)：1-上证综指；3145-沪深300 |
| 6 | `InSingleMonth` | 截止日1月前 | number(18,9) | ✓ | 53.37% |  |
| 7 | `InTwoMonth` | 截止日2月前 | number(18,9) | ✓ | 55.78% |  |
| 8 | `InThreeMonth` | 截止日3月前 | number(18,9) | ✓ | 79.01% |  |
| 9 | `InSixMonth` | 截止日6月前 | number(18,9) | ✓ | 76.15% |  |
| 10 | `InSingleYear` | 截止日1年前 | number(18,9) | ✓ | 70.45% |  |
| 11 | `InTwoYear` | 截止日2年前 | number(18,9) | ✓ | 58.68% |  |
| 12 | `InThreeYear` | 截止日3年前 | number(18,9) | ✓ | 60.45% |  |
| 13 | `InFiveYear` | 截止日5年前 | number(18,9) | ✓ | 35.31% |  |
| 14 | `InSevenYear` | 截止日7年前 | number(18,9) | ✓ | 21.85% |  |
| 15 | `InTenYear` | 截止日10年前 | number(18,9) | ✓ | 9.02% |  |
| 16 | `SinceThisYear` | 今年以来 | number(18,9) | ✓ | 77.51% |  |
| 17 | `SinceStart` | 成立以来 | number(18,9) | ✓ | 99.09% |  |
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
-- 查询 基金相关系数(全) 数据
SELECT *
FROM mf_fundcorrelcoeffin
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
