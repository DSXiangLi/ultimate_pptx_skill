# LC_IncentivePlanImplement

**中文名**: 激励计划实施

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IncentivePlanImplement` |
| MySQL表名 | `lc_incentiveplanimplement` |
| 中文名 | 激励计划实施 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.04 |

## 表描述

1.收录上市公司激励计划的实施结果信息，包括实施日期、激励权益数量、兑换比例、激励股票数量、激励价格、激励金额等指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `IncentivePlanEventCode` | 激励计划事项编码 | varchar2(30) | ✓ | 100.0% |  |
| 5 | `IncentiveMode` | 激励模式代码 | number(10) | ✗ | 100.0% | 激励模式代码(IncentiveMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1400，得... |
| 6 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 7 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 8 | `EffectiveStartDate` | 实施起始日期 | date | ✓ | 75.46% |  |
| 9 | `EffectiveDate` | 实施日期 | date | ✗ | 100.0% |  |
| 10 | `RightsNum` | 激励权益数量(万份) | number(18,9) | ✓ | 20.73% |  |
| 11 | `ShareRatio` | 兑换比例(1份:X股) | number(18,9) | ✓ | 20.73% |  |
| 12 | `SharesNum` | 激励股票数量(万股) | number(18,9) | ✓ | 99.21% |  |
| 13 | `IncentiveStockProportion` | 激励股本占总股本比例(%) | number(18,9) | ✓ | 98.92% |  |
| 14 | `IncentivePrice` | 激励价格(元) | number(19,4) | ✓ | 98.49% |  |
| 15 | `IncentiveSum` | 激励金额(万元) | number(18,9) | ✓ | 0.79% |  |
| 16 | `ChangeStatement` | 变动原因类别 | number(10) | ✓ | 0.0% | 变动原因类别(ChangeStatement)与(CT_SystemConst)表中的DM字段关联，令LB = 1323... |
| 17 | `ChangeType` | 变动原因说明 | varchar2(200) | ✓ | 0.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。

### IncentiveMode (激励模式代码)

激励模式代码(IncentiveMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1400，得到激励模式代码的具体描述：10-限制性股票，11-第一类限制性股票，12-第二类限制性股票，13-业绩股票，15-管理层持股，21-股票期权，23-股票增值权，25-虚拟股票，31-激励基金，90-未明确，99-其他。

### ChangeStatement (变动原因类别)

变动原因类别(ChangeStatement)与(CT_SystemConst)表中的DM字段关联，令LB = 1323 AND DM IN (1,2,3,31,33,35)，得到变动原因类别的具体描述：1-标的派现，2-标的送转，3-标的送转派，31-方案变更，33-激励基金购股，35-方案实施。

## SQL示例

```sql
-- 查询 激励计划实施 数据
SELECT *
FROM lc_incentiveplanimplement
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
