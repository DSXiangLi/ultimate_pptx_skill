# FP_IFSettlementRate

**中文名**: 保险理财产品结算利率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFSettlementRate` |
| MySQL表名 | `fp_ifsettlementrate` |
| 中文名 | 保险理财产品结算利率 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

收录保险产品的利率信息，包括结算日期、结算年利率、结算月利率、结算日利率、最低保证利率等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `FinProCode` | 保险产品编码 | varchar2(12) | ✗ | 100.0% | 保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `BeginDate` | 结算起始日 | date | ✗ | 100.0% |  |
| 5 | `EndDate` | 结算截止日 | date | ✗ | 100.0% |  |
| 6 | `BaseAnnualRate` | 保底结算年利率 | number(19,8) | ✓ | 63.91% |  |
| 7 | `DayRate` | 结算日利率 | number(19,8) | ✓ | 98.24% |  |
| 8 | `MonthlyRate` | 结算月利率 | number(19,8) | ✓ | 2.03% |  |
| 9 | `AnnualRate` | 结算年利率 | number(19,8) | ✓ | 99.97% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (保险产品编码)

保险产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

## SQL示例

```sql
-- 查询 保险理财产品结算利率 数据
SELECT *
FROM fp_ifsettlementrate
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
