# MF_AdvisorSharesChange

**中文名**: 公募基金管理人持有份额变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_AdvisorSharesChange` |
| MySQL表名 | `mf_advisorshareschange` |
| 中文名 | 公募基金管理人持有份额变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 季度更新 |
| 字段数量 | 14 |
| 版本 | 1 |

## 表描述

1.本表用于记录基金定期报告中披露的基金管理人持有基金份额变动情况。
2.数据范围：2013年3月31日-至今。
3.信息来源：依据基金定报中披露的持有人结构等信息，进行衍生计算获得市场范围内统计结果。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。 |
| 3 | `ReportType` | 报告类型 | number(10) | ✗ | 100.0% | 报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB=1032 AND DM I... |
| 4 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `StartShares` | 期初份额(份) | number(18,4) | ✓ | 99.95% |  |
| 7 | `ApplyingShares` | 本期申购/买入(份) | number(18,4) | ✓ | 22.82% |  |
| 8 | `SplitShares` | 拆分折算份额变动 | number(18,4) | ✓ | 0.78% |  |
| 9 | `RedeemShares` | 减:本期赎回(份) | number(18,4) | ✓ | 21.44% |  |
| 10 | `EndShares` | 期末份额(份) | number(18,4) | ✓ | 100.0% |  |
| 11 | `HoldRatio` | 持有比例(%) | number(18,6) | ✓ | 100.0% |  |
| 12 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 13 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 14 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### ReportType (报告类型)

报告类型(ReportType)与(CT_SystemConst)表中的DM字段关联，令LB=1032 AND DM IN (5,6,17,23,61,63)，得到报告类型的具体描述：5-年度报告，6-中期报告，17-第一季度报告，23-第三季度报告，61-第二季度报告，63-第四季度报告。

## SQL示例

```sql
-- 查询 公募基金管理人持有份额变动 数据
SELECT *
FROM mf_advisorshareschange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
