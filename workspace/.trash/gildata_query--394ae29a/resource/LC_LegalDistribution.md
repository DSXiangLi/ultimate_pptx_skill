# LC_LegalDistribution

**中文名**: 法人配售与战略投资者

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_LegalDistribution` |
| MySQL表名 | `lc_legaldistribution` |
| 中文名 | 法人配售与战略投资者 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 42 |
| 版本 | 1.11 |

## 表描述

1.收录公司首次发行、增发新股、发行可转债过程中采用网下配售方式过程中，获得配售的企业、基金明细。
2.数据范围：1994-04-23至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `DistributionSum` | 配售总股数(股/份/张) | number(18,2) | ✗ | 100.0% |  |
| 7 | `DistributionReason` | 配售原因 | number(10) | ✓ | 100.0% | 配售原因(DistributionReason)与(CT_SystemConst)表中的DM字段关联，令LB = 101... |
| 8 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `SerialNum` | 序号 | number(10) | ✓ | 100.0% |  |
| 10 | `AquirerName` | 获配企业名称(披露) | varchar2(200) | ✗ | 100.0% |  |
| 11 | `StandardAquirerName` | 获配企业名称(标准) | varchar2(200) | ✓ | 99.69% |  |
| 12 | `AquirerType` | 获配对象类型 | number(10) | ✓ | 54.5% | 获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获... |
| 13 | `SecuAccountNumber` | 证券账户号码 | varchar2(20) | ✓ | 51.81% |  |
| 14 | `BidderCode` | 配售对象代码 | varchar2(20) | ✓ | 3.69% |  |
| 15 | `AquirerCharacter` | 获配企业性质 | number(10) | ✓ |  |  |
| 16 | `SecuCoBelongedCode` | 所属券商编号 | number(10) | ✓ | 66.08% | 当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(Compa... |
| 17 | `SecuCoBelonged` | 所属券商名称 | varchar2(100) | ✓ | 32.87% | 所属券商名称(SecuCoBelonged)：历史字段，日增数据参考本表“InvestorName[投资者名称(披露)]... |
| 18 | `InvestorName` | 投资者名称(披露) | varchar2(200) | ✓ | 60.53% |  |
| 19 | `StandardInvestorName` | 投资者名称(标准) | varchar2(200) | ✓ | 62.17% |  |
| 20 | `InvestorType` | 投资者类型 | number(10) | ✓ | 60.53% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and... |
| 21 | `ClassofInvestor` | 投资者分类 | number(10) | ✓ | 12.48% | 投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到... |
| 22 | `InvestorCode` | 投资者编号 | number(10) | ✓ | 55.13% | 	 当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(Com... |
| 23 | `SecuCode` | 获配企业证券代码 | number(10) | ✓ | 56.7% | 获配企业证券代码(SecuCode)和证券主表(SecuMain)中的InnerCode关联 |
| 24 | `ValidApplyVol` | 有效申购股数(股/份/张) | number(18,2) | ✓ | 98.71% |  |
| 25 | `SupplementAmount` | 补款金额(元)(债券用) | number(19,4) | ✓ | 0.59% |  |
| 26 | `RefundAmount` | 退款金额(元) | number(19,4) | ✓ | 3.79% |  |
| 27 | `AquiredSum` | 配售股数(股/份/张) | number(18,2) | ✗ | 100.0% |  |
| 28 | `AquirerAmount` | 获配金额(元) | number(19,4) | ✓ | 99.69% |  |
| 29 | `RestrictedSum` | 有锁定期配售股数(股) | number(16,0) | ✓ | 34.08% |  |
| 30 | `NonRestrictedSum` | 无锁定期配售股数(股) | number(16,0) | ✓ | 94.46% |  |
| 31 | `DistributeNature` | 配售性质 | number(10) | ✓ | 100.0% | 配售性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1220 ... |
| 32 | `OwnedPeriod` | 锁定期限(月) | number(10) | ✓ | 95.96% |  |
| 33 | `FloatDate` | 锁定股份流通日期 | date | ✓ | 95.9% |  |
| 34 | `Notes` | 备注 | varchar2(255) | ✓ | 0.01% |  |
| 35 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 36 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 37 | `JSID` | JSID | number(19) | ✗ |  |  |
| 38 | `CoreStaffsStraSHVal` | 其中:高管、员工参与战略配售股份金额(万元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 39 | `SponsorStraSharesHVal` | 其中:保荐机构及相关子公司参与战略配售股份金额(万元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 40 | `OtherStraSHVol` | 其中:其他参与战略配售计划数量(万股)(废弃) | number(18,4) | ✓ | 0.0% |  |
| 41 | `OtherStraSHVal` | 其中:其他参与战略配售计划金额(万元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 42 | `OtherStraSHRat` | 其中:其他计划参与战略配售占比(%)(废弃) | number(9,4) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### DistributionReason (配售原因)

配售原因(DistributionReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1016，得到配售原因的具体描述：1-配股，2-发行新股，3-增发新股，4-可转换债券，5-吸收合并，6-基金发行，7-基金扩募，8-企业债券，9-基金营销，10-金融债券，11-股权分置，12-资产支持证券，13-权证发行，14-信用风险，15-港交所基金发行，16-可交换公司债券，17-优先股发行，18-CDR首发，19-CDR增发，20-CDR配股，21-非公开增发，22-公开增发，23-非公开增发配套融资，99-其他证券发行。

### AquirerType (获配对象类型)

获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获配对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### SecuCoBelongedCode (所属券商编号)

当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当获配对象类型(AquirerType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### SecuCoBelonged (所属券商名称)

所属券商名称(SecuCoBelonged)：历史字段，日增数据参考本表“InvestorName[投资者名称(披露)]”

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3)，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种。

### ClassofInvestor (投资者分类)

投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到投资者分类的具体描述：1-A类，2-B类，3-C类。

### InvestorCode (投资者编号)

	
当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当投资者类型(InvestorType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### SecuCode (获配企业证券代码)

获配企业证券代码(SecuCode)和证券主表(SecuMain)中的InnerCode关联

### DistributeNature (配售性质)

配售性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1220 AND DM IN (1,2,3,4,5,6)，得到配售性质的具体描述：1-一般法人，2-战略投资者，3-基金配售，4-原股东优先配售，5-高管及员工战略配售，6-保荐机构及相关子公司战略配售。

## SQL示例

```sql
-- 查询 法人配售与战略投资者 数据
SELECT *
FROM lc_legaldistribution
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
