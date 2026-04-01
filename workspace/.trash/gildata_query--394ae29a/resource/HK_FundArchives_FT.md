# HK_FundArchives_FT

**中文名**: 香港基金概况_繁体

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FundArchives_FT` |
| MySQL表名 | `hk_fundarchives_ft` |
| 中文名 | 香港基金概况_繁体 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 香港基金 |
| 更新频率 | 日更新 |
| 字段数量 | 12 |
| 版本 | 1 |

## 表描述

1.本表收录港交所ETF、杠杆及反向产品的基础信息，包含参与主体，相关日期，基金类别、投资策略、投资目标等信息。
2.历史数据：1999年11月起--至今。
3.数据来源：基金公司官网。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `RID` | RID | number(19) | ✗ | 100.0% |  |
| 3 | `FundName` | 基金 | varchar2(200) | ✓ | 100.0% |  |
| 4 | `FundNameAbbr` | 基金名称简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `FeeDescription` | 费用描述 | clob | ✓ | 98.13% |  |
| 6 | `TargetIndexChiName` | 标的指数中文名称 | varchar2(200) | ✓ | 86.88% |  |
| 7 | `DividendPolicy` | 派息政策 | clob | ✓ | 99.69% |  |
| 8 | `InvestStrategy` | 投资策略 | clob | ✓ | 99.53% |  |
| 9 | `Statement` | 解释说明 | varchar2(1000) | ✓ | 4.69% |  |
| 10 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 11 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 12 | `JSID` | JSID | number(19) | ✗ |  |  |

## SQL示例

```sql
-- 查询 香港基金概况_繁体 数据
SELECT *
FROM hk_fundarchives_ft
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
