# LC_TransferPlan

**中文名**: 股东增减持计划表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_TransferPlan` |
| MySQL表名 | `lc_transferplan` |
| 中文名 | 股东增减持计划表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 日更新 |
| 字段数量 | 43 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录上市公司(包含科创板)股东增持计划、减持计划、被动减持计划、不减持类别指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.99% |  |
| 6 | `PromiseSubject` | 承诺主体类型 | number(10) | ✓ | 100.0% | 承诺主体类型(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351 ... |
| 7 | `EventType` | 承诺事项类型 | number(10) | ✓ | 100.0% | 承诺事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352 AND D... |
| 8 | `IfEffected` | 承诺是否有效 | number(10) | ✓ | 100.0% | 承诺是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND D... |
| 9 | `EventProcedure` | 事件进程 | number(10) | ✓ | 81.41% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB=2380，得到事件... |
| 10 | `SHSN` | 股东序号 | number(10) | ✓ | 100.0% |  |
| 11 | `SHName` | 股东名称 | varchar2(200) | ✗ | 100.0% |  |
| 12 | `TransferPlanType` | 增减持计划类别 | number(10) | ✗ | 100.0% | 增减持计划类别(TransferPlanType)与(CT_SystemConst)表中的DM字段关联，令LB = 13... |
| 13 | `PromiseBeginDate` | 承诺起始日期 | date | ✓ | 82.88% |  |
| 14 | `PromiseEndDate` | 承诺截止日期 | date | ✓ | 82.73% |  |
| 15 | `PromiseStatment` | 承诺说明 | clob | ✓ | 4.48% |  |
| 16 | `IncreaseTime` | 增持时间描述 | varchar2(200) | ✓ | 14.07% |  |
| 17 | `IncreaseTerm` | 增持实施期限(月) | number(18,2) | ✓ | 13.75% |  |
| 18 | `IncreasePriceStatement` | 增持价格描述 | varchar2(200) | ✓ | 8.61% |  |
| 19 | `IncreasePriceCeiling` | 增持股票触发价格上限(元) | number(19,4) | ✓ | 1.88% |  |
| 20 | `IncreasePriceFloor` | 增持股票触发价格下限(元) | number(19,4) | ✓ | 0.15% |  |
| 21 | `IncreaseSize` | 增持规模描述 | varchar2(200) | ✓ | 14.11% |  |
| 22 | `IncreaseShareCeiling` | 增持股份数量上限(股/份) | number(18,2) | ✓ | 2.13% |  |
| 23 | `IncreaseShareFloor` | 增持股份数量下限(股/份) | number(18,2) | ✓ | 2.73% |  |
| 24 | `IncreaseRatioCeiling` | 增持比例上限-占总股本 | number(18,8) | ✓ | 3.22% |  |
| 25 | `IncreaseRatioFloor` | 增持比例下限-占总股本 | number(18,8) | ✓ | 1.27% |  |
| 26 | `IncreaseFundCeiling` | 增持投入资金上限(元) | number(19,4) | ✓ | 5.66% |  |
| 27 | `IncreaseFundFloor` | 增持投入资金下限(元) | number(19,4) | ✓ | 7.66% |  |
| 28 | `NotReducePromise` | 不减持承诺期限(月) | number(18,2) | ✓ | 7.98% |  |
| 29 | `TradeType` | 交易方式 | number(10) | ✓ | 72.4% | 交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM ... |
| 30 | `TradeTypeStatment` | 交易方式描述 | varchar2(50) | ✓ | 37.46% |  |
| 31 | `ReduceTime` | 减持时间描述 | varchar2(200) | ✓ | 54.06% |  |
| 32 | `ReduceTerm` | 减持实施期限(月) | number(18,2) | ✓ | 53.72% |  |
| 33 | `ReducePriceStatement` | 减持价格描述 | varchar2(200) | ✓ | 63.26% |  |
| 34 | `ReducePriceCeiling` | 减持股票触发价格上限(元) | number(19,4) | ✓ | 0.91% |  |
| 35 | `ReducePriceFloor` | 减持股票触发价格下限(元) | number(19,4) | ✓ | 2.24% |  |
| 36 | `ReduceSize` | 减持规模描述 | varchar2(200) | ✓ | 66.38% |  |
| 37 | `ReduceShareCeiling` | 减持股份数量上限(股/份) | number(18,2) | ✓ | 66.01% |  |
| 38 | `ReduceShareFloor` | 减持股份数量下限(股/份) | number(18,2) | ✓ | 5.48% |  |
| 39 | `ReduceRatioCeiling` | 减持比例上限-占总股本 | number(18,8) | ✓ | 65.4% |  |
| 40 | `ReduceRatioFloor` | 减持比例下限-占总股本 | number(18,8) | ✓ | 5.32% |  |
| 41 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 42 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 43 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### PromiseSubject (承诺主体类型)

承诺主体类型(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351 AND DM<>300，得到承诺主体类型的具体描述：100-非流通股东，110-间接控股股东，150-流通股东，500-公司管理层。

### EventType (承诺事项类型)

承诺事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352 AND DM IN (71,72)，得到承诺事项类型的具体描述：71-新股上市股东承诺，72-上市后股东追加承诺。

### IfEffected (承诺是否有效)

承诺是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到承诺是否有效的具体描述：1-是，2-否。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB=2380，得到事件进程的具体描述：1-承诺开始未实施，2-承诺实施完成，3-承诺未实施终止，4-承诺已实施终止，5-承诺到期未实施，6-承诺实施中。

### TransferPlanType (增减持计划类别)

增减持计划类别(TransferPlanType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306 AND DM IN (124,127,128,201)，得到增减持计划类别的具体描述：124-不减持，127-主动减持计划，128-被动减持计划，201-增持计划。

### TradeType (交易方式)

交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM IN (1,8,15,80,98,99)，得到交易方式的具体描述：1-协议转让，8-大宗交易，15-集中竞价，80-司法拍卖，98-多种交易方式，99-其他。

## SQL示例

```sql
-- 查询 股东增减持计划表 数据
SELECT *
FROM lc_transferplan
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
