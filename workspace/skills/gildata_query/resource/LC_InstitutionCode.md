# LC_InstitutionCode

**中文名**: 机构常用编码表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_InstitutionCode` |
| MySQL表名 | `lc_institutioncode` |
| 中文名 | 机构常用编码表 |
| 路径 | 聚源新版数据库 > 机构数据库 > 机构基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1、收录机构相关的各类编码，包括基金公司证监会编码、注册登记机构编码（中登）、swift码、公募产品直销编码、公募产品代销编码、资管产品直销编码、投资管理人TA、外包TA
2、数据源：证监会、中国证券登记结算有限责任公司、环球银行金融电信协会、中国资本市场标准网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 3 | `CompanyName` | 披露企业名称 | varchar2(100) | ✗ | 100.0% |  |
| 4 | `CodeType` | 编码类型 | number(10) | ✗ | 100.0% | 编码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1743 AND DM N... |
| 5 | `RelatedCode` | 对应编码 | varchar2(50) | ✗ | 100.0% |  |
| 6 | `StartDate` | 启用日期 | date | ✓ | 2.08% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN... |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### CodeType (编码类型)

编码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1743 AND DM NOT IN (1,3,5,11,12)，得到编码类型的具体描述：2-基金公司证监会编码，4-注册登记机构编码（中登），6-swift码，7-公募产品直销编码，8-公募产品代销编码，9-资管产品直销编码，10-投资管理人TA，13-公募外包TA，14-私募外包TA，15-LEI编码，16-基金投资顾问业务编码，17-基金托管人证监会编码，18-商业登记号码。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 机构常用编码表 数据
SELECT *
FROM lc_institutioncode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
