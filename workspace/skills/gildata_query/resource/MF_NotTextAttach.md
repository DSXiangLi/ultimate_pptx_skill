# MF_NotTextAttach

**中文名**: 公募基金公告原文非文本附表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_NotTextAttach` |
| MySQL表名 | `mf_nottextattach` |
| 中文名 | 公募基金公告原文非文本附表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金公告 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1.01 |

## 表描述

1.本表为MF_NotTextAnnouncement的附表，用于存放MF_NotTextAnnouncement表对应公告非文本的其他格式类型文件。文件格式包含：pdf、json、html。
2.历史数据：1998年3月起-至今。
3.数据来源：恒生聚源。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 字段：RID与MF_NotTextAnnouncement的ID关联，获取公告的相关信息，包含基金内部编码、媒体出处、信... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM I... |
| 5 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 6 | `HashCode` | MD5校验码 | varchar2(100) | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |
| 10 | `FileSize` | 文件大小(KB) | number(19,3) | ✓ | 76.57% |  |

## 字段说明

### RID (RID)

字段：RID与MF_NotTextAnnouncement的ID关联，获取公告的相关信息，包含基金内部编码、媒体出处、信息标题等；

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB = 1309 AND DM IN (1,5,29)，得到文件格式的具体描述：1-PDF，5-HTML，29-JSON。

## SQL示例

```sql
-- 查询 公募基金公告原文非文本附表 数据
SELECT *
FROM mf_nottextattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
