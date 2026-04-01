# FP_CodeRelationship

**中文名**: 金融产品代码关联

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_CodeRelationship` |
| MySQL表名 | `fp_coderelationship` |
| 中文名 | 金融产品代码关联 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 11 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录同一金融产品（银行理财、信托计划、券商资管、保险理财）的分级，分期，分期限，以及保险产品与投资账户的关联关系。
2.信息来源：银行、信托、证券、资产管理公司、保险公司等官网。
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✓ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `CodeDefine` | 代码关联方式 | varchar2(12) | ✗ | 100.0% | 代码关联方式（CodeDefine）：与“金融产品指标码表（FP_Indicator ）”中的“聚源指标代码（GilCo... |
| 5 | `RelatedFinProCode` | 关联代码金融产品编码 | varchar2(12) | ✗ | 100.0% | 关联代码金融产品编码（RelatedFinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编... |
| 6 | `StartDate` | 启用日期 | date | ✓ | 97.44% |  |
| 7 | `EndDate` | 终止日期 | date | ✓ | 90.56% |  |
| 8 | `IfEffected` | 是否有效 | varchar2(12) | ✓ | 100.0% | 是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财，FCC000000419-信托产品，FCC000000Y6I-券商理财，FCC0000014SG-保险理财产品，FCC000001654-保险产品投资账户。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### CodeDefine (代码关联方式)

代码关联方式（CodeDefine）：与“金融产品指标码表（FP_Indicator ）”中的“聚源指标代码（GilCode）”关联，得到代码关联方式的具体描述：FCC000000YDC-母子产品份额关联，FCC000001E0I-同一产品份额关联，FCC000001EF0-同一投资账户关联，FCC000000YDD-分期，FCC00000129X-分期限，FCC000001655-保险产品对应投资账户。

### RelatedFinProCode (关联代码金融产品编码)

关联代码金融产品编码（RelatedFinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联。

### IfEffected (是否有效)

是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：FCC000000005-是，FCC000000006-否。

## SQL示例

```sql
-- 查询 金融产品代码关联 数据
SELECT *
FROM fp_coderelationship
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
