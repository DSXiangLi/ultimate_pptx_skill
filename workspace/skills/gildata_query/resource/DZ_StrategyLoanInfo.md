# DZ_StrategyLoanInfo

**中文名**: 战略配售可出借信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `DZ_StrategyLoanInfo` |
| MySQL表名 | `dz_strategyloaninfo` |
| 中文名 | 战略配售可出借信息 |
| 路径 | 聚源新版数据库 > 国内上市公司定制库 > 上市公司股东股本 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1、内容说明：记录A股战略配售股份可参与融券上市流通的信息，包含创业板和科创板股票
2、数据范围：创业板注册制实施日起，科创板上市之日起
3、信息来源：深交所，上交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `TotalAFloats` | 流通A股合计 | number(16,0) | ✓ | 100.0% | 流通A股合计=限售股份(股)+无限售股份(股) |
| 5 | `LimitedShares` | 限售股份(股/份) | number(16,0) | ✓ | 100.0% |  |
| 6 | `UnLimitedShares` | 无限售股份(股/份) | number(16,0) | ✓ | 100.0% |  |
| 7 | `ALoanSharesSum` | 可出借总股数(股/份) | number(10) | ✓ | 99.99% |  可出借总股数(股)=剩余可出借股数(股)+已出借股数(股) |
| 8 | `ALoanShares` | 剩余可出借股数(股/份) | number(10) | ✓ | 99.99% |  |
| 9 | `LentShares` | 已出借股数(股/份) | number(10) | ✓ | 100.0% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### TotalAFloats (流通A股合计)

流通A股合计=限售股份(股)+无限售股份(股)

### ALoanSharesSum (可出借总股数(股/份))


可出借总股数(股)=剩余可出借股数(股)+已出借股数(股)

## SQL示例

```sql
-- 查询 战略配售可出借信息 数据
SELECT *
FROM dz_strategyloaninfo
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
