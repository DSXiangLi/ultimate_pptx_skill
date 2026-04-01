# HK_SHSellingList

**中文名**: 港股卖空名单表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_SHSellingList` |
| MySQL表名 | `hk_shsellinglist` |
| 中文名 | 港股卖空名单表 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股行情 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.记录港股指定卖空名单变化，包含字段有：信息发布日期、豁免卖空价规例、入选日期、剔除日期等。
2.数据范围：2016-05至今。
3.数据来源：港交所。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `ExempSPRule` | 豁免卖空价规例 | number(10) | ✓ | 100.0% | 豁免卖空价规例（ExempSPRule），该字段固定以下常量：1-是，2-否。 |
| 5 | `InDate` | 入选日期 | date | ✗ | 100.0% |  |
| 6 | `OutDate` | 剔除日期 | date | ✓ | 56.64% |  |
| 7 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% | 是否有效（IfEffected），该字段固定以下常量：1-是，2-否。 |
| 8 | `Remarks` | 备注 | varchar2(200) | ✓ | 9.2% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### ExempSPRule (豁免卖空价规例)

豁免卖空价规例（ExempSPRule），该字段固定以下常量：1-是，2-否。

### IfEffected (是否有效)

是否有效（IfEffected），该字段固定以下常量：1-是，2-否。

## SQL示例

```sql
-- 查询 港股卖空名单表 数据
SELECT *
FROM hk_shsellinglist
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
