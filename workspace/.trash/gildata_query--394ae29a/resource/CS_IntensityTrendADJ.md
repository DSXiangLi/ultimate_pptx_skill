# CS_IntensityTrendADJ

**中文名**: 境内股票强弱与趋向技术指标(后复权)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_IntensityTrendADJ` |
| MySQL表名 | `cs_intensitytrendadj` |
| 中文名 | 境内股票强弱与趋向技术指标(后复权) |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 42 |
| 版本 | 1 |

## 表描述

内容说明：收录境内股票上市之日起基于日、周、月、季、半年、年K线后复权行情衍生计算的趋向、强弱等大类技术指标
数据范围：股票上市起-至今
信息来源：基于沪深京交易所及股转系统行情数据衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `GilCode` | 聚源代码 | varchar2(12) | ✗ | 100.0% |  |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年 |
| 6 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN... |
| 7 | `MA5` | 收盘价简单移动平均(5日) | number(19,8) | ✓ | 90.5% |  |
| 8 | `MA10` | 收盘价简单移动平均(10日) | number(19,8) | ✓ | 84.95% |  |
| 9 | `MA20` | 收盘价简单移动平均(20日) | number(19,8) | ✓ | 78.97% |  |
| 10 | `MA30` | 收盘价简单移动平均(30日) | number(19,8) | ✓ | 75.46% |  |
| 11 | `MA60` | 收盘价简单移动平均(60日) | number(19,8) | ✓ | 69.2% |  |
| 12 | `MA120` | 收盘价简单移动平均(120日) | number(19,8) | ✓ | 62.51% |  |
| 13 | `MA250` | 收盘价简单移动平均(250日) | number(19,8) | ✓ | 54.15% |  |
| 14 | `BBI` | BBI多空指数 | number(19,8) | ✓ | 77.36% |  |
| 15 | `DMA_DMA` | DMA平均线差指标DMA | number(19,8) | ✓ | 70.88% |  |
| 16 | `DMA_AMA` | DMA平均线差指标AMA | number(19,8) | ✓ | 69.35% |  |
| 17 | `DMI_PDI` | DMI趋向指标PDI | number(19,8) | ✓ | 81.09% |  |
| 18 | `DMI_MDI` | DMI趋向指标MDI | number(19,8) | ✓ | 81.09% |  |
| 19 | `DMI_ADX` | DMI趋向指标ADX | number(19,8) | ✓ | 78.51% |  |
| 20 | `DMI_ADXR` | DMI趋向指标ADXR | number(19,8) | ✓ | 76.16% |  |
| 21 | `EXPMA12` | EXPMA指数平均数(12日) | number(19,8) | ✓ | 100.0% |  |
| 22 | `EXPMA26` | EXPMA指数平均数(26日) | number(19,8) | ✓ | 100.0% |  |
| 23 | `MACD_DIFF` | MACD指数平滑异同平均线DIFF | number(19,8) | ✓ | 100.0% |  |
| 24 | `MACD_DEA` | MACD指数平滑异同平均线DEA | number(19,8) | ✓ | 100.0% |  |
| 25 | `MACD_MACD` | MACD指数平滑异同平均线MACD | number(19,8) | ✓ | 100.0% |  |
| 26 | `MTM_MTM` | MTM动力指标MTM | number(19,8) | ✓ | 87.84% |  |
| 27 | `MTM_MTMMA` | MTM动力指标MTMMA | number(19,8) | ✓ | 83.41% |  |
| 28 | `PRICEOSC` | PRICEOSC价格震荡指标 | number(19,8) | ✓ | 76.67% |  |
| 29 | `TRIX_TR` | TRIX三重指数平滑平均线TR | number(19,8) | ✓ | 100.0% |  |
| 30 | `TRIX_TRIX` | TRIX三重指数平滑平均线TRIX | number(19,8) | ✓ | 96.66% |  |
| 31 | `TRIX_TRMA` | TRIX三重指数平滑平均线TRMA | number(19,8) | ✓ | 78.53% |  |
| 32 | `DDI_DDI` | DDI方向标准离差指数DDI | number(19,8) | ✓ | 81.58% |  |
| 33 | `DDI_ADDI` | DDI方向标准离差指数ADDI | number(19,8) | ✓ | 81.58% |  |
| 34 | `DDI_AD` | DDI方向标准离差指数AD | number(19,8) | ✓ | 79.4% |  |
| 35 | `Market_CSI300` | 大盘同步指标(沪深300) | number(19,8) | ✓ | 68.91% |  |
| 36 | `Strength_CSI300` | 阶段强势指标(沪深300) | number(19,8) | ✓ | 62.51% |  |
| 37 | `Weakness_CSI300` | 阶段弱势指标(沪深300) | number(19,8) | ✓ | 62.17% |  |
| 38 | `Bottoming_B` | 筑底指标B | number(19,8) | ✓ | 61.51% |  |
| 39 | `Bottoming_D` | 筑底指标D | number(19,8) | ✓ | 60.36% |  |
| 40 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 41 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 42 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### IndexCycle (指标周期)

指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

## SQL示例

```sql
-- 查询 境内股票强弱与趋向技术指标(后复权) 数据
SELECT *
FROM cs_intensitytrendadj
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
