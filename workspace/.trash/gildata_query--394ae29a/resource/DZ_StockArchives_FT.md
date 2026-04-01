# DZ_StockArchives_FT

**中文名**: A股公司概况_繁体

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_StockArchives_FT` |
| MySQL表名 | `dz_stockarchives_ft` |
| 中文名 | A股公司概况_繁体 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 54 |
| 版本 | 1 |

## 表描述

收录上市公司（包括科创板）的基本情况，包括：内容说明、数据范围、信息来源、联系方式、注册信息、中介机构、行业和产品、公司证券品种及背景资料等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `ChiName` | 公司中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `ExtendedAbbr` | 扩位简称 | varchar2(100) | ✓ | 4.0% | 扩位简称（ExtendedAbbr）：根据相关规定，扩位证券简称不少于4个汉字（6个字符），且不超过8个汉字（16个字符... |
| 5 | `UnprofitableMark` | 尚未盈利标识 | varchar2(10) | ✓ | 0.17% | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首... |
| 6 | `SpecialVoteMark` | 特殊表决权标识 | varchar2(10) | ✓ | 0.04% | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”... |
| 7 | `VIEMark` | 协议控制架构标识 | varchar2(10) | ✓ | 0.0% | 协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”... |
| 8 | `RedChipMark` | 红筹企业标识 | varchar2(10) | ✓ | 0.08% | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 |
| 9 | `State` | 省份 | number(10) | ✗ | 100.0% | 省份(State)与(CT_SystemConst)表中的DM字段关联，令LB=1145，得到省份的具体描述： |
| 10 | `SecretaryBD` | 董事会秘书 | varchar2(100) | ✓ | 98.06% |  |
| 11 | `SecretaryBDTel` | 董秘电话 | varchar2(100) | ✓ | 99.41% |  |
| 12 | `SecretaryBDFax` | 董秘传真 | varchar2(100) | ✓ | 95.42% |  |
| 13 | `SecretaryBDEmail` | 董秘电子邮件 | varchar2(100) | ✓ | 93.86% |  |
| 14 | `SecuAffairsRepr` | 证券/股证事务代表 | varchar2(100) | ✓ | 25.97% |  |
| 15 | `SecuAffairsReprTel` | 证券事务代表电话 | varchar2(100) | ✓ | 24.45% |  |
| 16 | `SecuAffairsReprFax` | 证券事务代表传真 | varchar2(100) | ✓ | 23.41% |  |
| 17 | `SecuAffairsReprEmail` | 证券事务代表电子邮件 | varchar2(100) | ✓ | 24.27% |  |
| 18 | `AuthReprSBD` | 董秘授权代表 | varchar2(20) | ✓ | 0.0% |  |
| 19 | `ContactTel` | 联系人电话 | varchar2(60) | ✓ | 99.81% |  |
| 20 | `ContactFax` | 联系人传真 | varchar2(60) | ✓ | 95.59% |  |
| 21 | `ContactEmail` | 联系人电子邮箱 | varchar2(100) | ✓ | 94.24% |  |
| 22 | `RegAddr` | 公司注册地址 | varchar2(200) | ✓ | 100.0% |  |
| 23 | `RegZipCode` | 公司注册地址邮编 | varchar2(6) | ✓ | 90.2% |  |
| 24 | `OfficeAddr` | 公司办公地址 | varchar2(200) | ✓ | 99.99% |  |
| 25 | `OfficeZipCode` | 公司办公地址邮编 | varchar2(6) | ✓ | 99.84% |  |
| 26 | `ContactAddr` | 公司联系地址 | varchar2(200) | ✓ | 100.0% |  |
| 27 | `ConatactZipCode` | 公司联系地址邮编 | varchar2(6) | ✓ | 99.97% |  |
| 28 | `Email` | 公司电子邮箱 | varchar2(100) | ✓ | 98.32% |  |
| 29 | `Website` | 公司网址 | varchar2(100) | ✓ | 93.57% |  |
| 30 | `DisclosureWebsites` | 信息披露网址 | varchar2(160) | ✓ | 89.3% |  |
| 31 | `DisclosurePapers` | 信息披露报纸 | varchar2(160) | ✓ | 24.83% |  |
| 32 | `EstablishmentDate` | 公司成立日期 | date | ✓ | 100.0% |  |
| 33 | `IRegPlace` | 首次注册登记地点 | varchar2(100) | ✓ | 86.6% |  |
| 34 | `BusinessRegNumber` | 企业法人营业执照注册号 | varchar2(100) | ✓ | 97.94% |  |
| 35 | `LegalRepr` | 法人代表1 | varchar2(100) | ✓ | 99.98% |  |
| 36 | `GeneralManager` | 总经理 | varchar2(100) | ✓ | 91.99% |  |
| 37 | `LegalConsultant` | 法律顾问 | varchar2(200) | ✓ | 32.61% |  |
| 38 | `AccountingFirm` | 会计师事务所 | varchar2(200) | ✓ | 34.04% |  |
| 39 | `InduCSRC` | 公司所属证监会行业(聚源) | number(10) | ✓ | 99.59% |  |
| 40 | `BusinessMajor` | 经营范围-主营 | clob | ✓ | 100.0% |  |
| 41 | `BusinessMinor` | 经营范围-兼营 | clob | ✓ | 0.17% |  |
| 42 | `AShareAbbr` | A股证券简称 | varchar2(100) | ✓ | 52.28% |  |
| 43 | `AStockCode` | A股证券代码 | varchar2(10) | ✓ | 52.28% |  |
| 44 | `BShareAbbr` | B股证券简称 | varchar2(100) | ✓ | 0.45% |  |
| 45 | `BStockCode` | B股证券代码 | varchar2(10) | ✓ | 0.45% |  |
| 46 | `HShareAbbr` | H股证券简称 | varchar2(20) | ✓ | 0.75% |  |
| 47 | `HStockCode` | H股证券代码 | varchar2(10) | ✓ | 0.75% |  |
| 48 | `CDRShareAbbr` | CDR证券简称 | varchar2(100) | ✓ | 0.0% |  |
| 49 | `CDRStockCode` | CDR证券代码 | varchar2(10) | ✓ | 0.0% |  |
| 50 | `BriefIntroText` | 公司简介 | clob | ✓ | 99.81% |  |
| 51 | `CityCode` | 地区代码1 | number(10) | ✓ | 100.0% |  |
| 52 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 53 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 54 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ExtendedAbbr (扩位简称)

扩位简称（ExtendedAbbr）：根据相关规定，扩位证券简称不少于4个汉字（6个字符），且不超过8个汉字（16个字符）。

### UnprofitableMark (尚未盈利标识)

尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。

### SpecialVoteMark (特殊表决权标识)

特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。

### VIEMark (协议控制架构标识)

协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”；上市后不再具有相关安排的，该特别标识取消，数据值为空。

### RedChipMark (红筹企业标识)

红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。

### State (省份)

省份(State)与(CT_SystemConst)表中的DM字段关联，令LB=1145，得到省份的具体描述：

## SQL示例

```sql
-- 查询 A股公司概况_繁体 数据
SELECT *
FROM dz_stockarchives_ft
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
