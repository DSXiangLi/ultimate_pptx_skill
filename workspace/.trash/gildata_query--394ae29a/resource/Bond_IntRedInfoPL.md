# Bond_IntRedInfoPL

**中文名**: 债券付息兑付(理论)

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_IntRedInfoPL` |
| MySQL表名 | `bond_intredinfopl` |
| 中文名 | 债券付息兑付(理论) |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 不定时更新 |
| 字段数量 | 31 |
| 版本 | 1.02 |

## 表描述

1.内容说明：目前仅包含债券初始发行文件公布的未来付息和兑付情况（ABS和ABN除外）
2.数据范围：1987-07-01至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InforSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 4 | `IssuanceOrg` | 公告披露机构 | number(10) | ✓ | 100.0% | 公告披露机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1525，得到公... |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `PaymentDate` | 计息周期起始日 | date | ✓ | 100.0% |  |
| 7 | `EndPaymentDay` | 计息周期截止日 | date | ✓ | 100.0% |  |
| 8 | `OriCouponRate` | 原始票面利率 | number(10,6) | ✓ | 88.93% |  |
| 9 | `EndDate` | 理论付息(兑付)日 | date | ✓ | 100.0% |  |
| 10 | `PayingRatio` | 每张兑付本金额 | number(19,5) | ✓ | 100.0% |  |
| 11 | `PayingValue` | 每张兑付本息额 | number(19,8) | ✓ | 100.0% |  |
| 12 | `IntPaymentMethod` | 付息方式 | number(10) | ✓ | 88.64% | 付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，... |
| 13 | `BondVolBFPayInt` | 付息规模基数(百万) | number(19,8) | ✓ | 99.99% |  |
| 14 | `EventType` | 事项类型 | number(10) | ✓ | 100.0% | 事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到事项类型的... |
| 15 | `PaymentYear` | 付息年次 | number(10) | ✓ | 88.64% |  |
| 16 | `AccumulatePaymentNum` | 累计付息次数(含本次) | number(10) | ✓ | 100.0% |  |
| 17 | `Interest` | 百元面值利息(含税) | number(19,8) | ✓ | 100.0% |  |
| 18 | `InterestTaxed` | 百元面值利息(扣税) | number(19,8) | ✓ | 100.0% |  |
| 19 | `InterestTaxRate` | 利息所得税率(%) | number(19,8) | ✓ | 100.0% |  |
| 20 | `IntRegDate` | 债权登记日 | date | ✓ | 100.0% |  |
| 21 | `RedRegDate` | 兑付登记日 | date | ✓ | 24.0% |  |
| 22 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |
| 24 | `InterestThisYear` | 债券年利率(%) | number(19,8) | ✓ | 0.38% |  |
| 25 | `IfEffected` | 是否有效 | number(10) | ✗ | 100.0% |  |
| 26 | `IntPaymentCode` | 付息代码 | varchar2(50) | ✓ | 0.0% |  |
| 27 | `ExDividenDate` | 除息基准日 | date | ✓ | 0.0% |  |
| 28 | `LastTradeDay` | 最后交易日 | date | ✓ | 0.0% |  |
| 29 | `DelistDate` | 停止交易日 | date | ✓ | 0.0% |  |
| 30 | `TradeEndDate` | 债券摘牌日 | date | ✓ | 0.0% |  |
| 31 | `StartDate` | 兑付起始日 | date | ✓ | 0.0% |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### IssuanceOrg (公告披露机构)

公告披露机构(IssuanceOrg)与(CT_SystemConst)表中的DM字段关联，令LB = 1525，得到公告披露机构的具体描述：1-深圳交易所，2-上海交易所，3-深圳登记结算公司，4-上海登记结算公司，5-发行人，6-承销机构，8-规则生成，9-未公告。

### IntPaymentMethod (付息方式)

付息方式(IntPaymentMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 1168，得到付息方式的具体描述：1-每年付息，2-半年付息，3-到期一次还本付息，4-按季付息，5-按月付息。

### EventType (事项类型)

事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 2034，得到事项类型的具体描述：1-付息，2-中途分期还本(减少面值)，3-中途分期还本(减少持仓)，4-到期分期还本(减少面值)，5-到期分期还本(减少持仓)，6-兑付。

## SQL示例

```sql
-- 查询 债券付息兑付(理论) 数据
SELECT *
FROM bond_intredinfopl
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
