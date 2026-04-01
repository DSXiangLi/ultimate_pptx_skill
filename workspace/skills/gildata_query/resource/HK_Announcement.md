# HK_Announcement

**中文名**: 港股公司公告

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_Announcement` |
| MySQL表名 | `hk_announcement` |
| 中文名 | 港股公司公告 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1.02 |

## 表描述

1.本表记录港股公司公告及通告，以文本的形式提供公告内容。
该表可与港股公告原文表通过原文ID关联，获取完整的公告内容。
2.数据范围：2014年8月至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `ArticleID` | 原文ID | number(19) | ✓ | 100.0% | 原文ID（ArticleID）与港股公告原文（HK_NotTextAnnouncement）表ID关联，获取港股公告原文... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✓ | 100.0% | 证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `AnnounceTypeF` | 一级公告类别 | number(10) | ✓ | 100.0% | 一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceT... |
| 6 | `AnnounceTypeS` | 二级公告类别 | number(10) | ✓ | 100.0% | 一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceT... |
| 7 | `AnnounceTypeT` | 三级公告类别 | number(10) | ✓ | 100.0% | 一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceT... |
| 8 | `InfoTitle` | 公告标题 | varchar2(2000) | ✓ | 100.0% |  |
| 9 | `ContentType` | 内容类别 | number(10) | ✓ | 100.0% | 内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1855，得到内容类... |
| 10 | `Content` | 详细内容 | clob | ✓ | 99.95% |  |
| 11 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### ArticleID (原文ID)

原文ID（ArticleID）与港股公告原文（HK_NotTextAnnouncement）表ID关联，获取港股公告原文的信息。

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### AnnounceTypeF (一级公告类别)

一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。

### AnnounceTypeS (二级公告类别)

一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。

### AnnounceTypeT (三级公告类别)

一级公告类别(AnnounceTypeF),二级公告类别(AnnounceTypeS),三级公告类别(AnnounceTypeT):与“港股公告类别结构表(HK_AnnounceStru)”中的“公告类别编码(TypeCode)”关联，得到公告类别的具体描述。

### ContentType (内容类别)

内容类别(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1855，得到内容类别的具体描述：1-公告正文，2-公告摘要。

## SQL示例

```sql
-- 查询 港股公司公告 数据
SELECT *
FROM hk_announcement
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
