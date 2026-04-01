# Bond_PreIsuue

**中文名**: 债券预发行

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_PreIsuue` |
| MySQL表名 | `bond_preisuue` |
| 中文名 | 债券预发行 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券基本资料 |
| 更新频率 | 不定期更新 |
| 字段数量 | 18 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录债券预发行相关信息，主要包括国债
2.数据范围：2013-10-8至今
3.信息来源：上交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 涉及债券内部编码 | number(10) | ✗ | 100.0% | 涉及债券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode... |
| 3 | `PreInnerCode` | 预发行内部编码 | number(10) | ✓ | 100.0% | 预发行内部编码（PreInnerCode）：与“债券预发行行情(Bond_PreIsuueQuote)”中的“预发行内部... |
| 4 | `PreCode` | 预发行代码 | varchar2(20) | ✓ | 100.0% |  |
| 5 | `PreAbbr` | 预发行简称 | varchar2(50) | ✓ | 100.0% |  |
| 6 | `SecuMarket` | 证券市场 | number(10) | ✓ | 100.0% | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM ... |
| 7 | `InitialInfoPublDate` | 预发行公告发布日期 | date | ✓ | 100.0% |  |
| 8 | `BidDate` | 预发行交割/招标日 | date | ✗ | 100.0% |  |
| 9 | `TradingStartDate` | 交易起始日 | date | ✓ | 100.0% |  |
| 10 | `TradingEndDate` | 交易截止日 | date | ✓ | 100.0% |  |
| 11 | `Maturity` | 债券期限(年) | number(10) | ✓ | 100.0% |  |
| 12 | `BenchmarkYield` | 基准收益率(%) | number(10,6) | ✓ | 28.61% |  |
| 13 | `BenchmarkPrice` | 基准价格(元) | number(19,4) | ✓ | 63.14% |  |
| 14 | `ReferenceDuration` | 参考久期(年) | number(9,6) | ✓ | 91.75% |  |
| 15 | `ListedState` | 上市状态 | number(10) | ✓ | 100.0% | 上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176，得到上市状... |
| 16 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 17 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 18 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (涉及债券内部编码)

涉及债券内部编码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到涉及债券的交易代码、债券简称等

### PreInnerCode (预发行内部编码)

预发行内部编码（PreInnerCode）：与“债券预发行行情(Bond_PreIsuueQuote)”中的“预发行内部编码（PreInnerCode）”关联，得到预发行的相关行情

### SecuMarket (证券市场)

证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB = 201 and DM in (71,83,89,90)，得到证券市场的具体描述：71-柜台交易市场，83-上海证券交易所，89-银行间债券市场，90-深圳证券交易所。

### ListedState (上市状态)

上市状态(ListedState)与(CT_SystemConst)表中的DM字段关联，令LB = 1176，得到上市状态的具体描述：1-上市，2-预上市，3-暂停，4-上市失败，5-终止，9-其他，10-交易，11-停牌，12-摘牌。

## SQL示例

```sql
-- 查询 债券预发行 数据
SELECT *
FROM bond_preisuue
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
