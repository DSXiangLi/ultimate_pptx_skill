# LC_STIBStockArchives

**中文名**: 科创板公司概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBStockArchives` |
| MySQL表名 | `lc_stibstockarchives` |
| 中文名 | 科创板公司概况 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 35 |
| 版本 | 1.04 |

## 表描述

1.内容说明：收录科创板公司的基本情况，包括：联系方式、注册信息、背景资料等内容。
2.数据范围：2019年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上... |
| 3 | `ChiName` | 公司中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `EngName` | 公司英文名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `AExtendedAbbr` | A股扩位简称 | varchar2(100) | ✓ | 62.84% | A股扩位简称（AExtendedAbbr）：根据相关规定，科创板股票及存托凭证应同时提供扩位证券简称。扩位证券简称不少于... |
| 6 | `UnprofitableMark` | 尚未盈利标识 | varchar2(10) | ✓ | 3.97% | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首... |
| 7 | `SpecialVoteMark` | 特殊表决权标识 | varchar2(10) | ✓ | 0.94% | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”... |
| 8 | `RedChipMark` | 红筹企业标识 | varchar2(10) | ✓ | 1.36% | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 |
| 9 | `EstablishmentDate` | 成立日期 | date | ✓ | 100.0% |  |
| 10 | `IRegPlace` | 首次注册登记地点 | varchar2(100) | ✓ | 86.95% |  |
| 11 | `CreditCode` | 统一社会信用代码 | varchar2(20) | ✓ | 98.64% |  |
| 12 | `LegalPersonRepr` | 法人代表 | varchar2(100) | ✓ | 99.9% |  |
| 13 | `RegCapital` | 注册资本(元) | number(19,4) | ✓ | 99.9% |  |
| 14 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 99.9% | 货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND ... |
| 15 | `RegAddr` | 注册地址 | varchar2(200) | ✓ | 100.0% |  |
| 16 | `Province` | 注册地省份 | number(10) | ✓ | 100.0% | 注册地省份（Province）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCo... |
| 17 | `City` | 注册地城市 | number(10) | ✓ | 100.0% | 注册地城市（City）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”... |
| 18 | `RegArea` | 注册地区县 | number(10) | ✓ | 100.0% | 注册地区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCod... |
| 19 | `GeneralManager` | 总经理 | varchar2(100) | ✓ | 95.72% |  |
| 20 | `SecretaryBD` | 董事会秘书 | varchar2(100) | ✓ | 99.06% |  |
| 21 | `SecretaryBDTel` | 董秘电话 | varchar2(100) | ✓ | 100.0% |  |
| 22 | `SecretaryBDFax` | 董秘传真 | varchar2(100) | ✓ | 93.74% |  |
| 23 | `SecretaryBDEmail` | 董秘电子邮件 | varchar2(100) | ✓ | 99.9% |  |
| 24 | `OfficeAddr` | 办公地址 | varchar2(200) | ✓ | 100.0% |  |
| 25 | `OfficeZipCode` | 办公地址邮编 | varchar2(50) | ✓ | 99.79% |  |
| 26 | `ContactAddr` | 联系地址 | varchar2(200) | ✓ | 100.0% |  |
| 27 | `ContactZip` | 联系地址邮编 | varchar2(50) | ✓ | 99.79% |  |
| 28 | `ContactTel` | 联系人电话 | varchar2(100) | ✓ | 99.69% |  |
| 29 | `ContactFax` | 联系人传真 | varchar2(100) | ✓ | 91.75% |  |
| 30 | `Email` | 联系人电邮 | varchar2(100) | ✓ | 99.9% |  |
| 31 | `Website` | 公司官方网站 | varchar2(100) | ✓ | 99.48% |  |
| 32 | `BriefIntroText` | 公司简介 | clob | ✓ | 14.41% |  |
| 33 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 34 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 35 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，上市板块(ListedSector)=7，得到科创板上市公司的交易代码、简称等。

### AExtendedAbbr (A股扩位简称)

A股扩位简称（AExtendedAbbr）：根据相关规定，科创板股票及存托凭证应同时提供扩位证券简称。扩位证券简称不少于4个汉字（6个字符），且不超过8个汉字（16个字符）。

### UnprofitableMark (尚未盈利标识)

尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。

### SpecialVoteMark (特殊表决权标识)

特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。

### RedChipMark (红筹企业标识)

红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1420,1000,1100)，得到货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### Province (注册地省份)

注册地省份（Province）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到注册地省份具体信息。

### City (注册地城市)

注册地城市（City）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到注册地城市具体信息。

### RegArea (注册地区县)

注册地区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到注册地区县具体信息。

## SQL示例

```sql
-- 查询 科创板公司概况 数据
SELECT *
FROM lc_stibstockarchives
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
