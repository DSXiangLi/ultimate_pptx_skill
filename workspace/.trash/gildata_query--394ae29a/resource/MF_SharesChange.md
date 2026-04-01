# MF_SharesChange

**中文名**: 公募基金份额变动

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_SharesChange` |
| MySQL表名 | `mf_shareschange` |
| 中文名 | 公募基金份额变动 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金持有人及份额变动 |
| 更新频率 | 交易所上市基金（如ETF、LOF）日更新，其他基金季更新 |
| 字段数量 | 23 |
| 版本 | 1.04 |

## 表描述

1.本表记录基金份额变动情况，包括期初份额，本期申购或赎回，期末份额等数据，份额变化的绝对值、变化率等数据。
2.历史数据：1998年3月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoSource` | 信息来源 | varchar2(100) | ✓ | 99.7% |  |
| 5 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 6 | `StatPeriod` | 统计区间 | varchar2(20) | ✓ | 100.0% | 统计区间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1087 AND DM... |
| 7 | `StartDate` | 起始日期 | date | ✓ | 17.73% |  |
| 8 | `EndDate` | 截止日期 | date | ✓ | 100.0% |  |
| 9 | `StartShares` | 期初份额(份) | number(18,4) | ✓ | 17.67% |  |
| 10 | `ApplyingShares` | 加:本期申购(份) | number(18,4) | ✓ | 15.99% |  |
| 11 | `RedeemShares` | 减:本期赎回(份) | number(18,4) | ✓ | 15.8% |  |
| 12 | `SplitShares` | 拆分折算份额变动 | number(18,4) | ✓ | 0.56% |  |
| 13 | `EndShares` | 期末份额(份) | number(18,4) | ✓ | 70.05% |  |
| 14 | `SharesChange` | 基金份额变化(申购赎回净额)(份) | number(18,4) | ✓ | 17.67% | 基金份额变化（SharesChange）：即申购赎回净额，由“期末份额-期初份额”计算得到。 |
| 15 | `RateOfSharesChange` | 基金份额变化率(%) | number(18,6) | ✓ | 17.33% | 基金份额变化率（RateOfSharesChange）=（期末份额-期初份额）/期初份额*100% |
| 16 | `FloatShares` | 流通份额(份) | number(18,4) | ✓ | 69.74% | 流通份额（FloatShares）：当“统计区间（StatPeriod）”等于996-日，为交易所公布每日场内份额数据。... |
| 17 | `DividendReinvestment` | 红利再投资(份) | number(18,4) | ✓ | 0.0% |  |
| 18 | `ShgiftIn` | 同系基金转入(份) | number(18,4) | ✓ | 0.0% |  |
| 19 | `ShiftOut` | 同系基金转出(份) | number(18,4) | ✓ | 0.0% |  |
| 20 | `IfCombine` | 是否合并披露 | number(10) | ✓ | 100.0% | 是否合并披露（IfCombine），该字段固定以下常量：1-是； 0-否 |
| 21 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 22 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 23 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。

### StatPeriod (统计区间)

统计区间(StatPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 1087 AND DM IN (3,6,12,993,995,996)，得到统计区间的具体描述：3-季度，6-半年，12-年度，993-截止时点，995-周，996-日。

### SharesChange (基金份额变化(申购赎回净额)(份))

基金份额变化（SharesChange）：即申购赎回净额，由“期末份额-期初份额”计算得到。

### RateOfSharesChange (基金份额变化率(%))

基金份额变化率（RateOfSharesChange）=（期末份额-期初份额）/期初份额*100%

### FloatShares (流通份额(份))

流通份额（FloatShares）：当“统计区间（StatPeriod）”等于996-日，为交易所公布每日场内份额数据。其中深交所上市基金上市之后的每日份额为交易所披露的盘前份额

### IfCombine (是否合并披露)

是否合并披露（IfCombine），该字段固定以下常量：1-是； 0-否

## SQL示例

```sql
-- 查询 公募基金份额变动 数据
SELECT *
FROM mf_shareschange
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
