# LC_STIBAdjustingFactor

**中文名**: 科创板复权因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBAdjustingFactor` |
| MySQL表名 | `lc_stibadjustingfactor` |
| 中文名 | 科创板复权因子 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录科创板股票因为分红、送转股、配股等发生除权除息，计算出比例复权因子，可用于推算股票前复权或后复权价格。
2.数据范围：证券上市起-至今
3.信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 4 | `AdjustingFactor` | 精确复权因子 | number(19,6) | ✗ | 100.0% |  |
| 5 | `AdjustingConst` | 精确复权常数 | number(19,6) | ✓ | 100.0% |  |
| 6 | `RatioAdjustingFactor` | 比例复权因子 | number(19,6) | ✓ | 100.0% |  |
| 7 | `AccuCashDivi` | 累计分红 | number(19,6) | ✓ | 100.0% |  |
| 8 | `AccuBonusShareRatio` | 累计送股 | number(19,6) | ✓ | 100.0% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 科创板复权因子 数据
SELECT *
FROM lc_stibadjustingfactor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
