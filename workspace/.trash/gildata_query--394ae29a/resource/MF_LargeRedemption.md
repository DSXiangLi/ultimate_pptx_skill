# MF_LargeRedemption

**中文名**: 基金巨额赎回

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_LargeRedemption` |
| MySQL表名 | `mf_largeredemption` |
| 中文名 | 基金巨额赎回 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 15 |
| 版本 | 1.02 |

## 表描述

1.本表记录基金发生巨额赎回的日期。
2.历史数据：1998年3月起-至今。
3.信息来源：基金公司官网披露的相关公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `LargeRedemptionDate` | 巨额赎回日期 | date | ✗ | 100.0% |  |
| 7 | `LargeRedemptionValue` | 巨额赎回金额 | number(19,4) | ✓ | 0.0% |  |
| 8 | `LargeRedemptionShare` | 巨额赎回份额 | number(19,4) | ✓ | 0.05% |  |
| 9 | `Remark` | 备注 | varchar2(500) | ✓ | 2.4% |  |
| 10 | `InsertTime` | 插入时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |
| 13 | `NetValueExRightStartDate` | 净值除权起始日 | date | ✓ | 19.87% |  |
| 14 | `NetValueExRightEndDate` | 净值除权截止日 | date | ✓ | 19.87% |  |
| 15 | `IfExRightDate` | 是否极值除权 | number(10) | ✓ | 100.0% |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

## SQL示例

```sql
-- 查询 基金巨额赎回 数据
SELECT *
FROM mf_largeredemption
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
