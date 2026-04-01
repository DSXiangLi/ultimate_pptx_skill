# HK_RelADRTransRatio

**中文名**: 港股关联ADR转换比例

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_RelADRTransRatio` |
| MySQL表名 | `hk_reladrtransratio` |
| 中文名 | 港股关联ADR转换比例 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.内容说明：新建港股关联ADR转换比例表，记录港股的ADR和正股的转换比率信息。
2.数据范围：2004年至今。
3.信息来源：美国证券交易所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部代码（InnerCode）：与“美股证券主表（US_SecuMain）”中的“证券内部代码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 92.86% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 78.98% | 信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1968，得到信息来源... |
| 5 | `IssuePublDate` | 事项公布日期 | date | ✓ | 49.46% |  |
| 6 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 7 | `EndDate` | 终止日期 | date | ✓ | 41.25% |  |
| 8 | `DataBeforeChange` | 变更前数据 | number(24,6) | ✓ | 30.4% |  |
| 9 | `DataAfterChange` | 变更后数据 | number(24,6) | ✓ | 100.0% |  |
| 10 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)：1-是,2-否。 |
| 11 | `ChangeType` | 变动原因类别 | number(10) | ✓ | 0.0% |  |
| 12 | `ChangeReason` | 变动原因说明 | varchar2(500) | ✓ | 0.2% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部代码（InnerCode）：与“美股证券主表（US_SecuMain）”中的“证券内部代码（InnerCode）”关联，得到美股的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)与(CT_SystemConst)表中的DM字段关联，令LB = 1968，得到信息来源的具体描述：2-一季报，3-中期报告，4-第三季报，5-年度报告，6-第二季报，7-第四季报，8-三季报，9-报告期调整，15-定期报告，16-临时公告，17-招股说明书，18-招股说明书（更正），19-更正报告，20-发行上市后续说明，30-累计报告，31-季度报告，32-更正年度报告，33-TTM报告，90-其他公告。

### IfEffected (是否有效)

是否有效(IfEffected)：1-是,2-否。

## SQL示例

```sql
-- 查询 港股关联ADR转换比例 数据
SELECT *
FROM hk_reladrtransratio
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
