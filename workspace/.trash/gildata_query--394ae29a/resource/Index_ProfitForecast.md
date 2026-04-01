# Index_ProfitForecast

**中文名**: 指数盈利预测

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_ProfitForecast` |
| MySQL表名 | `index_profitforecast` |
| 中文名 | 指数盈利预测 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 71 |
| 版本 | 1.02 |

## 表描述

1.内容说明：本表记录主要境内股票指数的盈利预测及衍生指标，包括预测市盈率、预测PEG、预测每股收益等指标。
2.数据范围：2008-01-01至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode = In... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `ForecastYear` | 预测年度 | number(10) | ✗ | 100.0% |  |
| 5 | `ForeYearLevel` | 预测年度层级 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `StatisPeriod` | 统计周期 | number(10) | ✗ | 100.0% | 统计周期(StatisPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND ... |
| 7 | `FPE` | 预测市盈率 | number(19,4) | ✓ | 99.67% |  |
| 8 | `FPEG` | 预测PEG | number(19,4) | ✓ | 98.17% | FPEG=Σ当日总市值 / Σ预测年度的预测归母净利润 / (预测年度的三年每股收益复合增长率*100)，当Σ预测年度的... |
| 9 | `FEPS` | 预测每股收益(元) | number(19,4) | ✓ | 99.67% |  |
| 10 | `FGrossIncomeRatio` | 预测毛利率(%) | number(19,4) | ✓ | 99.11% |  |
| 11 | `FOperatingIncome` | 预测营业收入(万元) | number(19,4) | ✓ | 99.59% |  |
| 12 | `FNetProfit` | 预测净利润(万元) | number(19,4) | ✓ | 99.33% |  |
| 13 | `FNPParentComOwners` | 预测归属母公司的净利润(万元) | number(19,4) | ✓ | 99.67% |  |
| 14 | `FPECoverRate` | 市盈率预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% | 市盈率预测公司覆盖率(%)(FPECoverRate)=研报提供预测归母净利润的公司数量/指数成份公司数量*100 |
| 15 | `FPEGCoverRate` | PEG预测公司覆盖率(%) | number(12,2) | ✓ | 74.16% |  |
| 16 | `FOpeRevCoverRate` | 营业收入预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 17 | `FPB` | 预测市净率 | number(19,4) | ✓ | 99.24% |  |
| 18 | `FROE` | 预测净资产收益率(%) | number(19,4) | ✓ | 99.24% |  |
| 19 | `FOCFPS` | 预测每股现金流 | number(19,4) | ✓ | 98.6% |  |
| 20 | `FDPS` | 预测每股股利 | number(19,4) | ✓ | 98.25% |  |
| 21 | `FBPS` | 预测每股净资产 | number(19,4) | ✓ | 99.24% |  |
| 22 | `FEBIT` | 预测息税前利润(万元) | number(19,4) | ✓ | 70.75% |  |
| 23 | `FEBITDA` | 预测息税折旧摊销前利润(万元) | number(19,4) | ✓ | 97.02% |  |
| 24 | `FTotalProfit` | 预测利润总额(万元) | number(19,4) | ✓ | 99.25% |  |
| 25 | `FOperatingProfit` | 预测营业利润(万元) | number(19,4) | ✓ | 99.27% |  |
| 26 | `FOperatingCost` | 预测营业成本(万元) | number(19,4) | ✓ | 99.12% |  |
| 27 | `FEPSYOY` | 预测每股收益同比增长率(%) | number(19,4) | ✓ | 74.67% |  |
| 28 | `FGrossIncomeRatioYOY` | 预测毛利率同比增长率(%) | number(19,4) | ✓ | 74.09% |  |
| 29 | `FOperatingIncomeYOY` | 预测营业收入同比增长率(%) | number(19,4) | ✓ | 74.59% |  |
| 30 | `FNetProfitYOY` | 预测净利润同比增长率(%) | number(19,4) | ✓ | 74.33% |  |
| 31 | `FNPParentComOwnersYOY` | 预测归属母公司的净利润同比增长率(%) | number(19,4) | ✓ | 74.67% |  |
| 32 | `FROEYOY` | 预测净资产收益率同比增长率(%) | number(19,4) | ✓ | 74.23% |  |
| 33 | `FOCFPSYOY` | 预测每股现金流同比增长率(%) | number(19,4) | ✓ | 73.56% |  |
| 34 | `FDPSYOY` | 预测每股股利同比增长率(%) | number(19,4) | ✓ | 72.91% |  |
| 35 | `FBPSYOY` | 预测每股净资产同比增长率(%) | number(19,4) | ✓ | 74.23% |  |
| 36 | `FEBITYOY` | 预测息税前利润同比增长率(%) | number(19,4) | ✓ | 46.92% |  |
| 37 | `FEBITDAYOY` | 预测息税折旧摊销前利润同比增长率(%) | number(19,4) | ✓ | 72.25% |  |
| 38 | `FTotalProfitYOY` | 预测利润总额同比增长率(%) | number(19,4) | ✓ | 74.24% |  |
| 39 | `FOperatingProfitYOY` | 预测营业利润同比增长率(%) | number(19,4) | ✓ | 74.25% |  |
| 40 | `FOperatingCostYOY` | 预测营业成本同比增长率(%) | number(19,4) | ✓ | 73.84% |  |
| 41 | `FEPSGrowRate` | 预测每股收益复合增长率(%) | number(19,4) | ✓ | 47.99% |  |
| 42 | `FGrossIncomeGrowRate` | 预测毛利率复合增长率(%) | number(19,4) | ✓ | 49.31% |  |
| 43 | `FOpeRevGrowRate` | 预测营业收入复合增长率(%) | number(19,4) | ✓ | 49.6% |  |
| 44 | `FNetProfitGrowRate` | 预测净利润复合增长率(%) | number(19,4) | ✓ | 47.91% |  |
| 45 | `FNPParentComOwnersGrowRate` | 预测归属母公司的净利润复合增长率(%) | number(19,4) | ✓ | 47.99% |  |
| 46 | `FROEGrowRate` | 预测净资产收益率复合增长率(%) | number(19,4) | ✓ | 47.83% |  |
| 47 | `FOCFPSGrowRate` | 预测每股现金流复合增长率(%) | number(19,4) | ✓ | 46.67% |  |
| 48 | `FDPSGrowRate` | 预测每股股利复合增长率(%) | number(19,4) | ✓ | 48.69% |  |
| 49 | `FBPSGrowRate` | 预测每股净资产复合增长率(%) | number(19,4) | ✓ | 49.48% |  |
| 50 | `FEBITGrowRate` | 预测息税前利润复合增长率(%) | number(19,4) | ✓ | 0.0% |  |
| 51 | `FEBITDAGrowRate` | 预测息税折旧摊销前利润复合增长率(%) | number(19,4) | ✓ | 47.82% |  |
| 52 | `FTotalProfitGrowRate` | 预测利润总额复合增长率(%) | number(19,4) | ✓ | 48.15% |  |
| 53 | `FOperatingProfitGrowRate` | 预测营业利润复合增长率(%) | number(19,4) | ✓ | 48.0% |  |
| 54 | `FOperatingCostGrowRate` | 预测营业成本复合增长率(%) | number(19,4) | ✓ | 48.9% |  |
| 55 | `FEPSCoverRate` | 每股收益预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 56 | `FGrossIncomeCoverRate` | 毛利率预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 57 | `FNetProfitCoverRate` | 净利润预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 58 | `FNPParentComOwnersCoverRate` | 归属母公司的净利润预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 59 | `FEBITCoverRate` | 息税前利润预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 60 | `FEBITDACoverRate` | 息税折旧摊销前利润预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 61 | `FTotalProfitCoverRate` | 利润总额预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 62 | `FOperatingProfitCoverRate` | 营业利润预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 63 | `FOperatingCostCoverRate` | 营业成本预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 64 | `FPBCoverRate` | 市净率预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 65 | `FROECoverRate` | 净资产收益率预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 66 | `FOCFPSCoverRate` | 每股现金流预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 67 | `FDPSCoverRate` | 每股股利预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 68 | `FBPSCoverRate` | 每股净资产预测公司覆盖率(%) | number(12,2) | ✓ | 75.0% |  |
| 69 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 70 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 71 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)与(SecuMain)表中的InnerCode字段关联，令IndexCode = InnerCode，得到指数内部编码的具体描述：

### StatisPeriod (统计周期)

统计周期(StatisPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 AND DM in (6)，得到统计周期的具体描述：6-六个月。

### FPEG (预测PEG)

FPEG=Σ当日总市值 / Σ预测年度的预测归母净利润 / (预测年度的三年每股收益复合增长率*100)，当Σ预测年度的预测归母净利润小于Σ预测年度三年前的归母净利润时，该字段为空，不进行计算

### FPECoverRate (市盈率预测公司覆盖率(%))

市盈率预测公司覆盖率(%)(FPECoverRate)=研报提供预测归母净利润的公司数量/指数成份公司数量*100

## SQL示例

```sql
-- 查询 指数盈利预测 数据
SELECT *
FROM index_profitforecast
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
