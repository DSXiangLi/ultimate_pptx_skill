# LC_Merger

**中文名**: 重大事项吸收合并

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Merger` |
| MySQL表名 | `lc_merger` |
| 中文名 | 重大事项吸收合并 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司重大事项 |
| 更新频率 | 不定时更新 |
| 字段数量 | 42 |
| 版本 | 1.01 |

## 表描述

1.收录上市公司公告中披露的公司吸收合并其他公司的事项，包括吸收合并日期进程、被合并公司代码及名称、主营、吸收合并股数、换股明细、被合并公司最新财务状况等指标。
2.数据范围：2006-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `PreSchemePublDate` | 吸收合并预案说明发布日 | date | ✓ | 67.55% |  |
| 5 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 73.95% |  |
| 6 | `AnouncementPublDate` | 吸收合并公告书发布日 | date | ✓ | 10.51% |  |
| 7 | `MergedCompanyCode` | 被合并公司代码 | number(10) | ✓ | 100.0% | 被合并公司代码（MergedCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号... |
| 8 | `MergedInnerCode` | 所属股票内部编码 | number(10) | ✓ | 6.22% | 所属股票内部编码（MergedInnerCode）：与“证券主表（SecuMain ）”中的“证券内部编码（InnerC... |
| 9 | `MergedParty` | 被合并公司名称 | varchar2(50) | ✗ | 100.0% |  |
| 10 | `FoundedDate` | 成立日期 | date | ✓ | 78.15% |  |
| 11 | `RegiCapital` | 注册资本(元) | number(19,4) | ✓ | 93.24% |  |
| 12 | `MainBusinesses` | 主营业务 | varchar2(200) | ✓ | 90.77% |  |
| 13 | `Industry` | 所属行业 | number(10) | ✓ | 7.86% | 所属行业（Industry）：与“行业表（CT_Industry）”中“行业编码(IndustryNum)”相关联，得到... |
| 14 | `MergeBaseDate` | 合并基准日 | date | ✓ | 34.83% |  |
| 15 | `AgreementDate` | 合并协议签署日 | date | ✓ | 10.51% |  |
| 16 | `ExchangeRateNumerator` | 折股比例分子 | float | ✓ | 8.14% |  |
| 17 | `ExchangeRateDenominator` | 折股比例分母 | float | ✓ | 8.14% |  |
| 18 | `InitialAmount` | 初始交易金额(元) | number(19,4) | ✓ | 3.56% |  |
| 19 | `FinalAmount` | 最终交易金额(元) | number(19,4) | ✓ | 1.92% |  |
| 20 | `ContraShares` | 合并抵消股份 | number(18,2) | ✓ | 2.65% |  |
| 21 | `IssueShares` | 发行股数 | number(18,2) | ✓ | 11.52% |  |
| 22 | `StateSharesAdded` | 其中:合并增加国家股(万股) | number(18,2) | ✓ | 0.46% |  |
| 23 | `LegalPersonSharesAdded` | 其中:合并增加法人股(万股) | number(18,2) | ✓ | 1.65% |  |
| 24 | `IndividualSharesAdded` | 其中:合并增加个人股(万股) | number(18,2) | ✓ | 1.55% |  |
| 25 | `ISharesAddedHoldingPeriod` | 合并增加个人股持股年限(年) | number(19,8) | ✓ | 1.28% |  |
| 26 | `ShareExchangeBeginDate` | 换股起始日 | date | ✓ | 3.29% |  |
| 27 | `ShareExchangeEndDate` | 换股截止日 | date | ✓ | 3.29% |  |
| 28 | `ExchangeRightRegDate` | 换股实施股权登记日 | date | ✓ | 5.12% |  |
| 29 | `EndDate` | 截至日期 | date | ✓ | 86.65% |  |
| 30 | `TotalAsset` | 资产总额(元) | number(19,4) | ✓ | 86.29% |  |
| 31 | `ShareholderEquity` | 股东权益(元) | number(19,4) | ✓ | 79.43% |  |
| 32 | `MainBusinessIncome` | 主营业务收入(元) | number(19,4) | ✓ | 67.0% |  |
| 33 | `NetProfit` | 净利润(元) | number(19,4) | ✓ | 72.12% |  |
| 34 | `ShareChangePublDate` | 股份变动公告日 | date | ✓ | 11.7% |  |
| 35 | `ShareCapitalBeforeMerge` | 合并前上市公司总股本(万股) | number(18,2) | ✓ | 9.87% |  |
| 36 | `ShareListDate` | 新增股份上市日 | date | ✓ | 7.13% |  |
| 37 | `ShareCustodyDate` | 股份托管确认日/股份托管日 | date | ✓ | 4.48% |  |
| 38 | `ICChangeRegiDate` | 工商变更登记日 | date | ✓ | 10.24% |  |
| 39 | `ChangeStatement` | 方案变动说明 | varchar2(255) | ✓ | 6.4% |  |
| 40 | `ChangeType` | 方案变动类型 | number(10) | ✓ | 6.22% | 方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案... |
| 41 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 42 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### MergedCompanyCode (被合并公司代码)

被合并公司代码（MergedCompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到被合并公司的名称等基本信息。

### MergedInnerCode (所属股票内部编码)

所属股票内部编码（MergedInnerCode）：与“证券主表（SecuMain
）”中的“证券内部编码（InnerCode）”关联，得到所属股票的交易代码、简称等。

### Industry (所属行业)

所属行业（Industry）：与“行业表（CT_Industry）”中“行业编码(IndustryNum)”相关联，得到所属行业的具体描述。

### ChangeType (方案变动类型)

方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。

## SQL示例

```sql
-- 查询 重大事项吸收合并 数据
SELECT *
FROM lc_merger
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
