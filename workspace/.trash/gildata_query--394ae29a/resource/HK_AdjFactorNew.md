# HK_AdjFactorNew

**中文名**: 港股复权因子(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_AdjFactorNew` |
| MySQL表名 | `hk_adjfactornew` |
| 中文名 | 港股复权因子(新) |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1.04 |

## 表描述

1.港股复权因子表数据主要基于三部分数据计算而得，港股分红、港股发行与上市、港股并股拆股。                                                                               2.本表已处理的情况包括，送股,分红送股，配股(也即供股)，并股拆股；本表处理的特殊情况如实物派送、红利认股证、以股代息等不涉及股本变动的情况，会结合行情表除权的数据进行更新。
3.对于货币单位问题。均以除权除息日30日内的平均汇率作为计算依据换算为交易货币。
4.数据范围：1999年至今。
5.数据来源：恒生聚源。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 4 | `AdjustingFactor` | 精确累积复权因子 | number(19,10) | ✓ | 100.0% |  |
| 5 | `AdjustingConst` | 精确累积复权常数 | number(19,10) | ✓ | 100.0% |  |
| 6 | `AdjustFactor` | 精确复权因子 | number(19,10) | ✓ | 100.0% |  |
| 7 | `AdjustConst` | 精确复权常数 | number(19,10) | ✓ | 100.0% |  |
| 8 | `RatioAdjustingFactor` | 比例复权因子 | number(19,10) | ✓ | 100.0% |  |
| 9 | `InformationMine` | 信息地雷 | varchar2(500) | ✓ | 100.0% |  |
| 10 | `EXDIfSusp` | 除权日是否停牌 | number(10) | ✓ | 100.0% | 除权日是否停牌（EXDIfSusp）：1-是，2-否。 |
| 11 | `NextResupDate` | 下一个复牌日期 | date | ✓ | 0.81% |  |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### EXDIfSusp (除权日是否停牌)

除权日是否停牌（EXDIfSusp）：1-是，2-否。

## SQL示例

```sql
-- 查询 港股复权因子(新) 数据
SELECT *
FROM hk_adjfactornew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
