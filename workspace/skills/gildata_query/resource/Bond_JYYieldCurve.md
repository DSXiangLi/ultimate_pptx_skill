# Bond_JYYieldCurve

**中文名**: 聚源债券收益率曲线

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_JYYieldCurve` |
| MySQL表名 | `bond_jyyieldcurve` |
| 中文名 | 聚源债券收益率曲线 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.本表记录聚源基于债券实时行情和报价编制的债券收益率曲线。
2.发布频率：二级市场收益率曲线为截止每个银行间交易日的10点,11点, 13点, 14点, 15点, 16点, 17点, 20点30分后各更新一根实时曲线；一级市场收益率曲线为每日盘后更新。
2.数据范围：2022-01-01 至今
3.信息来源：模型计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `CurveType` | 收益率曲线 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `CurveCode` | 收益率曲线代码 | varchar2(20) | ✗ | 100.0% | 收益率曲线代码(CurveCode)：JY00000001-聚源国债收益率曲线 |
| 5 | `YieldType` | 收益率类型 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `YieldTypeCode` | 收益率类型代码 | number(10) | ✗ | 100.0% | 收益率类型代码(YieldTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1449 ... |
| 7 | `MarketType` | 市场类型 | number(10) | ✗ | 100.0% | 市场类型(MarketType)与(CT_SystemConst)表中的DM字段关联，令LB = 2412，得到市场类型... |
| 8 | `StepType` | 步长类型 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `StepTypeCode` | 步长类型代码 | number(10) | ✗ | 100.0% | 步长类型代码(StepTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1550 AN... |
| 10 | `YearsToMaturity` | 待偿期(年) | number(18,4) | ✗ | 100.0% |  |
| 11 | `Yield` | 收益率(%) | number(18,8) | ✓ | 100.0% |  |
| 12 | `N` | N(年) | number(18,4) | ✗ | 100.0% | N(年)(N)：该字段为预留字段，适用于远期收益率曲线。 |
| 13 | `K` | K(年) | number(18,4) | ✗ | 100.0% | K(年)(K)：该字段为预留字段，适用于远期收益率曲线。 |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (收益率曲线代码)

收益率曲线代码(CurveCode)：JY00000001-聚源国债收益率曲线

### YieldTypeCode (收益率类型代码)

收益率类型代码(YieldTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1449 AND DM IN (1,2)，得到收益率类型代码的具体描述：1-到期，2-即期。

### MarketType (市场类型)

市场类型(MarketType)与(CT_SystemConst)表中的DM字段关联，令LB = 2412，得到市场类型的具体描述：1-一级市场，2-二级市场。

### StepTypeCode (步长类型代码)

步长类型代码(StepTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1550 AND DM IN (1,5,99)，得到步长类型代码的具体描述：1-步长0.1，5-步长0.01，99-标准待偿期。

### N (N(年))

N(年)(N)：该字段为预留字段，适用于远期收益率曲线。

### K (K(年))

K(年)(K)：该字段为预留字段，适用于远期收益率曲线。

## SQL示例

```sql
-- 查询 聚源债券收益率曲线 数据
SELECT *
FROM bond_jyyieldcurve
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
