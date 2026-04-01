# MF_QDIIPortfolioChange

**中文名**: 公募基金QDII基金组合重大变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_QDIIPortfolioChange` |
| MySQL表名 | `mf_qdiiportfoliochange` |
| 中文名 | 公募基金QDII基金组合重大变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > QDII投资组合 |
| 更新频率 | 半年更新 |
| 字段数量 | 22 |
| 版本 | 1.02 |

## 表描述

1.本表记录中报、年报公布报告期内QDII基金权益投资组合的重大变动,累计买入金额/卖出金额超出期初基金资产净值2%或前20名的权益投资明细。
2.历史数据：2007年12月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到Q... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `StatPeriod` | 统计区间 | number(10) | ✗ | 100.0% | 统计区间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM... |
| 8 | `InvestType` | 投资对象 | number(10) | ✗ | 100.0% | 投资对象(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1212，得到投资对象... |
| 9 | `ChangeType` | 变动类型 | number(10) | ✗ | 100.0% | 变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型... |
| 10 | `SerialNumber` | 序号 | number(5) | ✗ | 100.0% |  |
| 11 | `SecuCode` | 证券代码(披露) | varchar2(50) | ✓ | 100.0% |  |
| 12 | `SecuTradeCode` | 证券交易代码 | varchar2(10) | ✓ | 72.66% | 证券交易代码（SecuTradeCode）：当地市场交易代码 |
| 13 | `SecuInnerCode` | 证券内部编码 | number(10) | ✓ | 66.02% | 证券内部编码（SecuInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券代码（InnerCod... |
| 14 | `SecuName` | 公司名称 | varchar2(250) | ✓ | 99.7% |  |
| 15 | `ChiName` | 公司名称(中文) | varchar2(250) | ✓ | 72.44% |  |
| 16 | `TradeSum` | 买卖金额(元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `RatioInNVAtEnd` | 占期末净值比例 | number(10,6) | ✓ | 8.73% |  |
| 18 | `RatioInNVAtBegin` | 占期初净值比例 | number(10,6) | ✓ | 91.27% |  |
| 19 | `CodeType` | 代码类型 | number(10) | ✓ | 58.25% | 代码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1534，得到代码类型的具... |
| 20 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 21 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 22 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到QDII基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### StatPeriod (统计区间)

统计区间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1074 AND DM = 3，得到统计区间的具体描述：3-期末累计。

### InvestType (投资对象)

投资对象(InvestType)与(CT_SystemConst)表中的DM字段关联，令LB = 1212，得到投资对象的具体描述：1-股票，2-债券，3-转股期可转债，4-权证，5-资产支持证券，6-基金，7-港股，9-其他，10-资产证券化产品，11-新三板，12-基础设施证券投资基金，20-期货。

### ChangeType (变动类型)

变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型的具体描述：1-买入，2-卖出。

### SecuTradeCode (证券交易代码)

证券交易代码（SecuTradeCode）：当地市场交易代码

### SecuInnerCode (证券内部编码)

证券内部编码（SecuInnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券代码（InnerCode）”关联，得到QDII基金权益投资组合公布港股的代码、简称等。

### CodeType (代码类型)

代码类型(CodeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1534，得到代码类型的具体描述：10-ISIN代码，20-当地市场代码，30-SEDOL，40-CUSIP，50-彭博代码，90-其他。

## SQL示例

```sql
-- 查询 公募基金QDII基金组合重大变动 数据
SELECT *
FROM mf_qdiiportfoliochange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
