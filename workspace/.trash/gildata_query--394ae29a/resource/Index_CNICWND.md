# Index_CNICWND

**中文名**: 国证指数次日权重

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Index_CNICWND` |
| MySQL表名 | `index_cnicwnd` |
| 中文名 | 国证指数次日权重 |
| 路径 | 聚源新版数据库 > 产品代理 > 国证代理数据库 |
| 更新频率 | 日更新 |
| 字段数量 | 17 |
| 版本 | 1 |

## 表描述

内容说明：收录国证股票类指数，次日权重及次日开盘参考信息等数据。
数据范围：2020年至今
信息来源：深圳证券信息有限公司

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `IndexCode` | 指数内部编码 | number(10) | ✗ | 100.0% | 指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码(InnerCode)：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得... |
| 4 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 5 | `EffectiveDate` | 生效日期 | date | ✗ | 100.0% |  |
| 6 | `WeightedRatio` | 权重(%) | number(19,6) | ✓ | 100.0% |  |
| 7 | `ReferPrice` | 调整后开盘参考价(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `ClosePrice` | 收盘价(元) | number(19,4) | ✓ | 14.54% |  |
| 9 | `TotalShares` | 总股本(股) | number(19,2) | ✓ | 14.54% |  |
| 10 | `AdjustedShares` | 计算用股本(股) | number(19,2) | ✓ | 100.0% |  |
| 11 | `MarketValue` | 总市值(元) | number(19,4) | ✓ | 14.54% |  |
| 12 | `AdjustedMV` | 计算用市值(元) | number(19,4) | ✓ | 14.54% |  |
| 13 | `Currency` | 交易货币 | number(10) | ✓ | 100.0% |  |
| 14 | `ExchangeRate` | 汇率 | number(19,8) | ✓ | 74.3% |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 17 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### IndexCode (指数内部编码)

指数内部编码（IndexCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### InnerCode (证券内部编码)

证券内部编码(InnerCode)：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到样本券的代码、简称等。

## SQL示例

```sql
-- 查询 国证指数次日权重 数据
SELECT *
FROM index_cnicwnd
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
