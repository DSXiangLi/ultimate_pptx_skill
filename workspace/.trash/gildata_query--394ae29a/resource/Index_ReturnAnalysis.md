# Index_ReturnAnalysis

**中文名**: 指数收益指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_ReturnAnalysis` |
| MySQL表名 | `index_returnanalysis` |
| 中文名 | 指数收益指标 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 29 |
| 版本 | 1 |

## 表描述

1.内容说明：收录指数收益指标，包括夏普比率、信息比率、特雷诺比率、阿尔法系数等，衡量指数的盈利能力。计算周期为日度，无风险收益率为一年期国债收益率，采用普通收益率进行计算。
2.数据范围:指数基日至今
3.信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=Inne... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `IndicatorType` | 指标类型 | number(10) | ✗ | 100.0% | 指标类型(IndicatorType)与(CT_SystemConst)表中的DM字段关联，令LB=2148 AND D... |
| 5 | `TargetIndexCode` | 标的指数 | number(10) | ✓ | 65.76% | 标的指数(TargetIndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=... |
| 6 | `ReferrenceYield` | 参考收益率 | number(10) | ✓ | 49.66% | 参考收益率(ReferrenceYield)与(SecuMain)表中的InnerCode字段关联，令Referrenc... |
| 7 | `DataValueRW` | 近1周指标值 | number(22,6) | ✓ | 98.95% |  |
| 8 | `DataValueRWTwo` | 近2周指标值 | number(22,6) | ✓ | 99.76% |  |
| 9 | `DataValueRWFour` | 近4周指标值 | number(22,6) | ✓ | 99.78% |  |
| 10 | `DataValueRWFT` | 近52周指标值 | number(22,6) | ✓ | 99.85% |  |
| 11 | `DataValueRM` | 近1月指标值 | number(22,6) | ✓ | 99.78% |  |
| 12 | `DataValueRMTwo` | 近2月指标值 | number(22,6) | ✓ | 99.79% |  |
| 13 | `DataValueRMThree` | 近3月指标值 | number(22,6) | ✓ | 99.8% |  |
| 14 | `DataValueRMSix` | 近6月指标值 | number(22,6) | ✓ | 99.82% |  |
| 15 | `DataValueRY` | 近1年指标值 | number(22,6) | ✓ | 99.85% |  |
| 16 | `DataValueRYTwo` | 近2年指标值 | number(22,6) | ✓ | 99.9% |  |
| 17 | `DataValueRYThree` | 近3年指标值 | number(22,6) | ✓ | 99.93% |  |
| 18 | `DataValueRYFive` | 近5年指标值 | number(22,6) | ✓ | 99.95% |  |
| 19 | `DataValueRYTen` | 近10年指标值 | number(22,6) | ✓ | 99.96% |  |
| 20 | `DataValueTW` | 本周以来指标值 | number(22,6) | ✓ | 82.18% |  |
| 21 | `DataValueTM` | 本月以来指标值 | number(22,6) | ✓ | 95.51% |  |
| 22 | `DataValueTQ` | 本季度以来指标值 | number(22,6) | ✓ | 98.31% |  |
| 23 | `DataValueYTD` | 今年以来指标值 | number(22,6) | ✓ | 99.47% |  |
| 24 | `DataValueSHY` | 下半年以来指标值 | number(22,6) | ✓ | 51.05% |  |
| 25 | `DataValueFL` | 上市以来指标值 | number(22,6) | ✓ | 66.98% |  |
| 26 | `DataValueFB` | 基日以来指标值 | number(22,6) | ✓ | 99.95% |  |
| 27 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 28 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 29 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=InnerCode，得到指数内部编码的具体描述

### IndicatorType (指标类型)

指标类型(IndicatorType)与(CT_SystemConst)表中的DM字段关联，令LB=2148 AND DM in (1,3,4,5,28,82)，得到指标类型的具体描述：1-夏普比率，3-信息比率，4-特雷诺指数，5-詹森指数，28-阿尔法系数，82-平均收益率。

### TargetIndexCode (标的指数)

标的指数(TargetIndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=InnerCode，得到指数内部编码的具体描述

### ReferrenceYield (参考收益率)

参考收益率(ReferrenceYield)与(SecuMain)表中的InnerCode字段关联，令ReferrenceYield=InnerCode，得到指数内部编码的具体描述，ReferrenceYield固定为451399-一年期国债收益率

## SQL示例

```sql
-- 查询 指数收益指标 数据
SELECT *
FROM index_returnanalysis
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
