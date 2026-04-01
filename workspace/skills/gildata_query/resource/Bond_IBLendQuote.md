# Bond_IBLendQuote

**中文名**: 银行间债券借贷成交行情表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IBLendQuote` |
| MySQL表名 | `bond_iblendquote` |
| 中文名 | 银行间债券借贷成交行情表 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 本币市场成交收盘行情 > 债券市场成交收盘行情  |
| 更新频率 | 日更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

1.内容说明：收录银行间债券借贷各种期限品种成交情况。
2.数据范围：2016-09-28 至今
3.信息来源：中国外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券借贷品种内部编码 | number(10) | ✗ | 100.0% | 债券借贷品种内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `MaturityType` | 期限品种 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `OpeningRate` | 开盘费率(%) | number(18,10) | ✓ | 100.0% |  |
| 6 | `ClosingRate` | 收盘费率(%) | number(18,10) | ✓ | 100.0% |  |
| 7 | `PrevClosingRate` | 前收盘费率(%) | number(18,10) | ✓ | 99.94% |  |
| 8 | `HighestRate` | 最高费率(%) | number(18,10) | ✓ | 100.0% |  |
| 9 | `LowestRate` | 最低费率(%) | number(18,10) | ✓ | 100.0% |  |
| 10 | `WeightAverageRate` | 加权费率(%) | number(18,10) | ✓ | 90.95% |  |
| 11 | `PrevWeightAverageRate` | 前加权费率(%) | number(18,10) | ✓ | 90.89% |  |
| 12 | `BasePointChange` | 加权费率升降(基点) | number(18,10) | ✓ | 30.64% |  |
| 13 | `TurnoverDeals` | 成交笔数(笔) | number(10) | ✓ | 34.08% |  |
| 14 | `NumOfChange` | 成交笔数增减(笔) | number(10) | ✓ | 33.91% |  |
| 15 | `TurnoverValue` | 成交金额(元) | number(18,4) | ✓ | 98.91% |  |
| 16 | `ChangeOfTurnoverValue` | 成交金额增减(元) | number(18,4) | ✓ | 6.64% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券借贷品种内部编码)

债券借贷品种内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到债券借贷品种的交易代码、交易简称等。

## SQL示例

```sql
-- 查询 银行间债券借贷成交行情表 数据
SELECT *
FROM bond_iblendquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
