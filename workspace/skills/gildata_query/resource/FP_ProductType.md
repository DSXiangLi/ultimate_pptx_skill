# FP_ProductType

**中文名**: 金融产品分类层级表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_ProductType` |
| MySQL表名 | `fp_producttype` |
| 中文名 | 金融产品分类层级表 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录银行理财聚源分类的层级关系数据
2.数据范围：2024年1月起-至今
3.信息来源：聚源

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `Standard` | 分类标准 | varchar2(12) | ✗ | 100.0% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到分类标准的具体描述：F... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `CancelDate` | 取消日期 | date | ✓ | 0.0% |  |
| 6 | `IfEffected` | 是否有效 | varchar2(12) | ✓ | 100.0% | 是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 7 | `PubOrgCode` | 发布机构代码 | number(10) | ✓ | 100.0% | 发布机构代码(PubOrgCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Company... |
| 8 | `PubOrgName` | 发布机构名称 | varchar2(200) | ✓ | 100.0% |  |
| 9 | `ProductTypeName` | 分类名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `DisclosureCode` | 披露分类代码 | varchar2(50) | ✓ | 0.0% |  |
| 11 | `ProductTypeCode` | 聚源分类编码 | varchar2(12) | ✗ | 100.0% | 聚源分类编码(ProductTypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（G... |
| 12 | `ParentProductTypeCode` | 父级分类编码 | varchar2(12) | ✓ | 66.67% | 父级分类编码(ParentProductTypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源... |
| 13 | `StandardLevel` | 分类级别 | number(10) | ✗ | 100.0% |  |
| 14 | `Remark` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### Standard (分类标准)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到分类标准的具体描述：FCC000001EKL-聚源银行理财分类2024版。

### IfEffected (是否有效)

是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：FCC000000005-是，FCC000000006-否。

### PubOrgCode (发布机构代码)

发布机构代码(PubOrgCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到相关企业的具体名称、基本信息等。

### ProductTypeCode (聚源分类编码)

聚源分类编码(ProductTypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到聚源分类编码的具体描述。

### ParentProductTypeCode (父级分类编码)

父级分类编码(ParentProductTypeCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到父级分类编码的具体描述。

## SQL示例

```sql
-- 查询 金融产品分类层级表 数据
SELECT *
FROM fp_producttype
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
