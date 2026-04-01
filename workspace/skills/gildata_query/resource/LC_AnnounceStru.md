# LC_AnnounceStru

**中文名**: 公告分类指引表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_AnnounceStru` |
| MySQL表名 | `lc_announcestru` |
| 中文名 | 公告分类指引表 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司公告资讯 |
| 更新频率 | 不定期更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

收录聚源最新制定的公告分类标准。三级公告类别隶属于二级公告类别，二级公告类别隶属于一级公告类别，一级分类主要分为股票、基金、债券、指数、其他等五个大类。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TypeCode` | 公告类别编码 | number(19) | ✗ | 100.0% |  |
| 3 | `TypeName` | 公告类别名称 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `FTypeCode` | 父级公告类别编码 | number(19) | ✓ | 98.5% |  |
| 5 | `Standard` | 公告类别级别 | number(10) | ✗ | 100.0% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效（IfEffected）：与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM... |
| 7 | `Remark` | 备注说明 | varchar2(100) | ✓ | 0.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IfEffected (是否有效)

是否有效（IfEffected）：与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 公告分类指引表 数据
SELECT *
FROM lc_announcestru
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
