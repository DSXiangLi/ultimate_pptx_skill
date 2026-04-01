# LC_ZHSCActiveShares

**中文名**: 深港通成交活跃股

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ZHSCActiveShares` |
| MySQL表名 | `lc_zhscactiveshares` |
| 中文名 | 深港通成交活跃股 |
| 路径 | 聚源新版数据库 > 专题数据库 > 深港通数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1.01 |

## 表描述

1.内容说明：收录深港通交易每日/月前十大成交活跃股票信息。
2.数据范围：2016年12月起-至今
3.信息来源：聚源按照深交所、港交所披露整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 3 | `TradingType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and D... |
| 4 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码(InnerCode)：当TradingType=3时，与“证券主表(SecuMain)”中的“证券内部编码... |
| 5 | `SecuCode` | 证券代码 | varchar2(10) | ✓ | 100.0% | 证券代码（SecuCode）为公告原文中披露的证券代码 |
| 6 | `Ranking` | 排名 | number(10) | ✓ | 100.0% |  |
| 7 | `Currency` | 货币单位 | number(10) | ✓ | 100.0% | 货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM i... |
| 8 | `ReportPeriod` | 数据统计区间 | number(10) | ✗ | 100.0% | 数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 and... |
| 9 | `BTradeValue` | 买入金额(元) | number(19,4) | ✓ | 92.54% |  |
| 10 | `STradeValue` | 卖出金额(元) | number(19,4) | ✓ | 92.54% |  |
| 11 | `TTradeValue` | 买入及卖出金额(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TradingType (交易类型)

交易类型(TradingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1844 and DM IN (3,4)，得到交易类型的具体描述：3-深股通，4-港股通（深）。

### InnerCode (证券内部编码)

证券内部编码(InnerCode)：当TradingType=3时，与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到上市公司的证券代码、简称等；当TradingType=4时，与“港股证券主表(HK_SecuMain)”中的“证券内部编码(InnerCode)”关联，得到上市公司的证券代码、简称等

### SecuCode (证券代码)

证券代码（SecuCode）为公告原文中披露的证券代码

### Currency (货币单位)

货币单位(Currency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1100,1420)，得到货币单位的具体描述：1100-港元，1420-人民币元。

### ReportPeriod (数据统计区间)

数据统计区间(ReportPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 102 and DM in (27,28,29)，得到数据统计区间的具体描述：27-年，28-月，29-日。

## SQL示例

```sql
-- 查询 深港通成交活跃股 数据
SELECT *
FROM lc_zhscactiveshares
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
