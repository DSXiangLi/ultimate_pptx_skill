# LC_IndexPrepComponent

**中文名**: 指数备选成份

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndexPrepComponent` |
| MySQL表名 | `lc_indexprepcomponent` |
| 中文名 | 指数备选成份 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数成份构成 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.主要收录了上交所上海证券交易所和中证指数公司发布的部分指数的备选成份证券名单信息，包括生效日期、备选顺序。
2.历史数据：2007年1月至今
3.数据源：中证指数有限公司、上海证券交易所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `RankNo` | 备选顺序 | number(10) | ✓ | 100.0% |  |
| 6 | `InnerCode` | 备选成份股内部编码 | number(10) | ✗ | 100.0% | 备选成分股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (备选成份股内部编码)

备选成分股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到备选成份股的交易代码、简称等。

## SQL示例

```sql
-- 查询 指数备选成份 数据
SELECT *
FROM lc_indexprepcomponent
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
