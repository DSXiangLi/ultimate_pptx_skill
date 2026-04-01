# Index_GilDerivative

**中文名**: 聚源指数估值指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_GilDerivative` |
| MySQL表名 | `index_gilderivative` |
| 中文名 | 聚源指数估值指标 |
| 路径 | 聚源新版数据库 > 指数数据库 > 自编指数数据 > 衍生指标 |
| 更新频率 | 日更新 |
| 字段数量 | 36 |
| 版本 | 1 |

## 表描述

1.内容说明：收录聚源自编股票指数的衍生指标，包括指数总市值、静态市盈率、滚动市盈率、市净率、股息率、PEG等指标。
2.数据范围：指数基日-至今
3.信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `TotalMV` | 指数总市值(元) | number(19,4) | ✓ | 100.0% | TotalMV=∑成份股最新总股本*收盘价 |
| 5 | `NegotiableMV` | 指数流通市值(元) | number(19,4) | ✓ | 100.0% | NegotiableMV=∑成份股最新流通股本*收盘价 |
| 6 | `FreeFloatMV` | 指数自由流通市值(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `PE_LYR` | 静态市盈率 | number(19,4) | ✓ | 100.0% | PE_LYR=TotalMV/∑最新年报归母普通股东净利润 |
| 8 | `PE_TTM` | 滚动市盈率 | number(19,4) | ✓ | 100.0% | PE_TTM=TotalMV/∑归母普通股东净利润TTM |
| 9 | `PB_MRQ` | 市净率MRQ | number(19,4) | ✓ | 100.0% | PB_MRQ=TotalMV/∑最新报告期归母普通股东权益 |
| 10 | `PB_LF` | 市净率LF | number(19,4) | ✓ | 100.0% | PB_LF=TotalMV/∑最新归母普通股东权益 |
| 11 | `DividendRatioLYR` | 静态股息率(%) | number(19,4) | ✓ | 100.0% |  |
| 12 | `DividendRatioLYR2` | 静态股息率(报告期)(%) | number(19,4) | ✓ | 100.0% |  |
| 13 | `DividendRatio` | 滚动股息率(%) | number(19,4) | ✓ | 100.0% | DividendRatio=∑近12个月成份股现金分红/∑成份股所在市场市值*100 |
| 14 | `DividendRatio2` | 滚动股息率(报告期)(%) | number(19,4) | ✓ | 100.0% |  |
| 15 | `PCF_LYR` | 静态市现率 | number(19,4) | ✓ | 100.0% | PCF_LYR=TotalMV/∑最新年报经营现金流量净额 |
| 16 | `PCF_TTM` | 滚动市现率 | number(19,4) | ✓ | 100.0% | PCF_TTM=TotalMV/∑经营现金流量净额TTM |
| 17 | `PS_LYR` | 静态市销率 | number(19,4) | ✓ | 100.0% | PS_LYR=TotalMV/∑最新年报营业收入 |
| 18 | `PS_TTM` | 滚动市销率 | number(19,4) | ✓ | 100.0% | PS_TTM=TotalMV/∑营业收入TTM |
| 19 | `PE_LYR_ExNeg` | 静态市盈率剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 20 | `PE_TTM_ExNeg` | 滚动市盈率剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 21 | `PB_MRQ_ExNeg` | 市净率MRQ剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 22 | `PB_LF_ExNeg` | 市净率LF剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 23 | `PCF_LYR_ExNeg` | 静态市现率剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 24 | `PCF_TTM_ExNeg` | 滚动市现率剔除负值 | number(19,4) | ✓ | 100.0% |  |
| 25 | `PEG` | 指数PEG | number(19,4) | ✓ | 95.92% | PEG=PE_TTM/（近三年每股收益复合增长率*100)，当前年度指数成份的归母净利润TTM为负，并且当前年度每股归母... |
| 26 | `RiskPremium` | 风险溢价(%) | number(19,4) | ✓ | 83.3% | RiskPremium=(1/PE_TTM-十年期国债收益率)*100 |
| 27 | `RiskPremium_DivLYR` | 风险溢价(静态股息率)(%) | number(19,4) | ✓ | 81.84% | RiskPremium_DivLYR=(DividendRatioLYR/100-十年期国债收益率)*100 |
| 28 | `RiskPremium_Div` | 风险溢价(滚动股息率)(%) | number(19,4) | ✓ | 83.13% | RiskPremium_Div=(DividendRatio/100-十年期国债收益率)*100 |
| 29 | `RiskPremium1` | 风险溢价(比值) | number(19,4) | ✓ | 83.3% | RiskPremium1=(1/PE_TTM)/十年期国债收益率 |
| 30 | `RiskPremium_DivLYR1` | 风险溢价(静态股息率)(比值) | number(19,4) | ✓ | 81.84% | RiskPremium_DivLYR1=(DividendRatioLYR/100)/十年期国债收益率 |
| 31 | `RiskPremium_Div1` | 风险溢价(滚动股息率)(比值) | number(19,4) | ✓ | 83.13% | RiskPremium_Div1=(DividendRatio/100)/十年期国债收益率 |
| 32 | `LossNC` | 指数亏损成分股数量 | number(10) | ✓ | 100.0% |  |
| 33 | `IndexNC` | 指数成分股数量 | number(10) | ✓ | 100.0% |  |
| 34 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 35 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 36 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### TotalMV (指数总市值(元))

TotalMV=∑成份股最新总股本*收盘价

### NegotiableMV (指数流通市值(元))

NegotiableMV=∑成份股最新流通股本*收盘价

### PE_LYR (静态市盈率)

PE_LYR=TotalMV/∑最新年报归母普通股东净利润

### PE_TTM (滚动市盈率)

PE_TTM=TotalMV/∑归母普通股东净利润TTM

### PB_MRQ (市净率MRQ)

PB_MRQ=TotalMV/∑最新报告期归母普通股东权益

### PB_LF (市净率LF)

PB_LF=TotalMV/∑最新归母普通股东权益

### DividendRatio (滚动股息率(%))

DividendRatio=∑近12个月成份股现金分红/∑成份股所在市场市值*100

### PCF_LYR (静态市现率)

PCF_LYR=TotalMV/∑最新年报经营现金流量净额

### PCF_TTM (滚动市现率)

PCF_TTM=TotalMV/∑经营现金流量净额TTM

## SQL示例

```sql
-- 查询 聚源指数估值指标 数据
SELECT *
FROM index_gilderivative
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
