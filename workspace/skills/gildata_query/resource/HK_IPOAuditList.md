# HK_IPOAuditList

**中文名**: 港股企业上市审核表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IPOAuditList` |
| MySQL表名 | `hk_ipoauditlist` |
| 中文名 | 港股企业上市审核表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.记录拟上市公司审核信息，包括内容有：首次信息发布时间、事件进程、上市板块、刊发申请版本时间、刊发聆讯后资料集日期、失效时间、被拒绝时间、撤回时间、招股日期、上市日期、发回日期等。
2.数据范围：2013年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 证券代码 | number(10) | ✗ | 100.0% | 证券代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 4 | `Process` | 事件进程 | number(10) | ✗ | 100.0% | 事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1958，得到事件进程的具体... |
| 5 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM ... |
| 6 | `ListedSector` | 上市板块 | number(10) | ✗ | 100.0% | 上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207 and D... |
| 7 | `ApplProofsDate` | 刊发申请版本日期 | date | ✓ | 97.92% |  |
| 8 | `ApplPPHIPsDate` | 刊发聆讯后资料集日期 | date | ✓ | 39.72% |  |
| 9 | `ExpiryDate` | 失效日期 | date | ✓ | 50.15% |  |
| 10 | `RejectedDate` | 被拒绝日期 | date | ✓ | 1.11% |  |
| 11 | `WithdrawDate` | 撤回日期 | date | ✓ | 1.77% |  |
| 12 | `ProspectusDate` | 招股公告日期 | date | ✓ | 38.9% |  |
| 13 | `ListDate` | 上市日期 | date | ✓ | 38.27% |  |
| 14 | `ReturnDate` | 发回日期 | date | ✓ | 0.21% |  |
| 15 | `Remark` | 备注 | varchar2(2000) | ✓ | 2.72% |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券代码)

证券代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### Process (事件进程)

事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1958，得到事件进程的具体描述：1-已刊登申请版本，2-已刊登聆讯后资料集，3-失效，4-被拒绝，5-撤回，6-已上市，7-被发回，8-待上市。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM in (72)，得到证券市场的具体描述：72-香港联交所。

### ListedSector (上市板块)

上市板块(ListedSector)与(CT_SystemConst)表中的DM字段关联，令LB = 207 and DM in (1,6)，得到上市板块的具体描述：1-主板，6-创业板。

## SQL示例

```sql
-- 查询 港股企业上市审核表 数据
SELECT *
FROM hk_ipoauditlist
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
