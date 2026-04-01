# Bond_CBIndexComponent

**中文名**: 中债指数成份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBIndexComponent` |
| MySQL表名 | `bond_cbindexcomponent` |
| 中文名 | 中债指数成份 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债指数 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中央国债登记结算有限责任公司发布的指数成份券构成情况，包含成份券的入选日期、剔除日期、成份标志等信息
2.数据范围：2002年1月至今
3.信息来源：中央国债登记结算有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”... |
| 4 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 5 | `OutDate` | 剔除日期 | date | ✓ | 70.61% |  |
| 6 | `Flag` | 成份标志 | number(10) | ✗ | 100.0% | 成份标志（Flag），该字段固定以下常量：1-是；2-否 |
| 7 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (证券内部编码)

证券内部编码（SecuInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到成份券的代码、简称等。

### Flag (成份标志)

成份标志（Flag），该字段固定以下常量：1-是；2-否

## SQL示例

```sql
-- 查询 中债指数成份 数据
SELECT *
FROM bond_cbindexcomponent
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
