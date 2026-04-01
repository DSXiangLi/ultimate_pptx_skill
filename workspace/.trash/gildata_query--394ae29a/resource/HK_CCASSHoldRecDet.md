# HK_CCASSHoldRecDet

**中文名**: 港股中央结算系统持股记录明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CCASSHoldRecDet` |
| MySQL表名 | `hk_ccassholdrecdet` |
| 中文名 | 港股中央结算系统持股记录明细 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.收录香港中央结算系统披露的持股记录详细信息，包括市场中介者、愿意披露的投资者户口持有人等的详细持股记录。每个结算日更新。
2.历史数据：2017-07至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `HoldingDate` | 持股日期 | date | ✗ | 100.0% |  |
| 4 | `PartiNumber` | 参与者编号 | varchar2(100) | ✓ | 99.99% | 参与者编号（PartiNumber）：与“港股联交所参与者名单(HK_SEHKPartiList)”中的“参与者编号(P... |
| 5 | `Shareholding` | 持股量 | number(19,2) | ✓ | 100.0% |  |
| 6 | `ShareholdingRatio` | 持股量占比 | number(19,8) | ✓ | 99.7% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到国内上市证券的交易代码、简称等。

### PartiNumber (参与者编号)

参与者编号（PartiNumber）：与“港股联交所参与者名单(HK_SEHKPartiList)”中的“参与者编号(PartiNumber)”关联，得到参与者的相关信息。

## SQL示例

```sql
-- 查询 港股中央结算系统持股记录明细 数据
SELECT *
FROM hk_ccassholdrecdet
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
