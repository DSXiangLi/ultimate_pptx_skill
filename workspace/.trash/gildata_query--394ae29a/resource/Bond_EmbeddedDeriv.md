# Bond_EmbeddedDeriv

**中文名**: 含权债券衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_EmbeddedDeriv` |
| MySQL表名 | `bond_embeddedderiv` |
| 中文名 | 含权债券衍生指标 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 23 |
| 版本 | 1 |

## 表描述

1.收录（除ABS）外所有含回售、赎回等约定权利债券基于债券行情（银行间市场、沪深交易所竞价系统、上交所固定收益平台、深交所综合收益平台）、行权条件现金流等要素，计算的衍生指标；其中，违约债计算至实际违约前一天。
2.数据范围：1990-12-19至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 5 | `AccruedDays` | 计息天数 | number(10) | ✓ | 100.0% |  |
| 6 | `AccruedInterest` | 每百元应计利息(元) | number(18,12) | ✓ | 100.0% |  |
| 7 | `ExeYearsToMaturity` | 行权待偿期 | number(19,4) | ✓ | 100.0% |  |
| 8 | `OpType` | 行权类型 | number(10) | ✗ | 100.0% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN ... |
| 9 | `ExpectedExerciseDate` | 最近可能行权日 | date | ✓ | 100.0% |  |
| 10 | `CloseDirtyPrice` | 全价收盘价(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `ExeYTM_CL` | 行权收益率(%) | number(18,10) | ✓ | 100.0% |  |
| 12 | `ExeDuration_CL` | 行权麦氏久期 | number(18,10) | ✓ | 100.0% |  |
| 13 | `ExeModifiedDuration_CL` | 行权修正久期 | number(18,10) | ✓ | 100.0% |  |
| 14 | `ExeSpreadDuration_CL` | 行权利差久期 | number(18,10) | ✓ | 0.19% |  |
| 15 | `ExeIRDuration_CL` | 行权利率久期 | number(18,10) | ✓ | 0.19% |  |
| 16 | `ExeConvexity_CL` | 行权凸性 | number(18,10) | ✓ | 100.0% |  |
| 17 | `ExeSpreadConvexity_CL` | 行权利差凸性 | number(18,10) | ✓ | 0.19% |  |
| 18 | `ExeIRConvexity_CL` | 行权利率凸性 | number(18,10) | ✓ | 0.19% |  |
| 19 | `ExePointSpreadYield_CL` | 行权点差收益率(%) | number(18,10) | ✓ | 0.19% |  |
| 20 | `ExeBasisPointValue_CL` | 行权基点价值 | number(18,10) | ✓ | 100.0% |  |
| 21 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN(83,89,90) OR LB = 1006 AND DM IN(12,18,21) ，得到证券市场的具体描述：12-上交所固定收益平台，18-深交所综合收益平台，21-上交所大宗交易，83-上海证券交易所，89-银行间债券市场，90-深圳证券交易所。

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN (101,201,203)，得到行权类型的具体描述：101-发行人赎回权，201-持有人回售权，203-持有人定向转让权。

## SQL示例

```sql
-- 查询 含权债券衍生指标 数据
SELECT *
FROM bond_embeddedderiv
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
