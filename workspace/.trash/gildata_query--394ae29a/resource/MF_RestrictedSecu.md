# MF_RestrictedSecu

**中文名**: 公募基金所持流通受限制证券

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_RestrictedSecu` |
| MySQL表名 | `mf_restrictedsecu` |
| 中文名 | 公募基金所持流通受限制证券 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 半年更新 |
| 字段数量 | 32 |
| 版本 | 1.03 |

## 表描述

1.本表记录中报、年报中公布由于配售等原因暂时不能上市的证券明细，及暂时不能上市的原因、复牌的日期等信息。
2.历史数据：2003年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `StockInnerCode` | 股票代码 | varchar2(20) | ✗ | 100.0% | 股票代码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 8 | `SecuSpecies` | 证券品种 | number(10) | ✓ | 100.0% | 证券品种(SecuSpecies)与(CT_SystemConst)表中的DM字段关联，令LB = 1212，得到证券品... |
| 9 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 10 | `ObtainReason` | 受限原因代码 | varchar2(100) | ✓ | 99.99% | 受限原因代码(ObtainReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1089，得到... |
| 11 | `RestrictedType` | 受限类别代码 | number(10) | ✓ | 100.0% | 受限类别代码(RestrictedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1549 ... |
| 12 | `ObtainDate` | 持有日期 | date | ✓ | 81.43% |  |
| 13 | `RestrictedTerm` | 可流通日期 | date | ✓ | 35.83% |  |
| 14 | `RSTPeriodInfo` | 受限期描述 | varchar2(200) | ✓ | 45.55% |  |
| 15 | `RSTPeriodSum` | 受限期数量 | number(10) | ✓ | 36.02% |  |
| 16 | `RSTPeriodUnit` | 受限期单位 | number(10) | ✓ | 36.02% | 受限期单位(RSTPeriodUnit)与(CT_SystemConst)表中的DM字段关联，令LB=2097，得到受限... |
| 17 | `ObtainPrice` | 认购价格(元) | number(19,4) | ✓ | 85.84% |  |
| 18 | `SharesHolding` | 持有数量(股/份) | number(18,4) | ✓ | 100.0% |  |
| 19 | `ObtainCost` | 成本(元) | number(19,4) | ✓ | 86.01% |  |
| 20 | `MarketValue` | 估值/市值(元) | number(19,4) | ✓ | 99.98% |  |
| 21 | `ReportDateValue` | 期末估价(元) | number(18,4) | ✓ | 99.95% |  |
| 22 | `BVRatioInNV` | 账面价值占净值比例(%) | number(18,6) | ✓ | 0.03% |  |
| 23 | `CostInNV` | 成本占净值比例(%) | number(18,6) | ✓ | 0.03% |  |
| 24 | `SuspendDate` | 停牌日期 | date | ✓ | 4.91% |  |
| 25 | `SuspendReason` | 停牌原因 | varchar2(500) | ✓ | 99.86% |  |
| 26 | `ResumptionDate` | 复牌日期 | date | ✓ | 2.97% |  |
| 27 | `ResumptionOpenPrice` | 复牌开盘价 | number(19,4) | ✓ | 2.96% |  |
| 28 | `ListedDate` | 上市日期 | date | ✓ | 0.23% |  |
| 29 | `RepurchaseExpireDate` | 回购到期日 | date | ✓ | 13.46% |  |
| 30 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 31 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### StockInnerCode (股票代码)

股票代码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### SecuSpecies (证券品种)

证券品种(SecuSpecies)与(CT_SystemConst)表中的DM字段关联，令LB = 1212，得到证券品种的具体描述：1-股票，2-债券，3-转股期可转债，4-权证，5-资产支持证券，6-基金，7-港股，9-其他，10-资产证券化产品，11-新三板，12-基础设施证券投资基金，20-期货。

### ObtainReason (受限原因代码)

受限原因代码(ObtainReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1089，得到受限原因代码的具体描述：1-二级配售，2-新股上网申购，3-新股法人网下配售，4-配股，5-增发网上申购，6-增发法人网下配售，7-认购新发行债券，8-送股转增，9-非公开发行流通受限，10-公开发行及增发，11-新股中签（网上、网下），12-债券中签，13-认购新发行证券，14-认购新发增发证券（其他），15-新股认购，16-未上市，17-首发原股东限售股份，18-增发流通受限，19-新股锁定，20-资产重组，21-重大信息披露，22-召开股东大会，23-股权分置改革，24-未按时披露信息，25-股票交易异常波动，26-引进战略投资者，27-发行股份购买资产，28-股权激励、员工持股，29-澄清公告，30-暂时停牌(其他原因)，50-债券正回购质押。

### RestrictedType (受限类别代码)

受限类别代码(RestrictedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1549 AND DM IN(10,20,30)，得到受限类别代码的具体描述：10-认购新发增发证券，20-暂时停牌，30-债券抵押。

### RSTPeriodUnit (受限期单位)

受限期单位(RSTPeriodUnit)与(CT_SystemConst)表中的DM字段关联，令LB=2097，得到受限期单位的具体描述：1-自然日，2-交易日，3-自然月，4-年，5-滚动日，6-滚动月，7-滚动年，8-滚动周，9-工作日，10-月，11-周，12-日。

## SQL示例

```sql
-- 查询 公募基金所持流通受限制证券 数据
SELECT *
FROM mf_restrictedsecu
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
