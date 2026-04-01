# HK_AdjustingFactor

**中文名**: 港股复权因子表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_AdjustingFactor` |
| MySQL表名 | `hk_adjustingfactor` |
| 中文名 | 港股复权因子表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 6 |
| 版本 | 1 |

## 表描述

1.收录聚源计算的港股复权因子数据，包含主要字段有：除净日、比例复权因子。
2.数据范围：1999年至今。
3.数据来源：恒生聚源。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `ExDate` | 除净日 | date | ✗ | 100.0% |  |
| 4 | `RatioAdjustingFactor` | 比例复权因子 | float | ✓ | 100.0% |  |
| 5 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 6 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股复权因子表 数据
SELECT *
FROM hk_adjustingfactor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
