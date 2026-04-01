# DZ_NewestFinaIndex

**中文名**: 公司最新财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_NewestFinaIndex` |
| MySQL表名 | `dz_newestfinaindex` |
| 中文名 | 公司最新财务指标 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司财务指标 |
| 更新频率 | 不定期更新 |
| 字段数量 | 30 |
| 版本 | 1.02 |

## 表描述

1.内容说明：展示上市公司最新财务指标，这些指标的主要特点是已经发生了变化，但尚未在报表中反映出来；
2.覆盖企业以下行为：新股发行/上市、送股、转增股、分红派现、配股除权/上市、增发、并购重组、股权激励、回购、超额配售、可转债转股；
3.数据范围：1997-12-31至今
4.信息来源：发行上市书、定期报告等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `AdjustDate` | 调整日期 | date | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `AdjustReason` | 调整原因说明 | varchar2(255) | ✓ | 100.0% |  |
| 6 | `EndDate` | 财报截止日期 | date | ✓ | 89.53% |  |
| 7 | `ShareCapitalBeforeAdjust` | 调整前股本(股) | number(19,4) | ✓ | 0.0% |  |
| 8 | `SHareCapitalIncr` | 股本增加额(股) | number(19,4) | ✓ | 0.0% |  |
| 9 | `ShareCapitalAftereAdjust` | 调整后股本(股) | number(19,4) | ✓ | 99.99% |  |
| 10 | `CapitalReserveBeforeAdjust` | 调整前资本公积(元) | number(19,4) | ✓ | 96.03% |  |
| 11 | `CapitalReserveIncr` | 资本公积增加额(元) | number(19,4) | ✓ | 8.98% |  |
| 12 | `CapitalReserveAfterAdjust` | 调整后资本公积(元) | number(19,4) | ✓ | 96.03% |  |
| 13 | `RetainedProfitBeforeAdjust` | 调整前未分配利润(元) | number(19,4) | ✓ | 97.78% |  |
| 14 | `RetainedProfitIncr` | 未分配利润增加额(元) | number(19,4) | ✓ | 8.83% |  |
| 15 | `RetainedProfitAfterAdjust` | 调整后未分配利润(元) | number(19,4) | ✓ | 97.78% |  |
| 16 | `SurplusReserveBeforeAdjust` | 调整前盈余公积(元) | number(19,4) | ✓ | 0.0% |  |
| 17 | `SurplusReserveIncr` | 盈余公积增加额(元) | number(19,4) | ✓ | 0.0% |  |
| 18 | `SurplusReserveAfterAdjust` | 调整后盈余公积)(元) | number(19,4) | ✓ | 0.0% |  |
| 19 | `NetAssetBeforeAdjust` | 调整前净资产(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `NetAssetIncr` | 净资产增加额(元) | number(19,4) | ✓ | 16.74% |  |
| 21 | `NetAssetAfterAdjust` | 调整后净资产(元) | number(19,4) | ✓ | 100.0% |  |
| 22 | `EPS` | 每股收益(摊薄)(元/股) | number(19,4) | ✓ | 99.99% |  |
| 23 | `EPSTTM` | 每股收益TTM(元/股) | number(19,4) | ✓ | 99.57% |  |
| 24 | `NAPS` | 每股净资产(元/股) | number(19,4) | ✓ | 99.99% |  |
| 25 | `RetainedProfitPS` | 每股未分配利润(元) | number(19,4) | ✓ | 99.99% |  |
| 26 | `CapitalReservePS` | 每股资本公积金(元) | number(19,4) | ✓ | 99.99% |  |
| 27 | `NetOperateCashFlowPS` | 每股经营活动现金流量净额(元) | number(19,4) | ✓ | 97.62% |  |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 30 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

## SQL示例

```sql
-- 查询 公司最新财务指标 数据
SELECT *
FROM dz_newestfinaindex
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
