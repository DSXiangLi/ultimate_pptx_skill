# Bond_CBDerivNew

**中文名**: 可转换债券衍生指标新表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDerivNew` |
| MySQL表名 | `bond_cbderivnew` |
| 中文名 | 可转换债券衍生指标新表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1.03 |

## 表描述

1.收录可转换债券（包括可交换债券）衍生指标，包括纯债到期收益率，当期收益率，久期，凸性，转股价值，转股溢价率，纯债价值，纯债溢价率等。
2.信息来源：依据沪深交易所收盘行情衍生计算
3.数据范围：1993-01-04 至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% | 交易日期（TradingDay）：该字段可最早追溯到可转债发行日期起始日，此时对应字段计息天数（AccruedDays）... |
| 5 | `CloseDirtyPrice` | 全价收盘价(元) | number(19,4) | ✓ | 99.99% |  |
| 6 | `StockClosePrice` | 对应基础股票收盘价(元) | number(19,4) | ✓ | 99.81% |  |
| 7 | `AccruedDays` | 计息天数 | number(10) | ✓ | 99.79% |  |
| 8 | `AccruedInterest` | 每百元应计利息(元) | number(18,12) | ✓ | 99.78% |  |
| 9 | `YearsToMaturity` | 待偿期(年) | number(19,4) | ✓ | 99.95% |  |
| 10 | `YTM_CL` | 收盘价到期收益率(%) | number(18,10) | ✓ | 96.27% |  |
| 11 | `CBCurrentYield` | 当期收益率(%) | number(18,10) | ✓ | 99.88% |  |
| 12 | `Duration_CL` | 收盘价麦氏久期(年) | number(18,10) | ✓ | 96.27% |  |
| 13 | `ModifiedDuration_CL` | 收盘价修正久期 | number(18,10) | ✓ | 96.27% |  |
| 14 | `Convexity_CL` | 收盘价凸性 | number(18,10) | ✓ | 96.27% |  |
| 15 | `ConvertPrice` | 转股价(元) | number(19,4) | ✓ | 99.86% |  |
| 16 | `ConvertRatio` | 转股比例 | number(18,8) | ✓ | 99.86% |  |
| 17 | `CBConvertValue` | 转股价值 | number(18,8) | ✓ | 99.76% |  |
| 18 | `ConvertPremiumValue` | 转股溢价 | number(18,8) | ✓ | 99.75% |  |
| 19 | `ConvertPremiumRate` | 转股溢价率(%) | number(18,8) | ✓ | 99.71% |  |
| 20 | `ConvertParPrice` | 转换平价 | number(18,8) | ✓ | 99.84% |  |
| 21 | `CBStrbValue` | 纯债价值 | number(18,8) | ✓ | 98.28% |  |
| 22 | `CBStrbPremium` | 纯债溢价 | number(18,8) | ✓ | 98.27% |  |
| 23 | `CBStrbPremiumRatio` | 纯债溢价率(%) | number(18,8) | ✓ | 98.27% |  |
| 24 | `CBPSPremiumRate` | 平底溢价率(%) | number(18,8) | ✓ | 98.23% |  |
| 25 | `DoubleLow` | 双低 | number(18,8) | ✓ | 99.71% |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN(83,89,90,81) OR LB = 1006 AND DM IN(12,18,21,22) ，得到证券市场的具体描述：12-上交所固定收益平台，18-深交所综合收益平台，21-上交所大宗交易，22-上交所综合业务平台定转交易，81-三板市场，83-上海证券交易所，89-银行间债券市场，90-深圳证券交易所。

### TradingDay (交易日期)

交易日期（TradingDay）：该字段可最早追溯到可转债发行日期起始日，此时对应字段计息天数（AccruedDays）和每百元应计利息(元)（AccruedInterest）取值为空。

## SQL示例

```sql
-- 查询 可转换债券衍生指标新表 数据
SELECT *
FROM bond_cbderivnew
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
