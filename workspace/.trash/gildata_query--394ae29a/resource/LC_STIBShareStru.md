# LC_STIBShareStru

**中文名**: 科创板公司股本结构

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBShareStru` |
| MySQL表名 | `lc_stibsharestru` |
| 中文名 | 科创板公司股本结构 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 56 |
| 版本 | 1.04 |

## 表描述

1.内容说明：收录科创板上市公司股本结构历史变动情况。其中：标注“披露”的字段为公司公告原始披露，标注“计算”的字段为聚源依据股权登记日，并且考虑高管股锁定的实际情况计算所得的股本结构。
2.数据范围：2019年至今
3.信息来源：招股说明书、上市公告书、定报、临时公告等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `ParValue` | 每股面值 | number(25,10) | ✓ | 99.71% |  |
| 7 | `ParValueCurrencyUnit` | 每股面值货币单位 | number(10) | ✓ | 99.71% | 每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB... |
| 8 | `TotalShares` | 总股本(股) | number(16,0) | ✓ | 100.0% |  |
| 9 | `Ashares` | 1.A股(股) | number(16,0) | ✓ | 99.8% |  |
| 10 | `AFloats` | 1)流通A股(股) | number(16,0) | ✓ | 74.57% |  |
| 11 | `RestrictedAShares` | 1.1)有限售条件的流通A股(股)(计算) | number(16,0) | ✓ | 57.12% |  |
| 12 | `NonResiSharesJY` | 1.2)无限售条件流通A股(股)(计算) | number(16,0) | ✓ | 74.57% |  |
| 13 | `RestrictAShareP` | 1.3)有限售条件的流通A股(股)(披露) | number(16,0) | ✓ | 63.04% |  |
| 14 | `NonRestrictedShares` | 1.4)无限售条件流通A股(股)(披露) | number(16,0) | ✓ | 74.63% |  |
| 15 | `NonListedShares` | 2)未流通A股(股) | number(16,0) | ✓ | 25.19% |  |
| 16 | `SRUnlistedShare` | 已发行未上市股份(股) | number(16,0) | ✓ | 4.53% |  |
| 17 | `Hshares` | 2.H股(股) | number(16,0) | ✓ | 4.17% |  |
| 18 | `RestrictedHShares` | 有限售H股 | number(16,0) | ✓ | 0.0% |  |
| 19 | `NonRestrictedHShares` | 无限售H股 | number(16,0) | ✓ | 4.17% |  |
| 20 | `OtherFloatShares` | 3.海外上市股(股) | number(16,0) | ✓ | 0.0% |  |
| 21 | `Sshares` | 1)S股(股) | number(16,0) | ✓ | 0.0% |  |
| 22 | `Nshares` | 2)N股(股) | number(16,0) | ✓ | 0.0% |  |
| 23 | `Dshares` | 3)D股(股) | number(16,0) | ✓ | 0.0% |  |
| 24 | `PromoterShares` | 1.发起人股(股) | number(16,0) | ✓ | 22.34% |  |
| 25 | `StateShares` | 1)国家股(股) | number(16,0) | ✓ | 0.11% |  |
| 26 | `SLegalPersonShares` | 2)国有法人股(股) | number(16,0) | ✓ | 10.21% |  |
| 27 | `DLegalPersonShares` | 3)境内法人股(股) | number(16,0) | ✓ | 22.08% |  |
| 28 | `FLegalPersonShares` | 4)境外法人股(股) | number(16,0) | ✓ | 4.83% |  |
| 29 | `NLegalPersonShares` | 2.自然人法人股(股) | number(16,0) | ✓ | 18.4% |  |
| 30 | `DNLegalPersonShares` | 1)境内自然人法人股(股) | number(16,0) | ✓ | 17.76% |  |
| 31 | `FNLegalPersonShares` | 2)境外自然人法人股(股) | number(16,0) | ✓ | 2.04% |  |
| 32 | `FloatShare` | 流通股份(股) | number(16,0) | ✓ | 79.22% |  |
| 33 | `AFloatListed` | 1.已上市流通A股(包含高管股)(股) | number(16,0) | ✓ | 74.57% |  |
| 34 | `StategicInvestorShares` | 2.战略投资者配售持股(股) | number(16,0) | ✓ | 4.14% |  |
| 35 | `CommonLPShares` | 3.一般法人配售持股(股) | number(16,0) | ✓ | 4.15% |  |
| 36 | `RestrictedAFloatShares` | 4.有限售流通A股(股) | number(16,0) | ✓ | 57.12% |  |
| 37 | `NewIssueUnlisted` | 5.增发未上市(股) | number(16,0) | ✓ | 0.0% |  |
| 38 | `RightsIssueUnlisted` | 6.配股未上市(股) | number(16,0) | ✓ | 0.38% |  |
| 39 | `ForeignFloatListed` | 7.境外上市股(股) | number(16,0) | ✓ | 4.17% |  |
| 40 | `StateHolding` | 1.国家持股(股) | number(16,0) | ✓ | 0.09% |  |
| 41 | `SLegalPersonHolding` | 2.国有法人持股(股) | number(16,0) | ✓ | 26.09% |  |
| 42 | `OtherDCapitalHolding` | 3.其他内资持股(股) | number(16,0) | ✓ | 54.09% |  |
| 43 | `DLPersonHolding` | 3.1)境内法人持股(股) | number(16,0) | ✓ | 48.4% |  |
| 44 | `DNPersonHolding` | 3.2)境内自然人持股(股) | number(16,0) | ✓ | 41.73% |  |
| 45 | `ManagementShares` | ##高管股(股) | number(16,0) | ✓ | 0.0% |  |
| 46 | `ForeignHolding` | 4.外资持股(股) | number(16,0) | ✓ | 15.7% |  |
| 47 | `FLPersonHolding` | 4.1)境外法人持股(股) | number(16,0) | ✓ | 13.25% |  |
| 48 | `FNPersonHolding` | 4.2)境外自然人持股(股) | number(16,0) | ✓ | 5.13% |  |
| 49 | `OtherRestrictedShares` | 5.其他有限售(股) | number(16,0) | ✓ | 0.13% |  |
| 50 | `ChangeType` | 股本变动原因类别 | number(10) | ✓ | 55.31% | 股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AN... |
| 51 | `ChangeTypeDetail` | 股本变动原因类别明细 | number(10) | ✓ |  |  |
| 52 | `ChangeReason` | 股本变动原因说明 | varchar2(255) | ✓ | 55.31% |  |
| 53 | `OtherPromoterShares` | 5)其它发起人股(股) | number(16,0) | ✓ | 0.0% |  |
| 54 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 55 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 56 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到科创板上市公司的交易代码、简称等。

### ParValueCurrencyUnit (每股面值货币单位)

每股面值货币单位(ParValueCurrencyUnit)与(CT_SystemConst)表中的DM字段关联，令LB = 1068 AND DM IN (1000,1001,1100,1420)，得到每股面值货币单位的具体描述：1000-美元，1001-美分，1100-港元，1420-人民币元。

### ChangeType (股本变动原因类别)

股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM NOT IN (43,60,101,102,105,115,116,117,118,119,121,123,127,128,129,131,132,135)，得到股本变动原因类别的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非公开增发A股，19-定向增发法人股，20-增发A股，21-增发B股，22-增发A股上市，23-增发A股基金配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，26-H股增发，27-增发B股上市，28-H股首发上市，29-超额配售H股上市，30-国家股配售，35-股份回购，40-吸收合并，44-以股抵债，45-职工股上市，46-STAQ/NET系统法人股上市，47-外资法人股上市，48-可转换债券转股，49-股权转让，50-面值拆细，51-其他，52-CDR发行，53-CDR上市，54-CDR增发，55-CDR增发上市，56-CDR配股除权，57-CDR配股上市，58-CDR超额配售上市，59-优先股转普通股，71-股权分置方案实施，73-股权分置股份追送，75-股权分置限售流通，77-股权分置增持，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，84-股权激励方案实施，89-延长限售锁定期，90-延长限售锁定期流通，91-B股转H股，100-授予限制性股票，103-员工持股计划，104-员工持股计划限售流通，106-D股增发，107-D股首发上市，108-超额配售D股上市，109-超额配售A股上市，110-GDR基础股票首发上市，111-GDR基础股票增发上市，112-超额配售GDR基础股票上市，113-GDR基础股票生成兑回，114-三板挂牌，130-高管股份减少，134-战略配售股份出借，136-战略配售股份归还，137-高管股份增加，138-股东承诺不减持，139-分红股份上市，140-超额配售B股上市，141-追溯更新，142-承诺不减持到期。

## SQL示例

```sql
-- 查询 科创板公司股本结构 数据
SELECT *
FROM lc_stibsharestru
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
