# FP_SecuMain

**中文名**: 金融产品主表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_SecuMain` |
| MySQL表名 | `fp_secumain` |
| 中文名 | 金融产品主表 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录金融产品（银行理财、信托计划、券商资管、保险资管、养老金产品、保险理财）的具体名称、简称、交易状态等信息。
2.信息来源：银行、信托、证券、资产管理公司、保险公司等官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% |  |
| 3 | `EnterpriseCode` | 企业编码 | varchar2(12) | ✓ | 100.0% | 企业编码（EnterpriseCode）：与“ 企业码表（EP_CompanyMain）”中的“企业编码（Enterpr... |
| 4 | `CompanyCode` | 公司代码 | number(10) | ✓ | 100.0% | 公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyC... |
| 5 | `SecuCode` | 证券代码 | varchar2(50) | ✓ | 55.22% | 证券代码（SecuCode）：指银行、证券公司、基金公司等披露的产品代码。 |
| 6 | `ChiName` | 中文名称 | varchar2(200) | ✗ | 100.0% |  |
| 7 | `SecuAbbr` | 证券简称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `ChiSpelling` | 拼音缩写 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 10 | `SecuState` | 证券状态 | varchar2(12) | ✓ | 90.72% | 证券状态（SecuState）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”... |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### EnterpriseCode (企业编码)

企业编码（EnterpriseCode）：与“
企业码表（EP_CompanyMain）”中的“企业编码（EnterpriseCode）”关联，得到相关企业的具体名称、基本信息等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### SecuCode (证券代码)

证券代码（SecuCode）：指银行、证券公司、基金公司等披露的产品代码。

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC00000139S-保险资管，FCC00000139T-养老金产品，FCC0000014SG-保险理财产品，FCC000001654-保险产品投资账户。

### SecuState (证券状态)

证券状态（SecuState）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券状态的具体描述：FCC0000001TE-预售期，FCC0000001TF-募集期，FCC0000001TG-运行期，FCC0000001TH-已到期，FCC000001EXS-取消募集，FCC000001EXT-募集结束，FCC0000003BI-募集失败。

## SQL示例

```sql
-- 查询 金融产品主表 数据
SELECT *
FROM fp_secumain
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
