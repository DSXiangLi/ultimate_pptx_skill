# CS_EnergyTecIndexADJ

**中文名**: 境内股票能量、量价与压力支撑技术指标(后复权)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_EnergyTecIndexADJ` |
| MySQL表名 | `cs_energytecindexadj` |
| 中文名 | 境内股票能量、量价与压力支撑技术指标(后复权) |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 45 |
| 版本 | 1 |

## 表描述

内容说明：收录境内股票上市之日起基于日、周、月、季、半年、年K线后复权行情衍生计算的能量、量价、压力支撑等大类技术指标
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
| 7 | `ARBR_AR` | ARBR人气指标AR | number(19,8) | ✓ | 72.08% |  |
| 8 | `ARBR_BR` | ARBR意愿指标BR | number(19,8) | ✓ | 76.02% |  |
| 9 | `CR` | CR能量指标 | number(19,8) | ✓ | 76.26% |  |
| 10 | `PSY_PSY` | PSY心理指标PSY | number(19,8) | ✓ | 82.73% |  |
| 11 | `PSY_PSYMA` | PSY心理指标PSYMA | number(19,8) | ✓ | 79.87% |  |
| 12 | `WAD_WAD` | WAD威廉聚散指标WAD | number(19,8) | ✓ | 96.66% |  |
| 13 | `WAD_MAWAD` | WAD威廉聚散指标MAWAD | number(19,8) | ✓ | 75.17% |  |
| 14 | `MFI` | MFI资金流向指标 | number(19,4) | ✓ | 81.38% |  |
| 15 | `OBV` | OBV能量潮OBV | number(19,4) | ✓ | 100.0% |  |
| 16 | `OBV_OBV` | OBV能量潮修正OBV | number(19,4) | ✓ | 71.54% |  |
| 17 | `SOBV` | SOBV能量潮 | number(19,4) | ✓ | 100.0% |  |
| 18 | `PVT` | PVT量价趋势指标 | number(19,4) | ✓ | 96.48% |  |
| 19 | `WVAD_WVAD` | WVAD威廉变异离散量WVAD | number(19,4) | ✓ | 74.1% |  |
| 20 | `WVAD_MAWVAD` | WVAD威廉变异离散量MAWVAD | number(19,4) | ✓ | 72.78% |  |
| 21 | `BBIBOLL_BBI` | BBIBOLL多空布林线BBI | number(19,8) | ✓ | 77.36% |  |
| 22 | `BBIBOLL_UPR` | BBIBOLL多空布林线UPR | number(19,8) | ✓ | 74.61% |  |
| 23 | `BBIBOLL_DWN` | BBIBOLL多空布林线DWN | number(19,8) | ✓ | 74.61% |  |
| 24 | `BOLL_MID` | BOLL布林线MID | number(19,8) | ✓ | 76.67% |  |
| 25 | `BOLL_UPPER` | BOLL布林线UPPER | number(19,8) | ✓ | 76.67% |  |
| 26 | `BOLL_LOWER` | BOLL布林线LOWER | number(19,8) | ✓ | 76.67% |  |
| 27 | `CDP_CDP` | CDP逆势操作CDP | number(19,8) | ✓ | 96.66% |  |
| 28 | `CDP_NL` | CDP逆势操作NL | number(19,8) | ✓ | 96.66% |  |
| 29 | `CDP_NH` | CDP逆势操作NH | number(19,8) | ✓ | 96.66% |  |
| 30 | `CDP_AL` | CDP逆势操作AL | number(19,8) | ✓ | 96.66% |  |
| 31 | `CDP_AH` | CDP逆势操作AH | number(19,8) | ✓ | 96.66% |  |
| 32 | `ENV_UPPER` | ENV指标UPPER | number(19,8) | ✓ | 82.06% |  |
| 33 | `ENV_LOWER` | ENV指标LOWER | number(19,8) | ✓ | 82.06% |  |
| 34 | `MIKE_WR` | MIKE麦克指标初级压力线 | number(19,8) | ✓ | 83.41% |  |
| 35 | `MIKE_MR` | MIKE麦克指标中级压力线 | number(19,8) | ✓ | 83.41% |  |
| 36 | `MIKE_SR` | MIKE麦克指标强力压力线 | number(19,8) | ✓ | 83.41% |  |
| 37 | `MIKE_WS` | MIKE麦克指标初级支撑线 | number(19,8) | ✓ | 83.41% |  |
| 38 | `MIKE_MS` | MIKE麦克指标中级支撑线 | number(19,8) | ✓ | 83.41% |  |
| 39 | `MIKE_SS` | MIKE麦克指标强力支撑线 | number(19,8) | ✓ | 83.41% |  |
| 40 | `SAR_AF` | SAR加速因子 | number(19,8) | ✓ | 92.11% |  |
| 41 | `SAR_TREND` | SAR趋势判断 | number(10) | ✓ | 92.11% | SAR趋势判断(SAR_TREND)，该字段固定以下常量：0-上升趋势，1-下降趋势 |
| 42 | `SAR` | SAR抛物转向指标 | number(19,8) | ✓ | 92.11% |  |
| 43 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 44 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 45 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### IndexCycle (指标周期)

指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

### SAR_TREND (SAR趋势判断)

SAR趋势判断(SAR_TREND)，该字段固定以下常量：0-上升趋势，1-下降趋势

## SQL示例

```sql
-- 查询 境内股票能量、量价与压力支撑技术指标(后复权) 数据
SELECT *
FROM cs_energytecindexadj
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
