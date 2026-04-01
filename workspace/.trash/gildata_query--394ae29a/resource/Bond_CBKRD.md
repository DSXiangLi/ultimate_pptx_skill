# Bond_CBKRD

**中文名**: 中债关键利率久期表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBKRD` |
| MySQL表名 | `bond_cbkrd` |
| 中文名 | 中债关键利率久期表 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 28 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录为所有债券估值提供的中债KRD对应的O/N， 1M， 2M， 3M， 6M， 9M， 1Y， 2Y， 3Y， 4Y， 5Y， 6Y， 7Y， 8Y， 9Y， 10Y， 15Y， 20Y， 30Y，40Y， 50Y共21个关键期限点的关键利率久期值。
2.数据范围：2021年4月30日至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 估值日期 | date | ✗ | 100.0% |  |
| 4 | `YearsToMaturity` | 待偿期(年) | number(18,6) | ✗ | 100.0% |  |
| 5 | `ZeroYear` | O/N | number(18,6) | ✓ | 100.0% |  |
| 6 | `OneMonth` | 1M | number(18,6) | ✓ | 100.0% |  |
| 7 | `TwoMonth` | 2M | number(18,6) | ✓ | 100.0% |  |
| 8 | `ThreeMonth` | 3M | number(18,6) | ✓ | 100.0% |  |
| 9 | `SixMonth` | 6M | number(18,6) | ✓ | 100.0% |  |
| 10 | `NineMonth` | 9M | number(18,6) | ✓ | 100.0% |  |
| 11 | `OneYear` | 1Y | number(18,6) | ✓ | 100.0% |  |
| 12 | `TwoYear` | 2Y | number(18,6) | ✓ | 100.0% |  |
| 13 | `ThreeYear` | 3Y | number(18,6) | ✓ | 100.0% |  |
| 14 | `FourYear` | 4Y | number(18,6) | ✓ | 100.0% |  |
| 15 | `FiveYear` | 5Y | number(18,6) | ✓ | 100.0% |  |
| 16 | `SixYear` | 6Y | number(18,6) | ✓ | 100.0% |  |
| 17 | `SevenYear` | 7Y | number(18,6) | ✓ | 100.0% |  |
| 18 | `EightYear` | 8Y | number(18,6) | ✓ | 100.0% |  |
| 19 | `NineYear` | 9Y | number(18,6) | ✓ | 100.0% |  |
| 20 | `TenYear` | 10Y | number(18,6) | ✓ | 100.0% |  |
| 21 | `FifteenYear` | 15Y | number(18,6) | ✓ | 100.0% |  |
| 22 | `TwentyYear` | 20Y | number(18,6) | ✓ | 100.0% |  |
| 23 | `ThirtyYear` | 30Y | number(18,6) | ✓ | 100.0% |  |
| 24 | `FortyYear` | 40Y | number(18,6) | ✓ | 100.0% |  |
| 25 | `FiftyYear` | 50Y | number(18,6) | ✓ | 100.0% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 中债关键利率久期表 数据
SELECT *
FROM bond_cbkrd
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
