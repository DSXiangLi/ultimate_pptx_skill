# Index_SWSFundCW

**中文名**: 申万基金指数成份权重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_SWSFundCW` |
| MySQL表名 | `index_swsfundcw` |
| 中文名 | 申万基金指数成份权重 |
| 路径 | 聚源新版数据库 > 产品代理 > 申万代理数据库 > 申万指数 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录申万公募基金分类指数权重数据。
2.历史数据：2022年6月30日至今
3.数据源：申万宏源证券研究所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InnerCode` | 成份股内部编码 | number(10) | ✗ | 100.0% | 成份股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `WeightedRatio` | 权重(%) | number(19,8) | ✓ | 100.0% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称。

### InnerCode (成份股内部编码)

成份股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，获取成分证券的代码、简称等信息。

## SQL示例

```sql
-- 查询 申万基金指数成份权重 数据
SELECT *
FROM index_swsfundcw
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
