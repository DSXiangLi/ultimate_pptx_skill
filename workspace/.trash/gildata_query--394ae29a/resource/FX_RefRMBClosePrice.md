# FX_RefRMBClosePrice

**中文名**: 人民币即期汇率收盘价和参考价

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FX_RefRMBClosePrice` |
| MySQL表名 | `fx_refrmbcloseprice` |
| 中文名 | 人民币即期汇率收盘价和参考价 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中国外汇交易中心发布的即期汇率收盘价/参考价数据
2.数据范围：2021-03-31至今
3.信息来源：中国外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `QuoteTime` | 报价日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 货币对内部编码 | number(10) | ✗ | 100.0% |  |
| 4 | `CurrencyTradeName` | 货币对名称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `RefClosePrice` | 收盘价/参考价 | number(19,8) | ✓ | 100.0% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 人民币即期汇率收盘价和参考价 数据
SELECT *
FROM fx_refrmbcloseprice
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
