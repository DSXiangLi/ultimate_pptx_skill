# Bond_ConBDIssueTerm

**中文名**: 可转债发行条款

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ConBDIssueTerm` |
| MySQL表名 | `bond_conbdissueterm` |
| 中文名 | 可转债发行条款 |
| 路径 | 聚源新版数据库 > 债券数据库 > 可转债信息 |
| 更新频率 | 不定时更新 |
| 字段数量 | 20 |
| 版本 | 1.02 |

## 表描述

1.包含可转换债券在招募说明书中列示的各类发行条款。
2.数据范围：1992-11-01 至今
3.信息来源：上交所、深交所、巨潮资讯网等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部代码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 5 | `CouponRateTerm` | 利率及付息条款 | clob | ✓ | 11.0% |  |
| 6 | `CoupRateCompTerm` | 利息补偿条款 | clob | ✓ | 3.22% |  |
| 7 | `PrefPlaScheduleTerm` | 向原股东配售安排条款 | clob | ✓ | 66.18% |  |
| 8 | `ConversionPeriodTerm` | 转换期条款 | clob | ✓ | 98.42% |  |
| 9 | `InitialCPConfirmTerm` | 初始转股价确定条款 | clob | ✓ | 10.81% |  |
| 10 | `CPAdjustmentTerm` | 转股价格调整条款 | clob | ✓ | 38.24% |  |
| 11 | `CPRevisionTerm` | 转股价格修正条款 | clob | ✓ | 26.61% |  |
| 12 | `RedeemTerm` | 赎回条款 | clob | ✓ | 38.5% |  |
| 13 | `ConBRedeemTerm` | 可转债到期赎回条款 | clob | ✓ | 19.6% |  |
| 14 | `SellBackTerm` | 回售条款 | clob | ✓ | 22.5% |  |
| 15 | `FroceConvertTerm` | 强制性转股条款 | clob | ✓ | 1.45% |  |
| 16 | `DealingRemainCBTerm` | 转换余股处理条款 | clob | ✓ | 28.89% |  |
| 17 | `CYDiviAttrTerm` | 转换年度股利归属条款 | clob | ✓ | 40.96% |  |
| 18 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 19 | `JSID` | JSID | number(19) | ✗ |  |  |
| 20 | `InsertTime` | 发布时间 | date | ✓ |  |  |

## 字段说明

### InnerCode (内部代码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到可转换债券的交易代码、债券简称等。

## SQL示例

```sql
-- 查询 可转债发行条款 数据
SELECT *
FROM bond_conbdissueterm
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
