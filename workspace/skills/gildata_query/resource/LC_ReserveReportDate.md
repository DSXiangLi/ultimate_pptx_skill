# LC_ReserveReportDate

**中文名**: 财务报告预约披露日

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ReserveReportDate` |
| MySQL表名 | `lc_reservereportdate` |
| 中文名 | 财务报告预约披露日 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司财务报表 |
| 更新频率 | 不定时更新 |
| 字段数量 | 17 |
| 版本 | 1.05 |

## 表描述

1.收录上市公司（剔除科创板）定期报告预约披露日信息，包括公告类别、预约披露起始与截止日和实际披露日期等内容。
2.数据范围：1990-12-28至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `NoticeStartDate` | 预约披露起始日 | date | ✗ | 100.0% |  |
| 5 | `NoticeType` | 提示信息类别 | number(10) | ✗ | 100.0% | 提示信息类别(NoticeType)与(CT_SystemConst)表中的DM字段关联，令LB = 204 AND D... |
| 6 | `DateType` | 披露日期类别 | number(10) | ✓ | 100.0% | 披露日期类别(DateType)与(CT_SystemConst)表中的DM字段关联，令LB = 2372，得到披露日期... |
| 7 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 8 | `ActualDate` | 实际披露日期 | date | ✓ | 99.94% |  |
| 9 | `CorrectNum` | 更正公告披露次数 | number(10) | ✓ | 100.0% | 与 财务报告预约披露日附表（LC_ResReportDateAtta）表的RID关联，对应更正公告披露日期加总得到更正公... |
| 10 | `NoticeContent` | 提示信息内容 | clob | ✓ | 33.85% |  |
| 11 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM ... |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |
| 15 | `BulletinTypeName` | 公告类别名称(废弃) | varchar2(200) | ✓ | 100.0% |  |
| 16 | `BulletinType` | 公告类别(废弃) | number(10) | ✓ | 100.0% |  |
| 17 | `NoticeEndDate` | 预约披露截止日(废弃) | date | ✓ | 100.0% |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### NoticeType (提示信息类别)

提示信息类别(NoticeType)与(CT_SystemConst)表中的DM字段关联，令LB = 204 AND DM IN (50,51,52,53)，得到提示信息类别的具体描述：50-中报预约披露日，51-年报预约披露日，52-第一季报预约披露日，53-第三季报预约披露日。

### DateType (披露日期类别)

披露日期类别(DateType)与(CT_SystemConst)表中的DM字段关联，令LB = 2372，得到披露日期类别的具体描述：1-首次预约日期，2-第一次变更日期，3-第二次变更日期，4-第三次变更日期，5-第四次变更日期，6-第五次变更日期。

### CorrectNum (更正公告披露次数)

与
财务报告预约披露日附表（LC_ResReportDateAtta）表的RID关联，对应更正公告披露日期加总得到更正公告披露次数的相关信息。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 财务报告预约披露日 数据
SELECT *
FROM lc_reservereportdate
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
