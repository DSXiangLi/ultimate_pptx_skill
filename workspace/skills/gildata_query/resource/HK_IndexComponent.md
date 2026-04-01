# HK_IndexComponent

**中文名**: 港股指数成份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IndexComponent` |
| MySQL表名 | `hk_indexcomponent` |
| 中文名 | 港股指数成份 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数成份构成 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录了在港股市场上发布的主要指数的成份构成情况，包括成份证券的所有历史入选日期、删除日期以及成份标志等信息。
2.历史数据：1964年7月至今
3.数据源：恒生指数有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexInnerCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexInnerCode)与(SecuMain)表中的InnerCode字段关联，令IndexInne... |
| 3 | `SecuInnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（SecuInnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<SecuInnerCo... |
| 4 | `InDate` | 入选日期 | date | ✓ | 100.0% |  |
| 5 | `OutDate` | 剔除日期 | date | ✓ | 42.21% |  |
| 6 | `Flag` | 成份标志 | number(10) | ✗ | 100.0% | 成份标志(Flag)，该字段固定以下常量：1-是；0-否 |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexInnerCode (指数内部编码)

指数内部编码(IndexInnerCode)与(SecuMain)表中的InnerCode字段关联，令IndexInnerCode = InnerCode，得到指数内部编码的具体描述：

### SecuInnerCode (证券内部编码)

证券内部编码（SecuInnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<SecuInnerCode<=1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当1000000<SecuInnerCode<=2000000时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联；当7000000<SecuInnerCode<=10000000时，与“ 美股证券主表（US_SecuMain）”中的“证券内部编码（InnerCode）”关联

### Flag (成份标志)

成份标志(Flag)，该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 港股指数成份 数据
SELECT *
FROM hk_indexcomponent
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
