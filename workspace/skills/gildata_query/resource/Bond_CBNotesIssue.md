# Bond_CBNotesIssue

**中文名**: 央行票据发行

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_CBNotesIssue` |
| MySQL表名 | `bond_cbnotesissue` |
| 中文名 | 央行票据发行 |
| 路径 | 聚源新版数据库 > 债券数据库 > 央行公开市场操作 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1.03 |

## 表描述

1.收录中国人民银行公开市场业务操作中，历次央行票据发行情况。
2.数据范围：2002-06-25 至今
3.信息来源：中债登、中国人民银行

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `IssueDate` | 发行日 | date | ✓ | 100.0% |  |
| 4 | `IssueMethod` | 发行方式 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `ActualIssueSize` | 实际发行总额(亿元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `Maturity` | 债券期限(年) | number(5,2) | ✓ | 100.0% |  |
| 7 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `IssueRefYTM` | 参考收益率(%) | number(10,6) | ✓ | 99.9% |  |
| 9 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到央行票据的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 央行票据发行 数据
SELECT *
FROM bond_cbnotesissue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
