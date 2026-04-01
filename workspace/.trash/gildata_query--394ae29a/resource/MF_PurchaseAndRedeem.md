# MF_PurchaseAndRedeem

**中文名**: 公募基金申赎状态

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PurchaseAndRedeem` |
| MySQL表名 | `mf_purchaseandredeem` |
| 中文名 | 公募基金申赎状态 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.本表记录基金当前日期的申购赎回等状态情况。只针对全渠道的状态变更，如果状态变更只是针对某些特定的销售渠道，则不会影响总体基金的状态。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的产品说明书及相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到发... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `RedeemType` | 赎回状态 | varchar2(100) | ✓ | 100.0% | 赎回状态(RedeemType)：包括认购期，封闭期，可赎回，不可赎回，终止 |
| 5 | `ApplyingType` | 申购状态 | varchar2(100) | ✓ | 100.0% | 申购状态(ApplyingType)：包括认购期，封闭期，可申购，限大额，不可申购，终止 |
| 6 | `LargeApplyingMax` | 基金大额申购上限(元) | number(19,2) | ✓ | 12.39% | 基金大额申购上限（LargeApplyingMax）：该字段处理为大额申购上限数据。 |
| 7 | `IfInsideTrade` | 是否场内交易 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到发生上市状态变更证券的交易代码、交易简称等。

### RedeemType (赎回状态)

赎回状态(RedeemType)：包括认购期，封闭期，可赎回，不可赎回，终止

### ApplyingType (申购状态)

申购状态(ApplyingType)：包括认购期，封闭期，可申购，限大额，不可申购，终止

### LargeApplyingMax (基金大额申购上限(元))

基金大额申购上限（LargeApplyingMax）：该字段处理为大额申购上限数据。

## SQL示例

```sql
-- 查询 公募基金申赎状态 数据
SELECT *
FROM mf_purchaseandredeem
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
