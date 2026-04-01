# HK_SEHKPartiList

**中文名**: 港股联交所参与者名单

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SEHKPartiList` |
| MySQL表名 | `hk_sehkpartilist` |
| 中文名 | 港股联交所参与者名单 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.收录香港联交所参与者、香港期交所参与者、香港结算参与者、香港期货结算所参与者名单信息。
2.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股企业概况（HK_CompanyArchives）”中的“公司代码（Compa... |
| 3 | `ChiName` | 公司简称 | varchar2(100) | ✓ | 100.0% |  |
| 4 | `PartiCategories` | 参与者类别 | number(10) | ✗ | 100.0% | 参与者类别(PartiCategories)与(CT_SystemConst)表中的DM字段关联，令LB = 2036，... |
| 5 | `PartiIdentity` | 参与者身份 | number(10) | ✓ | 99.48% | 参与者身份(PartiIdentity)与(CT_SystemConst)表中的DM字段关联，令LB = 2037，得到... |
| 6 | `PartiNumber` | 参与者编号 | varchar2(100) | ✓ | 91.57% |  |
| 7 | `BrokerNumber` | 经纪编号 | varchar2(100) | ✓ | 77.65% |  |
| 8 | `EffectiveDate` | 生效日期 | date | ✓ | 28.98% |  |
| 9 | `ExpiryDate` | 失效日期 | date | ✓ | 27.85% |  |
| 10 | `TransactionStatus` | 交易状态 | number(10) | ✓ | 100.0% | 交易状态(TransactionStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2038... |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |
| 14 | `ClientCode` | 客户代码 | varchar2(100) | ✓ | 100.0% | 客户代码(ClientCode)：该字段已废弃，不再提供数据。  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股企业概况（HK_CompanyArchives）”中的“公司代码（CompanyCode）”关联。

### PartiCategories (参与者类别)

参与者类别(PartiCategories)与(CT_SystemConst)表中的DM字段关联，令LB = 2036，得到参与者类别的具体描述：1-联交所参与者，2-期交所参与者，3-香港结算参与者，4-期货结算所参与者。

### PartiIdentity (参与者身份)

参与者身份(PartiIdentity)与(CT_SystemConst)表中的DM字段关联，令LB = 2037，得到参与者身份的具体描述：1-CA，2-CP，3-DCP，4-GCP，5-NCP，6-SL，7-SPP，8-其他，9-双柜台庄家，10-交易所买卖产品庄家。

### TransactionStatus (交易状态)

交易状态(TransactionStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2038，得到交易状态的具体描述：1-正常交易，2-终止，3-暂停。

### ClientCode (客户代码)

客户代码(ClientCode)：该字段已废弃，不再提供数据。


## SQL示例

```sql
-- 查询 港股联交所参与者名单 数据
SELECT *
FROM hk_sehkpartilist
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
