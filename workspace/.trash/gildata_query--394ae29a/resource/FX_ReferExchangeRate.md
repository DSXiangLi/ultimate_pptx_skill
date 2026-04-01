# FX_ReferExchangeRate

**中文名**: 外汇参考汇率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FX_ReferExchangeRate` |
| MySQL表名 | `fx_referexchangerate` |
| 中文名 | 外汇参考汇率 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录外汇交易中心的参考汇率
2.数据范围：2015-08-24 至今
2.信息来源：外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingTime` | 交易时间 | varchar2(10) | ✗ | 100.0% |  |
| 4 | `InnerCode` | 货币对内部编码 | number(10) | ✗ | 100.0% |  |
| 5 | `CurrencyTradeName` | 货币对名称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ReferenceExchangeRate` | 参考汇率 | number(18,8) | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 外汇参考汇率 数据
SELECT *
FROM fx_referexchangerate
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
