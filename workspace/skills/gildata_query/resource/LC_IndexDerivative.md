# LC_IndexDerivative

**中文名**: 指数估值指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndexDerivative` |
| MySQL表名 | `lc_indexderivative` |
| 中文名 | 指数估值指标 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 36 |
| 版本 | 1.07 |

## 表描述

1.内容说明：本表记录A股、港股主要股票指数的衍生指标，包括指数总市值、静态市盈率、动态市盈率、市净率、股息率等指标。
2.数据范围：2000-01-01至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：当位数小于7位时，与“证券主表（SecuMain）”中的“证券内部编码（InnerC... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `TotalMV` | 指数总市值(元) | number(19,4) | ✓ | 99.99% | TotalMV=∑成份股最新总股本*收盘价 |
| 5 | `NegotiableMV` | 指数流通市值(元) | number(19,4) | ✓ | 99.74% | NegotiableMV=∑成份股最新流通股本*收盘价 |
| 6 | `PE_TTM` | 滚动市盈率 | number(19,4) | ✓ | 99.87% | PE_TTM=TotalMV/∑归母普通股东净利润TTM |
| 7 | `PE_LYR` | 静态市盈率(LYR) | number(19,4) | ✓ | 95.28% | PE_LYR=TotalMV/∑最新年报归母普通股东净利润 |
| 8 | `PB_LF` | 市净率(LF) | number(19,4) | ✓ | 95.28% | PB_LF=TotalMV/∑最新归母普通股东权益 |
| 9 | `PB_MRQ` | 市净率(MRQ) | number(19,4) | ✓ | 99.65% | PB_MRQ=TotalMV/∑最新报告期归母普通股东权益 |
| 10 | `PCF_LYR` | 静态市现率(LYR) | number(19,4) | ✓ | 95.28% | PCF_LYR=TotalMV/∑最新年报经营现金流量净额 |
| 11 | `PCF_TTM` | 滚动市现率 | number(19,4) | ✓ | 95.28% | PCF_TTM=TotalMV/∑经营现金流量净额TTM |
| 12 | `PS_LYR` | 静态市销率(LYR) | number(19,4) | ✓ | 95.28% | PS_LYR=TotalMV/∑最新年报营业收入 |
| 13 | `PS_TTM` | 滚动市销率 | number(19,4) | ✓ | 95.28% | PS_TTM=TotalMV/∑营业收入TTM |
| 14 | `DividendRatio` | 滚动股息率(%) | number(19,4) | ✓ | 95.28% | DividendRatio=∑近12个月成份股现金分红/∑成份股所在市场市值*100 |
| 15 | `PEG` | 历史PEG | number(19,4) | ✓ | 90.71% | PEG=PE_TTM/（近三年每股收益复合增长率*100)，当前年度指数成份的归母净利润TTM为负，并且当前年度每股归母... |
| 16 | `PE_TTM_ExNeg` | 滚动市盈率剔除负值 | number(19,4) | ✓ | 99.62% |  |
| 17 | `PE_LYR_ExNeg` | 静态市盈率剔除负值 | number(19,4) | ✓ | 95.11% |  |
| 18 | `PB_LF_ExNeg` | 市净率(LF)剔除负值 | number(19,4) | ✓ | 95.27% |  |
| 19 | `PB_MRQ_ExNeg` | 市净率(MRQ)剔除负值 | number(19,4) | ✓ | 99.64% |  |
| 20 | `PCF_LYR_ExNeg` | 静态市现率(LYR)剔除负值 | number(19,4) | ✓ | 94.83% |  |
| 21 | `PCF_TTM_ExNeg` | 滚动市现率剔除负值 | number(19,4) | ✓ | 94.8% |  |
| 22 | `LossNC` | 指数亏损成份股数量 | number(10) | ✓ | 100.0% | LossNC=归母普通股东净利润TTM为负的成份证券数量 |
| 23 | `IndexNC` | 指数成份股数量 | number(10) | ✓ | 100.0% |  |
| 24 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 25 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 26 | `JSID` | JSID | number(19) | ✗ |  |  |
| 27 | `FreeFloatMV` | 指数自由流通市值(元) | number(19,4) | ✓ | 84.14% |  |
| 28 | `DividendRatioLYR` | 静态股息率(%) | number(19,4) | ✓ | 94.83% |  |
| 29 | `DividendRatioLYR2` | 静态股息率(报告期)(%) | number(19,4) | ✓ | 94.83% |  |
| 30 | `DividendRatio2` | 滚动股息率(报告期)(%) | number(19,4) | ✓ | 94.83% |  |
| 31 | `RiskPremium` | 风险溢价(%) | number(19,4) | ✓ | 95.51% |  |
| 32 | `RiskPremium_DivLYR` | 风险溢价(静态股息率)(%) | number(19,4) | ✓ | 90.53% |  |
| 33 | `RiskPremium_Div` | 风险溢价(滚动股息率)(%) | number(19,4) | ✓ | 90.53% |  |
| 34 | `RiskPremium1` | 风险溢价(比值) | number(19,4) | ✓ | 95.51% |  |
| 35 | `RiskPremium_DivLYR1` | 风险溢价(静态股息率)(比值) | number(19,4) | ✓ | 90.53% |  |
| 36 | `RiskPremium_Div1` | 风险溢价(滚动股息率)(比值) | number(19,4) | ✓ | 90.53% |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：当位数小于7位时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称；反之与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### TotalMV (指数总市值(元))

TotalMV=∑成份股最新总股本*收盘价

### NegotiableMV (指数流通市值(元))

NegotiableMV=∑成份股最新流通股本*收盘价

### PE_TTM (滚动市盈率)

PE_TTM=TotalMV/∑归母普通股东净利润TTM

### PE_LYR (静态市盈率(LYR))

PE_LYR=TotalMV/∑最新年报归母普通股东净利润

### PB_LF (市净率(LF))

PB_LF=TotalMV/∑最新归母普通股东权益

### PB_MRQ (市净率(MRQ))

PB_MRQ=TotalMV/∑最新报告期归母普通股东权益

### PCF_LYR (静态市现率(LYR))

PCF_LYR=TotalMV/∑最新年报经营现金流量净额

### PCF_TTM (滚动市现率)

PCF_TTM=TotalMV/∑经营现金流量净额TTM

### PS_LYR (静态市销率(LYR))

PS_LYR=TotalMV/∑最新年报营业收入

## SQL示例

```sql
-- 查询 指数估值指标 数据
SELECT *
FROM lc_indexderivative
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
