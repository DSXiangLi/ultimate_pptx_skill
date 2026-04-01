# MF_FundHolderMeeting

**中文名**: 公募基金持有人大会

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundHolderMeeting` |
| MySQL表名 | `mf_fundholdermeeting` |
| 中文名 | 公募基金持有人大会 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 不定期更新 |
| 字段数量 | 46 |
| 版本 | 1.05 |

## 表描述

1.本表记录公募基金持有人大会基本情况介绍，包括召开方式、召开地点、大会议题、决议结果等等。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司发布的临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `NoticeDate` | 首次会议通知公告日 | date | ✗ | 100.0% |  |
| 5 | `MeetingProcess` | 会议进程 | number(10) | ✓ | 100.0% | 会议进程(MeetingProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 2202，得到... |
| 6 | `InfoTitle` | 公告标题 | varchar2(200) | ✓ | 100.0% |  |
| 7 | `LatestInfoPublDate` | 最新公告日期 | date | ✓ | 100.0% |  |
| 8 | `Year` | 年度 | number(10) | ✓ | 100.0% |  |
| 9 | `Frequency` | 次数 | number(10) | ✓ | 100.0% |  |
| 10 | `MeetingForm` | 召开方式 | number(10) | ✗ | 100.0% | 召开方式(MeetingForm)与(CT_SystemConst)表中的DM字段关联，令LB = 2116，得到召开方... |
| 11 | `MeetingPlace` | 召开地点 | varchar2(100) | ✓ | 2.41% |  |
| 12 | `NumOfFunds` | 代表基金份额 | number(19,2) | ✓ | 46.96% |  |
| 13 | `RatioInTotalShares` | 占基金总份额比例(%) | number(10,6) | ✓ | 47.01% |  |
| 14 | `Results` | 决议结果 | varchar2(2000) | ✓ | 49.13% |  |
| 15 | `IfEffected` | 是否有效 | number(10) | ✓ | 49.06% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 16 | `ReDate` | 权益登记日 | date | ✓ | 100.0% |  |
| 17 | `PreRegSDate` | 预登记时间起始日 | date | ✓ | 1.99% |  |
| 18 | `PreRegEDate` | 预登记时间截止日 | date | ✓ | 1.99% |  |
| 19 | `MeetingTimeSD` | 召开时间起始日 | date | ✓ | 2.41% |  |
| 20 | `MeetingTimeED` | 召开时间截止日 | date | ✓ | 2.33% |  |
| 21 | `MeetingTimeS` | 召开起始时间 | varchar2(8) | ✓ | 1.71% |  |
| 22 | `MeetingTimeE` | 召开截止时间 | varchar2(8) | ✓ | 0.04% |  |
| 23 | `VotingTimeSD` | 投票起始日 | date | ✓ | 97.58% |  |
| 24 | `VotingTimeED` | 投票截止日 | date | ✓ | 97.59% |  |
| 25 | `VotingTimeS` | 投票起始时间 | varchar2(8) | ✓ | 97.43% |  |
| 26 | `VotingTimeE` | 投票截止时间 | varchar2(8) | ✓ | 97.31% |  |
| 27 | `SuspensionSD` | 连续停牌起始日 | date | ✓ | 10.46% |  |
| 28 | `SuspensionED` | 连续停牌截止日 | date | ✓ | 5.72% |  |
| 29 | `ResultsBD` | 决议公告日 | date | ✓ | 49.06% |  |
| 30 | `Convener` | 召集人 | varchar2(200) | ✓ | 99.55% |  |
| 31 | `ConvenerCode` | 召集人编码 | number(10) | ✓ | 99.55% |  |
| 32 | `Superviser` | 监督人 | varchar2(200) | ✓ | 98.61% |  |
| 33 | `SuperviserCode` | 监督人编码 | number(10) | ✓ | 98.61% |  |
| 34 | `NotaryOffice` | 公证机构 | varchar2(200) | ✓ | 99.51% |  |
| 35 | `NotaryOfficeCode` | 公证机构编码 | number(10) | ✓ | 99.51% |  |
| 36 | `TestmonyLawOffice` | 见证律师事务所 | varchar2(200) | ✓ | 99.34% |  |
| 37 | `TestmonyLawOfficeCode` | 见证律师事务所编码 | number(10) | ✓ | 99.34% |  |
| 38 | `Remark` | 备注 | varchar2(2000) | ✓ | 29.86% |  |
| 39 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 40 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 41 | `JSID` | JSID | number(19) | ✗ |  |  |
| 42 | `MeetingTopic` | 大会议题 | varchar2(100) | ✓ | 0.0% | 注：本表该字段废弃，可根据NoticeDate和InnerCode关联附表【MF_FundHolderMeetingA】... |
| 43 | `NotaryFee` | 公证费用(元) | number(19,2) | ✓ | 39.62% |  |
| 44 | `AttorneyFee` | 律师费用(元) | number(19,2) | ✓ | 39.46% |  |
| 45 | `TotalFee` | 总费用(元) | number(19,2) | ✓ | 39.02% |  |
| 46 | `VotingMethod` | 大会投票方式 | varchar2(200) | ✓ | 100.0% |  |

## 字段说明

### InnerCode (基金代码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### MeetingProcess (会议进程)

会议进程(MeetingProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 2202，得到会议进程的具体描述：10-通知，11-补充通知，12-变更通知，20-决议，30-发行人答复，99-取消。

### MeetingForm (召开方式)

召开方式(MeetingForm)与(CT_SystemConst)表中的DM字段关联，令LB = 2116，得到召开方式的具体描述：10-现场方式，20-通讯方式，30-其他方式。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

### MeetingTopic (大会议题)

注：本表该字段废弃，可根据NoticeDate和InnerCode关联附表【MF_FundHolderMeetingA】，获取大会议题数据

## SQL示例

```sql
-- 查询 公募基金持有人大会 数据
SELECT *
FROM mf_fundholdermeeting
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
