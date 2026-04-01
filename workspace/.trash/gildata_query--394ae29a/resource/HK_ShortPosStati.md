# HK_ShortPosStati

**中文名**: 港股淡仓统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_ShortPosStati` |
| MySQL表名 | `hk_shortposstati` |
| 中文名 | 港股淡仓统计 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 周更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1.记录香港证监会披露的指明股份合计需申报淡仓的统计数据。
2.数据范围：2012年8月至今。
3.数据来源：香港证监会。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `AggRepShortPos` | 申报空仓总股数(股) | number(18,2) | ✓ | 100.0% |  |
| 5 | `AggRepShortMoney` | 申报空仓总金额(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=... |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CurrencyUnit (货币单位)

货币单位（CurrencyUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“货币单位”描述。
       1000-美元，1100-港元，1320-新加坡元，1420-人民币元，3030-英镑

## SQL示例

```sql
-- 查询 港股淡仓统计 数据
SELECT *
FROM hk_shortposstati
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
