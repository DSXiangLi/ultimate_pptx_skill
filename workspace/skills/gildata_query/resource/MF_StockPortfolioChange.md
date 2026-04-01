# MF_StockPortfolioChange

**中文名**: 公募基金股票组合重大变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_StockPortfolioChange` |
| MySQL表名 | `mf_stockportfoliochange` |
| 中文名 | 公募基金股票组合重大变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 半年更新 |
| 字段数量 | 14 |
| 版本 | 1.02 |

## 表描述

1.本表记录中报、年报中公布报告期内股票投资组合的重大变动，比如买入了哪些股票、市值有多少、占净资产的比例等。
2.历史数据：2004年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `ChangeType` | 变动类型 | number(10) | ✗ | 100.0% | 变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型... |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `StockInnerCode` | 股票内部代码 | number(10) | ✗ | 100.0% | 股票内部代码(StockInnerCode): 当StockInnerCode<1000000时，与“证券主表（Secu... |
| 9 | `AccumulatedTradeSum` | 累计买入/卖出金额(元) | number(19,4) | ✓ | 100.0% |  |
| 10 | `RatioInNVAtBegin` | 占期初基金净值比例 | number(18,6) | ✓ | 91.28% |  |
| 11 | `RatioInNVAtEnd` | 占期末基金净值比例 | number(18,6) | ✓ | 8.73% |  |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### ChangeType (变动类型)

变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型的具体描述：1-买入，2-卖出。

### StockInnerCode (股票内部代码)

股票内部代码(StockInnerCode): 当StockInnerCode<1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等；当StockInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得股票的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金股票组合重大变动 数据
SELECT *
FROM mf_stockportfoliochange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
