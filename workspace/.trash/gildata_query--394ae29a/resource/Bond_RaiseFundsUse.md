# Bond_RaiseFundsUse

**中文名**: 债券募集资金用途

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RaiseFundsUse` |
| MySQL表名 | `bond_raisefundsuse` |
| 中文名 | 债券募集资金用途 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.发行债券所得募集资金的项目投资情况以及改投状况。
2.数据范围：1992-11-01至今
3.信息来源：募集说明书以及募集资金用途改投公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `RaisingType` | 募集类型 | number(10) | ✓ | 100.0% | 募集类型(RaisingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2268，得到募集类... |
| 6 | `SwitchedType` | 改投类型 | number(10) | ✓ | 2.59% | 改投类型(SwitchedType)与(CT_SystemConst)表中的DM字段关联，令LB = 2269，得到改投... |
| 7 | `InvestProject` | 募资投向项目名称 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `PlannedSum` | 计划投入金额(元) | number(19,4) | ✓ | 73.54% |  |
| 9 | `ProjectStatement` | 项目内容 | clob | ✓ | 2.4% |  |
| 10 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 11 | `EndDate` | 有效截止日期 | date | ✓ | 2.38% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### RaisingType (募集类型)

募集类型(RaisingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2268，得到募集类型的具体描述：1-首次募集，2-募资改投，3-增发募集。

### SwitchedType (改投类型)

改投类型(SwitchedType)与(CT_SystemConst)表中的DM字段关联，令LB = 2269，得到改投类型的具体描述：1-变更投向项目，2-变更项目明细，3-变更投入金额，99-其他。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 债券募集资金用途 数据
SELECT *
FROM bond_raisefundsuse
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
