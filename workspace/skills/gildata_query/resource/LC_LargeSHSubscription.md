# LC_LargeSHSubscription

**中文名**: 配股大股东认配状况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_LargeSHSubscription` |
| MySQL表名 | `lc_largeshsubscription` |
| 中文名 | 配股大股东认配状况 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1.02 |

## 表描述

1.收录配股实施过程中大股东的认配状况，如全额实物认配、部分现金认配等内容。
2.数据范围：1993-03-29至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部代码 | number(10) | ✗ | 100.0% |  |
| 3 | `InitialInfoPublDate` | 首次信息发布时间 | date | ✗ | 100.0% |  |
| 4 | `SHSN` | 股东序号 | number(10) | ✓ | 100.0% |  |
| 5 | `SHName` | 股东名称 | varchar2(120) | ✓ | 100.0% |  |
| 6 | `SHID` | 股东ID | number(10) | ✓ | 86.28% |  |
| 7 | `SubscriptionWay` | 认配方式 | number(10) | ✓ |  |  |
| 8 | `OughtShares` | 应配股数(股) | number(16,0) | ✓ | 97.72% |  |
| 9 | `ActualShares` | 实配股数(股) | number(16,0) | ✓ | 65.67% |  |
| 10 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 配股大股东认配状况 数据
SELECT *
FROM lc_largeshsubscription
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
