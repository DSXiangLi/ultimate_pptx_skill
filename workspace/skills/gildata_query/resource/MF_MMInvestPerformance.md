# MF_MMInvestPerformance

**中文名**: 公募基金货币型基金定投收益表现

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MMInvestPerformance` |
| MySQL表名 | `mf_mminvestperformance` |
| 中文名 | 公募基金货币型基金定投收益表现 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益表现 |
| 更新频率 | 日更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.本表记录货币基金的定投收益表现，包括一年、二年、三年、五年、十年以来的定投收益表现。
2.历史数据：2014年1月起-至今。
3.信息来源：根据基金公司披露的万份收益、7日年化收益率数据计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 4 | `IRInSingleYear` | 一年定投收益率(%) | number(18,10) | ✓ | 99.12% |  |
| 5 | `IRInTwoYear` | 二年定投收益率(%) | number(18,10) | ✓ | 99.12% |  |
| 6 | `IRInThreeYear` | 三年定投收益率(%) | number(18,10) | ✓ | 99.12% |  |
| 7 | `IRInFiveYear` | 五年定投收益率(%) | number(18,10) | ✓ | 99.12% |  |
| 8 | `IRInTenYear` | 十年定投收益率(%) | number(18,10) | ✓ | 99.12% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部编码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金货币型基金定投收益表现 数据
SELECT *
FROM mf_mminvestperformance
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
