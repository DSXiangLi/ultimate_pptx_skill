# LC_STIBCodeChange

**中文名**: 科创板证券代码变更

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCodeChange` |
| MySQL表名 | `lc_stibcodechange` |
| 中文名 | 科创板证券代码变更 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：收录科创板证券代码的历次变更情况，包括启用日期和停用日期等内容
2.数据范围：科创板上市至今
3.信息来源：招股说明书、上市公告书、临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，取... |
| 3 | `SecuCodeBefore` | 变更前证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 4 | `SecuCodeAfter` | 变更后证券代码 | varchar2(20) | ✓ | 100.0% |  |
| 5 | `StartDate` | 启用日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 停用日期 | date | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，取“上市板块(ListedSector)”=7-科创板，得到科创板上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 科创板证券代码变更 数据
SELECT *
FROM lc_stibcodechange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
