# HK_BenchmarkAllocation

**中文名**: 香港基金基准配置

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_BenchmarkAllocation` |
| MySQL表名 | `hk_benchmarkallocation` |
| 中文名 | 香港基金基准配置 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.本表记录香港互认基金和香港ETF的参照的业绩比较基准，及所对应的起始日期、终止日期等信息。
2.历史数据：1999年起-至今。
3.信息来源：港交所、基金公司官网披露的产品说明书。
表数据更新频率： 日更新

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% | 基金内码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `IfExecuted` | 是否执行 | number(10) | ✓ | 100.0% | 是否执行(IfExecuted)，该字段固定以下常量：1-是；2-否 |
| 6 | `ExcuteDate` | 执行日期 | date | ✗ | 100.0% |  |
| 7 | `CancelDate` | 取消日期 | date | ✓ | 38.05% |  |
| 8 | `TracedIndexCode` | 参照基准指数内部编码 | number(10) | ✗ | 100.0% | 参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（Inner... |
| 9 | `IndexOriName` | 基准指数原始名称 | varchar2(500) | ✓ | 100.0% |  |
| 10 | `BenchWeight` | 基准权重 | number(18,6) | ✓ | 99.71% |  |
| 11 | `IfAfterTax` | 是否税后 | number(10) | ✓ | 0.0% | 是否税后(IfAfterTax)，该字段固定以下常量：1-是；2-否 |
| 12 | `IfCompound` | 是否复利 | number(10) | ✓ | 0.0% | 是否复利(IfCompound)，该字段固定以下常量：1-是；2-否 |
| 13 | `ExchangeRateInnerCode` | 汇率内部编码 | number(10) | ✓ | 0.29% | 汇率内部编码(ExchangeRateInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（Inn... |
| 14 | `Notes` | 业绩比较基准说明 | varchar2(500) | ✓ | 100.0% |  |
| 15 | `Remark` | 备注说明 | varchar2(500) | ✓ | 0.0% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内码)

基金内码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

### IfExecuted (是否执行)

是否执行(IfExecuted)，该字段固定以下常量：1-是；2-否

### TracedIndexCode (参照基准指数内部编码)

参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基准指数的交易代码、交易简称等。

### IfAfterTax (是否税后)

是否税后(IfAfterTax)，该字段固定以下常量：1-是；2-否

### IfCompound (是否复利)

是否复利(IfCompound)，该字段固定以下常量：1-是；2-否

### ExchangeRateInnerCode (汇率内部编码)

汇率内部编码(ExchangeRateInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得汇率的交易代码、简称等。

## SQL示例

```sql
-- 查询 香港基金基准配置 数据
SELECT *
FROM hk_benchmarkallocation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
