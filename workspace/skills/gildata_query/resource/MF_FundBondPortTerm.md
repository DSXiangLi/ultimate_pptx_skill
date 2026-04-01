# MF_FundBondPortTerm

**中文名**: 公募基金投资剩余期限分布

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_FundBondPortTerm` |
| MySQL表名 | `mf_fundbondportterm` |
| 中文名 | 公募基金投资剩余期限分布 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 38 |
| 版本 | 1.01 |

## 表描述

1.本表记录定期报告披露基金投资组合的剩余期限分布。如各类期限的资产占总资产的比例、各类期限的负债占总资产的比例。
2.历史数据：2004年6月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 99.96% |  |
| 5 | `ReportDate` | 报告期 | date | ✗ | 100.0% |  |
| 6 | `InfoSource` | 信息来源 | varchar2(50) | ✓ | 100.0% |  |
| 7 | `AverageTermToMaturity` | 平均剩余期限(天) | number(9,2) | ✓ | 99.96% |  |
| 8 | `TermARateOfNetValue` | 剩余期限0-30天(不含)占资产净值比例 | number(9,6) | ✓ | 99.99% |  |
| 9 | `TermBRateOfNetValue` | 剩余期限30天(含)-60天占资产净值比例 | number(9,6) | ✓ | 92.84% |  |
| 10 | `TermCRateOfNetValue` | 剩余期限60天(含)-90天占资产净值比例 | number(9,6) | ✓ | 93.15% |  |
| 11 | `TermDRateOfNetValue` | 剩余期限90天(含)-180天占资产净值比例 | number(9,6) | ✓ | 20.75% |  |
| 12 | `TermERateOfNetValue` | 剩余期限180天(含)以上占资产净值比例 | number(9,6) | ✓ | 20.88% |  |
| 13 | `TermFRateOfNetValue` | 剩余期限90天(含)-120天占资产净值比例 | number(9,6) | ✓ | 64.79% |  |
| 14 | `TermGRateOfNetValue` | 剩余期限120天(含)-397天占资产净值比例 | number(9,6) | ✓ | 69.47% |  |
| 15 | `DebtARateOfNetValue` | 剩余期限0-30天(不含)负债占资产净值比例 | number(18,6) | ✓ | 72.39% |  |
| 16 | `DebtBRateOfNetValue` | 剩余期限30天(含)-60天负债占资产净值比例 | number(18,6) | ✓ | 4.8% |  |
| 17 | `DebtCRateOfNetValue` | 剩余期限60天(含)-90天负债占资产净值比例 | number(18,6) | ✓ | 4.75% |  |
| 18 | `DebtDRateOfNetValue` | 剩余期限90天(含)-180天负债占资产净值比例 | number(18,6) | ✓ | 2.58% |  |
| 19 | `DebtERateOfNetValue` | 剩余期限180天(含)以上负债占资产净值比例 | number(18,6) | ✓ | 2.61% |  |
| 20 | `DebtFRateOfNetValue` | 剩余期限90天(含)-120天负债占资产净值比例 | number(18,6) | ✓ | 1.89% |  |
| 21 | `DebtGRateOfNetValue` | 剩余期限120天(含)-397天负债占资产净值比例 | number(18,6) | ✓ | 2.07% |  |
| 22 | `FRNRefARateOfNetValue` | 剩余期限0-30天(不含)中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 9.37% |  |
| 23 | `FRNRefBRateOfNetValue` | 剩余期限30天(含)-60天中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 8.12% |  |
| 24 | `FRNRefCRateOfNetValue` | 剩余期限60天(含)-90天中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 9.67% |  |
| 25 | `FRNRefDRateOfNetValue` | 剩余期限90天(含)-180天中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 3.9% |  |
| 26 | `FRNRefERateOfNetValue` | 剩余期限180天(含)以上中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 0.71% |  |
| 27 | `FRNRefFRateOfNetValue` | 剩余期限90天(含)-120天中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 0.76% |  |
| 28 | `FRNRefGRateOfNetValue` | 剩余期限120天(含)-397天中剩余存续期超过397天的浮动利率债占资产净值比例 | number(18,6) | ✓ | 0.27% |  |
| 29 | `FRNRefDebtARateOfNetValue` | 剩余期限0-30天(不含)中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 1.06% |  |
| 30 | `FRNRefDebtBRateOfNetValue` | 剩余期限30天(含)-60天中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 1.22% |  |
| 31 | `FRNRefDebtCRateOfNetValue` | 剩余期限60天(含)-90天中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 1.65% |  |
| 32 | `FRNRefDebtDRateOfNetValue` | 剩余期限90天(含)-180天中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 1.17% |  |
| 33 | `FRNRefDebtERateOfNetValue` | 剩余期限180天(含)以上中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 0.45% |  |
| 34 | `FRNRefDebtFRateOfNetValue` | 剩余期限90天(含)-120天中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 0.12% |  |
| 35 | `FRNRefDebtGRateOfNetValue` | 剩余期限120天(含)-397天中剩余存续期超过397天的浮动利率债负债占资产净值比例 | number(18,6) | ✓ | 0.12% |  |
| 36 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 37 | `XGRQ` | 更新日期 | date | ✗ |  |  |
| 38 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金投资剩余期限分布 数据
SELECT *
FROM mf_fundbondportterm
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
