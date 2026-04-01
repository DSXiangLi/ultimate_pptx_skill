# MF_REITsQuoteDetails

**中文名**: 基础设施基金(REITs)投资者报价情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_REITsQuoteDetails` |
| MySQL表名 | `mf_reitsquotedetails` |
| 中文名 | 基础设施基金(REITs)投资者报价情况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 基础设施公募REITs |
| 更新频率 | 不定时更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：收录基础设施公募REITs首次发行、基金扩募等询价过程中的投资者报价信息。
2.数据范围：2021年4月起-至今 。
3.信息来源：证监会公布的基金份额发售公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `QuoteReason` | 报价原因 | number(10) | ✗ | 100.0% | 报价原因(QuoteReason)与(CT_SystemConst)表中的DM字段关联，令LB=1016 AND DM ... |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `InvestorName` | 投资者名称 | varchar2(200) | ✓ | 53.45% |  |
| 7 | `InvestorCode` | 投资者编码 | number(10) | ✓ | 53.43% | 投资者编码(InvestorCode)：与“机构基本资料表(LC_InstiArchive)”中的CompanyCode... |
| 8 | `InvestorType` | 投资者类型 | number(10) | ✓ | 53.44% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到投资者... |
| 9 | `BidderCode` | 配售对象代码 | varchar2(20) | ✓ | 84.7% |  |
| 10 | `BidderName` | 配售对象名称 | varchar2(200) | ✗ | 100.0% |  |
| 11 | `BidderInnerCode` | 配售对象编码 | number(10) | ✓ | 0.19% |  |
| 12 | `BidderType` | 配售对象类型 | number(10) | ✓ | 100.0% | 配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB=1825，得到配售对象... |
| 13 | `PriceUnit` | 拟认购价格(元) | number(19,4) | ✓ | 100.0% |  |
| 14 | `PlannedBidVol` | 拟认购数量(份) | number(18,0) | ✓ | 100.0% |  |
| 15 | `QuoteSituation` | 报价情况 | number(10) | ✓ | 100.0% | 报价情况(QuoteSituation)与(CT_SystemConst)表中的DM字段关联，令LB=2288，得到报价... |
| 16 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### QuoteReason (报价原因)

报价原因(QuoteReason)与(CT_SystemConst)表中的DM字段关联，令LB=1016 AND DM IN(6,7)，得到报价原因的具体描述：6-基金发行，7-基金扩募。

### InvestorCode (投资者编码)

投资者编码(InvestorCode)：与“机构基本资料表(LC_InstiArchive)”中的CompanyCode关联，得到投资者基本信息。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### BidderType (配售对象类型)

配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB=1825，得到配售对象类型的具体描述：1-公募基金，2-社保基金或社保基金组合，3-个人或个人自有资金投资账户，4-其他，5-企业年金计划，6-机构自营投资账户，7-证券公司集合资产管理计划，8-基金公司或其资产管理子公司一对一，9-保险资金投资账户，10-证券公司限额特定资产管理计划，11-基金公司或其资产管理子公司一对多，12-QFII投资账户，13-私募基金，14-证券公司定向资产管理计划，15-集合信托计划，16-保险机构资产管理产品，17-期货公司或其资产管理子公司一对多。

### QuoteSituation (报价情况)

报价情况(QuoteSituation)与(CT_SystemConst)表中的DM字段关联，令LB=2288，得到报价情况的具体描述：1-有效报价，2-高价剔除，3-低价未入围，4-无效报价。

## SQL示例

```sql
-- 查询 基础设施基金(REITs)投资者报价情况 数据
SELECT *
FROM mf_reitsquotedetails
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
