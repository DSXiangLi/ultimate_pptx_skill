# Bond_ConBDPortfolioD

**中文名**: 可转债投资组合明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDPortfolioD` |
| MySQL表名 | `bond_conbdportfoliod` |
| 中文名 | 可转债投资组合明细 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 季更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.业务说明：本表记录基金债券组合中重仓可转债及处于转股期的可转换债券明细，包括债券代码、持有数量、持有市值、市值占净资产的比例等数据。
2.数据范围：2000-12 至今
3.信息来源：基金公司披露的定期报告和上市交易公告书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 可转债内部编码 | number(10) | ✗ | 100.0% | 可转债内部代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `FundInnerCode` | 投资基金内部编码 | number(10) | ✗ | 100.0% | 投资基金内部编码（FundInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode... |
| 6 | `FirstAssetCatCode` | 基金类别一级代码 | number(10) | ✓ | 100.0% | 一级分类代码(FirstAssetCatCode):公募基金分类表(MF_FundType)表中分类标准(Standar... |
| 7 | `SecAssetCatCode` | 基金类别二级代码 | number(10) | ✓ | 100.0% | 二级分类代码(SecAssetCatCode):公募基金分类表(MF_FundType)表中分类标准(Standard)... |
| 8 | `SharesHolding` | 持仓数量 | number(19,2) | ✓ | 99.97% |  |
| 9 | `MarketValue` | 持仓市值(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `RatioInNV` | 占净值比 | number(18,6) | ✓ | 100.0% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (可转债内部编码)

可转债内部代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得债券的交易代码、简称等。

### FundInnerCode (投资基金内部编码)

投资基金内部编码（FundInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FirstAssetCatCode (基金类别一级代码)

一级分类代码(FirstAssetCatCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75-聚源基金分类2019版,的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

### SecAssetCatCode (基金类别二级代码)

二级分类代码(SecAssetCatCode):公募基金分类表(MF_FundType)表中分类标准(Standard)=75-聚源基金分类2019版,的聚源分类编码(FundTypeCode)字段关联，得到分类的具体描述。

## SQL示例

```sql
-- 查询 可转债投资组合明细 数据
SELECT *
FROM bond_conbdportfoliod
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
