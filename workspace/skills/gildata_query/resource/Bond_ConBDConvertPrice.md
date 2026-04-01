# Bond_ConBDConvertPrice

**中文名**: 可转债转股价格变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDConvertPrice` |
| MySQL表名 | `bond_conbdconvertprice` |
| 中文名 | 可转债转股价格变动 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.包含可转换债券转股价的历次变动情况。
2.数据范围：1992-11-01 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.96% |  |
| 5 | `ValidDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `ConvertPrice` | 转股价(元/股) | number(19,4) | ✓ | 100.0% |  |
| 7 | `ChangeReason` | 变更原因 | varchar2(100) | ✓ | 78.45% | 变更原因（ChangeReason）：用于区分转股价格变动的原因，具体原因包含：增发、派现、配股、送转股、股票价格、其他... |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### ChangeReason (变更原因)

变更原因（ChangeReason）：用于区分转股价格变动的原因，具体原因包含：增发、派现、配股、送转股、股票价格、其他。可通过关键字筛选特定转股价格变动原因，当存在多个原因导致的转股价格变动时，会将变动原因拼接展示。

## SQL示例

```sql
-- 查询 可转债转股价格变动 数据
SELECT *
FROM bond_conbdconvertprice
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
