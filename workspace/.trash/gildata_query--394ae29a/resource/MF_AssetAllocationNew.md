# MF_AssetAllocationNew

**中文名**: 公募基金资产配置(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AssetAllocationNew` |
| MySQL表名 | `mf_assetallocationnew` |
| 中文名 | 公募基金资产配置(新) |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 不定时 |
| 字段数量 | 199 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金资产的大类配置情况，包括股票、债券、银行存款和清算备付金、其他资产、买入返售证券、卖出回购证券、国债及货币资金、可转换债券等。
2.历史数据：1998年6月起-至今。
3.数据来源：基金公司披露的上市交易公告书、定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `NV` | 资产净值 | number(19,4) | ✓ | 99.91% |  |
| 7 | `TotalAsset` | 资产总值 | number(19,4) | ✓ | 99.7% |  |
| 8 | `MVOfEquity` | 权益类投资资产市值(元) | number(19,4) | ✓ | 67.25% |  |
| 9 | `RIAOfEquity` | 权益类投资占资产总值比例 | number(18,6) | ✓ | 66.95% |  |
| 10 | `RINOfEquity` | 权益类投资占资产净值比例 | number(18,6) | ✓ | 67.16% |  |
| 11 | `RIAOfStock` | 股票投资合计占资产总值比例 | number(18,6) | ✓ | 66.76% |  |
| 12 | `MVOfStock` | 股票投资合计资产市值(元) | number(19,4) | ✓ | 67.06% |  |
| 13 | `RINOfStock` | 股票投资合计占资产净值比例 | number(18,6) | ✓ | 67.06% |  |
| 14 | `MVOfPreferred` | 优先股资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 15 | `RIAOfPreferred` | 优先股占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 16 | `RINOfPreferred` | 优先股占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 17 | `MVOfReceipts` | 存托凭证资产市值(元) | number(19,4) | ✓ | 0.05% |  |
| 18 | `RIAOfReceipts` | 存托凭证占资产总值比例 | number(18,6) | ✓ | 0.05% |  |
| 19 | `RINOfReceipts` | 存托凭证占资产净值比例 | number(18,6) | ✓ | 0.05% |  |
| 20 | `MVOfRealEstate` | 房地产信托资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 21 | `RIAOfRealEstate` | 房地产信托占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 22 | `RINOfRealEstate` | 房地产信托占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 23 | `MVOfLongTermEquity` | 长期股权投资市值(元) | number(19,4) | ✓ | 0.19% |  |
| 24 | `RIAOfLongTermEquity` | 长期股权投资占资产总值比例 | number(18,6) | ✓ | 0.19% |  |
| 25 | `RINOfLongTermEquity` | 长期股权投资占资产净值比例 | number(18,6) | ✓ | 0.1% |  |
| 26 | `MVOfFixedIncome` | 固定收益类投资资产市值(元) | number(19,4) | ✓ | 67.75% |  |
| 27 | `RIAOfFixedIncome` | 固定收益类投资占资产总值比例 | number(18,6) | ✓ | 67.71% |  |
| 28 | `RINOfFixedIncome` | 固定收益类投资占资产净值比例 | number(18,6) | ✓ | 67.75% |  |
| 29 | `MVOfBond` | 债券投资合计资产市值(元) | number(19,4) | ✓ | 67.75% |  |
| 30 | `RIAOfBond` | 债券投资合计占资产总值比例 | number(18,6) | ✓ | 67.7% |  |
| 31 | `RINOfBond` | 债券投资合计占资产净值比例 | number(18,6) | ✓ | 67.75% |  |
| 32 | `MVOfAssetBacked` | 资产支持证券资产市值(元) | number(19,4) | ✓ | 5.65% |  |
| 33 | `RIAOfAssetBacked` | 资产支持证券占资产总值比例 | number(18,6) | ✓ | 5.65% |  |
| 34 | `RINOfAssetBacked` | 资产支持证券占资产净值比例 | number(18,6) | ✓ | 5.65% |  |
| 35 | `MVOfFund` | 基金投资合计资产市值(元) | number(19,4) | ✓ | 5.73% |  |
| 36 | `RIAOfFund` | 基金投资合计占资产总值比例 | number(18,6) | ✓ | 5.73% |  |
| 37 | `RINOfFund` | 基金投资合计占资产净值比例 | number(18,6) | ✓ | 5.73% |  |
| 38 | `MVOfFixedDeriva` | 金融衍生品投资资产市值(元) | number(19,4) | ✓ | 0.61% |  |
| 39 | `RIAOfDeriva` | 金融衍生品投资占资产总值比例 | number(18,6) | ✓ | 0.61% |  |
| 40 | `RINOfDeriva` | 金融衍生品投资占资产净值比例 | number(18,6) | ✓ | 0.61% |  |
| 41 | `MVOfForward` | 其中:远期资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 42 | `RIAOfForward` | 其中:远期占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 43 | `RINOfForward` | 其中:远期占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 44 | `MVOfFuture` | 其中:期货资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 45 | `RIAOfFuture` | 其中:期货占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 46 | `RINOfFuture` | 其中:期货占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 47 | `MVOfOption` | 其中:期权资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 48 | `RIAOfOption` | 其中:期权占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 49 | `RINOfOption` | 其中:期权占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 50 | `MVOfSwap` | 其中:掉期资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 51 | `RIAOfSwap` | 其中:掉期占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 52 | `RINOfSwap` | 其中:掉期占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 53 | `MVOfWarrant` | 其中:权证资产市值(元) | number(19,4) | ✓ | 0.48% |  |
| 54 | `RIAOfWarrant` | 其中:权证占资产总值比例 | number(18,6) | ✓ | 0.48% |  |
| 55 | `RINOfWarrant` | 其中:权证占资产净值比例 | number(18,6) | ✓ | 0.48% |  |
| 56 | `MVOfMetals` | 贵金属投资合计资产市值(元) | number(19,4) | ✓ | 0.17% |  |
| 57 | `RIAOfMetals` | 贵金属投资合计占资产总值比例 | number(18,6) | ✓ | 0.17% |  |
| 58 | `RINOfMetals` | 贵金属投资合计占资产净值比例 | number(18,6) | ✓ | 0.17% |  |
| 59 | `MVOfBuyback` | 买入返售金融资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 60 | `RIAOfBuyback` | 买入返售金融资产占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 61 | `RINOfBuyback` | 买入返售金融资产占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 62 | `MVOfBuyBackRepo` | 其中:买断式回购的买入返售金融资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 63 | `RIAOfBuyBackRepo` | 其中:买断式回购的买入返售资产占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 64 | `RINOfBuyBackRepo` | 其中:买断式回购的买入返售金融占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 65 | `MVOfReturnSale` | 买入返售证券资产市值(元) | number(19,4) | ✓ | 23.87% |  |
| 66 | `RIAOfReturnSale` | 买入返售证券占资产总值比例 | number(18,6) | ✓ | 23.87% |  |
| 67 | `RINOfReturnSale` | 买入返售证券占资产净值比例 | number(18,6) | ✓ | 23.87% |  |
| 68 | `MVOfBBReturnSale` | 其中:买断式回购买入返售证券资产市值(元) | number(19,4) | ✓ | 0.14% |  |
| 69 | `RIAOfBBReturnSale` | 其中:买断式回购买入返售证券占资产总值比例 | number(18,6) | ✓ | 0.14% |  |
| 70 | `RINOfBBReturnSale` | 其中:买断式回购买入返售证券占资产净值比例 | number(18,6) | ✓ | 0.14% |  |
| 71 | `MVOfBondsRepu` | 国债融券回购资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 72 | `RIAOfBondsRepu` | 国债融券回购占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 73 | `RINOfBondsRepu` | 国债融券回购占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 74 | `MVOfMoney` | 货币市场工具资产市值(元) | number(19,4) | ✓ | 0.0% | 货币市场工具资产市值(元)(MVOfMoney)：对境内基金来说，本字段和下方【货币资金资产市值(元)(MVOfMone... |
| 75 | `RIAOfMoney` | 货币市场工具占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 76 | `RINOfMoney` | 货币市场工具占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 77 | `MVOfBankSaving` | 银行存款和清算备付金合计资产市值(元) | number(19,4) | ✓ | 0.0% | 银行存款和清算备付金合计资产市值(元)(MVOfBankSaving)：本科目维护在【货币资金资产市值(元)MVOfMo... |
| 78 | `RIAOfBankSaving` | 银行存款和清算备付金合计占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 79 | `RINOfBankSaving` | 银行存款和清算备付金合计占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 80 | `MVOfOtherI` | 其他资产资产市值(元) | number(19,4) | ✓ | 96.66% |  |
| 81 | `RIAOfOtherI` | 其他资产占资产总值比例 | number(18,6) | ✓ | 96.37% |  |
| 82 | `RINOfOtherI` | 其他资产占资产净值比例 | number(18,6) | ✓ | 96.65% |  |
| 83 | `MVOfIndex` | 指数投资资产市值(元) | number(19,4) | ✓ | 8.69% |  |
| 84 | `RIAOfIndex` | 指数投资占资产总值比例 | number(18,6) | ✓ | 8.67% |  |
| 85 | `RINOfIndex` | 指数投资占资产净值比例 | number(18,6) | ✓ | 8.69% |  |
| 86 | `MVOfActive` | 积极投资资产市值(元) | number(19,4) | ✓ | 6.08% |  |
| 87 | `RIAOfActive` | 积极投资占资产总值比例 | number(18,6) | ✓ | 6.06% |  |
| 88 | `RINOfActive` | 积极投资占资产净值比例 | number(18,6) | ✓ | 6.08% |  |
| 89 | `MVOfDomestic` | 境内投资资产市值(元) | number(19,4) | ✓ | 66.4% |  |
| 90 | `RIAOfDomestic` | 境内投资占资产总值比例 | number(18,6) | ✓ | 66.11% |  |
| 91 | `RINOfDomestic` | 境内投资占资产净值比例 | number(18,6) | ✓ | 66.4% |  |
| 92 | `MVOfHKConnect` | 港股通投资资产市值(元) | number(19,4) | ✓ | 12.36% |  |
| 93 | `RIAOfHKConnect` | 港股通投资占资产总值比例 | number(18,6) | ✓ | 12.36% |  |
| 94 | `RINOfHKConnect` | 港股通投资占资产净值比例 | number(18,6) | ✓ | 12.36% |  |
| 95 | `MVOfNational` | 国债及货币资金资产市值(元) | number(19,4) | ✓ | 100.0% |  |
| 96 | `RIAOfNational` | 国债及货币资金占资产总值比例 | number(18,6) | ✓ | 99.7% |  |
| 97 | `RINOfNational` | 国债及货币资金占资产净值比例 | number(18,6) | ✓ | 99.91% |  |
| 98 | `MVOfTreasuries` | 国债资产市值(元) | number(19,4) | ✓ | 34.86% |  |
| 99 | `RIAOfTreasuries` | 国债占资产总值比例 | number(18,6) | ✓ | 34.81% |  |
| 100 | `RINOfTreasuries` | 国债占资产净值比例 | number(18,6) | ✓ | 34.86% |  |
| 101 | `MVOfMonetary` | 货币资金资产市值(元) | number(19,4) | ✓ | 99.75% |  |
| 102 | `RIAOfMonetary` | 货币资金占资产总值比例 | number(18,6) | ✓ | 99.69% |  |
| 103 | `RINOfMonetary` | 货币资金占资产净值比例 | number(18,6) | ✓ | 99.66% |  |
| 104 | `MVOfNonGovBond` | 非国债债券资产市值(元) | number(19,4) | ✓ | 60.19% |  |
| 105 | `RIAOfNonGovBond` | 非国债债券占资产总值比例 | number(18,6) | ✓ | 60.0% |  |
| 106 | `RINOfNonGovBond` | 非国债债券占资产净值比例 | number(18,6) | ✓ | 60.19% |  |
| 107 | `MVOfCentralBank` | 央行票据资产市值(元) | number(19,4) | ✓ | 2.25% |  |
| 108 | `RIAOfCentralBank` | 央行票据占资产总值比例 | number(18,6) | ✓ | 2.25% |  |
| 109 | `RINOfCentralBank` | 央行票据占资产净值比例 | number(18,6) | ✓ | 2.25% |  |
| 110 | `MVOfFinancial` | 金融债券资产市值(元) | number(19,4) | ✓ | 46.2% |  |
| 111 | `RIAOfFinancial` | 金融债券占资产总值比例 | number(18,6) | ✓ | 46.18% |  |
| 112 | `RINOfFinancial` | 金融债券占资产净值比例 | number(18,6) | ✓ | 46.2% |  |
| 113 | `MVOfPolicyBond` | 其中:政策性金融债券资产市值(元) | number(19,4) | ✓ | 42.73% |  |
| 114 | `RIAOfPolicyBond` | 其中:政策性金融债券占资产总值比例 | number(18,6) | ✓ | 42.73% |  |
| 115 | `RINOfPolicyBond` | 其中:政策性金融债券占资产净值比例 | number(18,6) | ✓ | 42.73% |  |
| 116 | `MVOfCorporate` | 企业债券资产市值(元) | number(19,4) | ✓ | 28.45% |  |
| 117 | `RIAOfCorporate` | 企业债券占资产总值比例 | number(18,6) | ✓ | 28.44% |  |
| 118 | `RINOfCorporate` | 企业债券占资产净值比例 | number(18,6) | ✓ | 28.45% |  |
| 119 | `MVOfShortTerm` | 短期融资券资产市值(元) | number(19,4) | ✓ | 19.84% |  |
| 120 | `RIAOfShortTerm` | 短期融资券占资产总值比例 | number(18,6) | ✓ | 19.84% |  |
| 121 | `RINOfShortTerm` | 短期融资券占资产净值比例 | number(18,6) | ✓ | 19.84% |  |
| 122 | `MVOfMediumTerm` | 中期票据资产市值(元) | number(19,4) | ✓ | 24.33% |  |
| 123 | `RIAOfMediumTerm` | 中期票据占资产总值比例 | number(18,6) | ✓ | 24.33% |  |
| 124 | `RINOfMediumTerm` | 中期票据占资产净值比例 | number(18,6) | ✓ | 24.33% |  |
| 125 | `MVOfConvertible` | 可转换债券(含可交换债)资产市值(元) | number(19,4) | ✓ | 26.29% |  |
| 126 | `RIAOfConvertible` | 可转换债券(含可交换债)占资产总值比例 | number(18,6) | ✓ | 26.23% |  |
| 127 | `RINOfConvertible` | 可转换债券(含可交换债)占资产净值比例 | number(18,6) | ✓ | 26.29% |  |
| 128 | `MVOfMinorEnterp` | 中小企业私募债资产市值(元) | number(19,4) | ✓ | 0.01% |  |
| 129 | `RIAOfMinorEnterp` | 中小企业私募债占资产总值比例 | number(18,6) | ✓ | 0.01% |  |
| 130 | `RINOfMinorEnterp` | 中小企业私募债占资产净值比例 | number(18,6) | ✓ | 0.01% |  |
| 131 | `MVOfNCDs` | 同业存单资产市值(元) | number(19,4) | ✓ | 13.21% |  |
| 132 | `RIAOfNCDs` | 同业存单占资产总值比例 | number(18,6) | ✓ | 13.21% |  |
| 133 | `RINOfNCDs` | 同业存单占资产净值比例 | number(18,6) | ✓ | 13.21% |  |
| 134 | `MVOfLocalGov` | 地方政府债券资产市值(元) | number(19,4) | ✓ | 0.38% |  |
| 135 | `RIAOfLocalGov` | 地方政府债券占资产总值比例 | number(18,6) | ✓ | 0.38% |  |
| 136 | `RINOfLocalGov` | 地方政府债券占资产净值比例 | number(18,6) | ✓ | 0.38% |  |
| 137 | `MVOfCorporateII` | 公司债资产市值(元) | number(19,4) | ✓ | 0.04% |  |
| 138 | `RIAOfCorporateII` | 公司债占资产总值比例 | number(18,6) | ✓ | 0.04% |  |
| 139 | `RINOfCorporateII` | 公司债占资产净值比例 | number(18,6) | ✓ | 0.04% |  |
| 140 | `MVOfOtherBonds` | 其他债券资产市值(元) | number(19,4) | ✓ | 3.25% |  |
| 141 | `RIAOfOtherBonds` | 其他债券占资产总值比例 | number(18,6) | ✓ | 3.25% |  |
| 142 | `RINOfOtherBonds` | 其他债券占资产净值比例 | number(18,6) | ✓ | 3.25% |  |
| 143 | `MVOfReceiCredit` | 其他应收应付款贷方资产市值(元) | number(19,4) | ✓ | 0.16% |  |
| 144 | `RIAOfReceiCredit` | 其他应收应付款贷方占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 145 | `RINOfReceiCredit` | 其他应收应付款贷方占资产净值比例 | number(18,6) | ✓ | 0.16% |  |
| 146 | `MVOfReceiDebit` | 其他应收应付款借方资产市值(元) | number(19,4) | ✓ | 0.13% |  |
| 147 | `RIAOfReceiDebit` | 其他应收应付款借方占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 148 | `RINOfReceiDebit` | 其他应收应付款借方占资产净值比例 | number(18,6) | ✓ | 0.13% |  |
| 149 | `MVOfMargin` | 交易保证金资产市值(元) | number(19,4) | ✓ | 83.76% |  |
| 150 | `RIAOfMargin` | 交易保证金占资产总值比例 | number(18,6) | ✓ | 83.76% |  |
| 151 | `RINOfMargin` | 交易保证金占资产净值比例 | number(18,6) | ✓ | 83.76% |  |
| 152 | `MVOfLiquidation` | 应收证券清算款资产市值(元) | number(19,4) | ✓ | 45.41% |  |
| 153 | `RIAOfLiquidation` | 应收证券清算款占资产总值比例 | number(18,6) | ✓ | 45.41% |  |
| 154 | `RINOfLiquidation` | 应收证券清算款占资产净值比例 | number(18,6) | ✓ | 45.41% |  |
| 155 | `MVOfDividend` | 应收股利资产市值(元) | number(19,4) | ✓ | 8.06% |  |
| 156 | `RIAOfDividend` | 应收股利占资产总值比例 | number(18,6) | ✓ | 8.06% |  |
| 157 | `RINOfDividend` | 应收股利占资产净值比例 | number(18,6) | ✓ | 8.06% |  |
| 158 | `MVOfInterest` | 应收利息资产市值(元) | number(19,4) | ✓ | 49.88% |  |
| 159 | `RIAOfInterest` | 应收利息占资产总值比例 | number(18,6) | ✓ | 49.88% |  |
| 160 | `RINOfInterest` | 应收利息占资产净值比例 | number(18,6) | ✓ | 49.88% |  |
| 161 | `MVOfPurchase` | 应收申购款资产市值(元) | number(19,4) | ✓ | 70.39% |  |
| 162 | `RIAOfPurchase` | 应收申购款占资产总值比例 | number(18,6) | ✓ | 70.39% |  |
| 163 | `RINOfPurchase` | 应收申购款占资产净值比例 | number(18,6) | ✓ | 70.39% |  |
| 164 | `MVOfReceivables` | 应收帐款资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 165 | `RIAOfReceivables` | 应收帐款占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 166 | `RINOfReceivables` | 应收帐款占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 167 | `MVOfOtherReceiv` | 其他应收款资产市值(元) | number(19,4) | ✓ | 4.51% |  |
| 168 | `RIAOfOtherReceiv` | 其他应收款占资产总值比例 | number(18,6) | ✓ | 4.51% |  |
| 169 | `RINOfOtherReceiv` | 其他应收款占资产净值比例 | number(18,6) | ✓ | 4.51% |  |
| 170 | `MVOfApportCost` | 待摊费用资产市值(元) | number(19,4) | ✓ | 2.34% |  |
| 171 | `RIAOfApportCost` | 待摊费用占资产总值比例 | number(18,6) | ✓ | 2.34% |  |
| 172 | `RINOfApportCost` | 待摊费用占资产净值比例 | number(18,6) | ✓ | 2.34% |  |
| 173 | `MVOfShareWarrant` | 配股权证资产市值(元) | number(19,4) | ✓ | 0.01% |  |
| 174 | `RIAOfShareWarrant` | 配股权证占资产总值比例 | number(18,6) | ✓ | 0.01% |  |
| 175 | `RINOfShareWarrant` | 配股权证占资产净值比例 | number(18,6) | ✓ | 0.01% |  |
| 176 | `MVOfOtherII` | 其他资产-其他资产市值(元) | number(19,4) | ✓ | 0.75% |  |
| 177 | `RIAOfOtherII` | 其他资产-其他占资产总值比例 | number(18,6) | ✓ | 0.75% |  |
| 178 | `RINOfOtherII` | 其他资产-其他占资产净值比例 | number(18,6) | ✓ | 0.74% |  |
| 179 | `MVOfOther` | 其他配置资产市值(元) | number(19,4) | ✓ | 0.12% |  |
| 180 | `RIAOfOther` | 其他配置占资产总值比例 | number(18,6) | ✓ | 0.12% |  |
| 181 | `RINOfOther` | 其他配置占资产净值比例 | number(18,6) | ✓ | 0.12% |  |
| 182 | `MVOfBondRepoI` | 期内债券回购融资余额资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 183 | `RIAOfBondRepoI` | 期内债券回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 184 | `RINOfBondRepoI` | 期内债券回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 185 | `MVOfBuybackI` | 其中:期内买断式回购融资余额资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 186 | `RIAOfBuybackI` | 其中:期内买断式回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 187 | `RINOfBuybackI` | 其中:期内买断式回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 188 | `MVOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)资产市值(元) | number(19,4) | ✓ | 3.46% |  |
| 189 | `RIAOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)占资产总值比例 | number(18,6) | ✓ | 3.46% |  |
| 190 | `RINOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)占资产净值比例 | number(18,6) | ✓ | 3.46% |  |
| 191 | `MVOfBuybackII` | 其中:期末买断式回购融资余额资产市值(元) | number(19,4) | ✓ | 0.05% |  |
| 192 | `RIAOfBuybackII` | 其中:期末买断式回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.05% |  |
| 193 | `RINOfBuybackII` | 其中:期末买断式回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.05% |  |
| 194 | `MVOfFloRateBond` | 剩余存续期超过397天的浮动利率债券资产市值(元) | number(19,4) | ✓ | 0.86% |  |
| 195 | `RIAOfFloRateBond` | 剩余存续期超过397天的浮动利率债券占资产总值比例 | number(18,6) | ✓ | 0.86% |  |
| 196 | `RINOfFloRateBond` | 剩余存续期超过397天的浮动利率债券占资产净值比例 | number(18,6) | ✓ | 0.86% |  |
| 197 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 198 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 199 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### MVOfMoney (货币市场工具资产市值(元))

货币市场工具资产市值(元)(MVOfMoney)：对境内基金来说，本字段和下方【货币资金资产市值(元)(MVOfMonetary)】同义，记录常规基金定报中披露的银行存款和结算备付金，本字段无值，使用MVOfMonetary即可

### MVOfBankSaving (银行存款和清算备付金合计资产市值(元))

银行存款和清算备付金合计资产市值(元)(MVOfBankSaving)：本科目维护在【货币资金资产市值(元)MVOfMonetary】

## SQL示例

```sql
-- 查询 公募基金资产配置(新) 数据
SELECT *
FROM mf_assetallocationnew
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
