# LC_IndexNews

**中文名**: 指数动态信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_IndexNews` |
| MySQL表名 | `lc_indexnews` |
| 中文名 | 指数动态信息 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 14 |
| 版本 | 1.02 |

## 表描述

1.内容说明：收录了指数发布机构发布的指数动态，包含指数停用、指数代码/简称变更以及成份券的定期/临时调整预告等。
2.数据范围：2011年12月至今
3.信息来源：中证指数有限公司、上海证券交易所、深圳证券交易所、深圳证券信息有限公司等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexInnerCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.47% |  |
| 5 | `ContentType` | 事件类型 | number(10) | ✓ | 100.0% | 事件类型(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1910 AND D... |
| 6 | `EffectiveDate` | 事件生效日期 | date | ✓ | 99.57% |  |
| 7 | `BeforeChange` | 变更前内容 | varchar2(500) | ✓ | 71.58% |  |
| 8 | `AfterChange` | 变更后内容 | varchar2(500) | ✓ | 86.96% |  |
| 9 | `Remark` | 备注 | varchar2(200) | ✓ | 98.97% |  |
| 10 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 11 | `JSID` | JSID | number(19) | ✗ |  |  |
| 12 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 13 | `PreIndexCode` | 变更前指数代码 | varchar2(100) | ✓ | 5.46% |  |
| 14 | `PreIndexAbbr` | 变更前指数简称 | varchar2(100) | ✓ | 9.63% |  |

## 字段说明

### IndexInnerCode (指数内部编码)

指数内部编码（IndexInnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等；与“指数基本情况表（LC_IndexBasicInfo）”中的“指数内部代码（IndexCode）”关联，得到指数的类别、发布机构、简介等。

### ContentType (事件类型)

事件类型(ContentType)与(CT_SystemConst)表中的DM字段关联，令LB = 1910 AND DM NOT IN (1,4,5)，得到事件类型的具体描述：2-指数终止，3-指数代码变更，6-其他，7-样本断档，8-英文名称变更，9-暂停上市，10-恢复上市，11-指数简称变更，12-指数名称变更，13-英文简称变更，14-行情变更，15-编制方案变更。

## SQL示例

```sql
-- 查询 指数动态信息 数据
SELECT *
FROM lc_indexnews
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
