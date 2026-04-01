# DZ_FreshestShareStru

**中文名**: 最新公司股本结构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_FreshestShareStru` |
| MySQL表名 | `dz_freshestsharestru` |
| 中文名 | 最新公司股本结构 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 80 |
| 版本 | 1 |

## 表描述

1.内容说明：收录上市公司（包括科创板）最新股本机构数据,包括未流通股份、流通股份、有限售流通股份明细、总股本等内容。
2.数据范围：保留最新股本结构数据
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `PerValue` | 股票面值 | number(19,4) | ✓ | 99.92% |  |
| 7 | `NonListedShares` | 未流通股份(股) | number(16,0) | ✓ | 23.6% |  |
| 8 | `PromoterShares` | 1、发起人股(股) | number(16,0) | ✓ | 19.7% |  |
| 9 | `StateShares` | 国家股(股) | number(16,0) | ✓ | 0.7% |  |
| 10 | `SLegalPersonShares` | 国有法人股(股) | number(16,0) | ✓ | 6.75% |  |
| 11 | `DLegalPersonShares` | 境内法人股(股) | number(16,0) | ✓ | 18.91% |  |
| 12 | `FLegalPersonShares` | 外资法人股(股) | number(16,0) | ✓ | 2.49% |  |
| 13 | `RaisedLPShares` | 2、募集法人股(股) | number(16,0) | ✓ | 0.44% |  |
| 14 | `RaisedSLPShares` | 其中:募集国有法人股(股) | number(16,0) | ✓ | 0.01% |  |
| 15 | `NaturalPersonHoldLPShares` | 3、自然人法人股(股) | number(16,0) | ✓ | 16.23% |  |
| 16 | `StaffShares` | 4、职工股(股) | number(16,0) | ✓ | 0.04% |  |
| 17 | `RightsIssueTransferred` | 5、转配股(股) | number(16,0) | ✓ | 0.0% |  |
| 18 | `FloatShare` | 流通股份(股) | number(16,0) | ✓ | 77.67% |  |
| 19 | `AFloats` | 1、流通A股(股) | number(16,0) | ✓ | 77.09% |  |
| 20 | `AFloatListed` | 1)已上市流通A股(股) | number(16,0) | ✓ | 77.09% |  |
| 21 | `ManagementShares` | 其中:高管股(股) | number(16,0) | ✓ | 32.92% |  |
| 22 | `StategicInvestorShares` | 2)战略投资者配售持股(股) | number(16,0) | ✓ | 0.05% |  |
| 23 | `CommonLPShares` | 3)一般法人配售持股(股) | number(16,0) | ✓ | 0.09% |  |
| 24 | `MutualFundShares` | 4)基金配售持股(股) | number(16,0) | ✓ | 0.0% |  |
| 25 | `AdditionalIssueUnlisted` | 5)增发未上市(股) | number(16,0) | ✓ | 0.0% |  |
| 26 | `RightsIssueUnlisted` | 6)配股未上市(股) | number(16,0) | ✓ | 0.0% |  |
| 27 | `RestrictedAFloatShares` | 8)有限售流通A股(股) | number(16,0) | ✓ | 50.95% |  |
| 28 | `Bshares` | 2、B股(股) | number(16,0) | ✓ | 1.47% |  |
| 29 | `NonListedBShares` | 其中:未流通B股 | number(16,0) | ✓ | 0.0% |  |
| 30 | `RestrictedBFloatShares` | 3、有限售B股(股) | number(16,0) | ✓ | 0.03% |  |
| 31 | `Hshares` | 4、H股(股) | number(16,0) | ✓ | 2.51% |  |
| 32 | `OtherFloatShares` | 5、其他流通股(股) | number(16,0) | ✓ | 0.03% |  |
| 33 | `Sshares` | #S股(股) | number(16,0) | ✓ | 0.01% |  |
| 34 | `Nshares` | #N股(股) | number(16,0) | ✓ | 0.0% |  |
| 35 | `Dshares` | #D股(股) | number(16,0) | ✓ | 0.01% |  |
| 36 | `RestrictedShares` | 有限售股份(股) | number(16,0) | ✓ | 50.48% |  |
| 37 | `StateHolding` | 1.国家持股(股) | number(16,0) | ✓ | 0.19% |  |
| 38 | `SLegalPersonHolding` | 2.国有法人持股(股) | number(16,0) | ✓ | 5.83% |  |
| 39 | `OtherDCapitalHolding` | 3.其他内资持股(股) | number(16,0) | ✓ | 48.45% |  |
| 40 | `DLegalPersonHolding` | ##境内法人持股(股) | number(16,0) | ✓ | 12.86% |  |
| 41 | `DNaturalPersonHolding` | ##境内自然人持股(股) | number(16,0) | ✓ | 45.39% |  |
| 42 | `ForeignHolding` | 4.外资持股(股) | number(16,0) | ✓ | 3.9% |  |
| 43 | `FLegalPersonHolding` | ##境外法人持股(股) | number(16,0) | ✓ | 1.06% |  |
| 44 | `FNaturalPersonHolding` | ##境外自然人持股(股) | number(16,0) | ✓ | 3.01% |  |
| 45 | `OtherRestrictedShares` | 5.其他有限售(股) | number(16,0) | ✓ | 0.17% |  |
| 46 | `Rpt_RestrictedShares` | 一、有限售条件股份(万股) | number(18,0) | ✓ | 61.52% |  |
| 47 | `Rpt_StateHolding` | 1、国家持股 | number(18,0) | ✓ | 0.55% |  |
| 48 | `Rpt_SLegalPersonHolding` | 2、国有法人持股 | number(18,0) | ✓ | 2.95% |  |
| 49 | `Rpt_OtherDCapitalHolding` | 3、其他内资持股 | number(18,0) | ✓ | 27.15% |  |
| 50 | `Rpt_DLegalPersonHolding` | 1)境内法人持股 | number(18,0) | ✓ | 5.99% |  |
| 51 | `Rpt_DNaturalPersonHolding` | 2)境内自然人持股 | number(18,0) | ✓ | 23.8% |  |
| 52 | `Rpt_ForeignHolding` | 4、外资持股 | number(18,0) | ✓ | 1.99% |  |
| 53 | `Rpt_FLegalPersonHolding` | 1)境外法人持股 | number(18,0) | ✓ | 0.74% |  |
| 54 | `Rpt_FNaturalPersonHolding` | 2)境外自然人持股 | number(18,0) | ✓ | 1.72% |  |
| 55 | `Rpt_FloatListed` | 二、无限售条件股份 | number(18,0) | ✓ | 76.41% |  |
| 56 | `Rpt_AFloatListed` | 1、人民币普通股 | number(18,0) | ✓ | 76.4% |  |
| 57 | `Rpt_BFloatListed` | 2、境内上市的外资股 | number(18,0) | ✓ | 1.47% |  |
| 58 | `Rpt_FFloatListed` | 3、境外上市的外资股 | number(18,0) | ✓ | 2.71% |  |
| 59 | `Rpt_OtherFloatShares` | 4、其他无限售股份 | number(18,0) | ✓ | 0.35% |  |
| 60 | `Rpt_TotalShares` | 三、股份总数 | number(18,0) | ✓ | 76.41% |  |
| 61 | `Ashares` | A股(股) | number(16,0) | ✓ | 99.72% |  |
| 62 | `NonRestrictedShares` | 无限售条件流通A股(股) | number(16,0) | ✓ | 77.11% |  |
| 63 | `BsharesTotal` | B股总股本 | number(16,0) | ✓ | 1.47% |  |
| 64 | `ListedBShares` | 流通B股(股) | number(16,0) | ✓ | 1.47% |  |
| 65 | `NonListedRestrictedBShares` | 未流通B股(股) | number(16,0) | ✓ | 12.07% |  |
| 66 | `ForeignHoldingAshares` | 外资持A股(股) | number(16,0) | ✓ | 3.9% |  |
| 67 | `RestrictedAShares` | 有限售条件的流通A股(股) | number(16,0) | ✓ | 50.91% |  |
| 68 | `Rpt_ManagementShares` | 3)境内高管持股 | number(16,0) | ✓ | 1.74% |  |
| 69 | `TotalShares` | 总股本(股) | number(16,0) | ✓ | 100.0% |  |
| 70 | `ChangeType` | 股本变动原因类别 | number(10) | ✓ | 37.28% | 股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AN... |
| 71 | `ChangeReason` | 股本变动原因说明 | varchar2(255) | ✓ | 37.28% |  |
| 72 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 73 | `XGRQ` | 更新时间1 | date | ✗ |  |  |
| 74 | `JSID` | JSID | number(19) | ✗ |  |  |
| 75 | `OtherPromoterShares` | 其它发起人股(股) | number(16,0) | ✓ | 0.0% |  |
| 76 | `PreferredAndOtherShares` | 6、优先股及其他(股) | number(16,0) | ✓ | 0.0% |  |
| 77 | `PreferredShares` | 其中:优先股(股) | number(16,0) | ✓ | 0.0% |  |
| 78 | `OtherAFloatShares` | 7)其他流通股份(股) | number(16,0) | ✓ | 0.0% |  |
| 79 | `RestrinctStaffShares` | 其中:有限售流通股中职工股(股) | number(16,0) | ✓ | 0.0% |  |
| 80 | `GDRshares` | 6、GDR代表基础股票(股) | number(16,0) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ChangeType (股本变动原因类别)

股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM NOT IN (43,60,101,102,105,115,116,117,118,119,121,123,127,128,129,131,132,135)，得到股本变动原因类别的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非公开增发A股，19-定向增发法人股，20-增发A股，21-增发B股，22-增发A股上市，23-增发A股基金配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，26-H股增发，27-增发B股上市，28-H股首发上市，29-超额配售H股上市，30-国家股配售，35-股份回购，40-吸收合并，44-以股抵债，45-职工股上市，46-STAQ/NET系统法人股上市，47-外资法人股上市，48-可转换债券转股，49-股权转让，50-面值拆细，51-其他，52-CDR发行，53-CDR上市，54-CDR增发，55-CDR增发上市，56-CDR配股除权，57-CDR配股上市，58-CDR超额配售上市，59-优先股转普通股，71-股权分置方案实施，73-股权分置股份追送，75-股权分置限售流通，77-股权分置增持，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，84-股权激励方案实施，89-延长限售锁定期，90-延长限售锁定期流通，91-B股转H股，100-授予限制性股票，103-员工持股计划，104-员工持股计划限售流通，106-D股增发，107-D股首发上市，108-超额配售D股上市，109-超额配售A股上市，110-GDR基础股票首发上市，111-GDR基础股票增发上市，112-超额配售GDR基础股票上市，113-GDR基础股票生成兑回，114-三板挂牌，130-高管股份减少，134-战略配售股份出借，136-战略配售股份归还，137-高管股份增加，138-股东承诺不减持，139-分红股份上市，140-超额配售B股上市，141-追溯更新，142-承诺不减持到期。

## SQL示例

```sql
-- 查询 最新公司股本结构 数据
SELECT *
FROM dz_freshestsharestru
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
