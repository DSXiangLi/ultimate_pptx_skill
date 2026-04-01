# Bond_CSIBondIndicesQuote

**中文名**: 中证债券指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CSIBondIndicesQuote` |
| MySQL表名 | `bond_csibondindicesquote` |
| 中文名 | 中证债券指数行情 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 24 |
| 版本 | 1.03 |

## 表描述

1.收录了中证债券系列指数的每日指数值、成交量以及修正久期、凸性等；包含中证全债指数，以及4只分年期指数（中证3债、中证7债、中证10债、中证10+债）和3只分类别指数（中证国债、中证金融债、中证企业债）。
2.历史数据：2002年12月至今
3.数据源：中证指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `IndexCode` | 指数代码 | varchar2(30) | ✓ | 100.0% |  |
| 4 | `IndexAbbr` | 指数简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `TradingDate` | 交易日期 | date | ✓ | 100.0% |  |
| 6 | `PrevClosePrice` | 昨收盘 | number(19,4) | ✓ | 99.96% |  |
| 7 | `OpenPrice` | 开盘价(元/点) | number(19,4) | ✓ | 0.82% |  |
| 8 | `HighPrice` | 最高价(元/点) | number(19,4) | ✓ | 0.82% |  |
| 9 | `LowPrice` | 最低价(元/点) | number(19,4) | ✓ | 0.82% |  |
| 10 | `ClosePrice` | 收盘价 | number(19,4) | ✓ | 100.0% |  |
| 11 | `ChangePCT` | 涨跌幅(%) | number(18,6) | ✓ | 99.96% |  |
| 12 | `TurnoverVolume` | 成交量(万元) | number(19,4) | ✓ | 77.42% |  |
| 13 | `TurnoverValue` | 成交额(元) | number(19,4) | ✓ | 40.45% |  |
| 14 | `SettlementSum` | 结算金额(元) | number(19,4) | ✓ | 36.81% |  |
| 15 | `Duration` | 平均市值法久期 | number(10,4) | ✓ | 36.12% |  |
| 16 | `ModifiedDuration` | 平均市值法修正久期 | number(10,4) | ✓ | 36.17% |  |
| 17 | `Convexity` | 平均市值法凸性 | number(10,4) | ✓ | 36.17% |  |
| 18 | `YTM` | 平均市值法到期收益率(%) | number(18,8) | ✓ | 36.17% |  |
| 19 | `NumberOfComponents` | 指数样本数量 | number(10) | ✓ | 39.16% |  |
| 20 | `AvgPrice` | 平均价格 | number(19,4) | ✓ | 37.22% |  |
| 21 | `NetValueIndex` | 净价指数值 | number(19,4) | ✓ | 9.23% |  |
| 22 | `DividendReinvestIndex` | 利息及再投资指数值 | number(19,4) | ✓ | 9.23% |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (指数内部编码)

指数内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

## SQL示例

```sql
-- 查询 中证债券指数行情 数据
SELECT *
FROM bond_csibondindicesquote
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
