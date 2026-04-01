# Bond_HolderMeetingM

**中文名**: 债券持有人大会主表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_HolderMeetingM` |
| MySQL表名 | `bond_holdermeetingm` |
| 中文名 | 债券持有人大会主表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券机构信息 |
| 更新频率 | 日更新 |
| 字段数量 | 38 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录债券持有人大会的通知，变更通知，决议等信息，包含召会议召开时间，地点，召开方式，决议时间等信息。
此表一条会议进程一条记录，可根据最新公告日期获取最新的会议进展情况。
本表通过内部代码和首次会议通知公告日和债券持有人大会附表进行关联取得详细的议案信息。
2.数据范围：2015年至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InitialInfoPublDate` | 首次会议通知公告日 | date | ✗ | 100.0% |  |
| 4 | `MeetingProcess` | 会议进程 | number(10) | ✗ | 100.0% | 会议进程(MeetingProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 2202，得到... |
| 5 | `LatestInfoPublDate` | 最新公告日期 | date | ✗ | 100.0% |  |
| 6 | `InfoTitle` | 公告标题 | varchar2(200) | ✓ | 100.0% |  |
| 7 | `Year` | 年度 | number(10) | ✓ | 99.98% |  |
| 8 | `Phase` | 期次 | number(10) | ✓ | 99.97% |  |
| 9 | `RegDate` | 债权登记日 | date | ✓ | 98.94% |  |
| 10 | `RegEndDate` | 登记截止日 | date | ✓ | 84.82% |  |
| 11 | `MeetingDate` | 召开日期 | date | ✓ | 98.9% |  |
| 12 | `MeetingTimeS` | 召开起始时间 | varchar2(8) | ✓ | 66.02% |  |
| 13 | `MeetingTimeE` | 召开截止时间 | varchar2(8) | ✓ | 23.42% |  |
| 14 | `MeetingPlace` | 召开地址 | varchar2(300) | ✓ | 37.52% |  |
| 15 | `MeetingForm` | 召开方式 | number(10) | ✓ | 99.54% | 召开方式(MeetingForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到召开方... |
| 16 | `Statement` | 进展说明 | varchar2(2000) | ✓ | 22.18% |  |
| 17 | `VotingDateS` | 表决起始日期 | date | ✓ | 34.66% |  |
| 18 | `VotingDateE` | 表决截止日期 | date | ✓ | 91.71% |  |
| 19 | `VotingTimeS` | 表决起始时间 | varchar2(8) | ✓ | 7.06% |  |
| 20 | `VotingTimeE` | 表决截止时间 | varchar2(8) | ✓ | 69.86% |  |
| 21 | `NetVotingCode` | 网络投票代码 | varchar2(10) | ✓ | 0.31% |  |
| 22 | `NetVotingAbbr` | 网络投票简称 | varchar2(50) | ✓ | 0.3% |  |
| 23 | `NetSVotingDateS` | 网络投票起始日期 | date | ✓ | 0.66% |  |
| 24 | `NetSVotingDateE` | 网络投票截止日期 | date | ✓ | 0.71% |  |
| 25 | `NetSVotingTimeS` | 网络投票起始时间 | varchar2(8) | ✓ | 0.66% |  |
| 26 | `NetSVotingTimeE` | 网络投票截止时间 | varchar2(8) | ✓ | 0.7% |  |
| 27 | `InternetVotingDateS` | 互联网投票起始日期 | date | ✓ | 0.27% |  |
| 28 | `InternetVotingDateE` | 互联网投票截止日期 | date | ✓ | 0.27% |  |
| 29 | `InternetVotingTimeS` | 互联网投票起始时间 | varchar2(8) | ✓ | 0.27% |  |
| 30 | `InternetVotingTimeE` | 互联网投票截止时间 | varchar2(8) | ✓ | 0.27% |  |
| 31 | `Presider` | 主持人 | varchar2(200) | ✓ | 10.02% |  |
| 32 | `AttendNum` | 出席持有人数 | number(10) | ✓ | 41.02% |  |
| 33 | `NumOfbonds` | 代表债券(张) | number(19,2) | ✓ | 43.77% |  |
| 34 | `RatioInUnpaidCost` | 占未偿总额比例(%) | number(19,6) | ✓ | 44.59% |  |
| 35 | `TestmonyLawOffice` | 见证律师事务所 | number(10) | ✓ | 54.8% | 见证律师事务所(TestmonyLawOffice)：与“机构基本资料（LC_InstiArchive）”中的“企业编号... |
| 36 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 37 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 38 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### MeetingProcess (会议进程)

会议进程(MeetingProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 2202，得到会议进程的具体描述：10-通知，11-补充通知，12-变更通知，20-决议，30-发行人答复，99-取消。

### MeetingForm (召开方式)

召开方式(MeetingForm)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到召开方式的具体描述：1-网络投票，2-现场投票，3-网络和通讯，5-现场和网络投票，9-通讯表决，15-现场投票和通讯表决，16-现场投票、通讯表决和网络投票。

### TestmonyLawOffice (见证律师事务所)

见证律师事务所(TestmonyLawOffice)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到企业的基本信息。

## SQL示例

```sql
-- 查询 债券持有人大会主表 数据
SELECT *
FROM bond_holdermeetingm
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
