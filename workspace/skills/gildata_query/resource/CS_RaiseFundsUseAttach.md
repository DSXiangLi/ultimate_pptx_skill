# CS_RaiseFundsUseAttach

**中文名**: 股票募集资金用途变更事项说明

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_RaiseFundsUseAttach` |
| MySQL表名 | `cs_raisefundsuseattach` |
| 中文名 | 股票募集资金用途变更事项说明 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1. 内容说明：收录主板上市公司通过发行新股、增发新股、配股、优先股等方式所得募集资金用途变更明细。
2. 数据范围：2020/11/30至今
3. 信息来源：交易所公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID(RID)：与股票募集资金用途(CS_RaiseFundsUse)的ID关联，获取对应项目信息 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `ChangeItem` | 变更事项 | number(10) | ✗ | 100.0% | 变更事项(ChangeItem)与(CT_SystemConst)表中的DM字段关联，令LB=2594，得到变更事项的具... |
| 5 | `NewProjectSN` | 变更后新项目序号 | varchar2(40) | ✗ | 100.0% |  |
| 6 | `ChangeItemStatement` | 变更事项说明 | varchar2(2000) | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID(RID)：与股票募集资金用途(CS_RaiseFundsUse)的ID关联，获取对应项目信息

### ChangeItem (变更事项)

变更事项(ChangeItem)与(CT_SystemConst)表中的DM字段关联，令LB=2594，得到变更事项的具体描述：1-实施主体，2-实施方式，3-实施地点，4-计划投入募集金额，5-实施周期，6-实施项目(全部改投)，7-实施项目(部分改投)，99-其他。

## SQL示例

```sql
-- 查询 股票募集资金用途变更事项说明 数据
SELECT *
FROM cs_raisefundsuseattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
