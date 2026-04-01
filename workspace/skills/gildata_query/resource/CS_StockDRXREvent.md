# CS_StockDRXREvent

**中文名**: 境内股票除权除息记录表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `CS_StockDRXREvent` |
| MySQL表名 | `cs_stockdrxrevent` |
| 中文名 | 境内股票除权除息记录表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 不定期更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

内容说明：收录境内股票上市之日起除权除息事件
数据范围：股票上市起-至今
信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到... |
| 3 | `GilCode` | 聚源代码 | varchar2(12) | ✗ | 100.0% |  |
| 4 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 5 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN... |
| 6 | `CashDividend` | 派现(含税10派X元) | number(19,8) | ✓ | 100.0% |  |
| 7 | `BonusShareRatio` | 送股比例(10送X) | number(19,8) | ✓ | 100.0% |  |
| 8 | `TranAddShareRaio` | 转增股比例(10转增X) | number(19,8) | ✓ | 100.0% |  |
| 9 | `PlaRatio` | 配股比例(10配X) | number(19,8) | ✓ | 100.0% |  |
| 10 | `PlaPrice` | 每股配股价格(元) | number(19,8) | ✓ | 100.0% |  |
| 11 | `SEORatio` | 增发比例(10配X) | number(19,8) | ✓ | 100.0% |  |
| 12 | `SEOPrice` | 每股增发价格(元) | number(19,8) | ✓ | 100.0% |  |
| 13 | `ReformCashDivi` | 股权分置派现(含税10派X元) | number(19,8) | ✓ | 100.0% |  |
| 14 | `ReformBonus` | 股权分置送股比例(10送X) | number(19,8) | ✓ | 100.0% |  |
| 15 | `ReformTranAdd` | 股权分置转增股比例(10转增X) | number(19,8) | ✓ | 100.0% |  |
| 16 | `ShrinkSplitRatio` | 缩拆比例(10缩拆X) | number(19,8) | ✓ | 100.0% |  |
| 17 | `CDRTransRatio` | CDR转换比例(10转X) | number(19,8) | ✓ | 100.0% |  |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。

## SQL示例

```sql
-- 查询 境内股票除权除息记录表 数据
SELECT *
FROM cs_stockdrxrevent
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
