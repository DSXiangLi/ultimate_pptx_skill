# LC_RConsideration

**中文名**: 股权分置对价方案

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_RConsideration` |
| MySQL表名 | `lc_rconsideration` |
| 中文名 | 股权分置对价方案 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 45 |
| 版本 | 1 |

## 表描述

1.收录股权分置改革方案具体内容，包括公司派现、送转股、非流通股东现金对价、股份对价支付、非流通股缩情况、改革方案文字说明等。
2.数据范围：2005-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `LatestInfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效（IfEffected），该字段固定以下常量：0-否；1-是 |
| 6 | `ProgramType` | 方案类型(多选) | number(10) | ✓ |  |  |
| 7 | `GainerShareKind` | 获付股东股本性质 | number(10) | ✓ | 100.0% | 获付股东股本性质(GainerShareKind)与(CT_SystemConst)表中的DM字段关联，令LB = 10... |
| 8 | `GainerHolding` | 获付对价股东持股(股) | number(18,2) | ✓ | 100.0% |  |
| 9 | `PresenterHolding` | 支付对价非流通股东持股(股) | number(18,2) | ✓ | 100.0% |  |
| 10 | `RatioInNTSH` | 支付对价非流通股东持股占非流通股比例 | number(18,8) | ✓ | 46.8% |  |
| 11 | `CompanyGrantedShare` | 公司送股(10送X) | number(18,6) | ✓ | 0.63% |  |
| 12 | `NTSHTranPaid` | 其中:非流通股东转付 | number(18,8) | ✓ | 0.32% |  |
| 13 | `GTSharefromCompany` | 其中:直接从公司获付 | number(18,8) | ✓ | 0.63% |  |
| 14 | `CompanyTransformedShare` | 公司转增股(10转增X) | number(18,6) | ✓ | 21.94% |  |
| 15 | `NTSHTranPaidTShare` | 其中:非流通股东转付 | number(18,8) | ✓ | 5.64% |  |
| 16 | `CashBTfromCompany` | 其中:直接从公司获付 | number(18,8) | ✓ | 21.86% |  |
| 17 | `CompanyPaidCashBT` | 公司派现(10派X元) | number(18,6) | ✓ | 2.45% |  |
| 18 | `NTSHTranPaidCash` | 其中:非流通股东转付 | number(18,8) | ✓ | 2.17% |  |
| 19 | `WarrantfromCompany` | 其中:直接从公司获付 | number(18,8) | ✓ | 2.45% |  |
| 20 | `CompanyPaidCashAT` | 公司派现(税后10派X元) | number(18,8) | ✓ | 1.34% |  |
| 21 | `CompanyWarrantRate` | 公司认股证(10送X份) | number(18,8) | ✓ | 0.2% |  |
| 22 | `NTSNTranWarrant` | 其中:非流通股东转付 | number(18,8) | ✓ | 0.04% |  |
| 23 | `CashATfromCompany` | 其中:直接从公司获付 | number(18,8) | ✓ | 0.2% |  |
| 24 | `CompanyGTShare` | 公司合计送转股数(股) | number(18,2) | ✓ | 22.42% |  |
| 25 | `CompanyPaidCash` | 公司合计派现金额(元) | number(19,4) | ✓ | 2.45% |  |
| 26 | `CompanyWarrant` | 公司合计认股证份数(股) | number(18,2) | ✓ | 0.2% |  |
| 27 | `ShareConsiderationRate` | 对价股份(10送X) | number(18,6) | ✓ | 75.97% |  |
| 28 | `CashConsiderationRateBT` | 对价现金(10派X) | number(18,6) | ✓ | 3.67% |  |
| 29 | `CashConsiderationRateAT` | 对价现金(税后10派X) | number(18,8) | ✓ | 0.08% |  |
| 30 | `WarrantConsiderationRate` | 对价认股证(10送X) | number(18,6) | ✓ | 2.13% |  |
| 31 | `CallWarrant` | 其中:认购证(10送X) | number(18,8) | ✓ | 0.87% |  |
| 32 | `PutWarrant` | 认沽证(10送X) | number(18,8) | ✓ | 1.66% |  |
| 33 | `ShareConsideration` | 对价股份总额(股) | number(18,2) | ✓ | 75.97% |  |
| 34 | `CashConsiderationR` | 对价现金总额(元) | number(19,4) | ✓ | 3.67% |  |
| 35 | `WarrantConsideration` | 对价认股证总额(股) | number(18,2) | ✓ | 2.13% |  |
| 36 | `RatioOfNTShareBCompressed` | 缩股前非流通股占总股本比例 | number(18,8) | ✓ | 1.14% |  |
| 37 | `RatioOfNTShareACompressed` | 缩股后非流通股占总股本比例 | number(18,8) | ✓ | 1.14% |  |
| 38 | `ShareCompressedOfNTShare` | 非流通股缩股总额(股) | number(18,2) | ✓ | 1.14% |  |
| 39 | `Tshare` | 流通股 | number(18,2) | ✓ | 0.24% |  |
| 40 | `NTShare` | 非流通股 | number(18,2) | ✓ | 0.24% |  |
| 41 | `Program` | 改革方案说明 | varchar2(500) | ✓ | 100.0% |  |
| 42 | `PricingBasis` | 定价依据说明 | clob | ✓ | 12.15% |  |
| 43 | `Notes` | 备注 | varchar2(500) | ✓ | 99.96% |  |
| 44 | `XGRQ` | 修改日期 | date | ✗ |  |  |
| 45 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfEffected (是否有效)

是否有效（IfEffected），该字段固定以下常量：0-否；1-是

### GainerShareKind (获付股东股本性质)

获付股东股本性质(GainerShareKind)与(CT_SystemConst)表中的DM字段关联，令LB = 1024，得到获付股东股本性质的具体描述：1-流通A股，2-H股，3-B股，4-国家股，5-法人股，6-境外法人股，7-职工股，8-转配股，9-个人持股，10-S股，11-限售流通A股，12-境内优先股，13-境外优先股，15-N股，16-D股，17-三板流通股，43-国有法人股，51-A类普通股，52-B类普通股，53-C类普通股，54-D类普通股，80-有投票权的优先股，99-其他，100-个人股，101-GDR代表基础股票，102-CDR代表基础股票。

## SQL示例

```sql
-- 查询 股权分置对价方案 数据
SELECT *
FROM lc_rconsideration
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
