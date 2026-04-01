# Index_QFinIndicator

**中文名**: 指数单季度财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_QFinIndicator` |
| MySQL表名 | `index_qfinindicator` |
| 中文名 | 指数单季度财务指标 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 季度更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录主要境内指数单季度财务衍生指标，包括净资产收益率、总资产净利率、销售净利率、利润表同比环比等指标。
2.数据范围：2000-01-01至今
3.信息来源：聚源计算得到

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=Inne... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `IndexNC` | 指数成份股数量 | number(10) | ✓ | 100.0% |  |
| 6 | `CalcNC` | 计算用成份股数量 | number(10) | ✓ | 100.0% |  |
| 7 | `LossNC` | 指数亏损成份股数量 | number(10) | ✓ | 100.0% |  |
| 8 | `EPS` | 每股收益_期末股本摊薄(元/股) | number(12,4) | ✓ | 100.0% |  |
| 9 | `TotalOperateRevenuePS` | 每股营业总收入(元/股) | number(12,4) | ✓ | 99.99% |  |
| 10 | `OperCashFlowPS` | 每股经营活动产生的现金流量净额(元/股) | number(12,4) | ✓ | 99.72% |  |
| 11 | `ROEAvg` | 净资产收益率_平均(%) | number(12,4) | ✓ | 99.97% |  |
| 12 | `ROE` | 净资产收益率_摊薄(%) | number(12,4) | ✓ | 99.96% |  |
| 13 | `ROA` | 总资产净利率(%) | number(12,4) | ✓ | 99.98% |  |
| 14 | `DilutedROA` | 总资产净利率_摊薄(%) | number(12,4) | ✓ | 99.98% |  |
| 15 | `GrossIncomeRatio` | 销售毛利率(%) | number(12,4) | ✓ | 99.67% |  |
| 16 | `NetProfitRatio` | 销售净利率(%) | number(12,4) | ✓ | 99.98% |  |
| 17 | `NPToTOR` | 净利润/营业总收入(%) | number(12,4) | ✓ | 99.98% |  |
| 18 | `OperatingExpenseRate` | 销售费用/营业总收入(%) | number(12,4) | ✓ | 99.67% |  |
| 19 | `PeriodCostsRate` | 销售期间费用率(%) | number(12,4) | ✓ | 99.67% |  |
| 20 | `NPParentComOwnersYOY` | 归属母公司股东的净利润同比增长率(%) | number(12,4) | ✓ | 99.63% |  |
| 21 | `NPParentComOwnersMOM` | 归属母公司股东的净利润环比增长率(%) | number(12,4) | ✓ | 99.89% |  |
| 22 | `NetProfitYOY` | 净利润同比增长率(%) | number(12,4) | ✓ | 99.63% |  |
| 23 | `NetProfitMOM` | 净利润环比增长(%) | number(12,4) | ✓ | 99.89% |  |
| 24 | `OperatingRevenueYOY` | 营业收入同比增长率(%) | number(12,4) | ✓ | 99.61% |  |
| 25 | `OperatingRevenueMOM` | 营业收入环比增长率(%) | number(12,4) | ✓ | 99.85% |  |
| 26 | `NetOperateCashFlowYOY` | 经营活动产生的现金流量净额同比增长率(%) | number(12,4) | ✓ | 98.99% |  |
| 27 | `CashRateOfSales` | 经营活动产生的现金流量净额/营业收入(%) | number(12,4) | ✓ | 99.71% |  |
| 28 | `NetOpeCashFlowToNPPC` | 经营活动产生的现金流量净额/归属母公司股东的净利润(%) | number(12,4) | ✓ | 92.56% |  |
| 29 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 30 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode=InnerCode，得到指数内部编码的具体描述。

## SQL示例

```sql
-- 查询 指数单季度财务指标 数据
SELECT *
FROM index_qfinindicator
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
