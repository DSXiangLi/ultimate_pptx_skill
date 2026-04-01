# LC_PositionAtta

**中文名**: 公司领导人职务变动附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_PositionAtta` |
| MySQL表名 | `lc_positionatta` |
| 中文名 | 公司领导人职务变动附表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司人力资源 |
| 更新频率 | 不定期更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

内容说明：本表收录上市公司高管职务变动公告日期的追溯
数据范围：2021年起新增数据
信息来源：申报稿、招股说明书、临时公告

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID：本字段和<公司领导人任职情况 LC_LeaderPosition>的[ID]关联 |
| 3 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(200) | ✓ | 99.97% |  |
| 5 | `TermNumIn` | 任职届次 | number(10) | ✓ | 47.78% |  |
| 6 | `AdjustType` | 调整类型 | number(10) | ✗ | 100.0% | 调整类型(AdjustType)与(CT_SystemConst)表中的DM字段关联，令LB=2379，得到调整类型的具... |
| 7 | `AdjustDate` | 调整日期 | date | ✓ | 99.97% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID：本字段和<公司领导人任职情况 LC_LeaderPosition>的[ID]关联

### AdjustType (调整类型)

调整类型(AdjustType)与(CT_SystemConst)表中的DM字段关联，令LB=2379，得到调整类型的具体描述：10-提名候选，20-职务任职，21-职务续任，22-代理职务，50-职务离任，51-代理结束，90-取消候选提名资格，91-否决提名候选议案。

## SQL示例

```sql
-- 查询 公司领导人职务变动附表 数据
SELECT *
FROM lc_positionatta
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
