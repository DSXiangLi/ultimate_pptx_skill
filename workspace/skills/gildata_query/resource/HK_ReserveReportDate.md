# HK_ReserveReportDate

**中文名**: 港股财务报告预约披露日

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_ReserveReportDate` |
| MySQL表名 | `hk_reservereportdate` |
| 中文名 | 港股财务报告预约披露日 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股业绩与财务 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.内容说明：收录香港上市公司定期报告预约披露日信息，包括预约披露起始与截止日等内容。
2.数据范围：2023-01至今
3.信息来源：港交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `ReportType` | 报表类型 | number(10) | ✓ | 100.0% | 报表类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 204 AND DM ... |
| 6 | `PeriodMark` | 日期标志 | number(10) | ✗ | 100.0% | 日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314 AND DM I... |
| 7 | `NoticeStartDate` | 预约披露起始日 | date | ✗ | 100.0% |  |
| 8 | `NoticeEndDate` | 预约披露截止日 | date | ✓ | 100.0% |  |
| 9 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN... |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### ReportType (报表类型)

报表类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 204 AND DM IN (50,51,52,53)，得到报表类型的具体描述：50-中报预约披露日，51-年报预约披露日，52-第一季报预约披露日，53-第三季报预约披露日。

### PeriodMark (日期标志)

日期标志(PeriodMark)与(CT_SystemConst)表中的DM字段关联，令LB=1314 AND DM IN (3,6,8,9,12,15,18)，得到日期标志的具体描述：3-3个月，6-半年度，8-8个月，9-9个月，12-年度，15-15个月，18-18个月。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 港股财务报告预约披露日 数据
SELECT *
FROM hk_reservereportdate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
