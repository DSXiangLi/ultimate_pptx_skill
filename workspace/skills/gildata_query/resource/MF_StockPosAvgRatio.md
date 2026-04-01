# MF_StockPosAvgRatio

**中文名**: 公募基金股票持仓平均占比

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_StockPosAvgRatio` |
| MySQL表名 | `mf_stockposavgratio` |
| 中文名 | 公募基金股票持仓平均占比 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 季更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.内容说明：公募基金股票持仓占基金资产净值的比例及变化情况，包括周期内股票平均占比、股票占比波动率。
2.数据范围：1999年6月起-至今
3.信息来源：根据周期内基金所有季报披露的股票资产占基金资产净值比例，通过算术平均、标准差计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 5 | `RatioInNVIn1y` | 近一年股票占比 | number(18,6) | ✓ | 100.0% |  |
| 6 | `StockPosStdIn1y` | 近一年标准差 | number(18,6) | ✓ | 94.9% |  |
| 7 | `RatioInNVIn2y` | 近两年股票占比 | number(18,6) | ✓ | 100.0% |  |
| 8 | `StockPosStdIn2y` | 近两年标准差 | number(18,6) | ✓ | 95.07% |  |
| 9 | `RatioInNVIn3y` | 近三年股票占比 | number(18,6) | ✓ | 100.0% |  |
| 10 | `StockPosStdIn3y` | 近三年标准差 | number(18,6) | ✓ | 95.13% |  |
| 11 | `RatioInNVIn5y` | 近五年股票占比 | number(18,6) | ✓ | 100.0% |  |
| 12 | `StockPosStdIn5y` | 近五年标准差 | number(18,6) | ✓ | 95.15% |  |
| 13 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。


## SQL示例

```sql
-- 查询 公募基金股票持仓平均占比 数据
SELECT *
FROM mf_stockposavgratio
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
