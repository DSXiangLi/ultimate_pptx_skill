# CS_RaiseFundsUse

**中文名**: 股票募集资金用途

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_RaiseFundsUse` |
| MySQL表名 | `cs_raisefundsuse` |
| 中文名 | 股票募集资金用途 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定期更新 |
| 字段数量 | 24 |
| 版本 | 1 |

## 表描述

1. 内容说明：收录公司通过发行新股、增发新股、配股、优先股等方式所得募集资金的项目投资情况以及运用进展和改投状况。
2. 数据范围：2020/11/30至今
3. 信息来源：交易所公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `InitialInfoPublDate` | 募资首次信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `RaisingMethod` | 募资方式 | number(10) | ✗ | 100.0% | 募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2593 AND D... |
| 7 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM... |
| 8 | `PlannedProceeds` | 预计募集资金总额(元) | number(19,4) | ✓ | 92.8% |  |
| 9 | `ActualProceeds` | 实际募集资金总额(元) | number(19,4) | ✓ | 94.75% |  |
| 10 | `IssueCost` | 发行费用总额(元) | number(19,4) | ✓ | 93.75% |  |
| 11 | `ActualNetProceeds` | 实际募集资金净额(元) | number(19,4) | ✓ | 94.63% |  |
| 12 | `ProjectSN` | 项目序号 | varchar2(40) | ✗ | 100.0% |  |
| 13 | `ProjectName` | 项目名称 | varchar2(1000) | ✓ | 100.0% |  |
| 14 | `ProjectBriefIntroText` | 项目简介 | clob | ✓ | 100.0% |  |
| 15 | `ProjectPeriod` | 项目周期(月) | number(19,4) | ✓ | 50.1% |  |
| 16 | `ProjectPlannedSum` | 项目计划投入金额总额 | number(19,4) | ✓ | 99.59% |  |
| 17 | `PlannedProceedsAfterRaise` | 募资后项目计划投入募集金额(元) | number(19,4) | ✓ | 98.19% |  |
| 18 | `AccuSum` | 募集资金累计投入金额(元) | number(19,4) | ✓ | 75.12% |  |
| 19 | `EndDate` | 募集资金累计投入截止日 | date | ✓ | 77.59% |  |
| 20 | `IfChange` | 是否变更 | number(10) | ✓ | 100.0% | 是否变更(IfChange)：1-是，2-否。 |
| 21 | `ChangeReason` | 变更原因 | clob | ✓ | 47.56% |  |
| 22 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 23 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### RaisingMethod (募资方式)

募资方式(RaisingMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2593 AND DM IN (1,2,3,4,5,6)，得到募资方式的具体描述：1-首发，2-公开增发，3-非公开增发，4-非公开增发配套融资，5-配股，6-优先股发行。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM IN (1000,1100,1420) ，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### IfChange (是否变更)

是否变更(IfChange)：1-是，2-否。

## SQL示例

```sql
-- 查询 股票募集资金用途 数据
SELECT *
FROM cs_raisefundsuse
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
