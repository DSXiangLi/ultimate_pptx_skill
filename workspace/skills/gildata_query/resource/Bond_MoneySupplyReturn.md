# Bond_MoneySupplyReturn

**中文名**: 基础货币投放与回笼

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_MoneySupplyReturn` |
| MySQL表名 | `bond_moneysupplyreturn` |
| 中文名 | 基础货币投放与回笼 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.收录基础货币的投放与回笼明细数据，具体包含逆回购、MLF、TMLF、国库现金定存四个品种。
2.数据范围：2002-02-19至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `Name` | 品种 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `CurrencyType` | 货币品种代码 | number(10) | ✗ | 100.0% | 货币品种代码(CurrencyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2480，得到... |
| 5 | `CurrencyTypeDesc` | 货币品种名称 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `Maturity` | 期限 | number(10) | ✗ | 100.0% |  |
| 7 | `Amount` | 金额(亿元) | number(19,8) | ✓ | 100.0% |  |
| 8 | `Rate` | 利率(%) | number(9,6) | ✓ | 60.81% |  |
| 9 | `Direction` | 资金流向 | number(10) | ✗ | 100.0% | 资金流向(Direction)与(CT_SystemConst)表中的DM字段关联，令LB = 2479，得到资金流向的... |
| 10 | `IssueDate` | 对应投放日期 | date | ✓ | 61.08% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CurrencyType (货币品种代码)

货币品种代码(CurrencyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2480，得到货币品种代码的具体描述：1-逆回购，2-中期借贷便利(MLF)，3-定向中期借贷便利(TMLF)，4-国库现金定存。

### Direction (资金流向)

资金流向(Direction)与(CT_SystemConst)表中的DM字段关联，令LB = 2479，得到资金流向的具体描述：1-投放，2-回笼，3-当日净投放。

## SQL示例

```sql
-- 查询 基础货币投放与回笼 数据
SELECT *
FROM bond_moneysupplyreturn
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
