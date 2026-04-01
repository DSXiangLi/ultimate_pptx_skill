# HK_IPOKeyIndex

**中文名**: 港股新股重点关注指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_IPOKeyIndex` |
| MySQL表名 | `hk_ipokeyindex` |
| 中文名 | 港股新股重点关注指标 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股融资与分红 |
| 更新频率 | 日更新 |
| 字段数量 | 54 |
| 版本 | 1.03 |

## 表描述

1.内容说明：新建港股新股重点关注指标信息，记录港股新股发行中的重点关注信息。
2.数据范围：无。
3.信息来源：恒生聚源整理。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 an... |
| 4 | `IssueMethod` | 发行方式 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `ProspectusPublDate` | 招股章程发布日 | date | ✗ | 100.0% |  |
| 6 | `ApplyStartDate` | 申购起始日 | varchar2(10) | ✓ | 77.8% |  |
| 7 | `PayStartDate` | 缴款起始日 | varchar2(10) | ✓ | 77.8% |  |
| 8 | `PayEndDate` | 缴款截止日 | date | ✓ | 79.46% |  |
| 9 | `ApplyEndDate` | 申购截止日 | date | ✓ | 79.46% |  |
| 10 | `IssueEndDate` | 发行截止日 | date | ✓ | 79.46% |  |
| 11 | `PricingDate` | 定价日 | varchar2(10) | ✓ | 72.31% |  |
| 12 | `ReleaseDate` | 发行结果公布日 | varchar2(10) | ✓ | 88.1% |  |
| 13 | `TermPublDate` | 终止实施公布日 | varchar2(10) | ✓ | 3.29% |  |
| 14 | `DateToAccount` | 股票发放日 | varchar2(10) | ✓ | 91.64% |  |
| 15 | `RefundmentOutDate` | 退款寄发日 | varchar2(10) | ✓ | 81.59% |  |
| 16 | `DarkTradingDay` | 暗盘交易日 | varchar2(10) | ✓ | 98.97% |  |
| 17 | `ListedDate` | 上市日 | varchar2(10) | ✓ | 98.97% |  |
| 18 | `OAllOptionExpDate` | 超额配售权行使完成日 | varchar2(10) | ✓ | 32.15% |  |
| 19 | `OAllListDate` | 超额配售股份上市日 | varchar2(10) | ✓ | 31.98% |  |
| 20 | `IssuePriceUnit` | 发行价货币单位 | varchar2(20) | ✓ | 100.0% | 发行价货币单位(IssuePriceUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068... |
| 21 | `PurPriceInterval` | 申购价区间 | varchar2(50) | ✓ | 91.47% |  |
| 22 | `IssuePrice` | 每股发行价(元) | number(18,8) | ✓ | 88.03% |  |
| 23 | `TradingUnit` | 买卖单位(股/手) | number(10) | ✓ | 99.65% |  |
| 24 | `IssueVol` | 发行总股数 | number(18,0) | ✓ | 91.47% |  |
| 25 | `PublicOfferedShare` | 公开发售股数 | number(18,0) | ✓ | 79.28% |  |
| 26 | `InterAllotShare` | 国际配售股数 | number(18,0) | ✓ | 90.44% |  |
| 27 | `TotalProceeds` | 募资总额(元) | number(18,2) | ✓ | 91.47% |  |
| 28 | `OverAllotment` | 超额配售股数 | number(18,0) | ✓ | 69.97% |  |
| 29 | `OverAllotmentProceeds` | 超额配售募资总额(元) | number(18,2) | ✓ | 63.07% |  |
| 30 | `PublicOfferApplNum` | 公开发售申购人数 | number(18,0) | ✓ | 43.84% |  |
| 31 | `PublicOfferBallNum` | 公开发售中签人数 | number(18,0) | ✓ | 43.84% |  |
| 32 | `AdmissionFee` | 入场费 | number(18,4) | ✓ | 45.22% |  |
| 33 | `OneLotWinningRate` | 一手中签率(%) | number(18,4) | ✓ | 43.84% |  |
| 34 | `OverAllotApplMul` | 超额申购倍数 | number(18,2) | ✓ | 75.89% |  |
| 35 | `HeadHamApplSheet` | 顶头槌申购张数 | number(10) | ✓ | 100.0% |  |
| 36 | `MiniSubscribedShares` | 稳中认购股数 | number(10) | ✓ | 43.17% |  |
| 37 | `CallBackRatio` | 回拨比率(%) | number(18,2) | ✓ | 35.73% |  |
| 38 | `NSTotalShares` | 新股港股股本(股) | number(18,0) | ✓ | 100.0% |  |
| 39 | `NSMarketValue` | 新股港股市值(元) | number(18,2) | ✓ | 88.03% |  |
| 40 | `NSCTotalShares` | 新股总股本(股) | number(18,0) | ✓ | 100.0% |  |
| 41 | `NSCMarketValue` | 新股总市值(元) | number(18,2) | ✓ | 88.03% |  |
| 42 | `EPSBasic` | 调整每股收益(元) | number(18,4) | ✓ | 64.02% |  |
| 43 | `PERatio` | 静态市盈率 | number(18,4) | ✓ | 56.09% |  |
| 44 | `FPE` | 动态市盈率 | number(18,4) | ✓ | 54.11% |  |
| 45 | `PETTM` | 滚动市盈率 | number(18,4) | ✓ | 82.9% |  |
| 46 | `PS` | 市销率 | number(18,4) | ✓ | 80.24% |  |
| 47 | `PCF` | 市现率 | number(18,4) | ✓ | 79.99% |  |
| 48 | `PB` | 市净率 | number(18,4) | ✓ | 81.69% |  |
| 49 | `InduFHS` | 恒生一级行业分类 | number(10) | ✓ | 84.1% | 恒生一级行业分类（InduFHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（Industr... |
| 50 | `InduSHS` | 恒生二级行业分类 | number(10) | ✓ | 84.1% | 恒生二级行业分类（InduSHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（Industr... |
| 51 | `InduCHS` | 恒生三级行业分类 | number(10) | ✓ | 84.1% | 恒生三级行业分类（InduCHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（Industr... |
| 52 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 53 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 54 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 and DM in (1001,1016,3131)，得到事件进程的具体描述：1001-预案，1016-未实施终止，3131-方案实施。

### IssuePriceUnit (发行价货币单位)

发行价货币单位(IssuePriceUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 and DM in (1000,1100,1420)，得到发行价货币单位的具体描述：1000-美元，1100-港元，1420-人民币元。

### InduFHS (恒生一级行业分类)

恒生一级行业分类（InduFHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（IndustryNum）关联获得行业名称的描述。

### InduSHS (恒生二级行业分类)

恒生二级行业分类（InduSHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（IndustryNum）关联获得行业名称的描述。

### InduCHS (恒生三级行业分类)

恒生三级行业分类（InduCHS）：与港股行业分类表（HK_IndustryCategory）的行业编码（IndustryNum）关联获得行业名称的描述。

## SQL示例

```sql
-- 查询 港股新股重点关注指标 数据
SELECT *
FROM hk_ipokeyindex
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
