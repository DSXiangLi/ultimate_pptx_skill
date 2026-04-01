# Bond_RepoConversionStd

**中文名**: 债券回购折算比率表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_RepoConversionStd` |
| MySQL表名 | `bond_repoconversionstd` |
| 中文名 | 债券回购折算比率表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券回购信息 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.信息来源：中国证券登记结算公司。
2.收录中国证券登记结算公司根据《标准券折算率管理办法》，每周计算（或修正）的有关债券适用的最新标准券折算率。
3.数据范围：2000-12-27 至今
4.信息来源：中证登

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 债券到期日 | date | ✓ | 99.7% |  |
| 5 | `ExecuteStartDate` | 折算标准执行起始日 | date | ✓ | 100.0% |  |
| 6 | `ExecuteEndDate` | 折算标准执行截止日 | date | ✓ | 100.0% |  |
| 7 | `ParValue` | 债券面值(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `Coefficient` | 标准券折算率(每百元面值折算成标准券所乘的系数) | number(9,6) | ✓ | 100.0% |  |
| 9 | `StdBond` | 标准券(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到回购债券的证券代码、证券简称等。

## SQL示例

```sql
-- 查询 债券回购折算比率表 数据
SELECT *
FROM bond_repoconversionstd
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
