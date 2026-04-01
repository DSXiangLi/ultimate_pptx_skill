# LC_AnnounceClassifi

**中文名**: 公告分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AnnounceClassifi` |
| MySQL表名 | `lc_announceclassifi` |
| 中文名 | 公告分类表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 滚动更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

根据聚源最新制定的公告分类标准，收录了股票、基金、债券、CDR、指数、公司、违法违规类公告的具体分类信息，可根据分类筛选特定类型的公告信息。
数据范围： 2018年-至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% | 非文本ID：可与公司公告原文非文本（LC_NotTextAnnouncement）表ID关联、与公募基金公告原文非文本（... |
| 3 | `AnnLevel1` | 一级公告分类 | varchar2(12) | ✓ | 100.0% | 与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细... |
| 4 | `AnnLevel2` | 二级公告分类 | varchar2(12) | ✓ | 100.0% | 与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细... |
| 5 | `AnnLevel3` | 三级公告分类 | varchar2(12) | ✓ | 100.0% | 与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细... |
| 6 | `AnnLevel4` | 四级公告分类 | varchar2(12) | ✗ | 100.0% | 与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细... |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (RID)

非文本ID：可与公司公告原文非文本（LC_NotTextAnnouncement）表ID关联、与公募基金公告原文非文本（MF_NotTextAnnouncement）表ID关联、与债券公告非文本（Bond_NotTextAnnounce）表ID关联、与CDR公告原文非文本（LC_CDRNotTextAnnounce）表ID关联、与指数公告原文非文本（Index_NotTextAnnounce）表ID关联、与公司公告原文非文本(DZ_NotTextAnnouncement)表ID关联、与科创板公司公告原文主表
(LC_STIBNotTextAnnounce)表ID关联。

### AnnLevel1 (一级公告分类)

与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细信息。

### AnnLevel2 (二级公告分类)

与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细信息。

### AnnLevel3 (三级公告分类)

与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细信息。

### AnnLevel4 (四级公告分类)

与公告分类指引表新（LC_AnnounceStruNew）公告类别编码（AnnTypeCode）关联，获取公告分类的详细信息。

## SQL示例

```sql
-- 查询 公告分类表 数据
SELECT *
FROM lc_announceclassifi
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
