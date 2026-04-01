# MF_PortfolioPenetrate

**中文名**: 公募基金持仓分析表(季更)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_PortfolioPenetrate` |
| MySQL表名 | `mf_portfoliopenetrate` |
| 中文名 | 公募基金持仓分析表(季更) |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 季更新 |
| 字段数量 | 25 |
| 版本 | 1.01 |

## 表描述

1.内容说明：
【本表目标：本表记录ETF联接、FOF等投资了基金的基金的持仓穿透情况。对于ETF联接、FOF基金定报披露持仓基金，不能清晰反映该类基金持股及行业分布情况。本表对该类基金的持仓基金下穿至股票，基于季报、半年报、年报公布的持仓比例与持仓规模、数量进行计算，并对应个股行业分类，便于持股层面的行业筛选。】
【本表使用：本表作为 基金持仓行业穿透表(季更) MF_FundIndPenetrate的上游表之一，展现ETF联接、FOF类型基金的持仓，可用于展示这类基金的持股分布。】
2.数据范围：1990年1月起-至今。
3.信息来源：根据基金公司官网披露的定期报告中基金持仓数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% |  |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✗ | 100.0% |  |
| 4 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 5 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter)：1--重仓；2--持仓明细 |
| 6 | `FundProperties` | 基金属性 | number(10) | ✓ | 98.35% | 基金属性(FundProperties)：1-ETF联接基金；2-FOF基金 |
| 7 | `StockInnerCode` | 持仓股票内部编码 | number(10) | ✗ | 100.0% |  |
| 8 | `SecuCode` | 证券代码 | varchar2(50) | ✓ | 100.0% |  |
| 9 | `SecuName` | 证券名称 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `MarketValue` | 持仓规模 | number(24,9) | ✓ | 100.0% |  |
| 11 | `RatioInNV` | 持仓占资产净值比 | number(18,9) | ✓ | 100.0% |  |
| 12 | `RatioInStock` | 持仓占股票投资占比 | number(18,9) | ✓ | 100.0% |  |
| 13 | `RINOfStock` | 股票投资合计占资产净值比例 | number(18,9) | ✓ | 100.0% |  |
| 14 | `SharesHolding` | 持仓数量(张) | number(10) | ✓ | 99.82% |  |
| 15 | `IndustryNum` | 行业编码 | number(10) | ✗ | 100.0% |  |
| 16 | `Standard` | 分类标准 | number(10) | ✗ | 100.0% | 分类标准(Standard)：24-申万行业分类2014版，28-中证指数行业分类(2016版)，37-中信行业2019... |
| 17 | `FirstIndustryCode` | 对应一级行业代码 | varchar2(20) | ✗ | 100.0% |  |
| 18 | `FirstIndustryName` | 对应一级行业名称 | varchar2(100) | ✓ | 100.0% |  |
| 19 | `SecondIndustryCode` | 对应二级行业代码 | varchar2(20) | ✓ | 99.9% |  |
| 20 | `SecondIndustryName` | 对应二级行业名称 | varchar2(100) | ✓ | 99.9% |  |
| 21 | `ThirdIndustryCode` | 对应三级行业代码 | varchar2(20) | ✓ | 99.9% |  |
| 22 | `ThirdIndustryName` | 对应三级行业名称 | varchar2(100) | ✓ | 99.9% |  |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PosCharacter (持仓类型)

持仓类型(PosCharacter)：1--重仓；2--持仓明细

### FundProperties (基金属性)

基金属性(FundProperties)：1-ETF联接基金；2-FOF基金

### Standard (分类标准)

分类标准(Standard)：24-申万行业分类2014版，28-中证指数行业分类(2016版)，37-中信行业2019分类，38-申万行业分类(新)，40-中证指数行业分类(2021版) 【注：港股目前没有28/40分类】

## SQL示例

```sql
-- 查询 公募基金持仓分析表(季更) 数据
SELECT *
FROM mf_portfoliopenetrate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
