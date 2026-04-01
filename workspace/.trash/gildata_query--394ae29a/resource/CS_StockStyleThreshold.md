# CS_StockStyleThreshold

**中文名**: 境内股票风格分类门限值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockStyleThreshold` |
| MySQL表名 | `cs_stockstylethreshold` |
| 中文名 | 境内股票风格分类门限值 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 不定期更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

内容说明：收录境内A股股票风格分类门限值用于判断股票风格属性或规模属性
数据范围：2000-05至今
信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `LargeStockThreshold` | 大盘股门限值 | number(19,6) | ✓ | 100.0% |  |
| 5 | `MidStockThreshold` | 中盘股门限值 | number(19,6) | ✓ | 100.0% |  |
| 6 | `GrowthStockThreshold` | 成长型门限值 | number(19,6) | ✓ | 100.0% |  |
| 7 | `ValueStockThreshold` | 价值型门限值 | number(19,6) | ✓ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 境内股票风格分类门限值 数据
SELECT *
FROM cs_stockstylethreshold
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
