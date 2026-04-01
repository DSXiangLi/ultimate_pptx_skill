# Bond_Bid

**中文名**: 债券发行招标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_Bid` |
| MySQL表名 | `bond_bid` |
| 中文名 | 债券发行招标 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券发行与承销 |
| 更新频率 | 不定时更新 |
| 字段数量 | 49 |
| 版本 | 1.04 |

## 表描述

1.收录以招标方式发行的债券的招标及发行情况。
2.数据范围：2001-02-27 至今
3.信息来源：中债登

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 债券统一代码 | number(10) | ✗ | 100.0% | 债券统一代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关... |
| 3 | `IssueDate` | 发行日期 | date | ✓ | 100.0% |  |
| 4 | `IssueType` | 发行类型 | number(10) | ✓ | 100.0% | 发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1172，得到发行类型的... |
| 5 | `BidType` | 招标方式 | number(10) | ✓ | 100.0% | 招标方式(BidType)与(CT_SystemConst)表中的DM字段关联，令LB = 1178，得到招标方式的具体... |
| 6 | `BidCategory` | 招标类型 | number(10) | ✗ | 100.0% | 招标类型(BidCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 2025，得到招标类... |
| 7 | `DocumentNumber` | 招标书编号 | varchar2(50) | ✓ | 3.04% |  |
| 8 | `IssueSizePlanned` | 计划发行总量(万元) | number(19,4) | ✓ | 100.0% |  |
| 9 | `PaidAmount` | 缴款总金额(万元) | number(19,4) | ✓ | 3.04% |  |
| 10 | `ActualIssuSize` | 实际发行总量(万元) | number(19,4) | ✓ | 89.1% |  |
| 11 | `AdditionalSize` | 其中:当期追加发行量(万元) | number(19,4) | ✓ | 0.12% |  |
| 12 | `GeneralBasicUnderwrite` | 一般基本承购额(万元) | number(19,4) | ✓ | 0.0% |  |
| 13 | `BasicUnderwrite` | 基本承购总量(万元) | number(19,4) | ✓ | 3.04% |  |
| 14 | `MinUnderwrite` | 最低承购额总量(万元) | number(19,4) | ✓ | 0.0% |  |
| 15 | `BidAmount` | 招标总量(万元) | number(19,4) | ✓ | 3.05% |  |
| 16 | `CompanyNumPresent` | 应投家数 | number(10) | ✓ | 3.05% |  |
| 17 | `BidCompanyNum` | 投标家数(家) | number(10) | ✓ | 3.05% |  |
| 18 | `BidNumber` | 投标笔数(笔) | number(10) | ✓ | 3.04% |  |
| 19 | `ValidBidNumber` | 有效笔数(笔) | number(10) | ✓ | 3.05% |  |
| 20 | `InvalidBidNumber` | 无效笔数(笔) | number(10) | ✓ | 3.02% |  |
| 21 | `SubscriptionVolume` | 投标总量(万元) | number(19,4) | ✓ | 0.1% |  |
| 22 | `ValidAmount` | 有效投标总量(万元) | number(19,4) | ✓ | 3.05% |  |
| 23 | `HighBidPrice` | 最高投标价位 | number(19,4) | ✓ | 3.05% |  |
| 24 | `LowBidPrice` | 最低投标价位 | number(19,4) | ✓ | 3.05% |  |
| 25 | `CompanyNumWinBid` | 中标家数(家) | number(10) | ✓ | 3.05% |  |
| 26 | `NumWinBid` | 中标笔数(笔) | number(10) | ✓ | 3.04% |  |
| 27 | `AmountWinBid` | 中标总量(万元) | number(19,4) | ✓ | 3.05% |  |
| 28 | `DistributeAmountWinBid` | 分销中标总量(万元) | number(19,4) | ✓ | 0.0% |  |
| 29 | `SelfSupportAmountWinBid` | 自营中标总量(万元) | number(19,4) | ✓ | 2.95% |  |
| 30 | `HighPriceWinBid` | 最高中标价位(元) | number(19,4) | ✓ | 2.68% |  |
| 31 | `LowPriceWinBid` | 最低中标价位(元) | number(19,4) | ✓ | 2.68% |  |
| 32 | `MarginAmountBid` | 边际中标价位投标总量(万元) | number(19,4) | ✓ | 3.02% |  |
| 33 | `MarginAmountWinBid` | 边际中标价位中标总量(万元) | number(19,4) | ✓ | 3.02% |  |
| 34 | `InterestRateSpread` | 招标利差 | number(19,8) | ✓ | 0.29% |  |
| 35 | `IssuePrice` | 发行价格(元) | number(19,4) | ✓ | 98.85% |  |
| 36 | `PriceWinBid` | 中标价格(元) | number(19,4) | ✓ | 0.76% |  |
| 37 | `ReferrenceYield` | 参考收益率(%) | number(19,8) | ✓ | 97.64% | 参考收益率(%)(ReferrenceYield)：数据来源于中债官网披露。 |
| 38 | `CouponRate` | 票面利率(%) | number(19,8) | ✓ | 3.02% |  |
| 39 | `InterestRateWinBid` | 中标利率(%) | number(19,8) | ✓ | 1.96% |  |
| 40 | `MarginalRate` | 边际利率(%) | number(19,8) | ✓ | 0.1% |  |
| 41 | `FirstCouponRate` | 第一年计息利率(%) | number(19,8) | ✓ | 0.0% |  |
| 42 | `OverSubMultiple` | 全场倍数 | number(19,8) | ✓ | 0.1% |  |
| 43 | `MarginalMultiple` | 边际倍数 | number(19,8) | ✓ | 0.1% |  |
| 44 | `CompanyNumExcessBid` | 投标超额家数(家) | number(10) | ✓ | 0.0% |  |
| 45 | `AmountExcessBid` | 投标超额数量(万元) | number(19,4) | ✓ | 0.0% |  |
| 46 | `CompanyNumLackBid` | 投标不足家数(家) | number(10) | ✓ | 0.01% |  |
| 47 | `AmountLackBid` | 投标不足数量(万元) | number(19,4) | ✓ | 0.01% |  |
| 48 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 49 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券统一代码)

债券统一代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“统一内部编码（MainCode）”关联，得到债券统一代码下各个市场的交易代码、债券简称等。（若是跨市场发行的债券，需用MainCode进行查询。）

### IssueType (发行类型)

发行类型(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1172，得到发行类型的具体描述：1-一次发行，2-二次发行，3-三次发行，4-四次发行，5-五次发行，6-六次发行，7-七次发行，8-八次发行，9-九次发行，10-十次发行，11-十一次发行，12-十二次发行，13-十三次发行，14-十四次发行，15-十五次发行，16-十六次发行，17-十七次发行，18-十八次发行，19-十九次发行，20-二十次发行，21-二十一次发行，22-二十二次发行，23-二十三发行，24-二十四次发行，25-二十五次发行，26-二十六次发行，27-二十七次发行，28-二十八次发行，29-二十九次发行，30-三十次发行，31-三十一次发行，32-三十二次发行，33-三十三次发行，34-三十四次发行，35-三十五次发行，36-三十六次发行，37-三十七次发行，38-三十八次发行，39-三十九次发行，40-四十次发行，41-四十一次发行，42-四十二次发行，43-四十三次发行，44-四十四次发行，45-四十五次发行，46-四十六次发行，47-四十七次发行，48-四十八次发行，49-四十九次发行，50-五十次发行，901-一次发行(超额)，1001-到期赎回价格招标。

### BidType (招标方式)

招标方式(BidType)与(CT_SystemConst)表中的DM字段关联，令LB = 1178，得到招标方式的具体描述：1-竞争性招标，2-非竞争性招标，3-招标总览。

### BidCategory (招标类型)

招标类型(BidCategory)与(CT_SystemConst)表中的DM字段关联，令LB = 2025，得到招标类型的具体描述：1-首场招标，2-追加招标。

### ReferrenceYield (参考收益率(%))

参考收益率(%)(ReferrenceYield)：数据来源于中债官网披露。

## SQL示例

```sql
-- 查询 债券发行招标 数据
SELECT *
FROM bond_bid
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
