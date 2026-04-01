# LC_ViolatiEvent

**中文名**: 违规事件表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_ViolatiEvent` |
| MySQL表名 | `lc_violatievent` |
| 中文名 | 违规事件表 |
| 路径 | 聚源新版数据库 > 诚信数据库 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.该表以事件为维度，记录单条违规事件最新公告日期、首次信息发布日期、最新事件进程、事项内容、涉及公司、涉及证券等指标。
2.数据范围：2014年-至今
3.信息来源：交易所、上市公司公告、证监会等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EventCode` | 事件编号 | number(10) | ✗ | 100.0% |  |
| 3 | `LatestInfoPublDate` | 最新公告日期 | date | ✗ | 100.0% |  |
| 4 | `InitialInfoPublDate` | 首次信息发布日期 | date | ✗ | 100.0% |  |
| 5 | `NewestProcess` | 最新事件进程 | number(10) | ✓ | 100.0% | 最新事件进程(NewestProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得... |
| 6 | `EventContent` | 事项内容 | clob | ✓ | 0.69% |  |
| 7 | `InvolvedCompany` | 涉及公司 | number(10) | ✗ |  |  |
| 8 | `InvolvedSecurity` | 涉及证券 | number(10) | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### NewestProcess (最新事件进程)

最新事件进程(NewestProcess)与(CT_SystemConst)表中的DM字段关联，令LB = 1747，得到最新事件进程的具体描述：1-正常，2-维持，3-立案调查，4-送达公告，5-举行听证，6-提起诉讼，7-审理终结，8-延期回复，9-已回复，98-不予受理，99-撤消。

## SQL示例

```sql
-- 查询 违规事件表 数据
SELECT *
FROM lc_violatievent
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
