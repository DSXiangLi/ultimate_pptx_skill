# Bond_PreIsuueQuote

**中文名**: 债券预发行行情

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_PreIsuueQuote` |
| MySQL表名 | `bond_preisuuequote` |
| 中文名 | 债券预发行行情 |
| 路径 | 聚源新版数据库 > 债券数据库 > 债券估值及交易行情 |
| 更新频率 | 日更新 |
| 字段数量 | 13 |
| 版本 | 1 |

## 表描述

1.内容说明：本表记录国债预发行行情信息
2.数据范围：2013-10-10至今
3.信息来源：上交所

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `EndDate` | 日期 | date | ✗ | 100.0% |  |
| 3 | `PreInnerCode` | 预发行内部编码 | number(10) | ✗ | 100.0% | 预发行内部编码（PreInnerCode）：与“债券预发行(Bond_PreIsuue)”中的“预发行内部编码（PreI... |
| 4 | `PrevClosePrice` | 昨收盘 | number(10,6) | ✓ | 100.0% |  |
| 5 | `OpenPrice` | 今开盘 | number(10,6) | ✓ | 99.93% |  |
| 6 | `HighPrice` | 最高价 | number(10,6) | ✓ | 99.93% |  |
| 7 | `LowPrice` | 最低价 | number(10,6) | ✓ | 99.93% |  |
| 8 | `ClosePrice` | 收盘价 | number(10,6) | ✓ | 100.0% |  |
| 9 | `TurnoverVolume` | 成交量 | number(18,0) | ✓ | 47.61% |  |
| 10 | `TurnoverValue` | 成交金额 | number(19,4) | ✓ | 47.61% |  |
| 11 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 12 | `UpdateTime` | 修改时间 | date | ✗ |  |  |
| 13 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### PreInnerCode (预发行内部编码)

预发行内部编码（PreInnerCode）：与“债券预发行(Bond_PreIsuue)”中的“预发行内部编码（PreInnerCode）”关联，得到预发行的相关产品代码，简称

## SQL示例

```sql
-- 查询 债券预发行行情 数据
SELECT *
FROM bond_preisuuequote
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
