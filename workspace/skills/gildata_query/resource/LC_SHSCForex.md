# LC_SHSCForex

**中文名**: 沪港通汇率信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSCForex` |
| MySQL表名 | `lc_shscforex` |
| 中文名 | 沪港通汇率信息 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.收录沪港通交易的参考汇率及结算汇率。汇率为直接报价。
2.历史数据：2014年11月起-至今
3.数据来源：聚源按照上交所披露整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `ForeCurrency` | 外币种类 | number(10) | ✗ | 100.0% | 外币种类(ForeCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 4 | `DomeCurrency` | 本币种类 | number(10) | ✗ | 100.0% | 本币种类(DomeCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 5 | `RefBid` | 买入参考汇率 | number(18,6) | ✓ | 100.0% |  |
| 6 | `RefAsk` | 卖出参考汇率 | number(18,6) | ✓ | 100.0% |  |
| 7 | `SettleBid` | 买入结算汇率 | number(18,6) | ✓ | 99.96% |  |
| 8 | `SettleAsk` | 卖出结算汇率 | number(18,6) | ✓ | 99.96% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ForeCurrency (外币种类)

外币种类(ForeCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1100,1420)，得到外币种类的具体描述：1100-港元，1420-人民币元。

### DomeCurrency (本币种类)

本币种类(DomeCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1100,1420)，得到本币种类的具体描述：1100-港元，1420-人民币元。

## SQL示例

```sql
-- 查询 沪港通汇率信息 数据
SELECT *
FROM lc_shscforex
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
