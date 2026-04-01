# FP_RelatedInstitutions

**中文名**: 金融产品相关机构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_RelatedInstitutions` |
| MySQL表名 | `fp_relatedinstitutions` |
| 中文名 | 金融产品相关机构 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品主体信息 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录金融产品的相关主体机构。
2.信息来源：银行、信托、证券、资产管理公司、保险公司官网。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 34.36% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `AgentType` | 机构类别 | varchar2(12) | ✗ | 100.0% | 机构类别（AgentType）：FCC000000VIN-管理人，FCC000001EA3-托管人，FCC000001E... |
| 6 | `EnterpriseCode` | 企业编码 | varchar2(12) | ✗ | 100.0% | 企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（Enterpr... |
| 7 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 8 | `AgentName` | 机构名称 | varchar2(100) | ✓ | 100.0% |  |
| 9 | `StartDate` | 启用日期 | date | ✓ | 94.14% |  |
| 10 | `EndDate` | 终止日期 | date | ✓ | 89.81% |  |
| 11 | `IfEffected` | 是否有效 | varchar2(12) | ✓ | 100.0% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：F... |
| 12 | `SaleCode` | 销售代码 | varchar2(50) | ✓ | 0.65% |  |
| 13 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### AgentType (机构类别)

机构类别（AgentType）：FCC000000VIN-管理人，FCC000001EA3-托管人，FCC000001EA4-注册登记人，FCC000001EA5-销售机构。

### EnterpriseCode (企业编码)

企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### IfEffected (是否有效)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：FCC000000005-是，FCC000000006-否。

## SQL示例

```sql
-- 查询 金融产品相关机构 数据
SELECT *
FROM fp_relatedinstitutions
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
