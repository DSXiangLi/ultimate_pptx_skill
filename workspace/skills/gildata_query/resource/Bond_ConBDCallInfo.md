# Bond_ConBDCallInfo

**中文名**: 可转债券赎回信息

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDCallInfo` |
| MySQL表名 | `bond_conbdcallinfo` |
| 中文名 | 可转债券赎回信息 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 25 |
| 版本 | 1.05 |

## 表描述

1.收录可转债赎回信息，包括：赎回价，及触发条件等。
2.数据范围：1992-11-19 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(19) | ✗ | 100.0% |  |
| 3 | `BondCode` | 可转债券代码 | varchar2(50) | ✗ | 100.0% |  |
| 4 | `BondAbbr` | 可转债券简称 | varchar2(50) | ✗ | 100.0% |  |
| 5 | `StartDate` | 发行日期 | date | ✓ | 99.65% |  |
| 6 | `PaymentYearSequence` | 计息年度序列 | number(3) | ✓ | 100.0% | 计息年度序列（PaymentYearSequence）具体指某一个计息年度 |
| 7 | `PaymentYearStartDate` | 计息年度起始日 | date | ✓ | 99.53% |  |
| 8 | `PaymentYearEndDate` | 计息年度截止日 | date | ✓ | 99.53% |  |
| 9 | `CallPriceType` | 赎回价格是否唯一 | number(3) | ✓ | 100.0% | 赎回价格是否唯一(CallPriceType)与(CT_SystemConst)表中的DM字段关联，令LB = 999 ... |
| 10 | `CallPriceTypeName` | 赎回价格是否唯一名称 | varchar2(50) | ✓ | 100.0% |  |
| 11 | `CallPrice` | 年度赎回价 | number(19,4) | ✓ | 99.64% |  |
| 12 | `CallType` | 是否随时赎回 | number(3) | ✓ | 100.0% | 是否随时赎回(CallType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到是否随时... |
| 13 | `CallTypeName` | 是否随时赎回名称 | varchar2(50) | ✓ | 100.0% |  |
| 14 | `CallStartDate` | 赎回开始日期 | date | ✓ | 99.92% |  |
| 15 | `CallEndDate` | 赎回结束日期 | date | ✓ | 99.92% |  |
| 16 | `CallLevel` | 赎回触发票面比例 | number(19,8) | ✓ | 98.7% |  |
| 17 | `CallConditionDay` | 赎回条件天数 | number(10) | ✓ | 98.7% |  |
| 18 | `CallReachDay` | 赎回条件满足天数 | number(10) | ✓ | 98.7% |  |
| 19 | `CallUnconvertAmount` | 触发赎回未转股余额(万元) | number(18,4) | ✓ | 94.81% |  |
| 20 | `CallPriceInf` | 是否包含应记利息 | number(3) | ✓ | 100.0% | 是否包含应记利息(CallPriceInf)与(CT_SystemConst)表中的DM字段关联，令LB = 999 A... |
| 21 | `CallPriceInfName` | 是否包含应记利息名称 | varchar2(50) | ✓ | 100.0% |  |
| 22 | `MultiLevel` | 多个触发比例筛选 | number(10) | ✓ | 100.0% | 多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到... |
| 23 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 24 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 25 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PaymentYearSequence (计息年度序列)

计息年度序列（PaymentYearSequence）具体指某一个计息年度

### CallPriceType (赎回价格是否唯一)

赎回价格是否唯一(CallPriceType)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到赎回价格是否唯一的具体描述：1-是，2-否。

### CallType (是否随时赎回)

是否随时赎回(CallType)与(CT_SystemConst)表中的DM字段关联，令LB = 1481，得到是否随时赎回的具体描述：1-随时，2-每计息年度1次，3-12月内不超过1次。

### CallPriceInf (是否包含应记利息)

是否包含应记利息(CallPriceInf)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否包含应记利息的具体描述：1-是，2-否。

### MultiLevel (多个触发比例筛选)

多个触发比例筛选(MultiLevel)与(CT_SystemConst)表中的DM字段关联，令LB = 2392，得到多个触发比例筛选的具体描述：1-不存在多个，2-触发比例从大到小排序-1，3-触发比例从大到小排序-2。

## SQL示例

```sql
-- 查询 可转债券赎回信息 数据
SELECT *
FROM bond_conbdcallinfo
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
