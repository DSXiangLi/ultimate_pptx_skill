# LC_SHSZHSCIndTradeFlow

**中文名**: 沪(深)港通行业资金流向

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSZHSCIndTradeFlow` |
| MySQL表名 | `lc_shszhscindtradeflow` |
| 中文名 | 沪(深)港通行业资金流向 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 22 |
| 版本 | 1 |

## 表描述

1、内容说明：收录不同行业分类下沪(深)港通标的南北向资金变动信息，包括日频、周频、月频、季频、年频等区间统计信息。
2、数据范围：2017年3月起-至今
3、信息来源：聚源按照港交所披露衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 当TradingType=1时，表示陆股通行业资金流向；当TradingType=2时，表示港股通行业资金流向。 |
| 4 | `IndustryNum` | 行业内部编码 | number(10) | ✗ | 100.0% | 行业内部编码(IndustryNum)与(CT_IndustryType)表中的IndustryNum字段关联，令Ind... |
| 5 | `IndustryName` | 行业名称 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `IndustryCode` | 行业代码 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `Standard` | 行业划分标准 | number(10) | ✗ | 100.0% | 行业划分标准(Standard)与(CT_IndustryType)表中的Standard字段关联，22-证监会行业分类... |
| 8 | `SharesHolding` | 持股数量(股) | number(19,2) | ✓ | 100.0% |  |
| 9 | `MarketValue` | 持股市值(元) | number(19,2) | ✓ | 96.71% |  |
| 10 | `DailyNBV` | 日净流入额(元) | number(19,2) | ✓ | 96.67% |  |
| 11 | `DailyMRatioChange` | 日净流入额占行业市值比变化(%) | number(19,2) | ✓ | 95.06% |  |
| 12 | `WeeklyNBV` | 周净流入额(元) | number(19,2) | ✓ | 99.24% |  |
| 13 | `WeeklyMRatioChange` | 周净流入额占行业市值比变化(%) | number(19,2) | ✓ | 95.06% |  |
| 14 | `MonthlyNBV` | 月净流入额(元) | number(19,2) | ✓ | 99.96% |  |
| 15 | `MonthlyMRatioChange` | 月净流入额占行业市值比变化(%) | number(19,2) | ✓ | 95.06% |  |
| 16 | `QuarterlyNBV` | 季净流入额(元) | number(19,2) | ✓ | 99.96% |  |
| 17 | `QuarterlyMRatioChange` | 季净流入额占行业市值比变化(%) | number(19,2) | ✓ | 95.06% |  |
| 18 | `YearlyNBV` | 年净流入额(元) | number(19,2) | ✓ | 99.96% |  |
| 19 | `YearlyMRatioChange` | 年净流入额占行业市值比变化(%) | number(19,2) | ✓ | 95.06% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

当TradingType=1时，表示陆股通行业资金流向；当TradingType=2时，表示港股通行业资金流向。

### IndustryNum (行业内部编码)

行业内部编码(IndustryNum)与(CT_IndustryType)表中的IndustryNum字段关联，令IndustryNum=IndustryNum，得到行业内部编码的具体描述。

### Standard (行业划分标准)

行业划分标准(Standard)与(CT_IndustryType)表中的Standard字段关联，22-证监会行业分类2012版，37-中信行业2019分类，38-申万行业分类(新)，41-申万行业分类2021版

## SQL示例

```sql
-- 查询 沪(深)港通行业资金流向 数据
SELECT *
FROM lc_shszhscindtradeflow
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
