# LC_STIBSMAttendInfo

**中文名**: 科创板股东大会出席信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBSMAttendInfo` |
| MySQL表名 | `lc_stibsmattendinfo` |
| 中文名 | 科创板股东大会出席信息 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 55 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录科创版上市公司股东大会召开时间，地点，类别；投票方式；见证律师事务所及经办律师；全体股东出席情况。
2.数据范围：2019年至今
3.信息来源：临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 4.92% |  |
| 5 | `MeetingDate` | 股东大会召开日 | date | ✓ | 99.99% |  |
| 6 | `SHMeetingTime` | 股东大会召开时间 | varchar2(30) | ✓ | 99.18% |  |
| 7 | `SMRegDate` | 股东大会股权登记日 | date | ✓ | 99.99% |  |
| 8 | `MeetingRegStartDate` | 会议登记起始日 | date | ✓ | 85.37% |  |
| 9 | `MeetingRegEndDate` | 会议登记截止日 | date | ✓ | 90.91% |  |
| 10 | `SMAnnounceDate` | 股东大会公告日期 | date | ✓ | 97.52% |  |
| 11 | `ProposalContent` | 议案内容 | varchar2(2000) | ✓ | 87.51% |  |
| 12 | `CancelDate` | 股东大会取消日期 | date | ✓ | 1.93% |  |
| 13 | `Address` | 股东大会召开地址 | varchar2(100) | ✓ | 99.96% |  |
| 14 | `MeetingType` | 股东大会类别 | number(10) | ✗ | 100.0% | 股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND... |
| 15 | `Year` | 年度 | number(10) | ✓ | 100.0% |  |
| 16 | `Series` | 届次 | number(10) | ✓ | 69.84% |  |
| 17 | `VotingMeans` | 投票表决方式 | number(10) | ✓ | 100.0% | 投票表决方式(VotingMeans)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到投... |
| 18 | `NetVotingPlatform` | 网络投票通道 | number(10) | ✓ | 61.43% | 网络投票通道(NetVotingPlatform)与(CT_SystemConst)表中的DM字段关联，令LB = 25... |
| 19 | `NetVotingStartDate` | 网络投票起始日 | date | ✓ | 86.59% |  |
| 20 | `NetVotingEndDate` | 网络投票截止日 | date | ✓ | 86.59% |  |
| 21 | `SerialNumber` | 序号 | number(10) | ✓ | 99.93% |  |
| 22 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 23 | `Presider` | 大会主持人 | varchar2(50) | ✓ | 85.2% |  |
| 24 | `PresiderOfficialPost` | 主持人职务 | varchar2(100) | ✓ | 85.18% |  |
| 25 | `TestmonyLawOffice` | 见证律师事务所 | varchar2(200) | ✓ | 85.44% |  |
| 26 | `LawOfficeCode` | 律师事务所企业编号 | number(10) | ✓ | 84.77% | 律师事务所企业编号(LawOfficeCode)：与机构基本资料表(LC_InstiArchive)中公司代码(Comp... |
| 27 | `Lawyer` | 经办律师 | varchar2(50) | ✓ | 85.44% |  |
| 28 | `AttendanceType` | 股东出席类别 | number(10) | ✓ | 97.52% | 股东出席类别(AttendanceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1301，... |
| 29 | `AttendanceNumber` | 出席股东及代表人数(人) | number(10) | ✓ | 69.31% |  |
| 30 | `ASharesNumber` | #A股股东人数 | number(10) | ✓ | 0.86% |  |
| 31 | `HSharesNumber` | #H股股东人数 | number(10) | ✓ | 0.51% |  |
| 32 | `OtherSharesNumber` | #其他基础股票股东人数(人) | number(10) | ✓ | 0.16% |  |
| 33 | `ShareANumber` | #A类普通股股东人数 | number(10) | ✓ | 0.03% |  |
| 34 | `ShareBNumber` | #B类普通股股东人数 | number(10) | ✓ | 0.03% |  |
| 35 | `ShareReprensented` | 出席总体股东代表股份(股/份) | number(18,2) | ✓ | 69.28% |  |
| 36 | `ASharesReprensented` | #A股股东代表股份(股/份) | number(18,2) | ✓ | 0.87% |  |
| 37 | `HSharesReprensented` | #H股股东代表股份(股/份) | number(18,2) | ✓ | 0.51% |  |
| 38 | `OSharesReprensented` | #其他基础股票股东代表股份(股/份) | number(18,2) | ✓ | 0.16% |  |
| 39 | `ShareAReprensented` | #A类普通股股东代表股份(票)(以股/份计) | number(18,2) | ✓ | 0.07% |  |
| 40 | `ShareBReprensented` | #B类普通股股东代表股份(票)(以股/份计) | number(18,2) | ✓ | 0.07% |  |
| 41 | `RatioInTotalShare` | 出席总体股东股份占总股份比例(%) | number(18,8) | ✓ | 69.28% |  |
| 42 | `ASharesRatio` | #A股股东代表股份占比(%) | number(18,8) | ✓ | 0.87% |  |
| 43 | `HSharesRatio` | #H股股东代表股份占比(%) | number(18,8) | ✓ | 0.51% |  |
| 44 | `OtherSharesRatio` | #其他股东代表股份占比(%) | number(18,8) | ✓ | 0.16% |  |
| 45 | `ShareARatio` | #A类普通股股东代表股份比例(%) | number(18,8) | ✓ | 0.07% |  |
| 46 | `ShareBRatio` | #B类普通股股东代表股份比例(%) | number(18,8) | ✓ | 0.07% |  |
| 47 | `MSharesNumber` | 出席中小股东及代表人数 | number(10) | ✓ | 8.08% |  |
| 48 | `MShareReprensented` | 出席中小股东代表股份(股/份) | number(18,2) | ✓ | 8.4% |  |
| 49 | `MSharesRatio` | 出席中小股东股份占总股份比例(%) | number(18,8) | ✓ | 8.4% |  |
| 50 | `PSharesNumber` | 出席优先股股东及代表人数 | number(10) | ✓ | 0.0% |  |
| 51 | `PSharesReprensented` | 出席优先股股东代表股份(股/份) | number(18,2) | ✓ | 0.0% |  |
| 52 | `PSharesRatio` | 出席优先股股东股份占总股份比例(%) | number(18,8) | ✓ | 0.0% |  |
| 53 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 54 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 55 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### MeetingType (股东大会类别)

股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND DM IN (1,3,5)，得到股东大会类别的具体描述：1-年度股东大会，3-临时股东大会，5-出资人组会议。

### VotingMeans (投票表决方式)

投票表决方式(VotingMeans)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到投票表决方式的具体描述：1-网络投票，2-现场投票，3-网络和通讯，5-现场和网络投票，9-通讯表决，15-现场投票和通讯表决，16-现场投票、通讯表决和网络投票。

### NetVotingPlatform (网络投票通道)

网络投票通道(NetVotingPlatform)与(CT_SystemConst)表中的DM字段关联，令LB = 2521，得到网络投票通道的具体描述：1-中国证券登记结算有限责任公司网络系统，2-上海证券交易所交易系统，3-深圳证券交易所交易系统，4-互联网投票系统，5-中国证券登记结算有限责任公司网络系统、互联网投票系统，6-上海证券交易所交易系统、互联网投票系统，7-深圳证券交易所交易系统、互联网投票系统，999-其他。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

### LawOfficeCode (律师事务所企业编号)

律师事务所企业编号(LawOfficeCode)：与机构基本资料表(LC_InstiArchive)中公司代码(CompanyCode)关联，得到预测机构的具体信息。

### AttendanceType (股东出席类别)

股东出席类别(AttendanceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1301，得到股东出席类别的具体描述：1-总体出席，2-现场投票出席，3-网络投票出席。

## SQL示例

```sql
-- 查询 科创板股东大会出席信息 数据
SELECT *
FROM lc_stibsmattendinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
