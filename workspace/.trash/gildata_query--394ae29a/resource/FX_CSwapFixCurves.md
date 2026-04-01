# FX_CSwapFixCurves

**中文名**: 外汇掉期C-Swap定盘曲线

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FX_CSwapFixCurves` |
| MySQL表名 | `fx_cswapfixcurves` |
| 中文名 | 外汇掉期C-Swap定盘曲线 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：收录每个交易日外汇掉期各期限代表性价格（掉期点）构成的行情曲线数据
2.数据范围：2021-01-20至今
3.信息来源：全国银行间同业拆借中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingTime` | 交易时间 | varchar2(8) | ✗ | 100.0% |  |
| 4 | `CurveType` | 曲线类型 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `CurveName` | 曲线名称 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `CurveCode` | 曲线代码 | number(10) | ✗ | 100.0% | 曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB=2376 AND FVALU... |
| 7 | `Maturity` | 标准期限 | number(18,10) | ✓ | 100.0% |  |
| 8 | `MaturityCode` | 标准期限代码 | number(10) | ✗ | 100.0% | 标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB=1555，得到标准... |
| 9 | `SwapPointSource` | 掉期点来源 | varchar2(50) | ✓ | 100.0% | 掉期点来源(SwapPointSource)与(CT_SystemConst)表中的DM字段关联，令LB=2384，得到... |
| 10 | `SwapPoint` | 掉期点 | number(18,10) | ✓ | 100.0% |  |
| 11 | `SwapAllinRate` | 外汇掉期全价汇率 | number(18,10) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (曲线代码)

曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB=2376 AND FVALUE =2，得到曲线代码的具体描述：6200001-美元对人民币外汇掉期C-Swap定盘曲线。

### MaturityCode (标准期限代码)

标准期限代码(MaturityCode)与(CT_SystemConst)表中的DM字段关联，令LB=1555，得到标准期限代码的具体描述：1-ON，2-TN，3-SN，4-SW，5-2W，6-3W，7-1M，8-2M，9-3M，10-4M，11-5M，12-6M，13-9M，14-18M，15-1Y，16-2Y，17-3Y，18-T1，19-1D，20-1W，21-TOD，22-TOM，23-4Y，24-5Y，25-7M，26-8M，27-10M，28-11M，29-15M，30-21M，31-6Y，32-7Y，33-10Y，99-其他。

### SwapPointSource (掉期点来源)

掉期点来源(SwapPointSource)与(CT_SystemConst)表中的DM字段关联，令LB=2384，得到掉期点来源的具体描述：101-交易数据，102-报价数据，103-货币经纪，104-交易系统，120-C-SWAP，121-插值计算，122-前掉期点，1061-前收盘价曲线数据。

## SQL示例

```sql
-- 查询 外汇掉期C-Swap定盘曲线 数据
SELECT *
FROM fx_cswapfixcurves
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
