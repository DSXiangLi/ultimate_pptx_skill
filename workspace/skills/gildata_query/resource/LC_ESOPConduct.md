# LC_ESOPConduct

**中文名**: 员工持股计划实施情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ESOPConduct` |
| MySQL表名 | `lc_esopconduct` |
| 中文名 | 员工持股计划实施情况 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公司治理 |
| 更新频率 | 不定时更新 |
| 字段数量 | 25 |
| 版本 | 1.03 |

## 表描述

1.主要记录员工持股计划当期实施情况：包括相关日期、实施股份、实施价格等指标。
2.数据范围：2014.6-至今
3.信息来源：上市公司公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✓ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✓ | 0.0% | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得... |
| 4 | `IniInfoPublDate` | 首次信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `SerialNumber` | 员工持股计划序号 | number(10) | ✓ | 100.0% |  |
| 6 | `IfPeriod` | 是否分期实施 | number(10) | ✓ | 100.0% | 是否分期实施(IfPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 7 | `Period` | 分期实施期次 | number(10) | ✓ | 100.0% |  |
| 8 | `InitialImpleDay` | 首次实施公告日 | date | ✓ | 100.0% |  |
| 9 | `ImplementDate` | 实施公告日 | date | ✓ | 100.0% |  |
| 10 | `ImpleEndDate` | 实施截止日 | date | ✓ | 100.0% |  |
| 11 | `ShareSource` | 本次实施股票来源 | varchar2(2000) | ✓ | 100.0% |  |
| 12 | `PriceCelling` | 本次实施价格上限(元) | number(19,4) | ✓ | 90.91% |  |
| 13 | `PriceFloor` | 本次实施价格下限(元) | number(19,4) | ✓ | 90.91% |  |
| 14 | `AvgPrice` | 本次实施均价(元) | number(19,4) | ✓ | 90.73% |  |
| 15 | `ImplementShare` | 本次实施股份(股) | number(19) | ✓ | 100.0% |  |
| 16 | `Proportion` | 本次实施占总股本比例 | number(9,6) | ✓ | 97.11% |  |
| 17 | `LockDuration` | 锁定期(月) | number(19,2) | ✓ | 98.25% |  |
| 18 | `Counterpart` | 股票实施赠与方 | varchar2(2000) | ✓ | 0.0% |  |
| 19 | `AccumulateShare` | 累计实施股份(股) | number(19,2) | ✓ | 100.0% |  |
| 20 | `AccuProportion` | 累计占总股本比例 | number(9,6) | ✓ | 97.32% |  |
| 21 | `Statement` | 实施情况说明 | varchar2(4000) | ✓ | 100.0% |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |
| 24 | `ShareCelling` | 本次实施股份上限(股) | number(19,2) | ✓ | 100.0% |  |
| 25 | `ShareFloor` | 本次实施股份下限(股) | number(19,2) | ✓ | 100.0% |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。

### IfPeriod (是否分期实施)

是否分期实施(IfPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否分期实施的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 员工持股计划实施情况 数据
SELECT *
FROM lc_esopconduct
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
