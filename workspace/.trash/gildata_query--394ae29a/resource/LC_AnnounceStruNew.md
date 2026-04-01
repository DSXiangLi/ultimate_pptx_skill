# LC_AnnounceStruNew

**中文名**: 公告分类指引表(新)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AnnounceStruNew` |
| MySQL表名 | `lc_announcestrunew` |
| 中文名 | 公告分类指引表(新) |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

收录聚源最新制定的公告分类标准，涵盖四级分类标签层级，一级分类从股票、公募基金、债券、CDR、指数、公司、违法违规、港股基金8个维度关注公告披露的信息。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `AnnTypeCode` | 公告类别编码 | varchar2(12) | ✗ | 100.0% |  |
| 3 | `AnnTypeName` | 公告类别名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `AnnFTypeCode` | 公告父级类别编码 | varchar2(12) | ✓ | 100.0% | 公告父级类别编码（AnnFTypeCode）：此字段是公告类别编（AnnTypeCode）上一层级的类别编码。 |
| 5 | `AnnLevel` | 公告级别 | number(10) | ✗ | 100.0% | 公告级别（AnnLevel)：分成了一级、二级、三级、四级这四个层级，限定四级标签，可获取明细指标。 |
| 6 | `IfEffected` | 是否有效 | varchar2(12) | ✗ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM ... |
| 7 | `Remark` | 备注 | varchar2(100) | ✓ | 0.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### AnnFTypeCode (公告父级类别编码)

公告父级类别编码（AnnFTypeCode）：此字段是公告类别编（AnnTypeCode）上一层级的类别编码。

### AnnLevel (公告级别)

公告级别（AnnLevel)：分成了一级、二级、三级、四级这四个层级，限定四级标签，可获取明细指标。

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 and DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公告分类指引表(新) 数据
SELECT *
FROM lc_announcestrunew
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
