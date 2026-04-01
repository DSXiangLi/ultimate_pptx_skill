# Bond_FRNRefRate

**中文名**: 浮息债基准利率表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_FRNRefRate` |
| MySQL表名 | `bond_frnrefrate` |
| 中文名 | 浮息债基准利率表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 滚动更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.记录所有浮动利率计息基准每日数据
2.数据范围：1987-01-02 至今
3.信息来源：人民银行、货币网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到计... |
| 3 | `FRNRefRateText` | 浮动利率计息基准 | number(10) | ✗ | 100.0% | 浮动利率计息基准(FRNRefRateText)：可与债券要素新表(Bond_BasicInfoN)的浮动利率计息基准(... |
| 4 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 5 | `FRNRefRate` | 基准利率(%) | number(19,8) | ✓ | 100.0% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到计息基准利率中文名称等

### FRNRefRateText (浮动利率计息基准)

浮动利率计息基准(FRNRefRateText)：可与债券要素新表(Bond_BasicInfoN)的浮动利率计息基准(FRNRefRateSelecrRemark)关联使用。与系统常量表中的DM字段关联，令LB = 1012 ，可得到浮动利率计息基准的具体描述。

## SQL示例

```sql
-- 查询 浮息债基准利率表 数据
SELECT *
FROM bond_frnrefrate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
