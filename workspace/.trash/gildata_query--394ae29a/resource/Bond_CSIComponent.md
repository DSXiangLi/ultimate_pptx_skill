# Bond_CSIComponent

**中文名**: 中证债券指数成份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CSIComponent` |
| MySQL表名 | `bond_csicomponent` |
| 中文名 | 中证债券指数成份 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数成份构成 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.收录了中证指数有限公司发布的中证债券指数的成份债券构成情况，包含成份债券的所有历史入选日期、删除日期以及成份标志等信息。
2.历史数据：2012年8月至今
3.数据来源：聚源根据源数据推算而得

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：当SecuMarket=83、90或89时，与“证券主表（SecuMain）”中的“... |
| 4 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 5 | `OutDate` | 剔除日期 | date | ✓ | 67.71% |  |
| 6 | `Flag` | 成份标志 | number(10) | ✗ | 100.0% | 成份标志（Flag）：该字段采用固定常量：1->是    0->否 |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：当SecuMarket=83、90或89时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当SecuMarket=72时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联。

### Flag (成份标志)

成份标志（Flag）：该字段采用固定常量：1->是    0->否

## SQL示例

```sql
-- 查询 中证债券指数成份 数据
SELECT *
FROM bond_csicomponent
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
