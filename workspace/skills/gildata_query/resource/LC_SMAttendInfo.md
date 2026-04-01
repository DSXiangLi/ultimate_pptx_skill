# LC_SMAttendInfo

**中文名**: 股东大会出席信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SMAttendInfo` |
| MySQL表名 | `lc_smattendinfo` |
| 中文名 | 股东大会出席信息 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 71 |
| 版本 | 1.05 |

## 表描述

1.收录股东大会召开时间，地点，类别；投票方式；见证律师事务所及经办律师；全体股东出席情况；非流通股东出席情况；流通股东出席情况。
2.数据范围：1999-1-28至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 5.28% |  |
| 5 | `MeetingDate` | 股东大会召开日 | date | ✓ | 100.0% |  |
| 6 | `SHMeetingTime` | 股东大会召开时间 | varchar2(30) | ✓ | 56.74% |  |
| 7 | `SMRegDate` | 股东大会股权登记日 | date | ✓ | 99.99% |  |
| 8 | `MeetingRegStartDate` | 会议登记起始日 | date | ✓ | 92.5% |  |
| 9 | `MeetingRegEndDate` | 会议登记截止日 | date | ✓ | 94.98% |  |
| 10 | `AnounceDate` | 股东大会公告日期 | date | ✓ | 97.52% |  |
| 11 | `ProposalContent` | 议案内容 | varchar2(2000) | ✓ | 99.3% |  |
| 12 | `CancelDate` | 股东大会取消日期 | date | ✓ | 2.26% |  |
| 13 | `Address` | 股东大会召开地址 | varchar2(100) | ✓ | 99.87% |  |
| 14 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 15 | `SerialNumber` | 序号 | number(10) | ✓ | 99.86% |  |
| 16 | `MeetingType` | 股东大会类别 | number(10) | ✗ | 100.0% | 股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND... |
| 17 | `VotingMeans` | 投票表决方式 | number(10) | ✓ | 100.0% | 投票表决方式(VotingMeans)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到投... |
| 18 | `Year` | 年度 | number(10) | ✓ | 100.0% |  |
| 19 | `Series` | 届次 | number(10) | ✓ | 68.6% |  |
| 20 | `NetVotingPlatform` | 网络投票通道 | number(10) | ✓ | 74.78% | 网络投票通道(NetVotingPlatform)与(CT_SystemConst)表中的DM字段关联，令LB = 25... |
| 21 | `NetVotingCode` | 网络投票代码 | varchar2(50) | ✓ | 78.19% |  |
| 22 | `VotingAbbr` | 投票简称 | varchar2(50) | ✓ | 68.72% |  |
| 23 | `NetVotingStartDate` | 网络投票起始日 | date | ✓ | 70.07% |  |
| 24 | `NetVotingEndDate` | 网络投票截止日 | date | ✓ | 70.08% |  |
| 25 | `Presider` | 大会主持人 | varchar2(50) | ✓ | 92.93% |  |
| 26 | `PresiderOfficialPost` | 主持人职务(多选) | number(10) | ✓ |  |  |
| 27 | `TestmonyLawOffice` | 见证律师事务所 | varchar2(200) | ✓ | 94.42% |  |
| 28 | `LawOfficeCode` | 律师事务所企业编号 | number(10) | ✓ | 62.14% | 律师事务所企业编号(LawOfficeCode)：与机构基本资料表(LC_InstiArchive)中公司代码(Comp... |
| 29 | `Lawyer` | 经办律师 | varchar2(50) | ✓ | 93.65% |  |
| 30 | `AttendanceType` | 股东出席类别 | number(10) | ✓ | 97.52% | 股东出席类别(AttendanceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1301，... |
| 31 | `AttendanceNumber` | 出席总体股东及代表人数(人) | number(10) | ✓ | 87.58% |  |
| 32 | `ASharesNumber` | #A股股东人数(人) | number(10) | ✓ | 1.16% |  |
| 33 | `HSharesNumber` | #H股股东人数(人) | number(10) | ✓ | 0.59% |  |
| 34 | `OtherSharesNumber` | #其他基础股票股东人数(人) | number(10) | ✓ | 0.7% |  |
| 35 | `ShareANumber` | #A类普通股股东人数 | number(10) | ✓ | 0.0% |  |
| 36 | `ShareBNumber` | #B类普通股股东人数 | number(10) | ✓ | 0.0% |  |
| 37 | `ShareReprensented` | 出席总体股东代表股份(股)/(票) | number(18,2) | ✓ | 87.47% |  |
| 38 | `ASharesReprensented` | #A股股东代表股份(股) | number(18,2) | ✓ | 1.23% |  |
| 39 | `HSharesReprensented` | #H股股东代表股份(股) | number(18,2) | ✓ | 0.61% |  |
| 40 | `OSharesReprensented` | #其他基础股票股东代表股份占比(%) | number(18,2) | ✓ | 0.76% |  |
| 41 | `ShareAReprensented` | #A类普通股股东代表股份(票)(以股计) | number(18,2) | ✓ | 0.0% |  |
| 42 | `ShareBReprensented` | #B类普通股股东代表股份(票)(以股计) | number(18,2) | ✓ | 0.0% |  |
| 43 | `RatioInTotalShare` | 出席总体股东股份占总股份比例(%) | number(18,8) | ✓ | 87.43% |  |
| 44 | `ASharesRatio` | #A股股东代表股份占比(%) | number(18,8) | ✓ | 1.12% |  |
| 45 | `HSharesRatio` | #H股股东代表股份占比(%) | number(18,8) | ✓ | 0.59% |  |
| 46 | `OtherSharesRatio` | #其他基础股票股东代表股份占比(%) | number(18,8) | ✓ | 0.61% |  |
| 47 | `ShareARatio` | #A类普通股股东代表股份比例(%) | number(18,8) | ✓ | 0.0% |  |
| 48 | `ShareBRatio` | #B类普通股股东代表股份比例(%) | number(18,8) | ✓ | 0.0% |  |
| 49 | `MSharesNumber` | 出席中小股东及代表人数 | number(10) | ✓ | 19.69% |  |
| 50 | `MShareReprensented` | 出席中小股东代表股份(股) | number(18,2) | ✓ | 19.77% |  |
| 51 | `MSharesRatio` | 出席中小股东股份占总股份比例(%) | number(18,8) | ✓ | 19.78% |  |
| 52 | `PSharesNumber` | 出席优先股股东及代表人数 | number(10) | ✓ | 0.0% |  |
| 53 | `PSharesReprensented` | 出席优先股股东代表股份(股) | number(18,2) | ✓ | 0.0% |  |
| 54 | `PSharesRatio` | 出席优先股股东股份占总股份比例(%) | number(18,8) | ✓ | 0.0% |  |
| 55 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 56 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 57 | `JSID` | JSID | number(19) | ✗ |  |  |
| 58 | `NTSHNumber` | 非流通股东人数(人) | number(10) | ✓ | 0.28% |  |
| 59 | `ForeignNTSHNumber` | #外资非流通股东人数(人) | number(10) | ✓ | 0.0% |  |
| 60 | `NTSHRepresentedShare` | 非流通股东代表股份(股) | number(18,2) | ✓ | 0.28% |  |
| 61 | `FNTSHRepresentedShare` | #外资非流通股东代表股份(股) | number(18,2) | ✓ | 0.0% |  |
| 62 | `TSHNumber` | 流通股东人数(人) | number(10) | ✓ | 0.41% |  |
| 63 | `ATSHNumber` | #A股股东人数(人) | number(10) | ✓ | 0.03% |  |
| 64 | `BTSHNumber` | #B股股东人数(人) | number(10) | ✓ | 0.0% |  |
| 65 | `HTSHNumber` | #H股股东人数(人) | number(10) | ✓ | 0.0% |  |
| 66 | `OtherTSHNumber` | #其他流通股东人数(人) | number(10) | ✓ | 0.0% |  |
| 67 | `TSHRepresentedShare` | 流通股东代表股份(股) | number(18,2) | ✓ | 0.41% |  |
| 68 | `ATSHRepresentedShare` | #A股股东代表股份(股) | number(18,2) | ✓ | 0.03% |  |
| 69 | `BTSHRepresentedShare` | #B股股东代表股份(股) | number(18,2) | ✓ | 0.0% |  |
| 70 | `HTSHRepresentedShare` | #H股股东代表股份(股) | number(18,2) | ✓ | 0.0% |  |
| 71 | `OtherTSHRepresentedShare` | #其他流通股东代表股份(股) | number(18,2) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

### MeetingType (股东大会类别)

股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND DM IN (1,3,5)，得到股东大会类别的具体描述：1-年度股东大会，3-临时股东大会，5-出资人组会议。

### VotingMeans (投票表决方式)

投票表决方式(VotingMeans)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到投票表决方式的具体描述：1-网络投票，2-现场投票，3-网络和通讯，5-现场和网络投票，9-通讯表决，15-现场投票和通讯表决，16-现场投票、通讯表决和网络投票。

### NetVotingPlatform (网络投票通道)

网络投票通道(NetVotingPlatform)与(CT_SystemConst)表中的DM字段关联，令LB = 2521，得到网络投票通道的具体描述：1-中国证券登记结算有限责任公司网络系统，2-上海证券交易所交易系统，3-深圳证券交易所交易系统，4-互联网投票系统，5-中国证券登记结算有限责任公司网络系统、互联网投票系统，6-上海证券交易所交易系统、互联网投票系统，7-深圳证券交易所交易系统、互联网投票系统，999-其他。

### LawOfficeCode (律师事务所企业编号)

律师事务所企业编号(LawOfficeCode)：与机构基本资料表(LC_InstiArchive)中公司代码(CompanyCode)关联，得到预测机构的具体信息。

### AttendanceType (股东出席类别)

股东出席类别(AttendanceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1301，得到股东出席类别的具体描述：1-总体出席，2-现场投票出席，3-网络投票出席。

## SQL示例

```sql
-- 查询 股东大会出席信息 数据
SELECT *
FROM lc_smattendinfo
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
