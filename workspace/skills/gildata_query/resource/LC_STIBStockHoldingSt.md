# LC_STIBStockHoldingSt

**中文名**: 科创板股东持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBStockHoldingSt` |
| MySQL表名 | `lc_stibstockholdingst` |
| 中文名 | 科创板股东持股统计 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 139 |
| 版本 | 1.03 |

## 表描述

1.收录报告期末，各类机构投资者对每只股票的持仓情况，以及前十大（无限售条件）股东合计持股情况等。
2.机构持股统计中，基金持股综合考虑了上市公司披露的十大股东数据以及基金报告中披露的基金持股数据；机构持股合计包含上市公司披露的股东持股以及在同一截止时点上基金披露的所持股票数据。
3.计算公式：
1)机构持有无限售流通股数量＝机构持有无限售流通A股之和
2)机构持有无限售流通股比例＝(机构持有无限售流通股数量/无限售流通A股)*100%
3)机构持有A股数量＝机构持有A股之和
4)机构持有A股比例＝(机构持有A股数量/A股总数)*100%
5)机构持有股票数量＝机构持有股票之和
6)机构持有股票比例＝(机构持有股票数量/总股本)*100%
4.数据范围：2019年至今
5.信息来源：招股说明书、上市公告书、定报、临时公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `StatDate` | 统计日期 | date | ✓ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% | 信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“... |
| 7 | `InstitutionsHoldings` | 机构持有无限售流通A股数量合计(股) | number(18,2) | ✓ | 39.23% | 由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”... |
| 8 | `FundsHoldings` | 公募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.0% |  |
| 9 | `PrivFundHoldings` | 私募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 9.52% |  |
| 10 | `SecuCorpsHoldings` | 券商持有无限售流通A股数量(股) | number(18,2) | ✓ | 6.73% |  |
| 11 | `FinProductsHoldings` | 券商理财产品持有无限售流通A股数量(股) | number(18,2) | ✓ | 3.03% |  |
| 12 | `BankHoldings` | 银行持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.03% |  |
| 13 | `InsuranceCorpsHoldings` | 保险公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 3.5% |  |
| 14 | `SocialSecurityFundHold` | 社保基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 6.2% |  |
| 15 | `EntAnnuitiesHoldings` | 企业年金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.29% |  |
| 16 | `TrustCompaniesHoldings` | 信托公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.93% |  |
| 17 | `FinanceCoHoldings` | 财务公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.02% |  |
| 18 | `ForeignInstHoldings` | 外资机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 14.69% |  |
| 19 | `QFIIHoldings` | #QFII持有无限售流通A股数量(股) | number(18,2) | ✓ | 4.38% |  |
| 20 | `OtherInstiHoldings` | 其它机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 32.2% |  |
| 21 | `InstitutionsHoldProp` | 机构持有无限售流通A股比例合计(%) | number(18,4) | ✓ | 39.23% |  |
| 22 | `FundsHoldProp` | 公募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.0% |  |
| 23 | `PrivFundHoldProp` | 私募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 9.52% |  |
| 24 | `SecuCorpsHoldProp` | 券商持有无限售流通A股比例(%) | number(18,4) | ✓ | 6.73% |  |
| 25 | `FinProductsHoldProp` | 券商理财产品持有无限售流通A股比例(%) | number(18,4) | ✓ | 3.03% |  |
| 26 | `BankHoldProp` | 银行持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.03% |  |
| 27 | `InsuranceCorpsHoldProp` | 保险公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 3.5% |  |
| 28 | `SocialSecuFundHoldProp` | 社保基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 6.2% |  |
| 29 | `CorpAnnuitiesHoldProp` | 企业年金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.29% |  |
| 30 | `TrustCompaniesHoldProp` | 信托公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.93% |  |
| 31 | `FinanceCoHoldProp` | 财务公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.02% |  |
| 32 | `ForeignInstHoldProp` | 外资机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 14.69% |  |
| 33 | `QFIIHoldProp` | #QFII持有无限售流通A股比例(%) | number(18,4) | ✓ | 4.38% |  |
| 34 | `OtherInstiHoldProp` | 其它机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 32.2% |  |
| 35 | `InstiHoldNum` | 机构持有无限售流通A股户数 | number(10) | ✓ | 39.23% |  |
| 36 | `PrivFundHoldNum` | 私募基金持有无限售流通A股户数 | number(10) | ✓ | 9.52% |  |
| 37 | `SecuCorpsHoldNum` | 券商持有无限售流通A股户数 | number(10) | ✓ | 6.73% |  |
| 38 | `FinProductsHoldNum` | 券商理财产品持有无限售流通A股户数 | number(10) | ✓ | 3.03% |  |
| 39 | `BankHoldNum` | 银行持有无限售流通A股户数 | number(10) | ✓ | 0.03% |  |
| 40 | `InsurCorpsHoldNum` | 保险公司持有无限售流通A股户数 | number(10) | ✓ | 3.5% |  |
| 41 | `SocialSecuFundHoldN` | 社保基金持有无限售流通A股户数 | number(10) | ✓ | 6.2% |  |
| 42 | `EntAnnuitiesHoldNum` | 企业年金持有无限售流通A股户数 | number(10) | ✓ | 0.29% |  |
| 43 | `TrustCoHoldNum` | 信托公司持有无限售流通A股户数 | number(10) | ✓ | 0.93% |  |
| 44 | `FinanceCoHoldNum` | 财务公司持有无限售流通A股户数 | number(10) | ✓ | 0.02% |  |
| 45 | `ForeignInstHoldNum` | 外资持有无限售流通A股户数 | number(10) | ✓ | 14.69% |  |
| 46 | `QFIIHoldingsNum` | #QFII持有无限售流通A股户数 | number(10) | ✓ | 4.38% |  |
| 47 | `OtherInstiHoldNum` | 其他机构持有无限售流通A股户数 | number(10) | ✓ | 32.2% |  |
| 48 | `InstitutionsHoldingsA` | 机构持有A股数量合计(股) | number(18,2) | ✓ | 93.82% |  |
| 49 | `FundsHoldingsA` | 公募基金持有A股数量(股) | number(18,2) | ✓ | 91.4% |  |
| 50 | `PrivFundHoldingsA` | 私募基金持A股数量(股) | number(18,2) | ✓ | 9.65% |  |
| 51 | `SecuCorpsHoldingsA` | 券商持有A股数量(股) | number(18,2) | ✓ | 10.67% |  |
| 52 | `FinProductsHoldingsA` | 券商理财产品持有A股数量(股) | number(18,2) | ✓ | 5.56% |  |
| 53 | `BankHoldingsA` | 银行持有A股数量(股) | number(18,2) | ✓ | 0.03% |  |
| 54 | `InsurCorpsHoldingsA` | 保险公司持有A股数量(股) | number(18,2) | ✓ | 3.64% |  |
| 55 | `SocialSecuFundHoldA` | 社保基金持有A股数量(股) | number(18,2) | ✓ | 6.22% |  |
| 56 | `EntAnnuitiesHoldingsA` | 企业年金持有A股数量(股) | number(18,2) | ✓ | 0.38% |  |
| 57 | `TrustCoHoldingsA` | 信托公司持有A股数量(股) | number(18,2) | ✓ | 1.0% |  |
| 58 | `FinanceCompHoldingsA` | 财务公司持有A股数量(股) | number(18,2) | ✓ | 0.12% |  |
| 59 | `ForeignInstHoldingsA` | 外资机构持A股数量(股) | number(18,2) | ✓ | 17.5% |  |
| 60 | `QFIIHoldingsA` | #QFII持有A股数量(股) | number(18,2) | ✓ | 4.58% |  |
| 61 | `OtherInstiHoldingsA` | 其它机构持有A股数量(股) | number(18,2) | ✓ | 40.21% |  |
| 62 | `InstitutionsHoldPropA` | 机构持有A股比例合计(%) | number(18,4) | ✓ | 93.17% |  |
| 63 | `FundsHoldPropA` | 公募基金持有A股比例(%) | number(18,4) | ✓ | 90.76% |  |
| 64 | `PrivFundHoldPropA` | 私募基金持有A股比例(%) | number(18,4) | ✓ | 9.65% |  |
| 65 | `SecuCorpsHoldPropA` | 券商持有A股比例(%) | number(18,4) | ✓ | 10.67% |  |
| 66 | `FinProductsHoldPropA` | 券商理财产品持有A股比例(%) | number(18,4) | ✓ | 5.56% |  |
| 67 | `InsurCorpsHoldPropA` | 保险公司持有A股比例(%) | number(18,4) | ✓ | 3.64% |  |
| 68 | `SociSecuFundHoldPropA` | 社保基金持有A股比例(%) | number(18,4) | ✓ | 6.22% |  |
| 69 | `CorpAnnuitiesHoldPropA` | 企业年金持有A股比例(%) | number(18,4) | ✓ | 0.38% |  |
| 70 | `TrustCoHoldPropA` | 信托公司持有A股比例(%) | number(18,4) | ✓ | 1.0% |  |
| 71 | `FinanceCompHoldPropA` | 财务公司持有A股比例(%) | number(18,4) | ✓ | 0.12% |  |
| 72 | `BankHoldPropA` | 银行持有A股比例(%) | number(18,4) | ✓ | 0.03% |  |
| 73 | `ForeignInstHoldPropA` | 外资机构持有A股比例(%) | number(18,4) | ✓ | 17.5% |  |
| 74 | `QFIIHoldPropA` | #QFII持有A股比例(%) | number(18,4) | ✓ | 4.58% |  |
| 75 | `OtherInstiHoldPropA` | 其它机构持有A股比例(%) | number(18,4) | ✓ | 40.2% |  |
| 76 | `InstiHoldANum` | 机构持有流通A股户数 | number(10) | ✓ | 93.82% |  |
| 77 | `FundsHoldingsANum` | 公募基金持有流通A股户数 | number(10) | ✓ | 91.4% |  |
| 78 | `PrivFundHoldANum` | 私募基金持有流通A股户数 | number(10) | ✓ | 9.65% |  |
| 79 | `SecuCorpsHoldANum` | 券商持有流通A股户数 | number(10) | ✓ | 10.67% |  |
| 80 | `FinProductsHoldANum` | 券商理财产品持有流通A股户数 | number(10) | ✓ | 5.56% |  |
| 81 | `BankHoldANum` | 银行持有流通A股户数 | number(10) | ✓ | 0.03% |  |
| 82 | `InsurCorpsHoldANum` | 保险公司持有流通A股户数 | number(10) | ✓ | 3.64% |  |
| 83 | `SocialSecuFundHoldAN` | 社保基金持有流通A股户数 | number(10) | ✓ | 6.22% |  |
| 84 | `EntAnnuitiesHoldANum` | 企业年金持有流通A股户数 | number(10) | ✓ | 0.38% |  |
| 85 | `TrustCoHoldANum` | 信托公司持有流通A股户数 | number(10) | ✓ | 1.0% |  |
| 86 | `FinanceCoHoldANum` | 财务公司持有流通A股户数 | number(10) | ✓ | 0.12% |  |
| 87 | `ForeignInstHoldANum` | 外资持有流通A股户数 | number(10) | ✓ | 17.5% |  |
| 88 | `QFIIHoldANum` | #QFII持有流通A股户数 | number(10) | ✓ | 4.58% |  |
| 89 | `OtherInstiHoldANum` | 其他机构持有流通A股户数 | number(10) | ✓ | 40.21% |  |
| 90 | `InstitutionsHoldingsT` | 机构持股数量合计(股) | number(18,2) | ✓ | 99.95% |  |
| 91 | `FundsHoldingsT` | 公募基金持股数量(股) | number(18,2) | ✓ | 92.14% |  |
| 92 | `PrivFundHoldingsT` | 私募基金持股数量(股) | number(18,2) | ✓ | 9.7% |  |
| 93 | `SecuCorpsHoldingsT` | 券商持股数量(股) | number(18,2) | ✓ | 11.07% |  |
| 94 | `FinProductsHoldingsT` | 券商理财产品持股数量(股) | number(18,2) | ✓ | 5.58% |  |
| 95 | `BankHoldingsT` | 银行持股数量(股) | number(18,2) | ✓ | 0.03% |  |
| 96 | `InsurCorpsHoldingsT` | 保险公司持股数量(股) | number(18,2) | ✓ | 3.68% |  |
| 97 | `SocialSecuFundHoldT` | 社保基金持股数量(股) | number(18,2) | ✓ | 6.23% |  |
| 98 | `EntAnnuitiesHoldingsT` | 企业年金持股数量(股) | number(18,2) | ✓ | 0.38% |  |
| 99 | `TrustCoHoldingsT` | 信托公司持股数量(股) | number(18,2) | ✓ | 1.01% |  |
| 100 | `FinanceCompHoldingsT` | 财务公司持股数量(股) | number(18,2) | ✓ | 0.15% |  |
| 101 | `ForeignInstHoldingsT` | 外资机构持股数量(股) | number(18,2) | ✓ | 19.16% |  |
| 102 | `QFIIHoldingsT` | #QFII持股数量(股) | number(18,2) | ✓ | 4.71% |  |
| 103 | `OtherInstiHoldingsT` | 其它机构持股数量(股) | number(18,2) | ✓ | 45.83% |  |
| 104 | `InstitutionsHoldPropT` | 机构持股比例合计(%) | number(18,4) | ✓ | 99.41% |  |
| 105 | `FundsHoldPropT` | 公募基金持股比例(%) | number(18,4) | ✓ | 91.63% |  |
| 106 | `PrivFundHoldPropT` | 私募基金持股比例(%) | number(18,4) | ✓ | 9.7% |  |
| 107 | `SecuCorpsHoldPropT` | 券商持股比例(%) | number(18,4) | ✓ | 11.07% |  |
| 108 | `FinProductsHoldPropT` | 券商理财产品持股比例(%) | number(18,4) | ✓ | 5.58% |  |
| 109 | `BankHoldPropT` | 银行持股比例(%) | number(18,4) | ✓ | 0.03% |  |
| 110 | `InsurCorpsHoldPropT` | 保险公司持股比例(%) | number(18,4) | ✓ | 3.68% |  |
| 111 | `SociSecuFundHoldPropT` | 社保基金持股比例(%) | number(18,4) | ✓ | 6.23% |  |
| 112 | `CorpAnnuitiesHoldPropT` | 企业年金持股比例(%) | number(18,4) | ✓ | 0.38% |  |
| 113 | `TrustCoHoldPropT` | 信托公司持股比例(%) | number(18,4) | ✓ | 1.01% |  |
| 114 | `FinanceCompHoldPropT` | 财务公司持股比例(%) | number(18,4) | ✓ | 0.15% |  |
| 115 | `ForeignInstHoldPropT` | 外资机构持股比例(%) | number(18,4) | ✓ | 19.15% |  |
| 116 | `QFIIHoldPropT` | #QFII持股比例(%) | number(18,4) | ✓ | 4.71% |  |
| 117 | `OtherInstiHoldPropT` | 其它机构持股比例(%) | number(18,4) | ✓ | 45.8% |  |
| 118 | `InstiHoldTNum` | 机构持股户数 | number(10) | ✓ | 99.95% |  |
| 119 | `FundsHoldingsTNum` | 公募基金持股户数 | number(10) | ✓ | 92.14% |  |
| 120 | `PrivFundHoldTNum` | 私募基金持股户数 | number(10) | ✓ | 9.7% |  |
| 121 | `SecuCorpsHoldTNum` | 券商持股户数 | number(10) | ✓ | 11.07% |  |
| 122 | `FinProductsHoldTNum` | 券商理财产品持股户数 | number(10) | ✓ | 5.58% |  |
| 123 | `BankHoldTNum` | 银行持股户数 | number(10) | ✓ | 0.03% |  |
| 124 | `InsurCorpsHoldTNum` | 保险公司持股户数 | number(10) | ✓ | 3.68% |  |
| 125 | `SocialSecuFundHoldTN` | 社保基金持股户数 | number(10) | ✓ | 6.23% |  |
| 126 | `EntAnnuitiesHoldTNum` | 企业年金持股户数 | number(10) | ✓ | 0.38% |  |
| 127 | `TrustCoHoldTNum` | 信托公司持股户数 | number(10) | ✓ | 1.01% |  |
| 128 | `FinanceCoHoldTNum` | 财务公司持股户数 | number(10) | ✓ | 0.15% |  |
| 129 | `ForeignInstHoldTNum` | 外资持股户数 | number(10) | ✓ | 19.16% |  |
| 130 | `QFIIHoldTNumber` | #QFII持股户数 | number(10) | ✓ | 4.71% |  |
| 131 | `OtherInstiHoldTNum` | 其他机构持股户数 | number(10) | ✓ | 45.83% |  |
| 132 | `TopTenHoldersHoldings` | 前十大股东持股数量合计(股) | number(18,2) | ✓ | 46.68% |  |
| 133 | `TopTenHoldersHProp` | 前十大股东持股比例合计(%)1 | number(18,4) | ✓ | 46.68% |  |
| 134 | `TopTNRHoldersHoldings` | 前十大无限售股东持股数量合计(股) | number(18,2) | ✓ | 41.03% |  |
| 135 | `TopTenNRHoldersHToNRS` | 前十大无限售股东持股数占无限售股本比例(%) | number(18,4) | ✓ | 41.03% |  |
| 136 | `TopTenNRHoldersHToTS` | 前十大无限售股东持股数占总股本的比例(%) | number(18,4) | ✓ | 41.03% |  |
| 137 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 138 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 139 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到科创板A股发行人的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“基金定报”时，数据源为上市公司定报及基金定报。

### InstitutionsHoldings (机构持有无限售流通A股数量合计(股))

由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”的值暂时不计算，为空值

## SQL示例

```sql
-- 查询 科创板股东持股统计 数据
SELECT *
FROM lc_stibstockholdingst
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
