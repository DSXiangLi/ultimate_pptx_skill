# Bond_SZExchangeDetail

**中文名**: 深交所行情成交明细表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SZExchangeDetail` |
| MySQL表名 | `bond_szexchangedetail` |
| 中文名 | 深交所行情成交明细表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

1.内容说明：记录深交所现券交易逐笔成交明细。
2.固收产品于2022年5月16日前达成的大宗交易，视同为协商成交，不发布结算周期及结算方式。
3.数据范围：2009-01-06-至今
4.信息来源：深圳证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `TradeType` | 交易方式 | number(10) | ✗ | 100.0% | 交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 2650，得到交易方式的... |
| 5 | `AccuTurnoverDeals` | 累计成交笔数 | number(10) | ✗ | 100.0% |  |
| 6 | `TurnoverPrice` | 成交价格(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `TurnoverVolume` | 成交面额(万元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `TurnoverValue` | 成交金额(万元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `BuyerBranch` | 买方营业部 | varchar2(200) | ✓ | 17.06% |  |
| 10 | `BuyerBranchOrg` | 买方营业部所属机构 | number(10) | ✓ | 8.74% | 买方营业部所属机构(BuyerBranchOrg)：与“企业码表(EP_CompanyMain)”中的“企业编号(Com... |
| 11 | `SellerBranch` | 卖方营业部 | varchar2(200) | ✓ | 17.06% |  |
| 12 | `SellerBranchOrg` | 卖方营业部所属机构 | number(10) | ✓ | 8.52% | 卖方营业部所属机构(SellerBranchOrg)：与“企业码表(EP_CompanyMain)”中的“企业编号(Co... |
| 13 | `SettlementType` | 结算方式 | number(10) | ✓ | 82.94% | 结算方式(SettlementType)与(CT_SystemConst)表中的DM字段关联，令LB = 2651，得到... |
| 14 | `SettlementCycle` | 结算周期 | number(10) | ✓ | 82.94% | 结算周期(SettlementCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 1557，得... |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

债券内部编码(InnerCode)：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### TradeType (交易方式)

交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 2650，得到交易方式的具体描述：1-匹配成交，2-点击成交，3-询价成交，4-协商成交，5-竞买成交。

### BuyerBranchOrg (买方营业部所属机构)

买方营业部所属机构(BuyerBranchOrg)：与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息。

### SellerBranchOrg (卖方营业部所属机构)

卖方营业部所属机构(SellerBranchOrg)：与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息。

### SettlementType (结算方式)

结算方式(SettlementType)与(CT_SystemConst)表中的DM字段关联，令LB = 2651，得到结算方式的具体描述：1-净额，2-逐笔全额。

### SettlementCycle (结算周期)

结算周期(SettlementCycle)与(CT_SystemConst)表中的DM字段关联，令LB = 1557，得到结算周期的具体描述：1-T+0，2-T+1。

## SQL示例

```sql
-- 查询 深交所行情成交明细表 数据
SELECT *
FROM bond_szexchangedetail
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
