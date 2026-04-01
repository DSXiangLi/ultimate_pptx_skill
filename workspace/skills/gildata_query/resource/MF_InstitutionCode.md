# MF_InstitutionCode

**中文名**: 公募基金参与机构代码表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InstitutionCode` |
| MySQL表名 | `mf_institutioncode` |
| 中文名 | 公募基金参与机构代码表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金主体信息 |
| 更新频率 | 不定期更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

1. 本表记录公募基金参与机构在各类业务中的编码,包括公募产品直销编码、公募产品代销编码、投资管理人TA、资管产品直销编码等。
2. 信息来源:中国资本市场标准网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 企业编号 | number(10) | ✗ | 100.0% | 企业编号(CompanyCode):与机构基本资料(LC_InstiArchive)表的企业编号(CompanyCode... |
| 3 | `CodeType` | 编码类型 | number(10) | ✗ | 100.0% | 编码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1743 and DM i... |
| 4 | `RelatedCode` | 对应编码 | varchar2(50) | ✗ | 100.0% |  |
| 5 | `StartDate` | 启用日期 | date | ✓ | 0.0% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (企业编号)

企业编号(CompanyCode):与机构基本资料(LC_InstiArchive)表的企业编号(CompanyCode)字段关联,可查询机构的中文名称、英文名称、组织机构代码等基本信息。

### CodeType (编码类型)

编码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1743 and DM in (2,4,7,8,9,10,11)，得到编码类型的具体描述：2-基金公司证监会编码，4-注册登记机构编码（中登），7-公募产品直销编码，8-公募产品代销编码，9-资管产品直销编码，10-投资管理人TA，11-外包TA。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金参与机构代码表 数据
SELECT *
FROM mf_institutioncode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
