# FP_JYProductType

**中文名**: 金融产品聚源分类

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_JYProductType` |
| MySQL表名 | `fp_jyproducttype` |
| 中文名 | 金融产品聚源分类 |
| 路径 | 聚源新版数据库 > 金融产品 > 金融产品基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录银行理财聚源分类数据
2.数据范围：2024年1月起-至今
3.信息来源：聚源

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `SecuCategory` | 证券类别 | varchar2(12) | ✗ | 100.0% | 证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCod... |
| 3 | `FinProCode` | 金融产品编码 | varchar2(12) | ✗ | 100.0% | 金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCod... |
| 4 | `Standard` | 分类标准 | varchar2(12) | ✗ | 100.0% | 与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到分类标准的具体描述：F... |
| 5 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `CancelDate` | 取消日期 | date | ✓ | 99.99% |  |
| 7 | `IfEffected` | 是否有效 | varchar2(12) | ✗ | 100.0% | 是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）... |
| 8 | `FirstAssetCatCode` | 一级分类代码 | varchar2(12) | ✗ | 100.0% | 一级分类代码(FirstAssetCatCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码... |
| 9 | `FirstAssetCatName` | 一级分类名称 | varchar2(200) | ✗ | 100.0% |  |
| 10 | `SecAssetCatCode` | 二级分类代码 | varchar2(12) | ✗ | 100.0% | 二级分类代码(SecAssetCatCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（G... |
| 11 | `SecAssetCatName` | 二级分类名称 | varchar2(200) | ✗ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### SecuCategory (证券类别)

证券类别（SecuCategory）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到证券类别的具体描述：FCC0000001TD-银行理财。

### FinProCode (金融产品编码)

金融产品编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到产品的名称等信息。

### Standard (分类标准)

与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到分类标准的具体描述：FCC000001EKL-聚源银行理财分类2024版。

### IfEffected (是否有效)

是否有效（IfEffected）：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到是否有效的具体描述：FCC000000005-是，FCC000000006-否。

### FirstAssetCatCode (一级分类代码)

一级分类代码(FirstAssetCatCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到一级分类代码的具体描述。具体分类如下：FCC000001I94-现金管理类（一级），FCC0000001T8-固定收益类，FCC0000001TB-混合类，FCC0000001T9-权益类，FCC000001I92-商品及金融衍生品类（一级），FCC000001EKV-其他类。

### SecAssetCatCode (二级分类代码)

二级分类代码(SecAssetCatCode)：与“金融产品指标码表（FP_Indicator）”中的“聚源指标代码（GilCode）”关联，得到二级分类代码的具体描述。具体分类如下：FCC000001EMV-现金管理类（二级），FCC000001EL5-纯债类，FCC000001EL6-债券+非标类，FCC000001EL7-固收+，FCC000001EKZ-偏股混合，FCC000001EL0-偏债混合，FCC000001EL1-股债平衡，FCC000001EL2-灵活配置，FCC000001EKW-股票类，FCC000001EKX-股权类，FCC000001I93-商品及金融衍生品类（二级），FCC000001EKY-结构化产品类。

## SQL示例

```sql
-- 查询 金融产品聚源分类 数据
SELECT *
FROM fp_jyproducttype
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
