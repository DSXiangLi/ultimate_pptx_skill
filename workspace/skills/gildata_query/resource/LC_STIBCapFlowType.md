# LC_STIBCapFlowType

**中文名**: 科创板交易资金分类流向

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_STIBCapFlowType` |
| MySQL表名 | `lc_stibcapflowtype` |
| 中文名 | 科创板交易资金分类流向 |
| 路径 | 聚源新版数据库 > 科创板数据库 > 行情交易 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

1.内容说明：展示每个交易日科创板股票在不同单笔成交金额区间的累计主买、主卖金额及成交量情况。
本表仅包括二级市场科创板股票交易所产生的资金流向数据，不含大宗交易产生的资金流向；大宗交易资金流向数据可参考“股东股权变动（ LC_ShareTransfer）”表(TranMode='11')。
2.数据范围：科创板证券上市之日起至今
3.信息来源：恒生电子

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部代码 | number(10) | ✗ | 100.0% | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得... |
| 3 | `TradingDay` | 交易日期 | date | ✗ | 100.0% |  |
| 4 | `DividingStandard` | 划分标准 | number(10) | ✗ | 100.0% | 划分标准(DividingStandard)，该字段固定以下常量：1-Level1行情 |
| 5 | `ValueRange` | 单笔成交金额区间 | number(10) | ✗ | 100.0% | 单笔成交金额区间(ValueRange)： 该字段固定以下常量：1：小单-[0，4w)2：中单-[4w，20w)3：大单... |
| 6 | `BuyValue` | 流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 7 | `SellValue` | 流出额(元) | number(19,4) | ✓ | 100.0% |  |
| 8 | `BuyVolume` | 流入量(股) | number(16,0) | ✓ | 100.0% |  |
| 9 | `SellVolume` | 流出量(股) | number(16,0) | ✓ | 100.0% |  |
| 10 | `NetBuyValue` | 净流入额(元) | number(19,4) | ✓ | 100.0% |  |
| 11 | `NetBuyVolume` | 净流入量(股) | number(16,0) | ✓ | 100.0% |  |
| 12 | `BuyNum` | 流入单数(笔) | number(10) | ✓ | 97.24% |  |
| 13 | `SellNum` | 流出单数(笔) | number(10) | ✓ | 96.62% |  |
| 14 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 15 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (证券内部代码)

证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### DividingStandard (划分标准)

划分标准(DividingStandard)，该字段固定以下常量：1-Level1行情

### ValueRange (单笔成交金额区间)

单笔成交金额区间(ValueRange)： 该字段固定以下常量：1：小单-[0，4w)2：中单-[4w，20w)3：大单-[20w，100w)4：超大单-[100w，+∞)。

## SQL示例

```sql
-- 查询 科创板交易资金分类流向 数据
SELECT *
FROM lc_stibcapflowtype
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
