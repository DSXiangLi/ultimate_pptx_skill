# Bond_ConBDValuation

**中文名**: 中债可转债估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDValuation` |
| MySQL表名 | `bond_conbdvaluation` |
| 中文名 | 中债可转债估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债估值中心对可转债和可交换债估值数据。
2.数据范围：2023-09-22 至今
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValueFullPrice` | 估价全价(元) | number(18,8) | ✓ | 100.0% |  |
| 5 | `ValueCleanPrice` | 估价净价(元) | number(18,8) | ✓ | 99.35% |  |
| 6 | `OptionValue` | 期权价值(元) | number(18,8) | ✓ | 99.22% |  |
| 7 | `ConversionValue` | 转股价值(元) | number(18,8) | ✓ | 99.22% |  |
| 8 | `ConversionPremium` | 转股溢价率(%) | number(18,8) | ✓ | 99.22% |  |
| 9 | `BondPremium` | 纯债溢价率(%) | number(18,8) | ✓ | 99.23% |  |
| 10 | `BondFloorFullPrice` | 债底全价(元) | number(18,8) | ✓ | 100.0% |  |
| 11 | `BondFloorCleanPrice` | 债底净价(元) | number(18,8) | ✓ | 99.35% |  |
| 12 | `AccruedInterest` | 应计利息(元) | number(18,8) | ✓ | 99.35% |  |
| 13 | `BondFloorYTM` | 债底收益率(%) | number(18,8) | ✓ | 99.35% |  |
| 14 | `ModifiedDuration` | 债底修正久期 | number(18,8) | ✓ | 99.35% |  |
| 15 | `Convexity` | 债底凸性 | number(18,8) | ✓ | 99.35% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 中债可转债估值 数据
SELECT *
FROM bond_conbdvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
