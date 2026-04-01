# LC_IncPlanExerDetails

**中文名**: 激励计划行权明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IncPlanExerDetails` |
| MySQL表名 | `lc_incplanexerdetails` |
| 中文名 | 激励计划行权明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定期更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

表说明：收录公告中披露的公司实行股权激励计划方案中各归属期的行权明细数据，主要包括行权对象名称、行权数量和行权价格等指标。
数据范围：2018-至今
信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `IncentivePlanEventCodeVA` | 激励计划事项编码(归属期) | varchar2(30) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `VestingPeriod` | 归属期 | number(10) | ✓ | 100.0% |  |
| 6 | `AwardAttribute` | 授予性质 | number(10) | ✗ | 100.0% | 授予性质(AwardAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 2583，得到... |
| 7 | `ExerciseObjectName` | 行权对象名称 | varchar2(40) | ✗ | 100.0% |  |
| 8 | `ExerciseObjectPosition` | 行权对象职务 | varchar2(40) | ✓ | 93.34% |  |
| 9 | `ExerciseVolume` | 行权数量(股) | number(19) | ✓ | 100.0% |  |
| 10 | `ExercisePrice` | 行权价格(元) | number(19,4) | ✓ | 99.05% |  |
| 11 | `ListingDate` | 上市流通日期 | date | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AwardAttribute (授予性质)

授予性质(AwardAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 2583，得到授予性质的具体描述：1-首次授予，2-预留授予，11-首次授予-第一批次，12-首次授予-第二批次，13-首次授予-第三批次，21-预留授予-第一批次，22-预留授予-第二批次，23-预留授予-第三批次。

## SQL示例

```sql
-- 查询 激励计划行权明细 数据
SELECT *
FROM lc_incplanexerdetails
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
