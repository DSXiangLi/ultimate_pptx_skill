# LC_SHSCQuotaInfo

**中文名**: 沪港通额度信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SHSCQuotaInfo` |
| MySQL表名 | `lc_shscquotainfo` |
| 中文名 | 沪港通额度信息 |
| 路径 | 聚源新版数据库 > 专题数据库 > 沪港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.01 |

## 表描述

1.收录沪港通业务中，沪股通和港沪股通交易的每日额度及总额度信息。
2.历史数据：2014年11月起-至今
3.数据来源：聚源按照上交所、港交所披露整理
2016年8月15日后，交易所不再限制总额度，总额度相关字段值为NULL

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型（TradingType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=... |
| 4 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM I... |
| 5 | `AggregateQuota` | 总额度(元) | number(18,2) | ✓ | 15.89% |  |
| 6 | `AggregateBalance` | 总额余额(元) | number(18,2) | ✓ | 15.89% |  |
| 7 | `DailyQuota` | 每日额度(元) | number(18,2) | ✓ | 100.0% |  |
| 8 | `DailyBalance` | 每日额度余额(元) | number(18,2) | ✓ | 87.86% |  |
| 9 | `DailyUsed` | 每日已用额度(元) | number(18,2) | ✓ | 87.86% |  |
| 10 | `AccuUsed` | 累计已用额度(元) | number(18,2) | ✓ | 100.0% |  |
| 11 | `DailyBalanceRatio` | 每日额度余额占比(%) | number(18,2) | ✓ | 87.86% |  |
| 12 | `DailyUsedRatio` | 每日已用额度占比(%) | number(18,2) | ✓ | 87.86% |  |
| 13 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

交易类型（TradingType）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令“LB=1844” and DM in (1,2)，得到具体的交易类型。1-沪股通 2-港股通(沪)

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1100,1420)，得到货币单位的具体描述：1100-港元，1420-人民币元。

## SQL示例

```sql
-- 查询 沪港通额度信息 数据
SELECT *
FROM lc_shscquotainfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
