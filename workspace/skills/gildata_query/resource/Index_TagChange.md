# Index_TagChange

**中文名**: 指数标签变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_TagChange` |
| MySQL表名 | `index_tagchange` |
| 中文名 | 指数标签变动 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 17 |
| 版本 | 1.04 |

## 表描述

1.内容说明：收录指数的标签信息，风格（成长、价值）、规模（大盘、中盘、小盘等）、策略（红利股息、基本面、质量、等权、低波等）等。
2.数据范围：国内外主要指数
3.信息来源：聚源整理

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码(IndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TagCode` | 标签代码 | number(10) | ✗ | 100.0% |  |
| 4 | `TagName` | 标签名称 | varchar2(300) | ✓ | 100.0% |  |
| 5 | `Level` | 标签层级 | number(10) | ✗ | 100.0% |  |
| 6 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 7 | `CancelDate` | 取消日期 | date | ✓ | 0.0% |  |
| 8 | `IfEffected` | 是否有效 | number(10) | ✓ | 100.0% | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN... |
| 9 | `FirstTagCode` | 一级标签代码 | number(10) | ✓ | 100.0% |  |
| 10 | `FirstTagName` | 一级标签名称 | varchar2(300) | ✓ | 100.0% |  |
| 11 | `SecTagCode` | 二级标签代码 | number(10) | ✓ | 94.42% |  |
| 12 | `SecTagName` | 二级标签名称 | varchar2(300) | ✓ | 94.42% |  |
| 13 | `ThirdTagCode` | 三级标签代码 | number(10) | ✓ | 3.0% |  |
| 14 | `ThirdTagName` | 三级标签名称 | varchar2(300) | ✓ | 3.0% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码(IndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等信息

### IfEffected (是否有效)

是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。

## SQL示例

```sql
-- 查询 指数标签变动 数据
SELECT *
FROM index_tagchange
  AND IndexCode = 12345  -- 替换为实际的IndexCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
