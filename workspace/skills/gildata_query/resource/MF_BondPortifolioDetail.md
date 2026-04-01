# MF_BondPortifolioDetail

**中文名**: 公募基金债券组合明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BondPortifolioDetail` |
| MySQL表名 | `mf_bondportifoliodetail` |
| 中文名 | 公募基金债券组合明细 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季度更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金债券组合中重仓的债券及处于转股期的可转换债券明细，包括债券代码、持有数量、持有市值、市值占净资产的比例等数据。
2.历史数据：2000年12月起-至今。
3.数据来源：基金公司披露的定期报告和上市交易公告书。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 7 | `BondCode` | 债券内部代码 | number(10) | ✓ | 100.0% | 债券内部代码（BondCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债... |
| 8 | `HoldVolume` | 持有数量(张) | number(18,4) | ✓ | 99.57% |  |
| 9 | `MarketValue` | 市值(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `RatioInNV` | 占资产净值比例 | number(18,6) | ✓ | 100.0% |  |
| 11 | `IfInConvertibleTerm` | 是否转股期可转债或ABS | number(3) | ✗ | 100.0% | 报告期末是否处于转股期（IfInConvertibleTerm），该字段固定以下常量：1-处于转股期的可转换债券；2-A... |
| 12 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 13 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### BondCode (债券内部代码)

债券内部代码（BondCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债券的交易代码、简称等。

### IfInConvertibleTerm (是否转股期可转债或ABS)

报告期末是否处于转股期（IfInConvertibleTerm），该字段固定以下常量：1-处于转股期的可转换债券；2-ABS；0-重仓债券投资明细（公告原始披露的排名中包含转股期可转债、ABS）

## SQL示例

```sql
-- 查询 公募基金债券组合明细 数据
SELECT *
FROM mf_bondportifoliodetail
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
