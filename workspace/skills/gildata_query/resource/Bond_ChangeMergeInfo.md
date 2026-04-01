# Bond_ChangeMergeInfo

**中文名**: 债券调换与合并

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ChangeMergeInfo` |
| MySQL表名 | `bond_changemergeinfo` |
| 中文名 | 债券调换与合并 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 21 |
| 版本 | 1.01 |

## 表描述

1.收录含有调换选择权、转换选择权以及合并权的债券的相关信息。
2.包括行权期间、行权操作日、最低操作金额、行权目标券、调换比例、本券行权金额、目标券行权金额等。
3.数据范围：2002-03-13 至今
4.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `MainCode` | 内部代码 | number(10) | ✗ | 100.0% | 债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联... |
| 3 | `InfoPublDate` | 公告日期 | date | ✓ | 100.0% |  |
| 4 | `OpType` | 行权类型 | number(10) | ✓ | 100.0% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN ... |
| 5 | `OpRemark` | 权利描述 | clob | ✓ | 71.22% |  |
| 6 | `ExpectedExerciseDate` | 权利可能行使日 | date | ✓ | 89.98% |  |
| 7 | `OpProgress` | 行权进程 | number(10) | ✓ | 100.0% | 行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程... |
| 8 | `IfOption` | 是否行权 | number(10) | ✓ | 49.54% | 是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN... |
| 9 | `OptionReason` | 行权原因说明 | varchar2(2000) | ✓ | 47.54% |  |
| 10 | `CommOpApplStDate` | 行权申请受理起始日 | date | ✓ | 34.79% |  |
| 11 | `CommOpApplEdDate` | 行权申请受理截止日 | date | ✓ | 34.79% |  |
| 12 | `CommOptionDate` | 行权操作日 | date | ✓ | 49.36% |  |
| 13 | `LeastOpVol` | 最低操作金额 | number(19,4) | ✓ | 43.53% |  |
| 14 | `TargetBDCode` | 换/并入目标券代码 | number(10) | ✓ | 98.72% | 换/并入目标券代码（TargetBDCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（MainC... |
| 15 | `ChangeRatio` | 调换比例 | number(19,8) | ✓ | 99.64% |  |
| 16 | `RootBDOutVol` | 本券换/并出金额(元) | number(19,4) | ✓ | 22.77% |  |
| 17 | `RootBDOutstanding` | 本券换/并出后余额(元) | number(19,4) | ✓ | 44.81% |  |
| 18 | `TargetBDInVol` | 目标券换/并入金额(元) | number(19,4) | ✓ | 22.77% |  |
| 19 | `TargetBDSum` | 目标券换/并入后总金额(元) | number(19,4) | ✓ | 44.81% |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### MainCode (内部代码)

债券内部编码（MainCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券的交易代码、债券简称等。

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN (207,209,301)，得到行权类型的具体描述：207-持有人可调换选择权，209-持有人可转换选择权，301-合并。

### OpProgress (行权进程)

行权进程(OpProgress)与(CT_SystemConst)表中的DM字段关联，令LB = 1441，得到行权进程的具体描述：1-发行时权利约定，2-行权提示与结果。

### IfOption (是否行权)

是否行权(IfOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否行权的具体描述：1-是，2-否。

### TargetBDCode (换/并入目标券代码)

换/并入目标券代码（TargetBDCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（MainCode）”关联，得到换/并入目标券代码的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 债券调换与合并 数据
SELECT *
FROM bond_changemergeinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
