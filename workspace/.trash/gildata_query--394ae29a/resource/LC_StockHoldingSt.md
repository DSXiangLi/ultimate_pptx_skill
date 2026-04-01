# LC_StockHoldingSt

**中文名**: 股东持股统计

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_StockHoldingSt` |
| MySQL表名 | `lc_stockholdingst` |
| 中文名 | 股东持股统计 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 141 |
| 版本 | 1.04 |

## 表描述

1.收录报告期末，各类机构投资者对每只股票的持仓情况，以及前十大（无限售条件）股东合计持股情况等。
2.机构持股统计中，基金持股综合考虑了上市公司披露的十大股东数据以及基金报告中披露的基金持股数据；机构持股合计包含上市公司披露的股东持股以及在同一截止时点上基金披露的所持股票数据。
3.计算公式：
1)机构持有无限售流通股数量＝机构持有无限售流通A股之和
2)机构持有无限售流通股比例＝(机构持有无限售流通股数量/无限售A股)*100%
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
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `StatDate` | 统计日期 | date | ✓ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.96% | 信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“... |
| 7 | `InstitutionsHoldings` | 机构持有无限售流通A股数量合计(股) | number(18,2) | ✓ | 49.35% |  |
| 8 | `FundsHoldings` | 公募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.0% | 由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”... |
| 9 | `PrivFundHoldings` | 私募基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 6.03% |  |
| 10 | `SecuritiesCorpsHoldings` | 券商持有无限售流通A股数量(股) | number(18,2) | ✓ | 9.61% |  |
| 11 | `FinancingProductsHoldings` | 券商理财产品持有无限售流通A股数量(股) | number(18,2) | ✓ | 2.09% |  |
| 12 | `BankHoldings` | 银行持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.4% |  |
| 13 | `InsuranceCorpsHoldings` | 保险公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 7.91% |  |
| 14 | `SocialSecurityFundHold` | 社保基金持有无限售流通A股数量(股) | number(18,2) | ✓ | 9.23% |  |
| 15 | `EnterpriseAnnuitiesHold` | 企业年金持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.44% |  |
| 16 | `TrustCompaniesHoldings` | 信托公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 8.05% |  |
| 17 | `FinanceCompaniesHoldings` | 财务公司持有无限售流通A股数量(股) | number(18,2) | ✓ | 0.57% |  |
| 18 | `ForeignInstHoldings` | 外资机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 17.38% |  |
| 19 | `QFIIHoldings` | #QFII持有无限售流通A股数量(股) | number(18,2) | ✓ | 4.98% |  |
| 20 | `OtherInstitutionHoldings` | 其它机构持有无限售流通A股数量(股) | number(18,2) | ✓ | 44.04% |  |
| 21 | `InstitutionsHoldProp` | 机构持有无限售流通A股比例合计(%) | number(18,4) | ✓ | 49.06% |  |
| 22 | `FundsHoldProp` | 公募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.0% |  |
| 23 | `PrivFundHoldProp` | 私募基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 6.01% |  |
| 24 | `SecuritiesCorpsHoldProp` | 券商持有无限售流通A股比例(%) | number(18,4) | ✓ | 9.57% |  |
| 25 | `FinancingProductsHoldProp` | 券商理财产品持有无限售流通A股比例(%) | number(18,4) | ✓ | 2.09% |  |
| 26 | `BankHoldProp` | 银行持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.4% |  |
| 27 | `InsuranceCorpsHoldProp` | 保险公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 7.91% |  |
| 28 | `SocialSecuFundHoldProp` | 社保基金持有无限售流通A股比例(%) | number(18,4) | ✓ | 9.22% |  |
| 29 | `CorpAnnuitiesHoldProp` | 企业年金持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.43% |  |
| 30 | `TrustCompaniesHoldProp` | 信托公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 8.05% |  |
| 31 | `FinanceCompaniesHoldProp` | 财务公司持有无限售流通A股比例(%) | number(18,4) | ✓ | 0.57% |  |
| 32 | `ForeignInstHoldProp` | 外资机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 17.37% |  |
| 33 | `QFIIHoldProp` | #QFII持有无限售流通A股比例(%) | number(18,4) | ✓ | 4.98% |  |
| 34 | `OtherInstitutionHoldProp` | 其它机构持有无限售流通A股比例(%) | number(18,4) | ✓ | 43.79% |  |
| 35 | `InstiHoldNum` | 机构持有无限售流通A股户数 | number(10) | ✓ | 49.35% |  |
| 36 | `PrivFundHoldNum` | 私募基金持有无限售流通A股户数 | number(10) | ✓ | 6.03% |  |
| 37 | `SecuCorpsHoldNum` | 券商持有无限售流通A股户数 | number(10) | ✓ | 9.61% |  |
| 38 | `FinProductsHoldNum` | 券商理财产品持有无限售流通A股户数 | number(10) | ✓ | 2.09% |  |
| 39 | `BankHoldNum` | 银行持有无限售流通A股户数 | number(10) | ✓ | 0.4% |  |
| 40 | `InsurCorpsHoldNum` | 保险公司持有无限售流通A股户数 | number(10) | ✓ | 7.91% |  |
| 41 | `SocialSecuFundHoldN` | 社保基金持有无限售流通A股户数 | number(10) | ✓ | 9.23% |  |
| 42 | `EntAnnuitiesHoldNum` | 企业年金持有无限售流通A股户数 | number(10) | ✓ | 0.44% |  |
| 43 | `TrustCoHoldNum` | 信托公司持有无限售流通A股户数 | number(10) | ✓ | 8.05% |  |
| 44 | `FinanceCoHoldNum` | 财务公司持有无限售流通A股户数 | number(10) | ✓ | 0.57% |  |
| 45 | `ForeignInstHoldNum` | 外资持有无限售流通A股户数 | number(10) | ✓ | 17.38% |  |
| 46 | `QFIIHoldingsNum` | #QFII持有无限售流通A股户数 | number(10) | ✓ | 4.98% |  |
| 47 | `OtherInstiHoldNum` | 其他机构持有无限售流通A股户数 | number(10) | ✓ | 44.04% |  |
| 48 | `InstitutionsHoldingsA` | 机构持有A股数量合计(股) | number(18,2) | ✓ | 95.87% |  |
| 49 | `FundsHoldingsA` | 公募基金持有A股数量(股) | number(18,2) | ✓ | 87.41% |  |
| 50 | `PrivFundHoldingsA` | 私募基金持A股数量(股) | number(18,2) | ✓ | 6.31% |  |
| 51 | `SecuritiesCorpsHoldingsA` | 券商持有A股数量(股) | number(18,2) | ✓ | 9.96% |  |
| 52 | `FinanceProductsHoldingsA` | 券商理财产品持有A股数量(股) | number(18,2) | ✓ | 2.41% |  |
| 53 | `BankHoldingsA` | 银行持有A股数量(股) | number(18,2) | ✓ | 0.5% |  |
| 54 | `InsuranceCorpsHoldingsA` | 保险公司持有A股数量(股) | number(18,2) | ✓ | 8.22% |  |
| 55 | `SocialSecurityFundHoldA` | 社保基金持有A股数量(股) | number(18,2) | ✓ | 9.79% |  |
| 56 | `EnterpriseAnnuitiesHoldA` | 企业年金持有A股数量(股) | number(18,2) | ✓ | 0.45% |  |
| 57 | `TrustCompaniesHoldingsA` | 信托公司持有A股数量(股) | number(18,2) | ✓ | 8.63% |  |
| 58 | `FinanceCompHoldingsA` | 财务公司持有A股数量(股) | number(18,2) | ✓ | 0.7% |  |
| 59 | `ForeignInstHoldingsA` | 外资机构持A股数量(股) | number(18,2) | ✓ | 18.24% |  |
| 60 | `QFIIHoldingsA` | #QFII持有A股数量(股) | number(18,2) | ✓ | 5.05% |  |
| 61 | `OtherInstiHoldingsA` | 其它机构持有A股数量(股) | number(18,2) | ✓ | 47.61% |  |
| 62 | `InstitutionsHoldPropA` | 机构持有A股比例合计(%) | number(18,4) | ✓ | 95.38% |  |
| 63 | `FundsHoldPropA` | 公募基金持有A股比例(%) | number(18,4) | ✓ | 87.2% |  |
| 64 | `PrivFundHoldPropA` | 私募基金持有A股比例(%) | number(18,4) | ✓ | 6.29% |  |
| 65 | `SecuritiesCorpsHoldPropA` | 券商持有A股比例(%) | number(18,4) | ✓ | 9.92% |  |
| 66 | `FinanceProductsHoldPropA` | 券商理财产品持有A股比例(%) | number(18,4) | ✓ | 2.41% |  |
| 67 | `BankHoldPropA` | 银行持有A股比例(%) | number(18,4) | ✓ | 0.5% |  |
| 68 | `InsuranceCorpsHoldPropA` | 保险公司持有A股比例(%) | number(18,4) | ✓ | 8.22% |  |
| 69 | `SocialSecuFundHoldPropA` | 社保基金持有A股比例(%) | number(18,4) | ✓ | 9.79% |  |
| 70 | `CorpAnnuitiesHoldPropA` | 企业年金持有A股比例(%) | number(18,4) | ✓ | 0.44% |  |
| 71 | `TrustCompaniesHoldPropA` | 信托公司持有A股比例(%) | number(18,4) | ✓ | 8.62% |  |
| 72 | `FinanceCompHoldPropA` | 财务公司持有A股比例(%) | number(18,4) | ✓ | 0.69% |  |
| 73 | `ForeignInstHoldPropA` | 外资机构持有A股比例(%) | number(18,4) | ✓ | 18.23% |  |
| 74 | `QFIIHoldPropA` | #QFII持有A股比例(%) | number(18,4) | ✓ | 5.05% |  |
| 75 | `OtherInstiHoldPropA` | 其它机构持有A股比例(%) | number(18,4) | ✓ | 47.3% |  |
| 76 | `InstiHoldANum` | 机构持有A股户数 | number(10) | ✓ | 95.87% |  |
| 77 | `FundsHoldingsANum` | 公募基金持有流通A股户数 | number(10) | ✓ | 87.41% |  |
| 78 | `PrivFundHoldANum` | 私募基金持有流通A股户数 | number(10) | ✓ | 6.31% |  |
| 79 | `SecuCorpsHoldANum` | 券商持有A股户数 | number(10) | ✓ | 9.96% |  |
| 80 | `FinProductsHoldANum` | 券商理财产品持有A股户数 | number(10) | ✓ | 2.41% |  |
| 81 | `BankHoldANum` | 银行持有流通A股户数 | number(10) | ✓ | 0.5% |  |
| 82 | `InsurCorpsHoldANum` | 保险公司持有A股户数 | number(10) | ✓ | 8.22% |  |
| 83 | `SocialSecuFundHoldAN` | 社保基金持有A股户数 | number(10) | ✓ | 9.79% |  |
| 84 | `EntAnnuitiesHoldANum` | 企业年金持有A股户数 | number(10) | ✓ | 0.45% |  |
| 85 | `TrustCoHoldANum` | 信托公司持有A股户数 | number(10) | ✓ | 8.63% |  |
| 86 | `FinanceCoHoldANum` | 财务公司持有A股户数 | number(10) | ✓ | 0.7% |  |
| 87 | `ForeignInstHoldANum` | 外资持有流通A股户数 | number(10) | ✓ | 18.24% |  |
| 88 | `QFIIHoldANum` | #QFII持有A股户数 | number(10) | ✓ | 5.05% |  |
| 89 | `OtherInstiHoldANum` | 其他机构持有A股户数 | number(10) | ✓ | 47.61% |  |
| 90 | `InstitutionsHoldingsT` | 机构持股数量合计(股) | number(18,2) | ✓ | 99.22% |  |
| 91 | `FundsHoldingsT` | 公募基金持股数量(股) | number(18,2) | ✓ | 87.63% |  |
| 92 | `PrivFundHoldingsT` | 私募基金持股数量(股) | number(18,2) | ✓ | 6.33% |  |
| 93 | `SecuritiesCorpsHoldingsT` | 券商持股数量(股) | number(18,2) | ✓ | 10.56% |  |
| 94 | `FinanceProductsHoldingsT` | 券商理财产品持股数量(股) | number(18,2) | ✓ | 2.42% |  |
| 95 | `BankHoldingsT` | 银行持股数量(股) | number(18,2) | ✓ | 0.78% |  |
| 96 | `InsuranceCorpsHoldingsT` | 保险公司持股数量(股) | number(18,2) | ✓ | 8.35% |  |
| 97 | `SocialSecurityFundHoldT` | 社保基金持股数量(股) | number(18,2) | ✓ | 9.82% |  |
| 98 | `EnterpriseAnnuitiesHoldT` | 企业年金持股数量(股) | number(18,2) | ✓ | 0.46% |  |
| 99 | `TrustCompaniesHoldingsT` | 信托公司持股数量(股) | number(18,2) | ✓ | 9.31% |  |
| 100 | `FinanceCompHoldingsT` | 财务公司持股数量(股) | number(18,2) | ✓ | 0.8% |  |
| 101 | `ForeignInstHoldingsT` | 外资机构持股数量(股) | number(18,2) | ✓ | 20.82% |  |
| 102 | `QFIIHoldingsT` | #QFII持股数量(股) | number(18,2) | ✓ | 5.41% |  |
| 103 | `OtherInstiHoldingsT` | 其它机构持股数量(股) | number(18,2) | ✓ | 52.16% |  |
| 104 | `InstitutionsHoldPropT` | 机构持股比例合计(%) | number(18,4) | ✓ | 99.14% |  |
| 105 | `FundsHoldPropT` | 公募基金持股比例(%) | number(18,4) | ✓ | 87.57% |  |
| 106 | `PrivFundHoldPropT` | 私募基金持股比例(%) | number(18,4) | ✓ | 6.33% |  |
| 107 | `SecuritiesCorpsHoldPropT` | 券商持股比例(%) | number(18,4) | ✓ | 10.56% |  |
| 108 | `FinanceProductsHoldPropT` | 券商理财产品持股比例(%) | number(18,4) | ✓ | 2.42% |  |
| 109 | `BankHoldPropT` | 银行持股比例(%) | number(18,4) | ✓ | 0.78% |  |
| 110 | `InsuranceCorpsHoldPropT` | 保险公司持股比例(%) | number(18,4) | ✓ | 8.35% |  |
| 111 | `SocialSecuFundHoldPropT` | 社保基金持股比例(%) | number(18,4) | ✓ | 9.82% |  |
| 112 | `CorpAnnuitiesHoldPropT` | 企业年金持股比例(%) | number(18,4) | ✓ | 0.46% |  |
| 113 | `TrustCompaniesHoldPropT` | 信托公司持股比例(%) | number(18,4) | ✓ | 9.31% |  |
| 114 | `FinanceCompHoldPropT` | 财务公司持股比例(%) | number(18,4) | ✓ | 0.8% |  |
| 115 | `ForeignInstHoldPropT` | 外资机构持股比例(%) | number(18,4) | ✓ | 20.82% |  |
| 116 | `QFIIHoldPropT` | #QFII持股比例(%) | number(18,4) | ✓ | 5.41% |  |
| 117 | `OtherInstiHoldPropT` | 其它机构持股比例(%) | number(18,4) | ✓ | 52.13% |  |
| 118 | `InstiHoldTNum` | 机构持股户数 | number(10) | ✓ | 99.22% |  |
| 119 | `FundsHoldingsTNum` | 公募基金持股户数 | number(10) | ✓ | 87.63% |  |
| 120 | `PrivFundHoldTNum` | 私募基金持股户数 | number(10) | ✓ | 6.33% |  |
| 121 | `SecuCorpsHoldTNum` | 券商持股户数 | number(10) | ✓ | 10.56% |  |
| 122 | `FinProductsHoldTNum` | 券商理财产品持股户数 | number(10) | ✓ | 2.42% |  |
| 123 | `BankHoldTNum` | 银行持股户数 | number(10) | ✓ | 0.78% |  |
| 124 | `InsurCorpsHoldTNum` | 保险公司持股户数 | number(10) | ✓ | 8.35% |  |
| 125 | `SocialSecuFundHoldTN` | 社保基金持股户数 | number(10) | ✓ | 9.82% |  |
| 126 | `EntAnnuitiesHoldTNum` | 企业年金持股户数 | number(10) | ✓ | 0.46% |  |
| 127 | `TrustCoHoldTNum` | 信托公司持股户数 | number(10) | ✓ | 9.31% |  |
| 128 | `FinanceCoHoldTNum` | 财务公司持股户数 | number(10) | ✓ | 0.8% |  |
| 129 | `ForeignInstHoldTNum` | 外资持股户数 | number(10) | ✓ | 20.82% |  |
| 130 | `QFIIHoldTNumber` | #QFII持股户数 | number(10) | ✓ | 5.41% |  |
| 131 | `OtherInstiHoldTNum` | 其他机构持股户数 | number(10) | ✓ | 52.16% |  |
| 132 | `Top10StockholdersAmount` | 前十大股东持股数量合计(股) | number(18,2) | ✓ | 52.47% |  |
| 133 | `Top10StockholdersProp` | 前十大股东持股比例合计(%) | number(18,4) | ✓ | 52.47% |  |
| 134 | `Top10NRStockholdersAmount` | 前十大无限售股东持股数量合计(股) | number(18,2) | ✓ | 52.24% |  |
| 135 | `Top10NRHoldersAmountToNRS` | 前十大无限售股东持股数占无限售股本比例(%) | number(18,4) | ✓ | 52.21% |  |
| 136 | `Top10NRHoldersAmountToTS` | 前十大无限售股东持股数占总股本的比例(%) | number(18,4) | ✓ | 52.24% |  |
| 137 | `NRAFromTop10NRHolders` | 前十大无限售股东持有无限售A股数量合计(股) | number(18,2) | ✓ | 51.97% |  |
| 138 | `NRAFromTop10ToNRA` | 前十大无限售股东持有无限售A股数占无限售A股比例(%) | number(18,4) | ✓ | 51.93% |  |
| 139 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 140 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 141 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InfoSource (信息来源)

信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“基金定报”时，数据源为上市公司定报及基金定报。

### FundsHoldings (公募基金持有无限售流通A股数量(股))

由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”的值暂时不计算，为空值

## SQL示例

```sql
-- 查询 股东持股统计 数据
SELECT *
FROM lc_stockholdingst
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
