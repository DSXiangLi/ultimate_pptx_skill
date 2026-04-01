# Bond_ActiveBondQuote

**中文名**: 债券活跃券行情表

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `Bond_ActiveBondQuote` |
| MySQL表名 | `bond_activebondquote` |
| 中文名 | 债券活跃券行情表 |
| 路径 | 聚源新版数据库 > 债券数据库 > 利率债研究专题 |
| 更新频率 | 日更新 |
| 字段数量 | 16 |
| 版本 | 1 |

## 表描述

收录国债和国开债活跃券的行情，包括开盘价、最高价、最低价和收盘价及成交量等

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `TradingDay` | 交易日 | date | ✗ | 100.0% |  |
| 3 | `InnerCode` | 内部编码 | number(10) | ✗ | 100.0% | 内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联... |
| 4 | `SecuCode` | 债券代码 | varchar2(10) | ✓ | 100.0% |  |
| 5 | `SecuAbbr` | 债券简称 | varchar2(100) | ✓ | 100.0% |  |
| 6 | `YrMat` | 剩余期限 | number(18,8) | ✓ | 100.0% |  |
| 7 | `YTM_OP` | 开盘价到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 8 | `YTM_HI` | 最高价到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 9 | `YTM_LO` | 最低价到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 10 | `YTM_CL` | 收盘价到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 11 | `YTM_WAP` | 加权价到期收益率(%) | number(19,8) | ✓ | 100.0% |  |
| 12 | `TurnoverVolume` | 成交量(张) | number(19,4) | ✓ | 99.99% |  |
| 13 | `ActiveType` | 活跃券类别 | number(10) | ✓ | 100.0% | 活跃券类别（ActiveType）：1-10年期国开债活跃券，2-10年期国债活跃券 |
| 14 | `InsertTime` | 发布时间 | date | ✗ |  |  |
| 15 | `UpdateTime` | 更新时间 | date | ✗ |  |  |
| 16 | `JSID` | JSID | number(19) | ✗ |  |  |

## 字段说明

### InnerCode (内部编码)

内部代码（InnerCode）：与“债券代码对照表（Bond_Code）”中的“债券内部编码（InnerCode）”关联，得到债券的交易代码、债券简称等。

### ActiveType (活跃券类别)

活跃券类别（ActiveType）：1-10年期国开债活跃券，2-10年期国债活跃券

## SQL示例

```sql
-- 查询 债券活跃券行情表 数据
SELECT *
FROM bond_activebondquote
WHERE TradingDay >= '2024-01-01'
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
