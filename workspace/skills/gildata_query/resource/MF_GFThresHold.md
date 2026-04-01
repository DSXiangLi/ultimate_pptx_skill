# MF_GFThresHold

**中文名**: 公募基金_分级基金阀值

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_GFThresHold` |
| MySQL表名 | `mf_gfthreshold` |
| 中文名 | 公募基金_分级基金阀值 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 分级基金 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.记录分级基金不定期折算的阀值，即达到这个值，分级基金将进行上折或下折的操作。尤其是下折的操作，会对投资者产生较大的影响。
2.历史数据：2007年7月起-至今。
3.数据来源：基金产品招募说明书。
4.数据未更新原因：公募分级基金业务已终止。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 公告日期 | date | ✓ | 100.0% |  |
| 4 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 6 | `ThresHoldType` | 阀值类型 | number(10) | ✓ | 100.0% | 阀值类型(ThresHoldType)与(CT_SystemConst)表中的DM字段关联，令LB = 1873，得到阀... |
| 7 | `ReLation` | 条件关系 | number(10) | ✓ | 100.0% | 条件关系(ReLation)与(CT_SystemConst)表中的DM字段关联，令LB = 1872，得到条件关系的具... |
| 8 | `ThresHold` | 阀值 | number(9,6) | ✓ | 100.0% |  |
| 9 | `TriggerDays` | 触发所需天数(日) | number(10) | ✓ | 100.0% |  |
| 10 | `SplitType` | 阀值折算方式 | number(10) | ✓ | 100.0% |  |
| 11 | `RelatedInnerCode` | 比较基金代码 | number(10) | ✓ | 0.67% | 比较基金代码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCod... |
| 12 | `TrampShareCon` | 份额折算说明 | varchar2(1000) | ✓ | 100.0% |  |
| 13 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 14 | `Remark` | 备注 | varchar2(1000) | ✓ | 0.0% |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ThresHoldType (阀值类型)

阀值类型(ThresHoldType)与(CT_SystemConst)表中的DM字段关联，令LB = 1873，得到阀值类型的具体描述：1-固定净值，2-倍数。

### ReLation (条件关系)

条件关系(ReLation)与(CT_SystemConst)表中的DM字段关联，令LB = 1872，得到条件关系的具体描述：1-大于等于，2-大于，3-小于等于，4-小于。

### RelatedInnerCode (比较基金代码)

比较基金代码（RelatedInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公募基金_分级基金阀值 数据
SELECT *
FROM mf_gfthreshold
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
