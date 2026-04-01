# Bond_SCHIndexQuote

**中文名**: 上清所指数行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_SCHIndexQuote` |
| MySQL表名 | `bond_schindexquote` |
| 中文名 | 上清所指数行情 |
| 路径 | 聚源新版数据库 > 指数数据库 > 指数行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 21 |
| 版本 | 1.04 |

## 表描述

1.收录了上清所发布的银行间信用债综合指数(SCH00100)、银行间高等级信用债指数(SCH00200)、银行间中高等级信用债指数(SCH00300)、银行间高收益信用债指数(SCH00400)、银行间区域(上海)信用债指数(SCH00500)、非公开定向债务融资工具综合指数(SCH00600)、信用债综合指数(SCH00700)七大主指数及相应的待偿期指数（包含总值(即主指数)、1年以下、1-3年、3-5年、5-7年）的三种类型（即总收益、全价、净价）的指数点值。
2.历史数据：2014年12月至今
3.数据源：上海清算所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `MainIndexCode` | 主指数内部编码 | number(10) | ✓ | 100.0% | 主指数内部编码(MainIndexCode)：与“指数基本情况表(LC_IndexBasicInfo)”中的“指数内部代... |
| 5 | `MaturityIndexCode` | 待偿期指数内码 | number(10) | ✓ | 100.0% | 待偿期指数内码(MaturityIndexCode)：与“指数基本情况表(LC_IndexBasicInfo)”中的“指... |
| 6 | `IndexType` | 指数类型 | number(10) | ✓ | 100.0% | 指数类型(IndexType)与(CT_SystemConst)表中的DM字段关联，令LB = 1991，得到指数类型的... |
| 7 | `BasisPoint` | 基数 | number(18,6) | ✓ | 100.0% |  |
| 8 | `DivisorFactor` | 最新除数 | number(18,6) | ✓ | 99.92% |  |
| 9 | `ClosePrice` | 指数点 | number(18,6) | ✓ | 100.0% |  |
| 10 | `ChangePCT` | 指数涨跌幅(%) | number(18,6) | ✓ | 99.94% |  |
| 11 | `PrevClosePrice` | 前日指数点 | number(18,6) | ✓ | 99.94% |  |
| 12 | `ComponentSum` | 指数样本数量 | number(18,6) | ✓ | 100.0% |  |
| 13 | `TotalMarketValue` | 指数总市值(亿元) | number(18,6) | ✓ | 100.0% |  |
| 14 | `ReinvestmentMV` | 再投资总市值(亿元) | number(18,6) | ✓ | 100.0% |  |
| 15 | `AvgYTM_Index` | 指数平均收益率(%) | number(18,6) | ✓ | 100.0% |  |
| 16 | `AvgModifiedDuration` | 指数平均修正久期 | number(18,6) | ✓ | 100.0% |  |
| 17 | `AvgConvexity` | 指数平均凸性 | number(18,6) | ✓ | 100.0% |  |
| 18 | `AvgBasisPointValue` | 指数平均基点价值 | number(18,6) | ✓ | 100.0% |  |
| 19 | `AvgYearsToMaturity` | 指数平均待偿期 | number(18,6) | ✓ | 8.45% |  |
| 20 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 21 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到指数的代码、简称等。

### MainIndexCode (主指数内部编码)

主指数内部编码(MainIndexCode)：与“指数基本情况表(LC_IndexBasicInfo)”中的“指数内部代码(IndexCode)”关联，得到所属指数的基日、基点、发布机构等。

### MaturityIndexCode (待偿期指数内码)

待偿期指数内码(MaturityIndexCode)：与“指数基本情况表(LC_IndexBasicInfo)”中的“指数内部代码(IndexCode)”关联，得到所属指数的基日、基点、发布机构等。

### IndexType (指数类型)

指数类型(IndexType)与(CT_SystemConst)表中的DM字段关联，令LB = 1991，得到指数类型的具体描述：1-净价指数，2-全价指数，3-总收益指数。

## SQL示例

```sql
-- 查询 上清所指数行情 数据
SELECT *
FROM bond_schindexquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
