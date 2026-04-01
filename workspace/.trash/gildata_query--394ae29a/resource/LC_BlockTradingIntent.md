# LC_BlockTradingIntent

**中文名**: 大宗交易意向申报

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_BlockTradingIntent` |
| MySQL表名 | `lc_blocktradingintent` |
| 中文名 | 大宗交易意向申报 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司股票行情 |
| 更新频率 | 不定时更新 |
| 字段数量 | 10 |
| 版本 | 1 |

## 表描述

1.收录交易所公布的大宗交易意向申报数据，包括买卖方向、价格、数量等。
2.数据范围：2005-06-27至今
3.信息来源：上海证券交易所、深圳证券交易所、北京证券交易所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `TradingDay` | 申报日期 | date | ✗ | 100.0% |  |
| 4 | `BSDirection` | 买卖方向 | varchar2(20) | ✓ | 100.0% |  |
| 5 | `BSDirectionCode` | 买卖方向代码 | number(10) | ✗ | 100.0% | 买卖方向代码(BSDirectionCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1031... |
| 6 | `BSPrice` | 价格(元) | number(19,8) | ✓ | 100.0% |  |
| 7 | `BSVolume` | 数量(股/份/张) | number(19,2) | ✓ | 100.0% |  |
| 8 | `Remark` | 备注 | varchar2(500) | ✓ | 96.56% |  |
| 9 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### BSDirectionCode (买卖方向代码)

买卖方向代码(BSDirectionCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1031 AND DM IN(301,302)，得到买卖方向代码的具体描述：301-买入，302-卖出。

## SQL示例

```sql
-- 查询 大宗交易意向申报 数据
SELECT *
FROM lc_blocktradingintent
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
