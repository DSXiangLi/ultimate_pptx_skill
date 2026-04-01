# LC_AshareSNIBid

**中文名**: A股增发询价明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AshareSNIBid` |
| MySQL表名 | `lc_asharesnibid` |
| 中文名 | A股增发询价明细 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.03 |

## 表描述

1.股票增发是指上市公司通过指定投资者（如大股东或机构投资者）或全部投资者额外发行股份募集资金的融资方式。该表收录了A股增发询价对象的认购情况，包括申购价格、股数和金额等内容。
2.数据范围：2011-03-29至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 7 | `InvestorCode` | 投资者编码 | number(10) | ✓ | 83.32% | 投资者编码(InvestorCode):根据“InvestorType(投资者类型)”来确定, 当InvestorTyp... |
| 8 | `InvestorName` | 投资者名称 | varchar2(200) | ✗ | 100.0% |  |
| 9 | `InvestorType` | 投资者类型 | number(10) | ✓ | 100.0% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投... |
| 10 | `InquirerName` | 询价对象名称 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `InquirerType` | 询价对象类型 | number(10) | ✓ | 100.0% | 询价对象类型(InquirerType)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到询价... |
| 12 | `InquirerID` | 询价对象编码 | number(10) | ✓ | 79.51% | 询价对象编码(InquirerID):根据“InquirerType (询价对象类型)”来确定, 当InquirerTy... |
| 13 | `InquirerCateg` | 询价对象类别 | number(10) | ✓ | 9.66% | 询价对象类别(InquirerCateg)与(CT_SystemConst)表中的DM字段关联，令LB = 1825，得... |
| 14 | `PriceUnit` | 申购价格(元/股) | number(19,4) | ✓ | 99.65% |  |
| 15 | `PlannedBidVol` | 申购股数(股) | number(19,2) | ✓ | 99.34% |  |
| 16 | `PlannedBidSum` | 申购金额(元) | number(18,2) | ✓ | 99.63% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `InquirerCode` | 询价对象代码 | number(10) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InvestorCode (投资者编码)

投资者编码(InvestorCode):根据“InvestorType(投资者类型)”来确定,
当InvestorType(投资者类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当InvestorType(投资者类型)= 3 时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### InquirerType (询价对象类型)

询价对象类型(InquirerType)与(CT_SystemConst)表中的DM字段关联，令LB=1783，得到询价对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### InquirerID (询价对象编码)

询价对象编码(InquirerID):根据“InquirerType (询价对象类型)”来确定,
当InquirerType (询价对象类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当InquirerType (询价对象类型)= 3 时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### InquirerCateg (询价对象类别)

询价对象类别(InquirerCateg)与(CT_SystemConst)表中的DM字段关联，令LB = 1825，得到询价对象类别的具体描述。

## SQL示例

```sql
-- 查询 A股增发询价明细 数据
SELECT *
FROM lc_asharesnibid
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
