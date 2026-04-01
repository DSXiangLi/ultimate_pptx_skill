# HK_TempParTrade

**中文名**: 港股临时并行交易表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_TempParTrade` |
| MySQL表名 | `hk_temppartrade` |
| 中文名 | 港股临时并行交易表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.记录港股临时并行交易代码对应和时间信息，包含有买卖未缴款供股权、拆股合并、更改买卖单位等几种情况引起的临时并行买卖。
2.数据范围：1999年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 主代码内部编码 | number(10) | ✗ | 100.0% | 主代码内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode... |
| 3 | `EventType` | 事件类别 | number(10) | ✗ | 100.0% | 事件类别(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1902，得到事件类别的... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `OldTradeUnit` | 主代码旧交易单位(股/手) | number(10) | ✓ | 85.88% |  |
| 6 | `NewTradeUnit` | 主代码新交易单位(股/手) | number(10) | ✓ | 86.4% |  |
| 7 | `TempInnerCode` | 临时代码内部编码 | number(10) | ✓ | 100.0% | 临时代码内部编码（TempInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码(Inne... |
| 8 | `TempShareCode` | 临时代码 | varchar2(10) | ✗ | 100.0% |  |
| 9 | `TempShareAbbrName` | 临时证券简称 | varchar2(20) | ✓ | 100.0% |  |
| 10 | `TempTradeUnit` | 临时代码买卖单位(股/手) | number(10) | ✓ | 100.0% |  |
| 11 | `TempTradeBeginDate` | 临时买卖开始日期 | date | ✓ | 100.0% | 临时买卖开始日期（TempTradeBeginDate）：在事件类别是1-买卖未缴款供股权，2-更改买卖单位时，主交易代... |
| 12 | `SimulTradeBeginDate` | 并行买卖开始日期 | date | ✓ | 88.05% | 并行买卖开始日期（SimulTradeBeginDate）：正常是指当天09:00。 |
| 13 | `SimulTradeEndDate` | 临时并行结束日期 | date | ✓ | 100.0% | 临时并行结束日期(SimulTradeEndDate)：正常是指当天16:00。 |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | None | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (主代码内部编码)

主代码内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### EventType (事件类别)

事件类别(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1902，得到事件类别的具体描述：1-买卖未缴款供股权，2-更改买卖单位，3-股份拆细，4-股份合并，5-股份先并后拆，6-股份先拆后并，7-其他。

### TempInnerCode (临时代码内部编码)

临时代码内部编码（TempInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码(InnerCode)”关联，得到港股的临时交易代码等。

### TempTradeBeginDate (临时买卖开始日期)

临时买卖开始日期（TempTradeBeginDate）：在事件类别是1-买卖未缴款供股权，2-更改买卖单位时，主交易代码不停牌，因而临时买卖开始日期和并行买卖开始日期一致。正常生效时间是当天09:00。

### SimulTradeBeginDate (并行买卖开始日期)

并行买卖开始日期（SimulTradeBeginDate）：正常是指当天09:00。

### SimulTradeEndDate (临时并行结束日期)

临时并行结束日期(SimulTradeEndDate)：正常是指当天16:00。

## SQL示例

```sql
-- 查询 港股临时并行交易表 数据
SELECT *
FROM hk_temppartrade
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
