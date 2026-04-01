# HK_FundClassification

**中文名**: 香港基金分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundClassification` |
| MySQL表名 | `hk_fundclassification` |
| 中文名 | 香港基金分类表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.本表记录香港互认基金的银河证券分类数据，及所对应的起始日期、终止日期等信息。
2.历史数据：2017年起-至今。
3.信息来源：银河证券官网
表数据更新频率： 日更新

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% | 基金内码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `Standard` | 分类标准 | number(10) | ✗ | 100.0% | 分类标准(Standard)：18-银河证券分类2017版 |
| 4 | `StandardName` | 分类标准名称 | varchar2(50) | ✗ | 100.0% |  |
| 5 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `CancelDate` | 取消日期 | date | ✓ | 0.84% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% |  |
| 8 | `FirstAssetCatCode` | 一级分类代码 | number(10) | ✗ | 100.0% | 一级分类代码(FirstAssetCatCode):公募基金分类表(MF_FundType)表中，分类标准(Standa... |
| 9 | `FirstAssetCatName` | 一级分类名称 | varchar2(200) | ✗ | 100.0% | 一级银河分类有：297-互认基金 |
| 10 | `SecAssetCatCode` | 二级分类代码 | number(10) | ✓ | 100.0% | 二级分类代码(SecAssetCatCode):公募基金分类表(MF_FundType)表中，分类标准(Standard... |
| 11 | `SecAssetCatName` | 二级分类名称 | varchar2(200) | ✓ | 100.0% | 二级银河分类有：298-股票型互认基金，301-混合型互认基金，303-债券型互认基金 |
| 12 | `ThirdAssetCatCode` | 三级分类代码 | number(10) | ✓ | 100.0% | 三级分类代码(ThirdAssetCatCode)：公募基金分类表(MF_FundType)表中，分类标准(Standa... |
| 13 | `ThirdAssetCatName` | 三级分类名称 | varchar2(200) | ✓ | 100.0% | 三级银河分类有：299-常规股票型互认基金，300-股票指数型互认基金，302-混合型互认基金，304-债券型互认基金 |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内码)

基金内码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### Standard (分类标准)

分类标准(Standard)：18-银河证券分类2017版

### FirstAssetCatCode (一级分类代码)

一级分类代码(FirstAssetCatCode):公募基金分类表(MF_FundType)表中，分类标准(Standard)=18的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

### FirstAssetCatName (一级分类名称)

一级银河分类有：297-互认基金

### SecAssetCatCode (二级分类代码)

二级分类代码(SecAssetCatCode):公募基金分类表(MF_FundType)表中，分类标准(Standard)=18的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

### SecAssetCatName (二级分类名称)

二级银河分类有：298-股票型互认基金，301-混合型互认基金，303-债券型互认基金

### ThirdAssetCatCode (三级分类代码)

三级分类代码(ThirdAssetCatCode)：公募基金分类表(MF_FundType)表中，分类标准(Standard)=18的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

### ThirdAssetCatName (三级分类名称)

三级银河分类有：299-常规股票型互认基金，300-股票指数型互认基金，302-混合型互认基金，304-债券型互认基金

## SQL示例

```sql
-- 查询 香港基金分类表 数据
SELECT *
FROM hk_fundclassification
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
