# Bond_AdvancedDeriv

**中文名**: 债券进阶衍生指标

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_AdvancedDeriv` |
| MySQL表名 | `bond_advancedderiv` |
| 中文名 | 债券进阶衍生指标 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 30 |
| 版本 | 1 |

## 表描述

1.收录（除ABS）外所有债券基于债券行情计算的关键年期久期、Z利差、G利差等进阶衍生指标，包括行权与到期两种期限类型。
2.数据范围：1990-12-19至今
3.信息来源：衍生计算

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `SecuMarket` | 证券市场 | number(10) | ✗ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM ... |
| 5 | `MaturityType` | 期限类型 | number(10) | ✗ | 100.0% | 期限类型（MaturityType），该字段固定为以下常量：1-到期；2-行权 |
| 6 | `PriceType` | 价格类型 | number(10) | ✗ | 100.0% | 价格类型（PriceType），该字段固定为以下常量：1-收盘全价 |
| 7 | `OpType` | 行权类型 | number(10) | ✓ | 13.69% | 行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN ... |
| 8 | `ExpectedExerciseDate` | 最近可能行权日 | date | ✓ | 13.69% |  |
| 9 | `KRD_OneMonth` | 1月久期 | number(18,10) | ✓ | 100.0% |  |
| 10 | `KRD_ThreeMonth` | 3月久期 | number(18,10) | ✓ | 100.0% |  |
| 11 | `KRD_SixMonth` | 6月久期 | number(18,10) | ✓ | 100.0% |  |
| 12 | `KRD_OneYear` | 1年久期 | number(18,10) | ✓ | 100.0% |  |
| 13 | `KRD_TwoYear` | 2年久期 | number(18,10) | ✓ | 100.0% |  |
| 14 | `KRD_ThreeYear` | 3年久期 | number(18,10) | ✓ | 100.0% |  |
| 15 | `KRD_FourYear` | 4年久期 | number(18,10) | ✓ | 100.0% |  |
| 16 | `KRD_FiveYear` | 5年久期 | number(18,10) | ✓ | 100.0% |  |
| 17 | `KRD_SevenYear` | 7年久期 | number(18,10) | ✓ | 100.0% |  |
| 18 | `KRD_NineYear` | 9年久期 | number(18,10) | ✓ | 100.0% |  |
| 19 | `KRD_TenYear` | 10年久期 | number(18,10) | ✓ | 100.0% |  |
| 20 | `KRD_FifteenYear` | 15年久期 | number(18,10) | ✓ | 100.0% |  |
| 21 | `KRD_TwentyYear` | 20年久期 | number(18,10) | ✓ | 100.0% |  |
| 22 | `KRD_ThirtyYear` | 30年久期 | number(18,10) | ✓ | 100.0% |  |
| 23 | `KRD_FiftyYear` | 50年久期 | number(18,10) | ✓ | 100.0% |  |
| 24 | `KRD_ShortTerm` | 短边久期 | number(18,10) | ✓ | 100.0% |  |
| 25 | `KRD_LongTerm` | 长边久期 | number(18,10) | ✓ | 100.0% |  |
| 26 | `Z_Spread` | Z利差 | number(18,10) | ✓ | 99.25% |  |
| 27 | `G_Spread` | G利差 | number(18,10) | ✓ | 99.34% |  |
| 28 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 29 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 30 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN(83,89,90) OR LB = 1006 AND DM IN(12,18,21) ，得到证券市场的具体描述：12-上交所固定收益平台，18-深交所综合收益平台，21-上交所大宗交易，83-上海证券交易所，89-银行间债券市场，90-深圳证券交易所。

### MaturityType (期限类型)

期限类型（MaturityType），该字段固定为以下常量：1-到期；2-行权

### PriceType (价格类型)

价格类型（PriceType），该字段固定为以下常量：1-收盘全价

### OpType (行权类型)

行权类型(OpType)与(CT_SystemConst)表中的DM字段关联，令LB = 1440 AND DM IN (101,201,203)，得到行权类型的具体描述：101-发行人赎回权，201-持有人回售权，203-持有人定向转让权。

## SQL示例

```sql
-- 查询 债券进阶衍生指标 数据
SELECT *
FROM bond_advancedderiv
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
