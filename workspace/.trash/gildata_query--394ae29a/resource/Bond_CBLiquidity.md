# Bond_CBLiquidity

**中文名**: 中债流动性指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBLiquidity` |
| MySQL表名 | `bond_cbliquidity` |
| 中文名 | 中债流动性指标 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 估值附属指标 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中债估值中心发布的中债流动性指标
2.数据范围：2018年至今2021年，中债官方已于2021-12-8停止更新
3.信息来源：中债金融估值中心有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `AbLiqCoefficient` | 绝对流动性系数 | number(19,8) | ✓ | 100.0% |  |
| 5 | `PositionPercent` | 位置百分比(%) | number(19,8) | ✓ | 99.72% |  |
| 6 | `RelativeLiqCoefficient` | 相对流动性系数 | number(19,8) | ✓ | 100.0% |  |
| 7 | `RelativeLiqNum` | 相对流动性系数取值 | number(19,8) | ✓ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等；

## SQL示例

```sql
-- 查询 中债流动性指标 数据
SELECT *
FROM bond_cbliquidity
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
