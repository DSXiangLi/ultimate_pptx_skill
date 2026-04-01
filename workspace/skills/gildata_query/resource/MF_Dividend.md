# MF_Dividend

**中文名**: 公募基金分红

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_Dividend` |
| MySQL表名 | `mf_dividend` |
| 中文名 | 公募基金分红 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益分配 |
| 更新频率 | 不定时更新 |
| 字段数量 | 38 |
| 版本 | 1.05 |

## 表描述

1.本表记录基金单次分红信息，包括分红比例、登记日、除息日等信息，以及聚源根据相关数据计算的累计分红金额、累计分红次数等数据。
2.历史数据：1998年12月起-至今。
3.信息来源：基金公司官网披露的相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.94% |  |
| 6 | `DividendImplementDate` | 分红实施公告日 | date | ✓ | 99.94% |  |
| 7 | `EndDate` | 截止日期 | date | ✓ | 100.0% | 截止日期（EndDate）：基金收益分配基准日，同收益分配基准日[ProfitDistDate]字段一致。 |
| 8 | `ProfitDistDate` | 收益分配基准日 | date | ✓ | 100.0% | 收益分配基准日(ProfitDistDate)：基金本次分红依据的可分配利润的截止日期。即，以截止该日期的本基金的可分配... |
| 9 | `UnitProfit` | 单位基金收益(元) | number(19,4) | ✓ | 0.59% |  |
| 10 | `UnitRetainedProfit` | 单位基金未分配收益(元) | number(19,4) | ✓ | 0.04% |  |
| 11 | `IfDistributed` | 是否分红 | number(3) | ✓ | 100.0% | 是否分红（IfDistributed），该字段固定以下常量：1-是；0-否 |
| 12 | `DividendRatioBeforeTax` | 派现比例(含税10派X元) | number(18,6) | ✓ | 99.15% |  |
| 13 | `ActualRatioAfterTax` | 实派比例(税后10派X元) | number(18,6) | ✓ | 99.15% |  |
| 14 | `Dividendsum` | 派现金额合计(元) | number(18,2) | ✓ | 1.52% |  |
| 15 | `ReDate` | 权益登记日 | date | ✓ | 99.15% |  |
| 16 | `ExRightDate` | 除息日 | date | ✓ | 99.14% |  |
| 17 | `ExRightDateEX` | 场内除息日 | date | ✓ | 6.01% |  |
| 18 | `ExecuteDate` | 发放日 | date | ✓ | 99.15% |  |
| 19 | `ExecuteDateEX` | 场内发放日 | date | ✓ | 6.07% |  |
| 20 | `ReinvestDay` | 红利再投资日 | date | ✓ | 91.63% |  |
| 21 | `AccountDay` | 红利再投资份额到帐日 | date | ✓ | 84.67% |  |
| 22 | `RedemptionDay` | 红利再投资份额可赎回日 | date | ✓ | 73.65% |  |
| 23 | `DistributableProfits` | 基准日基金可供分配利润(元) | number(18,6) | ✓ | 96.98% |  |
| 24 | `AllocationValue` | 基准日应分配金额(元) | number(18,6) | ✓ | 35.59% |  |
| 25 | `SchemeModification` | 方案变更说明 | varchar2(250) | ✓ | 0.94% |  |
| 26 | `EventProcedureCode` | 事件进程代码 | number(10) | ✓ | 100.0% | 事件进程代码(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1... |
| 27 | `EventProcedure` | 事件进程 | varchar2(20) | ✓ | 100.0% |  |
| 28 | `DistributedRange` | 发放范围 | varchar2(500) | ✓ | 100.0% |  |
| 29 | `UnitProfitYTD` | 本年单位累计分红(元) | number(19,4) | ✓ | 99.18% | 本年单位累计分红（UnitProfitYTD）＝∑（Di），其中：Di为年初至今的第i次分红的单位分红金额。 |
| 30 | `DividendSumYTD` | 本年累计分红总额(元) | number(19,4) | ✓ | 1.52% |  |
| 31 | `DividendTimesYTD` | 本年累计分红次数(次) | number(10) | ✓ | 99.14% |  |
| 32 | `DiviSumSinceInception` | 历史累计分红总额(元) | number(19,4) | ✓ | 1.55% |  |
| 33 | `DiviTimesSinceIncepion` | 历史累计分红次数(次) | number(10) | ✓ | 99.14% |  |
| 34 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 35 | `JSID` | JSID | number(19) | ✗ |  |  |
| 36 | `ExRightDateCurbEX` | 场外除息日 | date | ✓ | 3.69% |  |
| 37 | `ExecuteDateCurbEX` | 场外发放日 | date | ✓ | 2.1% |  |
| 38 | `ReDateEX` | 场内权益登记日 | date | ✓ | 6.1% |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### EndDate (截止日期)

截止日期（EndDate）：基金收益分配基准日，同收益分配基准日[ProfitDistDate]字段一致。

### ProfitDistDate (收益分配基准日)

收益分配基准日(ProfitDistDate)：基金本次分红依据的可分配利润的截止日期。即，以截止该日期的本基金的可分配利润为准，向基金份额持有人按一定的分红比例实施分红。

### IfDistributed (是否分红)

是否分红（IfDistributed），该字段固定以下常量：1-是；0-否

### EventProcedureCode (事件进程代码)

事件进程代码(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1001,1004,3131)，得到事件进程代码的具体描述：1001-预案，1004-决案，3131-方案实施。

### UnitProfitYTD (本年单位累计分红(元))

本年单位累计分红（UnitProfitYTD）＝∑（Di），其中：Di为年初至今的第i次分红的单位分红金额。

## SQL示例

```sql
-- 查询 公募基金分红 数据
SELECT *
FROM mf_dividend
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
