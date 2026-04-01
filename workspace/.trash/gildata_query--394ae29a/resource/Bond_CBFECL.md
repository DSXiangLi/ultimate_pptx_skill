# Bond_CBFECL

**中文名**: 中债境外债预期信用损失

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBFECL` |
| MySQL表名 | `bond_cbfecl` |
| 中文名 | 中债境外债预期信用损失 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中债发布的境外债券预期信用损失
2.数据范围：2021年11月30号至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `SecuCode` | 债券代码 | varchar2(50) | ✗ | 100.0% |  |
| 4 | `InnerCode` | 内部编码 | number(10) | ✓ | 67.11% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 5 | `YearsToMaturity` | 待偿期 | number(18,8) | ✗ | 100.0% |  |
| 6 | `InitialRecStartDate` | 初始确认日期起始日 | date | ✗ | 100.0% |  |
| 7 | `InitialRecEndDate` | 初始确认日期截止日 | date | ✓ | 100.0% |  |
| 8 | `ProbDefaultStage` | 减值阶段 | number(10) | ✓ | 100.0% | 减值阶段(ProbDefaultStage)与(CT_SystemConst)表中的DM字段关联，令LB = 2357 ... |
| 9 | `ProbDefaultMat` | 减值期限 | number(18,8) | ✓ | 100.0% |  |
| 10 | `ValueImpliedPD` | 估值隐含违约率(%) | number(18,8) | ✓ | 100.0% |  |
| 11 | `LossGivenDefault` | 违约损失率(%) | number(18,8) | ✓ | 100.0% |  |
| 12 | `CreditLossR` | 信用损失比例(%) | number(18,8) | ✓ | 100.0% |  |
| 13 | `Remark` | 备注 | varchar2(200) | ✓ | 84.99% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。其中仅可提供自贸区离岸债券的关联，中资美元债需额外授权使用。

### ProbDefaultStage (减值阶段)

减值阶段(ProbDefaultStage)与(CT_SystemConst)表中的DM字段关联，令LB = 2357 and DM IN (1,2)，得到减值阶段的具体描述：1-阶段一，2-阶段二。

## SQL示例

```sql
-- 查询 中债境外债预期信用损失 数据
SELECT *
FROM bond_cbfecl
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
