# LC_MainQuarterData

**中文名**: 公司季度主要会计数据及财务指标_新会计准则

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_MainQuarterData` |
| MySQL表名 | `lc_mainquarterdata` |
| 中文名 | 公司季度主要会计数据及财务指标_新会计准则 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务指标 |
| 更新频率 | 季更新 |
| 字段数量 | 44 |
| 版本 | 1 |

## 表描述

1.反映上市公司的主要指标。
2.该表反映报告期为第三季度当季（7月-9月）财务数据。
3.该表中各财务科目的单位均为人民币元。
4.数据范围：2007-09-30至今
5.信息来源：定期报告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `BulletinType` | 公告类别 | varchar2(30) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 8 | `Mark` | 合并标志 | number(10) | ✓ | 100.0% | 合并标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN (1... |
| 9 | `BasicEPS` | 基本每股收益(元) | number(19,4) | ✓ | 99.92% |  |
| 10 | `DilutedEPS` | 稀释每股收益(元) | number(19,4) | ✓ | 95.37% |  |
| 11 | `BasicEPSCut` | 基本每股收益(扣除)(元) | number(19,4) | ✓ | 6.29% |  |
| 12 | `DilutedEPSCut` | 稀释每股收益(扣除)(元) | number(19,4) | ✓ | 0.07% |  |
| 13 | `EPS` | 每股收益(摊薄)(元) | number(19,4) | ✓ | 99.82% | 每股收益（摊薄）（EPS）：由归属于母公司所有者的净利润与最新总股本相除得来。 |
| 14 | `ROEByReport` | ##净资产收益率(摊薄)-原始披露(%) | number(18,4) | ✓ | 2.95% |  |
| 15 | `ROE` | 净资产收益率(摊薄)(%) | number(18,4) | ✓ | 9.38% | 净资产收益率（摊薄）（ROE）：由归属于母公司所有者的净利润与归属母公司的股东权益相除得来。 |
| 16 | `ROECut` | 净资产收益率(摊薄-扣除)(%) | number(18,4) | ✓ | 9.69% |  |
| 17 | `WROE` | 净资产收益率(加权)(%) | number(18,4) | ✓ | 89.08% |  |
| 18 | `WROECut` | 净资产收益率(加权-扣除)(%) | number(18,4) | ✓ | 18.14% |  |
| 19 | `OperatingReenue` | 营业收入(元) | number(19,4) | ✓ | 99.51% |  |
| 20 | `OperatingProfit` | 营业利润(元) | number(19,4) | ✓ | 51.61% |  |
| 21 | `TotalProfit` | 利润总额(元) | number(19,4) | ✓ | 51.56% |  |
| 22 | `NPFromParentCompanyOwners` | 净利润(不含少数损益)(元) | number(19,4) | ✓ | 99.97% |  |
| 23 | `NetProfitCut` | 扣除非经常性损益后净利润(元) | number(19,4) | ✓ | 76.07% |  |
| 24 | `ProfitatISA` | 国际会计准则净利润(元) | number(19,4) | ✓ | 0.0% |  |
| 25 | `MarginIntoOutStatement` | 境内外审计净利润差异说明 | clob | ✓ | 43.53% |  |
| 26 | `RetainedProfit` | 未分配利润(元) | number(19,4) | ✓ | 0.05% |  |
| 27 | `NetOperateCashFlow` | 经营活动现金流量净额(元) | number(19,4) | ✓ | 15.5% |  |
| 28 | `NetOperateCashFlowPS` | 每股经营活动现金流量净额(元) | number(19,4) | ✓ | 0.24% |  |
| 29 | `CashEquialentIncrease` | 现金及现金等价物净增加额(元) | number(19,4) | ✓ | 0.02% |  |
| 30 | `CashEquialents` | 货币资金(元) | number(19,4) | ✓ | 0.0% |  |
| 31 | `TotalAssets` | 总资产(元) | number(19,4) | ✓ | 0.0% |  |
| 32 | `SEWithoutMI` | 股东权益(不含少数权益)(元) | number(19,4) | ✓ | 0.0% |  |
| 33 | `NetAssetISA` | 国际会计准则净资产/股东权益(元) | number(19,4) | ✓ | 0.0% |  |
| 34 | `NAPSByReport` | ##每股净资产-原始披露(元) | number(19,4) | ✓ | 0.01% |  |
| 35 | `NAPS` | 每股净资产(元) | number(19,4) | ✓ | 0.0% |  |
| 36 | `NAPSAdjusted` | 调整后每股净资产(元) | number(19,4) | ✓ | 0.0% |  |
| 37 | `CapitalResereFund` | 资本公积金(元) | number(19,4) | ✓ | 0.05% |  |
| 38 | `TotalShares` | 总股本(股) | number(18,0) | ✓ | 99.99% |  |
| 39 | `DiidendFinancing` | 分配融资方案说明 | varchar2(200) | ✓ | 100.0% |  |
| 40 | `TotalRecompense` | 领导人报酬总额(元) | number(19,4) | ✓ | 0.0% |  |
| 41 | `FeeForAccountantOffice` | 会计师事务所费用(元) | number(19,4) | ✓ | 0.0% |  |
| 42 | `ModifiedAuditOpinion` | 非标准审计意见描述 | varchar2(100) | ✓ | 0.01% |  |
| 43 | `UpdateTime` | 更新日期 | date | ✓ |  |  |
| 44 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

### Mark (合并标志)

合并标志(Mark)与(CT_SystemConst)表中的DM字段关联，令LB = 1511 AND DM IN (1,2)，得到合并标志的具体描述：1-合并调整，2-合并未调整。

### EPS (每股收益(摊薄)(元))

每股收益（摊薄）（EPS）：由归属于母公司所有者的净利润与最新总股本相除得来。

### ROE (净资产收益率(摊薄)(%))

净资产收益率（摊薄）（ROE）：由归属于母公司所有者的净利润与归属母公司的股东权益相除得来。

## SQL示例

```sql
-- 查询 公司季度主要会计数据及财务指标_新会计准则 数据
SELECT *
FROM lc_mainquarterdata
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
