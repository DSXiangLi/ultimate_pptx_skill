# MF_StockPortfolioDetail

**中文名**: 公募基金股票组合明细

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_StockPortfolioDetail` |
| MySQL表名 | `mf_stockportfoliodetail` |
| 中文名 | 公募基金股票组合明细 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 半年更新 |
| 字段数量 | 15 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金年报、半年报公布股票组合明细信息，包括股票的名称、代码、持有数量、持有市值、市值占基金净资产的比例等数据。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表(SecuMain)”以及"港股证券主表(HK_SecuMain)中的“... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `InvestType` | 投资类型 | number(10) | ✗ | 100.0% | 投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型... |
| 7 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 8 | `StockInnerCode` | 股票内部代码 | number(10) | ✗ | 100.0% | 股票内部代码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 9 | `SharesHolding` | 持股数量(股) | number(18,0) | ✓ | 100.0% |  |
| 10 | `ChangeOfSharesHolding` | 较上期持仓量变动 | number(18,0) | ✓ | 92.01% |  |
| 11 | `MarketValue` | 估值/市值(元) | number(19,4) | ✓ | 100.0% |  |
| 12 | `RatioInNV` | 占资产净值比例 | number(18,6) | ✓ | 100.0% |  |
| 13 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 14 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 15 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表(SecuMain)”以及"港股证券主表(HK_SecuMain)中的“证券内部编码（InnerCode）"关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### InvestType (投资类型)

投资类型(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1090，得到投资类型的具体描述：1-综合投资，2-积极投资，3-指数投资，4-境内投资，5-港股通投资。

### StockInnerCode (股票内部代码)

股票内部代码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等。当StockInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金股票组合明细 数据
SELECT *
FROM mf_stockportfoliodetail
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
