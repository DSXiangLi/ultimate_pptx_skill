# HK_FundArchives

**中文名**: 香港基金概况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundArchives` |
| MySQL表名 | `hk_fundarchives` |
| 中文名 | 香港基金概况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 41 |
| 版本 | 1.05 |

## 表描述

1.本表收录港交所ETF、杠杆及反向产品的基础信息，包含参与主体，相关日期，基金类别、投资策略、投资目标等信息。
2.历史数据：1999年11月起--至今。
3.数据来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `MainFundCode` | 主基金代码 | number(10) | ✗ | 100.0% | 主基金代码(MainFundCode):与“港股证券主表(HK_SecuMain)”中的“证券内部编码(InnerCod... |
| 4 | `FundName` | 基金名称 | varchar2(200) | ✓ | 100.0% |  |
| 5 | `FundNameAbbr` | 基金简称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `InvestAdvisorCode` | 基金管理人 | number(10) | ✓ | 100.0% | 基金管理人（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutline）... |
| 7 | `TrusteeCode` | 基金托管人 | number(10) | ✓ | 77.66% | 基金托管人（TrusteeCode）：与“基金托管人概况表（MF_TrusteeOutline）”中的“基金托管人名称编... |
| 8 | `InitialIssueStartDate` | 首次发售起始日 | date | ✓ | 82.66% |  |
| 9 | `InitialIssueEndDate` | 首次发售截止日 | date | ✓ | 59.84% |  |
| 10 | `DividendPayableMonth` | 派息月份 | number(10) | ✓ |  |  |
| 11 | `EstablishmentDate` | 成立日期 | date | ✓ | 37.5% |  |
| 12 | `ListedDate` | 上市日期 | date | ✓ | 100.0% |  |
| 13 | `ListedType` | 上市方式 | number(10) | ✓ | 97.97% | 上市方式(ListedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1796，得到上市方式... |
| 14 | `FundType` | 基金类别 | number(10) | ✓ | 98.13% | 基金类别(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1797，得到基金类别的具... |
| 15 | `RegCountry` | 注册国家或地区 | number(10) | ✓ | 76.41% | 注册国家或地区(RegCountry)与(CT_SystemConst)表中的DM字段关联，令LB = 1005，得到注... |
| 16 | `IfStampDuty` | 是否缴纳印花税 | number(10) | ✓ | 93.28% | 是否缴纳印花税(IfStampDuty)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND... |
| 17 | `IfStockOption` | 是否纳入股票期权 | number(10) | ✓ | 98.13% | 是否纳入股票期权(IfStockOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 ... |
| 18 | `IfStockFuture` | 是否纳入股票期货 | number(10) | ✓ | 98.13% | 是否纳入股票期货(IfStockFuture)与(CT_SystemConst)表中的DM字段关联，令LB = 999 ... |
| 19 | `TotalFeeRatio` | 总费用比率(%) | number(19,8) | ✓ | 96.41% |  |
| 20 | `FeeDescription` | 费用说明 | clob | ✓ | 56.09% |  |
| 21 | `BaseCurrency` | 基础货币 | number(10) | ✓ | 100.0% | 基础货币(BaseCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得到基础... |
| 22 | `TradingCurrency` | 交易货币 | number(10) | ✓ | 100.0% | 交易货币(TradingCurrency)与(CT_SystemConst)表中的DM字段关联，令LB = 1068，得... |
| 23 | `PerTradeSize` | 每手买卖单位(份) | number(10) | ✓ | 100.0% |  |
| 24 | `LeastRedemptionUnit` | 增设/赎回最低单位(份) | number(10) | ✓ | 92.03% |  |
| 25 | `FiscalYearEndDate` | 财政年度终止日 | varchar2(10) | ✓ | 100.0% |  |
| 26 | `CouponFreq` | 派息频率 | number(10) | ✓ | 93.91% | 派息频率(CouponFreq)与(CT_SystemConst)表中的DM字段关联，令LB = 1798，得到派息频率... |
| 27 | `SedolCode` | 交易所官方牌价号码 | varchar2(10) | ✓ | 95.31% |  |
| 28 | `TargetIndexChiName` | 标的指数中文名称 | varchar2(200) | ✓ | 86.88% |  |
| 29 | `TargetIndexEngName` | 标的指数英文名称 | varchar2(500) | ✓ | 76.72% |  |
| 30 | `DividendPolicy` | 派息政策 | clob | ✓ | 65.78% |  |
| 31 | `InvestTarget` | 投资目标 | clob | ✓ | 51.56% |  |
| 32 | `InvestStrategy` | 投资策略 | clob | ✓ | 57.5% |  |
| 33 | `InvestPriority` | 投资重点 | number(10) | ✓ | 76.72% | 投资重点(InvestPriority)与(CT_SystemConst)表中的DM字段关联，令LB = 2356，得到... |
| 34 | `AssetCategory` | 资产类别 | number(10) | ✓ | 98.28% | 资产类别(AssetCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 1091 AND... |
| 35 | `InvestArea` | 地区重点 | number(10) | ✓ | 97.97% | 地区重点(InvestArea)与(CT_SystemConst)表中的DM字段关联，令LB = 1005，得到地区重点... |
| 36 | `Statement` | 备注说明 | varchar2(1000) | ✓ | 4.69% |  |
| 37 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 38 | `JSID` | JSID | number(19) | ✗ |  |  |
| 39 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 40 | `LeverMultiplier` | 杠杆倍数 | number(10) | ✓ | 11.87% |  |
| 41 | `SFCAuthorizationCode` | SFC注册代码 | varchar2(20) | ✓ | 57.08% |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### MainFundCode (主基金代码)

主基金代码(MainFundCode):与“港股证券主表(HK_SecuMain)”中的“证券内部编码(InnerCode)”关联，得到主基金的证券代码、中文名称等信息。

### InvestAdvisorCode (基金管理人)

基金管理人（InvestAdvisorCode）：与“基金管理人概况表（MF_InvestAdvisorOutline）”中的“基金管理人名称编号（InvestAdvisorCode）”关联，得到基金管理人的具体名称。

### TrusteeCode (基金托管人)

基金托管人（TrusteeCode）：与“基金托管人概况表（MF_TrusteeOutline）”中的“基金托管人名称编号（TrusteeCode）”关联，得到基金托管人的具体名称。

### ListedType (上市方式)

上市方式(ListedType)与(CT_SystemConst)表中的DM字段关联，令LB = 1796，得到上市方式的具体描述：1-本地，2-海外（相互上市）。

### FundType (基金类别)

基金类别(FundType)与(CT_SystemConst)表中的DM字段关联，令LB = 1797，得到基金类别的具体描述：1-实物资产，2-合成，3-期货，4-掉期，5-房地产投资信托基金。

### RegCountry (注册国家或地区)

注册国家或地区(RegCountry)与(CT_SystemConst)表中的DM字段关联，令LB = 1005，得到注册国家或地区的具体描述：1001-独联体，1005-西欧，1006-西北欧，1007-拉丁美洲，1008-中国，1009-俄罗斯，1011-韩国，1012-亚洲，1013-东亚，1015-东南亚，1016-荷兰，1018-意大利，1019-沙特阿拉伯，1021-日本，1022-印度尼西亚，1026-东京，1031-印尼，1033-泰国，1034-肯尼亚，1036-曼谷，1037-马来西亚，1038-巴西，1039-法国，1040-阿根廷，1041-安特卫普，1043-马来西亚吉隆坡，1044-土耳其，1046-欧洲鹿特丹，1048-德国汉堡，1051-亚洲新加坡，1053-英国，1055-英国利物浦，1056-伦敦，1061-伦敦市场，1066-英国东海岸南海岸，1068-欧洲，1070-加拿大，1071-美国，1076-美国市场，1081-美国纽约，1082-美国新奥尔良，1083-美国芝加哥，1086-美国纽约港，1088-美国海湾*，1089-美国海湾，1090-澳大利亚，1091-澳大利亚东部，1092-新西兰，1093-北海布伦特，2001-国内市场(国产)，2003-国内市场(进口)，3005-国际石油交易所，3009-纽约商业交易所，3010-纽约商品交易所，3011-纽约交易所，3012-纽约棉花交易所，3013-纽约可可、糖、咖啡交易所，3015-芝加哥粮谷交易所，3020-芝加哥商品交易所，3021-芝加哥商业交易所，3023-芝加哥期货交易所，3025-伦敦金融期货与期权交易所，3026-伦敦国际石油交易所，3027-伦敦战略金属市场，3028-伦敦商品交易所，3030-伦敦金属交易所，3035-悉尼交易所，3038-东京工业品交易所，3040-国际糖业组织，3042-新加坡商品交易所，3044-日本东京交易所，3046-日本横滨交易所，3048-日本名古屋交易所，3050-日本东京谷物交易所，3052-马来西亚橡胶交易所，3054-加拿大温尼伯交易所，4001-中国香港，4002-中国台湾，4003-中国（香港上市公司），4004-中国（中国上市公司），4005-中国（海外上市公司），4006-中国（中国及香港上市公司），4007-大中华，4008-印度，4009-菲律宾，4010-新加坡，4011-越南，4012-孟加拉，4013-巴基斯坦，4014-环球，4015-亚太(除日本)，4016-亚太，4017-全球新兴市场，4018-卢森堡，4019-亚洲(日本除外)。

### IfStampDuty (是否缴纳印花税)

是否缴纳印花税(IfStampDuty)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否缴纳印花税的具体描述：1-是，2-否。

### IfStockOption (是否纳入股票期权)

是否纳入股票期权(IfStockOption)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否纳入股票期权的具体描述：1-是，2-否。

### IfStockFuture (是否纳入股票期货)

是否纳入股票期货(IfStockFuture)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否纳入股票期货的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 香港基金概况 数据
SELECT *
FROM hk_fundarchives
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
