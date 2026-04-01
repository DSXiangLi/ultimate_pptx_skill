# HK_FundAdjustingFactor

**中文名**: 香港基金复权因子

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundAdjustingFactor` |
| MySQL表名 | `hk_fundadjustingfactor` |
| 中文名 | 香港基金复权因子 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 不定时更新 |
| 字段数量 | 7 |
| 版本 | 1 |

## 表描述

1.本表记录香港互认基金和香港ETF，由分红数据计算而来的复权因子数据。
2.历史数据：2015起-至今。
3.数据来源：聚源计算而得。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `ExDiviDate` | 除权除息日 | date | ✗ | 100.0% |  |
| 4 | `RatioAdjustingFactor` | 复权因子 | number(19,17) | ✗ | 100.0% |  |
| 5 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 6 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 7 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、交易简称等。

## SQL示例

```sql
-- 查询 香港基金复权因子 数据
SELECT *
FROM hk_fundadjustingfactor
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
