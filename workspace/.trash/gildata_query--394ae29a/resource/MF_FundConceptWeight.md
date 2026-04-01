# MF_FundConceptWeight

**中文名**: 基金热门概念板块持仓比重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundConceptWeight` |
| MySQL表名 | `mf_fundconceptweight` |
| 中文名 | 基金热门概念板块持仓比重 |
| 路径 | 聚源新版数据库 > 公募基金衍生指标库 > 基金产品衍生 > 业绩归因与风格分析 |
| 更新频率 | 周更新 |
| 字段数量 | 19 |
| 版本 | 1.01 |

## 表描述

1.内容说明：
【本表目标：本表记录偏股型基金定报披露的持仓的概念占比，以及概念市场占有率，旨在展示基金持仓的不同概念分布情况。其中涉及ETF联接、FOF等持有基金的基金，会使用基金持仓下穿持股的数据计算。】
【本表使用：可用于展示基金持股的热门概念情况。可基于基金的热门概念分布作为基金分类和筛选的参考。
同时本表有 如下3个字段 MarketValueT、RatioInStockT、ConceptMktWeight，会基于周度股票行情变化计算，较高时效的捕捉概念比率的变化。
概念包含呼吸机、口罩、基建、人工智能等。具体参见表 概念板块常量表(LC_ConceptList)】
2.数据范围：2019.4-至今
3.信息来源：根据基金持仓的概念计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 4 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 77.33% |  |
| 5 | `FundProperties` | 基金属性 | number(10) | ✓ | 77.33% | 基金属性(FundProperties)：1-ETF联接；2-FOF；3--持有基金的其他基金；4--未持有基金的基金。 |
| 6 | `ConceptCode` | 概念代码 | number(10) | ✗ | 100.0% | 概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptC... |
| 7 | `ConceptName` | 概念名称 | varchar2(100) | ✗ | 100.0% |  |
| 8 | `ConceptLevel` | 概念级别 | number(10) | ✓ | 77.33% | 概念级别(ConceptLevel)：3--三级（参见概念板块常量表(LC_ConceptList)）。 |
| 9 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 10 | `PosCharacter` | 持仓类型 | number(10) | ✗ | 100.0% | 持仓类型(PosCharacter)：1-重仓股；2-持仓明细。 |
| 11 | `MarketValue` | 持有规模 | number(24,4) | ✓ | 77.33% | 持有规模(MarketValue)：根据最新报告期持有规模加总计算。 |
| 12 | `HoldingWeight` | 持有比重 | number(18,9) | ✗ | 100.0% | 持有比重(HoldingWeight): 基金持有概念成分股总规模（按报告期披露规模）占基金资产净值的比重。 |
| 13 | `RatioInStock` | 持仓占股票投资占比 | number(18,9) | ✓ | 77.33% | 持仓占股票投资占比(RatioInStock)：基金持有概念成分股总规模（按报告期披露规模）占股票投资的比重。 |
| 14 | `MarketValueT` | 持有规模2 | number(24,4) | ✓ | 77.31% | 持有规模2(MarketValueT)：根据最新报告期披露的持有概念成份股数量×本表截止日期最新收盘价加总计算。 |
| 15 | `RatioInStockT` | 持仓占股票投资占比2 | number(18,9) | ✓ | 77.31% | 持仓占股票投资占比2(RatioInStockT)：分子为本表MarketValueT，分母为该基金全部持仓的Marke... |
| 16 | `ConceptMktWeight` | 概念板块市场占有率 | number(18,9) | ✗ | 100.0% | 概念板块市场占有率(ConceptMktWeight): 参见 概念估值指标-LC_ConceptDerivative。 |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### FundProperties (基金属性)

基金属性(FundProperties)：1-ETF联接；2-FOF；3--持有基金的其他基金；4--未持有基金的基金。

### ConceptCode (概念代码)

概念代码(ConceptCode)：与“概念板块常量表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。

### ConceptLevel (概念级别)

概念级别(ConceptLevel)：3--三级（参见概念板块常量表(LC_ConceptList)）。

### PosCharacter (持仓类型)

持仓类型(PosCharacter)：1-重仓股；2-持仓明细。

### MarketValue (持有规模)

持有规模(MarketValue)：根据最新报告期持有规模加总计算。

### HoldingWeight (持有比重)

持有比重(HoldingWeight): 基金持有概念成分股总规模（按报告期披露规模）占基金资产净值的比重。

### RatioInStock (持仓占股票投资占比)

持仓占股票投资占比(RatioInStock)：基金持有概念成分股总规模（按报告期披露规模）占股票投资的比重。

### MarketValueT (持有规模2)

持有规模2(MarketValueT)：根据最新报告期披露的持有概念成份股数量×本表截止日期最新收盘价加总计算。

### RatioInStockT (持仓占股票投资占比2)

持仓占股票投资占比2(RatioInStockT)：分子为本表MarketValueT，分母为该基金全部持仓的MarketValueT加总。

## SQL示例

```sql
-- 查询 基金热门概念板块持仓比重 数据
SELECT *
FROM mf_fundconceptweight
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
