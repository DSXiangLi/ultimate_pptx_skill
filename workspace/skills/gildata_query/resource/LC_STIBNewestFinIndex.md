# LC_STIBNewestFinIndex

**中文名**: 科创板最新财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBNewestFinIndex` |
| MySQL表名 | `lc_stibnewestfinindex` |
| 中文名 | 科创板最新财务指标 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 财务指标 |
| 更新频率 | 不定期更新 |
| 字段数量 | 25 |
| 版本 | 1 |

## 表描述

1.内容说明：收录科创板公司最新的一些财务指标，这些指标的主要特点是已经发生了变化，但尚未在报表中反映出来；
2.覆盖企业以下行为：新股发行/上市、送股、转增股、分红派现、配股除权/上市、增发、并购重组、股权激励、回购、超额配售、可转债转股；
3.数据范围：科创板上市至今
4.信息来源：科创板公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `AdjustDate` | 调整日期 | date | ✗ | 100.0% |  |
| 5 | `AdjustReason` | 调整原因说明 | varchar2(255) | ✓ | 100.0% |  |
| 6 | `EndDate` | 财报截止日期 | date | ✗ | 100.0% |  |
| 7 | `NewestTotalShares` | 最新总股本(股) | number(19,4) | ✓ | 100.0% |  |
| 8 | `CapitalResBeforeAdjust` | 调整前资本公积(元) | number(19,4) | ✓ | 98.3% |  |
| 9 | `CapitalResIncr` | 资本公积增加额(元) | number(19,4) | ✓ | 16.85% |  |
| 10 | `CapitalResAfterAdjust` | 调整后资本公积(元) | number(19,4) | ✓ | 98.3% |  |
| 11 | `RetaProfitBeforeAdjust` | 调整前未分配利润(元) | number(19,4) | ✓ | 98.71% |  |
| 12 | `RetaProfitIncr` | 未分配利润增加额(元) | number(19,4) | ✓ | 10.0% |  |
| 13 | `RetaProfitAfterAdjust` | 调整后未分配利润(元) | number(19,4) | ✓ | 98.71% |  |
| 14 | `NetAssetBeforeAdjust` | 调整前净资产(元) | number(19,4) | ✓ | 100.0% |  |
| 15 | `NetAssetIncr` | 净资产增加额(元) | number(19,4) | ✓ | 23.37% |  |
| 16 | `NetAssetAfterAdjust` | 调整后净资产(元) | number(19,4) | ✓ | 100.0% |  |
| 17 | `EPS` | 每股收益(摊薄)(元) | number(19,4) | ✓ | 100.0% | 每股收益(摊薄)（EPS）＝净利润/期末股本,分子取最近一个报告期的净利润,分母取这次调整后的股本 |
| 18 | `EPSTTM` | 每股收益TTM(元) | number(19,4) | ✓ | 100.0% | 每股收益TTM（元/股）(EPSTTM)＝最近四个季度净利润之和/期末股本，分母取这次调整后的股本。 |
| 19 | `NAPS` | 每股净资产(元) | number(19,4) | ✓ | 100.0% | 每股净资产（NAPS）＝（净资产-其他权益工具）/股本,分子分母取经过这次调整后的净资产和股本 |
| 20 | `RetainedProfitPS` | 每股未分配利润(元) | number(19,4) | ✓ | 100.0% | 每股未分配利润（RetainedProfitPS）=期末未分配利润/股本,分子分母取经过这次调整后的未分配利润和股本 |
| 21 | `CapitalReservePS` | 每股资本公积金(元) | number(19,4) | ✓ | 100.0% | 每股公积金（CapitalReservePS）=资本公积/股本,分子分母取经过这次调整后的资本公积和股本 |
| 22 | `NetOperateCashFlowPS` | 每股经营活动现金流量净额(元) | number(19,4) | ✓ | 99.95% | 每股经营活动现金流量净额（NetOperateCashFlowPS）=经营活动现金净流入/股本,分子取最近一个报告期的经... |
| 23 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 24 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### EPS (每股收益(摊薄)(元))

每股收益(摊薄)（EPS）＝净利润/期末股本,分子取最近一个报告期的净利润,分母取这次调整后的股本

### EPSTTM (每股收益TTM(元))

每股收益TTM（元/股）(EPSTTM)＝最近四个季度净利润之和/期末股本，分母取这次调整后的股本。

### NAPS (每股净资产(元))

每股净资产（NAPS）＝（净资产-其他权益工具）/股本,分子分母取经过这次调整后的净资产和股本

### RetainedProfitPS (每股未分配利润(元))

每股未分配利润（RetainedProfitPS）=期末未分配利润/股本,分子分母取经过这次调整后的未分配利润和股本

### CapitalReservePS (每股资本公积金(元))

每股公积金（CapitalReservePS）=资本公积/股本,分子分母取经过这次调整后的资本公积和股本

### NetOperateCashFlowPS (每股经营活动现金流量净额(元))

每股经营活动现金流量净额（NetOperateCashFlowPS）=经营活动现金净流入/股本,分子取最近一个报告期的经营活动现金净流入,分母取这次调整后的股本

## SQL示例

```sql
-- 查询 科创板最新财务指标 数据
SELECT *
FROM lc_stibnewestfinindex
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
