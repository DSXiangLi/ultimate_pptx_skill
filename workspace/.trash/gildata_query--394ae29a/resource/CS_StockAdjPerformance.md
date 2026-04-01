# CS_StockAdjPerformance

**中文名**: 境内股票复权行情表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockAdjPerformance` |
| MySQL表名 | `cs_stockadjperformance` |
| 中文名 | 境内股票复权行情表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

内容说明：收录精确复权因子、精确复权常数及比例复权因子计算的境内股票前复权及后复权行情；
数据范围：证券上市之日起至今；
信息来源：沪深京交易所行情数据，新三板行情文件，聚源计算。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `GilCode` | 聚源代码 | varchar2(12) | ✗ | 100.0% |  |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `ExDiviDate` | 除权除息日 | date | ✓ | 71.06% |  |
| 6 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN... |
| 7 | `AdjPrevClose` | 复权昨收盘(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `AdjOpenPrice` | 复权开盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `AdjHighPrice` | 复权最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `AdjLowPrice` | 复权最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `AdjClosePrice` | 复权收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `AdjustingMethod` | 复权方式 | number(10) | ✗ | 100.0% | 复权方式(AdjustingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2544，得到复... |
| 13 | `AdjustingStandard` | 复权标准 | number(10) | ✗ | 100.0% | 复权标准(AdjustingStandard)与(CT_SystemConst)表中的DM字段关联，令LB=2545，得... |
| 14 | `AdjustingFactor` | 复权因子 | number(19,4) | ✓ | 100.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

### AdjustingMethod (复权方式)

复权方式(AdjustingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2544，得到复权方式的具体描述：1-前复权，2-后复权。

### AdjustingStandard (复权标准)

复权标准(AdjustingStandard)与(CT_SystemConst)表中的DM字段关联，令LB=2545，得到复权标准的具体描述：1-精确复权，2-比例复权。

## SQL示例

```sql
-- 查询 境内股票复权行情表 数据
SELECT *
FROM cs_stockadjperformance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
