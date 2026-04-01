# MF_AssetAllocationAll

**中文名**: 公募基金资产配置总表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AssetAllocationAll` |
| MySQL表名 | `mf_assetallocationall` |
| 中文名 | 公募基金资产配置总表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 日更新 |
| 字段数量 | 188 |
| 版本 | 1 |

## 表描述

1.内容说明：公募基金资产配置合表，较之MF_AssetAllocationNew，包含了公募基金子份额数据，以及QDII基金数据、美元份额数据等，该表适用于展示场景等。
2.信息来源：基金公司披露的定期报告
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✗ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ReportType` | 报告类型 | number(10) | ✗ | 100.0% | 报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `MVOfEquity` | 权益类投资资产市值(元) | number(19,4) | ✓ | 64.27% |  |
| 8 | `RIAOfEquity` | 权益类投资占资产总值比例 | number(18,6) | ✓ | 64.09% |  |
| 9 | `RINOfEquity` | 权益类投资占资产净值比例 | number(18,6) | ✓ | 64.2% |  |
| 10 | `MVOfFixedIncome` | 固定收益类投资资产市值(元) | number(19,4) | ✓ | 68.81% |  |
| 11 | `RIAOfFixedIncome` | 固定收益类投资占资产总值比例 | number(18,6) | ✓ | 68.79% |  |
| 12 | `RINOfFixedIncome` | 固定收益类投资占资产净值比例 | number(18,6) | ✓ | 68.81% |  |
| 13 | `MVOfFund` | 基金投资合计资产市值(元) | number(19,4) | ✓ | 7.55% |  |
| 14 | `RIAOfFund` | 基金投资合计占资产总值比例 | number(18,6) | ✓ | 7.55% |  |
| 15 | `RINOfFund` | 基金投资合计占资产净值比例 | number(18,6) | ✓ | 7.55% |  |
| 16 | `MVOfMetals` | 贵金属投资合计资产市值(元) | number(19,4) | ✓ | 0.15% |  |
| 17 | `RIAOfMetals` | 贵金属投资合计占资产总值比例 | number(18,6) | ✓ | 0.15% |  |
| 18 | `RINOfMetals` | 贵金属投资合计占资产净值比例 | number(18,6) | ✓ | 0.15% |  |
| 19 | `MVOfFixedDeriva` | 金融衍生品投资资产市值(元) | number(19,4) | ✓ | 0.53% |  |
| 20 | `RIAOfDeriva` | 金融衍生品投资占资产总值比例 | number(18,6) | ✓ | 0.53% |  |
| 21 | `RINOfDeriva` | 金融衍生品投资占资产净值比例 | number(18,6) | ✓ | 0.53% |  |
| 22 | `MVOfReturnSale` | 买入返售证券资产市值(元) | number(19,4) | ✓ | 24.96% |  |
| 23 | `RIAOfReturnSale` | 买入返售证券占资产总值比例 | number(18,6) | ✓ | 24.96% |  |
| 24 | `RINOfReturnSale` | 买入返售证券占资产净值比例 | number(18,6) | ✓ | 24.96% |  |
| 25 | `MVOfMonetary` | 货币资金资产市值(元) | number(19,4) | ✓ | 99.84% |  |
| 26 | `RIAOfMonetary` | 货币资金占资产总值比例 | number(18,6) | ✓ | 99.81% |  |
| 27 | `RINOfMonetary` | 货币资金占资产净值比例 | number(18,6) | ✓ | 99.77% |  |
| 28 | `MVOfOtherI` | 其他资产资产市值(元) | number(19,4) | ✓ | 97.17% |  |
| 29 | `RIAOfOtherI` | 其他资产占资产总值比例 | number(18,6) | ✓ | 97.0% |  |
| 30 | `RINOfOtherI` | 其他资产占资产净值比例 | number(18,6) | ✓ | 97.16% |  |
| 31 | `TotalAsset` | 资产总值 | number(19,4) | ✓ | 99.82% |  |
| 32 | `NV` | 资产净值 | number(19,4) | ✓ | 99.93% |  |
| 33 | `MVOfStock` | 股票投资合计资产市值(元) | number(19,4) | ✓ | 64.09% |  |
| 34 | `RIAOfStock` | 股票投资合计占资产总值比例 | number(18,6) | ✓ | 63.91% |  |
| 35 | `RINOfStock` | 股票投资合计占资产净值比例 | number(18,6) | ✓ | 64.09% |  |
| 36 | `MVOfPreferred` | 优先股资产市值(元) | number(19,4) | ✓ | 0.04% |  |
| 37 | `RIAOfPreferred` | 优先股占资产总值比例 | number(18,6) | ✓ | 0.04% |  |
| 38 | `RINOfPreferred` | 优先股占资产净值比例 | number(18,6) | ✓ | 0.04% |  |
| 39 | `MVOfReceipts` | 存托凭证资产市值(元) | number(19,4) | ✓ | 0.97% |  |
| 40 | `RIAOfReceipts` | 存托凭证占资产总值比例 | number(18,6) | ✓ | 0.97% |  |
| 41 | `RINOfReceipts` | 存托凭证占资产净值比例 | number(18,6) | ✓ | 0.97% |  |
| 42 | `MVOfRealEstate` | 房地产信托资产市值(元) | number(19,4) | ✓ | 0.21% |  |
| 43 | `RIAOfRealEstate` | 房地产信托占资产总值比例 | number(18,6) | ✓ | 0.21% |  |
| 44 | `RINOfRealEstate` | 房地产信托占资产净值比例 | number(18,6) | ✓ | 0.21% |  |
| 45 | `MVOfLongTermEquity` | 长期股权投资市值(元) | number(19,4) | ✓ | 0.11% |  |
| 46 | `RIAOfLongTermEquity` | 长期股权投资占资产总值比例 | number(18,6) | ✓ | 0.11% |  |
| 47 | `RINOfLongTermEquity` | 长期股权投资占资产净值比例 | number(18,6) | ✓ | 0.04% |  |
| 48 | `MVOfBond` | 债券投资合计资产市值(元) | number(19,4) | ✓ | 68.81% |  |
| 49 | `RIAOfBond` | 债券投资合计占资产总值比例 | number(18,6) | ✓ | 68.78% |  |
| 50 | `RINOfBond` | 债券投资合计占资产净值比例 | number(18,6) | ✓ | 68.81% |  |
| 51 | `MVOfAssetBacked` | 资产支持证券资产市值(元) | number(19,4) | ✓ | 6.05% |  |
| 52 | `RIAOfAssetBacked` | 资产支持证券占资产总值比例 | number(18,6) | ✓ | 6.05% |  |
| 53 | `RINOfAssetBacked` | 资产支持证券占资产净值比例 | number(18,6) | ✓ | 6.05% |  |
| 54 | `MVOfForward` | 其中:远期资产市值(元) | number(19,4) | ✓ | 0.05% |  |
| 55 | `RIAOfForward` | 其中:远期占资产总值比例 | number(18,6) | ✓ | 0.05% |  |
| 56 | `RINOfForward` | 其中:远期占资产净值比例 | number(18,6) | ✓ | 0.05% |  |
| 57 | `MVOfFuture` | 其中:期货资产市值(元) | number(19,4) | ✓ | 0.01% |  |
| 58 | `RIAOfFuture` | 其中:期货占资产总值比例 | number(18,6) | ✓ | 0.01% |  |
| 59 | `RINOfFuture` | 其中:期货占资产净值比例 | number(18,6) | ✓ | 0.01% |  |
| 60 | `MVOfOption` | 其中:期权资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 61 | `RIAOfOption` | 其中:期权占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 62 | `RINOfOption` | 其中:期权占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 63 | `MVOfWarrant` | 其中:权证资产市值(元) | number(19,4) | ✓ | 0.35% |  |
| 64 | `RIAOfWarrant` | 其中:权证占资产总值比例 | number(18,6) | ✓ | 0.35% |  |
| 65 | `RINOfWarrant` | 其中:权证占资产净值比例 | number(18,6) | ✓ | 0.35% |  |
| 66 | `MVOfSwap` | 其中:掉期资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 67 | `RIAOfSwap` | 其中:掉期占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 68 | `RINOfSwap` | 其中:掉期占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 69 | `MVOfBBReturnSale` | 其中:买断式回购买入返售证券资产市值(元) | number(19,4) | ✓ | 0.16% |  |
| 70 | `RIAOfBBReturnSale` | 其中:买断式回购买入返售证券占资产总值比例 | number(18,6) | ✓ | 0.16% |  |
| 71 | `RINOfBBReturnSale` | 其中:买断式回购买入返售证券占资产净值比例 | number(18,6) | ✓ | 0.16% |  |
| 72 | `MVOfMoney` | 货币市场工具资产市值(元) | number(19,4) | ✓ | 0.03% |  |
| 73 | `RIAOfMoney` | 货币市场工具占资产总值比例 | number(18,6) | ✓ | 0.03% |  |
| 74 | `RINOfMoney` | 货币市场工具占资产净值比例 | number(18,6) | ✓ | 0.03% |  |
| 75 | `MVOfBondsRepu` | 国债融券回购资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 76 | `RIAOfBondsRepu` | 国债融券回购占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 77 | `RINOfBondsRepu` | 国债融券回购占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 78 | `MVOfIndex` | 指数投资资产市值(元) | number(19,4) | ✓ | 8.42% |  |
| 79 | `RIAOfIndex` | 指数投资占资产总值比例 | number(18,6) | ✓ | 8.41% |  |
| 80 | `RINOfIndex` | 指数投资占资产净值比例 | number(18,6) | ✓ | 8.42% |  |
| 81 | `MVOfActive` | 积极投资资产市值(元) | number(19,4) | ✓ | 5.87% |  |
| 82 | `RIAOfActive` | 积极投资占资产总值比例 | number(18,6) | ✓ | 5.86% |  |
| 83 | `RINOfActive` | 积极投资占资产净值比例 | number(18,6) | ✓ | 5.87% |  |
| 84 | `MVOfDomestic` | 境内投资资产市值(元) | number(19,4) | ✓ | 61.76% |  |
| 85 | `RIAOfDomestic` | 境内投资占资产总值比例 | number(18,6) | ✓ | 61.58% |  |
| 86 | `RINOfDomestic` | 境内投资占资产净值比例 | number(18,6) | ✓ | 61.76% |  |
| 87 | `MVOfHKConnect` | 港股通投资资产市值(元) | number(19,4) | ✓ | 13.56% |  |
| 88 | `RIAOfHKConnect` | 港股通投资占资产总值比例 | number(18,6) | ✓ | 13.56% |  |
| 89 | `RINOfHKConnect` | 港股通投资占资产净值比例 | number(18,6) | ✓ | 13.56% |  |
| 90 | `MVOfTreasuries` | 国债资产市值(元) | number(19,4) | ✓ | 36.88% |  |
| 91 | `RIAOfTreasuries` | 国债占资产总值比例 | number(18,6) | ✓ | 36.86% |  |
| 92 | `RINOfTreasuries` | 国债占资产净值比例 | number(18,6) | ✓ | 36.88% |  |
| 93 | `MVOfNonGovBond` | 非国债债券资产市值(元) | number(19,4) | ✓ | 60.05% |  |
| 94 | `RIAOfNonGovBond` | 非国债债券占资产总值比例 | number(18,6) | ✓ | 59.94% |  |
| 95 | `RINOfNonGovBond` | 非国债债券占资产净值比例 | number(18,6) | ✓ | 60.05% |  |
| 96 | `MVOfCentralBank` | 央行票据资产市值(元) | number(19,4) | ✓ | 1.61% |  |
| 97 | `RIAOfCentralBank` | 央行票据占资产总值比例 | number(18,6) | ✓ | 1.61% |  |
| 98 | `RINOfCentralBank` | 央行票据占资产净值比例 | number(18,6) | ✓ | 1.61% |  |
| 99 | `MVOfFinancial` | 金融债券资产市值(元) | number(19,4) | ✓ | 47.17% |  |
| 100 | `RIAOfFinancial` | 金融债券占资产总值比例 | number(18,6) | ✓ | 47.16% |  |
| 101 | `RINOfFinancial` | 金融债券占资产净值比例 | number(18,6) | ✓ | 47.17% |  |
| 102 | `MVOfPolicyBond` | 其中:政策性金融债券资产市值(元) | number(19,4) | ✓ | 43.86% |  |
| 103 | `RIAOfPolicyBond` | 其中:政策性金融债券占资产总值比例 | number(18,6) | ✓ | 43.86% |  |
| 104 | `RINOfPolicyBond` | 其中:政策性金融债券占资产净值比例 | number(18,6) | ✓ | 43.86% |  |
| 105 | `MVOfCorporate` | 企业债券资产市值(元) | number(19,4) | ✓ | 29.45% |  |
| 106 | `RIAOfCorporate` | 企业债券占资产总值比例 | number(18,6) | ✓ | 29.44% |  |
| 107 | `RINOfCorporate` | 企业债券占资产净值比例 | number(18,6) | ✓ | 29.45% |  |
| 108 | `MVOfShortTerm` | 短期融资券资产市值(元) | number(19,4) | ✓ | 21.84% |  |
| 109 | `RIAOfShortTerm` | 短期融资券占资产总值比例 | number(18,6) | ✓ | 21.84% |  |
| 110 | `RINOfShortTerm` | 短期融资券占资产净值比例 | number(18,6) | ✓ | 21.84% |  |
| 111 | `MVOfMediumTerm` | 中期票据资产市值(元) | number(19,4) | ✓ | 26.08% |  |
| 112 | `RIAOfMediumTerm` | 中期票据占资产总值比例 | number(18,6) | ✓ | 26.08% |  |
| 113 | `RINOfMediumTerm` | 中期票据占资产净值比例 | number(18,6) | ✓ | 26.08% |  |
| 114 | `MVOfConvertible` | 可转换债券(含可交换债)资产市值(元) | number(19,4) | ✓ | 25.78% |  |
| 115 | `RIAOfConvertible` | 可转换债券(含可交换债)占资产总值比例 | number(18,6) | ✓ | 25.74% |  |
| 116 | `RINOfConvertible` | 可转换债券(含可交换债)占资产净值比例 | number(18,6) | ✓ | 25.78% |  |
| 117 | `MVOfMinorEnterp` | 中小企业私募债资产市值(元) | number(19,4) | ✓ | 0.01% |  |
| 118 | `RIAOfMinorEnterp` | 中小企业私募债占资产总值比例 | number(18,6) | ✓ | 0.01% |  |
| 119 | `RINOfMinorEnterp` | 中小企业私募债占资产净值比例 | number(18,6) | ✓ | 0.01% |  |
| 120 | `MVOfNCDs` | 同业存单资产市值(元) | number(19,4) | ✓ | 14.52% |  |
| 121 | `RIAOfNCDs` | 同业存单占资产总值比例 | number(18,6) | ✓ | 14.52% |  |
| 122 | `RINOfNCDs` | 同业存单占资产净值比例 | number(18,6) | ✓ | 14.52% |  |
| 123 | `MVOfLocalGov` | 地方政府债券资产市值(元) | number(19,4) | ✓ | 0.41% |  |
| 124 | `RIAOfLocalGov` | 地方政府债券占资产总值比例 | number(18,6) | ✓ | 0.41% |  |
| 125 | `RINOfLocalGov` | 地方政府债券占资产净值比例 | number(18,6) | ✓ | 0.41% |  |
| 126 | `MVOfCorporateII` | 公司债资产市值(元) | number(19,4) | ✓ | 0.04% |  |
| 127 | `RIAOfCorporateII` | 公司债占资产总值比例 | number(18,6) | ✓ | 0.04% |  |
| 128 | `RINOfCorporateII` | 公司债占资产净值比例 | number(18,6) | ✓ | 0.04% |  |
| 129 | `MVOfOtherBonds` | 其他债券资产市值(元) | number(19,4) | ✓ | 3.38% |  |
| 130 | `RIAOfOtherBonds` | 其他债券占资产总值比例 | number(18,6) | ✓ | 3.38% |  |
| 131 | `RINOfOtherBonds` | 其他债券占资产净值比例 | number(18,6) | ✓ | 3.38% |  |
| 132 | `MVOfBondRepoI` | 期内债券回购融资余额资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 133 | `RIAOfBondRepoI` | 期内债券回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 134 | `RINOfBondRepoI` | 期内债券回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 135 | `MVOfBuybackI` | 其中:期内买断式回购融资余额资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 136 | `RIAOfBuybackI` | 其中:期内买断式回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 137 | `RINOfBuybackI` | 其中:期内买断式回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 138 | `MVOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)资产市值(元) | number(19,4) | ✓ | 4.49% |  |
| 139 | `RIAOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)占资产总值比例 | number(18,6) | ✓ | 4.49% |  |
| 140 | `RINOfBondRepoII` | 期末债券回购融资余额(卖出回购证券)占资产净值比例 | number(18,6) | ✓ | 4.49% |  |
| 141 | `MVOfBuybackII` | 其中:期末买断式回购融资余额资产市值(元) | number(19,4) | ✓ | 0.05% |  |
| 142 | `RIAOfBuybackII` | 其中:期末买断式回购融资余额占资产总值比例 | number(18,6) | ✓ | 0.05% |  |
| 143 | `RINOfBuybackII` | 其中:期末买断式回购融资余额占资产净值比例 | number(18,6) | ✓ | 0.05% |  |
| 144 | `MVOfFloRateBond` | 剩余存续期超过397天的浮动利率债券资产市值(元) | number(19,4) | ✓ | 1.02% |  |
| 145 | `RIAOfFloRateBond` | 剩余存续期超过397天的浮动利率债券占资产总值比例 | number(18,6) | ✓ | 1.02% |  |
| 146 | `RINOfFloRateBond` | 剩余存续期超过397天的浮动利率债券占资产净值比例 | number(18,6) | ✓ | 1.02% |  |
| 147 | `MVOfReceiCredit` | 其他应收应付款贷方资产市值(元) | number(19,4) | ✓ | 0.1% |  |
| 148 | `RIAOfReceiCredit` | 其他应收应付款贷方占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 149 | `RINOfReceiCredit` | 其他应收应付款贷方占资产净值比例 | number(18,6) | ✓ | 0.1% |  |
| 150 | `MVOfReceiDebit` | 其他应收应付款借方资产市值(元) | number(19,4) | ✓ | 0.07% |  |
| 151 | `RIAOfReceiDebit` | 其他应收应付款借方占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 152 | `RINOfReceiDebit` | 其他应收应付款借方占资产净值比例 | number(18,6) | ✓ | 0.07% |  |
| 153 | `MVOfMargin` | 交易保证金资产市值(元) | number(19,4) | ✓ | 80.56% |  |
| 154 | `RIAOfMargin` | 交易保证金占资产总值比例 | number(18,6) | ✓ | 80.56% |  |
| 155 | `RINOfMargin` | 交易保证金占资产净值比例 | number(18,6) | ✓ | 80.56% |  |
| 156 | `MVOfDividend` | 应收股利资产市值(元) | number(19,4) | ✓ | 8.21% |  |
| 157 | `RIAOfDividend` | 应收股利占资产总值比例 | number(18,6) | ✓ | 8.21% |  |
| 158 | `RINOfDividend` | 应收股利占资产净值比例 | number(18,6) | ✓ | 8.21% |  |
| 159 | `MVOfInterest` | 应收利息资产市值(元) | number(19,4) | ✓ | 44.78% |  |
| 160 | `RIAOfInterest` | 应收利息占资产总值比例 | number(18,6) | ✓ | 44.78% |  |
| 161 | `RINOfInterest` | 应收利息占资产净值比例 | number(18,6) | ✓ | 44.77% |  |
| 162 | `MVOfReceivables` | 应收帐款资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 163 | `RIAOfReceivables` | 应收帐款占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 164 | `RINOfReceivables` | 应收帐款占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 165 | `MVOfPurchase` | 应收申购款资产市值(元) | number(19,4) | ✓ | 72.27% |  |
| 166 | `RIAOfPurchase` | 应收申购款占资产总值比例 | number(18,6) | ✓ | 72.27% |  |
| 167 | `RINOfPurchase` | 应收申购款占资产净值比例 | number(18,6) | ✓ | 72.27% |  |
| 168 | `MVOfLiquidation` | 应收证券清算款资产市值(元) | number(19,4) | ✓ | 43.58% |  |
| 169 | `RIAOfLiquidation` | 应收证券清算款占资产总值比例 | number(18,6) | ✓ | 43.58% |  |
| 170 | `RINOfLiquidation` | 应收证券清算款占资产净值比例 | number(18,6) | ✓ | 43.58% |  |
| 171 | `MVOfOtherReceiv` | 其他应收款资产市值(元) | number(19,4) | ✓ | 4.18% |  |
| 172 | `RIAOfOtherReceiv` | 其他应收款占资产总值比例 | number(18,6) | ✓ | 4.18% |  |
| 173 | `RINOfOtherReceiv` | 其他应收款占资产净值比例 | number(18,6) | ✓ | 4.18% |  |
| 174 | `MVOfShareWarrant` | 配股权证资产市值(元) | number(19,4) | ✓ | 0.0% |  |
| 175 | `RIAOfShareWarrant` | 配股权证占资产总值比例 | number(18,6) | ✓ | 0.0% |  |
| 176 | `RINOfShareWarrant` | 配股权证占资产净值比例 | number(18,6) | ✓ | 0.0% |  |
| 177 | `MVOfApportCost` | 待摊费用资产市值(元) | number(19,4) | ✓ | 1.57% |  |
| 178 | `RIAOfApportCost` | 待摊费用占资产总值比例 | number(18,6) | ✓ | 1.57% |  |
| 179 | `RINOfApportCost` | 待摊费用占资产净值比例 | number(18,6) | ✓ | 1.57% |  |
| 180 | `MVOfOtherII` | 其他资产-其他资产市值(元) | number(19,4) | ✓ | 0.7% |  |
| 181 | `RIAOfOtherII` | 其他资产-其他占资产总值比例 | number(18,6) | ✓ | 0.7% |  |
| 182 | `RINOfOtherII` | 其他资产-其他占资产净值比例 | number(18,6) | ✓ | 0.69% |  |
| 183 | `MVOfOther` | 其他配置资产市值(元) | number(19,4) | ✓ | 0.08% |  |
| 184 | `RIAOfOther` | 其他配置占资产总值比例 | number(18,6) | ✓ | 0.08% |  |
| 185 | `RINOfOther` | 其他配置占资产净值比例 | number(18,6) | ✓ | 0.08% |  |
| 186 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 187 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 188 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportType (报告类型)

报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN(5,6,17,20,23,61,63,143)，得到报告类型的具体描述：5-年度报告，6-中期报告，17-第一季度报告，20-基金上市公告书，23-第三季度报告，61-第二季度报告，63-第四季度报告，143-月度报告。

## SQL示例

```sql
-- 查询 公募基金资产配置总表 数据
SELECT *
FROM mf_assetallocationall
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
