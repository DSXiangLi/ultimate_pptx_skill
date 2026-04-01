# Bond_ActiveBond

**中文名**: 债券活跃券表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ActiveBond` |
| MySQL表名 | `bond_activebond` |
| 中文名 | 债券活跃券表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

收录国债和国开债活跃券的相关信息，包括切换起始日、切换截止日、活跃天数、期间均价和发行总次数等信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `SecuCode` | 债券代码 | varchar2(10) | ✓ | 100.0% |  |
| 4 | `SecuAbbr` | 债券简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `ChangeStartDate` | 切换起始日 | date | ✗ | 100.0% |  |
| 6 | `ChangeEndDate` | 切换截止日 | date | ✓ | 98.21% |  |
| 7 | `PeriodDays` | 期间天数 | number(10) | ✓ | 100.0% |  |
| 8 | `PeriodAvgPrice` | 期间均价 | number(19,15) | ✓ | 100.0% |  |
| 9 | `PeriodHighPrice` | 期间最高 | number(19,15) | ✓ | 100.0% |  |
| 10 | `PeriodLowPrice` | 期间最低 | number(19,15) | ✓ | 100.0% |  |
| 11 | `IssueFrequency` | 发行总次数 | number(10) | ✓ | 100.0% |  |
| 12 | `ActualIssueSize` | 发行总规模(亿元) | number(19,6) | ✓ | 100.0% |  |
| 13 | `InterestTaxRate` | 利息税率(%) | number(19,8) | ✓ | 100.0% |  |
| 14 | `CouponRate` | 票面利率(%) | number(9,6) | ✓ | 100.0% |  |
| 15 | `ActiveType` | 活跃券类别 | number(10) | ✓ | 100.0% | 活跃券类别（ActiveType）：1-10年期国开债活跃券，2-10年期国债活跃券 |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### ActiveType (活跃券类别)

活跃券类别（ActiveType）：1-10年期国开债活跃券，2-10年期国债活跃券

## SQL示例

```sql
-- 查询 债券活跃券表 数据
SELECT *
FROM bond_activebond
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
