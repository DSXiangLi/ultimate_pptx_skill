# HK_StoDiscChgShares

**中文名**: 港股披露权益变动股数

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_StoDiscChgShares` |
| MySQL表名 | `hk_stodiscchgshares` |
| 中文名 | 港股披露权益变动股数 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.记录港股权益事件变动前后持股数量信息，包括内容有：持仓类型、事件前持股总数、事件前持股占比、事件后持股总数、事件后持股总数等。该表为港股披露权益系列表的附表之一。
2.数据范围：1997年至今。
3.数据来源:港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联 |
| 3 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到持仓... |
| 4 | `HoldSumBefEvent` | 事件前持股总数(股) | number(18,2) | ✓ | 98.99% |  |
| 5 | `HRatioBefEvent` | 事件前持股占比 | number(18,9) | ✓ | 98.99% | 事件前持股占比（HRatioBefEvent）：单位为数值，不是%。 |
| 6 | `HoldSumAfEvent` | 事件后持股总数(股) | number(18,2) | ✓ | 99.88% |  |
| 7 | `HRatioAfEvent` | 事件后持股占比 | number(18,9) | ✓ | 99.88% | 事件后持股占比（HRatioAfEvent）：单位有数值，没有%。 |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“港股披露权益信息（HK_StoDiscInf）”表的ID字段关联

### PosCharacter (持仓类型)

持仓类型(PosCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1342，得到持仓类型的具体描述：1-好仓，3-淡仓，9-可供借出股份。

### HRatioBefEvent (事件前持股占比)

事件前持股占比（HRatioBefEvent）：单位为数值，不是%。

### HRatioAfEvent (事件后持股占比)

事件后持股占比（HRatioAfEvent）：单位有数值，没有%。

## SQL示例

```sql
-- 查询 港股披露权益变动股数 数据
SELECT *
FROM hk_stodiscchgshares
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
