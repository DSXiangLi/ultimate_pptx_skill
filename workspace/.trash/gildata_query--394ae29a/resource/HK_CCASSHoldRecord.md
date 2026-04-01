# HK_CCASSHoldRecord

**中文名**: 港股中央结算系统持股记录

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CCASSHoldRecord` |
| MySQL表名 | `hk_ccassholdrecord` |
| 中文名 | 港股中央结算系统持股记录 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1.02 |

## 表描述

1.收录香港中央结算系统披露的持股记录信息，包括市场中介者、愿意披露的投资者户口持有人等的持股记录。每个结算日更新。
2.历史数据：2017-07至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `HoldingDate` | 持股日期 | date | ✗ | 100.0% |  |
| 4 | `IntermedPartiAmount` | 市场中介者参与者数目 | number(10) | ✓ | 100.0% |  |
| 5 | `IntermedShareholding` | 市场中介者持股量 | number(19,2) | ✓ | 100.0% |  |
| 6 | `IntermedShareProp` | 市场中介者持股量百分比 | number(19,8) | ✓ | 99.78% |  |
| 7 | `ConInvPartiAmount` | 愿意披露的投资者户口持有人数目 | number(10) | ✓ | 11.15% |  |
| 8 | `ConInvShareholding` | 愿意披露的投资者户口持有人持股量 | number(19,2) | ✓ | 11.15% |  |
| 9 | `ConInvShareProp` | 愿意披露的投资者户口持有人持股量百分比 | number(19,8) | ✓ | 11.13% |  |
| 10 | `NonConInvPartiAmount` | 不愿意披露的投资者户口持有人数目 | number(10) | ✓ | 52.41% |  |
| 11 | `NonConInvShareholding` | 不愿意披露的投资者户口持有人持股量 | number(19,2) | ✓ | 52.41% |  |
| 12 | `NonConInvShareProp` | 不愿意披露的投资者户口持有人持股量百分比 | number(19,8) | ✓ | 52.25% |  |
| 13 | `PartiAmount` | 参与者总数目 | number(10) | ✓ | 100.0% |  |
| 14 | `Shareholding` | 参与者总持股量 | number(19,2) | ✓ | 100.0% |  |
| 15 | `ShareProp` | 参与者总持股量百分比 | number(19,8) | ✓ | 99.78% |  |
| 16 | `IssuedShares` | 已发行股份 | number(19,2) | ✓ | 100.0% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联,得到证券的交易代码、简称等。国内上市证券与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股中央结算系统持股记录 数据
SELECT *
FROM hk_ccassholdrecord
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
