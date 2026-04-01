# MF_MainFinancialIndex

**中文名**: 公募基金报告期主要财务指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MainFinancialIndex` |
| MySQL表名 | `mf_mainfinancialindex` |
| 中文名 | 公募基金报告期主要财务指标 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金财务报表及分析 |
| 更新频率 | 半年更新 |
| 字段数量 | 27 |
| 版本 | 1.02 |

## 表描述

1.本表记录包含新会计准则下，基金在年报或半年报中披露的基金主要财务指标，并跟据新旧会计准则的科目对应关系，收录了指标的历史对应数据。
2.若某个报告期的数据有多次调整，则该表展示最新调整数据。
3.该表中各财务指标下数据对应的货币单位均为人民币元。
4.历史数据：1998年3月起-至今。
5.信息来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `BulletinType` | 公告类别 | number(10) | ✓ | 100.0% | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND ... |
| 8 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 9 | `AccountingStandards` | 会计准则 | number(10) | ✓ | 100.0% | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 14... |
| 10 | `TotalProfit` | 本期利润(元) | number(19,4) | ✓ | 99.8% |  |
| 11 | `NetIncome` | 本期利润扣减本期公允价值变动损益后的净额(元) | number(19,4) | ✓ | 98.85% |  |
| 12 | `TotalProfitPerShare` | 加权平均份额本期利润(元) | number(18,6) | ✓ | 92.99% |  |
| 13 | `DistributableProfits` | 期末可供分配利润(元) | number(19,4) | ✓ | 93.01% |  |
| 14 | `DistriProfitsPShare` | 期末可供分配份额利润(元) | number(18,6) | ✓ | 93.01% |  |
| 15 | `NetAssetsValue` | 期末基金资产净值(元) | number(19,4) | ✓ | 99.72% |  |
| 16 | `NVPerShare` | 期末基金份额净值(元) | number(18,6) | ✓ | 99.86% |  |
| 17 | `WANVProfitRate` | 本期加权平均净值利润率 | number(18,6) | ✓ | 92.96% |  |
| 18 | `UnitNVGrowthRate` | 本期份额净值增长率 | number(18,6) | ✓ | 99.76% |  |
| 19 | `UnitAccumulativeNVGR` | 份额累计净值增长率 | number(18,6) | ✓ | 99.79% |  |
| 20 | `TotalAsset` | 期末基金总资产(元) | number(19,4) | ✓ | 64.68% |  |
| 21 | `Gearing` | 期末基金总资产与净资产的比例 | number(18,6) | ✓ | 64.68% |  |
| 22 | `NetOperateCashFlow` | 本期经营活动产生的现金流量净额(元) | number(19,4) | ✓ | 0.1% |  |
| 23 | `TotalRevenue` | 本期收入(元) | number(19,4) | ✓ | 0.1% |  |
| 24 | `IndicativeFV` | 期末基金份额公允价值参考净值(元) | number(18,6) | ✓ | 0.02% |  |
| 25 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### BulletinType (公告类别)

公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN (5,6)，得到公告类别的具体描述：5-年度报告，6-中期报告。

### AccountingStandards (会计准则)

会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。

## SQL示例

```sql
-- 查询 公募基金报告期主要财务指标 数据
SELECT *
FROM mf_mainfinancialindex
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
