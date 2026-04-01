# HK_FundSharesSplit

**中文名**: 香港基金拆分折算

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundSharesSplit` |
| MySQL表名 | `hk_fundsharessplit` |
| 中文名 | 香港基金拆分折算 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录香港互认基金和香港ETF的份额拆分等信息。
2.数据范围：1999年11月起--至今。
3.信息来源：港交所披露的相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金代码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 5 | `SplitSumPerUnit` | 拆分数量/每基金单位 | number(9,4) | ✓ | 100.0% |  |
| 6 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% |  |
| 7 | `Remark` | 备注说明 | varchar2(1000) | ✓ | 0.0% |  |
| 8 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金代码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 香港基金拆分折算 数据
SELECT *
FROM hk_fundsharessplit
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
