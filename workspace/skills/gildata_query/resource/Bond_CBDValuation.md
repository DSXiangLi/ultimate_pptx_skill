# Bond_CBDValuation

**中文名**: 中债违约资产估值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBDValuation` |
| MySQL表名 | `bond_cbdvaluation` |
| 中文名 | 中债违约资产估值 |
| 路径 | 聚源新版数据库 > 产品代理 > 中债代理数据库 > 中债估值 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明: 收录每个交易日中债违约资产估值的数据
2.数据范围：2017-12-25至今
3.信息来源：中央国债登记结算有限责任公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% |  |
| 3 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 4 | `ValuePrice` | 估值价格 | number(18,8) | ✓ | 100.0% |  |
| 5 | `FloorRefPrice` | 参考价格区间下限 | number(18,8) | ✓ | 34.3% |  |
| 6 | `CapRefPrice` | 参考价格区间上限 | number(18,8) | ✓ | 34.3% |  |
| 7 | `CredibilityCode` | 可信度代码 | number(10) | ✗ | 100.0% | 可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐 |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CredibilityCode (可信度代码)

可信度代码（CredibilityCode），该字段固定以下常量：1-推荐；2-不推荐

## SQL示例

```sql
-- 查询 中债违约资产估值 数据
SELECT *
FROM bond_cbdvaluation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
