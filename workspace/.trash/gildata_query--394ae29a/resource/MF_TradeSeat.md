# MF_TradeSeat

**中文名**: 公募基金交易席位租用及交易状况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_TradeSeat` |
| MySQL表名 | `mf_tradeseat` |
| 中文名 | 公募基金交易席位租用及交易状况 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 24 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金中报、年报披露报告期租用交易席位交易及佣金状况，可以看出基金在本报告期内证券交易情况。
2.历史数据：1998年12月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 7 | `SecuCoName` | 券商名称 | varchar2(200) | ✓ | 100.0% |  |
| 8 | `InstitutionCode` | 券商代码 | number(10) | ✓ | 91.39% | 券商代码（InstitutionCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（Comp... |
| 9 | `SeatNumber` | 席位数(个) | number(10) | ✓ | 97.47% |  |
| 10 | `Commision` | 佣金(元) | number(19,4) | ✓ | 39.44% |  |
| 11 | `RatioInTotalCommision` | 占佣金总额比例 | number(9,6) | ✓ | 39.38% |  |
| 12 | `StockTradeVolume` | 股票交易量(元) | number(19,4) | ✓ | 39.04% |  |
| 13 | `RatioInTotalStockTrade` | 占股票交易总量比例 | number(9,6) | ✓ | 38.99% |  |
| 14 | `FundTradeVolume` | 基金交易量(元) | number(19,4) | ✓ | 1.28% |  |
| 15 | `RatioInTotalFundTrade` | 占基金交易总量比例 | number(9,6) | ✓ | 1.28% |  |
| 16 | `BondTradeVolume` | 债券交易量(元) | number(19,4) | ✓ | 15.7% |  |
| 17 | `RatioInTotalBondTrade` | 占债券交易总量比例 | number(9,6) | ✓ | 15.7% |  |
| 18 | `BondRepoVolume` | 债券回购交易量(元) | number(19,4) | ✓ | 14.15% |  |
| 19 | `RatioInTotalRepoVolume` | 占债券回购交易总量比例 | number(9,6) | ✓ | 14.18% |  |
| 20 | `WarrantTradeVolume` | 权证交易量(元) | number(19,4) | ✓ | 0.39% |  |
| 21 | `RatioInTotalWarrantTrade` | 权证交易量占权证交易总量比例 | number(9,6) | ✓ | 0.4% |  |
| 22 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 23 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

### InstitutionCode (券商代码)

券商代码（InstitutionCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到券商的基本资料。

## SQL示例

```sql
-- 查询 公募基金交易席位租用及交易状况 数据
SELECT *
FROM mf_tradeseat
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
