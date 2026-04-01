# MF_FundTypeIndexQuote

**中文名**: 基金分类指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundTypeIndexQuote` |
| MySQL表名 | `mf_fundtypeindexquote` |
| 中文名 | 基金分类指数行情 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品标签 > 属性标签 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：记录聚源基金一级、二级分类指数（基金组合）日行情数据。聚源分类参照<公募基金聚源分类 MF_JYFundType>
2.数据范围：1998年6月-至今。
3.信息来源：来自于聚源基金分类数据以及净值数据。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TypeCode` | 基金分类代码 | number(10) | ✗ | 100.0% | 基金分类代码(TypeCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75-聚源基... |
| 3 | `TypeName` | 基金分类名称 | varchar2(200) | ✗ | 100.0% |  |
| 4 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 5 | `ClosePrice` | 收盘价(点) | number(14,4) | ✓ | 100.0% |  |
| 6 | `ChangeOF` | 日涨跌 | number(14,4) | ✓ | 99.97% |  |
| 7 | `ChangePCT` | 日涨跌幅(%) | number(18,6) | ✓ | 99.97% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TypeCode (基金分类代码)

基金分类代码(TypeCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75-聚源基金分类2019版,的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。与公募基金聚源分类(MF_JYFundType)的二级分类代码(SecAssetCatCode)关联，可得到具体该分类下的基金。

## SQL示例

```sql
-- 查询 基金分类指数行情 数据
SELECT *
FROM mf_fundtypeindexquote
WHERE TradingDay >= '2024-01-01'
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
