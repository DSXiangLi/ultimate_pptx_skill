# DZ_DividendProgress

**中文名**: 公司分红进度

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_DividendProgress` |
| MySQL表名 | `dz_dividendprogress` |
| 中文名 | 公司分红进度 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司融资分红 |
| 更新频率 | 日更新 |
| 字段数量 | 40 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录上市公司分红的详细信息，以事件进程为维度，一次分红根据不同的进程，分多条记录展示，主要进程包括：意向、预案、决案、方案实施等。
2.数据范围：1991-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `SchemeNo` | 方案序号 | number(10) | ✗ | 100.0% | 方案序号（SchemeNo）：根据公告披露的不同方案做识别区分，如1代表第一个方案；2代表第二个方案。最终实施的方案根据... |
| 5 | `InfoPubDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 6 | `InfoPubType` | 信息发布日期类型 | number(10) | ✗ | 100.0% | 信息发布日期类型(InfoPubType)与(CT_SystemConst)表中的DM字段关联，令LB = 1740，得... |
| 7 | `SchemeType` | 方案类型 | number(10) | ✓ | 100.0% | 方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型... |
| 8 | `Process` | 事件进程 | number(10) | ✗ | 100.0% | 事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN... |
| 9 | `IfDividend` | 是否分红 | number(10) | ✓ | 100.0% | 是否分红(IfDividend)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 10 | `BonusShareRatio` | 送股比例(10股送X) | number(19,8) | ✓ | 3.37% |  |
| 11 | `TranAddShareRatio` | 转增股比例(10股转增X) | number(19,8) | ✓ | 11.66% |  |
| 12 | `CashDiviRMB` | 派现(含税10股派X元) | number(19,8) | ✓ | 55.5% |  |
| 13 | `ActualCashDiviRMB` | 实派(税后10股派X元) | number(19,8) | ✓ | 25.71% |  |
| 14 | `QFIIAcCashDiviRMB` | QFII实派(税后10股派X元) | number(19,8) | ✓ | 55.5% |  |
| 15 | `RSHolderAcCashDiviRMB` | 限售股持有人实派(税后10股派X元) | number(19,8) | ✓ | 3.37% |  |
| 16 | `FSHolderAcCashDiviRMB` | 流通股持有人实派(税后10股派X元) | number(19,8) | ✓ | 3.37% |  |
| 17 | `DiviBase` | 分红股本基数(股) | number(19,2) | ✓ | 58.75% |  |
| 18 | `DividendBaseDate` | 分红派息股本基准日 | date | ✓ | 19.12% |  |
| 19 | `DiviObject` | 分红对象 | number(10) | ✓ | 58.93% | 分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND D... |
| 20 | `DiviObjectNew` | 分红对象(新) | number(10) | ✓ | 58.93% | 分红对象(新)(DiviObjectNew)与(CT_SystemConst)表中的DM字段关联，令LB = 1197 ... |
| 21 | `SharesAfterDivi` | 送转后总股本 | number(19,2) | ✓ | 13.38% |  |
| 22 | `TotalCashDivi` | 合计派现金额(元) | number(19,4) | ✓ | 55.39% |  |
| 23 | `CashDiviAShare` | A股派现金额(元) | number(19,4) | ✓ | 54.8% |  |
| 24 | `RegisterDate` | 股权登记日 | date | ✓ | 19.09% |  |
| 25 | `ExDiviDate` | 除权除息日 | date | ✓ | 19.07% |  |
| 26 | `ExDiviRefPrice` | 除权除息参考价(元) | number(19,8) | ✓ | 18.38% |  |
| 27 | `BonusShareArrivalDate` | 送转股到账日 | date | ✓ | 1.61% |  |
| 28 | `BonusShareListDate` | 送转股上市日 | date | ✓ | 4.29% |  |
| 29 | `ToAccountDate` | 股息到帐日期/红利发放日 | date | ✓ | 17.84% |  |
| 30 | `BonusSHRatioAdjusted` | 送股比例(10股送X)(计算除权价用) | number(18,8) | ✓ | 3.37% |  |
| 31 | `TranAddRatioAdjusted` | 转增比例(10股转增X)(计算除权价用) | number(18,8) | ✓ | 11.66% |  |
| 32 | `CashDiviRMBAdjusted` | 派现(含税10股派X元)(计算除权价用) | number(18,8) | ✓ | 55.5% |  |
| 33 | `ChangeType` | 方案变更类型 | number(10) | ✓ |  | 方案变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1013，得到方案... |
| 34 | `ChangeStatement` | 方案变更说明 | varchar2(255) | ✓ | 1.47% |  |
| 35 | `SchemeStatement` | 方案补充说明 | varchar2(500) | ✓ | 0.05% |  |
| 36 | `UndistributeStatement` | 利润不分配说明 | varchar2(255) | ✓ | 40.86% |  |
| 37 | `Notes` | 备注 | varchar2(255) | ✓ | 1.48% |  |
| 38 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 39 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 40 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### SchemeNo (方案序号)

方案序号（SchemeNo）：根据公告披露的不同方案做识别区分，如1代表第一个方案；2代表第二个方案。最终实施的方案根据实际情况披露为准。

### InfoPubType (信息发布日期类型)

信息发布日期类型(InfoPubType)与(CT_SystemConst)表中的DM字段关联，令LB = 1740，得到信息发布日期类型的具体描述：10-预披露公告日，20-预案公告日，30-决案公告日，40-分红实施公告日，50-方案变更公告日，60-更正公告日，70-延期审议公告日，80-延缓实施公告日，99-其他公告日。

### SchemeType (方案类型)

方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型的具体描述：10-公司提出方案，20-股东提出方案，99-其它。

### Process (事件进程)

事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1000,1001,1004,3120,3125,3131,3305)，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，3120-董事会否决，3125-股东大会否决，3131-方案实施，3305-放弃。

### IfDividend (是否分红)

是否分红(IfDividend)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2,8,24,25,99)，得到是否分红的具体描述：1-是，2-否，8-对价，24-重整计划，25-特殊分红，99-其他分红。

### DiviObject (分红对象)

分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND DM  IN   (1,2,3)，得到分红对象的具体描述：1-全体股东，2-发行前股东，3-部分股东。

### DiviObjectNew (分红对象(新))

分红对象(新)(DiviObjectNew)与(CT_SystemConst)表中的DM字段关联，令LB = 1197  AND DM  IN   (1,6,7,8,9,11,12,13,14,15)，得到分红对象(新)的具体描述：1-全体股东，6-有限售股东，7-无限售股东，8-社会公众股东，9-其他类型股东，11-全体股东(扣除特定对象)，12-部分股东(含流通股股东)，13-部分股东(特定分红对象)，14-重整投资人，15-重整投资人及部分股东。

### ChangeType (方案变更类型)

方案变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1013，得到方案变更类型的具体描述：1-总量变更，2-总量不变，3-基数变更，4-基数不变，5-其他。

## SQL示例

```sql
-- 查询 公司分红进度 数据
SELECT *
FROM dz_dividendprogress
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
