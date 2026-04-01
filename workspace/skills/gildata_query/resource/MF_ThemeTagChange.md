# MF_ThemeTagChange

**中文名**: 公募基金概念标签变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ThemeTagChange` |
| MySQL表名 | `mf_themetagchange` |
| 中文名 | 公募基金概念标签变动 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 风格标签 > 风格标签2.0 |
| 更新频率 | 周更新 |
| 字段数量 | 20 |
| 版本 | 1.03 |

## 表描述

1.内容说明：记录偏股型基金的最新概念主题（二级、三级）标签及变动。三级概念比如无人驾驶、网红直播、雄安新区等。对应的二级概念比如新科技、新模式、区域协调发展等。目前包含360+个三级概念标签，60+二级概念标签。概念常量参见<概念板块常量表  LC_ConceptList>。应用场景为，XX时间范围内，将XX基金的实际投资风格匹配XX热点概念标签。
2.数据范围：2019年4月-至今。
3.信息来源：A股新增概念的主要逻辑有新概念涉及标的个数情况、概念爆发日个股强度等。概念成分股的调入调出逻辑主要包括基本面和资金面。热点概念的成分股参见<概念所属公司表  LC_COConcept>。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode)：当ClassLevel=3，与“概念板块常量表(LC_ConceptList)”中的... |
| 4 | `TagThreshold` | 标签阈值 | number(18,9) | ✓ | 100.0% | 标签阈值(TagThreshold)：0.1--区间在【0.1,0.2）；0.2--区间在【0.2,0.5）；0.5--... |
| 5 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 6 | `ClassLevel` | 标签概念级别 | number(10) | ✓ | 100.0% | 标签概念级别(ClassLevel)：2--2级；3--3级 |
| 7 | `FundTagName` | 标签名称 | varchar2(500) | ✗ | 100.0% |  |
| 8 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter): 1-重仓股；2-全部持仓 |
| 9 | `StartDate` | 启用日期 | date | ✗ | 100.0% |  |
| 10 | `EndDate` | 停用日期 | date | ✓ | 98.4% |  |
| 11 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效（IfEffected）：1-是，2-否 |
| 12 | `Relationship` | 关联类型 | number(10) | ✗ | 100.0% | 关联类型(Relationship): 1-聚源股票概念板块 |
| 13 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 14 | `ClassCode` | 所属1级概念代码 | number(10) | ✓ | 100.0% | 所属1级概念代码（ClassCode)：与“概念板块常量表(LC_ConceptList)”中的“所属1级概念代码（Cl... |
| 15 | `ClassName` | 所属1级概念名称 | varchar2(100) | ✓ | 100.0% |  |
| 16 | `SubclassCode` | 所属2级概念代码 | number(10) | ✓ | 100.0% | 所属2级概念代码（SubclassCode): 与“概念板块常量表(LC_ConceptList)”中的“所属2级概念代... |
| 17 | `SubclassName` | 所属2级概念名称 | varchar2(100) | ✓ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundTagCode (标签代码)

标签代码(FundTagCode)：当ClassLevel=3，与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联；当ClassLevel=2，与“概念板块常量表(LC_ConceptList)”中的“	所属2级概念代码(SubclassCode)”关联，得到所属概念的信息。

### TagThreshold (标签阈值)

标签阈值(TagThreshold)：0.1--区间在【0.1,0.2）；0.2--区间在【0.2,0.5）；0.5--区间在【0.5,1）。

### ClassLevel (标签概念级别)

标签概念级别(ClassLevel)：2--2级；3--3级

### PosCharacter (持仓类型)

持仓类型(PosCharacter): 1-重仓股；2-全部持仓

### IfEffected (是否有效)

是否有效（IfEffected）：1-是，2-否

### Relationship (关联类型)

关联类型(Relationship): 1-聚源股票概念板块

### ClassCode (所属1级概念代码)

所属1级概念代码（ClassCode)：与“概念板块常量表(LC_ConceptList)”中的“所属1级概念代码（ClassCode)”关联，得到所属概念的信息。

### SubclassCode (所属2级概念代码)

所属2级概念代码（SubclassCode): 与“概念板块常量表(LC_ConceptList)”中的“所属2级概念代码（SubclassCode)”关联，得到所属概念的信息。

## SQL示例

```sql
-- 查询 公募基金概念标签变动 数据
SELECT *
FROM mf_themetagchange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
