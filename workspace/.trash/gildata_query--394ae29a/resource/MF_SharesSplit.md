# MF_SharesSplit

**中文名**: 公募基金拆分折算

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_SharesSplit` |
| MySQL表名 | `mf_sharessplit` |
| 中文名 | 公募基金拆分折算 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益分配 |
| 更新频率 | 不定时更新 |
| 字段数量 | 29 |
| 版本 | 1.02 |

## 表描述

1.本表记录开放式基金的份额拆分、母子基金定期和不定期折算、ETF的份额折算、封转开的份额换算等信息。
2.历史数据：2005年2月起-至今。
3.信息来源：基金公司官网披露的相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 3 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `InfoType` | 信息类别 | number(10) | ✓ | 100.0% | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1409，得到信息类别的具... |
| 7 | `SplitType` | 拆分折算方式 | number(10) | ✓ | 100.0% | 拆分折算方式(SplitType)与(CT_SystemConst)表中的DM字段关联，令LB = 1993 AND D... |
| 8 | `SplitDay` | 拆分折算日_公布 | date | ✓ | 100.0% |  |
| 9 | `SplitDayEX` | 拆分折算日_场内_实际 | date | ✓ | 33.26% |  |
| 10 | `SplitRatio` | 拆分折算比例_公布(1:X) | number(19,10) | ✓ | 68.84% |  |
| 11 | `EsSplitRatio` | 拆分折算比例_预估(1:X) | number(19,10) | ✓ | 31.05% | 预估拆分折算比例(1:X)(EsSplitRatio )：该字段记录聚源计算的拆分折算比例数据，并非官方公布数据。 |
| 12 | `ActualSplitDay` | 拆分折算日_实际 | date | ✓ | 100.0% |  |
| 13 | `AFSplitRatio` | 拆分折算比例_复权(1:X) | number(19,10) | ✓ | 99.89% |  |
| 14 | `OutcomeNoticeIssueDate` | 结果公告日 | date | ✓ | 99.6% |  |
| 15 | `ChangeRegDate` | 份额变更登记日 | date | ✓ | 81.72% |  |
| 16 | `NV` | 基金资产净值 | number(19,4) | ✓ | 2.06% |  |
| 17 | `SharesBefore` | 拆分折算前份额 | number(19,2) | ✓ | 91.76% |  |
| 18 | `SharesAfter` | 拆分折算后份额 | number(19,2) | ✓ | 79.57% |  |
| 19 | `UnitNVBefore` | 拆分折算前单位净值 | number(19,8) | ✓ | 56.37% |  |
| 20 | `UnitNVAfter` | 拆分折算后单位净值 | number(19,8) | ✓ | 84.29% |  |
| 21 | `AccumulatedUnitNVBefore` | 拆分折算前累计净值 | number(19,8) | ✓ | 6.96% |  |
| 22 | `AccumulatedUnitNVAfter` | 拆分折算后累计净值 | number(19,8) | ✓ | 17.94% |  |
| 23 | `InnerCodeAdd` | 新增份额对象 | number(10) | ✓ | 37.2% | 新增份额对象（InnerCodeAdd）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 24 | `SplitRatioAdd` | 新增拆分比例(1:X) | number(19,9) | ✓ | 30.88% |  |
| 25 | `SharesAdd` | 新增份额 | number(19,6) | ✓ | 23.15% |  |
| 26 | `SharesAddCombine` | 新增份额(合并) | number(19,6) | ✓ | 3.36% |  |
| 27 | `Remark` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 28 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 29 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

基金代码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### InfoType (信息类别)

信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1409，得到信息类别的具体描述：1-份额拆分，2-份额折算(ETF)，3-原持有人份额补偿，4-封转开份额换算，5-份额合并。

### SplitType (拆分折算方式)

拆分折算方式(SplitType)与(CT_SystemConst)表中的DM字段关联，令LB = 1993 AND DM NOT IN (15)，得到拆分折算方式的具体描述：1-母子基金稳健份额定期折算，2-母子基金过渡期定期折算，3-母子基金转型份额转换，4-杠杆基金定期折算，5-杠杆基金不定期折算(上折)，6-杠杆基金不定期折算(下折)，7-杠杆基金到期折算/转换，8-一般基金份额拆分折算，9-ETF基金份额拆分折算，10-一般基金份额转换与合并，11-定开基金定期折算，12-定期支付定期折算，13-保本基金转入下一保本周期过渡折算，14-封转开份额折算，16-开转封份额折算，17-ETF基金转型份额转换。

### EsSplitRatio (拆分折算比例_预估(1:X))

预估拆分折算比例(1:X)(EsSplitRatio )：该字段记录聚源计算的拆分折算比例数据，并非官方公布数据。

### InnerCodeAdd (新增份额对象)

新增份额对象（InnerCodeAdd）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金拆分折算 数据
SELECT *
FROM mf_sharessplit
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
