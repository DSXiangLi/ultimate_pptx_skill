# FP_IFUnitPrice

**中文名**: 保险理财产品账户价格

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `FP_IFUnitPrice` |
| MySQL表名 | `fp_ifunitprice` |
| 中文名 | 保险理财产品账户价格 |
| 路径 | 聚源新版数据库 > 金融产品 > 保险理财 |
| 更新频率 | 日更新 |
| 字段数量 | 9 |
| 版本 | 1 |

## 表描述

收录保险产品投资账户的买入价和卖出价。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 3 | `FinProCode` | 账户编码 | varchar2(12) | ✗ | 100.0% | 账户编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）... |
| 4 | `EndDate` | 评估日期 | date | ✗ | 100.0% |  |
| 5 | `BidPrice` | 买入价(元) | number(19,8) | ✓ | 94.05% |  |
| 6 | `AskPrice` | 卖出价(元) | number(19,8) | ✓ | 100.0% |  |
| 7 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 8 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 9 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### FinProCode (账户编码)

账户编码（FinProCode）：与“金融产品主表（FP_SecuMain）”中的“金融产品编码（FinProCode）”关联，得到账户的名称等信息。

## SQL示例

```sql
-- 查询 保险理财产品账户价格 数据
SELECT *
FROM fp_ifunitprice
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
