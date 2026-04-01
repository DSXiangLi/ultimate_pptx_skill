# DZ_IPODeclaration

**中文名**: A股发行申报企业信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_IPODeclaration` |
| MySQL表名 | `dz_ipodeclaration` |
| 中文名 | A股发行申报企业信息 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 57 |
| 版本 | 1.03 |

## 表描述

1.内容说明：收录了中国证监会公布的首次公开发行股票申报企业基本信息，包括申报企业名称、所属板块、证监会所属行业代码以及涉及到的保荐机构、会计师事务所、律师事务所等内容。
2.数据范围：2012-01-31至今
3.信息来源：中国证监会、上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 91.51% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 申报企业编号 | number(10) | ✗ | 100.0% | 申报企业编号（CompanyCode）：与“公司概况（LC_StockArchives）”中的“公司代码（Company... |
| 4 | `CompanyName` | 申报企业名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `IssueMethod` | 发行方式 | number(10) | ✓ | 100.0% | 发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2344，得到发行方式的... |
| 6 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `AcceptanceDate` | 受理日期 | date | ✓ | 35.59% |  |
| 9 | `EstimatedFinanceAmt` | 预计融资金额(亿元) | number(19,4) | ✓ | 54.23% |  |
| 10 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 11 | `InfoSourceCode` | 信息来源编码 | number(10) | ✓ | 100.0% | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=2345，得到... |
| 12 | `PlateCode` | 所属板块 | number(10) | ✓ | 100.0% | 所属板块(PlateCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1670，得到所属板块的... |
| 13 | `CCSignDate` | 辅导协议签署日期 | date | ✓ | 0.78% |  |
| 14 | `CCRegDate` | 辅导备案日期 | date | ✓ | 0.83% |  |
| 15 | `CSRCInvolvedInstCode` | 证监会派出机构编码 | number(10) | ✓ | 0.83% |  |
| 16 | `EstiIssueVolume` | 预计发行股数(万股) | number(19,8) | ✓ | 46.74% |  |
| 17 | `EstiTotalSAfterIssue` | 预计发行后总股本(万股) | number(19,8) | ✓ | 0.0% |  |
| 18 | `IssueObject` | 发行对象 | number(10) | ✓ | 6.76% | 发行对象(IssueObject)与(CT_SystemConst)表中的DM字段关联，令LB = 2343，得到发行对... |
| 19 | `RefinanceMethod` | 再融资类型 | number(10) | ✓ | 8.05% | 再融资类型(RefinanceMethod)与(CT_SystemConst)表中的DM字段关联，令LB=1016 AN... |
| 20 | `RefinanceMethodDesc` | 再融资类型描述 | varchar2(50) | ✓ | 0.63% |  |
| 21 | `ReformType` | 重组类型 | number(10) | ✓ | 1.05% | 重组类型(ReformType)与(CT_SystemConst)表中的DM字段关联，令LB = 2139，得到重组类型... |
| 22 | `RaisingIssueValue` | 募集配套融资拟发行金额(亿元) | number(19,4) | ✓ | 0.4% |  |
| 23 | `PurchaseIssueValue` | 资产购买拟发行金额(亿元) | number(19,4) | ✓ | 0.24% |  |
| 24 | `ReformExamType` | 重组审核类型 | number(10) | ✓ | 0.23% | 重组审核类型(ReformExamType)与(CT_SystemConst)表中的DM字段关联，令LB = 2346，... |
| 25 | `ReformRecpDate` | 重组接收日期 | date | ✓ | 0.57% |  |
| 26 | `ReformCorrectDate` | 重组补正日期 | date | ✓ | 0.18% |  |
| 27 | `ReformFeedbDate` | 重组反馈日期 | date | ✓ | 0.43% |  |
| 28 | `ReformFeedbRepDate` | 重组反馈回复日期 | date | ✓ | 0.14% |  |
| 29 | `ReformMeetDate` | 并购重组委会议日期 | date | ✓ | 0.12% |  |
| 30 | `ReformResltDate` | 重组审结日期 | date | ✓ | 0.03% |  |
| 31 | `RegPlaceCode` | 注册地代码 | number(10) | ✓ | 79.01% | 注册地代码(RegPlaceCode)：可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；... |
| 32 | `CSRCIndustryName` | 所属行业/领域 | varchar2(100) | ✓ | 76.92% |  |
| 33 | `CSRCIndustryNum` | 证监会所属行业内码 | number(10) | ✓ | 76.92% | 与“行业表（CT_Industry）”中的“行业编码（IndustryNum）”关联，得到申报企业所属证监会行业信息。此... |
| 34 | `CSRCIndustryCode` | 证监会所属行业代码 | varchar2(10) | ✓ | 76.92% |  |
| 35 | `ListExchangeCode` | 拟上市地代码 | number(10) | ✓ | 90.88% | 拟上市地代码(ListExchangeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 201... |
| 36 | `SponsorName` | 保荐机构 | varchar2(200) | ✓ | 98.6% |  |
| 37 | `SponsorCode` | 保荐机构编号 | number(10) | ✓ |  |  |
| 38 | `SponsorRepresentative` | 保荐代表人 | varchar2(100) | ✓ | 78.6% |  |
| 39 | `IndeFinaAdvisor` | 独立财务顾问 | varchar2(200) | ✓ | 1.06% |  |
| 40 | `IndeFinaAdvisorCode` | 独立财务顾问编码 | number(10) | ✓ |  |  |
| 41 | `IndeFinaAdvisorMan` | 独立财务顾问主办人 | varchar2(100) | ✓ | 1.06% |  |
| 42 | `AccountingFirm` | 会计师事务所 | varchar2(200) | ✓ | 95.14% |  |
| 43 | `AccountingFirmCode` | 会计师事务所编号 | number(10) | ✓ |  |  |
| 44 | `SignatureAccountant` | 签字会计师 | varchar2(100) | ✓ | 79.66% |  |
| 45 | `LawFirm` | 律师事务所 | varchar2(200) | ✓ | 95.14% |  |
| 46 | `LawFirmCode` | 律师事务所编号 | number(10) | ✓ |  |  |
| 47 | `SignatureLaw` | 签字律师 | varchar2(100) | ✓ | 79.66% |  |
| 48 | `EvalAgent` | 评估机构 | varchar2(200) | ✓ | 10.4% |  |
| 49 | `EvalAgentCode` | 评估机构编码 | number(10) | ✓ |  |  |
| 50 | `SignatureEvaluator` | 签字评估师 | varchar2(100) | ✓ | 10.34% |  |
| 51 | `IssueSystemType` | 发行制度类型 | number(10) | ✓ | 90.88% | 发行制度类型(IssueSystemType)与(CT_SystemConst)表中的DM字段关联，令LB = 2553... |
| 52 | `DeclareState` | 申报状态 | number(10) | ✓ | 100.0% | 申报状态(DeclareState)与(CT_SystemConst)表中的DM字段关联，令LB = 1691，得到申报... |
| 53 | `TerminationReviewDate` | 终止审查决定日期 | date | ✓ | 0.36% |  |
| 54 | `SuppStatement` | 补充说明 | varchar2(2000) | ✓ | 2.28% |  |
| 55 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 56 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 57 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (申报企业编号)

申报企业编号（CompanyCode）：与“公司概况（LC_StockArchives）”中的“公司代码（CompanyCode）”关联，得到首次公开发行股票申报企业的基本信息。

### IssueMethod (发行方式)

发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB=2344，得到发行方式的具体描述：1-新股发行，2-再融资，3-重大资产重组，4-转板上市。

### InfoSourceCode (信息来源编码)

信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB=2345，得到信息来源编码的具体描述：1-上海证券交易所，2-深圳证券交易所，3-证监会创业板发行监管部，4-证监会发行监管部，5-北京证券交易所，6-证监会网上办事服务平台。

### PlateCode (所属板块)

所属板块(PlateCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1670，得到所属板块的具体描述：1-创业板，2-主板，3-科创板，4-北交所股票。

### IssueObject (发行对象)

发行对象(IssueObject)与(CT_SystemConst)表中的DM字段关联，令LB = 2343，得到发行对象的具体描述：1-向特定对象发行证券，2-向不特定对象发行证券。

### RefinanceMethod (再融资类型)

再融资类型(RefinanceMethod)与(CT_SystemConst)表中的DM字段关联，令LB=1016 AND DM IN (1,17,21,22,23,3,4)，得到再融资类型的具体描述：1-配股，3-增发新股，4-可转换债券，17-优先股发行，21-非公开增发，22-公开增发，23-非公开增发配套融资。

### ReformType (重组类型)

重组类型(ReformType)与(CT_SystemConst)表中的DM字段关联，令LB = 2139，得到重组类型的具体描述：10-协议收购，20-发行股份购买资产，30-二级市场收购（含产权交易所），40-吸收合并，50-增资，60-重组上市，70-发行股份购买资产（小额快速）。

### ReformExamType (重组审核类型)

重组审核类型(ReformExamType)与(CT_SystemConst)表中的DM字段关联，令LB = 2346，得到重组审核类型的具体描述：1-豁免/快速审核，2-正常审核，3-审慎审核。

### RegPlaceCode (注册地代码)

注册地代码(RegPlaceCode)：可关联系统常量表中的DM字段关联，令LB = 1145，得到地区代码的具体描述；也可关联国家城市代码表的“地区行政编码（AreaCode）”关联，得到地区代码的具体描述。

## SQL示例

```sql
-- 查询 A股发行申报企业信息 数据
SELECT *
FROM dz_ipodeclaration
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
