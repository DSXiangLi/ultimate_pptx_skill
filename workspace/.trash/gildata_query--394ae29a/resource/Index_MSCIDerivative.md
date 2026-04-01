# Index_MSCIDerivative

**中文名**: MSCI指数衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_MSCIDerivative` |
| MySQL表名 | `index_msciderivative` |
| 中文名 | MSCI指数衍生指标 |
| 路径 | 聚源新版数据库 > 产品代理 > MSCI代理数据库 |
| 更新频率 | 月更新 |
| 字段数量 | 28 |
| 版本 | 1 |

## 表描述

内容说明：收录MSCI指数估值和财务分析指标，包括市盈率、市净率、股息率、每股收益、每股收益增长率等数据。
数据范围：2003年1月至今
信息来源：MSCI

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `IndexNC` | 指数成份股数量 | number(10) | ✓ | 100.0% |  |
| 5 | `PE` | 市盈率 | number(18,4) | ✓ | 100.0% |  |
| 6 | `PE_TTM` | 指数滚动市盈率 | number(18,4) | ✓ | 93.27% |  |
| 7 | `ForwardPE` | 指数动态市盈率 | number(18,4) | ✓ | 93.5% |  |
| 8 | `PB` | 市净率 | number(18,4) | ✓ | 100.0% |  |
| 9 | `PCF` | 市现率 | number(18,4) | ✓ | 99.92% |  |
| 10 | `DividendRatio` | 股息率 | number(18,4) | ✓ | 99.97% |  |
| 11 | `EPSTTM` | 每股收益_TTM | number(18,4) | ✓ | 98.06% |  |
| 12 | `ForwardEPS` | 动态每股收益 | number(18,4) | ✓ | 91.76% |  |
| 13 | `ROE` | 净资产收益率 | number(18,4) | ✓ | 99.88% |  |
| 14 | `InternalGrowth` | 内含增长率 | number(18,4) | ✓ | 99.85% |  |
| 15 | `EPSTTMYOY` | 每股收益_TTM同比增长率(%) | number(18,4) | ✓ | 94.76% |  |
| 16 | `ForwardEPSYOY` | 动态每股收益同比增长率(%) | number(18,4) | ✓ | 88.83% |  |
| 17 | `EPSGrowthFiveYear` | 每股收益近5年增长率(%) | number(18,4) | ✓ | 91.75% |  |
| 18 | `EPSGrowthThreeYear` | 每股收益近3年增长率(%) | number(18,4) | ✓ | 90.41% |  |
| 19 | `FEPSLTGrowth` | 预测每股收益长期增长率(%) | number(18,4) | ✓ | 90.3% |  |
| 20 | `FEPSSTGrowth` | 预测每股收益短期增长率(%) | number(18,4) | ✓ | 91.75% |  |
| 21 | `SPSGrowthFiveYear` | 每股营收近5年增长率(%) | number(18,4) | ✓ | 91.72% |  |
| 22 | `SPSGrowthThreeYear` | 每股营收近3年增长率(%) | number(18,4) | ✓ | 90.47% |  |
| 23 | `DPSToEPS` | 每股股息/每股收益(%) | number(18,4) | ✓ | 91.16% |  |
| 24 | `AnnualizedDPSOneYear` | 每股股息近1年年化增长率 | number(18,4) | ✓ | 90.93% |  |
| 25 | `AnnualizedDPSFiveYear` | 每股股息近5年年化增长率 | number(18,4) | ✓ | 90.87% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部代码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

## SQL示例

```sql
-- 查询 MSCI指数衍生指标 数据
SELECT *
FROM index_msciderivative
WHERE TradingDay >= '2024-01-01'
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
