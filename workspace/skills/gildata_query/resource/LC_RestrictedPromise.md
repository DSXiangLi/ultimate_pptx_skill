# LC_RestrictedPromise

**中文名**: 股东限售锁定期限承诺表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_RestrictedPromise` |
| MySQL表名 | `lc_restrictedpromise` |
| 中文名 | 股东限售锁定期限承诺表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上市公司非流通股东承诺事项，包括上市限售解禁期限、延长锁定期限类别指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `SubjectType` | 承诺主体类型 | number(10) | ✓ | 100.0% | 承诺主体类型(SubjectType)与(CT_SystemConst)表中的DM字段关联，令LB = 1351 AND... |
| 7 | `EventType` | 承诺事项类型 | number(10) | ✓ | 100.0% | 承诺事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352 AND D... |
| 8 | `IfEffected` | 承诺是否有效 | number(10) | ✓ | 100.0% | 承诺是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND D... |
| 9 | `SHSN` | 股东序号 | number(10) | ✓ | 100.0% |  |
| 10 | `SHName` | 股东名单 | varchar2(200) | ✗ | 100.0% |  |
| 11 | `PromiseType` | 承诺类别 | number(10) | ✗ | 100.0% | 承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306 AND D... |
| 12 | `PromiseStatment` | 承诺说明 | clob | ✓ | 6.91% |  |
| 13 | `PromiseRestrictedTerm` | 获流通权后承诺限售期限 | number(18,2) | ✓ | 88.94% |  |
| 14 | `InvolvedSum` | 涉及股数(股) | number(19,2) | ✓ | 10.59% |  |
| 15 | `RestrictedState` | 限售状态(承诺时) | number(10) | ✓ | 10.9% | 限售状态(承诺时)(RestrictedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 16 | `ProlongedLockupPeriod` | 延长锁定期限(月) | number(18,2) | ✓ | 10.69% |  |
| 17 | `DeadlineLockupDate` | 锁定期限截止 | date | ✓ | 2.14% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 

### SubjectType (承诺主体类型)

承诺主体类型(SubjectType)与(CT_SystemConst)表中的DM字段关联，令LB = 1351 AND DM IN (100,110,150,500)，得到承诺主体类型的具体描述：100-非流通股东，110-间接控股股东，150-流通股东，500-公司管理层。

### EventType (承诺事项类型)

承诺事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352 AND DM IN (71,72)，得到承诺事项类型的具体描述：71-新股上市股东承诺，72-上市后股东追加承诺。

### IfEffected (承诺是否有效)

承诺是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到承诺是否有效的具体描述：1-是，2-否。

### PromiseType (承诺类别)

承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306 AND DM IN (101,121)，得到承诺类别的具体描述：101-上市限售期限，121-延长锁定期。

### RestrictedState (限售状态(承诺时))

限售状态(承诺时)(RestrictedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1507，得到限售状态(承诺时)的具体描述：1-无限售，2-限售，3-限售+无限售。

## SQL示例

```sql
-- 查询 股东限售锁定期限承诺表 数据
SELECT *
FROM lc_restrictedpromise
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
