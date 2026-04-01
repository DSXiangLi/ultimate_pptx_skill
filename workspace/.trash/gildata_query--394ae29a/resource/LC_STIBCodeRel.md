# LC_STIBCodeRel

**中文名**: 科创板公司代码关联

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCodeRel` |
| MySQL表名 | `lc_stibcoderel` |
| 中文名 | 科创板公司代码关联 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

本表记录国内科创板上市公司对应的三板等关联代码的信息。包括： 关联代码内部编码、关联代码公司代码等内容。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 科创板证券内部编码 | number(10) | ✗ | 100.0% | 科创板证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `CompanyCode` | 科创板公司代码 | number(10) | ✗ | 100.0% | 科创板公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关... |
| 4 | `CodeDefine` | 代码关联类型 | number(10) | ✗ | 100.0% | 代码关联类型(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 1350 AND ... |
| 5 | `RelatedInnerCode` | 关联证券内部编码 | number(10) | ✗ | 100.0% | 关联代码内部编码（RelatedInnerCode）：代码关联类型（CodeDefine）等于10时，与“港股证券主表（... |
| 6 | `RelatedCompanyCode` | 关联证券公司代码 | number(10) | ✗ | 100.0% | 关联代码公司代码（RelatedCompanyCode）：代码关联类型（CodeDefine）等于10时，与“港股证券主... |
| 7 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 8 | `EndDate` | 截止日期 | date | ✓ | 1.21% |  |
| 9 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (科创板证券内部编码)

科创板证券代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (科创板公司代码)

科创板公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### CodeDefine (代码关联类型)

代码关联类型(CodeDefine)与(CT_SystemConst)表中的DM字段关联，令LB = 1350 AND DM IN (10,100,101,107)，得到代码关联类型的具体描述：10-跨市场公司关联，100-三板转A股，101-A股转三板，107-北交所转科创板。

### RelatedInnerCode (关联证券内部编码)

关联代码内部编码（RelatedInnerCode）：代码关联类型（CodeDefine）等于10时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联。代码关联类型（CodeDefine）等于100时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联。

### RelatedCompanyCode (关联证券公司代码)

关联代码公司代码（RelatedCompanyCode）：代码关联类型（CodeDefine）等于10时，与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联。代码关联类型（CodeDefine）等于100时，与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM in (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 科创板公司代码关联 数据
SELECT *
FROM lc_stibcoderel
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
