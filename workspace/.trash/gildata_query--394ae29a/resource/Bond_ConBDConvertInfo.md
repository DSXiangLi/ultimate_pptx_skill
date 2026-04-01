# Bond_ConBDConvertInfo

**中文名**: 可转债转股及规模变动情况

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDConvertInfo` |
| MySQL表名 | `bond_conbdconvertinfo` |
| 中文名 | 可转债转股及规模变动情况 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 27 |
| 版本 | 1.01 |

## 表描述

1.记录可转换债券每次转股时的转股金额、转股数量、对应转股价、累计转股金额、剩余债券金额等信息，并展示因赎回、回售、兑付等引起的转债规模变动情况。
2.数据范围：2000-06-30 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 6 | `EventType` | 涉及事项 | number(10) | ✓ | 100.0% | 涉及事项(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1105 AND DM ... |
| 7 | `ConvertPrice` | 本次转股价(元/股) | number(19,4) | ✓ | 99.96% | 本次转股价格：本次转股金额/本次转股数量 |
| 8 | `AmountThisPeriod` | 本次转股金额(元) | number(19,4) | ✓ | 98.86% |  |
| 9 | `VolThisPeriod` | 本次转股数量(股) | number(18,2) | ✓ | 98.86% |  |
| 10 | `TotalAmountConverted` | 累计转股金额(元) | number(19,4) | ✓ | 98.87% |  |
| 11 | `TotalCBAmountConverted` | 累计转股张数(张) | number(10) | ✓ | 98.87% |  |
| 12 | `TotalVolConverted` | 累计转股数量(股) | number(18,2) | ✓ | 98.87% |  |
| 13 | `AccuRealCP` | 累计实际转股价(元/股) | number(19,4) | ✓ | 99.97% | 累计转股价：累计转股金额/累计转股数量 |
| 14 | `InitialConvetPrice` | 初始转股价(元/股) | number(19,4) | ✓ | 99.96% |  |
| 15 | `CPRSum` | 本次赎回/兑付/回售金额(元) | number(19,4) | ✓ | 1.13% |  |
| 16 | `TotalCPRSum` | 累计赎回/兑付/回售金额(元) | number(19,4) | ✓ | 1.13% |  |
| 17 | `IssueAmount` | 可转债总额(元) | number(19,4) | ✓ | 100.0% |  |
| 18 | `CurrentSizeChange` | 本次规模增减(元) | number(19,4) | ✓ | 100.0% |  |
| 19 | `RemainingAmount` | 可转债剩余金额(元) | number(19,4) | ✓ | 100.0% |  |
| 20 | `CurrentTotalShares` | 转股后总股本(股) | number(18,2) | ✓ | 95.44% |  |
| 21 | `TotalAmountConvertedR` | 累计转股比例(%) | number(19,12) | ✓ | 98.87% |  |
| 22 | `TotalAmountCallR` | 累计赎回比例(%) | number(19,12) | ✓ | 0.7% |  |
| 23 | `TotalAmountPutR` | 累计回售比例(%) | number(19,12) | ✓ | 0.32% |  |
| 24 | `TotalAmountPR` | 累计到期比例(%) | number(19,12) | ✓ | 100.0% |  |
| 25 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 26 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 27 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

### EventType (涉及事项)

涉及事项(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1105 AND DM NOT IN (2,3)，得到涉及事项的具体描述：1-转股，4-转债赎回，5-转债兑付，6-转债回售。

### ConvertPrice (本次转股价(元/股))

本次转股价格：本次转股金额/本次转股数量

### AccuRealCP (累计实际转股价(元/股))

累计转股价：累计转股金额/累计转股数量

## SQL示例

```sql
-- 查询 可转债转股及规模变动情况 数据
SELECT *
FROM bond_conbdconvertinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
