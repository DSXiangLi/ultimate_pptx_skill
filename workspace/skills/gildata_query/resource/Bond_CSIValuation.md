# Bond_CSIValuation

**中文名**: 中证债券估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CSIValuation` |
| MySQL表名 | `bond_csivaluation` |
| 中文名 | 中证债券估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中证代理数据库 > 中证估值 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.03 |

## 表描述

1.内容说明：收录对各类债券及优先股的估值数据
2.数据范围：2011-12-08 至今
3.信息来源：中证指数有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValueFullPrice` | 估价全价 | number(18,10) | ✓ | 100.0% |  |
| 5 | `VPYield` | 估价收益率(%) | number(18,12) | ✓ | 99.6% |  |
| 6 | `VPADuration` | 估价修正久期 | number(18,10) | ✓ | 99.6% |  |
| 7 | `VPConvexity` | 估价凸性 | number(18,10) | ✓ | 99.6% |  |
| 8 | `ValueCleanPrice` | 估价净价 | number(18,10) | ✓ | 100.0% |  |
| 9 | `ExpCouponRate` | 预期票面利率(%) | number(18,12) | ✓ | 7.96% |  |
| 10 | `DataMark` | 数据标志 | number(10) | ✓ | 74.48% | 数据标识（DataMark），该字段固定以下常量：1-行权；2-到期 |
| 11 | `CredibilityCode` | 可信度代码 | number(10) | ✓ | 74.48% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 12 | `AccruInterest` | 应计利息(元) | number(18,10) | ✓ | 100.0% |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；或与“优先股概况（PS_Archives）”中的“优先股代码（InnerCode）”关联，得到优先股的基本信息。

### DataMark (数据标志)

数据标识（DataMark），该字段固定以下常量：1-行权；2-到期

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

## SQL示例

```sql
-- 查询 中证债券估值 数据
SELECT *
FROM bond_csivaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
