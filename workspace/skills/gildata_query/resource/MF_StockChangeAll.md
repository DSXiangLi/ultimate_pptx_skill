# MF_StockChangeAll

**中文名**: 公募基金股票投资组合变动总表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_StockChangeAll` |
| MySQL表名 | `mf_stockchangeall` |
| 中文名 | 公募基金股票投资组合变动总表 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 日更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：公募基金股票投资组合变动总表,包含一般基金和QDII基金
2.信息来源：基金公司披露的定期报告
3.数据范围：至今

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% | 基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。 |
| 3 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.86% |  |
| 5 | `ReportType` | 报告类型 | number(10) | ✗ | 100.0% | 报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM... |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `ChangeType` | 变动类型 | number(10) | ✗ | 100.0% | 变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型... |
| 8 | `SerialNumber` | 序号 | number(10) | ✗ | 100.0% |  |
| 9 | `StockInnerCode` | 股票内部编码 | number(10) | ✓ | 99.28% |  |
| 10 | `SecuCode` | 证券代码 | varchar2(50) | ✓ | 99.4% |  |
| 11 | `SecuName` | 证券名称 | varchar2(200) | ✓ | 99.39% |  |
| 12 | `EngName` | 证券名称(英文) | varchar2(200) | ✓ | 2.31% |  |
| 13 | `TradeSum` | 买卖金额(元) | number(19,4) | ✓ | 100.0% |  |
| 14 | `RatioInNVAtBegin` | 占期初净值比例 | number(18,6) | ✓ | 91.07% |  |
| 15 | `RatioInNVAtEnd` | 占期末净值比例 | number(18,6) | ✓ | 8.93% |  |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### TransCode (基金转型统一编码)

基金转型统一编码(TransCode)是转型后的基金内码(InnerCode)，若发生多次转型，则为最新的基金内码。

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportType (报告类型)

报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB = 1032 AND DM IN(5,6)，得到报告类型的具体描述：5-年度报告，6-中期报告。

### ChangeType (变动类型)

变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1095，得到变动类型的具体描述：1-买入，2-卖出。

## SQL示例

```sql
-- 查询 公募基金股票投资组合变动总表 数据
SELECT *
FROM mf_stockchangeall
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
