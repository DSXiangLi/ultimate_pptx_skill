# MF_FundStyleAnalysis

**中文名**: 基金风格属性分析

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundStyleAnalysis` |
| MySQL表名 | `mf_fundstyleanalysis` |
| 中文名 | 基金风格属性分析 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

本表基于股票的风格属性指标，计算基金的风格属性，可用于定量判断衡量基金的风格。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `CalDate` | 计算日期 | date | ✓ | 100.0% |  |
| 5 | `ZGrowth` | 成长属性 | number(19,6) | ✓ | 100.0% |  |
| 6 | `ZValue` | 价值属性 | number(19,6) | ✓ | 100.0% |  |
| 7 | `ZGrowth_Value` | 成长价值属性 | number(19,6) | ✓ | 100.0% |  |
| 8 | `ZSize` | 规模属性 | number(19,6) | ✓ | 100.0% |  |
| 9 | `AVGMarketValue` | 持股日均市值(万元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 基金风格属性分析 数据
SELECT *
FROM mf_fundstyleanalysis
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
