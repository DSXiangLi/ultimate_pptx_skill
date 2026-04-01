# HK_ExFundAdjustFactor

**中文名**: 香港上市基金复权因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_ExFundAdjustFactor` |
| MySQL表名 | `hk_exfundadjustfactor` |
| 中文名 | 香港上市基金复权因子 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

本表记录香港ETF基金由分红数据计算而来的复权因子数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 4 | `AdjustFactor` | 精确复权因子 | number(19,10) | ✓ | 100.0% |  |
| 5 | `AdjustingFactor` | 精确累积复权因子 | number(19,10) | ✓ | 100.0% |  |
| 6 | `AdjustConst` | 精确复权常数 | number(19,10) | ✓ | 100.0% |  |
| 7 | `AdjustingConst` | 精确累积复权常数 | number(19,10) | ✓ | 100.0% |  |
| 8 | `RatioAdjustingFactor` | 比例复权因子 | number(19,10) | ✓ | 98.93% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 香港上市基金复权因子 数据
SELECT *
FROM hk_exfundadjustfactor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
