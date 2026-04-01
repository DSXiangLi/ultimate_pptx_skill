# CS_RiskAlert

**中文名**: 股票风险警示表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_RiskAlert` |
| MySQL表名 | `cs_riskalert` |
| 中文名 | 股票风险警示表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 滚动更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

记录股票被实施风险警示的开始时间和结束时间，包括其他风险警示，退市风险警示，叠加风险警示，暂停上市，特别转让，退市整理期等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `RiskAlertType` | 风险警示类型 | number(10) | ✗ | 100.0% | 风险警示类型(RiskAlertType）：1-ST， 2-暂停上市，3-PT，5-*ST，9-退市整理期，10-高风险... |
| 4 | `IfEntryRiskAlertBoard` | 是否进入风险警示板交易 | number(10) | ✓ | 45.06% | 是否进入风险警示板交易(IfEntryRiskAlertBoard)：1-是，2-否。 |
| 5 | `ImplAnnouceDate` | 实施公告日期 | date | ✓ | 100.0% |  |
| 6 | `ImplementDate` | 实施日期 | date | ✗ | 100.0% |  |
| 7 | `RemoveInfoPublDate` | 撤销公告日期 | date | ✓ | 90.99% |  |
| 8 | `RemoveDate` | 撤销日期 | date | ✓ | 90.99% |  |
| 9 | `ImplementReason` | 实施原因 | varchar2(2000) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### RiskAlertType (风险警示类型)

风险警示类型(RiskAlertType）：1-ST， 2-暂停上市，3-PT，5-*ST，9-退市整理期，10-高风险警示，12-叠加ST，14-叠加*ST。

### IfEntryRiskAlertBoard (是否进入风险警示板交易)

是否进入风险警示板交易(IfEntryRiskAlertBoard)：1-是，2-否。

## SQL示例

```sql
-- 查询 股票风险警示表 数据
SELECT *
FROM cs_riskalert
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
