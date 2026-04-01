# Bond_RFundsUseAttach

**中文名**: 债券募集资金用途附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RFundsUseAttach` |
| MySQL表名 | `bond_rfundsuseattach` |
| 中文名 | 债券募集资金用途附表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.发行债券所得募集资金用途的分类情况。
2.数据范围：1992-11-01至今
3.信息来源：募集说明书以及募集资金用途改投公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：与“债券募集资金用途Bond_RaiseFundsUse”表的ID字段相关联。 |
| 3 | `EventType` | 事件类型 | number(10) | ✗ | 100.0% | 事件类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2270，得到事件类型的... |
| 4 | `EventTypeF` | 事件分类一级 | number(10) | ✗ | 100.0% | 事件分类一级(EventTypeF)与(CT_SystemConst)表中的DM字段关联，令LB = 2271 AND ... |
| 5 | `EventTypeS` | 事件分类二级 | number(10) | ✓ | 88.04% | 事件分类二级(EventTypeS)与(CT_SystemConst)表中的DM字段关联，令LB = 2271 and ... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：与“债券募集资金用途Bond_RaiseFundsUse”表的ID字段相关联。

### EventType (事件类型)

事件类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2270，得到事件类型的具体描述：1-募资投向项目类型。

### EventTypeF (事件分类一级)

事件分类一级(EventTypeF)与(CT_SystemConst)表中的DM字段关联，令LB = 2271 AND IVALUE = 1，得到事件分类一级的具体描述：10-充实资金，20-偿还债务，30-投资经营，40-城市更新项目，80-地方政府债相关，99-其他。

### EventTypeS (事件分类二级)

事件分类二级(EventTypeS)与(CT_SystemConst)表中的DM字段关联，令LB = 2271 and IVALUE = 2，得到事件分类二级的具体描述：1001-补充营运资金，1002-充实资本，2001-偿还借款，2002-偿还到期债券，8001-地方政府债(专项)，8002-地方政府债(一般)，8003-地方政府债(置换)，8004-地方政府债(新增)。

## SQL示例

```sql
-- 查询 债券募集资金用途附表 数据
SELECT *
FROM bond_rfundsuseattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
