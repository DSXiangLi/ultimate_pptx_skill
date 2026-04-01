# HK_FreeFloat

**中文名**: 港股自由流通股本

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `HK_FreeFloat` |
| MySQL表名 | `hk_freefloat` |
| 中文名 | 港股自由流通股本 |
| 路径 | 聚源新版数据库 > 港股数据库 > 港股股东权益与股本 |
| 更新频率 | 不定期更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

内容说明：本表记录港股每只股票对应某一股本变动日期实际可在二级市场上交易的流通股数量。
数据范围：2021-12-31至今
信息来源：聚源计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关... |
| 3 | `CompanyCode` | 公司代码 | number(10) | ✗ | 100.0% | 公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `ChangeDate` | 股本变动日期 | date | ✗ | 100.0% |  |
| 6 | `HKStkShares` | 港股股数(股) | number(19) | ✓ | 100.0% |  |
| 7 | `HKFloatShare` | 港股流通股股数(股) | number(19) | ✓ | 100.0% |  |
| 8 | `InactiveFloats` | 非自由流通股本(股) | number(19) | ✓ | 93.67% |  |
| 9 | `FreeFloats` | 自由流通股本(股) | number(19) | ✓ | 100.0% |  |
| 10 | `ChangeReason` | 股本变动原因 | varchar2(500) | ✓ | 90.18% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“港股证券主表（HK_SecuMain）”中的“证券内部编码（InnerCode）”关联，得到港股的交易代码、简称等。

### CompanyCode (公司代码)

公司代码（CompanyCode）：与“港股证券主表（HK_SecuMain）”中的“公司代码（CompanyCode）”关联，得到港股的交易代码、简称等。

## SQL示例

```sql
-- 查询 港股自由流通股本 数据
SELECT *
FROM hk_freefloat
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
