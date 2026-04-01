# CS_StockStyleCoef

**中文名**: 境内股票风格系数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockStyleCoef` |
| MySQL表名 | `cs_stockstylecoef` |
| 中文名 | 境内股票风格系数 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 年更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

内容说明：收录境内A股股票风格系数，其中风格值与日均市值分别用于判断股票风格属性或规模属性(需结合门限值使用)，其余指标为计算风格值的中间指标
数据范围：2000-05至今
信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `AvgMarketValue` | 日均市值 | number(19,6) | ✓ | 100.0% |  |
| 6 | `EarningPriceRatio` | 每股收益价格比 | number(19,6) | ✓ | 100.0% |  |
| 7 | `NetAssetPriceRatio` | 每股净资产价格比 | number(19,6) | ✓ | 100.0% |  |
| 8 | `NetCashFlowPriceRatio` | 每股净现金流价格比 | number(19,6) | ✓ | 100.0% |  |
| 9 | `DividendRatio` | 股息率 | number(19,6) | ✓ | 100.0% |  |
| 10 | `NetProfitGrowRate` | 净利润复合增长率 | number(19,6) | ✓ | 99.97% |  |
| 11 | `OpeRevGrowRate` | 营业收入复合增长率 | number(19,6) | ✓ | 99.99% |  |
| 12 | `SustainableGrowRate` | 可持续增长率 | number(19,6) | ✓ | 100.0% |  |
| 13 | `EarningPriceRatio_Z` | 每股收益价格比Z值 | number(19,6) | ✓ | 99.82% |  |
| 14 | `NetAssetPriceRatio_Z` | 每股净资产价格比Z值 | number(19,6) | ✓ | 99.82% |  |
| 15 | `NCashFlowPriceRatio_Z` | 每股净现金流价格比Z值 | number(19,6) | ✓ | 99.82% |  |
| 16 | `DividendRatio_Z` | 股息率Z值 | number(19,6) | ✓ | 99.82% |  |
| 17 | `NetProfitGrowRate_Z` | 净利润复合增长率Z值 | number(19,6) | ✓ | 99.81% |  |
| 18 | `OpeRevGrowRate_Z` | 营业收入复合增长率Z值 | number(19,6) | ✓ | 99.82% |  |
| 19 | `SustainableGrowRate_Z` | 可持续增长率Z值 | number(19,6) | ✓ | 99.82% |  |
| 20 | `Growth_Z` | 成长因子Z分值 | number(19,6) | ✓ | 99.81% |  |
| 21 | `Value_Z` | 价值因子Z分值 | number(19,6) | ✓ | 99.82% |  |
| 22 | `StyleValue` | 风格值 | number(19,6) | ✓ | 99.81% |  |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

## SQL示例

```sql
-- 查询 境内股票风格系数 数据
SELECT *
FROM cs_stockstylecoef
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
