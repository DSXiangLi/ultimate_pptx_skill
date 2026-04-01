# MF_InvestAdvisorOutline

**中文名**: 公募基金管理人概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InvestAdvisorOutline` |
| MySQL表名 | `mf_investadvisoroutline` |
| 中文名 | 公募基金管理人概况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 28 |
| 版本 | 1.02 |

## 表描述

1.本表记录了基金管理人的基本情况介绍，包括成立日期、注册资本、法人代表、联系方式、背景简介等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InvestAdvisorCode` | 基金管理人编码 | number(10) | ✗ | 100.0% | 基金管理人编码(InvestAdvisorCode)：与机构基本资料(LC_InstiArchive)表的企业编号(Co... |
| 3 | `InvestAdvisorName` | 基金管理人名称 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `InvestAdvisorAbbrName` | 基金管理人简称 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `LegalRepr` | 法人代表 | varchar2(50) | ✓ | 77.03% |  |
| 6 | `GeneralManager` | 总经理 | varchar2(50) | ✓ | 77.39% |  |
| 7 | `EstablishmentDate` | 成立日期 | date | ✓ | 95.05% |  |
| 8 | `MaturityEndDate` | 存续截止日 | date | ✓ | 0.35% |  |
| 9 | `OrganizationForm` | 组织形式 | varchar2(50) | ✓ | 100.0% | 组织形式(OrganizationForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1133 ... |
| 10 | `EmployeeNum` | 员工人数 | number(10) | ✓ | 76.41% |  |
| 11 | `RegCapital` | 注册资本(元) | number(18,4) | ✓ | 77.03% |  |
| 12 | `RegCapitalCurrency` | 注册资本货币单位 | number(10) | ✓ | 80.63% | 注册资本货币单位(RegCapitalCurrency)与(CT_SystemConst)表中的DM字段关联，令LB =... |
| 13 | `RegAddr` | 注册地址 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `OfficeAddr` | 办公地址 | varchar2(100) | ✓ | 92.58% |  |
| 15 | `ZipCode` | 邮编 | varchar2(6) | ✓ | 69.26% |  |
| 16 | `Email` | 邮箱 | varchar2(50) | ✓ | 78.45% |  |
| 17 | `ContactAddr` | 联系地址 | varchar2(100) | ✓ | 91.52% |  |
| 18 | `Tel` | 联系电话 | varchar2(50) | ✓ | 87.63% |  |
| 19 | `Fax` | 传真 | varchar2(50) | ✓ | 75.27% |  |
| 20 | `WebSite` | 公司网址 | varchar2(50) | ✓ | 83.04% |  |
| 21 | `LinkMan` | 联系人 | varchar2(50) | ✓ | 71.02% |  |
| 22 | `ServiceLine` | 客服热线 | varchar2(50) | ✓ | 74.91% |  |
| 23 | `Region` | 所属地区 | number(10) | ✓ | 100.0% | 所属地区(Region)与系统常量表表中的DM字段关联，令LB = 1145，得到所属地区的具体描述 |
| 24 | `TACode` | 注册登记代码 | varchar2(20) | ✓ | 73.5% |  |
| 25 | `CSRCCode` | 证监会标识码 | varchar2(20) | ✓ | 0.0% |  |
| 26 | `Background` | 背景介绍 | clob | ✓ | 50.88% |  |
| 27 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 28 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InvestAdvisorCode (基金管理人编码)

基金管理人编码(InvestAdvisorCode)：与机构基本资料(LC_InstiArchive)表的企业编号(CompanyCode)字段关联，可查询基金管理人中文名称、英文名称、组织机构代码等基本信息。

### OrganizationForm (组织形式)

组织形式(OrganizationForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1133 and DM in (100,150,159,160,210,310,900)，得到组织形式的具体描述：100-内资企业，150-有限责任公司，159-其他有限责任公司，160-股份有限公司，210-港澳台合资经营企业，310-中外合资经营企业，900-其他性质。

### RegCapitalCurrency (注册资本货币单位)

注册资本货币单位(RegCapitalCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1548 and DM in (1000,1100,1420)，得到注册资本货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### Region (所属地区)

所属地区(Region)与系统常量表表中的DM字段关联，令LB = 1145，得到所属地区的具体描述

## SQL示例

```sql
-- 查询 公募基金管理人概况 数据
SELECT *
FROM mf_investadvisoroutline
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
