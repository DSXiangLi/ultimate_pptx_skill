# HK_StoDiscInf

**中文名**: 港股披露权益信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_StoDiscInf` |
| MySQL表名 | `hk_stodiscinf` |
| 中文名 | 港股披露权益信息 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.记录港股披露权益的基础信息，包括股份类型、持有人名称、持有性质、事件日期、持有人知悉日期等数据内容。该表为港股披露权益系列表的主表。
2.数据范围：1997年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `Companyode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 3 | `CompanyName` | 公司名称 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `InnerCode` | 港股内部代码 | number(10) | ✗ | 100.0% | 港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 5 | `SecuCode` | 证券代码 | varchar2(10) | ✓ | 100.0% |  |
| 6 | `ShareCategory` | 股份类型 | varchar2(200) | ✓ | 99.9% |  |
| 7 | `IssuedShares` | 已发行股份(股) | number(18,2) | ✓ | 100.0% |  |
| 8 | `ChiHolderName` | 持有人姓名 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `HolderCharacter` | 持有人性质 | number(10) | ✗ | 100.0% | 持有人性质(HolderCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1700，... |
| 10 | `EventDate` | 事件日期 | date | ✗ | 100.0% |  |
| 11 | `HolderNotcDate` | 持有人知悉日期 | date | ✓ | 24.49% |  |
| 12 | `SN` | 序号 | number(10) | ✗ | 100.0% |  |
| 13 | `Status` | 信息状态 | number(10) | ✓ | 42.31% | 信息状态(Status)与(CT_SystemConst)表中的DM字段关联，令LB=2285，得到信息状态的具体描述：... |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (港股内部代码)

港股内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### HolderCharacter (持有人性质)

持有人性质(HolderCharacter)与(CT_SystemConst)表中的DM字段关联，令LB = 1700，得到持有人性质的具体描述：101-董事，102-大股东，103-其他（含最高行政人員），104-个人大股东，105-法团大股东，106-董事-上市法团股份，107-董事-相联法团股份，108-董事-上市法团债券证，109-董事-相联法团债券证。

### Status (信息状态)

信息状态(Status)与(CT_SystemConst)表中的DM字段关联，令LB=2285，得到信息状态的具体描述：1-被取替，2-被撤回，3-修订，4-正常，99-其他。

## SQL示例

```sql
-- 查询 港股披露权益信息 数据
SELECT *
FROM hk_stodiscinf
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
