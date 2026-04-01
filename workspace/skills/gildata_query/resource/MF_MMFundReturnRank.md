# MF_MMFundReturnRank

**中文名**: 货币基金收益率排名

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MMFundReturnRank` |
| MySQL表名 | `mf_mmfundreturnrank` |
| 中文名 | 货币基金收益率排名 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录货币基金万份收益、七日年化同类均值及排名。
2.数据范围：2004年1月起-至今。
3.信息来源：根据基金公司披露的万份收益和七日年化计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TypeCode` | 基金分类口径代码 | number(10) | ✓ | 100.0% | 10-证监会基金分类,916自定义分类 |
| 5 | `TypeName` | 基金分类口径描述 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✓ | 100.0% | 1109代表货币型，1106代表短期理财债券型,91603代表‘货币型(仅A类)’，91604代表‘短期理财债券型(仅A... |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `DailyProfit` | 每万份基金单位当日收益(元) | number(18,6) | ✓ | 99.92% |  |
| 9 | `DailyProfitMean` | 同类基金万份收益均值 | number(18,6) | ✓ | 100.0% |  |
| 10 | `DailyProfitRank` | 基金万份收益排名 | varchar2(100) | ✓ | 99.92% |  |
| 11 | `LatestWeeklyYield` | 最近7日折算年收益率(%) | number(18,8) | ✓ | 99.4% |  |
| 12 | `LatestWeeklyYieldMean` | 同类基金7日年化均值(%) | number(18,8) | ✓ | 100.0% |  |
| 13 | `LatestWeeklyYieldRank` | 基金七日年化排名 | varchar2(100) | ✓ | 99.4% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TypeCode (基金分类口径代码)

10-证监会基金分类,916自定义分类

### FundTypeCode (基金类别代码)

1109代表货币型，1106代表短期理财债券型,91603代表‘货币型(仅A类)’，91604代表‘短期理财债券型(仅A类)’

## SQL示例

```sql
-- 查询 货币基金收益率排名 数据
SELECT *
FROM mf_mmfundreturnrank
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
