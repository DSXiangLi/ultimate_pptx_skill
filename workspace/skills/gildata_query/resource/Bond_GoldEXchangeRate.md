# Bond_GoldEXchangeRate

**中文名**: 黄金基准汇价

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_GoldEXchangeRate` |
| MySQL表名 | `bond_goldexchangerate` |
| 中文名 | 黄金基准汇价 |
| 路径 | 聚源新版数据库 > 产品代理 > 外汇交易中心（CFETS）代理数据库 > 外汇市场基准 |
| 更新频率 | 实时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录中国外汇交易中心发布的黄金基准汇价的数据，包括中间价、最高价、最低价。
2.数据范围：2021-04-01至今
3.信息来源：中国外汇交易中心

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 交易品种代码 | number(10) | ✗ | 100.0% |  |
| 4 | `TypeVarietyName` | 交易品种名称 | varchar2(100) | ✓ | 100.0% | AUX/CNY对应成色不低于99.95％的黄金交易标的，AUY/CNY对应成色不低于99.99％的黄金交易标的。交易单位... |
| 5 | `PeriodBegPrice` | 中间价(人民币元/克) | number(19,4) | ✓ | 100.0% |  |
| 6 | `HighestPrice` | 最高价(人民币元/克) | number(19,4) | ✓ | 100.0% |  |
| 7 | `LowestPrice` | 最低价(人民币元/克) | number(19,4) | ✓ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TypeVarietyName (交易品种名称)

AUX/CNY对应成色不低于99.95％的黄金交易标的，AUY/CNY对应成色不低于99.99％的黄金交易标的。交易单位为1.00克。

## SQL示例

```sql
-- 查询 黄金基准汇价 数据
SELECT *
FROM bond_goldexchangerate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
