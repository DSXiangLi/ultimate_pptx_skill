# Bond_SExchangeDetailFI

**中文名**: 沪固收行情成交明细表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SExchangeDetailFI` |
| MySQL表名 | `bond_sexchangedetailfi` |
| 中文名 | 沪固收行情成交明细表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：包含在上交所固定收益平台交易的所有债券的成交明细数据。
2.每一笔交易的成交净价、全价、到期收益率、成交量、成交方式等，对于上交所固定收益平台的交易债券都收录了其公布值。
3.数据范围：2023-08-31 至今
4.信息来源：上交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `TradingTime` | 交易时间 | varchar2(12) | ✗ | 100.0% |  |
| 5 | `AccuTurnoverDeals` | 累计成交笔数 | number(10) | ✗ | 100.0% |  |
| 6 | `CleanPrice` | 成交净价(元) | number(19,8) | ✓ | 100.0% |  |
| 7 | `AccruedInterest` | 应计利息(元) | number(19,8) | ✓ | 100.0% |  |
| 8 | `FullPrice` | 成交全价(元) | number(19,8) | ✓ | 100.0% |  |
| 9 | `YTM` | 到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 10 | `TurnoverVolume` | 成交量(手) | number(19,4) | ✓ | 100.0% |  |
| 11 | `TurnoverValue` | 成交金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `TradeType` | 沪固收行情成交方式 | number(10) | ✗ | 100.0% | 沪固收行情成交方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB=2578 ，得到沪... |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### TradeType (沪固收行情成交方式)

沪固收行情成交方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB=2578 ，得到沪固收行情成交方式的具体描述：1-确定报价成交，2-待定报价成交，3-询价成交，5-场务应急，6-指定对手方(含合并申报)，7-竞买。

## SQL示例

```sql
-- 查询 沪固收行情成交明细表 数据
SELECT *
FROM bond_sexchangedetailfi
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
