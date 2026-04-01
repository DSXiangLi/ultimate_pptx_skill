# Bond_Deriv

**中文名**: 债券基础衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_Deriv` |
| MySQL表名 | `bond_deriv` |
| 中文名 | 债券基础衍生指标 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 65 |
| 版本 | 1.01 |

## 表描述

1.收录（除ABS、永续债）外所有类型债券基于债券行情（银行间市场、沪深交易所竞价系统、上交所固定收益平台、深交所综合收益平台）、现金流等要素，计算的基础衍生指标；其中，违约债计算至实际违约前一天。
2.数据范围：1990-12-19至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令(LB = 201 AND DM... |
| 5 | `AccruedDays` | 计息天数 | number(10) | ✓ | 99.99% |  |
| 6 | `AccruedInterest` | 每百元应计利息(元) | number(18,12) | ✓ | 99.99% |  |
| 7 | `YearsToMaturity` | 待偿期 | number(19,4) | ✓ | 100.0% |  |
| 8 | `OpenDirtyPrice` | 全价开盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `YTM_OP` | 开盘价到期收益率(%) | number(18,10) | ✓ | 99.99% |  |
| 10 | `Duration_OP` | 开盘价麦氏久期 | number(18,10) | ✓ | 100.0% |  |
| 11 | `ModifiedDuration_OP` | 开盘价修正久期 | number(18,10) | ✓ | 100.0% |  |
| 12 | `Convexity_OP` | 开盘价凸性 | number(18,10) | ✓ | 100.0% |  |
| 13 | `IRDuration_OP` | 开盘价利率久期 | number(18,10) | ✓ | 0.55% |  |
| 14 | `SpreadDuration_OP` | 开盘价利差久期 | number(18,10) | ✓ | 0.55% |  |
| 15 | `IRConvexity_OP` | 开盘价利率凸性 | number(18,10) | ✓ | 0.55% |  |
| 16 | `SpreadConvexity_OP` | 开盘价利差凸性 | number(18,10) | ✓ | 0.55% |  |
| 17 | `PointSpreadYield_OP` | 开盘价点差收益率(%) | number(18,10) | ✓ | 0.55% |  |
| 18 | `BasisPointValue_OP` | 开盘价基点价值 | number(18,10) | ✓ | 100.0% |  |
| 19 | `HighDirtyPrice` | 全价最高价(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `YTM_HI` | 最高价到期收益率(%) | number(18,10) | ✓ | 99.99% |  |
| 21 | `Duration_HI` | 最高价麦氏久期 | number(18,10) | ✓ | 100.0% |  |
| 22 | `ModifiedDuration_HI` | 最高价修正久期 | number(18,10) | ✓ | 100.0% |  |
| 23 | `Convexity_HI` | 最高价凸性 | number(18,10) | ✓ | 100.0% |  |
| 24 | `IRDuration_HI` | 最高价利率久期 | number(18,10) | ✓ | 0.55% |  |
| 25 | `SpreadDuration_HI` | 最高价利差久期 | number(18,10) | ✓ | 0.55% |  |
| 26 | `IRConvexity_HI` | 最高价利率凸性 | number(18,10) | ✓ | 0.55% |  |
| 27 | `SpreadConvexity_HI` | 最高价利差凸性 | number(18,10) | ✓ | 0.55% |  |
| 28 | `PointSpreadYield_HI` | 最高价点差收益率(%) | number(18,10) | ✓ | 0.55% |  |
| 29 | `BasisPointValue_HI` | 最高价基点价值 | number(18,10) | ✓ | 100.0% |  |
| 30 | `LowDirtyPrice` | 全价最低价(元) | number(19,4) | ✓ | 100.0% |  |
| 31 | `YTM_LO` | 最低价到期收益率(%) | number(18,10) | ✓ | 99.99% |  |
| 32 | `Duration_LO` | 最低价麦氏久期 | number(18,10) | ✓ | 100.0% |  |
| 33 | `ModifiedDuration_LO` | 最低价修正久期 | number(18,10) | ✓ | 100.0% |  |
| 34 | `Convexity_LO` | 最低价凸性 | number(18,10) | ✓ | 100.0% |  |
| 35 | `IRDuration_LO` | 最低价利率久期 | number(18,10) | ✓ | 0.55% |  |
| 36 | `SpreadDuration_LO` | 最低价利差久期 | number(18,10) | ✓ | 0.55% |  |
| 37 | `IRConvexity_LO` | 最低价利率凸性 | number(18,10) | ✓ | 0.55% |  |
| 38 | `SpreadConvexity_LO` | 最低价利差凸性 | number(18,10) | ✓ | 0.55% |  |
| 39 | `PointSpreadYield_LO` | 最低价点差收益率(%) | number(18,10) | ✓ | 0.55% |  |
| 40 | `BasisPointValue_LO` | 最低价基点价值 | number(18,10) | ✓ | 100.0% |  |
| 41 | `CloseDirtyPrice` | 全价收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 42 | `YTM_CL` | 收盘价到期收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 43 | `Duration_CL` | 收盘价麦氏久期 | number(18,10) | ✓ | 100.0% |  |
| 44 | `ModifiedDuration_CL` | 收盘价修正久期 | number(18,10) | ✓ | 100.0% |  |
| 45 | `Convexity_CL` | 收盘价凸性 | number(18,10) | ✓ | 100.0% |  |
| 46 | `IRDuration_CL` | 收盘价利率久期 | number(18,10) | ✓ | 0.55% |  |
| 47 | `SpreadDuration_CL` | 收盘价利差久期 | number(18,10) | ✓ | 0.55% |  |
| 48 | `IRConvexity_CL` | 收盘价利率凸性 | number(18,10) | ✓ | 0.55% |  |
| 49 | `SpreadConvexity_CL` | 收盘价利差凸性 | number(18,10) | ✓ | 0.55% |  |
| 50 | `PointSpreadYield_CL` | 收盘价点差收益率(%) | number(18,10) | ✓ | 0.55% |  |
| 51 | `BasisPointValue_CL` | 收盘价基点价值 | number(18,10) | ✓ | 100.0% |  |
| 52 | `WeightedDirtyPrice` | 全价加权价(元) | number(19,4) | ✓ | 81.33% |  |
| 53 | `YTM_WAP` | 加权价到期收益率(%) | number(18,10) | ✓ | 72.41% |  |
| 54 | `Duration_WAP` | 加权价麦氏久期 | number(18,10) | ✓ | 72.41% |  |
| 55 | `ModifiedDuration_WAP` | 加权价修正久期 | number(18,10) | ✓ | 72.41% |  |
| 56 | `Convexity_WAP` | 加权价凸性 | number(18,10) | ✓ | 72.41% |  |
| 57 | `IRDuration_WAP` | 加权价利率久期 | number(18,10) | ✓ | 0.51% |  |
| 58 | `SpreadDuration_WAP` | 加权价利差久期 | number(18,10) | ✓ | 0.51% |  |
| 59 | `IRConvexity_WAP` | 加权价利率凸性 | number(18,10) | ✓ | 0.51% |  |
| 60 | `SpreadConvexity_WAP` | 加权价利差凸性 | number(18,10) | ✓ | 0.51% |  |
| 61 | `PointSpreadYield_WAP` | 加权价点差收益率(%) | number(18,10) | ✓ | 0.51% |  |
| 62 | `BasisPointValue_WAP` | 加权价基点价值 | number(18,10) | ✓ | 72.41% |  |
| 63 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 64 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 65 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令(LB = 201 AND DM IN(81,83,89,90)) OR (LB = 1006 AND DM IN(12,18,21))，得到证券市场的具体描述：12-上交所固定收益平台，18-深交所综合收益平台，21-上交所大宗交易，81-三板市场，83-上海证券交易所，89-银行间债券市场，90-深圳证券交易所。

## SQL示例

```sql
-- 查询 债券基础衍生指标 数据
SELECT *
FROM bond_deriv
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
