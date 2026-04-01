# HK_EX_Stock

**中文名**: 港股评级

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_EX_Stock` |
| MySQL表名 | `hk_ex_stock` |
| 中文名 | 港股评级 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股盈利预测 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：本表统计各研究机构对港股上市公司流通股票的评级情况
2.数据范围：2020年至今数据
3.信息来源：FactSet

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `StatPeriod` | 统计周期(天) | number(10) | ✓ | 100.0% | 统计周期(天)（StatPeriod）：该字段固定常量：100-100天 |
| 5 | `BuyNum` | 买入评级机构数 | number(10) | ✓ | 100.0% |  |
| 6 | `AddNum` | 增持评级机构数 | number(10) | ✓ | 100.0% |  |
| 7 | `NeutralNum` | 中性评级机构数 | number(10) | ✓ | 100.0% |  |
| 8 | `ReduceNum` | 减持评级机构数 | number(10) | ✓ | 100.0% |  |
| 9 | `SellNum` | 卖出评级机构数 | number(10) | ✓ | 100.0% |  |
| 10 | `RatingNum` | 评级总机构数 | number(10) | ✓ | 100.0% |  |
| 11 | `StandardScore` | 评级标准分 | number(19,8) | ✓ | 100.0% |  |
| 12 | `NoRatingOrg` | 未予评级机构数 | number(10) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### StatPeriod (统计周期(天))

统计周期(天)（StatPeriod）：该字段固定常量：100-100天

## SQL示例

```sql
-- 查询 港股评级 数据
SELECT *
FROM hk_ex_stock
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
