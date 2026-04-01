# Bond_CBYieldCurveOpen

**中文名**: 中债债券收益率曲线(公开)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBYieldCurveOpen` |
| MySQL表名 | `bond_cbyieldcurveopen` |
| 中文名 | 中债债券收益率曲线(公开) |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债收益率曲线 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：收录中登公司发布的可以公开下载债券收益率曲线信息，目前只包括标准待偿期的中债国债收益率曲线（到期）。
2.数据范围：2002-01-04 至今
3.信息来源：中央国债登记结算有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `CurveType` | 收益率曲线 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `CurveCode` | 收益率曲线代码 | number(10) | ✓ | 100.0% | 收益率曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1448 AND ... |
| 5 | `YieldType` | 收益率类型 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `YieldTypeCode` | 收益率类型代码 | number(10) | ✓ | 100.0% | 收益率类型代码(YieldTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1449，... |
| 7 | `StepType` | 步长类型 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `StepTypeCode` | 步长类型代码 | number(10) | ✓ | 100.0% | 步长类型代码(StepTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1550，得到... |
| 9 | `YearsToMaturity` | 待偿期 | number(18,4) | ✓ | 100.0% |  |
| 10 | `Yield` | 收益率 | number(18,8) | ✓ | 100.0% |  |
| 11 | `N` | N(年) | number(18,4) | ✓ | 100.0% |  |
| 12 | `K` | K(年) | number(18,4) | ✓ | 100.0% |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurveCode (收益率曲线代码)

收益率曲线代码(CurveCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1448 AND DM = 10，得到收益率曲线代码的具体描述：10-中债国债收益率曲线。

### YieldTypeCode (收益率类型代码)

收益率类型代码(YieldTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1449，得到收益率类型代码的具体描述：1-到期，2-即期，3-远期的到期，4-远期的即期，5-远期。

### StepTypeCode (步长类型代码)

步长类型代码(StepTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1550，得到步长类型代码的具体描述：1-步长0.1，2-步长0.2，3-步长0.5，4-步长1，5-步长0.01，99-标准待偿期，100-任意待偿期。

## SQL示例

```sql
-- 查询 中债债券收益率曲线(公开) 数据
SELECT *
FROM bond_cbyieldcurveopen
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
