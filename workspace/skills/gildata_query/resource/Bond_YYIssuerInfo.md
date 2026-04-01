# Bond_YYIssuerInfo

**中文名**: YY主体信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_YYIssuerInfo` |
| MySQL表名 | `bond_yyissuerinfo` |
| 中文名 | YY主体信息 |
| 路径 | 聚源新版数据库 > 产品代理 > 瑞霆狗代理数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 54 |
| 版本 | 1 |

## 表描述

1.内容说明：本表收录全市场发债主体最新YY评级，主体隐含评级，行业分类，对于主体的点评信息以及不同类型主体的特有指标。
2.数据范围：2024年9月13日至今
2.信息来源：瑞霆狗(深圳)信息技术有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `CompanyType` | 公司类型 | number(10) | ✓ | 100.0% | 公司类型(CompanyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2640，得到公司类... |
| 6 | `CRCode` | 最新评级代码 | number(10) | ✓ | 100.0% | 最新评级代码(CRCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2637，得到最新评级代码... |
| 7 | `CRDesc` | 最新评级描述 | varchar2(50) | ✓ | 100.0% |  |
| 8 | `CRStatus` | 评级状态 | number(10) | ✓ | 100.0% | 评级状态(CRStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2042，得到评级状态的具... |
| 9 | `ImpliedGrade` | 隐含评级 | number(14,4) | ✓ | 50.18% |  |
| 10 | `ExternalRating` | 外部评级 | varchar2(50) | ✓ | 79.47% |  |
| 11 | `CROutlook` | 外部评级展望 | number(10) | ✓ | 76.85% | 外部评级展望(CROutlook)与(CT_SystemConst)表中的DM字段关联，令LB = 1704 and D... |
| 12 | `CRAsName` | 评级机构名称 | varchar2(200) | ✓ | 79.47% |  |
| 13 | `CRAsCode` | 评级机构代码 | number(10) | ✓ | 79.47% | 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名... |
| 14 | `MSHName` | 大股东名称 | varchar2(120) | ✓ | 93.58% |  |
| 15 | `SHID` | 股东ID | number(10) | ✓ | 75.65% | 与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名... |
| 16 | `MSHPercentage` | 持股比例(%) | number(9,6) | ✓ | 93.56% |  |
| 17 | `CompanyCval` | 公司属性 | number(10) | ✓ | 100.0% | 公司属性(CompanyCval)与(CT_SystemConst)表中的DM字段关联，令LB = 1096 and D... |
| 18 | `IfListed` | 是否上市 | number(10) | ✓ | 100.0% | 是否上市(IfListed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in... |
| 19 | `ReportDate` | 报告期 | date | ✓ | 82.23% |  |
| 20 | `CreditAnalysis` | 信用分析 | clob | ✓ | 80.15% |  |
| 21 | `IndustryAnalysis` | 行业分析 | varchar2(2000) | ✓ | 27.34% |  |
| 22 | `ShareHolderAnalysis` | 股东分析 | varchar2(2000) | ✓ | 27.39% |  |
| 23 | `OperatingAnalysis` | 经营分析 | varchar2(2000) | ✓ | 36.06% |  |
| 24 | `FinancialAnalysis` | 财务分析 | varchar2(2000) | ✓ | 36.08% |  |
| 25 | `KeyPoints` | 重点关注 | varchar2(2000) | ✓ | 27.36% |  |
| 26 | `CorpGovernance` | 公司治理 | varchar2(2000) | ✓ | 8.65% |  |
| 27 | `ReguIndicator` | 监管指标 | varchar2(2000) | ✓ | 8.57% |  |
| 28 | `YYFirstIndustry` | YY一级行业 | varchar2(100) | ✓ | 40.81% |  |
| 29 | `YYSecondIndustry` | YY二级行业 | varchar2(100) | ✓ | 40.81% |  |
| 30 | `Country` | 所属国家 | varchar2(50) | ✓ | 41.64% |  |
| 31 | `Province` | 所属省份 | varchar2(50) | ✓ | 41.63% |  |
| 32 | `ProvinceCode` | 所属省份代码 | number(10) | ✓ | 41.63% | 与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码... |
| 33 | `City` | 所属城市 | varchar2(50) | ✓ | 37.55% |  |
| 34 | `CityCode` | 所属城市代码 | number(10) | ✓ | 37.33% | 与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码... |
| 35 | `District` | 所属区县 | varchar2(100) | ✓ | 29.89% |  |
| 36 | `DistrictCode` | 所属区县代码 | number(10) | ✓ | 24.64% | 与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码... |
| 37 | `Town` | 所属镇 | varchar2(100) | ✓ | 2.16% |  |
| 38 | `TownCode` | 所属镇代码 | number(10) | ✓ | 0.26% | 与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码... |
| 39 | `Grade` | 行政级别 | varchar2(100) | ✓ | 41.64% |  |
| 40 | `ReguRating` | 监管级别 | varchar2(100) | ✓ | 1.09% |  |
| 41 | `ReguRatingCode` | 监管级别代码 | number(10) | ✓ | 1.09% | 监管级别代码(ReguRatingCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2002，... |
| 42 | `InsuranceCorpType` | 保险公司类别 | varchar2(100) | ✓ | 0.66% |  |
| 43 | `AreaImportance` | 平台重要性 | number(10) | ✓ | 41.24% | 平台重要性(AreaImportance)与(CT_SystemConst)表中的DM字段关联，令LB = 2531 a... |
| 44 | `BusinessType` | 城投平台业务类型 | number(10) | ✓ | 41.24% | 城投平台业务类型(BusinessType)与(CT_SystemConst)表中的DM字段关联，令LB = 2528 ... |
| 45 | `GDP` | 地区生产总值(亿元) | number(14,4) | ✓ | 36.75% |  |
| 46 | `GenPublicBudgetRev` | 一般公共预算收入(亿元) | number(14,4) | ✓ | 40.21% |  |
| 47 | `GovFundsRev` | 政府性基金收入(亿元) | number(14,4) | ✓ | 36.64% |  |
| 48 | `YYRatio` | YY负债率(%) | number(14,4) | ✓ | 38.89% |  |
| 49 | `PublicBusRatio` | 公益性资产占比(%) | number(14,4) | ✓ | 31.07% |  |
| 50 | `IndicatorYear` | 指标年份 | number(10) | ✓ | 41.45% |  |
| 51 | `AreaAnalysis` | 区域分析 | clob | ✓ | 41.43% |  |
| 52 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 53 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 54 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyType (公司类型)

公司类型(CompanyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2640，得到公司类型的具体描述：1-产业，2-城投，3-金融。

### CRCode (最新评级代码)

最新评级代码(CRCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2637，得到最新评级代码的具体描述：10--2，11--1，12-0，20-1，21-2，22-3，23-4+，24-4，25-4-，26-5+，27-5，28-5-，29-6+，30-6，31-6-，32-7+，33-7，34-7-，35-8+，36-8，37-8-，38-9，39-10。

### CRStatus (评级状态)

评级状态(CRStatus)与(CT_SystemConst)表中的DM字段关联，令LB = 2042，得到评级状态的具体描述：1-正常，2-失效。

### CROutlook (外部评级展望)

外部评级展望(CROutlook)与(CT_SystemConst)表中的DM字段关联，令LB = 1704 and DM in (1201,1202,1203)，得到外部评级展望的具体描述：1201-正面，1202-稳定，1203-负面。

### CRAsCode (评级机构代码)

与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### SHID (股东ID)

与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyCval (公司属性)

公司属性(CompanyCval)与(CT_SystemConst)表中的DM字段关联，令LB = 1096 and DM in (6,7,10,11,12,16)，得到公司属性的具体描述：6-民营，7-集体企业，10-中央国有企业，11-国有企业，12-地方国有企业，16-公众企业。

### IfListed (是否上市)

是否上市(IfListed)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否上市的具体描述：1-是，2-否。

### ProvinceCode (所属省份代码)

与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到地区的行政编码、中文名称等。

## SQL示例

```sql
-- 查询 YY主体信息 数据
SELECT *
FROM bond_yyissuerinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
