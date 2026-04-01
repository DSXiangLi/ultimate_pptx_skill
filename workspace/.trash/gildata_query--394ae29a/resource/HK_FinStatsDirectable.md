# HK_FinStatsDirectable

**中文名**: 港股财报目录表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FinStatsDirectable` |
| MySQL表名 | `hk_finstatsdirectable` |
| 中文名 | 港股财报目录表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 39 |
| 版本 | 1.02 |

## 表描述

1.介绍港股财报的基础信息 ,包括一份财报披露的表单信息，单季度数据和常规数据，是否包含母公司报表，财报披露遵循的会计准则，财报披露适用的一般格式，财报中是否使用有两个以上货币单位等信息。
2.数据范围：1998年至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 3 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 4 | `DateTypeCode` | 日期标识 | number(10) | ✗ | 100.0% | 日期标识(DateTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期... |
| 5 | `ReportType` | 报告类型 | number(10) | ✗ | 100.0% | 报告类型（ReportType）：1-单季度报告；2-常规报表。 |
| 6 | `HasBalanceSheet` | 是否有资产负债表 | number(10) | ✓ | 100.0% | 是否有资产负债表（HasBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB... |
| 7 | `HasPCBalanceSheet` | 是否有母公司资产负债表 | number(10) | ✓ | 100.0% | 是否有母公司资产负债表（HasPCBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关... |
| 8 | `InfoPublDateBS` | 信息发布日期-资产负债表 | date | ✓ | 76.35% |  |
| 9 | `InitialInfoPublDateBS` | 首次信息发布日期-资产负债表 | date | ✓ | 75.73% |  |
| 10 | `InfoSourceBS` | 信息来源-资产负债表 | varchar2(100) | ✓ | 76.35% |  |
| 11 | `BeginDateBS` | 期初日期-资产负债表 | date | ✓ | 76.3% |  |
| 12 | `CompanyNatureBS` | 公司性质-资产负债表 | number(10) | ✓ | 76.35% | 公司性质-资产负债表(CompanyNatureBS)与(CT_SystemConst)表中的DM字段关联，令LB=13... |
| 13 | `AccountingStandardsBS` | 会计准则-资产负债表 | number(10) | ✓ | 76.35% | 会计准则-资产负债表(AccountingStandardsBS)与(CT_SystemConst)表中的DM字段关联，... |
| 14 | `MajoyCurrencyUnitBS` | 主货币类别-资产负债表 | number(10) | ✓ | 76.35% | 主货币类别-资产负债表(MajoyCurrencyUnitBS)与(CT_SystemConst)表中的DM字段关联，令... |
| 15 | `HasTwoCurrencyBS` | 是否有两个以上货币-资产负债表 | number(10) | ✓ | 76.35% | 是否有两个以上货币-资产负债表（HasTwoCurrencyBS）：与系统常量表（CT_SystemConst）中的DM... |
| 16 | `HasCashFlowStatement` | 是否有现金流量表 | number(10) | ✓ | 100.0% | 是否有现金流量表（HasCashFlowStatement）：与系统常量表（CT_SystemConst）中的DM字段关... |
| 17 | `HasPCCashFlowStatement` | 是否有母公司现金流量表 | number(10) | ✓ | 100.0% | 是否有母公司现金流量表（HasPCCashFlowStatement）：与系统常量表（CT_SystemConst）中的... |
| 18 | `InfoPublDateCS` | 信息发布日期-现金流量表 | date | ✓ | 77.35% |  |
| 19 | `InitialInfoPublDateCS` | 首次信息发布日期-现金流量表 | date | ✓ | 76.32% |  |
| 20 | `InfoSourceCS` | 信息来源-现金流量表 | varchar2(100) | ✓ | 77.35% |  |
| 21 | `FiscalYearCS` | 财政年度-现金流量表 | date | ✓ | 77.35% |  |
| 22 | `BeginDateCS` | 起始日期-现金流量表 | date | ✓ | 77.31% |  |
| 23 | `CompanyNatureCS` | 公司性质-现金流量表 | number(10) | ✓ | 77.35% | 公司性质-现金流量表(CompanyNatureCS)与(CT_SystemConst)表中的DM字段关联，令LB=13... |
| 24 | `AccountingStandardsCS` | 会计准则-现金流量表 | number(10) | ✓ | 77.35% | 会计准则-现金流量表(AccountingStandardsCS)与(CT_SystemConst)表中的DM字段关联，... |
| 25 | `MajoyCurrencyUnitCS` | 主货币单位-现金流量表 | number(10) | ✓ | 77.35% | 主货币单位-现金流量表(MajoyCurrencyUnitCS)与(CT_SystemConst)表中的DM字段关联，令... |
| 26 | `HasTwoCurrencyCS` | 是否有两个以上货币-现金流量表 | number(10) | ✓ | 77.35% | 是否有两个以上货币-现金流量表（HasTwoCurrencyCS）：与系统常量表（CT_SystemConst）中的DM... |
| 27 | `HasIncomeStatement` | 是否有利润分配表 | number(10) | ✓ | 100.0% | 是否有利润分配表（HasIncomeStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，... |
| 28 | `HasPCIncomeStatement` | 是否有母公司利润分配表 | number(10) | ✓ | 100.0% | 是否有母公司利润分配表（HasPCIncomeStatement）：与系统常量表（CT_SystemConst）中的DM... |
| 29 | `InfoPublDateIS` | 信息发布日期-利润分配表 | date | ✓ | 99.97% |  |
| 30 | `InitialInfoPublDateIS` | 首次信息发布日期-利润分配表 | date | ✓ | 99.09% |  |
| 31 | `InfoSourceIS` | 信息来源-利润分配表 | varchar2(100) | ✓ | 99.97% |  |
| 32 | `FiscalYearIS` | 财政年度-利润分配表 | date | ✓ | 99.97% |  |
| 33 | `BeginDateIS` | 起始日期-利润分配表 | date | ✓ | 99.91% |  |
| 34 | `CompanyNatureIS` | 公司性质-利润分配表 | number(10) | ✓ | 99.97% | 公司性质-利润分配表(CompanyNatureIS)与(CT_SystemConst)表中的DM字段关联，令LB=13... |
| 35 | `AccountingStandardsIS` | 会计准则-利润分配表 | number(10) | ✓ | 99.97% | 会计准则-利润分配表(AccountingStandardsIS)与(CT_SystemConst)表中的DM字段关联，... |
| 36 | `MajoyCurrencyUnitIS` | 主货币单位-利润分配表 | number(10) | ✓ | 99.97% | 主货币单位-利润分配表(MajoyCurrencyUnitIS)与(CT_SystemConst)表中的DM字段关联，令... |
| 37 | `HasTwoCurrencyIS` | 是否有两个以上货币-利润分配表 | number(10) | ✓ | 99.97% | 是否有两个以上货币-利润分配表（HasTwoCurrencyIS）：与系统常量表（CT_SystemConst）中的DM... |
| 38 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 39 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到所属公司股票的交易代码、简称等。

### DateTypeCode (日期标识)

日期标识(DateTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1314，得到日期标识的具体描述：1-1个月，2-2个月，3-3个月，4-4个月，5-5个月，6-半年度，7-7个月，8-8个月，9-9个月，10-10个月，11-11个月，12-年度，13-13个月，14-14个月，15-15个月，16-16个月，17-17个月，18-18个月，90-季度，99-其他。

### ReportType (报告类型)

报告类型（ReportType）：1-单季度报告；2-常规报表。

### HasBalanceSheet (是否有资产负债表)

是否有资产负债表（HasBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有资产负债表的描述：1-是；2-否。

### HasPCBalanceSheet (是否有母公司资产负债表)

是否有母公司资产负债表（HasPCBalanceSheet）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有母公司资产负债表的描述：1-是；2-否。

### CompanyNatureBS (公司性质-资产负债表)

公司性质-资产负债表(CompanyNatureBS)与(CT_SystemConst)表中的DM字段关联，令LB=1356，得到公司性质-资产负债表的具体描述：1-普通，2-金融，3-保险。

### AccountingStandardsBS (会计准则-资产负债表)

会计准则-资产负债表(AccountingStandardsBS)与(CT_SystemConst)表中的DM字段关联，令LB = 1357，得到会计准则-资产负债表的具体描述：7-国际会计准则，110-香港会计准则，120-澳门会计准则，502-美国会计准则，503-新加坡会计准则，510-国际会计准则及香港会计准则，520-中国会计准则(2007)，521-中国会计准则(1993)。

### MajoyCurrencyUnitBS (主货币类别-资产负债表)

主货币类别-资产负债表(MajoyCurrencyUnitBS)与(CT_SystemConst)表中的DM字段关联，令B = 1068 AND DM NOT IN (9900,9901,9990,9999,1002,1003) AND MS NOT LIKE '%废弃%'，得到主货币类别-资产负债表的具体描述：

### HasTwoCurrencyBS (是否有两个以上货币-资产负债表)

是否有两个以上货币-资产负债表（HasTwoCurrencyBS）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有两个以上货币-资产负债表的描述：1-是；2-否。

### HasCashFlowStatement (是否有现金流量表)

是否有现金流量表（HasCashFlowStatement）：与系统常量表（CT_SystemConst）中的DM字段关联，令LB=999，得到是否有现金流量表的描述：1-是；2-否。

## SQL示例

```sql
-- 查询 港股财报目录表 数据
SELECT *
FROM hk_finstatsdirectable
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
