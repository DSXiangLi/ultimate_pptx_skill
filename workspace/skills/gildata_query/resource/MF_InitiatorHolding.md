# MF_InitiatorHolding

**中文名**: 公募基金发起人持股

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_InitiatorHolding` |
| MySQL表名 | `mf_initiatorholding` |
| 中文名 | 公募基金发起人持股 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金发行与上市 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.本表记录基金发起人持有基金份额情况，包括发起人的名称、发起人持有的份额、持有的比例等信息。
2.历史数据：2001年6月起-至今。
3.信息来源：基金公司官网披露的相关临时公告。
4.数据未更新原因：表内相关基金业务已终止。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 37.86% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.57% |  |
| 5 | `FundTotalVolume` | 基金总份额(份) | number(10,0) | ✓ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 7 | `SerialNumber` | 序号 | number(10) | ✓ | 100.0% |  |
| 8 | `InitiatorName` | 发起人名称 | varchar2(100) | ✗ | 100.0% |  |
| 9 | `InitiatorCode` | 发起人编码 | varchar2(20) | ✓ | 99.79% |  |
| 10 | `HoldingShares` | 持有份额(份) | number(18,0) | ✓ | 100.0% |  |
| 11 | `HoldingRatio` | 持有比例 | number(18,6) | ✓ | 100.0% |  |
| 12 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金发起人持股 数据
SELECT *
FROM mf_initiatorholding
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
