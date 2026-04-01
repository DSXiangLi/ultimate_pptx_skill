# MF_ETFPRComponents

**中文名**: 公募基金ETF申购赎回成份股信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_ETFPRComponents` |
| MySQL表名 | `mf_etfprcomponents` |
| 中文名 | 公募基金ETF申购赎回成份股信息 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > ETF类别 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1.01 |

## 表描述

1.本表收录ETF基金每个交易日公布的申购赎回成份股信息，包括成分股的名称、代码、现金替代标志等数据。
2.历史数据：2006年4月起-至今。
3.数据来源：基金公司官网和交易所官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.99% |  |
| 4 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 5 | `SecuCode` | 成份股代码 | varchar2(50) | ✗ | 100.0% |  |
| 6 | `SecuAbbr` | 成份股简称 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `SecuInnerCode` | 成份股内部编码 | number(10) | ✓ | 99.62% | 成份股内部编码（SecuInnerCode）：当SecuInnerCode<1000000时，与“证券主表（SecuMa... |
| 8 | `StockAmount` | 股票数量(股) | number(10) | ✓ | 99.87% |  |
| 9 | `CashSubstituteSignDescrip` | 现金替代标志描述 | varchar2(50) | ✓ | 100.0% |  |
| 10 | `CashSubstituteSign` | 现金替代标志 | number(10) | ✓ | 100.0% | 现金替代标志(CashSubstituteSign)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 11 | `CashSubstituteProportion` | 现金替代比例 | number(19,8) | ✓ | 26.08% |  |
| 12 | `ApplyCashPremiumRate` | 申购现金替代溢价比例 | number(19,8) | ✓ | 71.94% |  |
| 13 | `RedeemCashDiscountRate` | 赎回现金替代折价比例 | number(19,8) | ✓ | 60.49% |  |
| 14 | `FixedSubstituteSum` | 固定替代金额(元) | number(19,4) | ✓ | 32.58% |  |
| 15 | `ApplySubstituteSum` | 申购替代金额(元) | number(19,4) | ✓ | 27.25% |  |
| 16 | `RedeemSubstituteSum` | 赎回替代金额(元) | number(19,4) | ✓ | 27.12% |  |
| 17 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到ETF的交易代码、简称等。

### SecuInnerCode (成份股内部编码)

成份股内部编码（SecuInnerCode）：当SecuInnerCode<1000000时，与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联；当SecuInnerCode在1000000与2000000之间时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联；当SecuInnerCode在7000000与10000000之间时，与“美股证券主表（US_SecuMain）”中的“证券内部编码（InnerCode）”关联；SecuInnerCode在2000000与3000000之间时，与“期货合约（Fut_ContractMain）”中的“合约内部编码（ContractInnerCode）”关联；得到ETF成份股的交易代码、简称等信息。

### CashSubstituteSign (现金替代标志)

现金替代标志(CashSubstituteSign)与(CT_SystemConst)表中的DM字段关联，令LB = 1498，得到现金替代标志的具体描述：1-允许，2-必须，3-禁止，4-退补。

## SQL示例

```sql
-- 查询 公募基金ETF申购赎回成份股信息 数据
SELECT *
FROM mf_etfprcomponents
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
