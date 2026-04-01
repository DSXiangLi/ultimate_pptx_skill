# LC_ViolProcess

**中文名**: 违规事件进程

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ViolProcess` |
| MySQL表名 | `lc_violprocess` |
| 中文名 | 违规事件进程 |
| 路径 | 聚源新版数据库 > 诚信数据库 |
| 更新频率 | 不定时更新 |
| 字段数量 | 8 |
| 版本 | 1.01 |

## 表描述

1.该表记录每个违规事件下的每一步事件进程，包括事件进程、事件进程日期等指标。
2.数据范围：2014年-至今
3.信息来源：交易所、上市公司公告、证监会等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 违规事件表ID | number(19) | ✗ | 100.0% | 违规事件表ID（RID）：与违规事件表（LC_ViolatiEvent）ID关联。 |
| 3 | `AnnID` | 公告ID | number(19) | ✓ | 99.97% | 公告ID（AnnID）：与违规公告原文非文本（LC_ViolAnnouncement）ID关联 |
| 4 | `EventCode` | 事件编号 | number(10) | ✗ | 100.0% |  |
| 5 | `EventProcedure` | 事件进程 | number(10) | ✗ | 100.0% | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得到... |
| 6 | `ProcessDate` | 事件进程日期 | date | ✗ | 100.0% |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (违规事件表ID)

违规事件表ID（RID）：与违规事件表（LC_ViolatiEvent）ID关联。

### AnnID (公告ID)

公告ID（AnnID）：与违规公告原文非文本（LC_ViolAnnouncement）ID关联

### EventProcedure (事件进程)

事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得到事件进程的具体描述：1-正常，2-维持，3-立案调查，4-送达公告，5-举行听证，6-提起诉讼，7-审理终结，8-延期回复，9-已回复，98-不予受理，99-撤消。

## SQL示例

```sql
-- 查询 违规事件进程 数据
SELECT *
FROM lc_violprocess
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
