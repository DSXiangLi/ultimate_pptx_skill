# LC_STIBIPOQuoteDetails

**中文名**: 科创板IPO投资者报价情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBIPOQuoteDetails` |
| MySQL表名 | `lc_stibipoquotedetails` |
| 中文名 | 科创板IPO投资者报价情况 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 分红融资 |
| 更新频率 | 不定时更新 |
| 字段数量 | 26 |
| 版本 | 1.05 |

## 表描述

1.内容说明：收录科创板新上市公司首次发行股票公告中披露的投资者报价信息
2.数据范围：科创板上市至今
3.信息来源：上市公司首次发行股票公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✗ | 100.0% |  |
| 5 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 6 | `InvestorName` | 投资者名称(披露) | varchar2(200) | ✓ | 100.0% |  |
| 7 | `StandardInvestorName` | 投资者名称(标准) | varchar2(200) | ✓ | 100.0% |  |
| 8 | `InvestorType` | 投资者类型 | number(10) | ✓ | 100.0% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投... |
| 9 | `InvestorID` | 投资者编码 | number(10) | ✓ | 100.0% | 投资者编码(InvestorID):根据“InvestorType(投资者类型)”来确定, 当InvestorType(... |
| 10 | `BidderName` | 配售对象名称(披露) | varchar2(200) | ✓ | 100.0% |  |
| 11 | `StandardAquirerName` | 配售对象名称(标准) | varchar2(200) | ✓ | 100.0% |  |
| 12 | `BidderType` | 配售对象类型 | number(10) | ✓ | 100.0% | 配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到配售... |
| 13 | `BidderID` | 配售对象编码 | number(10) | ✓ | 73.32% | 配售对象编码(BidderID)：根据“BidderType(配售对象类型)”来确定, 当BidderType(配售对象... |
| 14 | `BidderCode` | 配售对象代码 | varchar2(20) | ✓ | 0.22% |  |
| 15 | `SecuAccountNumber` | 证券账户号码 | varchar2(20) | ✓ | 72.77% |  |
| 16 | `PriceUnit` | 每股/份申购价格(元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `PlannedBidVol` | 拟申购数量(股/份) | number(16,0) | ✓ | 100.0% |  |
| 18 | `QuoteSituation` | 报价情况 | number(10) | ✓ | 100.0% | 报价情况(QuoteSituation)与(CT_SystemConst)表中的DM字段关联，令LB = 2288，得到... |
| 19 | `QuoteSituationDesc` | 报价情况描述 | varchar2(50) | ✓ | 100.0% |  |
| 20 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 21 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |
| 23 | `LimitSaleType` | 限售方式 | number(10) | ✓ | 1.12% | 限售方式(LimitSaleType)与(CT_SystemConst)表中的DM字段关联，令LB=2668，得到限售方... |
| 24 | `LimitSalePeriod` | 限售期 | number(10) | ✓ | 1.12% |  |
| 25 | `LimitSalePeriodUnit` | 限售期单位 | number(10) | ✓ | 1.12% | 限售期单位(LimitSalePeriodUnit)与(CT_SystemConst)表中的DM字段关联，令LB=102... |
| 26 | `RestriHoldingRatio` | 限售比例(%) | number(9,4) | ✓ | 1.12% |  |

## 字段说明

### InnerCode (内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### InvestorID (投资者编码)

投资者编码(InvestorID):根据“InvestorType(投资者类型)”来确定,
当InvestorType(投资者类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当InvestorType(投资者类型)= 3 时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### BidderType (配售对象类型)

配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到配售对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### BidderID (配售对象编码)

配售对象编码(BidderID)：根据“BidderType(配售对象类型)”来确定,
当BidderType(配售对象类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当BidderType(配售对象类型)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### QuoteSituation (报价情况)

报价情况(QuoteSituation)与(CT_SystemConst)表中的DM字段关联，令LB = 2288，得到报价情况的具体描述：1-有效报价，2-高价剔除，3-低价未入围，4-无效报价。

### LimitSaleType (限售方式)

限售方式(LimitSaleType)与(CT_SystemConst)表中的DM字段关联，令LB=2668，得到限售方式的具体描述：1-摇号限售，2-比例限售，3-约定限售。

### LimitSalePeriodUnit (限售期单位)

限售期单位(LimitSalePeriodUnit)与(CT_SystemConst)表中的DM字段关联，令LB=102 AND DM IN (27,28,29)，得到限售期单位的具体描述：27-年，28-月，29-日。

## SQL示例

```sql
-- 查询 科创板IPO投资者报价情况 数据
SELECT *
FROM lc_stibipoquotedetails
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
