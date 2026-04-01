# MF_IncomePayment

**中文名**: 公募基金收益支付

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_IncomePayment` |
| MySQL表名 | `mf_incomepayment` |
| 中文名 | 公募基金收益支付 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金收益分配 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1.01 |

## 表描述

1.本表记录基金收益支付信息，包括收益支付的结转日、份额到账日，本次收益支付的区间起始日、区间截止日等信息。
2.历史数据：2004年2月起-至今。
3.信息来源：基金公司官网披露的相关临时公告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 最新信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `IncomePaymentDate` | 收益支付份额结转日 | date | ✓ | 100.0% |  |
| 7 | `BeginDateOfIncome` | 收益区间起始 | date | ✓ | 100.0% |  |
| 8 | `EndDateOfIncome` | 收益区间截止 | date | ✓ | 100.0% |  |
| 9 | `ShareToAccountDate` | 份额到帐日 | date | ✓ | 94.7% |  |
| 10 | `BeginDateOfRedemption` | 可赎回起始日 | date | ✓ | 94.83% |  |
| 11 | `PaymentObject` | 收益支付对象 | varchar2(200) | ✓ | 99.42% |  |
| 12 | `PaymentMethod` | 收益支付办法 | varchar2(200) | ✓ | 99.27% |  |
| 13 | `Remarks` | 备注 | varchar2(200) | ✓ | 0.02% |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `XGRQ` | 更新时间 | date | ✓ |  |  |
| 16 | `JSID` | JSID | number(19) | ✓ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

## SQL示例

```sql
-- 查询 公募基金收益支付 数据
SELECT *
FROM mf_incomepayment
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
