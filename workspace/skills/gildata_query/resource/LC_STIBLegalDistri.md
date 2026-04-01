# LC_STIBLegalDistri

**中文名**: 科创板法人配售与战略投资者

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBLegalDistri` |
| MySQL表名 | `lc_stiblegaldistri` |
| 中文名 | 科创板法人配售与战略投资者 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 40 |
| 版本 | 1.08 |

## 表描述

收录科创板公司首次发行、增发新股、发行可转债过程中采用网下配售方式过程中，获得配售的企业、基金明细。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `IssueType` | 发行类别 | number(10) | ✗ | 100.0% | 发行类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM ... |
| 7 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `DistributionSum` | 配售总股数 | number(18,2) | ✗ | 100.0% |  |
| 9 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 10 | `AquirerCode` | 获配对象企业编号 | number(10) | ✓ | 74.67% | 当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(Compa... |
| 11 | `AquirerInner` | 获配对象证券内码 | number(10) | ✓ | 73.83% | 获配对象证券内码(AquirerInner)和证券主表(SecuMain)中的InnerCode关联；得到证券品种的基本... |
| 12 | `AquirerName` | 获配对象名称(披露) | varchar2(200) | ✗ | 100.0% |  |
| 13 | `StandardAquirerName` | 获配对象名称(标准) | varchar2(200) | ✓ | 100.0% |  |
| 14 | `AquirerType` | 获配对象类型 | number(10) | ✓ | 98.59% | 获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获... |
| 15 | `SecuAccountNumber` | 证券账户号码 | varchar2(20) | ✓ | 98.74% |  |
| 16 | `DistributeNature` | 配售对象性质 | number(10) | ✓ | 100.0% | 配售对象性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 122... |
| 17 | `BidderCode` | 配售对象代码 | varchar2(20) | ✓ | 0.0% |  |
| 18 | `InvestorName` | 投资者名称(披露) | varchar2(200) | ✓ | 89.25% |  |
| 19 | `StandardInvestorName` | 投资者名称(标准) | varchar2(200) | ✓ | 99.48% |  |
| 20 | `InvestorType` | 投资者类型 | number(10) | ✓ | 89.25% | 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投... |
| 21 | `ClassofInvestor` | 投资者分类 | number(10) | ✓ | 15.85% | 投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到... |
| 22 | `InvestorCode` | 投资者编号 | number(10) | ✓ | 89.37% | 	 当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(Com... |
| 23 | `ValidApplyVol` | 有效申购股数(股/份) | number(18,2) | ✓ | 99.91% |  |
| 24 | `AquiredSum` | 配售股数(股/份) | number(18,2) | ✓ | 100.0% |  |
| 25 | `RestrictedSum` | 有锁定期配售股数(股/份) | number(16,0) | ✓ | 21.17% |  |
| 26 | `NonRestrictedSum` | 无锁定期配售股数(股/份) | number(16,0) | ✓ | 96.38% |  |
| 27 | `AquirerAmount` | 获配金额(元) | number(19,4) | ✓ | 100.0% |  |
| 28 | `Commission` | 新股配售经纪佣金(元) | number(19,4) | ✓ | 83.33% |  |
| 29 | `PayableSUM` | 应缴款总额(元) | number(19,4) | ✓ | 100.0% |  |
| 30 | `OwnedPeriod` | 锁定期限(月) | number(10) | ✓ | 100.0% |  |
| 31 | `FloatDate` | 锁定股份流通日期 | date | ✓ | 99.19% |  |
| 32 | `Remark` | 备注 | varchar2(255) | ✓ | 0.0% |  |
| 33 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 34 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 35 | `JSID` | JSID | number(19) | ✗ |  |  |
| 36 | `CoreStaffsStraSHVal` | 其中:高管、员工参与战略配售股份金额(元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 37 | `SponsorStraSharesHVal` | 其中:保荐机构及相关子公司参与战略配售股份金额(元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 38 | `OtherStraSHVol` | 其中:其他参与战略配售计划数量(股/份)(废弃) | number(16,0) | ✓ | 0.0% |  |
| 39 | `OtherStraSHVal` | 其中:其他参与战略配售计划金额(元)(废弃) | number(19,4) | ✓ | 0.0% |  |
| 40 | `OtherStraSHRat` | 其中:其他计划参与战略配售占比(%)(废弃) | number(9,4) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (证券内部编码)

 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### IssueType (发行类别)

发行类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (2,17,21,22,23)，得到发行类别的具体描述：2-发行新股，17-优先股发行，21-非公开增发，22-公开增发，23-非公开增发配套融资。

### AquirerCode (获配对象企业编号)

当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当获配对象类型(AquirerType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

### AquirerInner (获配对象证券内码)

获配对象证券内码(AquirerInner)和证券主表(SecuMain)中的InnerCode关联；得到证券品种的基本信息。

### AquirerType (获配对象类型)

获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获配对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### DistributeNature (配售对象性质)

配售对象性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1220，得到配售对象性质的具体描述：1-一般法人，2-战略投资者，3-基金配售，4-原股东优先配售，5-高管及员工战略配售，6-保荐机构及相关子公司战略配售。

### InvestorType (投资者类型)

投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。

### ClassofInvestor (投资者分类)

投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到投资者分类的具体描述：1-A类，2-B类，3-C类。

### InvestorCode (投资者编号)

	
当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当投资者类型(InvestorType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。

## SQL示例

```sql
-- 查询 科创板法人配售与战略投资者 数据
SELECT *
FROM lc_stiblegaldistri
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
