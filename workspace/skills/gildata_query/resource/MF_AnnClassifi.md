# MF_AnnClassifi

**中文名**: 公募基金公告分类表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AnnClassifi` |
| MySQL表名 | `mf_annclassifi` |
| 中文名 | 公募基金公告分类表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金公告 |
| 更新频率 | 滚动更新 |
| 字段数量 | 8 |
| 版本 | 1 |

## 表描述

1.该表记录公募基金公告非文本的分类情况，类别分为三级，三级分类包括基金季报/中报/年报的全文/摘要、基金招募说明书、基金合同、基金托管协议、基金折算公告等，分类细致、明晰。
2.历史数据：1998.06--至今
3.信息来源：上交所、深交所、基金管理公司、巨潮、四大报披露的基金公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `NotTextAnnID` | 基金公告非文本ID | number(19) | ✗ | 100.0% | 基金公告非文本ID（NotTextAnnID）：与公募基金公告原文非文本（MF_NotTextAnnouncement）... |
| 3 | `Level1` | 一级分类 | number(10) | ✓ | 100.0% | 一级分类（Level1）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_... |
| 4 | `Level2` | 二级分类 | number(10) | ✓ | 100.0% | 二级分类（Level2）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_... |
| 5 | `Level3` | 三级分类 | number(10) | ✓ | 100.0% | 三级分类（Level3）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_... |
| 6 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 7 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 8 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### NotTextAnnID (基金公告非文本ID)

基金公告非文本ID（NotTextAnnID）：与公募基金公告原文非文本（MF_NotTextAnnouncement）表ID关联,获得公告的基本信息。

### Level1 (一级分类)

一级分类（Level1）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_AnnounceStru.Standard=1,获取公告一级分类的详细信息。

### Level2 (二级分类)

二级分类（Level2）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_AnnounceStru.Standard=2,获取公告二级分类的详细信息。

### Level3 (三级分类)

三级分类（Level3）：与公告分类指引（LC_AnnounceStru）公告类别编码（TypeCode）关联，令LC_AnnounceStru.Standard=3,获取公告三级分类的详细信息。

## SQL示例

```sql
-- 查询 公募基金公告分类表 数据
SELECT *
FROM mf_annclassifi
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
