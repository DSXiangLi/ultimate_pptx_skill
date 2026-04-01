# LC_AnnClassifi

**中文名**: 股票公告分类

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AnnClassifi` |
| MySQL表名 | `lc_annclassifi` |
| 中文名 | 股票公告分类 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 滚动更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.根据聚源制定的最新公告分类标准，收录股票类公告的具体分类信息，包括一级分类，二级分类，三级分类三个层级，可根据分类筛选特定类型的公告信息。
2.数据范围：证券上市-至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 非文本ID | number(19) | ✗ | 100.0% | 非文本ID（RID）：与公司公告原文非文本（LC_NotTextAnnouncement）表ID关联或与公司公告（不含原... |
| 3 | `Level1` | 一级分类 | number(10) | ✓ | 100.0% | 一级分类（Level1）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告... |
| 4 | `Level2` | 二级分类 | number(10) | ✓ | 100.0% | 二级分类（Level2）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告... |
| 5 | `Level3` | 三级分类 | number(10) | ✓ | 100.0% | 三级分类（Level3）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (非文本ID)

非文本ID（RID）：与公司公告原文非文本（LC_NotTextAnnouncement）表ID关联或与公司公告（不含原文）（LC_AnnouncementInfo）表ID关联。

### Level1 (一级分类)

一级分类（Level1）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告分类的详细信息。

### Level2 (二级分类)

二级分类（Level2）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告分类的详细信息。

### Level3 (三级分类)

三级分类（Level3）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，获取公告分类的详细信息。

## SQL示例

```sql
-- 查询 股票公告分类 数据
SELECT *
FROM lc_annclassifi
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
