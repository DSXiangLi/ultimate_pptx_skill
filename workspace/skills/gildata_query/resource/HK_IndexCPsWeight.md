# HK_IndexCPsWeight

**中文名**: 港股指数成份股权重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IndexCPsWeight` |
| MySQL表名 | `hk_indexcpsweight` |
| 中文名 | 港股指数成份股权重 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数权重信息 |
| 更新频率 | 日更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.收录了在港股市场上发布的主要指数成份证券的权重信息，通过与港股证券主表进行关联，可以获取指数以及成份股的基本信息。
2.历史数据：2015年2月至今
3.数据源：恒生指数有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）或 港股证券主表（HK_SecuMain）”中的“证... |
| 3 | `InnerCode` | 成份股内部编码 | number(10) | ✗ | 100.0% | 成份股内部编码（InnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<InnerCode<=100... |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `Weight` | 权重 | number(18,8) | ✗ | 100.0% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）或 港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (成份股内部编码)

成份股内部编码（InnerCode）：关联不同主表，查询证券代码、证券简称等基本信息。当0<InnerCode<=1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当1000000<InnerCode<=2000000时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联；当7000000<InnerCode<=10000000时，与“ 美股证券主表（US_SecuMain）”中的“证券内部编码（InnerCode）”关联

## SQL示例

```sql
-- 查询 港股指数成份股权重 数据
SELECT *
FROM hk_indexcpsweight
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
