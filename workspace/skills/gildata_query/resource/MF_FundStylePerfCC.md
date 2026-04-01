# MF_FundStylePerfCC

**中文名**: 基金标签业绩相似度

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundStylePerfCC` |
| MySQL表名 | `mf_fundstyleperfcc` |
| 中文名 | 基金标签业绩相似度 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 日更新 |
| 字段数量 | 11 |
| 版本 | 1 |

## 表描述

1.内容说明：用于衡量基金主要标签（包括行业风格和概念风格）与风格指数的相关性，相关系数的绝对值越大，代表与风格指数的相关性越强。
2.数据范围：2019年4月-至今。
3.信息来源：在基金属于该风格的时间内，根据基金每个交易日公布的复权单位净值收益率、股票风格指数收益率计算而得。公式为：Covariance(基金收益率，风格指数收益率)/{std(基金收益率)*std(风格指数收益率)}，基金收益率的样本首日需大于等于截止日期往前追溯相应周期的日历日期加一天。
注：主要来源 公募基金行业标签变动MF_IndustryTagChange 和 公募基金概念标签变动MF_ThemeTagChange。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `TagCategory` | 标签种类 | number(10) | ✗ | 100.0% | 标签种类(TagCategory): 1-热点概念板块，2-热点概念板块(二级)，3-中证一级行业，4-申万一级行业，5... |
| 4 | `FundTagCode` | 标签代码 | number(10) | ✗ | 100.0% | 标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金概念... |
| 5 | `FundTagName` | 标签名称 | varchar2(500) | ✓ | 100.0% |  |
| 6 | `TradingDay` | 交易日 | date | ✗ | 100.0% | 交易日（TradingDay）：选取交易日当天基金所属的风格的指数收益率与当天的基金收益率，指标周期内的交易日需要在基金... |
| 7 | `IndexCycle` | 指标周期 | number(10) | ✗ | 100.0% | 指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM... |
| 8 | `DataValue` | 指标值 | number(18,9) | ✓ | 100.0% |  |
| 9 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TagCategory (标签种类)

标签种类(TagCategory): 1-热点概念板块，2-热点概念板块(二级)，3-中证一级行业，4-申万一级行业，5-申万二级行业

### FundTagCode (标签代码)

标签代码(FundTagCode): 当标签种类（TagCategory)=1, 则FundTagCode跟公募基金概念标签变动(MF_ThemeTagChange)的标签代码(FundTagCode)关联。当标签种类（TagCategory)=2，则FundTagCode跟公募基金概念标签变动(MF_ThemeTagChange)所属2级概念代码(SubclassCode) 关联。当标签种类（TagCategory)=3、4、5， 则FundTagCode跟公募基金行业标签变动(MF_IndustryTagChange)的标签代码(FundTagCode)关联。

### TradingDay (交易日)

交易日（TradingDay）：选取交易日当天基金所属的风格的指数收益率与当天的基金收益率，指标周期内的交易日需要在基金属于该风格的时间范围内。

### IndexCycle (指标周期)

指标周期(IndexCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 2149 and DM in(6,12,36)，得到指标周期的具体描述：6-六个月，12-一年，36-三年。

## SQL示例

```sql
-- 查询 基金标签业绩相似度 数据
SELECT *
FROM mf_fundstyleperfcc
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
