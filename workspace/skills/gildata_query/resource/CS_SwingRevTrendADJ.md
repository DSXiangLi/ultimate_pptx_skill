# CS_SwingRevTrendADJ

**中文名**: 境内股票摆动与反趋向技术指标(后复权)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_SwingRevTrendADJ` |
| MySQL表名 | `cs_swingrevtrendadj` |
| 中文名 | 境内股票摆动与反趋向技术指标(后复权) |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 49 |
| 版本 | 1 |

## 表描述

内容说明：收录境内股票上市之日起基于日、周、月、季、半年、年K线后复权行情衍生计算的反趋向、摆动、波动、超买超卖等大类技术指标
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
| 7 | `B612` | B612 | number(19,8) | ✓ | 83.41% |  |
| 8 | `B36` | B36 | number(19,8) | ✓ | 89.07% |  |
| 9 | `BIAS` | BIAS乖离率 | number(19,8) | ✓ | 83.41% |  |
| 10 | `CCI` | CCI顺势指标 | number(19,8) | ✓ | 81.82% |  |
| 11 | `DBCD_DBCD` | DBCD异同离差乖离率DBCD | number(19,8) | ✓ | 78.53% |  |
| 12 | `DBCD_MM` | DBCD异同离差乖离率MM | number(19,8) | ✓ | 77.01% |  |
| 13 | `DPO_DPO` | DPO区间震荡线DPO | number(19,8) | ✓ | 75.17% |  |
| 14 | `DPO_MADPO` | DPO区间震荡线MADPO | number(19,8) | ✓ | 73.82% |  |
| 15 | `KDJ_K` | KDJ随机指标K | number(19,8) | ✓ | 100.0% |  |
| 16 | `KDJ_D` | KDJ随机指标D | number(19,8) | ✓ | 99.97% |  |
| 17 | `KDJ_J` | KDJ随机指标J | number(19,8) | ✓ | 99.97% |  |
| 18 | `LWR_LWR1` | LWR威廉指标LWR1 | number(19,8) | ✓ | 100.0% |  |
| 19 | `LWR_LWR2` | LWR威廉指标LWR2 | number(19,8) | ✓ | 99.97% |  |
| 20 | `ROC_ROC` | ROC变动速率ROC | number(19,8) | ✓ | 82.73% |  |
| 21 | `ROC_ROCMA` | ROC变动速率ROCMA | number(19,8) | ✓ | 79.87% |  |
| 22 | `RSI` | RSI相对强弱指标 | number(19,8) | ✓ | 93.44% |  |
| 23 | `SI` | SI摆动指标 | number(19,8) | ✓ | 90.76% |  |
| 24 | `SRDM_SRDM` | SRDM动向速度比率SRDM | number(19,8) | ✓ | 84.15% |  |
| 25 | `SRDM_ASRDM` | SRDM动向速度比率ASRDM | number(19,8) | ✓ | 84.15% |  |
| 26 | `WR` | WR威廉指标 | number(19,8) | ✓ | 81.58% |  |
| 27 | `MI_A` | MI动量指标A | number(19,8) | ✓ | 82.73% |  |
| 28 | `MI_MI` | MI动量指标MI | number(19,8) | ✓ | 82.73% |  |
| 29 | `MICD_DIF` | MICD异同离差动力指数DIF | number(19,8) | ✓ | 78.12% |  |
| 30 | `MICD_MICD` | MICD异同离差动力指数MICD | number(19,8) | ✓ | 78.12% |  |
| 31 | `RC` | RC变化率指数 | number(19,8) | ✓ | 70.7% |  |
| 32 | `RCCD_DIF` | RCCD异同离差变化率指数DIF | number(19,8) | ✓ | 65.53% |  |
| 33 | `RCCD_RCCD` | RCCD异同离差变化率指数RCCD | number(19,8) | ✓ | 65.53% |  |
| 34 | `SRMI` | MI修正指标 | number(19,8) | ✓ | 84.95% |  |
| 35 | `ATR_TR` | ATR真实波幅TR | number(19,8) | ✓ | 96.66% |  |
| 36 | `ATR_ATR` | ATR真实波幅ATR | number(19,8) | ✓ | 81.43% |  |
| 37 | `MASS` | MASS梅丝线 | number(19,8) | ✓ | 75.24% |  |
| 38 | `STD` | STD标准差 | number(19,8) | ✓ | 76.08% |  |
| 39 | `VHF` | VHF纵横指标 | number(19,8) | ✓ | 75.69% |  |
| 40 | `CVLT` | CVLT佳庆离散指标 | number(19,8) | ✓ | 78.53% |  |
| 41 | `ADTM_ADTM` | ADTM动态买卖气指标ADTM | number(19,8) | ✓ | 76.98% |  |
| 42 | `ADTM_ADTMMA` | ADTM动态买卖气指标ADTMMA | number(19,8) | ✓ | 74.8% |  |
| 43 | `SKDJ_K` | SKDJ慢速随机指标K | number(19,8) | ✓ | 85.8% |  |
| 44 | `SKDJ_D` | SKDJ慢速随机指标D | number(19,8) | ✓ | 84.15% |  |
| 45 | `DKX_DKX` | DKX多空线DKX | number(19,8) | ✓ | 78.53% |  |
| 46 | `DKX_DKXMA` | DKX多空线DKXMA | number(19,8) | ✓ | 75.46% |  |
| 47 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 48 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 49 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### IndexCycle (指标周期)

指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

## SQL示例

```sql
-- 查询 境内股票摆动与反趋向技术指标(后复权) 数据
SELECT *
FROM cs_swingrevtrendadj
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
