# MF_ManagerExperience

**中文名**: 基金经理任职及管理年限统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ManagerExperience` |
| MySQL表名 | `mf_managerexperience` |
| 中文名 | 基金经理任职及管理年限统计 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.本表记录了聚源整理的基金经理担任基金经理的所有历程，及其管理基金年限统计，包括本公司管理年限、历史平均管理年限、总计管理年限等。
2.历史数据：1998年3月起-至今。
3.信息来源：聚源根据常用基金概况表数据整理而成。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `PersonalCode` | 基金经理代码 | number(10) | ✗ | 100.0% | 基金经理代码（PersonalCode）：与“公募基金经理基本资料（MF_PersonalInfo）”中的“所属人员编码... |
| 3 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 4 | `InvestAdvisorCode` | 基金管理人编号 | number(10) | ✗ | 100.0% | 基金管理人编号(InvestAdvisorCode)与“公募基金管理人概况(MF_InvestAdvisorOutlin... |
| 5 | `BeginDate` | 开始日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 52.24% |  |
| 7 | `EmploymentCompany` | 本公司管理年限(月) | number(18,2) | ✓ | 100.0% |  |
| 8 | `EmploymentAverage` | 历史平均管理年限(月) | number(18,2) | ✓ | 60.91% |  |
| 9 | `EmploymentAll` | 总计管理年限(月) | number(18,2) | ✓ | 100.0% |  |
| 10 | `Incumbent` | 是否在任 | number(10) | ✗ | 100.0% | 是否在任（Incumbent）该字段固定以下常量：1-是；0-否 |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PersonalCode (基金经理代码)

基金经理代码（PersonalCode）：与“公募基金经理基本资料（MF_PersonalInfo）”中的“所属人员编码（PersonalCode）”关联，得到基金经理的基本资料。

### InvestAdvisorCode (基金管理人编号)

基金管理人编号(InvestAdvisorCode)与“公募基金管理人概况(MF_InvestAdvisorOutline)”中的“ 基金管理人编码（InvestAdvisorCode）”关联，得到基金管理人的基本资料。

### Incumbent (是否在任)

是否在任（Incumbent）该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 基金经理任职及管理年限统计 数据
SELECT *
FROM mf_managerexperience
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
