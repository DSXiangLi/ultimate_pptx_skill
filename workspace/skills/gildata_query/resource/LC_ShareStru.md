# LC_ShareStru

**中文名**: 公司股本结构变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ShareStru` |
| MySQL表名 | `lc_sharestru` |
| 中文名 | 公司股本结构变动 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股东与股本 |
| 更新频率 | 不定时更新 |
| 字段数量 | 75 |
| 版本 | 1.06 |

## 表描述

1.收录上市公司股本结构历史变动情况。其中：标注“披露”的字段为公司公告原始披露，标注“计算”的字段为聚源依据股权登记日，并且考虑高管股锁定的实际情况计算所得的股本结构。
2.数据范围：1990-12-10至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 99.89% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `PerValue` | 每股面值 | number(25,10) | ✓ | 99.73% |  |
| 7 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 99.73% | 每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 8 | `TotalShares` | 总股本(股) | number(16,0) | ✓ | 100.0% |  |
| 9 | `Ashares` | 1.A股(股) | number(16,0) | ✓ | 99.57% |  |
| 10 | `AFloats` | 1)流通A股(股) | number(16,0) | ✓ | 88.71% |  |
| 11 | `RestrictedAShares` | 1.1)有限售条件的流通A股(股)(计算) | number(16,0) | ✓ | 66.71% |  |
| 12 | `NonResiSharesJY` | 1.2)无限售条件流通A股(股)(计算) | number(16,0) | ✓ | 88.71% |  |
| 13 | `RestrictAShareP` | 1.3)有限售条件的流通A股(股)(披露) | number(16,0) | ✓ | 69.47% |  |
| 14 | `NonRestrictedShares` | 1.4)无限售条件流通A股(股)(披露) | number(16,0) | ✓ | 77.39% |  |
| 15 | `NonListedShares` | 2)未流通A股(股) | number(16,0) | ✓ | 22.15% |  |
| 16 | `BsharesTotal` | 2.B股(股) | number(16,0) | ✓ | 3.1% |  |
| 17 | `ListedBShares` | 1)流通B股(股) | number(16,0) | ✓ | 3.09% |  |
| 18 | `NonResiBShares` | 其中:无限售流通B股 | number(16,0) | ✓ | 3.09% |  |
| 19 | `NonListedRestrictedBShares` | 2)未流通B股(股) | number(16,0) | ✓ | 0.42% |  |
| 20 | `Hshares` | 3.H股(股) | number(16,0) | ✓ | 2.66% |  |
| 21 | `RestrictedHShares` | 有限售H股 | number(16,0) | ✓ | 0.05% |  |
| 22 | `NonRestrictedHShares` | 无限售H股 | number(16,0) | ✓ | 2.66% |  |
| 23 | `OtherFloatShares` | 4.海外上市股(股) | number(16,0) | ✓ | 0.05% |  |
| 24 | `Sshares` | 1)S股(股) | number(16,0) | ✓ | 0.03% |  |
| 25 | `Nshares` | 2)N股(股) | number(16,0) | ✓ | 0.01% |  |
| 26 | `Dshares` | 3)D股(股) | number(16,0) | ✓ | 0.02% |  |
| 27 | `SRUnlistedShare` | 已发行未上市股份(股) | number(16,0) | ✓ | 4.82% |  |
| 28 | `OUnListedShares` | 其他未流通股(股) | number(16,0) | ✓ | 0.01% |  |
| 29 | `RestrictedShares` | 有限售条件的流通股(股) | number(16,0) | ✓ | 66.47% |  |
| 30 | `StateHolding` | A.国家持股(股) | number(16,0) | ✓ | 2.32% |  |
| 31 | `SLegalPersonHolding` | B.国有法人持股(股) | number(16,0) | ✓ | 13.64% |  |
| 32 | `OtherDCapitalHolding` | C.其他内资持股(股) | number(16,0) | ✓ | 60.67% |  |
| 33 | `DLegalPersonHolding` | a.境内法人持股(股) | number(16,0) | ✓ | 30.38% |  |
| 34 | `DNaturalPersonHolding` | b.境内自然人持股(股) | number(16,0) | ✓ | 53.43% |  |
| 35 | `ManagementShares` | ##高管股(股) | number(16,0) | ✓ | 36.24% |  |
| 36 | `ForeignHolding` | D.外资持股(股) | number(16,0) | ✓ | 6.84% |  |
| 37 | `FLegalPersonHolding` | 其中:境外法人持股(股) | number(16,0) | ✓ | 3.94% |  |
| 38 | `FNaturalPersonHolding` | 其中:境外自然人持股(股) | number(16,0) | ✓ | 3.46% |  |
| 39 | `OtherRestrictedShares` | E.其他有限售(股) | number(16,0) | ✓ | 2.05% |  |
| 40 | `PromoterShares` | 1.发起人股(股) | number(16,0) | ✓ | 19.06% |  |
| 41 | `StateShares` | 国家股(股) | number(16,0) | ✓ | 7.93% |  |
| 42 | `SLegalPersonShares` | 国有法人股(股) | number(16,0) | ✓ | 2.98% |  |
| 43 | `DLegalPersonShares` | 境内法人股(股) | number(16,0) | ✓ | 14.3% |  |
| 44 | `FLegalPersonShares` | 外资法人股(股) | number(16,0) | ✓ | 1.88% |  |
| 45 | `RaisedLPShares` | 2.募集法人股(股) | number(16,0) | ✓ | 5.09% |  |
| 46 | `RaisedSLPShares` | 其中:募集国有法人股(股) | number(16,0) | ✓ | 0.0% |  |
| 47 | `NaturalPersonHoldLPShares` | 3.自然人法人股(股) | number(16,0) | ✓ | 6.61% |  |
| 48 | `StaffShares` | 4.职工股(股) | number(16,0) | ✓ | 1.81% |  |
| 49 | `RightsIssueTransferred` | 5.转配股(股) | number(16,0) | ✓ | 0.8% |  |
| 50 | `OtherNonListedShares` | 8.其他未流通股(股) | number(16,0) | ✓ | 0.01% |  |
| 51 | `FloatShare` | 流通股份(股) | number(16,0) | ✓ | 90.85% |  |
| 52 | `AFloatListed` | 1)已上市流通A股(包含高管股)(股) | number(16,0) | ✓ | 88.69% |  |
| 53 | `StategicInvestorShares` | 2)战略投资者配售持股(股) | number(16,0) | ✓ | 0.24% |  |
| 54 | `CommonLPShares` | 3)一般法人配售持股(股) | number(16,0) | ✓ | 1.72% |  |
| 55 | `MutualFundShares` | 4)基金配售持股(股) | number(16,0) | ✓ | 0.05% |  |
| 56 | `AdditionalIssueUnlisted` | 5)增发未上市(股) | number(16,0) | ✓ | 1.3% |  |
| 57 | `RightsIssueUnlisted` | 6)配股未上市(股) | number(16,0) | ✓ | 1.68% |  |
| 58 | `RestrictedAFloatShares` | 8)有限售流通A股(股) | number(16,0) | ✓ | 52.59% |  |
| 59 | `Bshares` | B股_旧(股) | number(16,0) | ✓ | 3.1% |  |
| 60 | `NonListedBShares` | 其中:未流通B股_旧 | number(16,0) | ✓ | 0.11% |  |
| 61 | `RestrictedBFloatShares` | 有限售B股(股) | number(16,0) | ✓ | 0.06% |  |
| 62 | `ForeignHoldingAshares` | 外资持A股(股) | number(16,0) | ✓ | 6.81% |  |
| 63 | `ChangeType` | 股本变动原因类别 | number(10) | ✓ | 48.96% | 股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AN... |
| 64 | `ChangeTypeDetail` | 股本变动原因类别明细 | number(10) | ✓ |  |  |
| 65 | `ChangeReason` | 股本变动原因说明 | varchar2(255) | ✓ | 48.94% |  |
| 66 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 67 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 68 | `JSID` | JSID | number(19) | ✗ |  |  |
| 69 | `GDRshares` | 5.GDR代表基础股票(股) | number(16,0) | ✓ | 0.0% |  |
| 70 | `OtherPromoterShares` | 其它发起人股(股) | number(16,0) | ✓ | 0.0% |  |
| 71 | `PreferredAndOtherShares` | 6.优先股及其他(股) | number(16,0) | ✓ | 0.0% |  |
| 72 | `PreferredShares` | 其中:优先股(股) | number(16,0) | ✓ | 0.0% |  |
| 73 | `OtherFNonListedShares` | 7.其他外资股(股) | number(16,0) | ✓ | 0.0% |  |
| 74 | `OtherAFloatShares` | 7)其他流通股份(股) | number(16,0) | ✓ | 0.0% |  |
| 75 | `RestrinctStaffShares` | 其中:有限售流通股中职工股(股) | number(16,0) | ✓ | 0.0% |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### ParValueCurrencyUnit (每股面值货币单位)

每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1000,1001,1100,1420)，得到每股面值货币单位的具体描述：1000-美元，1001-美分，1100-港元，1420-人民币元。

### ChangeType (股本变动原因类别)

股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM NOT IN (43,60,101,102,105,115,116,117,118,119,121,123,127,128,129,131,132,135)，得到股本变动原因类别的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非公开增发A股，19-定向增发法人股，20-增发A股，21-增发B股，22-增发A股上市，23-增发A股基金配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，26-H股增发，27-增发B股上市，28-H股首发上市，29-超额配售H股上市，30-国家股配售，35-股份回购，40-吸收合并，44-以股抵债，45-职工股上市，46-STAQ/NET系统法人股上市，47-外资法人股上市，48-可转换债券转股，49-股权转让，50-面值拆细，51-其他，52-CDR发行，53-CDR上市，54-CDR增发，55-CDR增发上市，56-CDR配股除权，57-CDR配股上市，58-CDR超额配售上市，59-优先股转普通股，71-股权分置方案实施，73-股权分置股份追送，75-股权分置限售流通，77-股权分置增持，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，84-股权激励方案实施，89-延长限售锁定期，90-延长限售锁定期流通，91-B股转H股，100-授予限制性股票，103-员工持股计划，104-员工持股计划限售流通，106-D股增发，107-D股首发上市，108-超额配售D股上市，109-超额配售A股上市，110-GDR基础股票首发上市，111-GDR基础股票增发上市，112-超额配售GDR基础股票上市，113-GDR基础股票生成兑回，114-三板挂牌，130-高管股份减少，134-战略配售股份出借，136-战略配售股份归还，137-高管股份增加，138-股东承诺不减持，139-分红股份上市，140-超额配售B股上市，141-追溯更新，142-承诺不减持到期。

## SQL示例

```sql
-- 查询 公司股本结构变动 数据
SELECT *
FROM lc_sharestru
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
