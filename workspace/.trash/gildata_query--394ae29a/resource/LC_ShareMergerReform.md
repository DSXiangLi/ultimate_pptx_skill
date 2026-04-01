# LC_ShareMergerReform

**中文名**: 股权分置

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ShareMergerReform` |
| MySQL表名 | `lc_sharemergerreform` |
| 中文名 | 股权分置 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 73 |
| 版本 | 1 |

## 表描述

1.收录上市公司股权分置改革中日期进程以及方案实施前后股本结构对比，包括事件进程、方案类型、保荐机构、董事会决议公布日、股东大会决议公布日、获批日、改革方案实施公告日、股权登记日、实施后交易首日、对价股票支付日等指标。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `Process` | 事件进程 | number(10) | ✓ | 100.0% | 事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体... |
| 6 | `EventAnnounceDate` | 改革事项公告日期 | date | ✓ | 99.86% |  |
| 7 | `PrimaryIntention` | 股权分置改革初步意向 | varchar2(500) | ✓ | 95.45% |  |
| 8 | `ProgramType` | 方案类型 | number(10) | ✓ |  |  |
| 9 | `ContactTel` | 联系电话 | varchar2(50) | ✓ | 97.59% |  |
| 10 | `Fax` | 传真 | varchar2(50) | ✓ | 97.52% |  |
| 11 | `Email` | 电子邮箱 | varchar2(50) | ✓ | 96.97% |  |
| 12 | `ContactMan` | 联系人 | varchar2(50) | ✓ | 60.99% |  |
| 13 | `Sponsor` | 保荐机构 | varchar2(200) | ✓ | 97.59% |  |
| 14 | `CompanyNumber` | 企业编号 | number(10) | ✓ |  |  |
| 15 | `SponsorHolding` | 保荐机构持股 | number(18,2) | ✓ | 95.18% |  |
| 16 | `DMDate` | 董事会审议改革方案日 | date | ✓ | 0.34% |  |
| 17 | `DMDAnnounceDate` | 董事会决议公布日 | date | ✓ | 97.59% |  |
| 18 | `OnlineVotingStartDate` | 网络投票起始日 | date | ✓ | 0.34% |  |
| 19 | `OnlineVotingEndDate` | 网络投票截至日 | date | ✓ | 0.34% |  |
| 20 | `SMRecordDate` | 股东大会登记日 | date | ✓ | 96.76% |  |
| 21 | `SMDate` | 股东大会召开日 | date | ✓ | 96.62% |  |
| 22 | `SMAddress` | 股东大会召开地址 | varchar2(100) | ✓ | 96.83% |  |
| 23 | `VoterCollector` | 投票权征集人 | varchar2(100) | ✓ | 95.66% |  |
| 24 | `ProgramPrePublDate` | 沟通确认方案公布日 | date | ✓ | 93.94% |  |
| 25 | `AdjustmentType` | 方案调整类别 | number(10) | ✓ | 93.94% | 方案调整类别(AdjustmentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1369，... |
| 26 | `IDCollectStartDate` | 独立董事征集投票权起始日 | date | ✓ | 0.34% |  |
| 27 | `IDCollectEndDate` | 独立董事征集投票权截至日 | date | ✓ | 0.34% |  |
| 28 | `Authorizingdept` | 方案实施上级批准部门 | varchar2(100) | ✓ | 74.57% |  |
| 29 | `IfAuthorized` | 是否获批 | number(10) | ✓ | 72.43% | 是否获批（IfAuthorized），该字段固定以下常量：0-否；1-是 |
| 30 | `IfFCLPShareAuthorized` | 外资法人股是否获批 | number(10) | ✓ | 3.03% | 外资法人股是否获批（IfFCLPShareAuthorized），该字段固定以下常量：0-否；1-是 |
| 31 | `AuthorizedDate` | 获批日 | date | ✓ | 73.05% |  |
| 32 | `SMDAnnounceDate` | 股东大会决议公布日 | date | ✓ | 96.49% |  |
| 33 | `IfPassed` | 改革方案是否通过 | number(10) | ✓ | 96.49% | 改革方案是否通过（IfPassed），该字段固定以下常量：0-否；1-是 |
| 34 | `ImplementionAnnouceDate` | 改革方案实施公告日期 | date | ✓ | 92.07% |  |
| 35 | `ImplementionRecordDate` | 方案实施的股权登记日 | date | ✓ | 92.07% |  |
| 36 | `SuspendDate` | 实施后停牌日 | date | ✓ | 28.53% |  |
| 37 | `RecoverTradinDate` | 实施后交易首日 | date | ✓ | 91.66% |  |
| 38 | `SConsiderationPayDate` | 对价股票支付日 | date | ✓ | 30.88% |  |
| 39 | `SConsiderationListDate` | 对价股票上市流通日 | date | ✓ | 89.25% |  |
| 40 | `CConsiderationPayDate` | 对价现金发放日 | date | ✓ | 4.69% |  |
| 41 | `WarrantIssueDate` | 权证发行日 | date | ✓ | 0.07% |  |
| 42 | `BaseShareCapital` | 基准股本 | number(18,2) | ✓ | 97.59% |  |
| 43 | `NTShareBR` | 1)非流通股 | number(18,2) | ✓ | 97.59% |  |
| 44 | `NTTermEShare` | ##限期上市职工股 | number(18,2) | ✓ | 0.76% |  |
| 45 | `NTEShare` | ##暂不上市职工股 | number(18,2) | ✓ | 0.34% |  |
| 46 | `FCLPShareBR` | ##外资法人股 | number(18,2) | ✓ | 4.14% |  |
| 47 | `TShareBR` | 2)流通股 | number(18,2) | ✓ | 97.59% |  |
| 48 | `TAShareBR` | ##流通A股 | number(18,2) | ✓ | 97.52% |  |
| 49 | `BShareBR` | ##B股 | number(18,2) | ✓ | 6.34% |  |
| 50 | `HShareBR` | ##H股 | number(18,2) | ✓ | 2.27% |  |
| 51 | `OTShareBR` | ##其他流通股 | number(18,2) | ✓ | 0.21% |  |
| 52 | `TotalShareAR` | 方案实施后总股本 | number(18,2) | ✓ | 97.38% |  |
| 53 | `RestrainedTShare` | 1)有限售条件流通股 | number(18,2) | ✓ | 97.38% |  |
| 54 | `RTTermEShare` | ##限期上市职工股 | number(18,2) | ✓ | 0.48% |  |
| 55 | `RTEShare` | ##暂不上市职工股 | number(18,2) | ✓ | 0.28% |  |
| 56 | `RTFCLPShare` | ##外资法人股 | number(18,2) | ✓ | 4.2% |  |
| 57 | `UnstintedTShare` | 2)无限售条件流通股 | number(18,2) | ✓ | 97.38% |  |
| 58 | `TAShareAR` | ##流通A股 | number(18,2) | ✓ | 97.24% |  |
| 59 | `BShareAR` | ##B股 | number(18,2) | ✓ | 6.34% |  |
| 60 | `HShareAR` | ##H股 | number(18,2) | ✓ | 2.27% |  |
| 61 | `OTShareAR` | ##其他流通股 | number(18,2) | ✓ | 0.21% |  |
| 62 | `TotalSharePaid` | 1)公司合计送转股数 | number(18,2) | ✓ | 22.54% |  |
| 63 | `TotalCashPaid` | 公司合计派现金额 | number(19,4) | ✓ | 2.27% |  |
| 64 | `TotalWarrant` | 公司合计认股证份数 | number(18,2) | ✓ | 0.14% |  |
| 65 | `SConsideration` | 2)非流通股东对价股份总额 | number(18,2) | ✓ | 73.81% |  |
| 66 | `CConsideration` | 非流通股东对价现金总额 | number(19,4) | ✓ | 4.27% |  |
| 67 | `Wconsideration` | 非流通股东对价认股证总额 | number(18,2) | ✓ | 2.0% |  |
| 68 | `ShareCompressed` | 3)非流通股东缩股总额 | number(18,2) | ✓ | 0.96% |  |
| 69 | `SubsidiaryProgram` | 上市公司配套方案 | number(10) | ✓ | 8.75% | 上市公司配套方案(SubsidiaryProgram)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 70 | `SPStatement` | 配套方案说明 | varchar2(1000) | ✓ | 10.54% |  |
| 71 | `Note` | 备注 | varchar2(500) | ✓ | 2.69% |  |
| 72 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 73 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### Process (事件进程)

事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-涉诉，1053-可能涉诉，1055-预估，1303-收到，1305-部分收到，2001-逾期，2003-还款，2005-延期，2007-展期，2501-诉前，2504-诉中，2507-诉后，3001-提前回收，3002-提前部分回收，3003-到期后协议延期，3004-到期回收，3005-到期待回收，3006-到期部分待回收，3007-到期无法回收，3008-到期部分无法回收，3101-改革意向，3103-股改动议取消，3105-董事会改革方案，3108-沟通确认方案，3111-上级部门批准，3115-上级部门驳回，3120-董事会否决，3121-股东大会通过，3125-股东大会否决，3126-有效期内未实施，3131-方案实施，3201-证监会审核通过，3202-证监会审核否决，3203-证监会核准，3204-证监会未核准，3205-并购重组委核准，3206-并购重组委否决，3212-方案部分实施，3301-已注册未发行，3302-已发行有额度，3303-已发行无额度，3304-提前终止，3305-放弃，3306-暂停实施，3399-其他。

### AdjustmentType (方案调整类别)

方案调整类别(AdjustmentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1369，得到方案调整类别的具体描述：2-不调整，11-对价方案调整，13-股东承诺调整，17-对价与承诺调整。

### IfAuthorized (是否获批)

是否获批（IfAuthorized），该字段固定以下常量：0-否；1-是

### IfFCLPShareAuthorized (外资法人股是否获批)

外资法人股是否获批（IfFCLPShareAuthorized），该字段固定以下常量：0-否；1-是

### IfPassed (改革方案是否通过)

改革方案是否通过（IfPassed），该字段固定以下常量：0-否；1-是

### SubsidiaryProgram (上市公司配套方案)

上市公司配套方案(SubsidiaryProgram)与(CT_SystemConst)表中的DM字段关联，令LB = 1308，得到上市公司配套方案的具体描述：101-回购流通股，105-定向回购，201-发行认股证，301-资产重组。

## SQL示例

```sql
-- 查询 股权分置 数据
SELECT *
FROM lc_sharemergerreform
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
