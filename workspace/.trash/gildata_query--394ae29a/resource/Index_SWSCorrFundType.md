# Index_SWSCorrFundType

**中文名**: 申万基金指数与分类对应

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_SWSCorrFundType` |
| MySQL表名 | `index_swscorrfundtype` |
| 中文名 | 申万基金指数与分类对应 |
| 路径 | 聚源新版数据库 > 产品代理 > 申万代理数据库 > 申万指数 |
| 更新频率 | 不定时更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

内容说明：本表收录申万基金指数对应基金分类信息
数据范围：申万基金分类指数
信息来源：申万宏源证券研究所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)：与“证券主表(SecuMain)”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `Standard` | 分类标准 | number(10) | ✗ | 100.0% | 分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 AND DM I... |
| 4 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `CancelDate` | 取消日期 | date | ✓ | 0.0% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% |  |
| 7 | `FundTypeCode` | 聚源分类编码 | number(10) | ✗ | 100.0% | 聚源分类编码(FundTypeCode)与申万基金分类层级表(MF_SWSClassification)表中的FundT... |
| 8 | `FundTypeName` | 分类名称 | varchar2(200) | ✗ | 100.0% |  |
| 9 | `DisclosureCode` | 披露分类代码 | varchar2(20) | ✗ | 100.0% |  |
| 10 | `StandardLevel` | 分类级别 | number(10) | ✗ | 100.0% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)：与“证券主表(SecuMain)”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### Standard (分类标准)

分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1252 AND DM IN (91)，得到分类标准的具体描述：91-申万宏源公募基金基础分类。

### FundTypeCode (聚源分类编码)

聚源分类编码(FundTypeCode)与申万基金分类层级表(MF_SWSClassification)表中的FundTypeCode字段关联，令Standard=Standard，得到基金分类的具体描述；

## SQL示例

```sql
-- 查询 申万基金指数与分类对应 数据
SELECT *
FROM index_swscorrfundtype
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
