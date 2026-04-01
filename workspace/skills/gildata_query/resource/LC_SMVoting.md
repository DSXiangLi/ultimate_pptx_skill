# LC_SMVoting

**中文名**: 股东大会表决

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SMVoting` |
| MySQL表名 | `lc_smvoting` |
| 中文名 | 股东大会表决 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 104 |
| 版本 | 1.03 |

## 表描述

1.收录股东大会议案、普通股全部股东表决情况、普通股中小股东表决情况、优先股股东表决情况、非流通股东表决情况、流通股东表决情况等。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `MeetingType` | 股东大会类别 | number(10) | ✓ | 100.0% | 股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND... |
| 6 | `Series` | 届次 | number(10) | ✓ | 51.51% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✓ | 99.99% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 8 | `TitleSN` | 议案大标题序号 | number(10) | ✓ | 100.0% |  |
| 9 | `Title` | 议案大标题 | varchar2(200) | ✓ | 100.0% |  |
| 10 | `SubtitleSN` | 议案小标题序号 | number(10) | ✓ | 29.54% |  |
| 11 | `Subtitle` | 议案小标题 | varchar2(200) | ✓ | 29.54% |  |
| 12 | `IfConnectedTransaction` | 是否关联交易 | number(10) | ✓ | 99.84% | 是否关联交易（IfConnectedTransaction），该字段固定以下常量：0-否；1-是 |
| 13 | `ProposalType` | 议案类别 | number(10) | ✓ | 99.94% | 议案类别(ProposalType)与(CT_SystemConst)表中的DM字段关联，令LB = 1303，得到议案... |
| 14 | `VotingType` | 议案投票类型 | number(10) | ✓ | 99.8% | 议案投票类型(VotingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2219，得到议案... |
| 15 | `IfPassed` | 是否通过 | number(10) | ✓ | 97.96% | 是否通过(IfPassed)，该字段固定以下常量：0-否；1-是 |
| 16 | `SharesAvoiding` | 回避表决股数(票)(以股计) | number(18,2) | ✓ | 9.34% |  |
| 17 | `VotesAvoiding` | 回避表决股份(票)(以份计) | number(18,2) | ✓ | 0.0% |  |
| 18 | `SharesApprovedASH` | 同意股数(股) | number(18,2) | ✓ | 73.64% |  |
| 19 | `ASharesApprovedASH` | #A股同意股数(股) | number(18,2) | ✓ | 27.33% |  |
| 20 | `HSharesApprovedASH` | #H股同意股数(股) | number(18,2) | ✓ | 2.31% |  |
| 21 | `OSharesApprovedASH` | #其他基础股票股东同意股数(股) | number(18,2) | ✓ | 1.28% |  |
| 22 | `ShareAApprovedASH` | #A类普通股股东同意股份(票)(以股计) | number(18,2) | ✓ | 0.01% |  |
| 23 | `ShareBApprovedASH` | #B类普通股股东同意股份(票)(以股计) | number(18,2) | ✓ | 0.01% |  |
| 24 | `RatioApprovedASH` | 同意所占比率(%) | number(18,8) | ✓ | 72.79% |  |
| 25 | `RatioApprovedAASH` | #A股同意所占比率(%) | number(18,8) | ✓ | 27.31% |  |
| 26 | `RatioApprovedHASH` | #H股同意所占比率(%) | number(18,8) | ✓ | 2.3% |  |
| 27 | `RatioApprovedOASH` | #其他基础股票股东同意所占比率(%) | number(18,8) | ✓ | 1.27% |  |
| 28 | `RatioApprovedASHA` | #A类普通股股东同意所占比率(%) | number(18,8) | ✓ | 0.02% |  |
| 29 | `RatioApprovedASHB` | #B类普通股股东同意所占比率(%) | number(18,8) | ✓ | 0.02% |  |
| 30 | `SharesOpposedASH` | 反对股数(股) | number(18,2) | ✓ | 60.49% |  |
| 31 | `ASharesOpposedASH` | #A股反对股数(股) | number(18,2) | ✓ | 27.16% |  |
| 32 | `HSharesOpposedASH` | #H股反对股数(股) | number(18,2) | ✓ | 2.22% |  |
| 33 | `OSharesOpposedASH` | #其他基础股票股东反对股数(股) | number(18,2) | ✓ | 1.2% |  |
| 34 | `ShareAOpposedASH` | #A类普通股股东反对股份(票)(以股计) | number(18,2) | ✓ | 0.02% |  |
| 35 | `ShareBOpposedASH` | #B类普通股股东反对股份(票)(以股计) | number(18,2) | ✓ | 0.02% |  |
| 36 | `RatioOpposedASH` | 反对所占比率(%) | number(18,8) | ✓ | 59.91% |  |
| 37 | `RatioOpposedAASH` | #A股反对所占比率(%) | number(18,8) | ✓ | 27.11% |  |
| 38 | `RatioOpposedHASH` | #H股反对所占比率(%) | number(18,8) | ✓ | 2.2% |  |
| 39 | `RatioOpposedOASH` | #其他基础股东股东反对所占比率(%) | number(18,8) | ✓ | 1.18% |  |
| 40 | `RatioOpposedASHA` | #A类普通股股东反对所占比率(%) | number(18,8) | ✓ | 0.01% |  |
| 41 | `RatioOpposedASHB` | #B类普通股股东反对所占比率(%) | number(18,8) | ✓ | 0.01% |  |
| 42 | `SharesDisclaimedASH` | 弃权股数(股) | number(18,2) | ✓ | 60.42% |  |
| 43 | `ASharesDisclaimedASH` | #A股弃权股数(股) | number(18,2) | ✓ | 27.07% |  |
| 44 | `HSharesDisclaimedASH` | #H股弃权股数(股) | number(18,2) | ✓ | 2.18% |  |
| 45 | `OSharesDisclaimedASH` | #其他基础股票股东弃权股数(股) | number(18,2) | ✓ | 1.19% |  |
| 46 | `ShareADisclaimedASH` | #A类普通股股东弃权股份(票)(以股计) | number(18,2) | ✓ | 0.01% |  |
| 47 | `ShareBDisclaimedASH` | #B类普通股股东弃权股份(票)(以股计) | number(18,2) | ✓ | 0.01% |  |
| 48 | `RatioDisclaimedASH` | 弃权所占比率(%) | number(18,8) | ✓ | 59.21% |  |
| 49 | `RatioDisclaimedAASH` | #A股弃权所占比率(%) | number(18,8) | ✓ | 26.94% |  |
| 50 | `RatioDisclaimedHASH` | #H股弃权所占比率(%) | number(18,8) | ✓ | 2.11% |  |
| 51 | `RatioDisclaimedOASH` | #其他基础股票股东弃权所占比率(%) | number(18,8) | ✓ | 1.15% |  |
| 52 | `RatioDisclaimedASHA` | #A类普通股股东弃权所占比率(%) | number(18,8) | ✓ | 0.02% |  |
| 53 | `RatioDisclaimedASHB` | #B类普通股股东弃权所占比率(%) | number(18,8) | ✓ | 0.02% |  |
| 54 | `VotesApprovedASH` | 同意股份(票)(以份计) | number(18,2) | ✓ | 0.0% |  |
| 55 | `VoteAApprovedASH` | #A类普通股股东同意股份(票)(以份计) | number(18,2) | ✓ | 0.0% |  |
| 56 | `VoteBApprovedASH` | #B类普通股股东同意股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 57 | `VotesOpposedASH` | 反对股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 58 | `VoteAOpposedASH` | #A类普通股股东反对股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 59 | `VoteBOpposedASH` | #B类普通股股东反对股份(票)(以份计) | number(18,2) | ✓ | 0.0% |  |
| 60 | `VotesDisclaimedASH` | 弃权股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 61 | `VoteADisclaimedASH` | #A类普通股股东弃权股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 62 | `VoteBDisclaimedASH` | #B类普通股股东弃权股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 63 | `SharesApprovedMSH` | 同意股数(票)(以股计) | number(18,2) | ✓ | 73.95% |  |
| 64 | `VotesApprovedMSH` | 同意股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 65 | `RatioApprovedMSH` | 同意所占比率(%) | number(18,8) | ✓ | 72.73% |  |
| 66 | `SharesOpposedMSH` | 反对股数(票)(以股计) | number(18,2) | ✓ | 62.16% |  |
| 67 | `VotesOpposedMSH` | 反对股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 68 | `RatioOpposedMSH` | 反对所占比率(%) | number(18,8) | ✓ | 61.51% |  |
| 69 | `SharesDisclaimedMSH` | 弃权股数(票)(以股计) | number(18,2) | ✓ | 62.1% |  |
| 70 | `VotesDisclaimedMSH` | 弃权股份(票)(以份计) | number(18,2) | ✓ | 0.01% |  |
| 71 | `RatioDisclaimedMSH` | 弃权所占比率(%) | number(18,8) | ✓ | 60.9% |  |
| 72 | `SharesApprovedPSH` | 同意股数(股) | number(18,2) | ✓ | 0.01% |  |
| 73 | `RatioApprovedPSH` | 同意所占比率(%) | number(18,8) | ✓ | 0.0% |  |
| 74 | `SharesOpposedPSH` | 反对股数(股) | number(18,2) | ✓ | 0.0% |  |
| 75 | `RatioOpposedPSH` | 反对所占比率(%) | number(18,8) | ✓ | 0.0% |  |
| 76 | `SharesDisclaimedPSH` | 弃权股数(股) | number(18,2) | ✓ | 0.0% |  |
| 77 | `RatioDisclaimedPSH` | 弃权所占比率(%) | number(18,8) | ✓ | 0.0% |  |
| 78 | `SharesApprovedNTSH` | 同意股数(股) | number(18,2) | ✓ | 0.21% |  |
| 79 | `RatioApprovedNTSH` | 同意所占比率(%) | number(18,8) | ✓ | 0.21% |  |
| 80 | `SharesOpposedNTSH` | 反对股数(股) | number(18,2) | ✓ | 0.07% |  |
| 81 | `RatioOpposedNTSH` | 反对所占比率(%) | number(18,8) | ✓ | 0.06% |  |
| 82 | `SharesDisclaimedNTSH` | 弃权股数(股) | number(18,2) | ✓ | 0.07% |  |
| 83 | `RatioDisclaimedNTSH` | 弃权所占比率(%) | number(18,8) | ✓ | 0.06% |  |
| 84 | `SharesApprovedTSH` | 同意股数(股) | number(18,2) | ✓ | 0.21% |  |
| 85 | `RatioApprovedTSH` | 同意所占比率(%) | number(18,8) | ✓ | 0.21% |  |
| 86 | `ASharesApprovedTSH` | #A股同意股数(股) | number(18,2) | ✓ | 0.02% |  |
| 87 | `BSharesApprovedTSH` | #B股同意股数(股) | number(18,2) | ✓ | 0.0% |  |
| 88 | `HSharesApprovedTSH` | #H股同意股数(股) | number(18,2) | ✓ | 0.0% |  |
| 89 | `OSharesApprovedTSH` | #其他流通股东同意股数(股) | number(18,2) | ✓ | 0.0% |  |
| 90 | `SharesOpposedTSH` | 反对股数(股) | number(18,2) | ✓ | 0.21% |  |
| 91 | `RatioOpposedTSH` | 反对所占比率(%) | number(18,8) | ✓ | 0.21% |  |
| 92 | `ASharesOpposedTSH` | #A股反对股数(股) | number(18,2) | ✓ | 0.02% |  |
| 93 | `BSharesOpposedTSH` | #B股反对股数(股) | number(18,2) | ✓ | 0.0% |  |
| 94 | `HSharesOpposedTSH` | #H股反对股数(股) | number(18,2) | ✓ | 0.0% |  |
| 95 | `OSharesOpposedTSH` | #其他流通股东反对股数(股) | number(18,2) | ✓ | 0.0% |  |
| 96 | `SharesDisclaimedTSH` | 弃权股数(股) | number(18,2) | ✓ | 0.21% |  |
| 97 | `RatioDisclaimedTSH` | 弃权所占比率(%) | number(18,8) | ✓ | 0.21% |  |
| 98 | `ASharesDisclaimedTSH` | #A股弃权股数(股) | number(18,2) | ✓ | 0.02% |  |
| 99 | `BSharesDisclaimedTSH` | #B股弃权股数(股) | number(18,2) | ✓ | 0.0% |  |
| 100 | `HSharesDisclaimedTSH` | #H股弃权股数(股) | number(18,2) | ✓ | 0.0% |  |
| 101 | `OSharesDisclaimedTSH` | #其他流通股东弃权股数(股) | number(18,2) | ✓ | 0.0% |  |
| 102 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 103 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 104 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### MeetingType (股东大会类别)

股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND DM IN (1,3)，得到股东大会类别的具体描述：1-年度股东大会，3-临时股东大会。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

### IfConnectedTransaction (是否关联交易)

是否关联交易（IfConnectedTransaction），该字段固定以下常量：0-否；1-是

### ProposalType (议案类别)

议案类别(ProposalType)与(CT_SystemConst)表中的DM字段关联，令LB = 1303，得到议案类别的具体描述：1101-股权分置，1102-增发新股，1103-配股，1104-优先股发行，1106-减资分立，1107-发行债券，1108-利润分配，1109-股权激励，1110-股权回购，1111-员工持股计划，2001-暂停上市，2002-恢复上市，2003-终止上市，3001-年度报告，3002-中期报告，3003-第一季报，3004-第三季报，3005-董监高工作报告，3006-财务预决算报告，3007-财务数据调整修正，3008-股东未来分红回报，4001-名称变更，4002-地址变更，4003-经营范围变更，4004-工商登记变更，4005-中介机构变动，4006-人事变动，4007-高管薪酬，4008-章程制度，5001-借贷，5002-担保，5003-诉讼仲裁，5004-重大经营合同，5005-资产重组，5006-资产托管与租赁，5007-资产出售与转让，5008-资产抵押，5009-资产拍卖，5010-资产置换，5011-资产赠与，5012-投资收购，5013-委托理财，5014-税负变动，5015-补偿补贴，5016-违规处罚，5017-吸收合并，9999-其他。

### VotingType (议案投票类型)

议案投票类型(VotingType)与(CT_SystemConst)表中的DM字段关联，令LB = 2219，得到议案投票类型的具体描述：1-非累积投票，2-累计投票。

### IfPassed (是否通过)

是否通过(IfPassed)，该字段固定以下常量：0-否；1-是

## SQL示例

```sql
-- 查询 股东大会表决 数据
SELECT *
FROM lc_smvoting
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
