# Index_PForecastFTM

**中文名**: 指数滚动盈利预测

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_PForecastFTM` |
| MySQL表名 | `index_pforecastftm` |
| 中文名 | 指数滚动盈利预测 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1 |

## 表描述

1.内容说明：本表计算未来12个月的指数盈利预测数据，包括预测市盈率、预测PEG、预测每股收益等指标。
2.数据范围：2016年10月至今
3.信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)：与"证券主表(SecuMain)"表中的"证券内部编码(InnerCode)"字段关... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `FPE` | 预测市盈率 | number(19,4) | ✓ | 99.81% |  |
| 5 | `FPEG` | 预测PEG | number(19,4) | ✓ | 98.66% |  |
| 6 | `FEPS` | 预测每股收益(元) | number(19,4) | ✓ | 99.81% |  |
| 7 | `FOCFPS` | 预测每股现金流 | number(19,4) | ✓ | 98.92% |  |
| 8 | `FROE` | 预测净资产收益率(%) | number(19,4) | ✓ | 98.98% |  |
| 9 | `FGrossIncomeRatio` | 预测毛利率(%) | number(19,4) | ✓ | 98.8% |  |
| 10 | `FOperatingIncome` | 预测营业收入(万元) | number(19,4) | ✓ | 99.7% |  |
| 11 | `FOperatingCost` | 预测营业成本(万元) | number(19,4) | ✓ | 98.8% |  |
| 12 | `FOpCostAndSurcharges` | 预测营业成本及附加(万元) | number(19,4) | ✓ | 0.0% |  |
| 13 | `FOperatingProfit` | 预测营业利润(万元) | number(19,4) | ✓ | 99.02% |  |
| 14 | `FTotalProfit` | 预测利润总额(万元) | number(19,4) | ✓ | 98.99% |  |
| 15 | `FNetProfit` | 预测净利润(万元) | number(19,4) | ✓ | 99.17% |  |
| 16 | `FNPParentComOwners` | 预测归属母公司的净利润(万元) | number(19,4) | ✓ | 99.81% |  |
| 17 | `FEBIT` | 预测息税前利润(万元) | number(19,4) | ✓ | 94.47% |  |
| 18 | `FEBITDA` | 预测息税折旧摊销前利润(万元) | number(19,4) | ✓ | 96.38% |  |
| 19 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 20 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)：与"证券主表(SecuMain)"表中的"证券内部编码(InnerCode)"字段关联，得到指数内部编码的具体描述

## SQL示例

```sql
-- 查询 指数滚动盈利预测 数据
SELECT *
FROM index_pforecastftm
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
