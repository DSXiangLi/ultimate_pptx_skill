# MF_MoneySpecialIndex

**中文名**: 公募基金货币型基金专项指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `MF_MoneySpecialIndex` |
| MySQL表名 | `mf_moneyspecialindex` |
| 中文名 | 公募基金货币型基金专项指标 |
| 路径 | 聚源新版数据库 > 公募基金数据库 > 公募基金投资组合 |
| 更新频率 | 季更新 |
| 字段数量 | 24 |
| 版本 | 1.01 |

## 表描述

1.本表记录包括货币基金的季报数据，年报数据及半年报数据的债券回购融资情况，平均剩余期限入资产净值的偏离值。
2.历史数据：2004年3月起-至今。
3.数据来源：基金公司披露的定期报告。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 基金内部编码 | number(10) | ✗ | 100.0% | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TransCode` | 基金转型统一编码 | number(10) | ✓ | 100.0% |  |
| 4 | `InfoPublDate` | 信息发布日期 | date | ✓ | 100.0% |  |
| 5 | `BeginDate` | 起始日期 | date | ✗ | 100.0% |  |
| 6 | `EndDate` | 截止日期 | date | ✗ | 100.0% |  |
| 7 | `DRPBondRepurFin` | 报告期内债券回购融资余额 | number(19,4) | ✓ | 3.78% |  |
| 8 | `DRPBalaRepurFin` | 其中:报告期内买断式回购融入的资金 | number(19,4) | ✓ | 0.66% |  |
| 9 | `BondRepurFin` | 报告期末债券回购融资余额 | number(19,4) | ✓ | 65.98% |  |
| 10 | `BalaRepurFin` | 其中:报告期末买断式回购融入的资金 | number(19,4) | ✓ | 1.35% |  |
| 11 | `DRPBondRepurFinPCT` | 报告期内债券回购融资余额占基金资产净值比例 | number(18,6) | ✓ | 93.13% |  |
| 12 | `DRPBalaRepurFinPCT` | 其中:报告期内买断式回购融入的资金占基金资产净值比例 | number(18,6) | ✓ | 7.13% |  |
| 13 | `BondRepurFinPCT` | 报告期末债券回购融资余额占基金资产净值比例 | number(18,6) | ✓ | 66.5% |  |
| 14 | `BalaRepurFinPCT` | 其中:报告期末买断式回购融入的资金占基金资产净值比例 | number(18,6) | ✓ | 2.89% |  |
| 15 | `FPAverRemPer` | 报告期末投资组合平均剩余期限 | number(10) | ✓ | 99.48% |  |
| 16 | `MaxFPAverRemPer` | 报告期末投资组合平均剩余期限最高值 | number(10) | ✓ | 99.48% |  |
| 17 | `MinFPAverRemPer` | 报告期末投资组合平均剩余期限最低值 | number(10) | ✓ | 99.43% |  |
| 18 | `AbsDeviCount` | 报告期内偏离度的绝对值在0.25%(含)-0.5%的次数 | number(10) | ✓ | 76.74% |  |
| 19 | `MaxDevi` | 报告期内偏离度的最高值(%) | number(18,6) | ✓ | 98.09% |  |
| 20 | `MinDevi` | 报告期内偏离度的最低值(%) | number(18,6) | ✓ | 98.04% |  |
| 21 | `AvgAbsDevi` | 报告期内每个交易日偏离度的绝对值的简单平均值(%) | number(18,6) | ✓ | 98.08% |  |
| 22 | `InsertTime` | 插入时间 | date | ✓ |  |  |
| 23 | `UpdateTime` | 更新日期 | date | ✗ |  |  |
| 24 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (基金内部编码)

基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。当基金交易代码非主代码时，与“公募基金代码关联(新)（MF_CodeRelationshipNew）”中的“关联代码内部编码（RelatedInnerCode）”关联，令CodeDefine=21，得到基金主代码“内部编码（InnerCode）”，利用主代码进行查询。

## SQL示例

```sql
-- 查询 公募基金货币型基金专项指标 数据
SELECT *
FROM mf_moneyspecialindex
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
