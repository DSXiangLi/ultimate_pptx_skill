# Bond_CBECL

**中文名**: 中债登债券预期信用损失

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBECL` |
| MySQL表名 | `bond_cbecl` |
| 中文名 | 中债登债券预期信用损失 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中债发布的债券预期信用损失
2.数据范围：2020-03-31 至今
3.信息来源：中债登

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `YearsToMaturity` | 待偿期 | number(18,8) | ✗ | 100.0% | 对于含权债券，其他条件都相同时显示两种待偿期，较长的待偿期表示到期的情况，较短的待偿期表示行权的情况. |
| 5 | `InitialRecStartDate` | 初始确认日期起始日 | date | ✗ | 100.0% |  |
| 6 | `InitialRecEndDate` | 初始确认日期截止日 | date | ✓ | 100.0% |  |
| 7 | `ProbDefaultStage` | 减值阶段 | number(10) | ✓ | 100.0% | 减值阶段(ProbDefaultStage)与(CT_SystemConst)表中的DM字段关联，令LB = 2357 ... |
| 8 | `ProbDefaultMat` | 减值期限 | number(18,8) | ✓ | 100.0% |  |
| 9 | `ValueImpliedPD` | 估值隐含违约率(%) | number(18,8) | ✓ | 100.0% |  |
| 10 | `LossGivenDefault` | 违约损失率(%) | number(18,8) | ✓ | 100.0% |  |
| 11 | `CreditLossR` | 信用损失比例(%) | number(18,8) | ✓ | 100.0% |  |
| 12 | `Remark` | 备注 | varchar2(200) | ✓ | 84.2% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等

### YearsToMaturity (待偿期)

对于含权债券，其他条件都相同时显示两种待偿期，较长的待偿期表示到期的情况，较短的待偿期表示行权的情况.

### ProbDefaultStage (减值阶段)

减值阶段(ProbDefaultStage)与(CT_SystemConst)表中的DM字段关联，令LB = 2357 and DM IN (1,2)，得到减值阶段的具体描述：1-阶段一，2-阶段二。

## SQL示例

```sql
-- 查询 中债登债券预期信用损失 数据
SELECT *
FROM bond_cbecl
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
