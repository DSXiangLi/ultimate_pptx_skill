# MF_BenchmarkAllocation

**中文名**: 公募基金基准配置

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_BenchmarkAllocation` |
| MySQL表名 | `mf_benchmarkallocation` |
| 中文名 | 公募基金基准配置 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金基本资料 |
| 更新频率 | 日更新 |
| 字段数量 | 20 |
| 版本 | 1 |

## 表描述

1.本表记录基金业绩比较基准的相关配置信息，如基准指数及比例、执行取消日期等
2.数据范围：2002年4月至今
3.信息来源：基金公司官网披露的产品说明书

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✗ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `ExcuteDate` | 执行日期 | date | ✗ | 100.0% |  |
| 7 | `CancelDate` | 取消日期 | date | ✓ | 25.67% |  |
| 8 | `TracedIndexCode` | 参照基准指数内部编码 | number(10) | ✗ | 100.0% | 参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（Inner... |
| 9 | `TopWeight` | 基准权重上限 | number(18,6) | ✓ | 98.8% |  |
| 10 | `MinimumWeight` | 基准权重下限 | number(18,6) | ✓ | 98.8% |  |
| 11 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 12 | `OperationMark` | 运算标志 | number(10) | ✓ | 1.2% | 运算标志(OperationMark)与(CT_SystemConst)表中的DM字段关联，令LB=1862，得到运算标... |
| 13 | `Constant` | 常数 | number(18,6) | ✓ | 1.2% |  |
| 14 | `IfAfterTax` | 是否税后 | number(10) | ✓ | 17.69% | 是否税后(IfAfterTax)，该字段固定以下常量：1-是；2-否 |
| 15 | `IfCompound` | 是否复利 | number(10) | ✓ | 17.69% | 是否复利(IfCompound)，该字段固定以下常量：1-是；2-否 |
| 16 | `ExchangeRateInnerCode` | 汇率内部编码 | number(10) | ✓ | 5.28% | 汇率内部编码(ExchangeRateInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（Inn... |
| 17 | `IfExecuted` | 是否执行 | number(10) | ✓ | 100.0% | 是否执行(IfExecuted)，该字段固定以下常量：1-是；2-否 |
| 18 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 19 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 20 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TracedIndexCode (参照基准指数内部编码)

参照基准指数内部编码(TracedIndexCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基准指数的交易代码、交易简称等。

### OperationMark (运算标志)

运算标志(OperationMark)与(CT_SystemConst)表中的DM字段关联，令LB=1862，得到运算标志的具体描述：1-加，2-减，3-乘，4-除，5-max，6-min。

### IfAfterTax (是否税后)

是否税后(IfAfterTax)，该字段固定以下常量：1-是；2-否

### IfCompound (是否复利)

是否复利(IfCompound)，该字段固定以下常量：1-是；2-否

### ExchangeRateInnerCode (汇率内部编码)

汇率内部编码(ExchangeRateInnerCode)：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得汇率的交易代码、简称等。

### IfExecuted (是否执行)

是否执行(IfExecuted)，该字段固定以下常量：1-是；2-否

## SQL示例

```sql
-- 查询 公募基金基准配置 数据
SELECT *
FROM mf_benchmarkallocation
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
