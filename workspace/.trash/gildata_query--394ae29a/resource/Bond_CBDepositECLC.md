# Bond_CBDepositECLC

**中文名**: 中债存款预期信用损失(定制)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDepositECLC` |
| MySQL表名 | `bond_cbdepositeclc` |
| 中文名 | 中债存款预期信用损失(定制) |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中债发布的存款预期信用损失的定制化数据，包括存单编号，存单的具体信息以及违约率，违约损失率和信用损失比例等数据
2.数据范围：2021-12-7 至今
3.信息来源：中债登

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `DepositCode` | 存单编号 | varchar2(50) | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 存款机构代码 | number(10) | ✗ | 100.0% | 存款机构代码（CompanyCode): 与“机构基本资料（LC_InstiArchive）”中的“企业编号（Compa... |
| 4 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 5 | `YearsToMaturity` | 待偿期 | number(18,8) | ✗ | 100.0% |  |
| 6 | `ValueDate` | 存款起息日 | date | ✓ | 100.0% |  |
| 7 | `DepositEndDate` | 存款到期日 | date | ✓ | 100.0% |  |
| 8 | `IfWithdrawal` | 是否可提前支取 | number(10) | ✓ | 100.0% | 是否可提前支取(IfWithdrawl): 该字段固定以下常量：1-是；2-否 |
| 9 | `WithdrawlDate` | 提前支取开始日 | date | ✓ | 42.13% |  |
| 10 | `ProbDefaultStage` | 减值阶段 | number(10) | ✓ | 100.0% | 减值阶段(ProbDefaultStage): 该字段固定以下常量：1-阶段一；2-阶段二 |
| 11 | `ProbDefaultMat` | 减值期限(年) | number(18,8) | ✓ | 100.0% |  |
| 12 | `ValueImpliedPD` | 估值隐含违约率(%) | number(18,8) | ✓ | 100.0% |  |
| 13 | `LossGivenDefault` | 违约损失率(%) | number(18,8) | ✓ | 100.0% |  |
| 14 | `CreditLossR` | 信用损失比例(%) | number(18,8) | ✓ | 100.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (存款机构代码)

存款机构代码（CompanyCode): 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### IfWithdrawal (是否可提前支取)

是否可提前支取(IfWithdrawl): 该字段固定以下常量：1-是；2-否

### ProbDefaultStage (减值阶段)

减值阶段(ProbDefaultStage): 该字段固定以下常量：1-阶段一；2-阶段二

## SQL示例

```sql
-- 查询 中债存款预期信用损失(定制) 数据
SELECT *
FROM bond_cbdepositeclc
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
