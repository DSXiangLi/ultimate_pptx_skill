# Bond_ABSIBQuote

**中文名**: 资产支持证券交易行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ABSIBQuote` |
| MySQL表名 | `bond_absibquote` |
| 中文名 | 资产支持证券交易行情 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 本币市场成交收盘行情 > 债券市场成交收盘行情  |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1 |

## 表描述

1.内容说明：收录每个交易日，银行间债券市场资产支持证券净价交易行情。
2.数据范围：2009-10-27 至今
3.信息来源：全国银行间同业拆借中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券代码 | number(10) | ✗ | 100.0% | 证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到回... |
| 4 | `PrevCloseNetPrice` | 前收盘净价(元) | number(18,10) | ✓ | 51.69% |  |
| 5 | `PrevWeightedNetPrice` | 前加权净价(元) | number(18,10) | ✓ | 51.71% |  |
| 6 | `OpenNetPrice` | 开盘净价(元) | number(18,10) | ✓ | 100.0% |  |
| 7 | `HighNetPrice` | 最高净价(元) | number(18,10) | ✓ | 100.0% |  |
| 8 | `LowNetPrice` | 最低净价(元) | number(18,10) | ✓ | 100.0% |  |
| 9 | `CloseNetPrice` | 收盘净价(元) | number(18,10) | ✓ | 100.0% |  |
| 10 | `WeightedAverageNetPrice` | 加权平均净价(元) | number(18,10) | ✓ | 100.0% |  |
| 11 | `PrevClosePriceYTM` | 前收盘收益率(%) | number(18,10) | ✓ | 0.14% |  |
| 12 | `PrevWeightedPriceYTM` | 前加权平均收益率(%) | number(18,10) | ✓ | 0.03% |  |
| 13 | `OpenPriceYTM` | 开盘收益率(%) | number(18,10) | ✓ | 0.15% |  |
| 14 | `HighPriceYTM` | 最高收益率(%) | number(18,10) | ✓ | 0.15% |  |
| 15 | `LowPriceYTM` | 最低收益率(%) | number(18,10) | ✓ | 0.15% |  |
| 16 | `ClosePriceYTM` | 收盘收益率(%) | number(18,10) | ✓ | 99.8% |  |
| 17 | `WeightedPriceYTM` | 加权平均收益率(%) | number(18,10) | ✓ | 0.15% |  |
| 18 | `ParValueVol` | 券面总额(元) | number(19,4) | ✓ | 99.81% |  |
| 19 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 99.84% |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券代码)

证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到回购的交易代码、回购简称等。

## SQL示例

```sql
-- 查询 资产支持证券交易行情 数据
SELECT *
FROM bond_absibquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
