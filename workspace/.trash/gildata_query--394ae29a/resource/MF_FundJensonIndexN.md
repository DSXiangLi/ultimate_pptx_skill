# MF_FundJensonIndexN

**中文名**: 基金詹森指数(全)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundJensonIndexN` |
| MySQL表名 | `mf_fundjensonindexn` |
| 中文名 | 基金詹森指数(全) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 收益与规模分析(全) |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1 |

## 表描述

1.内容说明：基金收益评价指标，表示基金实际收益率与位于证券市场线（SML）上的证券组合的期望收益率之差，用于评价基金相对沪深300指数等指数的阿尔法能力。
詹森指数=Ri,t—[Rf,t+βi(Rm,t-Rft)]，其中： Rm,t为市场投资组合（标的指数）在t时期的收益率；Ri,t为i基金在t时期的收益率；Rf,t为t时期的无风险收益率，βi为基金投资组合所承担的系统风险。
2.数据范围：2022.10.11-至今。
3.信息来源：根据基金公司官网披露的净值数据计算而得。
注：本表计算的指标值均为非年化数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StepLength` | 步长 | number(10) | ✗ | 100.0% | 步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN ... |
| 5 | `YieldRiskFreeCode` | 无风险收益率内码 | number(10) | ✗ | 100.0% | 无风险收益率内码(YieldRiskFreeCode)：451399-一年期国债收益率；451400-十年期国债收益率；... |
| 6 | `TargetIndexCode` | 标的指数 | number(10) | ✗ | 100.0% | 标的指数(TargetIndexCode)：1-上证综指；3145-沪深300 |
| 7 | `InSingleMonth` | 截止日1月前 | number(18,9) | ✓ | 53.85% |  |
| 8 | `InTwoMonth` | 截止日2月前 | number(18,9) | ✓ | 53.61% |  |
| 9 | `InThreeMonth` | 截止日3月前 | number(18,9) | ✓ | 56.45% |  |
| 10 | `InSixMonth` | 截止日6月前 | number(18,9) | ✓ | 77.32% |  |
| 11 | `InSingleYear` | 截止日1年前 | number(18,9) | ✓ | 71.62% |  |
| 12 | `InTwoYear` | 截止日2年前 | number(18,9) | ✓ | 58.24% |  |
| 13 | `InThreeYear` | 截止日3年前 | number(18,9) | ✓ | 45.9% |  |
| 14 | `InFiveYear` | 截止日5年前 | number(18,9) | ✓ | 35.75% |  |
| 15 | `InSevenYear` | 截止日7年前 | number(18,9) | ✓ | 22.27% |  |
| 16 | `InTenYear` | 截止日10年前 | number(18,9) | ✓ | 9.21% |  |
| 17 | `SinceThisYear` | 今年以来 | number(18,9) | ✓ | 75.0% |  |
| 18 | `SinceStart` | 成立以来 | number(18,9) | ✓ | 95.39% |  |
| 19 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### StepLength (步长)

步长(StepLength)与(CT_SystemConst)表中的DM字段关联，令LB=1174 AND DM IN (1,7,30,365)，得到步长的具体描述：1-1，7-7，30-30，365-365。

### YieldRiskFreeCode (无风险收益率内码)

无风险收益率内码(YieldRiskFreeCode)：451399-一年期国债收益率；451400-十年期国债收益率；2398-一年定期存款利率（税后）

### TargetIndexCode (标的指数)

标的指数(TargetIndexCode)：1-上证综指；3145-沪深300

## SQL示例

```sql
-- 查询 基金詹森指数(全) 数据
SELECT *
FROM mf_fundjensonindexn
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
