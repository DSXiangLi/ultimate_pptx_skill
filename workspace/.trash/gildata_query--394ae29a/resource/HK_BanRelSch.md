# HK_BanRelSch

**中文名**: 港股限售解禁时间表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_BanRelSch` |
| MySQL表名 | `hk_banrelsch` |
| 中文名 | 港股限售解禁时间表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 17 |
| 版本 | 1.01 |

## 表描述

1.内容说明：记录上市公司股东限售解禁的情况，方便客户准确查询和掌握最新情况；
2.数据范围：2010-01-01至今；
3.信息来源：恒生聚源整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | number(10) | ✓ | 100.0% |  |
| 5 | `SHID` | 股东编码 | number(10) | ✓ | 85.16% |  |
| 6 | `SHName` | 股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 7 | `RestrictedDate` | 限售日期 | date | ✓ | 100.0% |  |
| 8 | `RelieveDate` | 解禁日期 | date | ✗ | 100.0% |  |
| 9 | `LimitSalePeriod` | 限售期(月) | number(18,2) | ✓ | 100.0% |  |
| 10 | `HoldSharesBegin` | 期初持有总股数 | number(18,2) | ✓ | 100.0% |  |
| 11 | `CorSharesRelDate` | 解禁日对应解禁股数 | number(18,2) | ✓ | 100.0% |  |
| 12 | `HoldratioOfTotEqu` | 占公司总股数比例(%) | number(18,4) | ✓ | 100.0% |  |
| 13 | `RelieveType` | 解禁类型 | number(10) | ✗ | 100.0% | 解禁类型(RelieveType):1-基石限售解禁。 |
| 14 | `StockType` | 股票类型 | number(10) | ✓ | 100.0% | 股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1341，得到股票类型的... |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### RelieveType (解禁类型)

解禁类型(RelieveType):1-基石限售解禁。

### StockType (股票类型)

股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1341，得到股票类型的具体描述：10-普通股，20-优先股，30-债权证，40-普通股-A类，50-普通股-B类，60-A股，70-B股，80-内资股，90-非H股外资股。

## SQL示例

```sql
-- 查询 港股限售解禁时间表 数据
SELECT *
FROM hk_banrelsch
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
