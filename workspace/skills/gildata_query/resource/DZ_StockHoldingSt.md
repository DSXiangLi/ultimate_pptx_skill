# DZ_StockHoldingSt

**中文名**: 股东持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_StockHoldingSt` |
| MySQL表名 | `dz_stockholdingst` |
| 中文名 | 股东持股统计 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 141 |
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
4.数据范围：1992年至今
5.信息来源：招股说明书、上市公告书、定报、临时公告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% |  |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `StatDate` | 统计日期 | date | ✓ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.96% | 信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“... |
| 7 | `InstitutionsHoldings` | 机构持有无限售流通A股数量合计(股) | number(18,2) | ✓ | 48.82% |  |
| 8 | `FundsHoldings` | 公募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.0% | 由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”... |
| 9 | `PrivFundHoldings` | 私募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 6.2% |  |
| 10 | `SecuCorpsHoldings` | 券商持有无限售流通A股数量(股) | number(18,2) | ✓ | 9.46% |  |
| 11 | `FinProductsHoldings` | 券商理财产品持有无限售流通A股数量(股) | number(18,2) | ✓ | 2.14% |  |
| 12 | `BankHoldings` | 银行持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.38% |  |
| 13 | `InsuranceCorpsHoldings` | 保险公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 7.68% |  |
| 14 | `SocialSecurityFundHold` | 社保基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 9.07% |  |
| 15 | `EntAnnuitiesHoldings` | 企业年金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.43% |  |
| 16 | `TrustCompaniesHoldings` | 信托公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 7.69% |  |
| 17 | `FinanceCoHoldings` | 财务公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.54% |  |
| 18 | `ForeignInstHoldings` | 外资机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 17.23% |  |
| 19 | `QFIIHoldings` | #QFII持有无限售流通A股数量(股) | number(18,2) | ✓ | 4.95% |  |
| 20 | `OtherInstiHoldings` | 其它机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 43.44% |  |
| 21 | `InstitutionsHoldProp` | 机构持有无限售流通A股比例合计(%) | number(18,4) | ✓ | 48.55% |  |
| 22 | `FundsHoldProp` | 公募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.0% |  |
| 23 | `PrivFundHoldProp` | 私募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 6.18% |  |
| 24 | `SecuCorpsHoldProp` | 券商持有无限售流通A股比例(%) | number(18,4) | ✓ | 9.42% |  |
| 25 | `FinProductsHoldProp` | 券商理财产品持有无限售流通A股比例(%) | number(18,4) | ✓ | 2.14% |  |
| 26 | `BankHoldProp` | 银行持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.38% |  |
| 27 | `InsuranceCorpsHoldProp` | 保险公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 7.68% |  |
| 28 | `SocialSecuFundHoldProp` | 社保基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 9.06% |  |
| 29 | `CorpAnnuitiesHoldProp` | 企业年金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.42% |  |
| 30 | `TrustCompaniesHoldProp` | 信托公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 7.68% |  |
| 31 | `FinanceCoHoldProp` | 财务公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.54% |  |
| 32 | `ForeignInstHoldProp` | 外资机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 17.22% |  |
| 33 | `QFIIHoldProp` | QFII持有无限售流通A股比例(%) | number(18,4) | ✓ | 4.95% |  |
| 34 | `OtherInstiHoldProp` | 其它机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 43.19% |  |
| 35 | `InstiHoldNum` | 机构持有无限售流通A股户数 | number(10) | ✓ | 48.82% |  |
| 36 | `PrivFundHoldNum` | 私募基金持有无限售流通A股户数 | number(10) | ✓ | 6.2% |  |
| 37 | `SecuCorpsHoldNum` | 券商持有无限售流通A股户数 | number(10) | ✓ | 9.46% |  |
| 38 | `FinProductsHoldNum` | 券商理财产品持有无限售流通A股户数 | number(10) | ✓ | 2.14% |  |
| 39 | `BankHoldNum` | 银行持有无限售流通A股户数 | number(10) | ✓ | 0.38% |  |
| 40 | `InsurCorpsHoldNum` | 保险公司持有无限售流通A股户数 | number(10) | ✓ | 7.68% |  |
| 41 | `SocialSecuFundHoldN` | 社保基金持有无限售流通A股户数 | number(10) | ✓ | 9.07% |  |
| 42 | `EntAnnuitiesHoldNum` | 企业年金持有无限售流通A股户数 | number(10) | ✓ | 0.43% |  |
| 43 | `TrustCoHoldNum` | 信托公司持有无限售流通A股户数 | number(10) | ✓ | 7.69% |  |
| 44 | `FinanceCoHoldNum` | 财务公司持有无限售流通A股户数 | number(10) | ✓ | 0.54% |  |
| 45 | `ForeignInstHoldNum` | 外资持有无限售流通A股户数 | number(10) | ✓ | 17.23% |  |
| 46 | `QFIIHoldingsNum` | #QFII持有无限售流通A股户数 | number(10) | ✓ | 4.95% |  |
| 47 | `OtherInstiHoldNum` | 其他机构持有无限售流通A股户数 | number(10) | ✓ | 43.44% |  |
| 48 | `InstitutionsHoldingsA` | 机构持有A股数量合计(股) | number(18,2) | ✓ | 95.73% |  |
| 49 | `FundsHoldingsA` | 公募基金持有A股数量(股) | number(18,2) | ✓ | 87.55% |  |
| 50 | `PrivFundHoldingsA` | 私募基金持A股数量(股) | number(18,2) | ✓ | 6.47% |  |
| 51 | `SecuCorpsHoldingsA` | 券商持有A股数量(股) | number(18,2) | ✓ | 9.99% |  |
| 52 | `FinProductsHoldingsA` | 券商理财产品持有A股数量(股) | number(18,2) | ✓ | 2.57% |  |
| 53 | `BankHoldingsA` | 银行持有A股数量(股) | number(18,2) | ✓ | 0.47% |  |
| 54 | `InsurCorpsHoldingsA` | 保险公司持有A股数量(股) | number(18,2) | ✓ | 7.99% |  |
| 55 | `SocialSecuFundHoldA` | 社保基金持有A股数量(股) | number(18,2) | ✓ | 9.61% |  |
| 56 | `EntAnnuitiesHoldingsA` | 企业年金持有A股数量(股) | number(18,2) | ✓ | 0.45% |  |
| 57 | `TrustCoHoldingsA` | 信托公司持有A股数量(股) | number(18,2) | ✓ | 8.24% |  |
| 58 | `FinanceCompHoldingsA` | 财务公司持有A股数量(股) | number(18,2) | ✓ | 0.67% |  |
| 59 | `ForeignInstHoldingsA` | 外资机构持A股数量(股) | number(18,2) | ✓ | 18.19% |  |
| 60 | `QFIIHoldingsA` | #QFII持有A股数量(股) | number(18,2) | ✓ | 5.02% |  |
| 61 | `OtherInstiHoldingsA` | 其它机构持有A股数量(股) | number(18,2) | ✓ | 47.22% |  |
| 62 | `InstitutionsHoldPropA` | 机构持有A股比例合计(%) | number(18,4) | ✓ | 95.22% |  |
| 63 | `FundsHoldPropA` | 公募基金持有A股比例(%) | number(18,4) | ✓ | 87.31% |  |
| 64 | `PrivFundHoldPropA` | 私募基金持有A股比例(%) | number(18,4) | ✓ | 6.46% |  |
| 65 | `SecuCorpsHoldPropA` | 券商持有A股比例(%) | number(18,4) | ✓ | 9.95% |  |
| 66 | `FinProductsHoldPropA` | 券商理财产品持有A股比例(%) | number(18,4) | ✓ | 2.57% |  |
| 67 | `BankHoldPropA` | 银行持有A股比例(%) | number(18,4) | ✓ | 0.47% |  |
| 68 | `InsurCorpsHoldPropA` | 保险公司持有A股比例(%) | number(18,4) | ✓ | 7.98% |  |
| 69 | `SociSecuFundHoldPropA` | 社保基金持有A股比例(%) | number(18,4) | ✓ | 9.6% |  |
| 70 | `CorpAnnuitiesHoldPropA` | 企业年金持有A股比例(%) | number(18,4) | ✓ | 0.44% |  |
| 71 | `TrustCoHoldPropA` | 信托公司持有A股比例(%) | number(18,4) | ✓ | 8.23% |  |
| 72 | `FinanceCompHoldPropA` | 财务公司持有A股比例(%) | number(18,4) | ✓ | 0.66% |  |
| 73 | `ForeignInstHoldPropA` | 外资机构持有A股比例(%) | number(18,4) | ✓ | 18.17% |  |
| 74 | `QFIIHoldPropA` | #QFII持有A股比例(%) | number(18,4) | ✓ | 5.02% |  |
| 75 | `OtherInstiHoldPropA` | 其它机构持有A股比例(%) | number(18,4) | ✓ | 46.93% |  |
| 76 | `InstiHoldANum` | 机构持有流通A股户数 | number(10) | ✓ | 95.73% |  |
| 77 | `FundsHoldingsANum` | 公募基金持有流通A股户数 | number(10) | ✓ | 87.55% |  |
| 78 | `PrivFundHoldANum` | 私募基金持有流通A股户数 | number(10) | ✓ | 6.47% |  |
| 79 | `SecuCorpsHoldANum` | 券商持有流通A股户数 | number(10) | ✓ | 9.99% |  |
| 80 | `FinProductsHoldANum` | 券商理财产品持有流通A股户数 | number(10) | ✓ | 2.57% |  |
| 81 | `BankHoldANum` | 银行持有流通A股户数 | number(10) | ✓ | 0.47% |  |
| 82 | `InsurCorpsHoldANum` | 保险公司持有流通A股户数 | number(10) | ✓ | 7.99% |  |
| 83 | `SocialSecuFundHoldAN` | 社保基金持有流通A股户数 | number(10) | ✓ | 9.61% |  |
| 84 | `EntAnnuitiesHoldANum` | 企业年金持有流通A股户数 | number(10) | ✓ | 0.45% |  |
| 85 | `TrustCoHoldANum` | 信托公司持有流通A股户数 | number(10) | ✓ | 8.24% |  |
| 86 | `FinanceCoHoldANum` | 财务公司持有流通A股户数 | number(10) | ✓ | 0.67% |  |
| 87 | `ForeignInstHoldANum` | 外资持有流通A股户数 | number(10) | ✓ | 18.19% |  |
| 88 | `QFIIHoldANum` | #QFII持有流通A股户数 | number(10) | ✓ | 5.02% |  |
| 89 | `OtherInstiHoldANum` | 其他机构持有流通A股户数 | number(10) | ✓ | 47.22% |  |
| 90 | `InstitutionsHoldingsT` | 机构持股数量合计(股) | number(18,2) | ✓ | 99.24% |  |
| 91 | `FundsHoldingsT` | 公募基金持股数量(股) | number(18,2) | ✓ | 87.79% |  |
| 92 | `PrivFundHoldingsT` | 私募基金持股数量(股) | number(18,2) | ✓ | 6.5% |  |
| 93 | `SecuCorpsHoldingsT` | 券商持股数量(股) | number(18,2) | ✓ | 10.59% |  |
| 94 | `FinProductsHoldingsT` | 券商理财产品持股数量(股) | number(18,2) | ✓ | 2.57% |  |
| 95 | `BankHoldingsT` | 银行持股数量(股) | number(18,2) | ✓ | 0.75% |  |
| 96 | `InsurCorpsHoldingsT` | 保险公司持股数量(股) | number(18,2) | ✓ | 8.11% |  |
| 97 | `SocialSecuFundHoldT` | 社保基金持股数量(股) | number(18,2) | ✓ | 9.63% |  |
| 98 | `EntAnnuitiesHoldingsT` | 企业年金持股数量(股) | number(18,2) | ✓ | 0.45% |  |
| 99 | `TrustCoHoldingsT` | 信托公司持股数量(股) | number(18,2) | ✓ | 8.9% |  |
| 100 | `FinanceCompHoldingsT` | 财务公司持股数量(股) | number(18,2) | ✓ | 0.77% |  |
| 101 | `ForeignInstHoldingsT` | 外资机构持股数量(股) | number(18,2) | ✓ | 20.72% |  |
| 102 | `QFIIHoldingsT` | #QFII持股数量(股) | number(18,2) | ✓ | 5.37% |  |
| 103 | `OtherInstiHoldingsT` | 其它机构持股数量(股) | number(18,2) | ✓ | 51.85% |  |
| 104 | `InstitutionsHoldPropT` | 机构持股比例合计(%) | number(18,4) | ✓ | 99.14% |  |
| 105 | `FundsHoldPropT` | 公募基金持股比例(%) | number(18,4) | ✓ | 87.7% |  |
| 106 | `PrivFundHoldPropT` | 私募基金持股比例(%) | number(18,4) | ✓ | 6.5% |  |
| 107 | `SecuCorpsHoldPropT` | 券商持股比例(%) | number(18,4) | ✓ | 10.59% |  |
| 108 | `FinProductsHoldPropT` | 券商理财产品持股比例(%) | number(18,4) | ✓ | 2.57% |  |
| 109 | `BankHoldPropT` | 银行持股比例(%) | number(18,4) | ✓ | 0.75% |  |
| 110 | `InsurCorpsHoldPropT` | 保险公司持股比例(%) | number(18,4) | ✓ | 8.11% |  |
| 111 | `SociSecuFundHoldPropT` | 社保基金持股比例(%) | number(18,4) | ✓ | 9.63% |  |
| 112 | `CorpAnnuitiesHoldPropT` | 企业年金持股比例(%) | number(18,4) | ✓ | 0.45% |  |
| 113 | `TrustCoHoldPropT` | 信托公司持股比例(%) | number(18,4) | ✓ | 8.9% |  |
| 114 | `FinanceCompHoldPropT` | 财务公司持股比例(%) | number(18,4) | ✓ | 0.77% |  |
| 115 | `ForeignInstHoldPropT` | 外资机构持股比例(%) | number(18,4) | ✓ | 20.72% |  |
| 116 | `QFIIHoldPropT` | #QFII持股比例(%) | number(18,4) | ✓ | 5.37% |  |
| 117 | `OtherInstiHoldPropT` | 其它机构持股比例(%) | number(18,4) | ✓ | 51.83% |  |
| 118 | `InstiHoldTNum` | 机构持股户数 | number(10) | ✓ | 99.24% |  |
| 119 | `PrivFundHoldTNum` | 私募基金持股户数 | number(10) | ✓ | 6.5% |  |
| 120 | `FundsHoldingsTNum` | 公募基金持股户数 | number(10) | ✓ | 87.79% |  |
| 121 | `SecuCorpsHoldTNum` | 券商持股户数 | number(10) | ✓ | 10.59% |  |
| 122 | `FinProductsHoldTNum` | 券商理财产品持股户数 | number(10) | ✓ | 2.57% |  |
| 123 | `BankHoldTNum` | 银行持股户数 | number(10) | ✓ | 0.75% |  |
| 124 | `InsurCorpsHoldTNum` | 保险公司持股户数 | number(10) | ✓ | 8.11% |  |
| 125 | `SocialSecuFundHoldTN` | 社保基金持股户数 | number(10) | ✓ | 9.63% |  |
| 126 | `EntAnnuitiesHoldTNum` | 企业年金持股户数 | number(10) | ✓ | 0.45% |  |
| 127 | `TrustCoHoldTNum` | 信托公司持股户数 | number(10) | ✓ | 8.9% |  |
| 128 | `FinanceCoHoldTNum` | 财务公司持股户数 | number(10) | ✓ | 0.77% |  |
| 129 | `ForeignInstHoldTNum` | 外资持股户数 | number(10) | ✓ | 20.72% |  |
| 130 | `QFIIHoldTNumber` | #QFII持股户数 | number(10) | ✓ | 5.37% |  |
| 131 | `OtherInstiHoldTNum` | 其他机构持股户数 | number(10) | ✓ | 51.85% |  |
| 132 | `TopTenHoldersHoldings` | 前十大股东持股数量合计(股) | number(18,2) | ✓ | 52.2% |  |
| 133 | `TopTenHoldersHProp` | 前十大股东持股比例合计(%) | number(18,4) | ✓ | 52.2% |  |
| 134 | `TopTNRHoldersHoldings` | 前十大无限售股东持股数量合计(股) | number(18,2) | ✓ | 51.69% |  |
| 135 | `TopTenNRHoldersHToNRS` | 前十大无限售股东持股数占无限售股本比例(%) | number(18,4) | ✓ | 51.65% |  |
| 136 | `TopTenNRHoldersHToTS` | 前十大无限售股东持股数占总股本的比例(%) | number(18,4) | ✓ | 51.69% |  |
| 137 | `TopTenNRHoldersHToNRA` | 前十大无限售股东持有无限售A股数量合计(股) | number(18,2) | ✓ | 51.42% |  |
| 138 | `TopTenNRAHoldersHToNRA` | 前十大无限售股东持有无限售A股数占无限售A股比例(%) | number(18,4) | ✓ | 51.38% |  |
| 139 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 140 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 141 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到A股、B股、CDR等发行人的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“基金定报”时，数据源为上市公司定报及基金定报。

### FundsHoldings (公募基金持有无限售流通A股数量(股))

由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”的值暂时不计算，为空值

## SQL示例

```sql
-- 查询 股东持股统计 数据
SELECT *
FROM dz_stockholdingst
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
