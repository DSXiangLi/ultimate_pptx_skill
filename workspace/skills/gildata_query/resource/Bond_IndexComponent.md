# Bond_IndexComponent

**中文名**: 债券指数成份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IndexComponent` |
| MySQL表名 | `bond_indexcomponent` |
| 中文名 | 债券指数成份 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数成份构成 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录了市场上主要债券指数的成份债券构成情况，包含成份债券的所有历史入选日期、删除日期以及成份标志等信息。
2.历史数据：1996年7月至今
3.数据源：上海交易所、深圳交易所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“债券指数概况（Bond_IndexBasicInfo）”中的“指数内部代码（In... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 4 | `InDate` | 入选日期 | date | ✓ | 100.0% |  |
| 5 | `OutDate` | 剔除日期 | date | ✓ | 72.04% |  |
| 6 | `Flag` | 成份标志 | number(10) | ✓ | 100.0% | 成份标志(Flag)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,... |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“债券指数概况（Bond_IndexBasicInfo）”中的“指数内部代码（IndexCode）”关联，得到指数的代码、简称等。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到成份债券的交易代码、简称等。

### Flag (成份标志)

成份标志(Flag)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到成份标志的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 债券指数成份 数据
SELECT *
FROM bond_indexcomponent
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
