# Bond_ConBDIssueProject

**中文名**: 可转债发行预案

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDIssueProject` |
| MySQL表名 | `bond_conbdissueproject` |
| 中文名 | 可转债发行预案 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 32 |
| 版本 | 1.04 |

## 表描述

1.该表包含上市公司发行可转换债券的发行预案信息。
2.该表收录了所有可转换债券的发行预案信息，其中尚未实施的预案可以通过“实施与否”字段进行判断。
3.数据范围：1991-08-11 至今
4.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 可转债内部编码 | number(10) | ✓ | 60.94% | 可转债内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，... |
| 3 | `StockInnerCode` | 正股内部编码 | number(10) | ✓ | 100.0% | 正股内部编码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `CompanyCode` | 公司代码(发债公司内部编码) | number(10) | ✓ | 100.0% | 公司代码(发债公司内部编码)（CompanyCode）：与“公司概况（LC_StockArchives）”中的“公司代码... |
| 5 | `Issuer` | 发行人 | varchar2(200) | ✗ | 100.0% |  |
| 6 | `SecuCode` | 股票代码 | varchar2(10) | ✓ | 100.0% |  |
| 7 | `SecuAbbr` | 股票简称 | varchar2(100) | ✓ | 100.0% |  |
| 8 | `CBCode` | 可转债代码 | varchar2(10) | ✓ | 60.94% |  |
| 9 | `CBAbbr` | 可转债简称 | varchar2(100) | ✓ | 60.94% |  |
| 10 | `CBType` | 可转债性质 | number(10) | ✓ | 100.0% | 可转债性质(CBType)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到可转债性质的具... |
| 11 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 12 | `EventProcedure` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 an... |
| 13 | `AdvanceDate` | 预案公告日期 | date | ✓ | 99.67% |  |
| 14 | `ValidStartDate` | 预案有效期起始日 | date | ✓ | 94.4% |  |
| 15 | `ValidEndDate` | 预案有效期截止日 | date | ✓ | 93.74% |  |
| 16 | `SMDeciPublDate` | 股东大会决议公告日期 | date | ✓ | 94.63% |  |
| 17 | `CSRCIACApprovalDate` | 交易所上市审核委员会审核日期 | date | ✓ | 62.27% | 实行注册制之前，该字段代表证监会发审委审核日期 |
| 18 | `CSRCApprovalDate` | 证监会注册日期 | date | ✓ | 61.16% | 实行注册制之前，该字段代表证监会核准发行日期 |
| 19 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 99.89% |  |
| 20 | `Maturity` | 债券期限(年) | number(9,6) | ✓ | 91.36% |  |
| 21 | `LowerLimit` | 计划发行规模下限(不少于)(百万元) | number(19,4) | ✓ | 6.76% |  |
| 22 | `UpperLimit` | 计划发行规模上限(不多于)(百万元) | number(19,4) | ✓ | 97.06% |  |
| 23 | `CompoundMethod` | 计息方式 | number(10) | ✓ | 8.64% | 计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AN... |
| 24 | `IntPaymentMethod` | 付息方式 | number(10) | ✓ | 94.29% | 付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，... |
| 25 | `IssueMethod` | 发行方式 | varchar2(500) | ✓ | 93.85% |  |
| 26 | `LeadUnderwriter` | 主承销商 | varchar2(1000) | ✓ | 1.22% |  |
| 27 | `ProjAlteType` | 预案变动类型 | number(10) | ✓ | 6.54% | 预案变动类型(ProjAlteType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 an... |
| 28 | `ProjAlteRemark` | 预案变动说明 | varchar2(500) | ✓ | 6.54% |  |
| 29 | `IfImplemented` | 实施与否 | number(10) | ✓ | 100.0% | 实施与否(IfImplemented)：该字段固定以下常量：1-已实施，0-未实施。 |
| 30 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 31 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 32 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (可转债内部编码)

可转债内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### StockInnerCode (正股内部编码)

正股内部编码（StockInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到可转债对应正股的交易代码、股票简称等。

### CompanyCode (公司代码(发债公司内部编码))

公司代码(发债公司内部编码)（CompanyCode）：与“公司概况（LC_StockArchives）”中的“公司代码（CompanyCode）”关联，得到发债公司的交易代码、简称等。

### CBType (可转债性质)

可转债性质(CBType)与(CT_SystemConst)表中的DM字段关联，令LB = 1413，得到可转债性质的具体描述：1-常规债券，2-分离交易可转债，3-本息分离交易债券，4-可交换公司债券。

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 and DM in (1001,1016,1022,3121,3125,3201,3202,3203,3204,3212)，得到事件进程的具体描述：1001-预案，1016-未实施终止，1022-实施完成，3121-股东大会通过，3125-股东大会否决，3201-证监会审核通过，3202-证监会审核否决，3203-证监会核准，3204-证监会未核准，3212-方案部分实施。

### CSRCIACApprovalDate (交易所上市审核委员会审核日期)

实行注册制之前，该字段代表证监会发审委审核日期

### CSRCApprovalDate (证监会注册日期)

实行注册制之前，该字段代表证监会核准发行日期

### CompoundMethod (计息方式)

计息方式(CompoundMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1213 AND DM in (1,3,4,5,6)，得到计息方式的具体描述：1-单利(固定利率)，3-浮动利率，4-累进利率，5-贴现，6-无序利率。

### IntPaymentMethod (付息方式)

付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，得到付息方式的具体描述：1-每年付息，2-半年付息，3-到期一次还本付息，4-按季付息，5-按月付息。

### ProjAlteType (预案变动类型)

预案变动类型(ProjAlteType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194 and DM in (11,12,13,19)，得到预案变动类型的具体描述：11-更改发行规模，12-延长有效期，13-其他，19-宣布发行不成功。

## SQL示例

```sql
-- 查询 可转债发行预案 数据
SELECT *
FROM bond_conbdissueproject
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
