# HK_FundAnnounceFile

**中文名**: 香港基金公告转换文件表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundAnnounceFile` |
| MySQL表名 | `hk_fundannouncefile` |
| 中文名 | 香港基金公告转换文件表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

存放香港基金公告源文件转换后的PDF、HTML、JSON、TXT格式文件，满足不同客户公告展示的需求。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | RID与HK_FundNotTextAnnounce的ID关联，获取公告的信息标题、媒体出处等相关信息。 |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `FileType` | 文件格式 | number(10) | ✗ | 100.0% | 文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309 AND DM IN ... |
| 5 | `Content` | 信息内容 | blob | ✓ | 0.0% |  |
| 6 | `HashCode` | MD5校验码 | varchar2(100) | ✗ | 100.0% |  |
| 7 | `FileSize` | 文件大小(KB) | number(19,3) | ✗ | 100.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

RID与HK_FundNotTextAnnounce的ID关联，获取公告的信息标题、媒体出处等相关信息。

### FileType (文件格式)

文件格式(FileType)与(CT_SystemConst)表中的DM字段关联，令LB=1309 AND DM IN (1,3,5,29)，得到文件格式的具体描述：1-PDF，3-TXT，5-HTML，29-JSON。

## SQL示例

```sql
-- 查询 香港基金公告转换文件表 数据
SELECT *
FROM hk_fundannouncefile
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
