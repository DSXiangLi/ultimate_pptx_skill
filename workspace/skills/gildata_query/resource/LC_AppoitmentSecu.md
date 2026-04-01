# LC_AppoitmentSecu

**中文名**: 约定购回式证券交易

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AppoitmentSecu` |
| MySQL表名 | `lc_appoitmentsecu` |
| 中文名 | 约定购回式证券交易 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 22 |
| 版本 | 1.02 |

## 表描述

1.记录投资者以融资为目的的交易行为，符合条件的客户以约定价格向其指定交易的证券公司卖出标的证券（即\初始交易\"），并约定在未来某一日期客户按照另一约定价格从证券公司购回标的证券（即\"购回交易）。
2.数据范围：2012-09-03至今
3.信息来源：约定购回式证券交易公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 3 | `InfoSource` | 信息来源 | varchar2(300) | ✓ | 100.0% |  |
| 4 | `TargetType` | 标的类型 | number(10) | ✓ | 100.0% | 标的类型(TargetType)与(CT_SystemConst)表中的DM字段关联，令LB = 1008 AND DM... |
| 5 | `InnerCode` | 标的证券内码 | number(10) | ✗ | 100.0% | 标的证券内码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 6 | `TradeType` | 交易类型 | number(10) | ✗ | 100.0% | 交易类型(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1756 AND DM ... |
| 7 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 8 | `ClientDisclName` | 客户披露名称 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `Client` | 客户 | number(10) | ✓ | 97.58% |  |
| 10 | `SecurityDisclName` | 证券公司披露名称 | varchar2(100) | ✓ | 98.31% |  |
| 11 | `SecurityCompany` | 证券公司 | number(10) | ✓ | 98.31% |  |
| 12 | `TargetSecurityN` | 标的证券数量(股、份、手) | number(19,2) | ✗ | 100.0% |  |
| 13 | `RepurchaseTermUnit` | 购回期限单位 | number(10) | ✓ | 73.12% | 购回期限单位(RepurchaseTermUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 14 | `RepurchaseTerm` | 购回期限 | number(10) | ✓ | 73.12% |  |
| 15 | `TradeBeforeHolding` | 交易前持有数量(股、份、手) | number(19,2) | ✓ | 99.52% |  |
| 16 | `TradeBeforeRatio` | 交易前占比(%) | number(9,6) | ✓ | 99.03% |  |
| 17 | `TradeAfterHolding` | 交易后持有数量(股、份、手) | number(19,2) | ✓ | 99.76% |  |
| 18 | `TradeAfterRatio` | 交易后占比(%) | number(9,6) | ✓ | 98.79% |  |
| 19 | `RepurchaseTradeType` | 购回交易类型 | number(10) | ✓ | 40.19% | 购回交易类型(RepurchaseTradeType)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 20 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 21 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TargetType (标的类型)

标的类型(TargetType)与(CT_SystemConst)表中的DM字段关联，令LB = 1008 AND DM IN (1000,1300,1500)，得到标的类型的具体描述：1000-股票，1300-基金，1500-债券。

### InnerCode (标的证券内码)

标的证券内码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### TradeType (交易类型)

交易类型(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1756 AND DM IN (100,200,300,400)，得到交易类型的具体描述：100-初始交易，200-购回交易，300-暂停交易，400-终止交易。

### RepurchaseTermUnit (购回期限单位)

购回期限单位(RepurchaseTermUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 102 AND DM IN (27,28,29)，得到购回期限单位的具体描述：27-年，28-月，29-日。

### RepurchaseTradeType (购回交易类型)

购回交易类型(RepurchaseTradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1756 AND DM IN (201,202,203,204,209)，得到购回交易类型的具体描述：201-到期购回，202-提前购回，203-延期购回，204-终止购回，209-其他约定方式。

## SQL示例

```sql
-- 查询 约定购回式证券交易 数据
SELECT *
FROM lc_appoitmentsecu
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
