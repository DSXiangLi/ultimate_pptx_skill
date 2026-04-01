# LC_ZHSCQuotaInfo

**中文名**: 深港通额度信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ZHSCQuotaInfo` |
| MySQL表名 | `lc_zhscquotainfo` |
| 中文名 | 深港通额度信息 |
| 路径 | 聚源新版数据库 > 专题数据库 > 深港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1.01 |

## 表描述

1.收录深港通业务中，深股通和港深股通交易的每日额度及总额度信息。
2.历史数据：2016年12月起-至今
3.数据来源：聚源按照深交所、港交所披露整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and D... |
| 4 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM i... |
| 5 | `DailyQuota` | 每日额度(元) | number(19,4) | ✓ | 100.0% |  |
| 6 | `DailyBalance` | 每日额度余额(元) | number(19,4) | ✓ | 85.12% |  |
| 7 | `DailyUsed` | 每日已用额度(元) | number(18,2) | ✓ | 85.12% |  |
| 8 | `AccuUsed` | 累计已用额度(元) | number(18,2) | ✓ | 96.66% |  |
| 9 | `DailyBalanceRatio` | 每日额度余额占比(%) | number(18,2) | ✓ | 85.12% |  |
| 10 | `DailyUsedRatio` | 每日已用额度占比(%) | number(18,2) | ✓ | 85.12% |  |
| 11 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and DM IN (3,4)，得到交易类型的具体描述：3-深股通，4-港股通（深）。

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1100,1420)，得到货币单位的具体描述：1100-港元，1420-人民币元。

## SQL示例

```sql
-- 查询 深港通额度信息 数据
SELECT *
FROM lc_zhscquotainfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
