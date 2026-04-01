# HK_RiskStockList

**中文名**: 港股风险个股名单表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_RiskStockList` |
| MySQL表名 | `hk_riskstocklist` |
| 中文名 | 港股风险个股名单表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：新建港股风险个股名单表，记录有潜在风险的个股。
2.数据范围：2000年至今。
3.信息来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `RiskType` | 风险类型 | number(10) | ✗ | 100.0% | 风险类型(RiskType)：10-存在过合股行为；20-存在超50%股份增长；30-存在过超20%折让配售；40-近两... |
| 4 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 5 | `LastTime` | 最近一次日期 | date | ✓ | 49.8% |  |
| 6 | `OutDate` | 剔除日期 | date | ✓ | 30.56% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)：1-是；2-否 |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### RiskType (风险类型)

风险类型(RiskType)：10-存在过合股行为；20-存在超50%股份增长；30-存在过超20%折让配售；40-近两年净利润为负

### IfEffected (是否有效)

是否有效(IfEffected)：1-是；2-否

## SQL示例

```sql
-- 查询 港股风险个股名单表 数据
SELECT *
FROM hk_riskstocklist
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
