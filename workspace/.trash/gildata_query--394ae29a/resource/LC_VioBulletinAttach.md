# LC_VioBulletinAttach

**中文名**: 违规公告文号关联表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_VioBulletinAttach` |
| MySQL表名 | `lc_viobulletinattach` |
| 中文名 | 违规公告文号关联表 |
| 路径 | 聚源新版数据库 > 诚信数据库 |
| 更新频率 | 不定期更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

本表为LC_ViolAnnouncement的附表，用于存放公告对应的文号信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | 公告原文非文本ID | number(19) | ✗ | 100.0% | 公告原文非文本ID(RID)：与LC_ViolAnnouncement的ID关联，获取公告的相关信息。 |
| 3 | `IndiCategoryCode` | 指标类别代码 | number(10) | ✗ | 100.0% | 指标类别代码(IndiCategoryCode)：1-文号 |
| 4 | `IndiCategoryName` | 指标类别描述 | varchar2(100) | ✓ | 100.0% | 指标类别描述(IndiCategoryName)：1-文号 |
| 5 | `IndicatorCode` | 指标代码 | varchar2(100) | ✗ | 100.0% |  |
| 6 | `IndicatorDesc` | 指标描述 | varchar2(500) | ✓ | 0.0% |  |
| 7 | `Remark` | 备注 | varchar2(500) | ✓ | 0.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### RID (公告原文非文本ID)

公告原文非文本ID(RID)：与LC_ViolAnnouncement的ID关联，获取公告的相关信息。

### IndiCategoryCode (指标类别代码)

指标类别代码(IndiCategoryCode)：1-文号

### IndiCategoryName (指标类别描述)

指标类别描述(IndiCategoryName)：1-文号

## SQL示例

```sql
-- 查询 违规公告文号关联表 数据
SELECT *
FROM lc_viobulletinattach
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
