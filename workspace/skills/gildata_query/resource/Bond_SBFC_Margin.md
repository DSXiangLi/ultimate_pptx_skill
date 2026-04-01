# Bond_SBFC_Margin

**中文名**: 标准债券远期保证金率

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SBFC_Margin` |
| MySQL表名 | `bond_sbfc_margin` |
| 中文名 | 标准债券远期保证金率 |
| 路径 | 聚源新版数据库 > 债券数据库 > 标准债券远期合约 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上海清算所披露的标准债券远期的保证金率、交割月保证金率和交割月超仓保证金率
2.信息来源：上海清算所
2.数据范围：2024-04-22 至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `ContractInnerCode` | 合约内部编码 | number(10) | ✗ | 100.0% | 合约内部编码（ContractInnerCode）：与“标准债券远期合约基本信息（Bond_SBFC_Info）”中的“... |
| 4 | `MarginRatio` | 保证金率 | number(19,8) | ✓ | 100.0% |  |
| 5 | `DeliMonthMarginRatio` | 交割月保证金率 | number(19,8) | ✓ | 60.12% |  |
| 6 | `DeliMonthOpMarginRatio` | 交割月超仓保证金率 | number(19,8) | ✓ | 60.12% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ContractInnerCode (合约内部编码)

合约内部编码（ContractInnerCode）：与“标准债券远期合约基本信息（Bond_SBFC_Info）”中的“合约内部编码（ContractInnerCode）”关联，得到该合约的基础信息。

## SQL示例

```sql
-- 查询 标准债券远期保证金率 数据
SELECT *
FROM bond_sbfc_margin
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
