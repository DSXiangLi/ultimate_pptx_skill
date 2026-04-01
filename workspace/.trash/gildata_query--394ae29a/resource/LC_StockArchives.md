# LC_StockArchives

**中文名**: 公司概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_StockArchives` |
| MySQL表名 | `lc_stockarchives` |
| 中文名 | 公司概况 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 54 |
| 版本 | 1.06 |

## 表描述

收录上市公司的基本情况，包括：联系方式、注册信息、中介机构、行业和产品、公司证券品种及背景资料等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `ChiName` | 公司中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `ExtendedAbbr` | 扩位简称 | varchar2(100) | ✓ | 2.5% |  |
| 5 | `UnprofitableMark` | 尚未盈利标识 | varchar2(10) | ✓ | 0.02% | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首... |
| 6 | `SpecialVoteMark` | 特殊表决权标识 | varchar2(10) | ✓ | 0.0% | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”... |
| 7 | `VIEMark` | 协议控制架构标识 | varchar2(10) | ✓ | 0.0% | 协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”... |
| 8 | `RedChipMark` | 红筹企业标识 | varchar2(10) | ✓ | 0.03% | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 |
| 9 | `State` | 省份 | number(10) | ✗ | 100.0% | 省份（State）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联... |
| 10 | `SecretaryBD` | 董事会秘书 | varchar2(100) | ✓ | 98.04% |  |
| 11 | `SecretaryBDTel` | 董秘电话 | varchar2(100) | ✓ | 99.41% |  |
| 12 | `SecretaryBDFax` | 董秘传真 | varchar2(100) | ✓ | 95.39% |  |
| 13 | `SecretaryBDEmail` | 董秘电子邮件 | varchar2(100) | ✓ | 97.69% |  |
| 14 | `SecuAffairsRepr` | 证券/股证事务代表 | varchar2(100) | ✓ | 25.9% |  |
| 15 | `SecuAffairsReprTel` | 证券事务代表电话 | varchar2(100) | ✓ | 24.26% |  |
| 16 | `SecuAffairsReprFax` | 证券事务代表传真 | varchar2(100) | ✓ | 23.3% |  |
| 17 | `SecuAffairsReprEmail` | 证券事务代表电子邮件 | varchar2(100) | ✓ | 24.08% |  |
| 18 | `AuthReprSBD` | 董秘授权代表 | varchar2(20) | ✓ | 0.0% |  |
| 19 | `ContactTel` | 联系人电话 | varchar2(60) | ✓ | 99.86% |  |
| 20 | `ContactFax` | 联系人传真 | varchar2(60) | ✓ | 95.63% |  |
| 21 | `ContactEmail` | 联系人电子邮箱 | varchar2(100) | ✓ | 98.11% |  |
| 22 | `RegAddr` | 公司注册地址 | varchar2(200) | ✓ | 100.0% |  |
| 23 | `RegZipCode` | 公司注册地址邮编 | varchar2(50) | ✓ | 90.25% |  |
| 24 | `OfficeAddr` | 公司办公地址 | varchar2(200) | ✓ | 100.0% |  |
| 25 | `OfficeZipCode` | 公司办公地址邮编 | varchar2(50) | ✓ | 99.98% |  |
| 26 | `ContactAddr` | 公司联系地址 | varchar2(200) | ✓ | 100.0% |  |
| 27 | `ConatactZipCode` | 公司联系地址邮编 | varchar2(50) | ✓ | 99.98% |  |
| 28 | `Email` | 公司电子邮箱 | varchar2(100) | ✓ | 98.71% |  |
| 29 | `Website` | 公司网址 | varchar2(100) | ✓ | 94.06% |  |
| 30 | `DisclosureWebsites` | 信息披露网址 | varchar2(160) | ✓ | 93.96% |  |
| 31 | `DisclosurePapers` | 信息披露报纸 | varchar2(160) | ✓ | 24.88% |  |
| 32 | `EstablishmentDate` | 公司成立日期 | date | ✓ | 100.0% |  |
| 33 | `IRegPlace` | 首次注册登记地点 | varchar2(100) | ✓ | 90.33% |  |
| 34 | `BusinessRegNumber` | 企业法人营业执照注册号 | varchar2(100) | ✓ | 97.89% |  |
| 35 | `LegalRepr` | 法人代表 | varchar2(100) | ✓ | 99.99% |  |
| 36 | `GeneralManager` | 总经理 | varchar2(100) | ✓ | 92.12% |  |
| 37 | `LegalConsultant` | 法律顾问 | varchar2(200) | ✓ | 31.97% |  |
| 38 | `AccountingFirm` | 会计师事务所 | varchar2(200) | ✓ | 33.5% |  |
| 39 | `InduCSRC` | 公司所属证监会行业(聚源) | number(10) | ✓ | 99.86% | 与(CT_IndustryType)表中的"行业内部编码(IndustryNum)"字段关联,当Standard=1时,... |
| 40 | `BusinessMajor` | 经营范围-主营 | clob | ✓ | 0.64% |  |
| 41 | `BusinessMinor` | 经营范围-兼营 | clob | ✓ | 0.09% |  |
| 42 | `AShareAbbr` | A股证券简称 | varchar2(100) | ✓ | 54.26% |  |
| 43 | `AStockCode` | A股证券代码 | varchar2(10) | ✓ | 54.26% |  |
| 44 | `BShareAbbr` | B股证券简称 | varchar2(100) | ✓ | 0.48% |  |
| 45 | `BStockCode` | B股证券代码 | varchar2(10) | ✓ | 0.48% |  |
| 46 | `HShareAbbr` | H股证券简称 | varchar2(20) | ✓ | 0.76% |  |
| 47 | `HStockCode` | H股证券代码 | varchar2(10) | ✓ | 0.76% |  |
| 48 | `CDRShareAbbr` | CDR证券简称 | varchar2(100) | ✓ | 0.0% |  |
| 49 | `CDRStockCode` | CDR证券代码 | varchar2(10) | ✓ | 0.0% |  |
| 50 | `BriefIntroText` | 公司简介 | clob | ✓ | 0.65% |  |
| 51 | `CityCode` | 地区代码 | number(10) | ✓ | 100.0% | 地区代码(CityCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCod... |
| 52 | `RegArea` | 所属区县 | number(10) | ✓ | 100.0% | 所属区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode... |
| 53 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 54 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### UnprofitableMark (尚未盈利标识)

尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。

### SpecialVoteMark (特殊表决权标识)

特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。

### VIEMark (协议控制架构标识)

协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”；上市后不再具有相关安排的，该特别标识取消，数据值为空。

### RedChipMark (红筹企业标识)

红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。

### State (省份)

省份（State）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到省份具体信息。

### InduCSRC (公司所属证监会行业(聚源))

与(CT_IndustryType)表中的"行业内部编码(IndustryNum)"字段关联,当Standard=1时,LB=1；当Standard=22时,LB=22；当Standard=25时,LB=25；当Standard=26时,LB=26。

### CityCode (地区代码)

地区代码(CityCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到城市具体信息。

### RegArea (所属区县)

所属区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到所属区县具体信息。

## SQL示例

```sql
-- 查询 公司概况 数据
SELECT *
FROM lc_stockarchives
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
