# LC_Dividend

**中文名**: 公司分红

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_Dividend` |
| MySQL表名 | `lc_dividend` |
| 中文名 | 公司分红 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司融资与分红 |
| 更新频率 | 不定时更新 |
| 字段数量 | 65 |
| 版本 | 1.04 |

## 表描述

1.该表包括上市公司历次分红预案及实施进展，以及下年分配次数、方式等，以分红事件为维度，一次分红做一条记录。
2.数据范围：证券上市起-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `ProposalSN` | 议案编号 | number(10) | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AN... |
| 6 | `EventProcedureDesc` | 事件进程描述 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `IfDividend` | 是否分红 | number(10) | ✓ | 100.0% | 是否分红(IfDividend)固定以下常量：0-否，1-是，8-对价，24-重整计划，25-特殊分红，26-面值拆分，... |
| 8 | `SchemeType` | 方案类型 | number(10) | ✓ | 99.39% | 方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型... |
| 9 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 10 | `DiviIntentPublDate` | 分红意向公布日 | date | ✓ | 1.43% |  |
| 11 | `AdvanceDate` | 预案公布日 | date | ✓ | 99.93% |  |
| 12 | `SMDeciPublDate` | 决案公布日(股东大会决议公告日) | date | ✓ | 52.28% |  |
| 13 | `DividendImplementDate` | 分红实施公告日 | date | ✓ | 36.36% |  |
| 14 | `BonusShareRatio` | 送股比例(10送X) | number(18,8) | ✓ | 2.3% |  |
| 15 | `TranAddShareRaio` | 转增股比例(10转增X) | number(18,8) | ✓ | 7.01% |  |
| 16 | `PriceUnit` | 派现外币单位 | number(10) | ✓ | 1.14% | 派现外币单位（PriceUnit）：与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“L... |
| 17 | `CashDiviRMB` | 派现(含税10派X元)(人民币) | number(18,8) | ✓ | 34.39% |  |
| 18 | `ActualCashDiviRMB` | 实派(税后10派X元)(人民币) | number(18,8) | ✓ | 33.9% |  |
| 19 | `CashDiviFC` | 派现(含税10派X外币) | number(18,8) | ✓ | 1.13% |  |
| 20 | `ActualCashDiviFC` | 实派(税后10派X外币) | number(18,8) | ✓ | 1.13% |  |
| 21 | `RightRegDate` | 股权登记日 | date | ✓ | 36.19% |  |
| 22 | `ExDiviDate` | 除权除息日 | date | ✓ | 36.36% |  |
| 23 | `ExDiviRefPrice` | 除权除息参考价(元) | number(19,8) | ✓ | 34.93% |  |
| 24 | `BonusShareArrivalDate` | 送转股到账日 | date | ✓ | 3.08% |  |
| 25 | `BonusShareListDate` | 送转股上市日 | date | ✓ | 8.22% |  |
| 26 | `ToAccountDate` | 股息到帐日期/红利发放日 | date | ✓ | 33.85% |  |
| 27 | `FinalTradingDay` | 最后交易日 | date | ✓ | 1.24% |  |
| 28 | `DiviBase` | 分红股本基数(股) | number(16,0) | ✓ | 36.61% |  |
| 29 | `DividendBaseDate` | 分红派息股本基准日 | date | ✓ | 35.39% |  |
| 30 | `SharesAfterDivi` | 送转后总股本(股) | number(16,0) | ✓ | 8.31% |  |
| 31 | `DiviObject` | 分红对象 | number(10) | ✓ | 36.61% | 分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND D... |
| 32 | `DiviObjectNew` | 分红对象(新) | number(10) | ✓ | 36.61% | 分红对象(新)(DiviObjectNew)与(CT_SystemConst)表中的DM字段关联，令LB = 1197 ... |
| 33 | `TotalCashDiviComRMB` | 公司合计派现金额(人民币元) | number(19,4) | ✓ | 34.39% |  |
| 34 | `TotalCashDiviComFC` | 公司合计派现金额(外币元) | number(19,4) | ✓ | 1.13% |  |
| 35 | `CashDiviAShare` | 其中:A股派现金额(元) | number(19,4) | ✓ | 33.25% |  |
| 36 | `CashDiviBShareRMB` | B股派现金额(人民币元) | number(19,4) | ✓ | 1.14% |  |
| 37 | `CashDiviBShareFC` | B股派现金额(外币元) | number(19,4) | ✓ | 1.14% |  |
| 38 | `BonusSHRatioAdjusted` | 送股比例(10送X)(计算除权价用) | number(18,8) | ✓ | 2.3% |  |
| 39 | `TranAddRatioAdjusted` | 转增比例(10转增X)(计算除权价用) | number(18,8) | ✓ | 7.01% |  |
| 40 | `CashDiviRMBAdjusted` | 派现(含税10派X元)(计算除权价用) | number(18,8) | ✓ | 34.39% |  |
| 41 | `IFSchemeChange` | 方案是否变更 | number(10) | ✓ | 97.36% | 方案是否变更（IFSchemeChange），该字段固定以下常量：1-是；0-否 |
| 42 | `ChangeStatement` | 方案变更说明 | varchar2(255) | ✓ | 0.81% |  |
| 43 | `ChangeType` | 方案变更类型 | number(10) | ✓ |  | 方案变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1013，得到方案... |
| 44 | `Notes` | 备注 | varchar2(255) | ✓ | 1.93% |  |
| 45 | `SchemeStatement` | 方案补充说明 | varchar2(500) | ✓ | 0.01% |  |
| 46 | `UndistributeStatement` | 利润不分配说明 | varchar2(255) | ✓ | 63.39% |  |
| 47 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 48 | `JSID` | JSID | number(19) | ✗ |  |  |
| 49 | `EPS` | 每股收益(元) | number(9,4) | ✓ | 29.13% |  |
| 50 | `DiviStartDate` | 红利发放起始日 | date | ✓ | 1.18% |  |
| 51 | `DiviEndDate` | 红利发放截止日 | date | ✓ | 1.14% |  |
| 52 | `IfDiviBeforeChange` | 变更前是否分红 | number(10) | ✓ | 0.79% | 变更前是否分红（IfDiviBeforeChange），该字段固定以下常量：1-是；0-否 |
| 53 | `BonusShareRatioBeforeChange` | 变更前送股比例(10送X) | number(9,4) | ✓ | 0.04% |  |
| 54 | `TranAddShareRatioBeforeChange` | 变更前转增股比例(10转增X) | number(9,4) | ✓ | 0.19% |  |
| 55 | `CashDiviBeforeChangeRMB` | 变更前派现(含税10派X元)(人民币) | number(19,4) | ✓ | 0.74% |  |
| 56 | `CashDiviBeforeChangeFC` | 变更前派现(含税10派X外币) | number(19,4) | ✓ | 0.0% |  |
| 57 | `DiviBaseBeforeChange` | 变更前分红股本基数(股) | number(16,0) | ✓ | 0.48% |  |
| 58 | `DistributeTimes` | 利润分配次数 | varchar2(10) | ✓ | 1.5% |  |
| 59 | `CeilingNext` | 下限(废弃1) | number(9,6) | ✓ | 1.18% |  |
| 60 | `FloorNext` | 上限(废弃1) | number(9,6) | ✓ | 0.51% |  |
| 61 | `Ceiling` | 下限(废弃2) | number(9,6) | ✓ | 0.96% |  |
| 62 | `Floor` | 上限(废弃2) | number(9,6) | ✓ | 0.43% |  |
| 63 | `MainForm` | 主要分配形式 | number(10) | ✓ |  |  |
| 64 | `CashDiviCeiling` | 下限(废弃3) | number(9,6) | ✓ | 0.85% |  |
| 65 | `CashDiviFloor` | 上限(废弃3) | number(9,6) | ✓ | 0.3% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1000,1001,1004,3120,3125,3131,3305)，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，3120-董事会否决，3125-股东大会否决，3131-方案实施，3305-放弃。

### IfDividend (是否分红)

是否分红(IfDividend)固定以下常量：0-否，1-是，8-对价，24-重整计划，25-特殊分红，26-面值拆分，99-其他分红。

### SchemeType (方案类型)

方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型的具体描述：10-公司提出方案，20-股东提出方案，99-其它。

### PriceUnit (派现外币单位)

派现外币单位（PriceUnit）：与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1068”，得到派现外币单位的具体描述。1000-美元，1100-港元。该字段主要记录B股分红涉及的外币单位，A股分红因通常单位都是人民币，故派现外币单位为NULL。

### DiviObject (分红对象)

分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND DM  IN   (1,2,3)，得到分红对象的具体描述：1-全体股东，2-发行前股东，3-部分股东。

### DiviObjectNew (分红对象(新))

分红对象(新)(DiviObjectNew)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND DM  IN   (1,6,7,8,9,11,12,13,14,15)，得到分红对象(新)的具体描述：1-全体股东，6-有限售股东，7-无限售股东，8-社会公众股东，9-其他类型股东，11-全体股东(扣除特定对象)，12-部分股东(含流通股股东)，13-部分股东(特定分红对象)，14-重整投资人，15-重整投资人及部分股东。

### IFSchemeChange (方案是否变更)

方案是否变更（IFSchemeChange），该字段固定以下常量：1-是；0-否

### ChangeType (方案变更类型)

方案变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1013，得到方案变更类型的具体描述：1-总量变更，2-总量不变，3-基数变更，4-基数不变，5-其他。

### IfDiviBeforeChange (变更前是否分红)

变更前是否分红（IfDiviBeforeChange），该字段固定以下常量：1-是；0-否

## SQL示例

```sql
-- 查询 公司分红 数据
SELECT *
FROM lc_dividend
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
