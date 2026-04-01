# HK_SuspendResump

**中文名**: 港股停复牌表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SuspendResump` |
| MySQL表名 | `hk_suspendresump` |
| 中文名 | 港股停复牌表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股停复牌表，记录港股停牌时间以及对于的复牌时间。
2.数据范围：2004年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoSource` | 信息来源 | varchar2(20) | ✓ | 100.0% |  |
| 4 | `SuspendTime` | 停牌时间 | varchar2(20) | ✗ | 100.0% |  |
| 5 | `SuspendReason` | 停牌原因 | varchar2(500) | ✓ | 100.0% |  |
| 6 | `ResumptionTime` | 复牌时间 | varchar2(20) | ✓ | 97.13% |  |
| 7 | `ResumptionReason` | 复牌原因 | varchar2(500) | ✓ | 97.13% |  |
| 8 | `SuspendTerm` | 停牌天数 | number(10) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股停复牌表 数据
SELECT *
FROM hk_suspendresump
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
