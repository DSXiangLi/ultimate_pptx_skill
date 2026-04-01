# MF_NetValueReDeExt

**中文名**: 公募基金复权净值(去极值)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NetValueReDeExt` |
| MySQL表名 | `mf_netvalueredeext` |
| 中文名 | 公募基金复权净值(去极值) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金净值 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：记录巨额赎回调整后的复权净值。
2.数据范围：1990年1月起-至今。
3.信息来源：根据基金公司官网披露的净值数据和巨额赎回公告计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `UnitNV` | 单位净值 | number(18,6) | ✗ | 100.0% |  |
| 5 | `GrowthRateFactor` | 复权因子 | number(18,15) | ✓ | 91.1% |  |
| 6 | `DeExtFactor` | 巨额赎回修正因子 | number(18,15) | ✓ | 0.98% |  |
| 7 | `IfOutlier` | 是否极值 | number(10) | ✓ | 100.0% | 是否极值(IfOutlier)：1--是；0--否 |
| 8 | `GrowthRateFactorR` | 修正后复权因子 | number(18,15) | ✓ | 100.0% |  |
| 9 | `UnitNVRestored` | 复权单位净值 | number(18,6) | ✗ | 100.0% |  |
| 10 | `NVRDailyGrowthRate` | 复权单位净值日增长率(%) | number(18,9) | ✓ | 99.91% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfOutlier (是否极值)

是否极值(IfOutlier)：1--是；0--否

## SQL示例

```sql
-- 查询 公募基金复权净值(去极值) 数据
SELECT *
FROM mf_netvalueredeext
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
