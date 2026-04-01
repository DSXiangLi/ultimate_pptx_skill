# Bond_InstalRedempPrin

**中文名**: 分期兑付本金表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_InstalRedempPrin` |
| MySQL表名 | `bond_instalredempprin` |
| 中文名 | 分期兑付本金表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券付息兑付 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.内容说明：记录债券提前分期还本的类型及债券还本比例值，其中ABS因为不确定未来还本计划，所以生成比例和会存在不等于100的情况。
2.数据范围：2006-01-23 至今
3.信息来源：中债登、货币网、上清所、上交所、深交所等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InfoPublDate` | 公告日期 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 债券内部编码 | number(10) | ✗ | 100.0% | 针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。同一只债券在不... |
| 4 | `InstalmentRepayType` | 分期偿还类型 | number(10) | ✗ | 100.0% | 分期偿还类型(InstalmentRepayType)与(CT_SystemConst)表中的DM字段关联，令LB = ... |
| 5 | `EarlyRepayDate` | 提前偿还日 | date | ✗ | 100.0% | 提前偿还日（EarlyRepayDate）：为推算的还本日期，即如遇假日，不跳过假日，方便客户最新面值、托管量的计算。 |
| 6 | `EarlyRepayRatio` | 提前偿还比例 | number(19,8) | ✓ | 100.0% |  |
| 7 | `InfoSource` | 信息来源 | varchar2(500) | ✓ | 0.62% |  |
| 8 | `Remark` | 备注 | varchar2(1000) | ✓ | 0.62% |  |
| 9 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (债券内部编码)

针对同一债券在不同市场的交易代码不统一的问题，设置了Main Code字段和InnerCode字段来区分。同一只债券在不同的交易市场将产生多个InnerCode，对于同一只债券，一个市场对应一个InnerCode。

### InstalmentRepayType (分期偿还类型)

分期偿还类型(InstalmentRepayType)与(CT_SystemConst)表中的DM字段关联，令LB = 1829，得到分期偿还类型的具体描述：1-减少面值，2-减少持仓。

### EarlyRepayDate (提前偿还日)

提前偿还日（EarlyRepayDate）：为推算的还本日期，即如遇假日，不跳过假日，方便客户最新面值、托管量的计算。

## SQL示例

```sql
-- 查询 分期兑付本金表 数据
SELECT *
FROM bond_instalredempprin
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
