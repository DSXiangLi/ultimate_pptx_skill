# Bond_CurSwapCurveQuote

**中文名**: 货币掉期曲线报价行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CurSwapCurveQuote` |
| MySQL表名 | `bond_curswapcurvequote` |
| 中文名 | 货币掉期曲线报价行情 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：收录每个交易日公布的货币掉期曲线行情数据；
2.数据范围：2012-12-28 至今
3.信息来源：货币网

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 报价日期 | date | ✗ | 100.0% |  |
| 3 | `TradingTime` | 报价时间 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `CurveCode` | 曲线代码 | number(10) | ✗ | 100.0% | 曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1972，得到曲线代码的... |
| 6 | `CurveName` | 曲线名称 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `Tenor` | 标准期限 | number(10) | ✓ | 100.0% | 标准期限(Tenor)与(CT_SystemConst)表中的DM字段关联，令LB = 1723，得到标准期限的具体描述... |
| 8 | `PriceUnit` | 计价单位 | number(10) | ✓ | 100.0% | 计价单位（PriceUnit）：固定常量——当曲线代码(CurveCode)=1时，计价单位（PriceUnit）为1-... |
| 9 | `Bid` | 报买 | number(18,6) | ✓ | 100.0% |  |
| 10 | `Ask` | 报卖 | number(18,6) | ✓ | 100.0% |  |
| 11 | `Mean` | 均值 | number(18,6) | ✓ | 100.0% |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (曲线代码)

曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1972，得到曲线代码的具体描述：1-人民币固定利率对美元Libor_3M，2-人民币Shibor_3M对美元Libor_3M。

### Tenor (标准期限)

标准期限(Tenor)与(CT_SystemConst)表中的DM字段关联，令LB = 1723，得到标准期限的具体描述：1-1M，2-2M，3-3M，4-6M，5-9M，6-1W，7-7D，21-1Y，22-2Y，23-3Y，24-4Y，25-5Y，26-7Y，27-10Y，28-1D，29-9Y，30-8Y，31-6Y，32-30Y，33-20Y。

### PriceUnit (计价单位)

计价单位（PriceUnit）：固定常量——当曲线代码(CurveCode)=1时，计价单位（PriceUnit）为1-%；当曲线代码(CurveCode)=2时，计价单位（PriceUnit）为2-BP

## SQL示例

```sql
-- 查询 货币掉期曲线报价行情 数据
SELECT *
FROM bond_curswapcurvequote
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
