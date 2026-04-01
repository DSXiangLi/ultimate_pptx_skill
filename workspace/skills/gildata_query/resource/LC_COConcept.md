# LC_COConcept

**中文名**: 概念所属公司表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_COConcept` |
| MySQL表名 | `lc_coconcept` |
| 中文名 | 概念所属公司表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司行业板块 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1.01 |

## 表描述

记录A股上市公司所属概念信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ConceptCode` | 概念代码 | number(10) | ✗ | 100.0% | 概念代码(ConceptCode)：与“概念板块表(LC_ConceptList)”中的“概念代码(ConceptCod... |
| 4 | `InDate` | 纳入日期 | date | ✗ | 100.0% |  |
| 5 | `OutDate` | 剔除日期 | date | ✓ | 93.53% |  |
| 6 | `IndiState` | 所属状态 | number(10) | ✗ | 100.0% | 所属状态(IndiState)，该字段固定以下常量：1-正常，0-终止。 |
| 7 | `Remark` | 备注 | varchar2(1000) | ✓ | 98.87% | 备注(Remark):字段解释了该成分股属于此概念的原因及逻辑。 |
| 8 | `InfoPublDate` | 发布时间 | date | ✗ | 100.0% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### ConceptCode (概念代码)

概念代码(ConceptCode)：与“概念板块表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。

### IndiState (所属状态)

所属状态(IndiState)，该字段固定以下常量：1-正常，0-终止。

### Remark (备注)

备注(Remark):字段解释了该成分股属于此概念的原因及逻辑。

## SQL示例

```sql
-- 查询 概念所属公司表 数据
SELECT *
FROM lc_coconcept
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
