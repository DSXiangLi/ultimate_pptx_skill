# DZ_AdjustingFactor

**中文名**: 复权因子表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AdjustingFactor` |
| MySQL表名 | `dz_adjustingfactor` |
| 中文名 | 复权因子表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股票行情 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：收录股票、基金、债券等因为分红配股发生除权除息，衍生计算出的复权因子、复权常数、比例复权因子等指标，可用于推算股票前复权或后复权价格。
2.数据范围:证券上市起-至今
3.信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `AdjustingFactor` | 精确复权因子 | number(19,6) | ✓ | 100.0% |  |
| 5 | `AdjustingConst` | 精确复权常数 | number(19,6) | ✓ | 100.0% |  |
| 6 | `RatioAdjustingFactor` | 比例复权因子 | number(19,6) | ✓ | 100.0% |  |
| 7 | `AccuCashDivi` | 累计分红 | number(19,8) | ✓ | 96.94% |  |
| 8 | `AccuBonusShareRatio` | 累计送股 | number(19,8) | ✓ | 96.94% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 复权因子表 数据
SELECT *
FROM dz_adjustingfactor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
