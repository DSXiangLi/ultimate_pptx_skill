# Bond_MuniSpread

**中文名**: 城投债利差表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_MuniSpread` |
| MySQL表名 | `bond_munispread` |
| 中文名 | 城投债利差表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 城投专题信息 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：整合中债估值以及相关曲线要素用于计算城投债的信用利差
2.数据范围：2019年9月4日至今
3.1信息来源：中债估值信息(全)Bond_CBValuationAll

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `MainCode` | 债券统一代码 | number(10) | ✓ | 100.0% |  |
| 4 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 5 | `TrueRemainMaturity` | 实际待偿期 | number(18,8) | ✓ | 100.0% |  |
| 6 | `Yield_GZ` | 国债曲线收益率 | number(18,10) | ✓ | 99.82% |  |
| 7 | `Spread_GZ` | 信用利差(国债基准)(%) | number(18,10) | ✓ | 99.82% |  |
| 8 | `Yield_GK` | 国开债曲线收益率 | number(18,10) | ✓ | 99.82% |  |
| 9 | `Spread_GK` | 信用利差(国开债基准)(%) | number(18,10) | ✓ | 99.82% |  |
| 10 | `CredibilityCode` | 可信度代码 | number(10) | ✗ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 11 | `YieldCode` | 收益率类型代码 | number(10) | ✓ | 100.0% | 收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益... |
| 12 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

### YieldCode (收益率类型代码)

收益率类型代码（YieldCode），该字段固定以下常量，通过“实际待偿期”来区分是否行权：1-行权收益率；2-到期收益率

## SQL示例

```sql
-- 查询 城投债利差表 数据
SELECT *
FROM bond_munispread
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
