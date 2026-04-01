# Bond_AccruedInterest

**中文名**: 债券应计利息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_AccruedInterest` |
| MySQL表名 | `bond_accruedinterest` |
| 中文名 | 债券应计利息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.记录各类债券在每个交易日的债券应计利息信息。
2.数据范围：1986-07-01 至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `ValueDatePer` | 计息起始日 | date | ✓ | 100.0% |  |
| 4 | `DatePer` | 计息日期 | date | ✓ | 100.0% |  |
| 5 | `AccruedInterest` | 每百元应计利息(元)(8位应计利息) | number(18,8) | ✓ | 100.0% |  |
| 6 | `AccruedInterest12B` | 每百元应计利息(元)(12位应计利息) | number(18,12) | ✓ | 100.0% |  |
| 7 | `AccruedDays` | 计息天数 | number(10) | ✓ | 100.0% |  |
| 8 | `CouponRate` | 本年度利率(%) | number(18,6) | ✓ | 84.68% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 债券应计利息 数据
SELECT *
FROM bond_accruedinterest
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
