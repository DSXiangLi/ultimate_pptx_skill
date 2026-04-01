# DZ_FloatingSchedule

**中文名**: 限售股票解禁时间表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_FloatingSchedule` |
| MySQL表名 | `dz_floatingschedule` |
| 中文名 | 限售股票解禁时间表 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 19 |
| 版本 | 1 |

## 表描述

内容说明：收录上市公司（包括科创板）因为股权分置改革、定向增发、公开增发等原因所限售的股票的具体解禁时间，以上市公司为维度，不区分具体股东，主要包括可流通起始日、本次新增可售股份、已流通股份、待流通股份、总股本、股本变动原因说明等指标。
数据范围：国内上市公司
信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 3 | `InnerCode` | A股内部编码 | number(10) | ✗ | 100.0% | A股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 91.66% |  |
| 6 | `StartDateForFloating` | 可流通起始日 | date | ✗ | 100.0% |  |
| 7 | `NewMarketableAShares` | 本次新增可售A股(万股) | number(18,4) | ✓ | 100.0% |  |
| 8 | `Proportion1` | 本次新增可售A股占上期末已流通A股比例(%) | number(18,4) | ✓ | 100.0% |  |
| 9 | `AccuMarketableAShares` | 已流通A股(万股) | number(18,4) | ✓ | 100.0% |  |
| 10 | `NonMarketableAShares` | 待流通A股(万股) | number(18,4) | ✓ | 100.0% |  |
| 11 | `TotalAShares` | A股总数(万股) | number(18,4) | ✓ | 100.0% |  |
| 12 | `Proportion2` | 已流通A股占A股总数比例(%) | number(18,4) | ✓ | 100.0% |  |
| 13 | `TotalShares` | 总股本(万股) | number(18,4) | ✓ | 100.0% |  |
| 14 | `NewMarketableSharesSource` | 本次解禁股票来源 | varchar2(100) | ✓ | 100.0% |  |
| 15 | `SourceType` | 本次解禁股票来源代码 | number(10) | ✓ | 100.0% | 本次解禁股票来源代码(SourceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 ... |
| 16 | `ChangeReason` | 本次股本变动说明 | varchar2(255) | ✓ | 99.85% |  |
| 17 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### InnerCode (A股内部编码)

A股内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。

### SourceType (本次解禁股票来源代码)

本次解禁股票来源代码(SourceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM IN ('4','24','25','45','47','51','73','75','78','79','80','81','82','83','90')，得到本次解禁股票来源代码的具体描述：4-A股发行法人配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，45-职工股上市，47-外资法人股上市，51-其他，73-股权分置股份追送，75-股权分置限售流通，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，90-延长限售锁定期流通。

## SQL示例

```sql
-- 查询 限售股票解禁时间表 数据
SELECT *
FROM dz_floatingschedule
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
