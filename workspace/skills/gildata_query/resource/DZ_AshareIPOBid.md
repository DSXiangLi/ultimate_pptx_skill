# DZ_AshareIPOBid

**中文名**: A股IPO询价明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_AshareIPOBid` |
| MySQL表名 | `dz_ashareipobid` |
| 中文名 | A股IPO询价明细 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1.01 |

## 表描述

1.收录新上市A股询价、网下配售明细，包括投资者名称、配售对象名称、申报价格、拟申购股数、总实际申购股数和总获配售股数等内容。
2.数据范围：2014-01-17至今
3.信息来源：上交所、深交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% |  |
| 4 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 5 | `InvestorCode` | 投资者编码 | number(10) | ✓ | 85.74% | 投资者编码(InvestorCode):根据“InvestorType(投资者类型)”来确定, 当InvestorTyp... |
| 6 | `InvestorName` | 投资者名称 | varchar2(100) | ✓ | 99.96% |  |
| 7 | `InvestorType` | 投资者类型 | number(10) | ✓ | 99.96% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投... |
| 8 | `BidderName` | 配售对象名称 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `BidderType` | 配售对象类型 | number(10) | ✓ | 100.0% | 配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到配售... |
| 10 | `BidderID` | 配售对象编码 | number(10) | ✓ | 65.15% | 配售对象编码(BidderID)：根据“BidderType(配售对象类型)”来确定, 当BidderType(配售对象... |
| 11 | `PriceUnit` | 申报价格 | number(19,4) | ✓ | 100.0% |  |
| 12 | `PlannedBidVol` | 拟申购股数(股/份) | number(19,2) | ✓ | 100.0% |  |
| 13 | `PremiumRate` | 申报价折溢价比率 | number(19,4) | ✓ | 100.0% | 申报价折溢价比率(PremiumRate)=申报价格/每股发行价格。 |
| 14 | `BidVolEx` | 被剔除申购股数(股/份) | number(19,2) | ✓ | 86.19% |  |
| 15 | `ActualBidVol` | 总实际申购股数(股/份) | number(19,2) | ✓ | 86.19% |  |
| 16 | `ActualAllotment` | 总获配售股数(股/份) | number(19,2) | ✓ | 94.08% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `BidderCode` | 配售对象代码 | number(10) | ✓ | 0.0% |  |
| 21 | `BidderCategory` | 配售对象类别 | number(10) | ✓ | 65.73% | 配售对象类别(BidderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1825，... |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### InvestorCode (投资者编码)

投资者编码(InvestorCode):根据“InvestorType(投资者类型)”来确定,
当InvestorType(投资者类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当InvestorType(投资者类型)= 3 时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### BidderType (配售对象类型)

配售对象类型(BidderType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到配售对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### BidderID (配售对象编码)

配售对象编码(BidderID)：根据“BidderType(配售对象类型)”来确定,
当BidderType(配售对象类型)=2时,与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息;
当BidderType(配售对象类型)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### PremiumRate (申报价折溢价比率)

申报价折溢价比率(PremiumRate)=申报价格/每股发行价格。

### BidderCategory (配售对象类别)

配售对象类别(BidderCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1825，得到配售对象类别的具体描述：1-公募基金，2-社保基金或社保基金组合，3-个人或个人自有资金投资账户，4-其他，5-企业年金计划，6-机构自营投资账户，7-证券公司集合资产管理计划，8-基金公司或其资产管理子公司一对一，9-保险资金投资账户，10-证券公司限额特定资产管理计划，11-基金公司或其资产管理子公司一对多，12-QFII投资账户，13-私募基金，14-证券公司定向资产管理计划，15-集合信托计划，16-保险机构资产管理产品，17-期货公司或其资产管理子公司一对多。

## SQL示例

```sql
-- 查询 A股IPO询价明细 数据
SELECT *
FROM dz_ashareipobid
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
