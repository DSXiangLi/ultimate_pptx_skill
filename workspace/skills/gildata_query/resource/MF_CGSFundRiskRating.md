# MF_CGSFundRiskRating

**中文名**: 公募基金评级-银河证券基金分类风险等级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_CGSFundRiskRating` |
| MySQL表名 | `mf_cgsfundriskrating` |
| 中文名 | 公募基金评级-银河证券基金分类风险等级 |
| 路径 | 聚源新版数据库 > 产品代理 > 基金评级代理数据库 |
| 更新频率 | 月更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.本表记录银河证券按月提供的基金分类风险等级信息。
2.历史数据：2017年7月起-至今。
3.数据来源：聚源按照源原始披露整理。
4.授权提示：此表需要额外拿到银河证券的授权才能使用。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TypeCode` | 分类代码 | number(10) | ✗ | 100.0% |  |
| 4 | `FundTypeName` | 分类名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `RiskLevelCodeLvI` | 风险等级编码(一级) | varchar2(20) | ✓ | 100.0% |  |
| 6 | `RiskLevelNameLvI` | 风险等级名称(一级) | number(10) | ✓ | 100.0% | 风险等级名称（一级）(RiskLevelNameLvI)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 7 | `RiskLevelCodeLvII` | 风险等级编码(二级) | varchar2(20) | ✓ | 100.0% |  |
| 8 | `RiskLevelNameLvII` | 风险等级名称(二级) | number(10) | ✓ | 100.0% | 风险等级名称（二级）(RiskLevelNameLvII)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 9 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 10 | `CancelDate` | 取消日期 | date | ✓ | 47.32% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### RiskLevelNameLvI (风险等级名称(一级))

风险等级名称（一级）(RiskLevelNameLvI)与(CT_SystemConst)表中的DM字段关联，令LB = 2079，得到风险等级名称（一级）的具体描述：1-低风险; 2-中低风险; 3-中风险; 4-中高风险; 5-高风险.

### RiskLevelNameLvII (风险等级名称(二级))

风险等级名称（二级）(RiskLevelNameLvII)与(CT_SystemConst)表中的DM字段关联，令LB = 2079，得到风险等级名称（二级）的具体描述：11-低风险-1；12-低风险-2；13-低风险-3；14-低风险-4；15-低风险-5，等

## SQL示例

```sql
-- 查询 公募基金评级-银河证券基金分类风险等级 数据
SELECT *
FROM mf_cgsfundriskrating
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
