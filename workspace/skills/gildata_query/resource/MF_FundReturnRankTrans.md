# MF_FundReturnRankTrans

**中文名**: 公募基金收益率排名(转型)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundReturnRankTrans` |
| MySQL表名 | `mf_fundreturnranktrans` |
| 中文名 | 公募基金收益率排名(转型) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 同类分析体系 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录公募基金收益率、收益率同类均值及排名。
2.数据范围：2014年7月起-至今。
3.信息来源：根据基金公司披露的净值、分红、拆分折算数据计算而得，其中货币型基金的收益率根据基金公司披露的万份收益、7日年化收益率数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `TypeCode` | 基金分类代码 | number(10) | ✗ | 100.0% | 基金分类口径代码（TypeCode）：与系统常量表中的DM字段关联，令LB=1252，DM in(10,75),得到指标... |
| 5 | `TypeName` | 基金分类描述 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `FundTypeCode` | 基金类别代码 | number(10) | ✗ | 100.0% |  |
| 7 | `FundTypeName` | 基金类别描述 | varchar2(100) | ✗ | 100.0% | 基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTy... |
| 8 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 1-一个月，3-三个月，6-六个月，7-七天，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年... |
| 9 | `FundReturn` | 基金收益率(%) | number(18,9) | ✓ | 100.0% |  |
| 10 | `FundReturnMean` | 同类基金收益率均值(%) | number(18,9) | ✓ | 100.0% |  |
| 11 | `FundAnnReturn` | 基金年化收益率(%) | number(18,9) | ✓ | 31.07% | 基金年化收益率(%)(FundAnnReturn)：仅计算IndexCycle IN (24,36,60,120,990... |
| 12 | `FundAnnReturnMean` | 同类基金年化收益率均值(%) | number(18,9) | ✓ | 31.07% |  |
| 13 | `FundReturnRank` | 同类基金收益率排名 | varchar2(100) | ✓ | 100.0% |  |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TypeCode (基金分类代码)

基金分类口径代码（TypeCode）：与系统常量表中的DM字段关联，令LB=1252，DM in(10,75),得到指标周期的具体描述：10-证监会基金分类；75-聚源基金分类

### FundTypeName (基金类别描述)

基金类别代码(FundTypeCode):当基金分类口径描述(TypeName)=证监会基金分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=1737，得到证监会基金分类的具体描述。当基金分类口径描述(TypeName)=聚源一级分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=2197，IVALUE=1，得到聚源基金一级分类的具体描述。当基金分类口径描述(TypeName)=聚源二级分类，基金类别(FundTypeCode)与系统常量表中的DM字段关联，令LB=2197，IVALUE=2，得到聚源基金二级分类的具体描述。

### IndexCycle (指标周期)

1-一个月，3-三个月，6-六个月，7-七天，12-一年，24-两年，36-三年，60-五年，120-十年，998-今年以来，999-成立以来。

### FundAnnReturn (基金年化收益率(%))

基金年化收益率(%)(FundAnnReturn)：仅计算IndexCycle IN (24,36,60,120,990,999).

## SQL示例

```sql
-- 查询 公募基金收益率排名(转型) 数据
SELECT *
FROM mf_fundreturnranktrans
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
