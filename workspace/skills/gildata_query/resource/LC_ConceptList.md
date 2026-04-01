# LC_ConceptList

**中文名**: 概念板块常量表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ConceptList` |
| MySQL表名 | `lc_conceptlist` |
| 中文名 | 概念板块常量表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 不定时更新 |
| 字段数量 | 15 |
| 版本 | 1.02 |

## 表描述

记录A股市场中热点概念的相关信息

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ClassCode` | 所属1级概念代码 | number(10) | ✗ | 100.0% |  |
| 3 | `ClassName` | 所属1级概念名称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `SubclassCode` | 所属2级概念代码 | number(10) | ✗ | 100.0% |  |
| 5 | `SubclassName` | 所属2级概念名称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `ConceptCode` | 概念代码 | number(10) | ✗ | 100.0% |  |
| 7 | `ConceptName` | 概念名称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `BeginDate` | 生成日期 | date | ✗ | 100.0% |  |
| 9 | `EndDate` | 终止日期 | date | ✓ | 28.07% |  |
| 10 | `ConceptState` | 所属状态 | number(10) | ✗ | 100.0% | 所属状态(ConceptState)，该字段固定以下常量：1-正常，0-终止。 |
| 11 | `Remark` | 备注 | varchar2(500) | ✓ | 79.01% |  |
| 12 | `InfoPublDate` | 发布时间 | date | ✗ | 100.0% |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |
| 15 | `ConceptEngName` | 概念英文名称 | varchar2(100) | ✓ | 89.87% |  |

## 字段说明

### ConceptState (所属状态)

所属状态(ConceptState)，该字段固定以下常量：1-正常，0-终止。

## SQL示例

```sql
-- 查询 概念板块常量表 数据
SELECT *
FROM lc_conceptlist
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
