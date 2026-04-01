# LC_SpecialTrade

**中文名**: 证券特别处理

## 基本信息

| 属性 | 值 |
|------|-----|
| 表名 | `LC_SpecialTrade` |
| MySQL表名 | `lc_specialtrade` |
| 中文名 | 证券特别处理 |
| 路径 | 聚源新版数据库 > 国内上市公司数据库 > 上市公司基本资料 |
| 更新频率 | 不定时更新 |
| 字段数量 | 11 |
| 版本 | 1.01 |

## 表描述

收录证券（含股票，债券）被特别处理(或撤销)的相关信息,包括ST、PT、*ST、撤销ST、撤销PT、撤销*ST等。

## 字段列表

| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |
|------|--------|--------|------|------|--------|------|
| 1 | `ID` | ID | number(19) | ✗ |  |  |
| 2 | `InnerCode` | 证券内部编码 | number(10) | ✗ | 100.0% | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证... |
| 3 | `InfoPublDate` | 信息发布日期 | date | ✗ | 100.0% |  |
| 4 | `SecurityAbbr` | 证券简称 | varchar2(100) | ✓ | 100.0% |  |
| 5 | `SpecialTradeType` | 特别处理(或撤销)类别 | number(10) | ✗ | 100.0% | 特别处理(或撤销)类别(SpecialTradeType)与(CT_SystemConst)表中的DM字段关联，令LB ... |
| 6 | `SpecialTradeTime` | 特别处理(或撤销)实施日期 | date | ✓ | 100.0% |  |
| 7 | `SpecialTradeExplain` | 特别处理(或撤销)事项描述 | varchar2(400) | ✓ | 99.08% |  |
| 8 | `InsertTime` | 发布时间 | date | ✓ |  |  |
| 9 | `XGRQ` | 更新时间 | date | ✗ |  |  |
| 10 | `JSID` | JSID | number(19) | ✗ |  |  |
| 11 | `SpecialTradeReason` | 特别处理原因 | varchar2(255) | ✓ | 0.0% |  |

## 字段说明

### InnerCode (证券内部编码)

内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。

### SpecialTradeType (特别处理(或撤销)类别)

特别处理(或撤销)类别(SpecialTradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1185，得到特别处理(或撤销)类别的具体描述：1-ST，2-撤销ST，3-PT，4-撤销PT，5-*ST，6-撤销*ST，7-撤消*ST并实行ST，8-从ST变为*ST，9-退市整理期，10-高风险警示，11-撤销高风险警示，12-叠加ST，13-撤销叠加ST，14-叠加*ST，15-撤销叠加*ST。

## SQL示例

```sql
-- 查询 证券特别处理 数据
SELECT *
FROM lc_specialtrade
  AND InnerCode = 12345  -- 替换为实际的InnerCode
LIMIT 10;
```

---

*文档生成时间: 2026-03-03 15:15:54*
