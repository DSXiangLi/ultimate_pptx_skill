# LC_PromiseImplement

**中文名**: 股东承诺实施

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PromiseImplement` |
| MySQL表名 | `lc_promiseimplement` |
| 中文名 | 股东承诺实施 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 31 |
| 版本 | 1 |

## 表描述

1.收录自股权分置开始，股东对于承诺实施日期、承诺实施截止日期、承诺实施价格、承诺事项说明等具体承诺详情。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.99% |  |
| 6 | `PromiseSubject` | 承诺主体 | number(10) | ✓ | 100.0% | 承诺主体(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351，得到... |
| 7 | `EventType` | 事项类型 | number(10) | ✓ | 100.0% | 事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352，得到事项类型的... |
| 8 | `InfoType` | 信息类别 | number(10) | ✓ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1353，得到信息类别的具... |
| 9 | `SHSN` | 股东序号 | number(10) | ✓ | 100.0% |  |
| 10 | `SHName` | 股东名单 | varchar2(200) | ✓ | 100.0% |  |
| 11 | `CompanyNumber` | 企业编号 | number(10) | ✓ | 55.53% | 企业编号（CompanyNumber）与机构基本资料表（LC_InstiArchive）中企业编号（CompanyCod... |
| 12 | `PromiseType` | 承诺类别 | number(10) | ✓ | 100.0% | 承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306，得到承诺类... |
| 13 | `ImplementStartDate` | 承诺实施日期起始 | date | ✓ | 5.84% |  |
| 14 | `ImplementEndDate` | 承诺实施日期截止 | date | ✓ | 4.98% |  |
| 15 | `TriggerPrice` | 承诺触发价格 | number(19,4) | ✓ | 5.82% |  |
| 16 | `ImplementPrice` | 承诺实施价格 | number(19,4) | ✓ | 0.0% |  |
| 17 | `EffectiveDate` | 生效日期 | date | ✓ | 5.84% |  |
| 18 | `ChangeReason` | 变动原因 | number(10) | ✓ | 5.27% | 变动原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1216，得到变动... |
| 19 | `PromiseStatement` | 承诺事项说明 | varchar2(1000) | ✓ | 94.78% |  |
| 20 | `EndDate` | 截止日期 | date | ✓ | 94.05% |  |
| 21 | `IfImplemented` | 是否实施 | number(10) | ✓ | 94.15% | 是否实施(IfImplemented)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND ... |
| 22 | `Reason` | 原因类别 | number(10) | ✓ | 5.92% | 原因类别(Reason)与(CT_SystemConst)表中的DM字段关联，令LB = 1354，得到原因类别的具体描... |
| 23 | `ImplementStatement` | 实施情况说明 | varchar2(1000) | ✓ | 94.07% |  |
| 24 | `ImplementShares` | 本次实施股数(股/份) | number(18,2) | ✓ | 93.88% |  |
| 25 | `ImplementMoney` | 本次实施金额(元) | number(19,4) | ✓ | 69.66% |  |
| 26 | `ImplementSharesTotal` | 累计实施股数(股/份) | number(18,2) | ✓ | 93.83% |  |
| 27 | `ImplementMoneyTotal` | 累计实施金额(元) | number(19,4) | ✓ | 74.68% |  |
| 28 | `ImplementPriceBottom` | 实施价格区间起始 | number(19,4) | ✓ | 67.18% |  |
| 29 | `ImplementPriceCeiling` | 实施价格区间截止 | number(19,4) | ✓ | 67.18% |  |
| 30 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 31 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### PromiseSubject (承诺主体)

承诺主体(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351，得到承诺主体的具体描述：100-非流通股东，110-间接控股股东，150-流通股东，300-上市公司，500-公司管理层。

### EventType (事项类型)

事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352，得到事项类型的具体描述：10-股改时承诺，15-股改后追加承诺，25-发行后追加承诺，31-承诺总体说明，35-承诺变更说明，51-对价支付及持股变动，61-招股时承诺，71-新股上市股东承诺，72-上市后股东追加承诺。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1353，得到信息类别的具体描述：1-承诺要素变更，5-承诺实施情况。

### CompanyNumber (企业编号)

企业编号（CompanyNumber）与机构基本资料表（LC_InstiArchive）中企业编号（CompanyCode）关联

### PromiseType (承诺类别)

承诺类别(PromiseType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306，得到承诺类别的具体描述：11-直接支付对价，13-转付对价，15-直接缩股，19-其他对价，20-不支付转付对价，21-由其他股东垫付对价，31-代其他股东垫付对价，101-上市限售期限，102-询价转让限售期限，104-最低持股比例，107-分步出售比例，110-上市价格限制，121-延长锁定期，124-不减持，127-主动减持计划，128-被动减持计划，201-增持计划，301-流通股东出售权，401-股份追送，403-股价差额现金支付，501-股权激励，991-违约责任承诺，992-分红承诺，993-资产注入承诺，999-其他承诺。

### ChangeReason (变动原因)

变动原因(ChangeReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1216，得到变动原因的具体描述：1-派现，2-送转股，3-配股，4-增发，5-股票价格，9-其他。

### IfImplemented (是否实施)

是否实施(IfImplemented)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否实施的具体描述：1-是，2-否。

### Reason (原因类别)

原因类别(Reason)与(CT_SystemConst)表中的DM字段关联，令LB = 1354，得到原因类别的具体描述：10-触发条件，50-期满未触发条件，53-未触发条件主动增持。

## SQL示例

```sql
-- 查询 股东承诺实施 数据
SELECT *
FROM lc_promiseimplement
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
