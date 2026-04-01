# MF_StkHoldingAna

**中文名**: 基金持股风格分析

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_StkHoldingAna` |
| MySQL表名 | `mf_stkholdingana` |
| 中文名 | 基金持股风格分析 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 季更新 |
| 字段数量 | 50 |
| 版本 | 1.02 |

## 表描述

1.内容说明：
【本表目标：本表旨在尽可能全面展现对基金的持股分析的情况。
本表记录基金的股票持仓风格，包括大中小盘持股风格、成长价值平衡持股风格、三种市场通用的持股集中度指标、不同周期的基金持有股票的换手率、拿到的实际股票交易费率、实际的股息率、和行业仓位波动率等指标。】
【本表使用：可以通过本表中持股风格、行业占比等指标，对偏股型基金的风格做出筛选，辅助于基金的分类与评价。可用于平台的基金风格展示。
出于尽可能减少对基金持股风格偏差的考量，本表一、三季度依据基金季报中重仓持股数据计算；二、四季度依据基金中报和年报中全部持股数据计算。
成长，价值，均衡风格指标仅针对A股做了统计，港股由于其特性暂未纳入计算。】
2.数据范围：1998年-至今
3.信息来源：根据公募基金披露的季报、中报、年报的数据整理后计算而得，算法详见注释。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 4 | `SharesHoldingYear` | 平均持仓时间(年) | number(18,9) | ✓ | 40.64% | 平均持仓时间(年) (SharesHoldingYear): 近一年换手率的倒数 |
| 5 | `InvestConcentra` | 投资集中度 | number(18,9) | ✓ | 97.44% | 投资集中度( InvestConcentra): sum【（基金持有该股票的市值/该股票的总市值）*Wi】，Wi=基金持... |
| 6 | `SharesHoldingPETTM` | 持股市盈率(TTM) | number(18,9) | ✓ | 97.44% | 持股市盈率(TTM)（ SharesHoldingPETTM）: 基金持仓的前10大重仓股票（含科创板）的滚动市盈率，按... |
| 7 | `SharesHoldingPB` | 持股市净率 | number(18,9) | ✓ | 97.44% | 持股市净率(SharesHoldingPB):基金持仓的前10大重仓股票(含科创板）的市净率，按照基金持有股票市值，计算... |
| 8 | `SharesHoldingROECW` | 持股ROE(扣除,加权)(%) | number(18,9) | ✓ | 71.58% | 持股ROE(扣除,加权)(%)(SharesHoldingROECW):基金持仓的前10大重仓股票（含科创板）的ROE（... |
| 9 | `TopOneIndustryRatio` | 第一大行业占全部行业比(%) | number(18,9) | ✓ | 83.4% | 第一大行业占全部行业比(%)(TopOneIndustryRatio): 基金持仓第一名的行业（证监会行业分类）市值占所... |
| 10 | `TopThreeIndustryRatio` | 前三大行业占全部行业比(%) | number(18,9) | ✓ | 83.4% | 前三大行业占全部行业比(%)(TopThreeIndustryRatio): 基金持仓前3大行业（证监会行业分类）市值占... |
| 11 | `TopFiveIndustryRatio` | 前五大行业占全部行业比(%) | number(18,9) | ✓ | 70.57% | 前五大行业占全部行业比(TopFiveIndustryRatio): 基金持仓前5大行业（证监会行业分类）市值占所有投资... |
| 12 | `TopTenIndustryRatio` | 前十大行业占全部行业比(%) | number(18,9) | ✓ | 31.54% | 前十大行业占全部行业比(TopTenIndustryRatio):持仓前10大行业（证监会行业分类）市值占所有投资行业市... |
| 13 | `StkConcI` | 持股集中度一 | number(18,9) | ✓ | 98.33% | 持股集中度一(StkConcI):基金持仓的前10大重仓股票占组合净资产值的比例之和 |
| 14 | `StkConcII` | 持股集中度二 | number(18,9) | ✓ | 98.32% | 持股集中度二(StkConcII): 基金持仓前10大股票市值占基金投资股票市值的比例 |
| 15 | `HHI` | 持股集中度三(赫希曼指数) | number(18,9) | ✓ | 47.83% | 持股集中度三(赫希曼指数)(HHI): 基金持仓全部股票（中报、年报披露）的市值占总市值比例的平方和。如果HHI越接近1... |
| 16 | `TurnoverRateSixM` | 近半年股票换手率 | number(18,9) | ✓ | 44.71% | 近半年股票换手率(TurnoverRateSixM): 近半年换手率=（半年内买入股票成本+半年内卖出股票收入）/(半年... |
| 17 | `TurnoverRateOneY` | 近一年股票换手率 | number(18,9) | ✓ | 40.64% | 近一年股票换手率(TurnoverRateOneY): 近一年换手率=（一年内买入股票成本+一年内卖出股票收入）/(近一... |
| 18 | `StkTranFeeSixM` | 近半年实际股票交易费率 | number(18,9) | ✓ | 19.2% | 近半年实际股票交易费率(StkTranFeeSixM): 半年内交易费用/（半年内买入股票成本+半年内卖出股票收入）。 |
| 19 | `StkTranFeeOneY` | 近一年实际股票交易费率 | number(18,9) | ✓ | 17.3% | 近一年实际股票交易费率(StkTranFeeOneY): 一年内交易费用/（一年内买入股票成本+一年内卖出股票收入）。 |
| 20 | `DividendRatioSixM` | 近半年实际股息率 | number(18,9) | ✓ | 44.85% | 近半年实际股息率(DividendRatioSixM): 近半年股利收入/近半年（近3个季度报告披露的）股票市值均值。 |
| 21 | `DividendRatioOneY` | 近一年实际股息率 | number(18,9) | ✓ | 31.4% | 近一年实际股息率(DividendRatioOneY): 近一年股利收入/近一年（近5个季度报告披露的）股票市值均值。 |
| 22 | `IndusAlloVolOneY` | 近一年行业仓位波动率 | number(18,9) | ✓ | 76.87% | 近一年行业仓位波动率（IndusAlloVolOneY）：按照证监会行业分类口径，计算所有行业的近一年行业持仓占资产净值... |
| 23 | `IndusAlloVolTwoY` | 近二年行业仓位波动率 | number(18,9) | ✓ | 62.88% | 近二年行业仓位波动率（IndusAlloVolTwoY）：按照证监会行业分类口径，计算所有行业的近二年行业持仓占资产净值... |
| 24 | `IndusAlloVolThreeY` | 近三年行业仓位波动率 | number(18,9) | ✓ | 50.48% | 近三年行业仓位波动率（IndusAlloVolThreeY）：按照证监会行业分类口径，计算所有行业的近三年行业持仓占资产... |
| 25 | `IndusAlloVolFiveY` | 近五年行业仓位波动率 | number(18,9) | ✓ | 31.76% | 近五年行业仓位波动率（IndusAlloVolFiveY）：按照证监会行业分类口径，计算所有行业的近五年行业持仓占资产净... |
| 26 | `LCHoldingWeight` | 大盘股持仓比重 | number(18,9) | ✓ | 93.32% | 大盘股持仓比重(LCHoldingWeight): 基金持有大盘风格股票的比重（占基金净值比）。（股票风格根据日均累计市... |
| 27 | `LCMarketValue` | 大盘股市值 | number(18,4) | ✓ | 93.45% | 大盘股市值(LCMarketValue): 基金所持有的的大盘股总市值 |
| 28 | `LCMarketValueRatio` | 大盘股市值占比 | number(18,9) | ✓ | 93.44% | 大盘股市值占比（LCMarketValueRatio）：基金所持有的的大盘股总市值/基金的股票投资合计。 |
| 29 | `MCHoldingWeight` | 中盘股持仓比重 | number(18,9) | ✓ | 72.9% |  |
| 30 | `MCMarketValue` | 中盘股市值 | number(18,4) | ✓ | 73.63% |  |
| 31 | `MCMarketValueRatio` | 中盘股市值占比 | number(18,9) | ✓ | 73.62% |  |
| 32 | `SCHoldingWeight` | 小盘股持仓比重 | number(18,9) | ✓ | 53.67% |  |
| 33 | `SCMarketValue` | 小盘股市值 | number(18,4) | ✓ | 54.3% |  |
| 34 | `SCMarketValueRatio` | 小盘股市值占比 | number(18,9) | ✓ | 54.3% |  |
| 35 | `GHoldingWeight` | 成长股持仓比重 | number(18,9) | ✓ | 89.35% | 成长股持仓比重(GHoldingWeight):基金持有成长风格股票的比重（占基金净值比）。股票风格根据价值与成长因子聚... |
| 36 | `GMarketValue` | 成长股市值 | number(18,4) | ✓ | 89.61% |  |
| 37 | `GMarketValueRatio` | 成长股市值占比 | number(18,9) | ✓ | 89.6% |  |
| 38 | `VHoldingWeight` | 价值股持仓比重 | number(18,9) | ✓ | 79.64% |  |
| 39 | `VMarketValue` | 价值股市值 | number(18,4) | ✓ | 79.82% |  |
| 40 | `VMarketValueRatio` | 价值股市值占比 | number(18,9) | ✓ | 79.82% |  |
| 41 | `BHoldingWeight` | 平衡股持仓比重 | number(18,9) | ✓ | 89.6% |  |
| 42 | `BMarketValue` | 平衡股市值 | number(18,4) | ✓ | 89.83% |  |
| 43 | `BMarketValueRatio` | 平衡股市值占比 | number(18,9) | ✓ | 89.82% |  |
| 44 | `InduConcI` | 申万行业集中度一(%) | number(18,9) | ✓ | 95.91% | 申万行业集中度一(%)（InduConcI): 基金持仓第一大行业（申万行业分类）市值占所有投资行业市值的比例 |
| 45 | `InduConcII` | 申万行业集中度二(%) | number(18,9) | ✓ | 90.39% | 申万行业集中度二(%)（InduConcII): 基金持仓前三大行业（申万行业分类）市值占所有投资行业市值的比例 |
| 46 | `InduConcIII` | 申万行业集中度三(%) | number(18,9) | ✓ | 81.98% | 申万行业集中度三(%)（InduConcIII): 基金持仓前五大行业（申万行业分类）市值占所有投资行业市值的比例 |
| 47 | `InduConcIV` | 申万行业集中度四(%) | number(18,9) | ✓ | 40.33% | 申万行业集中度四(%)（InduConcIV): 基金持仓前十大行业（申万行业分类）市值占所有投资行业市值的比例 |
| 48 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 49 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 50 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### SharesHoldingYear (平均持仓时间(年))

平均持仓时间(年) (SharesHoldingYear): 近一年换手率的倒数

### InvestConcentra (投资集中度)

投资集中度( InvestConcentra): sum【（基金持有该股票的市值/该股票的总市值）*Wi】，Wi=基金持有该股票的市值/sum（同一基金同一报告期各个股票的市值）。也可用于辅助判断基金的控盘情况。

### SharesHoldingPETTM (持股市盈率(TTM))

持股市盈率(TTM)（ SharesHoldingPETTM）: 基金持仓的前10大重仓股票（含科创板）的滚动市盈率，按照基金持有股票市值，计算加权平均数。

### SharesHoldingPB (持股市净率)

持股市净率(SharesHoldingPB):基金持仓的前10大重仓股票(含科创板）的市净率，按照基金持有股票市值，计算加权平均数。

### SharesHoldingROECW (持股ROE(扣除,加权)(%))

持股ROE(扣除,加权)(%)(SharesHoldingROECW):基金持仓的前10大重仓股票（含科创板）的ROE（加权扣非），按照基金持有股票市值，计算加权平均数。

### TopOneIndustryRatio (第一大行业占全部行业比(%))

第一大行业占全部行业比(%)(TopOneIndustryRatio): 基金持仓第一名的行业（证监会行业分类）市值占所有投资行业市值的比例

### TopThreeIndustryRatio (前三大行业占全部行业比(%))

前三大行业占全部行业比(%)(TopThreeIndustryRatio): 基金持仓前3大行业（证监会行业分类）市值占所有投资行业市值的比例

### TopFiveIndustryRatio (前五大行业占全部行业比(%))

前五大行业占全部行业比(TopFiveIndustryRatio): 基金持仓前5大行业（证监会行业分类）市值占所有投资行业市值的比例

### TopTenIndustryRatio (前十大行业占全部行业比(%))

前十大行业占全部行业比(TopTenIndustryRatio):持仓前10大行业（证监会行业分类）市值占所有投资行业市值的比例

## SQL示例

```sql
-- 查询 基金持股风格分析 数据
SELECT *
FROM mf_stkholdingana
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
