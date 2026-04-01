# CS_AShareIPOWinning

**中文名**: A股发行与上市中签数据

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_AShareIPOWinning` |
| MySQL表名 | `cs_ashareipowinning` |
| 中文名 | A股发行与上市中签数据 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 滚动更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

该表记录A股发行新股时的中签数据

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `LastDigit` | 末尾位数 | number(10) | ✗ | 100.0% |  |
| 5 | `WinningNumber` | 中签的号码 | varchar2(200) | ✓ | 100.0% |  |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 A股发行与上市中签数据 数据
SELECT *
FROM cs_ashareipowinning
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
