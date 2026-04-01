# HK_CompanyArchives

**中文名**: 港股企业概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_CompanyArchives` |
| MySQL表名 | `hk_companyarchives` |
| 中文名 | 港股企业概况 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 30 |
| 版本 | 1.01 |

## 表描述

1.记录香港证券相关的上市/非上市企业基本信息。
2.数据来源：港交所、香港公司注册处综合资讯系统等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `ChiName` | 中文名称 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `ChiNameAbbr` | 中文简称 | varchar2(100) | ✓ | 68.82% |  |
| 5 | `ChiSpelling` | 简称拼音 | varchar2(100) | ✓ | 52.82% |  |
| 6 | `EngName` | 英文名称 | varchar2(200) | ✓ | 84.66% |  |
| 7 | `EngNameAbbr` | 英文简称 | varchar2(100) | ✓ | 27.46% |  |
| 8 | `EstablishmentDate` | 成立日期 | date | ✓ | 69.2% |  |
| 9 | `RegCapital` | 注册资本(元) | number(18,3) | ✓ | 45.49% |  |
| 10 | `AuthorizedCapital` | 法定股本(元) | number(18,3) | ✓ | 23.79% |  |
| 11 | `ParValue` | 面值 | number(19,10) | ✓ | 23.97% |  |
| 12 | `CurrencyUnit` | 货币单位 | number(10) | ✓ | 45.48% | 货币单位(CurrencyUnit)：与系统常量表中的DM字段关联，令LB = 1068 AND DM NOT IN (... |
| 13 | `RegAddr` | 注册地址 | varchar2(400) | ✓ | 81.86% |  |
| 14 | `RegCountry` | 注册国家 | number(10) | ✓ | 40.7% | 注册国家（RegCountry）：与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerC... |
| 15 | `RegArea` | 注册地城市 | number(10) | ✓ | 83.69% | 注册地城市（RegArea）：与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerCod... |
| 16 | `RegZip` | 注册地址邮编 | varchar2(100) | ✓ | 20.6% |  |
| 17 | `HeadOfficeAddress` | 总部地址 | varchar2(400) | ✓ | 46.67% |  |
| 18 | `HKOffice` | 香港营业地点 | varchar2(400) | ✓ | 29.97% |  |
| 19 | `Chairman` | 主席 | varchar2(100) | ✓ | 23.61% |  |
| 20 | `Tel` | 电话 | varchar2(200) | ✓ | 51.0% |  |
| 21 | `Fax` | 传真 | varchar2(200) | ✓ | 25.9% |  |
| 22 | `Email` | 邮箱 | varchar2(200) | ✓ | 42.17% |  |
| 23 | `Website` | 网址链接 | varchar2(200) | ✓ | 33.98% |  |
| 24 | `BriefIntroText` | 公司简介 | clob | ✓ | 5.7% |  |
| 25 | `MainBusiness` | 主营业务 | clob | ✓ | 7.92% |  |
| 26 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 27 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |
| 29 | `IfExisted` | 是否存在 | number(10) | ✓ | 100.0% | 是否存在(IfExisted)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN ... |
| 30 | `CloseDate` | 存续截止日期 | date | ✓ | 1.45% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

### CurrencyUnit (货币单位)

货币单位(CurrencyUnit)：与系统常量表中的DM字段关联，令LB = 1068 AND DM NOT IN (3450)，得到货币单位的具体描述。

### RegCountry (注册国家)

注册国家（RegCountry）：与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerCode)”关联，得到注册国家的相关信息。

### RegArea (注册地城市)

注册地城市（RegArea）：与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerCode)”关联，得到注册地城市的相关信息。

### IfExisted (是否存在)

是否存在(IfExisted)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否存在的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 港股企业概况 数据
SELECT *
FROM hk_companyarchives
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
